width = 20
height = 50
print(width * height / 2)
print(globals()['width'])


students = [('홍길동', 3.9, 2016303),
            ('김철수', 3.0, 2016302),
            ('최자영', 4.3, 2016301),]

result = sorted(students, key=lambda student: -student[2])
print(result)


customer_name = '박찬호'

print('-' * 70)
print(' {0} 고객님께.\n\n {0} 고객님 안녕하세요.'.format(customer_name))
print(' 고객님께서 접수하신 A/S건에 대해서 연락을 드렸으나 연락이 어려워 메일 드립니다.\n\n' \
      ' ··· 중략 ··· \n\n <A/S 접수 내용>\n  성함 : {} \n  내용 : 에어컨 고장'
      .format(customer_name))
print('-' * 70)

customer_name = '홍길동'

print('-' * 70)
print(''' {0} 고객님께.

 {0} 고객님 안녕하세요.
 고객님께서 접수하신 A/S건에 대해서 연락을 드렸으나 연락이 어려워 메일 드립니다.

 ··· 중략 ···
 
 <A/S 접수 내용>
  성함 : {0} 
  내용 : 에어컨 고장'''.format(customer_name))
print('-' * 70)