
def level1(queries):
    database = {}
    ttl_dict = {}  # A dictionary to store the TTL for each key-field pair
    results = []

    # Helper function to check and remove expired entries based on TTL
    def check_and_remove_expired(timestamp):
        expired_entries = []
        for (key, field), expiry_time in ttl_dict.items():
            if timestamp >= expiry_time:
                expired_entries.append((key, field))
        
        for key, field in expired_entries:
            if key in database and field in database[key]:
                del database[key][field]
            del ttl_dict[(key, field)]

    for query in queries:
        operation = query[0]
        timestamp = int(query[1])  # Convert the timestamp to integer
        
        # Check and remove expired entries before each operation
        check_and_remove_expired(timestamp)

        key = query[2]
        
        if operation == "SET":
            field = query[3]
            value = query[4]
            if key not in database:
                database[key] = {}
            database[key][field] = value
            results.append("")

        elif operation == "GET":
            field = query[3]
            if key in database and field in database[key]:
                results.append(database[key][field])
            else:
                results.append("")

        elif operation == "COMPARE_AND_SET":
            field = query[3]
            expected_value = query[4]
            new_value = query[5]
            if key in database and field in database[key] and database[key][field] == expected_value:
                database[key][field] = new_value
                results.append("True")
            else:
                results.append("False")

        elif operation == "COMPARE_AND_DELETE":
            field = query[3]
            expected_value = query[4]
            if key in database and field in database[key] and database[key][field] == expected_value:
                del database[key][field]
                results.append("True")
            else:
                results.append("False")

        elif operation == "SCAN":
            if key in database:
                fields_values = sorted(database[key].items(), key=lambda x: x[0])  # Sorting by field
                results.append(", ".join([f"{field}({value})" for field, value in fields_values]))
            else:
                results.append("")

        elif operation == "SCAN_BY_PREFIX":
            prefix = query[3]
            if key in database:
                fields_values = sorted(database[key].items(), key=lambda x: x[0])  # Sorting by field
                results.append(", ".join([f"{field}({value})" for field, value in fields_values if field.startswith(prefix)]))
            else:
                results.append("")

        elif operation == "SET_WITH_TTL":
            field = query[3]
            value = query[4]
            ttl = int(query[5])  # Convert the TTL to integer
            if key not in database:
                database[key] = {}
            database[key][field] = value
            ttl_dict[(key, field)] = timestamp + ttl
            results.append("")

        elif operation == "COMPARE_AND_SET_WITH_TTL":
            field = query[3]
            expected_value = query[4]
            new_value = query[5]
            ttl = int(query[6])  # Convert the TTL to integer
            if key in database and field in database[key] and database[key][field] == expected_value:
                database[key][field] = new_value
                ttl_dict[(key, field)] = timestamp + ttl
                results.append("True")
            else:
                results.append("False")

    return results


queries = [
    ["SET_WITH_TTL", "160000000", "foo", "bar", "150", "50"],
    ["GET", "160000020", "foo", "bar"],
    ["GET", "160000030", "foo", "bar"],
    ["GET", "160000050", "foo", "bar"],
    ["GET", "160000080", "foo", "bar"]
]

# Running the queries through level1 function again
results = level1(queries)
print(results)
# Testing the function with some sample queries
queries = [["SET_WITH_TTL","160000000","a","a","200","40"], 
 ["SET_WITH_TTL","160000010","a","d","100","60"], 
 ["SCAN","160000020","a"], 
 ["COMPARE_AND_SET","160000030","a","a","100","200"], 
 ["COMPARE_AND_SET_WITH_TTL","160000050","a","d","100","30","20"], 
 ["SET_WITH_TTL","160000060","a","d","20","2"], 
 ["COMPARE_AND_SET_WITH_TTL","160000065","a","d","20","50","5"], 
 ["SCAN_BY_PREFIX","160000068","a","a"], 
 ["SCAN","160000070","a"], 
 ["GET","160000072","a","d"], 
 ["SET","160000100","d","d","3"], 
 ["SCAN","160000170","d"], 
 ["COMPARE_AND_SET_WITH_TTL","160000200","d","d","3","30","10"], 
 ["SCAN","160000220","d"], 
 ["SET_WITH_TTL","160000300","d","d","100","30"], 
 ["COMPARE_AND_DELETE","160000310","d","d","100"], 
 ["SET","160000311","d","d","500"], 
 ["SCAN","160000400","a"], 
 ["SCAN","800000000","d"]]

print(level1(queries))
