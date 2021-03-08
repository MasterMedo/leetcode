class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        invalid = set()
        ts = []
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            ts.append((i, name, int(time), int(amount), city))
            if int(amount) > 1000:
                invalid.add(i)

        for i, name, time, amount, city in ts:
            for j, name_, time_, amount_, city_ in ts:
                if name == name_ and city != city_ and time >= time_ and time <= time_ + 60:
                    invalid.add(i)
                    invalid.add(j)

        return [transactions[i] for i in invalid]
