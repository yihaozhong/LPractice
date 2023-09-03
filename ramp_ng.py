
def level1(queries):
    database = {}
    results = []

    for query in queries:
        operation = query[0]
        timestamp = query[1]
        key = query[2]
        field = query[3]
        
        if operation == "SET":
            value = query[4]
            if key not in database:
                database[key] = {}
            database[key][field] = value
            results.append("")

        elif operation == "GET":
            if key in database and field in database[key]:
                results.append(database[key][field])
            else:
                results.append("")

        elif operation == "COMPARE_AND_SET":
            expected_value = query[4]
            new_value = query[5]
            if key in database and field in database[key] and database[key][field] == expected_value:
                database[key][field] = new_value
                results.append(True)
            else:
                results.append(False)

        elif operation == "COMPARE_AND_DELETE":
            expected_value = query[4]
            if key in database and field in database[key] and database[key][field] == expected_value:
                del database[key][field]
                results.append(True)
            else:
                results.append(False)

    return results

# Testing the function with some sample queries
queries = [
    ("SET", 1630673400000, "user1", "age", 25),
    ("GET", 1630673400100, "user1", "age"),
    ("SET", 1630673400100, "user2", "height", 180),
    ("COMPARE_AND_SET", 1630673400200, "user1", "age", 25, 26),
    ("GET", 1630673400100, "user1", "age"),
    ("COMPARE_AND_DELETE", 1630673400300, "user2", "height", 180),
    ("GET", 1630673400400, "user2", "height")
]

print(level1(queries))