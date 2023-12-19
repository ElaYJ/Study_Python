'''
# [실행(메인) 파일]
    ▶ 파이썬에서 제공하고 있는 전역변수 '__name__'을 이용해 실행/메인 파일을 만들 수 있다.
    ▶ 기본적으로 파이썬 파일(.py)마다 '__name__'변수에 특정 값이 저장되는데,
        해당 파일에서 실행(Run)이 이루어지면 '__main__'이라는 문자열이 할당되고,
        해당 파일이 다른 파일의 모듈로서 사용되어지면 파일명이 할당된다.
    ▶ 만든 파이썬 파일이 다른 파일에 import되어 모듈로 사용될 수도 있고, 실행 파일이 될 수도 있다.
      이때 모듈로서 실행되면 안되는 코드를 '__name__'을 이용해 조건문으로 걸러낼 수 있다.
'''
print(f'MainFile.py __name__: {__name__}')

import unit_conversion as unit

if __name__ == '__main__':
    inputNum = 10 # int(input('길이(cm) 입력: '))

    returnVal = unit.CmToMm(inputNum)
    print(f'{inputNum}cm: {returnVal}mm')

    returnVal = unit.CmToM(inputNum)
    print(f'{inputNum}cm: {returnVal}m')

    returnVal = unit.CmToInch(inputNum)
    print(f'{inputNum}cm: {returnVal}inch')

    returnVal = unit.CmToFeet(inputNum)
    print(f'{inputNum}cm: {returnVal}ft')

