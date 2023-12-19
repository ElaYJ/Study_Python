'''
# [논리 연산자] : and, or, not
'''

# and 연산
print('{} and {} : {}'.format(True, True, (True and True)))
print('{} and {} : {}'.format(False, True, (False and True)))
print('{} and {} : {}'.format(True, False, (True and False)))
print('{} and {} : {}'.format(False, False, (False and False)))

# or 연산
print('{} or {} : {}'.format(True, True, (True or True)))
print('{} or {} : {}'.format(False, True, (False or True)))
print('{} or {} : {}'.format(True, False, (True or False)))
print('{} or {} : {}'.format(False, False, (False or False)))

# not 연산
print('not {} : {}'.format(True, (not True)))
print('not {} : {}'.format(False, (not False)))