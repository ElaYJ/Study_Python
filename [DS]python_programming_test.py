# 데이터 사이언스 스쿨(AI 스쿨)

# 모든 공지사항을 꼼꼼하게 확인해주시기 바랍니다! 

# 파이썬 프로그래밍 테스트
# 내용: 파이썬 활용 능력 평가
# 범위: 파이썬 강의 기반
# 문항: 1 ~ 6번, 총 6문제
# 배점: 총점 100점 
# 1,2번 각 10점 
# 3,4번 각 15점 
# 5,6번 각 25점

# 채점 기준 
# 각 문제마다, print() 값의 결과만 나오시게끔 작성하시면 됩니다.
# 코드는 어떻게 작성하셔도 상관없습니다. 
# 코드 정상작동 만점 (각 배점에 맞게 만점)
# 코드 미실행(에러 발생)은 0점
# 부분 점수는 없습니다
 
# 숙지 사항
# 아래 각 문제에, pass 부분을 지우시고 코드를 작성해주시면 됩니다. 
# 모든 코드를 작성하셨을 때, 코드가 정상적으로 실행되어야 합니다. 
# 모든 문제는 print() 문으로 결과가 출력되어야 합니다. 
# 제출 코드는 실행했을 때 자동으로 실행되게끔 작성해주세요(input 함수 사용 금지). 
  

# start ! 

# 문제 1 (10점)
# 이름이 tmp인 크기가 0인 리스트 데이터를 만드시오.
# 문제 1번은 함수가 아닌, 변수만 선언해주시면 됩니다. 

print("1번 답안")
tmp = []
print(len(tmp))


# 문제 2 (10점)
# data_type 이라는 이름의 데이터형을 판별하는 함수를 작성해 주세요. 이 함수는 하나의 입력을 받아서
# 데이터형을 알아내야 합니다. Int, float, string, list, dict, tuple 등을 알아야 하며,
# 만약 list 형 데이터라면 list형 데이터 안에 있는 각 데이터의 데이터타입도 반환해야 합니다.
# 아래 실행 예시를 확인해 주세요
# >> data_type(1)
# int
# >> data_type(5.)
# float
# >> data_type([2, 3, [2, 3], "Hello"])
# list, <int, int, list <int, int>, string>

def data_type(data):

    def base_type(d):
        b_rlt = ''
        if isinstance(d, int): b_rlt = 'int, '
        elif isinstance(d, float): b_rlt = 'float, '
        elif isinstance(d, str): b_rlt = 'string, '
        elif isinstance(d, dict): b_rlt = 'dict, '
        elif isinstance(d, tuple): b_rlt = 'tuple, '

        return b_rlt

    def list_type(l_d):
        l_rlt = 'list <'

        for item in l_d:
            if type(item) == list:
                l_rlt += list_type(item)
            else:
                l_rlt += base_type(item)

        return l_rlt.rstrip(', ') + '>, '


    result = ''
    if type(data) == list:
        result = list_type(data)
    else:
        result = base_type(data)

    return result.rstrip(', ')

 
print("2번 답안")
print(data_type([1, 5., [2, 3], "Hello", [{1: 2}, [1, [2, 3.1]], "5"], (10, 11)]))


# 문제 3 (15점)
# 우리나라와 달리 미국은 간단한 식사만 해도 팁을 주는 문화가 있습니다. 그래서 팁을 계산하는 함수를
# 만들면 좋겠습니다. 팁은 함수에서 입력 받도록 하죠. 팁을 계산하는 함수는 calc_tips라는 이름으로 하고,
# 입력은 전체 금액, 팁 비율로 하면 되겠네요. 혹시 사용자가 팁 비율을 입력하지 않으면 디폴트로 10%를
# 적용하도록 해주세요. 그런데, 1달러 단위로 딱딱 떨어졌으면 좋겠습니다. 동전을 들고 다니는건
# 불편하니까요. 그래서 만약 계산했는데, 5.6달러가 나오면 그냥 6달러로, 5.1달러가 나와도 그냥 6달러로
# 계산하도록 해주세요. 함수의 결과는 return이 아니라 print가 되도록 해주세요.
def calc_tips(price, ratio=10): # 단위: (달러, 퍼센트)

    result = price * (ratio/100)

    print(f'팁(금액 {price}$의 {ratio}%): {round(result + 0.5)}달러')

