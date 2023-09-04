
def solution(queries):
    account = {}
    account_trans = {}
    scheduled_transfer = {}
    transfer_count = 0

    def helper(timestamp):
        for transfer_id, transfer_data in list(scheduled_transfer.items()):
            if int(timestamp) > transfer_data["expiration"] and transfer_data["status"] == "pending":
                account[transfer_data["src"]] += transfer_data["amount"]
                transfer_data["status"] = "expired"
                del scheduled_transfer[transfer_id]

    def create_acc(timestamp, account_id):

        if account_id in account:
            return 'false'
        else:
            account[account_id] = 0
            account_trans[account_id] = 0
            return 'true'

    def deposit(timestamp, account_id, amount):
        helper(timestamp)
        if account_id not in account:
            return ''

        account[account_id] += amount
        account_trans[account_id] += amount

        return str(account[account_id])

    def pay(timestamp, account_id, amount):
        helper(timestamp)
        if account_id not in account or account[account_id] < amount:
            return ''
        account[account_id] -= amount
        account_trans[account_id] += amount
        return str(account[account_id])

    def top_activity(timestamp, n):
        helper(timestamp)
        sorted_acc = sorted(account_trans.items(), key=lambda x: (-x[1], x[0]))
        top = sorted_acc[:n]
        return ", ".join(["{}({})".format(acc[0], acc[1]) for acc in top])

    def transfer(timestamp, src, tgt, amount):
        helper(timestamp)
        print(account)
        nonlocal transfer_count

        if src == tgt or src not in account or tgt not in account:
            return ""
        if account[src] < amount:
            return ""

        transfer_count += 1
        transfer_id = "transfer{}".format(transfer_count)
        # print(timestamp + 86400000)
        scheduled_transfer[transfer_id] = {
            "src": src,
            "tgt": tgt,
            "amount": amount,
            "expiration": timestamp + 86400000,
            "status": "pending"
        }
        account[src] -= amount
        return transfer_id

    def accept_transfer(timestamp, account_id, transfer_id):
        helper(timestamp)
        if transfer_id not in scheduled_transfer:
            print(1)

            return "false"
        transfer_D = scheduled_transfer[transfer_id]
        if transfer_D["status"] == "accepted" or timestamp > transfer_D["expiration"]:
            print(2)

            return "false"
        if transfer_D["tgt"] != account_id:
            print(3)

            return "false"
        print(account)
        account[account_id] += int(transfer_D["amount"])
        account_trans[account_id] += transfer_D["amount"]
        account_trans[transfer_D["src"]] += transfer_D["amount"]
        transfer_D["status"] = "accepted"
        print(account)
        return "true"

    def merge_accounts(timestamp, account_id1, account_id2):
        if account_id1 == account_id2 or account_id1 not in account or account_id2 not in account:
            return "false"

        account[account_id1] += account[account_id2]
        account_trans[account_id1] += account_trans[account_id2]

        # Cancel outgoing transfers from account_id2
        for transfer_id, transfer_data in list(scheduled_transfer.items()):
            if transfer_data["src"] == account_id2:
                transfer_data["src"] = account_id1
            if transfer_data["tgt"] == account_id2:
                transfer_data["tgt"] = account_id1

        del account[account_id2]
        del account_trans[account_id2]
        return "true"

    def get_balance_at_timestamp(timestamp, account_id, time_at):
        if account_id not in account:
            return ''
        return str(account[account_id])

    result = []
    for q in queries:
        ops = q[0]
        if ops == "CREATE_ACCOUNT":
            result.append(create_acc(q[1], q[2]))
        elif ops == "DEPOSIT":
            result.append(deposit(q[1], q[2], int(q[3])))
        elif ops == "PAY":
            result.append(pay(q[1], q[2], int(q[3])))
        elif ops == "TOP_ACTIVITY":
            result.append(top_activity(q[1], int(q[2])))
        elif ops == "TRANSFER":
            result.append(transfer(int(q[1]), q[2], q[3], int(q[4])))
        elif ops == "ACCEPT_TRANSFER":
            result.append(accept_transfer(int(q[1]), q[2], q[3]))
        elif ops == "MERGE_ACCOUNTS":
            result.append(merge_accounts(q[1], q[2], q[3]))
        elif ops == "GET_BALANCE":
            result.append(get_balance_at_timestamp(int(q[1]), q[2], int(q[3])))

    return result
