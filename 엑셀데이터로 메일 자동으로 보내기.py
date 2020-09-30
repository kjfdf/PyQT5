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

for i in lst:
    x,y=gui.locateCenterOnScreen('03_01.PNG')
    gui.click(x,y) #x,y가 눌려서 메일쓰기가 되도록
    time.sleep(1) #1초의 딜레이를 줘서 화면바뀌는것을 기다림
    clp.copy(i[-1])
    gui.hotkey('ctrl','v')
    time.sleep(1)
    gui.hotkey('tab')
    gui.hotkey('tab')
    clp.copy('[파이썬 마켓]{}님의 주문 내역을 안내드립니다.'.format(i[1]))
    gui.hotkey('ctrl','v')
    time.sleep(1)
    gui.hotkey('tab')
    clp.copy('''
    안녕하세요. {}님. 파이썬 마켓입니다.
    {}-{}-{}에 주문하신 제품에 대해 안내드립니다.
    
    제품명:{}
    금액:{:,}
    
    주문해주셔서 감사합니다.
    '''.format(i[1],i[0].yaer,i[0].month,i[0].day,
               i[2],i[3]))
    gui.hotkey('ctrl','v')
    time.sleep(1)

    x,y=gui.locateCenterOnScreen('03_02.PNG',grayscale=True) #보내기버튼을 누르기
    gui.click(x,y)
    time.sleep(20) #20초정도 딜레이를 주고 반복하도록 실행시키기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog=MainDialog()
    main_dialog.show()
    app.exec_()

