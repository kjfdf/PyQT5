import pyautogui,time

i=1
for i in range(13):
    pyautogui.moveTo(2995,969) #유튜브 저장 버튼으로 가서 클릭
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(2012,262) #저장창 나오면 pyautogui디렉토리로 가서 클릭
    pyautogui.click()
    pyautogui.moveTo(2056,635) #디렉토리 파일 이름명으로 가서 마우스 왼쪽버튼 클릭하고 순서대로 숫자 넣기
    time.sleep(1)
    pyautogui.typewrite('i')
    time.sleep(0.5)
    pyautogui.moveTo(2875,703) #저장버튼있는곳으로 이동
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(3721, 314)
    pyautogui.dragRel(0, 36)
    pyautogui.moveTo(3526, 311)
    i+=1
    continue
