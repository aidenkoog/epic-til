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