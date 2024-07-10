s = "11(18(72(7)))" # input()
print(s)
s_list = [*s]
print(s_list)
print(s_list.pop())

s_reverse = s[::-1]
perenthesis = []
result, i = 1, 0
for c in s_reverse:
    print(c, c.isdigit())
    if c.isdigit():
        if i+1 == len(s): break
        if s_reverse[i+1].isdigit():
            result += 1
            i += 1
        elif s_reverse[i+1] == '(':
            result *= int(s_reverse[i+2])
            perenthesis.append(1)
            i += 2
    elif c == ')':
        perenthesis.append(-1)
        i += 1

print(sum(perenthesis))
print(result)
