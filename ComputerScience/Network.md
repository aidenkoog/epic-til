# Network

정리될 내용들은 아래와 같습니다.

- 개념 / 용어 정의, 사용 이유


## Network, 이더넷 프레임 (Ethernet Frame) - IEEE 802.3

- Preamble: 물리계층, 7바이트로 송신자와 수신자 간의 동기화 설정
    - 10101010
- SOF(Start Of Frame)
    - 이더넷 헤더라고 알려주는 신호로 1바이트 (10101011)
- Destination Address: 목적지 MAC주소(6바이트)
- Source Address: 송신자 MAC주소(6바이트)
- Type: 상위계층 프로토콜 종류(IP:0800, ARP:0806) 2바이트
- Data: 전달하는 데이터, 최소 46바이트이고 최대 1500바이트
- PAD(Packet Assembler Disassembler)
    - Data가 46바이트이하이면 0으로 채움
- FCS(Frame Check Sequence): 프레임 오류 체크(4바이트)

## Internet, IPv4 Header (Datagram)

- Version: IPv4
- Header Length: 헤더길이 (4Byte)
- Tos(Type of Service): 서비스 품질, 대부분 사용 안함
- Total Packet Length: IP 패킷 전체길이(바이트 단위)
- Fragment Identifier: 동일한 데이터그램의 일련번호
- Fragmentation Flag: 분열여부
- Fragmentation Offset: 조각 데이터그램 위치
- TTL(Time To Live): 통과할 수 있는 라우터수
- Header Checksum: 오류검출
- Source Address: 송신자 IP
- Destination Address: 목적지 IP

## Internet, IPv6 Header

- Version: IPv6
- Traffic Class(Priority): Qos를 위한 클래스 설정(우선순위)
- Flow Label: Flow를 위한 인덱스 지정
- Next Header: 기본헤더 다음의 헤더 정보로 IPv6 확장헤더, TCP, UDP일 수 있음
- Hop Limit: IPv4의 TTL
- Source Address: 송신자 IP
- Destination Address: 목적지 IP

## Internet, ICMP Header

- Type: ICMP 메시지 유형
- Code: Type과 같이 사용되며 세부적 유형을 표현
- Checksum: 오류검출
- ICMP Message: 메시지 타입별 추가정보

## Internet, ARP Header

- Hardware Type: MAC 주소 형식(Ethernet은 항상 1임)
- Protocol Type: 매핑되는 프로토콜 주소(IPv4는 0x0800)
- Hardware Address Length
- Protocol Address Length
- Operation Code
    - 1: ARP Request
    - 2: ARP Reply
    - 3: RARP Request
    - 4: RARP Reply

## Transport, TCP Header (Segment)

- Source Port: 송신자 포트번호
- Destination Port: 목적지 포트번호
- Sequence Number: 일렬의 순서번호
- Acknowledgement Number: 수신자 응답 번호
- Control Flags
    - ACK: 유효성
    - SYN: 연결요구
    - URG: 긴급 데이터
    - PSH: 버퍼링을 하지 않음
    - FIN: 정상 접속 종료
    - RST: 재연결
- Window Size: 수신 윈도우 버퍼크기, 수신 가능한 바이트 수
- Checksum: 오류 검출
- Urgent pointer: URG Flag가 지정된 경우만 유효함, 긴급 데이터 전송
- Optional Data: 기타 목적

## Transport, UDP Header

- Source Port: 송신자 포트번호
- Destination Port: 목적지 포트번호
- Length: 헤더길이
- Checksum: 오류검출

## Application, HTTP Header (Message)

