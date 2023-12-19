from abc import ABCMeta
from abc import abstractmethod

# 추상 클래스는 사전 클래스가 반드시 가져야 하는 기능에 강제성을 부여
class AbsDictionary(metaclass=ABCMeta):

    def __init__(self):
        self.wordDic = {}

    @abstractmethod
    def registWord(self, w1, w2): # 단어, 번역단어
        pass

    @abstractmethod
    def removeWord(self, w1):
        pass

    @abstractmethod
    def updateWord(self, w1, w2):
        pass

    @abstractmethod
    def searchWord(self, w1):
        pass


class KorToEng(AbsDictionary):

    def __init__(self):
        super().__init__()

    def registWord(self, w1, w2):
        print(f'[KorToEng] registWord() : {w1} to {w2}')
        self.wordDic[w1] = w2

    def removeWord(self, w1):
        print(f'[KorToEng] removeWord() : {w1}')
        del self.wordDic[w1]

    def updateWord(self, w1, w2):
        print(f'[KorToEng] updateWord() : {w1} to {w2}')
        self.wordDic[w1] = w2

    def searchWord(self, w1):
        print(f'[KorToEng] searchWord() : {w1}')
        return self.wordDic[w1]

    def printWords(self):
        for k in self.wordDic:
            print(f'{k} : {self.wordDic[k]}')


class KorToJpa(AbsDictionary):

    def __init__(self):
        super().__init__()

    def registWord(self, w1, w2):
        print(f'[KorToJpa] registWord() : {w1} to {w2}')
        self.wordDic[w1] = w2

    def removeWord(self, w1):
        print(f'[KorToJpa] removeWord() : {w1}')
        del self.wordDic[w1]

    def updateWord(self, w1, w2):
        print(f'[KorToJpa] updateWord() : {w1} to {w2}')
        self.wordDic[w1] = w2

    def searchWord(self, w1):
        print(f'[KorToJpa] searchWord() : {w1}')
        return self.wordDic[w1]

    def printWords(self):
        for k in self.wordDic:
            print(f'{k} : {self.wordDic[k]}')


if __name__ == '__main__':
    kTe = KorToEng()
    
    # 단어 등록
    kTe.registWord('책', 'bok')
    kTe.registWord('나비', 'butterfly')
    kTe.registWord('연필', 'pencil')
    kTe.registWord('학생', 'studen')
    kTe.registWord('선생님', 'teacher')

    # 단어 수정
    kTe.updateWord('책', 'book')
    kTe.updateWord('학생', 'student')

    # 단어 검색
    print(f'책 : {kTe.searchWord("책")}')
    print(f'나비 : {kTe.searchWord("나비")}')
    print(f'연필 : {kTe.searchWord("연필")}')
    print(f'학생 : {kTe.searchWord("학생")}')
    print(f'선생님 : {kTe.searchWord("선생님")}')
    
    # 단어 삭제
    kTe.removeWord('책')

    # 사전 출력
    kTe.printWords()

    