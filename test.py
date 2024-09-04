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

