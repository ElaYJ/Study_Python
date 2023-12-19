'''
 # Diary는 읽고 쓰는 기능을 가짐
'''

import time

def writeDiary(u, f, d): # uri, file_nmae, diary_contents
    lt = time.localtime()
    timeStr = time.strftime('%Y-%m-%d %I:%M:%S %p', lt)

    filePath = u + f
    with open(filePath, 'a') as f:
        f.write(f'[{timeStr}] {d}\n')

def readDiary(u, f):
    lt = time.localtime()
    timeStr = time.strftime('<%Y-%m-%d %I:%M:%S %p>\n', lt)

    filePath = u + f
    datas = []
    datas.append(timeStr)
    with open(filePath, 'r') as f:
        datas.extend(f.readlines())

    return datas