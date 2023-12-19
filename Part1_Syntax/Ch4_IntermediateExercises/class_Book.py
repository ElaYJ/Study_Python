class Book:

    def __init__(self, name, price, isbn):
        self.bName = name
        self.bPrice = price
        self.bIsbn = isbn


class BookRepository:

    def __init__(self):
        self.bDic = {}  # {isbn:classBookObj}

    def registBook(self, b):
        self.bDic[b.bIsbn] = b

    def removeBook(self, isbn):
        del self.bDic[isbn]

    def printBooksInfo(self):
        for isbn in self.bDic.keys():
            b = self.bDic[isbn]
            print(f'{b.bName}, {b.bPrice}, {b.bIsbn}')

    def printBookInfo(self, isbn):
        if isbn in self.bDic:
            b = self.bDic[isbn]
            print(f'{b.bName}, {b.bPrice}, {b.bIsbn}')
        else:
            print('Lookup result does not exist')


if __name__ == '__main__':
    br = BookRepository()

    br.registBook(Book('python', 20000, '1234567890'))
    br.registBook(Book('java', 25000, '852147963'))
    br.registBook(Book('c/c++', 27000, '951378624'))
    br.registBook(Book('javascript', 15000, '9874563254'))

    br.printBooksInfo()
    br.printBookInfo('1234567890')
    br.removeBook('1234567890')
    br.printBooksInfo()