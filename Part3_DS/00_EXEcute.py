num_list = [3, 4, 5]
min_val = min(num_list)
print(min_val)

ship1 = 72; ship2 = 54; ship3 = 12 # 주기
min_val = min(ship1, ship2, ship3)
print(min_val)

gcd = 0
for i in range(1, min_val + 1):
    if ship1 % i == 0 and ship2 % i == 0 and ship3 % i == 0:
       gcd = i

lcm = (ship1 * ship2 * ship3) // (gcd ** 2)

print(gcd, lcm)

num1 = 72
num2 = 54
num3 = 12
min_val = min(num1, num2, num3)
gcd = 0

for i in range(1, (min_val + 1)):
    print('cnt:\t\t\t', i)
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
        gcd = i
        print('공약수: {}'.format(i))
print('gcd: ', gcd)
