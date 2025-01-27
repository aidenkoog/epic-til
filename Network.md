# Network

정리될 내용들은 아래와 같습니다.

- 개념 / 용어 정의, 사용 이유
- Interview Question, Answer

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