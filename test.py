[a, b] = ['python', 'life']
print(a, type(a), b, type(b))


class Family:
    lastname = '김'

print(Family.lastname)

a = Family()
b = Family()
print(a.lastname, b.lastname)

a.lastname = "최"
print(a.lastname, b.lastname, Family.lastname)


a = [1, 2, 3]
b = list(a)
a[1] = 0
print(a, b)

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초컬릿', '젤리']

result = zip(students, snacks)
print(list(result))

