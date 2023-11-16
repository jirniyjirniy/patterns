class Account:
    def __init__(self, account_number: str, balance: int):
        self.account_number = account_number
        self.balance = balance


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __iter__(self):
        return BankIterator(self)


class BankIterator:
    def __init__(self, bank):
        self.bank = bank
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.bank.accounts):
            raise StopIteration
        else:
            account = self.bank.accounts[self.current_index]
            self.current_index += 1
            return account


if __name__ == '__main__':
    bank = Bank()
    bank.add_account(Account("12345", 1000))
    bank.add_account(Account("67890", 2000))
    bank.add_account(Account("13579", 3000))

    for account in bank:
        print(f"Account Number: {account.account_number}, Balance: {account.balance}$")