print("3번 답안")   
print(calc_tips(73.5))


# 문제 4 (15점)
# 여러 문장으로 된 문서를 입력받아서 매칭되는 문자열의 횟수와 해당 문자열의 위치(index)를 알려주는
# search_target이라는 이름의 함수를 작성해주세요.
# 예)
# >> sentence = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."
# >> target = "than"
# >> search_target(sentence, target)
# 3, [20, 50, 82]
def search_target(sentence, target):
    indexes = []
    start_idx = 0

    while start_idx != -1:
        start_idx = sentence.find(target, start_idx)
        if start_idx != -1:
            indexes.append(start_idx)
            start_idx += 1

    print(len(indexes), indexes, sep=', ')
    
print("4번 답안")

sentence = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."
target = "than"

print(search_target(sentence, target))


# 문제 5 (25점)
# 여러분들은 div_ab라는 이름의 함수를 하나 만들어 주세요. 이 함수는 입력 인자로 a, b를 받으며, 받은
# 인자의 첫 번째를 a, 두 번째를 b라고 합니다. 이 함수는 입력 인자가 꼭 정수여야 하며, 함수 코드 내부에서
# 정수인지 아닌지를 판별하도록 해서 정수일 때만 나눗셈을 수행하도록 해주세요. 함수의 출력(return)은
# 없고, 함수의 마지막에 print 문으로 a / b를 계산하는 나눗셈의 결과를 출력하는 함수입니다. 출력의 형태는
# 정확하게는 몫과 나머지를 구하는 함수입니다. 출력의 첫 번째 항은 몫, 두 번째 항은 나머지가 되도록
# 코드를 작성해 주세요. 여러분에게 한 가지 안타까운 소식은 div_ab라는 함수를 만들 때 나눗셈 기호( / )나
# 어떤 모듈이든 나눗셈을 직접 수행하는 명령을 사용할 순 없습니다. 나눗셈 명령 없이 나눗셈을 수행해
# 주세요.
# 예)
# >> div_ab(3, 2)
# 3나누기 2의 결과 : 몫 1, 나머지 1
def div_ab(a, b):
    if isinstance(a, int) and isinstance(b, int):
        div_num = a
        quot, rest = 0, 0

        while div_num >= b:
            div_num -= b
            quot += 1

        rest = div_num

        print(f"{a}나누기 {b}의 결과 : 몫 {quot}, 나머지 {rest}")

    else:
        print("정수가 아닌 수로 나눗셈은 불가합니다.")

print("5번 답안")
a = 3
b = 2
print(div_ab(a, b))


# 문제 6 (25점)
# 하노이탑 문제가 있습니다. 아래 첨부된 사진의 글자가 흐릿하지만 신경쓰지 않아도 됩니다. 아래 그림을
# 설명해 보겠습니다. 크기 순으로 쌓여있는 원반 세 개가 있습니다. 이 원반은 A, B, C 장소 중 현재는 A에
# 있습니다. 하노이 탑 문제는 작은 원반 위에 큰 원반이 올려질 수 없다는 것과 한 번에 하나만 옮길 수
# 있다는 것을 지켜야 합니다. A에서 C로 갑자기 건너가는 것은 괜찮습니다.
# 여러분은 Python으로 아래 그림에 묘사된 하노이 탑 문제를 풀어야 합니다. 여러분의 문제는 하노이탑
# 원반의 개수는 n개입니다. 이 n개의 원반을 B 지점 혹은 C 지점으로 옮길 수 있어야 합니다. 즉, 하노이탑
# 문제를 풀 여러분이 작성해 주어야할 함수는 원반의 개수(n)와 어디서 원반이 시작하고(start_point) 어디서
# 옮기는지(end_point)를 입력받아야 합니다.
# 여러분이 만들어야하는 코드의 출력은 원반을 어디서 어디로 옮긴다는 메시지가 나타나면 됩니다. 위
# 그림을 예로 들면, 함수의 이름이 hanoi_sol이라면 위 그림의 상황은 Hanoi_sol(3, A, B)라고 입력해야 하고,
# 그 출력은 print 문으로
# A -> B
# A -> C
# B -> C
# A -> B
# C -> A
# C -> B
# A -> B
# 라고 화면에 출력되면 됩니다. 꼭 장소는 알파벳이어야 하며, 위 결과처럼 표기되어야 합니다.

