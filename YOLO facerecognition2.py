import cv2  # OpenCV 라이브러리로 카메라 제어 및 이미지 처리를 위한 모듈
import streamlit as st  # 간단한 웹 앱 제작을 위한 Streamlit 라이브러리
import os  # 파일 저장 경로 관리에 필요한 모듈
import time  # 시간 관련 작업 (딜레이, 타임스탬프) 처리에 필요한 모듈

class CameraApp:
    def __init__(self):
        # 클래스 생성자, 필요한 변수 초기화
        self.capture = None  # 현재 캡처된 사진 데이터
        self.photo_saved = None  # 저장된 사진의 경로
        self.is_camera_active = False  # 카메라 작동 상태를 추적

    def check_camera_in_use(self):
        """웹캠이 사용 중인지 확인하는 메서드"""
        cap = cv2.VideoCapture(0)  # 기본 카메라(0번 장치) 접근 시도
        if not cap.isOpened():
            return True  # 카메라를 열 수 없으면 다른 앱에서 사용 중으로 간주
        ret, _ = cap.read()  # 카메라에서 프레임 읽기 시도
        cap.release()  # 카메라 리소스를 해제
        if not ret:
            return True  # 프레임을 읽지 못하면 사용 중으로 간주
        return False  # 카메라가 사용 중이 아님

    def capture_photo(self):
        """사진을 촬영하고 저장하는 메서드"""
        cap = cv2.VideoCapture(0)  # 기본 카메라(0번 장치) 접근
        time.sleep(1)  # 카메라 안정화를 위해 1초 대기
        if not cap.isOpened():
            st.error("카메라를 열 수 없습니다.")  # 오류 메시지 출력
            return None, None
        
        ret, frame = cap.read()  # 사진 촬영(프레임 읽기)
        if ret:
            filename = f"captured_{int(time.time())}.jpg"  # 파일 이름 생성 (타임스탬프 기반)
            filepath = os.path.join(os.getcwd(), filename)  # 현재 디렉토리 기준 저장 경로 생성
            cv2.imwrite(filepath, frame)  # 이미지를 지정된 경로에 저장
            self.photo_saved = filepath  # 저장된 경로를 클래스 변수에 저장
            cap.release()  # 카메라 리소스 해제
            return frame, filepath  # 프레임과 경로를 반환
        cap.release()  # 촬영 실패 시에도 리소스 해제
        return None, None

    def start_camera(self):
        """실시간 카메라 피드를 보여주는 메서드"""
        cap = cv2.VideoCapture(0)  # 기본 카메라 접근
        self.is_camera_active = True  # 카메라 활성 상태 플래그 설정
        start_time = time.time()  # 카메라 실행 시작 시간 저장
        st_frame = st.empty()  # Streamlit 내 실시간 피드를 표시할 공간 생성
        
        # 카메라 피드를 5초 동안 실행
        while time.time() - start_time < 5:
            ret, frame = cap.read()  # 프레임 읽기
            if not ret:
                break  # 읽기 실패 시 반복 종료
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR(RGB) 색상 변환
            st_frame.image(frame, channels="RGB")  # Streamlit에 이미지 표시
        cap.release()  # 카메라 리소스 해제
        self.is_camera_active = False  # 카메라 비활성 상태 플래그 설정

    def show_ui(self):
        """Streamlit UI를 구성하는 메서드"""
        st.title("📷 AI 기반 얼굴 인식 보안 시스템")  # 제목 출력

        # 카메라 사용 상태 확인
        if self.check_camera_in_use():
            st.warning("웹캠을 다른 어플에서 사용 중입니다. 종료 후 다시 시도해주세요.")
            if st.button("🔄 재실행"):  # 재실행 버튼
                st.experimental_rerun()  # Streamlit 페이지 리로드
            return  # 이 상태에서는 더 이상 진행 불가
        
        # 사진 촬영 시작 버튼
        if st.button("📸 사진 촬영 시작"):
            self.start_camera()  # 카메라 활성화
            frame, path = self.capture_photo()  # 사진 촬영 및 저장
            if frame is not None:  # 촬영에 성공한 경우
                st.image(frame, caption="촬영된 사진", use_container_width=True)  # 촬영된 사진 표시
                if path:
                    st.success(f"✅ 사진이 저장되었습니다! 저장 경로: {path}")  # 저장 경로 출력
                
                col1, col2 = st.columns(2)  # 추가 동작을 위한 두 개의 버튼
                with col1:
                    if st.button("📷 추가 촬영"):
                        self.start_camera()  # 추가 촬영
                with col2:
                    if st.button("💾 사진 저장"):
                        st.success("📸 추가 저장이 완료되었습니다!")  # 저장 성공 메시지

if __name__ == "__main__":
    app = CameraApp()  # CameraApp 클래스의 인스턴스 생성
    app.show_ui()  # UI 표시
