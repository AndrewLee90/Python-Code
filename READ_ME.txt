# YouTube Downloader with Qt

이 프로젝트는 유튜브 동영상을 다운로드하여 MP4(영상), MP3(음원), JPG(프레임 이미지) 형식으로 저장할 수 있는 데스크톱 애플리케이션입니다. Python과 PySide6 기반으로 만들어졌으며, `yt-dlp`와 `ffmpeg` 라이브러리를 사용합니다.

## 주요 기능
- 유튜브 URL 입력 후 동영상 다운로드
- MP4, MP3, JPG 형식 중 선택 가능
- 다운로드 진행 상황 표시
- 사용자 지정 저장 경로 설정

## 설치 방법

이 프로젝트를 실행하기 위해 필요한 Python 패키지들을 pip install 명령어를 사용해 설치해야 합니다. 
주어진 코드에 기반하여 아래와 같은 패키지들을 설치하면 됩니다:

bash
pip install PySide6 yt-dlp

subprocess와 os는 Python 표준 라이브러리로 포함되어 있어 별도로 설치하지 않아도 됩니다.

ffmpeg 실행 파일이 필요하므로, ffmpeg 공식 사이트에서 다운로드하고 적절한 경로에 설정하세요.
공식사이트 주소 - https://ffmpeg.org/download.html?form=MG0AV3

`ffmpeg`를 다운로드한 뒤, 실행 파일 경로를 코드에서 지정합니다.

## 주의사항
- `ffmpeg` 경로를 정확히 설정해야 합니다.
- 인터넷 연결이 필요합니다.

## 향후 업데이트
- 다국어 지원
- GUI 디자인 개선
