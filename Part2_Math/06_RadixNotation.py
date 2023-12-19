'''
 # [진법(Radix Notation)]
    2진수(binary), 8진수(octal), 16진수(hexadecimal: 16진(기수)법)
'''

dNum = 30

# 10진수 -> X진수
print(' 2진수: {}'.format(bin(dNum)))
print(' 8진수: {}'.format(oct(dNum)))
print('16진수: {}'.format(hex(dNum)))

print('Type of bin(dNum): {}'.format(type(bin(dNum))))
print('Type of oct(dNum): {}'.format(type(oct(dNum))))
print('Type of oct(dNum): {}'.format(type(hex(dNum))))
print()

# 10진수 -> X진수(format()함수 이용)
print(' 2진수: {}'.format(format(dNum, '#b')))
# print(' 2진수: {}'.format(format(dNum, '#B'))) -> ValueError: Unknown format code 'B' for object of type 'int'
print(' 8진수: {}'.format(format(dNum, '#o')))
# print(' 8진수: {}'.format(format(dNum, '#O'))) -> ValueError: Unknown format code 'O' for object of type 'int'
print('16진수: {}'.format(format(dNum, '#x')))
print('16진수: {}'.format(format(dNum, '#X')))

print('Type of format(dNum): {}'.format(type(format(dNum, '#b'))))
print('Type of format(dNum): {}'.format(type(format(dNum, '#o'))))
print('Type of format(dNum): {}'.format(type(format(dNum, '#x'))))

print('2진수: {:#b}, 8진수: {:#o}, 16진수: {:#x}'.format(dNum, dNum, dNum))
print('2진수: {0:#b}, 8진수: {0:#o}, 16진수: {0:#x}'.format(dNum))
print()

# 형식문자(0b, 0o, 0x)
print(' 2진수: {}'.format(format(dNum, 'b')))
print(' 8진수: {}'.format(format(dNum, 'o')))
print('16진수: {}'.format(format(dNum, 'x')))
print('2진수: {0:b}, 8진수: {0:o}, 16진수: {0:x}'.format(dNum))
print()

# X진수 -> 10진수
print('2진수(0b11110)\t-> 10진수({})'.format(int(0b11110)))
print('8진수(0o36) \t\t-> 10진수({})'.format(int(0o36)))
print('16진수(0x1e) \t-> 10진수({})'.format(int(0x1e)))
# 문자열로 입력할 경우
print('2진수(0b11110)\t-> 10진수({})'.format(int('0b11110', 2)))
print('8진수(0o36) \t\t-> 10진수({})'.format(int('0o36', 8)))
print('16진수(0x1e) \t-> 10진수({})'.format(int('0x1e', 16)))

print('2진수(0b11110)\t-> 10진수({})'.format(int(bin(dNum), 2)))
print('8진수(0o36) \t\t-> 10진수({})'.format(int(oct(dNum), 8)))
print('16진수(0x1e) \t-> 10진수({})'.format(int(hex(dNum), 16)))
print()

# X진수 -> X진수
print('2진수(0b11110) ->  8진수({})'.format(oct(0b11110)))
print('2진수(0b11110) -> 10진수({})'.format(int(0b11110)))
print('2진수(0b11110) -> 16진수({})'.format(hex(0b11110)))

print('8진수(0o36) ->  2진수({})'.format(bin(0o36)))
print('8진수(0o36) -> 10진수({})'.format(int(0o36)))
print('8진수(0o36) -> 16진수({})'.format(hex(0o36)))

print('16진수(0x1e) ->  2진수({})'.format(bin(0x1e)))
print('16진수(0x1e) ->  8진수({})'.format(oct(0x1e)))
print('16진수(0x1e) -> 10진수({})'.format(int(0x1e)))
print()

# EX =====================================================================================

dNum = 27

# 10진수 > 2, 8, 16진수
print(' 2진수: {}'.format(bin(dNum)))
print(' 8진수: {}'.format(oct(dNum)))
print('16진수: {}'.format(hex(dNum)))


# X진수 -> 10진수
print(' 2진수(0b10101)\t-> 10진수({})'.format(int('0b10101', 2)))
print(' 8진수(0o135) \t-> 10진수({})'.format(int('0o135', 8)))
print('16진수(0x5f) \t-> 10진수({})'.format(int('0x5f', 16)))


# X진수 -> X진수
print('2진수(0b10101) \t->  8진수({})'.format(oct(0b10101)))
print('2진수(0b10101) \t-> 10진수({})'.format(int(0b10101)))
print('2진수(0b10101) \t-> 16진수({})'.format(hex(0b10101)))


print('8진수(0o675) \t->  2진수({})'.format(bin(0o675)))
print('8진수(0o675) \t-> 10진수({})'.format(int(0o675)))
print('8진수(0o675) \t-> 16진수({})'.format(hex(0o675)))


print('16진수(0x45d) \t->  2진수({})'.format(bin(0x45d)))
print('16진수(0x45d) \t->  8진수({})'.format(oct(0x45d)))
print('16진수(0x45d) \t-> 10진수({})'.format(int(0x45d)))

