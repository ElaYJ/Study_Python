'''
 # [공배수(common multiple)] 두 개 이상의 수에서 공통된 배수
 # [최대공배수(the Least/lowest Common Multiple)] 공배수 중 가장 작은 수
'''

#수 두개의 최소공배수
num1 = 24
num2 = 42
min_num = min(num1, num2)
gcd = 0

# 둘 중 작은 수만큼만 for문을 돌면 된다.
for i in range(1, (min_num + 1)):
    if num1 % i == 0 and num2 % i == 0:
        print('공약수: {}'.format(i))
        gcd = i

print('최대공약수: {}'.format(gcd))

# 최소공배수는 두 수의 곱을 최대공약수로 나눈 몫과 같다.
minNum = (num1 * num2) // gcd
print('최소공배수: {}'.format(minNum))



# 수 세개의 최소공배수
num1 = 24
num2 = 42
num3 = 14
min_num = min(num1, num2, num3)
gcd = 0

for i in range(1, (min_num + 1)):
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
        gcd = i

print('최대공약수: {}'.format(gcd))

# 세 수를 곱하면 최대공약수가 2번 더 곱해지므로 2번 나눠준다.
lcm = (num1 * num2 * num3) // (gcd ** 2)
print('{}, {}, {}의 최소공배수: {}'.format(num1, num2, num3, minNum))



# <Q> ----------------------------------------------------------------------
ship1 = 3; ship2 = 4; ship3 = 5
maxDay = 0

for i in range(1, (ship1 + 1)):
    if ship1 % i == 0 and ship2 % i == 0 and ship3 % i == 0:
        maxDay = i

print('최대공약수: {}'.format(maxDay))

minDay = (ship1 * ship2 * ship3) // (maxDay ** 2)
print('{}, {}, {}의 최소공배수: {}'.format(ship1, ship2, ship3, minDay))

print('{}일마다 모든 선박이 입항합니다.'.format(minDay))



