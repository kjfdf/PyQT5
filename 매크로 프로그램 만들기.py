import pyautogui
import time

# pyautogui.position() 마우스의 현재 위치의 좌표를 알려줌
# pyautogui.moveTo(100,200,3) 마우스를 100,200의 좌표위치로 3초에 걸쳐 이동시킴
# pyautogui.moveRel(0,300,2) 마우스를 현재 위치 기준 300픽셀 y위치를 이동시킴
# pyautogui.click(clicks=2,interval=2) 클릭을 2초간격으로 2번함.
# pyautogui.click(center) 해당 영역의 가운데 위치(클릭할 지점)를 튜플의 형태
# pyautogui.doubleClick()
# time.sleep(1) #더블클릭을 하고나서 1초를 쉬고나서 type write를 실행시킴 (click이후에 명령 실행할때 시간간격 필요하므로 같이 설정해야함)
# pyautogui.typewrite('Hello')
# pyautogui.typewrite(['enter']) 키보드의 엔터키를 누르게 하는 방법 []추가
# pyautogui.typewrite(['abc','enter'])는 안됨. (['a','b','c','enter'])는 됨. 키보드에는 a,b,c키는 있어도 abc키는 없으므로
# pyautogui.screenshot('my_region.png', region=(0, 0, 300, 300)) x=0, y=0에서 x=300, y=300 위치까지의 사각형 영역을 my_region.png 이미지 파일로 저장
# pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
# pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste 단축키 입력하기
# pyautogui.keyDown('c')
# pyautogui.keyUp('c') 개별 키 입력하기
# pyautogui.press('c')press() 는 keyDown() 과 keyUp() 동작을 함께 수행합니다
# print(pyautogui.KEYBOARD_KEYS) PyAutuGUI 모듈의 모든 키 리스트는 pyautogui.KEYBOARD_KEYS 를 출력하면 확인할 수 있습니다
# pyautogui.locateOnScreen('five.PNG') locateOnScreen() 에 그림(‘five.PNG’)를 설정해주면, 왼쪽 위의 위치와 영역의 가로, 세로 크기를 튜플의 형태((left, top, width, height))로 출력
# pyautogui.center(five_btn) 해당 영역의 가운데 위치(클릭할 지점)를 튜플의 형태
# pyautogui.PAUSE = 2.5
# pyautogui.moveTo(200, 200)
# pyautogui.click() moveTo() 함수 뒤에 2.5초, click() 함수 뒤에 2.5초의 딜레이
# pyautogui.dragTo(x, y, button=’right’) 마우스 오른쪽 버튼을 클릭한 채로 커서를 입력한 위치로 이동합니다. (‘left’, ‘right’, ‘middle’)
# pyautogui.dragRel(x, y) 마우스를 클릭한 채로 현재 위치에서 입력한 위치로 이동
# pyautogui.click(x, y) 마우스 커서를 입력한 위치로 이동해서 한 번클릭