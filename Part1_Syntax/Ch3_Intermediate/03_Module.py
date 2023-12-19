'''
# [모둘] : 함수가 선언되어 있는 파이썬 파일, 특정 기능을 가지고 있는 파이썬 파일
    ▶ 파이썬 모듈은 내부, 외부, 사용자 모듈로 구분할 수 있다.
    ▶ 내부 모듈 : 파이썬 설치 시 기본적으로 사용할 수 있는 모듈 ex) random, time, ...
    ▶ 외부 모듈 : 별도 설치 후 사용할 수 있는 모듈 ex) Panda, NumPy, ...
        - 판다스(Pandas)는 파이썬 데이터 분석 라이브러리 중 하나로,
           데이터 조작, 정제, 분석, 시각화 등을 위한 다양한 기능을 제공
        - 넘파이(NumPy)는 수치해석용 파이썬 패키지
    ▶ 사용자 모듈 : 사용자가 직접 만든 모듈
'''

# 내부 모듈 ========================================================================================
# random
import random

# 1부터 100사이의 난수  1개 생성
rNum = random.randint(1, 10)
print(f'rNum: {rNum}')

# 0부터 100사이의 난수 10개 생성
rNums = random.sample(range(0, 101), 10)
print(f'rNums: {rNums} \n {type(rNums)}')
print()


# 사용자 모듈 =======================================================================================
import module_calculator

module_calculator.AddCal(10, 20)
module_calculator.SubCal(10, 20)
module_calculator.MulCal(10, 20)
module_calculator.DivCal(10, 20)
print()

# <Q> ----------------------------------------------------------------------------------------
# 로또 번호 6개를 출력하는 모듈 만들기
import module_lotto

lottoNums = module_lotto.GetLottoNumbers()
print(f'lottoNumbers: {lottoNums}')

# <Q> ----------------------------------------------------------------------------------------
# 문자열을 거꾸로 반환하는 모듈
import module_reversStr

userStr = 'hello~ python' # input('문자열 입력: ')
reverseResult = module_reversStr.ReverseString(userStr)
print(f'Reversed String: {reverseResult}')
print()


# 모듈 사용법 =======================================================================================
# 'as' Keyword를 이용해 모듈 이름을 단축시킬 수 있다.
import module_calculator as calculator

calculator.AddCal(12, 17)
calculator.SubCal(12, 17)
calculator.MulCal(12, 17)
calculator.DivCal(12, 17)
print()

# 'from ~ import' Keyword를 사용해 모듈의 특정 기능(함수)만 사용할 수 있다.
# 콤마(,)를 이용해 이용하고자 하는 함수를 나열해서 쓸 수 있다.
# 'from' 키워드를 사용할 경우 함수를 호출할 때 모듈명을 적을 필요가 없다.
# 'from' 키워드를 이용해 해당 모듈 내 모든 함수를 쓰고 싶다면 '*'(전체를 의미)을 사용한다.
from module_calculator import AddCal, SubCal

AddCal(21, 46)
SubCal(21, 46)
print()

# <Q> ----------------------------------------------------------------------------------------
# 국어, 영어, 수학 점수를 입력하면 총점, 평균을 출력하는 모듈
import module_scores as scores

korScore = 85 # int(input('국어 점수 입력: '))
engScore = 92 # int(input('영어 점수 입력: '))
matScore = 79 # int(input('수학 점수 입력: '))

scores.AddScore(korScore)
scores.AddScore(engScore)
scores.AddScore(matScore)

print(scores.GetScores())
print('총점:', scores.GetTotalScore())
print('평균:', scores.GetAvgScore())

scores.DelScore()
scores.AddfScore(korScore, engScore, matScore)

print(scores.GetScores())
print('총점:', scores.GetTotalScore())
print('평균:', scores.GetAvgScore())