- HTTP Request Header
    - Request Method: GET, POST, OPTIONS, PUT, DELETE, CONNECT
    - Accept: 사용 가능한 미디어 타입(text/*, text/html)
    - Accept-Language: 웹 브라우저 인식 언어
    - User-Agent: 웹 브라우저 정보
    - Accept-Encoding: 인코딩 방식(gzip)
    - Host: 웹서버 URL
    - Connection: Keep Alive 혹은 Close
- HTTP Response Header
    - Status Code: HTTP 응답코드(200, 404)
    - Server: 서버 프로그램 이름과 버전
    - Expires: 자원 만료일자
    - Cache control: 캐시 사용여부, no-cache는 사용 안함
    - Pragma: 캐시 사용여부
    - Content-Encoding: 메시지 인코딩 방식
    - Content-Length: 리소스크기
    - Keep-Alive: 연결유지 시간
    - Connection: Keep-Alive 사용여부
    - Content-Type: 미디어 타입

## 인터넷망 ~ 내부네트워크

- 인터넷망에서 ~ 내부네트워크까지 흐름
    - 인터넷망 > L3스위치(웹 방화벽/방화벽, 웹서버, DB서버)
    - L3스위치 > VPN > 트래픽 수집 장비(TAP) > 방화벽 / 위협관리시스템(IDS, TMS)
    - 방화벽 / 위협관리시스템(IDS, TMS) > 침입방지시스템(IPS) > 백본스위치
    - 백본 스위치 > 방화벽 > 허브 > 서버팜 (내부 네트워크)
- 벡본 (벡본스위치)
    - 네트워크의 중심. 방화벽, 워크그룹 스위치, 각종 서버가 접속하는 핵심영역
    - 많은 트래픽을 처리해야 해서 고가용성, 고성능, 고확장성이 확보되는 기가급 장비를 많이 사용
    - 이 장비의 성능이 안 좋으면 이곳에서 병목(bottleneck)이 걸릴 가능성이 많다.
    - 주로 L3스위치가 백본스위치 역할을 한다.
    - 스위치를 그리지 않고 선으로만 표시하기도 한다.
- 허브(Hub)
    - 여러 개의 시스템을 연결할 경우 각 포트별로 케이블을 연결하여 사용하는 물리계층의 장치
- 스위치(Switch) L1~L3까지 사용
    - 포트에 연결된 네트워크 연결상태 관리
    - 포트에 네트워크 관리 기능이 추가
    - 터널링 기술 및 Qos를 지원
        - 터널링
            - 한 네트워크에서 다른 네트워크로 패킷을 이동시키는 방법
            - 데이터스트림을 인터넷상에서 가상의 파이프를 통해 전달시키는 기술
        - Qos (Quality of service)
            - 한정된 네트워크 용량으로 트래픽을 제어하고 주요 애플리케이션의 성능을 보장하기 위해 메커니즘이나 기술을 활용하는 것
- VPN의 종류
    - SSL VPN: OSI 4~7계층 동작
        - 웹 브라우저를 기반으로 동작, RSA / X.509방식
    - IPSEC VPN: 전송모드와 터널모드
    - PPTP VPN: MS의 RAS를 기반으로 데이터 링크 계층에서 동작
    - L2TP VPN: 데이터 링크 계층, PPTP와 호환
- 침입차단시스템(방화벽)
    - Access Control을 하는 보안장비
        - 스크리닝 라우터
        - 버스천 호스트
        - 듀얼 홈
        - 스크린드 호스트
        - 스크린드 서브넷
- 침입탐지시스템(IDS/TMS)
    - 호스트 및 네트워크 침입을 탐지하는 시스템
    - 오용탐지(Misuse)
        - 시그니처 기반, 지식기반, 미리정의된 Rule과 비교
        - False Positive가 낮고 False Negative가 크다
    - 비정상탐지(Anomaly)
        - 프로파일, 행위기반, 통계기반, 사용패턴과 비교, Zero day attack에 대응
        - False Positive가 크다
    - False Positive
        - 공격이 아닌 것을 공격으로 오판
    - False Negative
        - 공격인데 공격이 아니라고 오판
- IDS 종류
    - Network, Host, Application, Misuse, Anomaly, Real time, Interval-based
    - Active(탐지만 수행), Passive(대응 수행)
- ESM(Enterprise Security Management)
    - 로그를 실시간으로 수집해서 분석하는 통합보안 관제 시스템
- SIEM(Security Information & Event Management)
    - 로그 수집, 취약점 관리, 실시간 탐지, 경보 등을 수행하는 이벤트 기반 보안 관제 시스템
- NAC(Network Access Control)
    - End Point 보안, IP 및 MAC 주소를 사용해서 네트워크 접근 제어
- Honeypot
    - 공격자를 유인하기 위한 함정
    - Zero day 공격을 탐지하기 위한 수단
- 웹 방화벽(Web Firewall)
    - 웹 애플리케이션의 취약점을 탐지 및 대응
    - 홈 페이지 및 웹 프로토콜에 대한 보안 서비스