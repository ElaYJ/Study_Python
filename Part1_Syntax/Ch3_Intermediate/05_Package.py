'''
 # [패키지] : 폴더처럼 관련 있는 모듈을 모아 그룹으로 관리할 수 있다.
    ▶ 동일한 기능을 하는 모듈이 존재할 경우
      모듈을 담고 있는 패키지가 도메인처럼 고유한 구분자 역할을 할 수도 있다.
      (동일한 기능을 하는 모듈이 있는 경우 패키지가 도메인처럼 고유한 구분자가 될 수도 있다.)
    ▶ 패키지 내 모듈을 사용하려면 실행 파일과 동일한 디렉토리 내에 패키지가 존재해야만 가능하다.
      이때 모듈을 'site-packages'라는 폴더에 넣어두면 어디에서 사용할 수 있는 범용 모듈이 된다.
'''

# site-package에 있는 모듈은 어디서나 사용할 수 있다.
# site-packages 폴더 내에 있는 모듈은 어디서나(어느 디렉토리에서나) 범용적으로 사용할 수 있다.
# Module sys - https://docs.python.org/3.12/library/sys.html
import sys # system에 대한 간략한 정보들을 가지고 있는 모듈

for path in sys.path: # 모듈이 있는 경로들을 가지고 있다.
    print(path)
# 현재 라인까지의 프로그램이 돌아가기위해(실행되기위해) 참조하게 되는 디렉터리들
# 이 디렉터리 중 어딘가에 Module sys가 있을 것이고 찾아서 가져와 실행한 것이다.
# D:\ElaYJ_study\_IDE_pyCharm\pythonProject\venv\Scripts\python.exe D:\ElaYJ_study\_IDE_pyCharm\pythonProject\Ch_3_Intermediate\05_Package.py
# D:\ElaYJ_study\_IDE_pyCharm\pythonProject\Ch_3_Intermediate
# D:\ElaYJ_study\_IDE_pyCharm\pythonProject
# C:\Python312\python312.zip
# C:\Python312\DLLs
# C:\Python312\Lib
# C:\Python312
# D:\ElaYJ_study\_IDE_pyCharm\pythonProject\venv -> virtual environment 가상 환경 : version별 충돌이 일어나지 았도록 독립적인 환경을 구현해준다.
# D:\ElaYJ_study\_IDE_pyCharm\pythonProject\venv\Lib\site-packages

# <Q> ------------------------------------------------------------------------------------------
# 내가 만든 모듈을 site-packages 폴더에 넣어두면 어디에서나 사용할 수 있는 모듈이 된다.
# site-packages에 약수와 소수를 리스트로 반환하는 모듈 만들기

from package_divisor import divisor_mod as dm, prime_num_mod as pnm

print(f'10의 약수: {dm.divisor(10)}')
print(f'50까지의 소수: {pnm.prime_number(50)}')
