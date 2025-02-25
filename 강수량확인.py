import tkinter as tk
from tkinter import messagebox
import webbrowser
import pyautogui
import time
import os

# 기본 설정
root = tk.Tk()
root.title("오늘은 우산을 챙겨야할까?")
root.geometry("500x500")

# 스크린샷 찍을 좌표 (네이버 검색 결과 페이지에서 원하는 위치를 지정)
# 해상도는 3440 x 1440 크롬 전체화면 기준

START_X = 1066  # 시작 X 좌표: 스크린샷 영역의 왼쪽 상단 가로 위치
START_Y = 92    # 시작 Y 좌표: 스크린샷 영역의 왼쪽 상단 세로 위치
END_X = 1853    # 끝 X 좌표: 스크린샷 영역의 오른쪽 하단 가로 위치
END_Y = 1146    # 끝 Y 좌표: 스크린샷 영역의 오른쪽 하단 세로 위치


#좌표값 설정 코딩
#import pyautogui
#import time

#while True:
#   print(pyautogui.position())
#  time.sleep(1.0)



# 네이버 검색 열기 및 오늘 강수량 확인 함수
def check_today():
    url = "https://search.naver.com/search.naver?query=오늘+강수량"
    webbrowser.open(url)
    time.sleep(5)  # 브라우저가 완전히 로드될 때까지 대기 (5초로 늘림)

    # 스크린 샷 시작 좌표 클릭 
    pyautogui.click(START_X, START_Y)
    time.sleep(1)  # 클릭 후 대기

# 스크린샷 여부 확인
    if messagebox.askyesno ("확인", "오늘 날씨 정보를 스크린샷 하시겠습니까?"):
        # Yes를 선택한 경우, 다이얼로그가 닫힌 후 추가 대기 후 스크린샷
        time.sleep(2)  # 다이얼로그 닫힘 후 페이지 안정화를 위해 2초 대기
        take_screenshot("today_rainfall")
    else:
        messagebox.showinfo("안내", "월간 탭으로 이동하면 월간 강수량 정보를 확인할 수 있습니다.\n스크린샷은 찍히지 않았습니다.")

# 스크린샷 찍고 저장
def take_screenshot(filename):
    # 스크린샷 영역 계산: (left, top, width, height)
    width = END_X - START_X
    height = END_Y - START_Y
    screenshot = pyautogui.screenshot(region=(START_X, START_Y, width, height))
    exe_dir = os.path.dirname(os.path.abspath(__file__))  # EXE 파일 경로
    screenshot.save(os.path.join(exe_dir, f"{filename}.png"))
    time.sleep(1)  # 스크린샷 저장 후 1초 대기 후 메시지
    messagebox.showinfo("성공", f"{filename}.png 파일이 저장되었습니다!\n저장 위치: {exe_dir}\n월간 탭으로 이동하면 월간 강수량 정보를 확인할 수 있습니다")

# GUI 구성
label = tk.Label(root, text="오늘은 우산을 챙겨야할까?", font=("나눔고딕", 16))
label.pack(pady=20)

# 버튼 구성
today_button = tk.Button(root, text="오늘 강수량 확인", command=check_today)
today_button.pack(pady=10)

#우산 파일 유무 (이미지 파일이 있다면 사용)
try:
    umbrella_img = tk.PhotoImage(file="umbrella.png")  # 이미지 파일 경로
    umbrella_label = tk.Label(root, image=umbrella_img)
    umbrella_label.pack(pady=10)
except tk.TclError:
    # 이미지 파일이 없으면 텍스트로 대체
    umbrella_text = tk.Label(root, text="☂☂ 우산 ☂☂", font=("나눔고딕", 12))
    umbrella_text.pack(pady=10)

# 프로그램 실행
root.mainloop()



# pyinstaller --onefile --add-data "umbrella_icon.png:." "심화과제 강수량확인.py"
# exe 파일 만들기 명령어
