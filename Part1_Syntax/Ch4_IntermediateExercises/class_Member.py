class Member:
    def __init__(self, i, p):
        self.id = i
        self.pw = p


class MemberRepository:

    def __init__(self):
        self.members = {}

    def addMember(self, m): # 'm' argument : class Member Object
        self.members[m.id] = m.pw

    def loginMember(self, i, p):
        isMember = i in self.members

        if isMember and self.members[i] == p:
            print(f'{i}: Log-in success!!')

        else:
            print(f'{i}: Log-in fail!!')

    def removeMember(self, i, p):
        if i in self.members:
            if self.members[i] == p:
                del self.members[i]
                print(f'{i}: Account Delete success!!')
            else:
                print(f'{i}: Wrong Password! Check Again!')
        else:
            print(f'{i}: You are not Our Member!!')

    def printMembers(self):
        for mk in self.members.keys():
            print(f'ID: {mk}')
            print(f'PW: {self.members[mk]}')
