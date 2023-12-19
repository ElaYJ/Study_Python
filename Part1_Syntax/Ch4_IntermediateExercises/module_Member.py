class EmptyDataException(Exception):

    def __init__(self, i):
        super().__init__(f'{i} is empty! Fail to register')

def checkInputData(n, m, p, a, ph):

    if n == '':
        raise EmptyDataException('name')
    elif m == '':
        raise EmptyDataException('mail')
    elif p == '':
        raise EmptyDataException('password')
    elif a == '':
        raise EmptyDataException('address')
    elif ph == '':
        raise EmptyDataException('phone')
    else:
        return True

class RegisterMember():

    def __init__(self, n, m, p, a, ph):
        self.m_name = n
        self.m_mail = m
        self.m_pw = p
        self.m_addr = a
        self.m_phone = ph
        # print('Membership completed!!')
        if checkInputData(n, m, p, a, ph):
            print('Membership completed!!')
        # try:
        #     if checkInputData(n, m, p, a, ph):
        #         print('Membership completed!!')
        # except EmptyDataException as e:
        #     print(e)

    def printMemberInfo(self):
        print(f'm_name: {self.m_name}')
        print(f'm_mail: {self.m_mail}')
        print(f'm_pw: {self.m_pw}')
        print(f'm_addr: {self.m_addr}')
        print(f'm_phone: {self.m_phone}')