def hanoi_sol(disc_cnt, start_point, end_point):
    bars = ['A', 'B', 'C']
    bars.remove(start_point); bars.remove(end_point)
    via_point = bars[0]

    if disc_cnt == 1:
        print(f'{start_point} -> {end_point}')

    else:
        hanoi_sol(disc_cnt - 1, start_point, via_point)
        print(f'{start_point} -> {end_point}')
        hanoi_sol(disc_cnt - 1, via_point, end_point)



print("6번 답안") 
print(hanoi_sol(3, 'A', 'B'))


print("모든 문제가 끝났습니다")
print("수고하셨습니다 :)")
# end !

# 시험이 끝난 후에는? 
# 제출 방법: 제공드린 설문지에 파일을 업로드 해주세요 
# 제출 양식: [DS]python_programming_honggildong.py 

# 대괄호 안에 대문자로 [DS] 
# _ 언더바 사용 
# 수강생분 성함(성부터 이름 순으로 모두 소문자 작성)
# 잘못된 예 -> [ds]_HongGilDong.py 또는 [ds]_HongGilDong.py.py 또는 [DS]_Hongggildong.py 등 위에 제시드린 제출 양식과 다른 모든 표현은 감점입니다.
# 파일 제출 양식 또한 감점 요인에 포함되오니, 반드시 꼼꼼하게 확인해주시기를 바랍니다. 
# 제출 양식 잘못됐을 시, 전체 점수에서 3점 감점

# 해설 또는 답안 공유 안내
# 문제에 대한 해설 또는 답안은 기본적으로는 공유드리지 않을 예정입니다
# 정해진 답을 제시드리는 것 보다, 각 문제에 대해 여러분들이 작성한 답안을 서로 공유해주셨으면 좋겠습니다 :) 
# 같은 기간, 같은 강의를 듣고 같이 공부하시는 다른 분들은 어떤 식으로 문제를 푸셨는지 서로 논의하실 수 있는 장이 마련됐으면 좋겠습니다.

# 왜 그렇게 하나요?
# 데이터 사이언스를 공부하시는 여러분은, 정답이 정해진 분야를 공부하고 계신 것이 아닙니다. 
# 여러분이 생각하는 모든 것이 정답일 수 있습니다. 
# 나의 생각을 다른 사람에게 표현하고, 설득하고, 공유하시는 방식에 익숙해지셨으면 하는 마음입니다. 

# 이번 테스트 뿐만 아니라, 추후 제공드리는 강의, 과제, 프로젝트에서도 정답을 바로 찾고 이해하려 하시는 것보다 
# 나라면 어떻게 할까? 이렇게 하는 게 더 좋지 않을까? 다른 사람들은 어떻게 생각할까? 나는 이렇게 생각하고 문제를 해결했는데 어떤 것 같나요? 
# 문제에 대해 스스로 사유하고, 해결한 나만의 방식을 공유하시는 힘을 길렀으면 좋겠습니다. 
# 남은 기간 더욱 힘내셨으면 하는 바램입니다. 
