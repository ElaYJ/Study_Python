import random as rd

class Dice:

    def __init__(self):
        self.cNum = 0
        self.uNum = 0

    def setCnum(self):
        print('[Dice] setCnum()')
        self.cNum = rd.randint(1, 6)

    def setUnum(self):
        print('[Dice] setUnum()')
        self.uNum = rd.randint(1, 6)

    # 주사위를 던진다.
    def startGame(self):
        print('[Dice] startGame()')
        self.setCnum()
        self.setUnum()

    # 결과 확인
    def printResult(self):
        print('[Dice] printResult()')

        if self.cNum == 0 or self.uNum == 0:
            print('주사위 숫자 설정 전 입니다.')

        else:
            if self.cNum > self.uNum:
                print(f'컴퓨터 vs 유저 : {self.cNum} vs {self.uNum} >> 컴퓨터 승!!')

            elif self.cNum < self.uNum:
                print(f'컴퓨터 vs 유저 : {self.cNum} vs {self.uNum} >> 유저 승!!')

            elif self.cNum == self.uNum:
                print(f'컴퓨터 vs 유저 : {self.cNum} vs {self.uNum} >> 무승부!!')


if __name__ == '__main__':
    dc = Dice()
    dc.startGame()
    dc.printResult()
