📝 기획 의도

네트워크를 공부하거나 보안 시스템을 설계할 때, IP 주소와 서브넷 마스크의 개념을 정확히 이해하는 것은 필수적입니다. 
이를 위해 IP 주소 대역과 서브넷 정보를 한눈에 확인할 수 있는 파이썬 스크립트를 작성하였습니다. 
사용자가 IP/CIDR 주소를 입력하면, 해당 네트워크의 주요 정보를 자동으로 계산해 줍니다.

📌 기능 소개

네트워크 주소 및 브로드캐스트 주소 계산
사용 가능한 IP 주소 범위 및 개수 확인
총 IP 개수 계산
유효하지 않은 IP 입력 시 예외 처리




import ipaddress

def calculate_subnet_info(ip_cidr):
    try:
        # IP 네트워크 객체 생성
        network = ipaddress.ip_network(ip_cidr, strict=False)
        
        # 네트워크 주소와 브로드캐스트 주소
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        
        # 사용 가능한 호스트 IP 주소 범위
        usable_hosts = list(network.hosts())
        if usable_hosts:
            first_usable = usable_hosts[0]
            last_usable = usable_hosts[-1]
            usable_count = len(usable_hosts)
        else:
            first_usable = last_usable = None
            usable_count = 0

        # 결과 출력
        print(f"입력값: {ip_cidr}")
        print(f"네트워크 주소: {network_address}")
        print(f"브로드캐스트 주소: {broadcast_address}")
        print(f"사용 가능한 IP 주소 범위: {first_usable} ~ {last_usable}")
        print(f"사용 가능한 IP 개수: {usable_count}")
        print(f"총 IP 개수: {network.num_addresses}")
    
    except ValueError as e:
        print(f"유효하지 않은 IP 입력: {e}")

# 사용 예시
input_ip = "216.39.106.163/28"  # 원하는 IP 대역 입력
calculate_subnet_info(input_ip)


예상결과

입력값: 216.39.106.163/28
네트워크 주소: 216.39.106.160
브로드캐스트 주소: 216.39.106.175
사용 가능한 IP 주소 범위: 216.39.106.161 ~ 216.39.106.174
사용 가능한 IP 개수: 14
총 IP 개수: 16
