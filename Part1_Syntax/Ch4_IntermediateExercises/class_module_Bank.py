import random

class PrivateBank:

    def __init__(self, bank, account_name):
        self.bank = bank
        self.account_name = account_name

        while True:
            newAccountNo = random.randint(10000, 99999)
            if bank.isAccount(newAccountNo):
                continue
            else:
                self.account_no = newAccountNo
                break

        self.totalMoney = 0
        bank.addAccount(self)

    def printBankInfo(self):
        print('-' * 40)
        print(f'account_name: {self.account_name}')
        print(f'account_no: {self.account_no}')
        print(f'totalMoney: {self.totalMoney}원')
        print('-' * 40)


class Bank:

    def __init__(self):
        self.accounts = {}

    def addAccount(self, privateBank):
        self.accounts[privateBank.account_no] = privateBank

    def isAccount(self, ano):
        return ano in self.accounts

    def doDeposit(self, ano, m):
        pb = self.accounts[ano]
        pb.totalMoney = pb.totalMoney + m

    def doWithdraw(self, ano, m):
        pb = self.accounts[ano]
        if pb.totalMoney - m < 0:
            raise LackException(pb.totalMoney, m)
        pb.totalMoney = pb.totalMoney - m


class LackException(Exception):
    def __init__(self, m1, m2):
        super().__init__(f'잔고부족!!, 잔액: {m1}, 출금액: {m2}')

