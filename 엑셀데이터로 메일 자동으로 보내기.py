import openpyxl as xl
import pyperclip as clp
import pyautogui as gui
import time

wb=xl.load_workbook('mail_add.xlsx') #엑셀데이터 불러오기
ws=wb.active #엑셀데이터가 행단위로 리스트형태로 저장됨
lst=[]
for r in ws.rows: #모든셀의 데이터를 하나씩 불러와서 명령문 실행
    if r[0].value is None: #데이터가 비어있으면 단계를 건너뛰는 코드, 빈데이터를 none으로 처리
        continue
    lst.append([]) #셀값이 비어있지 않으면 데이터를 차례로 추가
    for c in r:
        lst[-1].append(c.value)
    print(lst[-1])
lst.pop(0) #엑셀 첫행의 필드명은 자동화 작업에는 필요가 없어서 제거해줌 
