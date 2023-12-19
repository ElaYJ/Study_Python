'''
# 이 파일이 실행파일이 되면 전체 코드가 모두 실행된다.
'''
print(f'unit_conversion.py __name__: {__name__}')

def CmToMm(n):
    return round(n * 10, 3)

def CmToM(n):
    return round(n * 0.01, 3)

def CmToInch(n):
    return round(n * 0.393, 3)

def CmToFeet(n):
    return round(n * 0.032, 3)


# 모듈일 때는 실행되는 않는 부분 --------------------------------------
# 즉, __nmae__ == 'unit_conversion'일 때는 실행 되지 않는 부분

if __name__ == '__main__':
    print(f'10cm: {CmToMm(10)}mm')
    print(f'10cm: {CmToM(10)}m')
    print(f'10cm: {CmToInch(10)}inch')
    print(f'10cm: {CmToFeet(10)}ft')

print()


