# 정리가 완료되지 않은 내용 (Temporary Note)

정리될 내용들은 아래와 같습니다.

- 개념 / 용어 정의, 사용 이유
- Interview Question, Answer

#### Web3 (3.0)

- Read Only (ex. wikipedia)
  - 게시판 (Web 1.0) ~ 2005, 제작자의 컨셉만을 따라야 하는 방식
  - 닷컴버블 사태 (IT Company)
    - 2002, 소셜 네트워크 발전의 시작, 사용자의 능동적인 행동 가능 (Web 2.0, 2005 ~)
    - Web 2.0: Read / Write, 소셜미디어 / 핀테크 / 클라우드 (개인 정보 노출) / 고유의 이메일 계정 필요
  - 주요 키워드 : 탈중앙화, 개빈 우드 (이더리움, 폴카닷) - 서비스의 운명은 기업에 달려있다.
    - 서비스 제공자가 없는 서비스가 될 것.
    - 모든 정보가 NFT화 되어 블록체인에 기록. 소유권이 100% 유저에게 있음.
    - 개인의 정보를 중앙화된 기업이 소유하지 못할 것
    - 지갑을 통해 단일 로그인 방식으로 다양한 플랫폼에서 이용.
    - 브라우저에서 금융활동 가능할 것.
    - Web 2.0 중앙화 시스템 장점: 기업이 주는 신뢰, 탈중앙화의 신뢰는? 블록체인 내 프로그램 코드 -> Certik, Hacken, Slomist, 수호.io, 해치랩스 등의 업체에서 코드 검증
    - Web 3.0 소개 용어들
      - 블록체인, DAO (탈중앙화 자율조직) - 서비스 이용자 사이에 제안 / 투표로 의자 및 정책 결정이 이루어짐.
      - 지갑: 신분, 익명성 보장 (Distributed Ledger Technology), Metamask
      - De-Fi (탈중앙화 금융): 웹 상에서 금융 서비스 실현 (Decentralized Finance)
      - dApp
      - Smart Contract
      - ICO (Initial Coin Offering)
      - IPFS
      - AI, 자연어, Symentic Web, Metabus, Token (Coin)
      - OnChain 통신 (Web3.js, ether.js, caver.js)
- 기술이라는 관점보다는 미래 인터넷 세계 관련한 운동 / 방향 / 지향점으로 이해

#### IaaS / PaaS / SaaS 개념 설명

- 클라우드 서비스 종류
- **IaaS** (Infrastructure as a Service)
  - 서비스로 제공되는 인프라 구조
  - 개발사에 제공되는 물리적 자원을 가상화
  - 확장성이 높고 자동화된 컴퓨팅 리소스를 가상화하여 제공
  - 제공하는 서비스
    - 가상화 / 서버 / 스토리지 / 네트워크
  - Ex: **AWS**, Microsoft Azure, DigitalOcean, GCE
- **PaaS** (Platform as a Service)
  - 서비스로 제공되는 플랫폼
  - 개발사에 제공되는 플랫폼을 가상화
  - 주로 응용 프로그램을 개발할 때 필요한 플랫폼을 제공
  - 제공하는 서비스
    - 런타임 / 미들웨어 / 운영체제 / 가상화 / 서버 / 스토리지 / 네트워크
  - Ex: AWS Elastic Beanstalk, Windows Azure, **Heroku**, Google App Engine
- **SaaS** (Software as a Service)
  - 서비스로 제공되는 플랫폼
  - 고객에게 제공되는 소프트웨어를 가상화
  - 클라이언트 측에서 별도의 다운로드 / 설치 불필요
  - 제공하는 서비스
    - 애플리케이션 / 데이터 / 런타임 / 미들웨어 / 운영체제 / 가상화 / 서버 / 스토리지 / 네트워크
  - Google Apps, **Dropbox**, Salesforce, WhaTap

#### 서버리스 배포와 API 제공자

- 베르셀(Vercel) / 네트리파이(Netlify)

#### 프론트엔드 툴과 프레임워크

- 스벨트(Svelte)
- 퀵(Qwik)

#### 분리 아키텍쳐 (마이크로서비스)

- API, 프론트엔드 진화, 커스텀 미들웨어 등

#### 디지털 페어런팅 (Digital Parenting)

- 디지털과 페어런팅의 합성어
- 전통적 육아 방식 + 디지털적 요소 병합
- 디지털 기기 사용을 차단하기 보다 아이에게 올바른 디지털 기기 사용법을 제시하는 방법
- 무엇을 했는지? / 상 또는 벌칙 부여 / 규칙의 이유에 대한 설명 / 디지털 경험 증대
- 스스로 규칙을 정하고 지킬 수 있도록 동기 부여
- 자율성 존중, 방치가 아닌 관리하는 방향

#### 덕 타이핑 

- Duck Typing
- 동적 타이핑의 한 종류로, 객체의 변수 및 메소드의 집합이 객체의 타입을 결정하는 것을 말함
- 사람이 오리처럼 행동하면 오리로 봐도 무방하다라는게 덕 타이핑(Duck Typing)
- 타입을 미리 정하는게 아니라 실행이 되었을 때 해당 Method들을 확인하여 타입을 결정
- 장점
  - 타입에 대해 매우 자유로움
  - 런타임 데이터를 기반으로 한 기능과 자료형을 창출하는 것
- 단점
  - 런타임 자료형 오류가 발생할 수 있음
  - 런타임에서, 값은 예상치 못한 유형이 있을 수 있고, 그 자료형에 대한 무의미한 작업이 적용됨
  - 이런 오류가 프로그래밍 실수 구문에서 오랜 시간 후에 발생할 가능성이 있음
- 데이터의 잘못된 자료형의 장소로 전달되는 구문은 작성하지 않아야 함
  - 버그를 찾기 어려울 수도 있음
- 예시
  - 스몰토크, 루비, 파이썬

#### 안드로이드 파편화

- 구글이 아무리 업데이트를 발 빠르게 한다할지라도 해당 단말 제조사에서 업데이트를 해주지 않게 되면
- 안드로이드 플랫폼 버전의 파편화가 발생
- iOS는 애플이 모든것을 관리하므로 파편화가 적음

#### MQTT

- Message Queueing Telemetry Transport
- 2016년 표준화, 발행 - 구독 기반의 메시지 송수신 프로토콜
- 네트워크 대역폭이 제한되는 원격 통신을 위해, 즉 IoT와 같은 제한된, 또는 대규모 트래픽 전송을 위해 만들어진 프로토콜
- TCP/IP 프로토콜 위에서 동작하나 그보다 가볍고 많은 통신 제약을 해결해준다고 함?
- MQTT는 블루투스나 지그비처럼 별도의 모듈로 별도의 대역폭을 갖는 통신 규약이 아님
- Wi-Fi나 기타 방법을 통해? 인터넷을 통해 TCP/IP 기반의 메시지 송수신을 한다라고 이해하면 될듯함.
- 예. 페이스북 메신저 --> MQTT 채택, 배민 서비스에서도 중계 시스템 개선을 위해 도입 시도를 한적이 있음
- 트레이드 오프는 존재, 메시지가 가벼운 만큼 유형이나 QoS (서비스 품질) 에는 제약있음
- 특이점 / 장점
  - 연결 지향적
    - Sensor --> MQTT Broker --> Mobile / Desktop
    - TCP/IP 소켓 연결을 한 후 명시적으로 연결을 끊거나 네트워크 사정에 의한 끊어짐을 제외하고는 계속 연결 상태 유지
    - Live Heartbeat와 토픽에 발행되는 메시지를 통해 연결 유지 / 메시지 송수신
    - 끊어지면 재 접속 가능
  - 브로커 통한 통신
    - 통신은 브로커를 통해서만 가능
    - 일대일 또는 일대다 모두 가능 (브로커가 있으므로)
  
#### B2B, B2C 개발 정리

- B2B
  - 기업 고객의 요구사항에 맞는 솔루션을 판매 및 유지보수 해주거나, 직접 만들어주는 비즈니스를 수행
  - 고객의 요구사항을 구현하는데 좀 더 집중하게 되며, 개발 도중 누락된 요구사항, 문의사항이 있을 경우 빠르게 의사소통하여 해결하는 좀 더 비즈니스 쪽에 치우친 역할을 담당
  - 솔루션의 라이센스 개수가 곧 매출
- B2C
  - 다수의 불특정 개인/집단을 상대로 자체 서비스 비즈니스를 수행
  - 사용자 수를 쉽게 예측할 수 없으며, 기업의 매출의 대부분이 해당 서비스를 통해 나오므로, 끊임없이 트래픽 개선, 시장성 실험 등의 요구사항을 소프트웨어 적으로 해결해야 함
  - 매출 한계 없음

#### A/B Testing

- A/B 테스팅이란 웹 사이트 방문자를 임의로 두 집단으로 나누고, 한 집단에게는 기존 사이트를 보여주고 다른 집단에게는 새로운 사이트를 보여준 다음, 두 집단 중 어떤 집단이 더 높은 성과를 보이는지 측정하여, 새 사이트가 기존 사이트에 비해 좋은지를 정량적으로 평가하는 방식
- 여기에서 성과란 새 사이트가 목표로 했던 바에 따라 다른데, 보통은 회원 가입율, 재방문율, 구매전환율 등의 지표를 봄

#### 페이먼트 연동 관련 내용 정리

- 앱에서 가맹점 시스템으로 주문하는 플로우 (스마트 오더링, 예. 스타벅스 등)
  - 가맹점 / 메뉴 선택
  - 주문하기
  - 주문 내용 전달 --> 가맹점 시스템
  - 주문 내용 전달에 대한 응답
  - 주문 정보 업데이트
  - 가맹점 시스템으로부터 정보 전달 받음 (예. 주문 접수 / 대기열 / 등등)
  - 주문 정보 업데이트
  - 주문 확인 사항 사용자에게 전달
  - 주문한 음식 또는 물건의 제조의 완료
  - 제조완료 정보 전달
  - 주문 정보 업데이트
  - 주문한 것에 대한 제조가 완료되었음을 사용자에게 표시
  - 주문한 물건 또는 음식을 픽업
- PG 사 연동 시 결제 처리 흐름
  - 결제 준비
  - 결제 준비 요청에 대한 응답
  - 결제 승인
  - 결제 승인 요청에 대한 응답
  - 아래는 결제 취소 건에 대한 흐름
    - 결제 취소 요청
    - 결제 취소 요청에 대한 거래 결과 응답
    - 기타 정보 (정산 정보, 영수증 정보 조회 및 응답 처리)
   
#### PG, VAN 사 개념 정리

- 온라인이든 오프라인이든 상점, 카드사, 금융기관이 서로 결제 정보를 주고 받을 망이 필요
- 오프라인 결제의 핵심, Value Added Network Van은 카드사와 상점의 통신을 연결하는 부가가치통신망이라 보면 됨
  - 오프라인 상점에서 입력한 고객의 결제 데이터를 카드사로 안전하게 보내주는 역할
  - 결제 정보를 주고 받는 일종의 파이프 역할
  - 업장에서 계산할 때 사용하는 카드 단말기 / 포스 단말기 모두 VAN 기반
  - 오프라인, 소비자 - 가맹점 - VAN (중계) - 카드사
    - 카드사는 VAN 사용료 지급 의무
    - VAN사는 중계 역할만 수행
    - 가맹점의 매출액 지급은 밴사가 관여하지 않음
    - 가맹점은 8개의 카드사로부터 매출액 각각 지급 받음(?)
  - VAN : 데이터를 안전하고 정확하게 연결해주는 역할만 함 (매출 정산 등의 추가 서비스 제공하지 않음)
    - 포스 단말기나 매출 장부 서비스 등을 사용하지 않으면 8개의 카드사에서 발생한 매출 내역을 따로따로 관리해야 함
    - VAN은 수수료가 없어서 고정비 절감 가능하나 가게 운영자의 역할이 늘어남 (8개 카드사로부터 각각 다른 날짜에 매출액을 입금받아야 함)
    - 신용카드 가맹점과 신용카드 회사 사이에서 신용카드 결제를 중계해주는 부가사업자
    - 신용카드 결제 -> 밴사 -> 신용카드사
    - KSNET / KIS정보통신 / 나이스정보통신 / KOVAN / 금융결제원 / fiserv. / DAOU데이터 / Smartro / KICC / NHN KCP / JTNet / KOCES / SPC NETWORKS.
    - VAN 사가 없다면 -> 매장마다 신용카드사별 전용 결제 단말기를 각각 설치해야 되는 상황 발생
  - PG : 온라인 결제의 핵심
    - Payments Gateway, 신용카드사와 직접 계약하기 어려운 온라인 쇼핑몰을 대신해 결제 업무를 대신해 주는 역할
    - 온라인, 소비자 - 가맹점 - PG - VAN - 카드사
    - 카드사는 가맹점에서 발생한 매출액을 PG 사에 지급
    - PG 사는 중계 역할 + 정산 역할 같이 수행
    - PG 사는 매출액을 가맹점에 지급 (PG 수수료 정산)
    - 여러 곳의 카드사와 거래를 가능하게 할 뿐 아니라 PG사와 계약한 정산일에 맞춰 한 번에 매출액을 정산해 줌
    - (이 정산 시스템은 카드사마다 매출 금액 지급일이 달라 발생할 수 있는 혼란을 없애고 현금 흐름을 쉽게 파악 가능케 함)
  - 가맹점 입장에서 VAN, PG 관련 체감할 수 있는 큰 차이점은 수수료
    - VAN 사는 가맹점 업주에게 수수료를 받지 않고 카드사로부터 수수료를 받음
    - PG 사는 PG사가 카드사에 수수료를 내고 결제를 연동하는 구조, 그리고 카드사마다 다른 매출 정산 내역을 일괄로 정산해주는 역할도 해주기 때문에 수수료가 발생
    - (즉, 밴사와 다르게 연동 구조도 다르고 제공되는 서비스가 많기에 수수료가 발생하는 것이라 이해)
    - 대표 PG 사: 토스페이먼츠 / KG이니시스 / 나이스페이먼츠 / NHN한국사이버결제
    - 온라인 결제 서비스 중에서도 VAN의 역할만 해주는 곳도 존재, 수수료를 줄일것인가, 매출 관리나 정산 업무를 강화시킬것인가에 대해 확인 후 선택 필요 

## 랜섬웨어란?

- 랜섬웨어(Ransomware)는 사용자의 파일이나 시스템에 접근하지 못하도록 잠그거나 암호화한 뒤, 이를 해제하는 대가로 금전을 요구하는 악성 소프트웨어입니다. “랜섬(Ransom)“은 몸값을 의미하며, “웨어(Ware)“는 소프트웨어를 뜻합니다. 이 악성코드는 주로 이메일 첨부파일, 악성 링크, 취약한 네트워크를 통해 감염됩니다.

## 랜섬웨어의 작동 방식
- 감염 경로
  - 피싱 이메일: 악성 파일이 첨부된 이메일을 통해 감염됩니다.
	- 악성 웹사이트: 악성 스크립트가 포함된 웹사이트 방문 시 감염될 수 있습니다.
	- 소프트웨어 취약점: 운영체제, 네트워크, 또는 프로그램의 취약점을 통해 감염됩니다.
	- USB 및 외장 장치: 감염된 USB나 외장 하드를 연결할 경우 확산될 수 있습니다.
- 시스템 및 파일 암호화
	- 랜섬웨어가 설치되면, 시스템 내의 파일(문서, 사진, 데이터 등)을 AES, RSA 등 강력한 암호화 알고리즘으로 암호화합니다.
	- 일부 랜섬웨어는 시스템 부팅 섹터를 암호화하여 운영체제 자체를 사용할 수 없게 만듭니다.
- 몸값 요구
	- 파일이나 시스템을 복구하려면 비트코인, 이더리움 등 암호화폐로 몸값을 지불하도록 요구합니다.
	- 화면에는 협박 메시지가 나타나며, 시간이 지날수록 몸값이 증가하거나 데이터가 영구 삭제될 것이라고 경고합니다.

## 랜섬웨어의 유형
	1.	암호화형 랜섬웨어 (Encrypting Ransomware)
	- 시스템의 중요한 파일을 암호화하여 접근을 막습니다.
	- 예: CryptoLocker, WannaCry
	2.	잠금형 랜섬웨어 (Locker Ransomware)
	- 컴퓨터나 디바이스 자체를 잠그고 사용하지 못하도록 만듭니다.
	- 예: WinLocker
	3.	이중 갈취 랜섬웨어
	- 데이터를 암호화할 뿐만 아니라, 이를 외부로 유출한 뒤 공개하지 않는 대가로 몸값을 요구합니다.
	- 예: Maze, REvil
	4.	서비스형 랜섬웨어 (Ransomware-as-a-Service, RaaS)
	- 랜섬웨어를 제작 및 배포하는 조직이 사용자(범죄자)에게 서비스를 제공합니다. 성공하면 수익을 나눕니다.

대표적인 랜섬웨어 사례
	1.	WannaCry (2017)
	- 전 세계 150개국 이상, 230,000개 시스템을 감염시켰습니다.
	- Windows의 SMBv1 취약점을 이용해 네트워크를 통해 확산되었습니다.
	2.	NotPetya (2017)
	- 우크라이나를 중심으로 시작된 공격으로, 파일 암호화보다는 데이터 파괴가 주요 목표였습니다.
	3.	CryptoLocker (2013)
	- 최초로 암호화폐를 대가로 요구한 랜섬웨어 중 하나입니다.

랜섬웨어의 피해
	1.	경제적 손실
	- 몸값 지불 비용.
	- 시스템 복구 및 운영 중단으로 인한 손실.
	2.	데이터 손실
	- 암호화된 데이터를 복구하지 못할 경우 영구적으로 손실됩니다.
	3.	평판 손상
	- 데이터 유출로 인해 기업의 신뢰도가 하락할 수 있습니다.
	4.	법적 문제
	- 개인정보 보호법이나 규정을 위반한 경우 벌금이 부과될 수 있습니다.

랜섬웨어 예방 방법
	1.	백업
	- 중요 데이터를 정기적으로 외장 하드나 클라우드에 백업합니다.
	- 백업 데이터를 네트워크와 분리하여 보관합니다.
	2.	보안 소프트웨어
	- 최신 안티바이러스 및 안티랜섬웨어 소프트웨어를 설치합니다.
	3.	시스템 업데이트
	- 운영체제, 소프트웨어, 드라이버를 최신 버전으로 유지합니다.
	- 특히, 알려진 취약점을 패치합니다.
	4.	이메일 및 인터넷 사용 주의
	- 의심스러운 이메일 첨부파일이나 링크는 절대 열지 않습니다.
	- 신뢰할 수 없는 웹사이트를 방문하지 않습니다.
	5.	네트워크 보안 강화
	- 방화벽과 VPN을 활용하여 네트워크를 보호합니다.
	- 중요 시스템에 다중 인증(MFA)을 적용합니다.
	6.	교육 및 훈련
	- 직원들에게 랜섬웨어와 사이버 보안에 대한 교육을 실시합니다.

감염 시 대처 방법
	1.	즉각적인 네트워크 분리
	- 감염된 시스템을 네트워크에서 분리하여 확산을 방지합니다.
	2.	보안 전문가와 상담
	- 전문 보안 팀이나 랜섬웨어 복구 전문 회사에 도움을 요청합니다.
	3.	복구 시도
	- 백업 데이터를 활용하거나, 보안 커뮤니티에서 제공하는 복호화 툴을 사용합니다.
(예: No More Ransom 프로젝트)
	4.	몸값 지불 자제
	- 공격자에게 몸값을 지불해도 데이터를 복구하지 못할 가능성이 큽니다.
	- 지불은 추가적인 공격을 유발할 수 있습니다.

랜섬웨어는 개인과 기업 모두에게 심각한 위협이 될 수 있으므로 예방과 신속한 대응이 필수적입니다. 꾸준히 보안 상태를 점검하고, 위기 상황에 대비하는 것이 중요합니다.

스타벅스와 같은 대형 브랜드의 앱에서 “카드 등록”과 “결제 정산”이 이루어지는 방식은 다음과 같은 구조를 통해 작동합니다. 이를 이해하려면 결제 구조, 사업자 간의 관계, 정산 방식에 대해 살펴봐야 합니다.

1. 카드 등록 기능의 구조

앱에서 카드 등록 기능은 보통 **PG사(Payment Gateway)**와 연동되어 작동합니다. 주요 특징은 다음과 같습니다:
	- 공통 카드 등록
	- 사용자가 등록한 카드는 앱에 저장되지 않고 PG사 또는 VAN사(결제 대행사)에서 토큰화(Tokenization) 과정을 통해 관리됩니다.
	- 앱은 이 토큰화된 정보를 활용하여 결제를 진행하며, 카드 정보를 직접 보유하지 않습니다.
	- 이 방식은 보안성과 편리성을 동시에 제공하며, 사용자 입장에서 매장에 상관없이 동일한 결제 수단을 사용할 수 있도록 합니다.

2. 매장별 사업자 구조

스타벅스와 같은 대형 브랜드에서 매장별 사업자가 다를 수 있는 이유는 다음과 같습니다:
	- 프랜차이즈 구조
	- 매장은 각기 다른 프랜차이즈 사업자(가맹점) 소유일 수 있습니다.
	- 예를 들어, 스타벅스 매장 A는 사업자 A, 매장 B는 사업자 B로 등록될 수 있습니다.
	- 직영점 구조
	- 일부 매장은 본사가 직접 운영할 수 있으며, 사업자가 하나로 통합될 수도 있습니다.
	- 그러나 많은 경우, 프랜차이즈 가맹점 방식으로 운영됩니다.

3. 결제와 정산의 흐름

사용자가 카드 등록 후 특정 매장에서 결제할 때, 결제와 정산은 다음 단계로 이루어집니다:

1) 결제 요청
	- 사용자가 앱에서 결제 버튼을 누르면, 앱은 PG사에 결제 요청을 보냅니다.
	- PG사는 카드 정보를 토큰화된 데이터로 전달받아 카드사와의 결제를 처리합니다.

2) 매장 정보 전송
	- 결제 요청에는 **매장의 고유 식별자(사업자 정보)**가 포함됩니다.
	- 매장 ID, 사업자 등록 번호 등이 PG사로 함께 전달됩니다.
	- 이 정보를 통해 PG사는 어느 매장(사업자)에서 결제가 이루어졌는지 식별합니다.

3) 결제 승인 및 완료
	- PG사는 카드사로부터 결제 승인을 받아내고, 매장의 사업자 계좌로 결제 금액을 전달할 준비를 합니다.

4) 정산
	- PG사는 매출 데이터를 매장별로 분리하여 각 사업자에게 정산합니다.
	- 예를 들어, 매장 A에서 발생한 결제는 사업자 A 계좌로, 매장 B에서 발생한 결제는 사업자 B 계좌로 입금됩니다.
	- PG사가 결제 수수료를 공제한 후 각 사업자에게 송금합니다.

4. 정산 방식의 세부 구조

매장별 사업자 정보가 다르더라도, 결제와 정산이 가능한 이유는 PG사가 모든 결제 흐름을 중앙에서 관리하기 때문입니다.

예시
	1.	사용자가 매장 A에서 5,000원을 결제하면:
	- 사업자 A의 PG 계정으로 매출이 기록됩니다.
	- PG사가 사업자 A의 계좌로 정산금을 송금합니다.
	2.	사용자가 매장 B에서 7,000원을 결제하면:
	- 사업자 B의 PG 계정으로 매출이 기록됩니다.
	- PG사가 사업자 B의 계좌로 정산금을 송금합니다.

이 과정에서 PG사가 매출 정산 데이터를 정확히 관리하기 때문에, 사용자는 같은 앱과 카드를 사용하더라도 매장별 사업자가 다르게 정산됩니다.

5. 스타벅스의 사례

스타벅스의 경우, 대부분의 매장은 직영점으로 운영되기 때문에 사업자 정보가 통합되어 있을 가능성이 높습니다.
	- 스타벅스 전용 결제 시스템
	- 스타벅스는 자체 충전식 카드 및 앱 내 결제를 제공하며, 이는 본사가 중앙에서 통합 관리합니다.
	- 충전된 금액은 “선불”로 본사 계정에 저장되며, 매장에서 결제 시 본사가 각 매장으로 내부 정산합니다.

6. 결론

앱에서 카드 등록과 매장별 결제 및 정산은 PG사의 중앙 집중화된 결제 시스템을 통해 이루어집니다. 매장별로 사업자가 달라도, PG사는 매장 ID 및 사업자 정보를 활용하여 정확히 정산합니다. 스타벅스와 같은 경우, 자체 결제 시스템이 더해져 보다 효율적인 정산 체계를 구축할 수 있습니다.


객체 간의 데이터 보호를 위한 정보은닉(Information Hiding) 
정보 은닉(Information Hiding) 개요

**정보 은닉(Information Hiding)**은 객체지향 프로그래밍(OOP)의 중요한 설계 원칙 중 하나로, 객체의 내부 데이터와 구현 세부사항을 외부에서 접근하지 못하도록 제한하여 시스템의 복잡성을 줄이고 유지보수성을 향상시키는 기술입니다. 이는 캡슐화(encapsulation)의 하위 개념으로 간주되며, 클래스 설계 시 필수적으로 고려되어야 하는 요소입니다.

1. 정보 은닉의 정의 및 원리
	1.	정의
	- 정보 은닉이란 객체 내부의 데이터 및 메서드를 외부에서 직접 접근하지 못하도록 보호하고, 객체 외부에는 필요한 정보만을 제공하는 설계 기법입니다.
	- 객체는 공개 인터페이스(public method)를 통해서만 데이터를 조작하거나 동작을 수행하도록 설계됩니다.
	2.	원리
	- 객체의 내부 구현 세부사항은 외부에서 알 수 없도록 감춥니다.
	- 외부에서는 객체의 동작에 필요한 **공개된 인터페이스(public API)**만 사용합니다.
	- 데이터와 행위를 밀접하게 결합하여, 외부에서의 직접적인 접근 및 수정 가능성을 차단합니다.

2. 정보 은닉의 주요 목적
	1.	데이터 보호
	- 객체 내부 데이터에 대한 부적절한 접근 및 수정 방지.
	- 데이터의 무결성과 일관성을 유지.
	2.	모듈화 향상
	- 객체 간 결합도를 낮추어 시스템 모듈 간의 독립성을 강화.
	3.	유지보수성 증대
	- 내부 구현 변경 시 외부 코드에 영향을 주지 않음으로써 수정 및 확장 용이.
	4.	보안성 강화
	- 민감한 정보가 외부로 노출되지 않도록 설계.
	5.	재사용성 증대
	- 객체의 내부 구현에 의존하지 않는 코드 작성이 가능하여 재사용성이 높아짐.

3. 정보 은닉을 구현하는 방법
	1.	접근 제어자 활용
	- private: 클래스 내부에서만 접근 가능하도록 제한.
	- protected: 상속받은 클래스 및 동일 패키지 내에서 접근 가능.
	- public: 모든 클래스에서 접근 가능.
	- default(package-private): 동일 패키지 내에서 접근 가능.
	2.	Getter와 Setter 메서드 사용
	- 데이터를 직접 노출하지 않고, 간접적으로 접근 및 수정하도록 구현.
	- 데이터 검증, 로깅 등 추가 로직을 삽입할 수 있음.

public class Account {
    private double balance;

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        if (balance >= 0) {
            this.balance = balance;
        }
    }
}


	3.	인터페이스 설계
	- 공개된 인터페이스를 통해 외부와의 상호작용을 제한하고 내부 구현은 감춤.
	- 인터페이스 변경이 최소화되므로 유지보수가 용이.
	4.	불변 객체(Immutable Object) 설계
	- 데이터를 변경할 수 없는 객체로 설계하여 불필요한 접근 및 수정 차단.

public final class ImmutableUser {
    private final String name;

    public ImmutableUser(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

4. 정보 은닉의 장점
	1.	캡슐화 강화
	- 객체의 데이터와 행위를 하나의 단위로 묶어 외부와의 상호작용을 최소화.
	2.	변경 용이성
	- 내부 구현 변경이 외부 코드에 영향을 미치지 않으므로 유지보수가 간편.
	3.	디버깅 및 테스트 용이성
	- 데이터를 관리하는 책임을 객체 내부로 제한하여 디버깅 및 오류 원인 파악이 쉬움.
	4.	시스템 안정성
	- 외부의 잘못된 접근 및 변경으로 인한 시스템 오류를 방지.
	5.	보안 강화
	- 민감한 데이터가 외부로 노출되지 않아 정보 유출 위험 감소.

5. 정보 은닉 적용 사례
	1.	Java의 접근 제어자
	- private, protected, public 키워드를 활용하여 클래스 멤버의 접근 범위를 제어.
	2.	Spring Framework
	- DAO(Data Access Object) 클래스에서 데이터 접근 로직은 감추고 서비스 계층을 통해서만 접근.
	3.	안드로이드 개발
	- ViewModel을 활용하여 UI 데이터를 은닉하고, Activity/Fragment는 관찰(Observer)만 수행.
	4.	데이터베이스 접근 계층
	- 데이터베이스 연결 정보는 외부에 노출되지 않도록 캡슐화하며, 오직 쿼리 실행 API를 통해서만 접근 가능.

6. 정보 은닉의 한계와 주의사항
	1.	설계 복잡도 증가
	- 모든 데이터를 감추고 Getter/Setter를 구현하는 것이 필수는 아니며, 과도한 정보 은닉은 오히려 코드 복잡도를 높일 수 있음.
	2.	퍼포먼스 영향
	- 불필요한 Getter/Setter 메서드 호출이 많아지면 성능에 영향을 줄 수 있음.
	3.	의존성 문제
	- 너무 강하게 은닉할 경우, 객체 간 협력이 필요한 기능 설계가 어려워질 수 있음.

결론

정보 은닉은 객체지향 설계의 핵심 원칙으로, 데이터 보호와 시스템 안정성을 보장하는 데 중요한 역할을 합니다. 그러나 설계의 복잡도를 고려하여 적절한 수준에서 은닉을 적용해야 하며, 객체 간의 협력과 성능을 저해하지 않도록 유연한 설계가 필요합니다.


동적계획법 (Dynamic Programming, DP)

1. 정의 (What)

동적계획법은 복잡한 문제를 작은 하위 문제들로 나누어 해결하고, 그 결과를 저장하여 중복 계산을 방지하는 최적화 알고리즘 기법이다. 문제를 최적 부분 구조(Optimal Substructure)와 중복되는 하위 문제(Overlapping Subproblems)로 나눌 수 있을 때 효과적으로 사용된다.

2. 원리 및 특징 (How)
	1.	분할과 정복 (Divide and Conquer)
	- 문제를 더 작은 하위 문제로 나누고, 이를 해결한 결과를 조합하여 원래 문제를 해결한다.
	- 모든 하위 문제를 독립적으로 해결하는 분할정복과는 달리, 하위 문제의 결과를 재사용한다.
	2.	최적 부분 구조 (Optimal Substructure)
	- 문제의 최적해가 하위 문제들의 최적해로 구성될 수 있어야 한다.
	3.	메모이제이션 (Memoization)
	- 재귀적으로 문제를 해결하며, 이미 계산된 하위 문제의 결과를 저장해 중복 계산을 방지한다. (Top-Down 방식)
	4.	테이블 작성 (Tabulation)
	- 작은 문제부터 해결해 나가며, 테이블에 결과를 저장하여 상위 문제를 해결한다. (Bottom-Up 방식)

3. 장점 (Why)
	1.	성능 최적화
	- 중복 계산을 줄이기 때문에 시간 복잡도가 획기적으로 개선된다.
예: 피보나치 수열 계산에서 O(2^N) → O(N)으로 감소
	2.	다양한 문제 해결
	- 경로 최적화, 문자열 문제, 그래프 문제 등 다양한 문제에 적용 가능하다.
	3.	구현 용이성
	- 메모이제이션과 테이블 작성 방식 모두 비교적 간단한 구현이 가능하다.

4. 단점 및 한계
	1.	공간 복잡도 문제
	- 테이블 또는 캐시를 저장하기 위한 메모리가 많이 필요할 수 있다.
	2.	문제 특성 제한
	- 최적 부분 구조와 중복되는 하위 문제를 만족하지 않는 경우 사용할 수 없다.

5. 주요 적용 사례
	1.	피보나치 수열
	- 재귀 호출 중복 문제를 해결하기 위한 대표적인 예제.
	2.	최장 공통 부분 문자열 (Longest Common Subsequence, LCS)
	- 두 문자열의 공통 부분 문자열 길이를 구하는 문제.
	3.	최단 경로 문제 (Shortest Path Problem)
	- 다익스트라 알고리즘, 플로이드-워셜 알고리즘에서 활용.
	4.	배낭 문제 (Knapsack Problem)
	- 제한된 무게에서 최대 가치를 찾는 최적화 문제.

6. 사례 코드

# 피보나치 수열 동적계획법 (Bottom-Up)
def fibonacci(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fibonacci(10))  # 출력: 55

7. 결론 (핵심 요약)

동적계획법은 하위 문제의 결과를 저장하여 계산 효율성을 높이는 강력한 알고리즘 기법으로, 최적화 문제를 해결하는 데 유용하다. 최적 부분 구조와 중복되는 하위 문제를 만족하는 문제에서 활용 가능하며, 성능 및 코드 효율성을 크게 향상시킨다.

#### 미정리 스터디 내용

- 2023/03/08
  HTML로 구조를 잡고 CSS 로 스타일을 적용하고 클릭 등의 동적 이벤트는 자바스크립트로 처리한다.
  이 전체를 제품이라고 함 (웹앱, 어플리케이션).
  우리는 웹의 표준을 배우는 것, 누가 제정하는가? W3C
  브라우저 벤더 -> 제정된 웹표준을 근거해서 브라우저를 제작.
- 리액트
  - 페이지 상호작용
  - 전통적인 웹 구현 방식 (HTML 요청 -> 서버로부터 HTML 수집)
  - 리액트란 무엇인가?
  - 왜 자바스크립트 대신 리액트를 사용하는가?
  - 리액트 구동되는 메커니즘
  - 리액트 선택 장점
    - 코드의 양
    - 명령형 프로그래밍 X
    - 복잡한 인터페이스 구현에 적합, 선언형 컴포넌트 (컴포넌트 기반)
    - 싱글 페이지 어플리케이션 (서버는 오직 하나의 HTML 만을 전달한다.)
    - 추가적인 기능이 필요한 경우 외부 라이브러리 설치 필요
  - 프레임워크 / 라이브러리 차이점
    - 앵귤러 - 처음부터 타입스크립트 수용 / 컴포넌트 중심 / 기능 많음
    - 뷰 - 컴포넌트 기반, 기능은 리액트보다는 많음
    - 리액트, 앵귤러, 뷰 간의 차이 / 선택 기준은 무엇인가?
  - props, state, 컴포넌트 스타일링, 리액트 훅, Refs, Context API, 리덕스
  - 데이터베이스, HTTP, 라우팅, 배포 방법, 넥스트 JS
  - 모던 자바스크립트
  - 비주얼 스튜디오 코드
  - let, const
  - 화살표 함수 (키워드 this 이슈)
  - Export / Import Modules (default, as, \*) / Named Import
  - Class, Property, Method (클래스와 화살표 함수 간의 관계)
  - 연산자
    - Spread 연산자 (배열의 원소를 펼칠 때, 클래스 안에서 … 사용법)
    - 레스트 연산자 (함수에서 사용, filter 연산)
  - Destructuring
  - 객체와 배열은 참조형 자료 타입, 재할당한다면 값이 아닌 포인터를 복사하는 것, 자체를 복사하고 싶으면 즉, 진짜로 복사하고 싶다면 프로퍼티를 복사해야 한다.
  - 자바스크립트 ES6, 7 등 버전에 따른 차이점
  - 배열함수 (map)
  - 모질라 자바스크립트 네트워크에서 추가 설명
  - JSX, Component Usage, Data Handling
  - 리액트는 컴포넌트에 대한 모든 것 (리액트 = 컴포넌트)
  - 왜 컴포넌트인가 ? : 재사용성, 관심사 분리 OOP 적 완성을 위한 목적
  - 커스텀 HTML Element 구성 => 리액트
  - 앱 설치 및 실행에 필요한 요소들
    - Node.js (자바 스크립트 런타임)
    - npm, yarn install
  - index.js, index.html (div id="root")
  - JSX: 작성 용이, 브라우저에서 해석 가능, 화면 뒷단에서 변경 (개발자 도구 (크롬))
  - 기본적으로 커스텀 HTML 요소
  - 관례: 첫단어 대문자, 카멜 케이스 적용
  - 가독성을 위해 괄호로 태그를 묶는다. (return (div…div))
  - text 태그없이 div 내에 텍스트 작성 가능 (경고 메세지 제거 위한 목적)
  - 다른 컨텐츠 주변에서 셀 역할을 하는 컴포넌트를 생성하고 싶다면 ?
    - 각각의 컨텐츠들에서 공통적인 속성을 묶을 때 컴포지션 children prop 사용
    - 재사용 가능한 래퍼 컴포넌트를 만들기 위한 목적
    - 클래스네임 중첩
    - 컴포넌트를 결합할 때 마다 컴포지션 개념을 사용
  - 내부적으로 JSX 문법은 아래와 같이 변환된다.
    - React.createElement() <-- 세가지 인자 필요 (태그 이름, 속성 객체, 컨텐츠 컴포넌트 정보)
    - React.createElement('div', {}, React.createElement('h2', {}, "TEST"), React.createElement(Object, {items: objItems})
  - function 스타일 --> 대체 함수 문법 (화살표 함수)
  - 관례적인 함수 작명법
  - useState
    - 사전 지식
      - 컴포넌트는 JSX 를 반환하는 함수형이므로 누군가는 호출을 해줘야 한다.
      - JSX 는 함수 불러오기의 나열 / 모든 것은 index.js 에서 부터 시작
      - 기본적으로 리액트는 화면 렌더링을 반복하지 않는다.
      - 그러므로 리액트에게 어떤 것이 변경되었고 특정 컴포넌트가 업데이트 되어야 한다고 알려줘야 함.
    - 컴포넌트 함수 바깥 및 중첩된 함수 내에서는 동작하지 않음
    - 배열을 반환
    - 컴포넌트 함수는 useState 를 업데이트하는 함수, useState를 초기화했던 부분에서 다시 시작된다. (set을 할 경우)
    - setXXX 는 리액트에게 상태를 변경하고 싶다고 알리고 useState 에게 state가 등록된 컴포넌트가 업데이트 되어야 한다고 리액트에게 알린다.
    - setXXX 는 바로 값을 변경하지 않고 대신 이 state의 업데이트를 예약한다. (그래서 다음 라인에서 로그 출력 시도를 해도 값이 그대로임)
    - State 는 컴포넌트 인스턴트 별로 나뉘어져 있음.
    - 가장 최근에 설정된 값을 항상 보여준다.
    - 여러가지 상태를 업데이트하는 경우 객체로서 업데이트도 가능
    - 이전 상태에 의존하는 상태 업데이트 (ex. setUserInput((prevState) => { return { ...prevState, enteredName: event.name}) <-- 스냅샷 이용 방법 권장
  - 입력창 처리 : form 태그 (label, input 태그)
    - onChange (event 객체, event.target.value)
    - form 태그 onSubmit (button type 이 'submit')
    - 기본적으로 서브밋을 하면 웹페이지가 갱신된다. (event.preventDefault())
    - input 태그의 value 속성
  - 부모 <-> 자식 컴포넌트 간 통신 방법
  - Lifting State Up (자식 --> 부모 --> 다른 자식)
  - select 태그 (option 태그)
  - 컴포넌트 용어 (참고)
    - 프레젠테이셔널 / 덤프 컴포넌트 / 무상태 컴포넌트
    - 스마트 / 상태 유지 컴포넌트
  - {} 와 배열 map() 활용한 동적 리스트 구성
  - 아이템 keys 이해 --> 리액트가 모든 아이템을 정확하게 인식할 수 있게 하기 위한 목적
  - 배열 filter 연산 (props.items.filter(item => { return item.date.getFullYear().toString() === filteredYear})
  - JSX 구문 복잡성을 줄이고 컴포넌트 함수 상단에서 연산을 처리하는 방향으로 코딩
  - 조건부 내용 출력 건 => && 연산 뒤의 내용이 출력되므로 이를 활용 가능
  - JSX 코드를 변수에 저장하는 것 가능
  - ul, li 태그
  - 동적 스타일 추가
    - 동적 스타일 추가 (style): style={{}}
    - 동적 스타일 추가 백틱 문자열 기호 사용한 클래스 네임
    - 패키지: styled components
    - ex. const Button = styled.button``
    - & input:focus, & label
    - props 사용한 동적 스타일 구성 (\$와 {}활용)
    - 미디어 쿼리 @media
    - CSS 모듈: Button.module.css 등
  - Users -> src -> 원본소스 확인 -> 브레이크 포인트 설정
  - DevTools (Chrome Extension)
  - label 태그: htmlFor
  - form 태그 onSubmit (기본 동작은 누르면 웹페이지가 갱신됨)
  - import classes from './Xxx.module.css'
  - 자바스크립트 파일이 아닌 경우에는 Import 시 확장자 작성 필요
  - Fallback 처리: type={props.type || 'button'} <- 전달된 타입이 없는 경우에 대한 Fallback 처리
- 자바스크립트
  - 데이터 타입을 자동으로 유추
  - 동적 해석 프로그래밍 언어
  - 동적 작업을 위해 필요
  - 브라우저 내에 자바스크립트 엔진 존재 -> 자바스크립트 실행 가능
  - 자바스크립트는 로컬 파일 시스템은 접근 불가
  - 구글 자바스크립트 엔진 V8
  - NodeJs
    - Node.js (웹 백엔드 / 서버 구축)
    - Node.js 는 컴퓨터에서 직접 실행되기 때문에 파일 시스템 접근 가능
  - DOM (Document Object Model)
  - OOP, Class, Constructor, Prototypes
  - 비동기 처리, Ajax, 브라우저 API
  - 코드 분할
  - 웹팩, Babel, 브라우저 스토리지
  - 자바스크립트 프레임워크
  - 메타 프로그래밍
  - 코드 보안, 성능 최적화, 메모리 누수 방지
  - 자바스크립트 vs 자바 (브라우저에서 직접 지원 X)
  - LiveScript / JavaScript / ECMAScript / ActionScript / jScript
  - 구글 크롬 (개발자 도구) + 비주얼 스튜디오 코드
  - VSCODE: Preferences - Settings - (.vscode) - ex. prettier (코드 포맷팅 수정)
  - 기본 세팅: 자동 세미콜론 + 탭 2칸 + 싱글 따옴표 (Quote)
  - 확장 프로그램 영향 줄이기 위해서는 개발 시 시크릿 모드 권장
  - script src="assets/app.js"
  - 페이지 로드 완료된 이 후 무엇인가를 처리하려면?
  - Case Sensitive / Camel Case Format
  - Snake Case is NOT recommended.
  - "+ - \* / % \*\*"
  - 백틱 문자 (\$ 사용 가능, 코틀린과 유사), 쌍따옴표 내 싱글 따옴표
  - 템플릿 리터럴
  - Arrow Function: 코드 양 줄일 수 있고 다양한 형태로 작성 가능
    - const add = (a, b) => a + b;
  - 기본값 함수 매개변수 (const add = (a, b = 2) => a + b;)
- 타입 스크립트
  - 프로그래밍 언어 / 도구
  - 브라우저는 타입스크립트를 실행할 수 없다.
  - 타입 추가 / 브라우저 런타임에서 에러 발생 전 코드의 에러를 미리 식별 가능, 에러가 적은 코드 작성 가능
  - 숫자 연산, 문자열 연결 예제가 대표적인 자바스크립트, 타입스크립트 차이점 예제
  - +number1 + +number2 / typeof === "number"
  - 설치 : npm install -g typescript
  - 타입스크립트 컴파일 방법: tsc xxx.ts -> xxx.js 파일 생성됨
  - 데코레이터, 제네릭, 클래스, 인터페이스
  - 네임 스페이스, 모듈
  - 웹팩 (Webpack): 프론트엔드 웹 개발 시 사용하는 구축 도구
  - VsCode Plugins: Prettier (format document - shortcut), EsLint, Path Intellisense, Material Icon, TSLint
  - lite-server (localhost:3000)
  - node_modules: 타사 패키지와 종속성을 모두 저장하는 폴더
  - Extra Sanity Check
  - 정적 타입, 런타임 중에 변수와 매개변수가 변하지 않음.
  - 타입 추론 (자바스크립트, 타입스크립트)
  - let result = "Result.." / result = 0 (에러) <--- 문자열로 추론
  - 클래스: const person: { name: string; age: number } = { name='', age: 30}
  - any 타입
  - Tuple
    - Tuple 타입, Fixed length array.
    - Tuple 타입, Push 기능 관련 이슈
  - Enum 타입 - Enum 왜 사용하는지에 대한 근본적인 질문
  - 문자열보다 숫자를 사용하면 메모리 점유와 코드 양 줄일 수 있음.
  - enum CustomEnum { TEST1, TEST2, TEST3 } / CustomEnum.TEST1
  - 유니언 타입 (예. number | string -> if (typeof input1 === ''number))
    - 런타임 체크 필요한 경우 발생
  - result: 'as-number' | 'as-text' 리터럴 타입
  - 커스텀 유니언 타입: type 으로 정의. 예. type customType = number | string
    - 불필요한 반복 지양, 타입 중심 관리 가능
  - undefined, unknown
  - 컴파일
    - 소스 맵 (크롬 - 개발자도구) : 브라우저와 개발자 도구 간의 다리 역할 sourceMap: true (tsconfig.json)
    - rootDir / outDir (ex. outDir: ./dist, rootDir: ./src)
    - dist
    - remoteComments: true (주석 제거)
    - noEmit: true (산출물 만들지 않기), noEmitOnError (에러 발생 시에는 .js 파일 생성하지 않음)
    - strict, strictNullCheck, Dom의 버튼 객체를 예로 듬. 또는 if (button) xxx
    - strictBindCallApply, ex. clickHandler.bind(null)
    - Debugger for chrome 플러그인 (VsCode) - sourceMap 활성화 필요, launche.json
  - let 과 var 의 변수 유효 범위 ({} 내 var 변수는 {} 바깥에서 참조가능)
  - Arrow Function:
    - const printOutput: (a: number | string) => void = output => console.log(output);
    - if (button) button.addEventListener('click', event => console.log(event));
  - 스프레드 연산자
    - 배열의 푸쉬 동작 원리
    - ex. xxx.push(...bases)
    - ex. const person = { name: "xxx", age: 33 }; const copied = { ...person };
- 공통
  - 프론트엔드 개발: HTML, CSS, JS를 사용해 데이터를 그래픽 사용자 인터페이스로 변환하고 그것으로 사용자와 상호 작용할 수 있도록 하는 것.
    - 웹페이지를 만들어서 사용자에게 보여주는 것. (백엔드 --> 컴퓨터 (크롬, 엣지, 사파리 등) --> (프론트엔드, 앞단 (사용자의)) --> 사용자)
    - (참고) 비즈니스 로직: 웹사이트가 동작하는 데 필요한 핵심 데이터 처리를 수행하는 알고리즘.
    - 풀스택 개발: GUI 프론트엔드부터 데이터베이스 백엔드 등 모든 소프트웨어 스택을 개발하는 것.
    - HTML: 페이지의 제목, 문단, 표, 이미지, 동영상 등 웹의 구조를 담당 (핵심: 구조 구성)
      - Hyper Text Markup Language
    - HTML (기획자), CSS (디자이너), JS (개발자)
    - CSS (Cascading Style Sheet): 실제 화면에 표시되는 방법 (색상, 크기, 폰트, 레이아웃 등)을 지정해 콘텐츠를 꾸며주는 시각적인 표현(정적)을 담당 (핵심: 스타일)
    - JS: 콘텐츠를 바꾸고 움직이는 등 페이지를 동작시키는 동적 처리 담당. (핵심: 동적 처리)
      - 제작된 웹 사이트(웹 어플리케이션, 웹앱)를 제품(Product)이라고 부르기도 한다.
    - HTML + CSS: 레이아웃을 중심으로 사고 / JS: 데이터를 중심으로 사고
  - 테스트 TDD
  - 하이퍼텍스트: 참조를 통해 (링크를 통해) 현재 페이지에서 다른 문서로 즉시 접근(이동)할 수 있는 텍스트
  - 통신 프로토콜, 통신 규약은 컴퓨터나 원거리 통신 장비 사이에서 메세지를 주고 받는 양식 / 규칙의 체계를 의미 (대표적: HTTP, HTTPS, FTP, SSL)
  - 웹앱 동작 원리
    - 사용자 컴퓨터(브라우저) --> 페이지 주소 작성 --> (Request) --> 서버 --> 최초 응답(Response HTML) --> 사용자 브라우저 --> 추가 요청 --> 서버 --> 추가 응답 (CSS, JS, JPG..)
      - 필요 시 추가 요청이 이루어지고 해당 정보들을 응답받는다.
  - 웹 표준, 브라우저
    - 웹 표준: 웹에서 사용되는 표준 기술 / 규칙, W3C의 죠준화 제정 단계의 권고안(REC)에 해당하는 기술
      - 표준화 제정 단계 4가지
        - 초안, Working Draft, WD
        - 후보권고안, Candidate Recommendation, CR
        - 제안권고안, Proposed Recommendation, PR
        - 권고안, W3C Recommendation, REC
  - 크로스 브라우징: 조금은 다르게 구동되는 여러 브라우저에서, 동일한 사용자 경험 (같은 화면, 동작 등)을 줄 수 있도록 제작하는 기술, 방법
  - 2020. 08 부터는 익스플로러는 지원 X <-- 웹 표준을 따르지 않고 있는 것들이 많았다.
  - 뷰 포트 (Viewport): 하나의 웹페이지가 출력 (렌더링) 되는 영역,
    - 렌더링: 브라우저의 뷰 포트에 웹 사이트를 출력하는 행위.
  - 오픈 소스 라이센스
    - 라이센스: 저작권과 관계
    - 오픈소스: 어떤 제품을 개발하는 과정에 필요한 소스 코드나 설계도를 누구나 접근해서 열람할 수 있도록 공개하는 것.
      - 아파치: 개인/상업적, 배포 수정, 특허 신청 가능
      - MIT: 매사추세츠공과대학, 소스에 명시만 해주면 됨 (프로젝트 소스 코드에 외부에서 가져온 오픈 소스의 라이센스 내용만 정확히 명시하면 충분, 대부분 자동으로 오픈소스가 같이 빌드되기 때문에 따로 관리할 필요는 없음)
      - BSD: 버클리 캘리포니아대학, MIT 와 동일
      - Beerware
  - 테스트
    - Mockito
    - 테스트 고전파, 런던파
  - 웹접근성, 렌더링 퍼포먼스 개선
  - 이슈 발생 시 이슈 발생 지점 추측 방법
  - SSR, CSR 환경
  - PHP 단점 / 장점 (프레임워크)
  - Cypress 라이브러리
  - Redis / MemCache / EhCache
  - EC2 서버, RDS, SQS
  - 트래픽 처리는 어떻게 하는가?
  - 멀티 마스터?, DB Write IO 임계치 초과했을 때 어떻게 처리하는가?
  - 레플리카 DB - 조회 서비스
  - 사용자 트랜잭션이 자주 일어나는 서비스 동작 / 상황 대처 방법
  - 정부과제 - 연구내용/노트
  - TF (Team Fortress)
  - 경력 정리
    - 나는 무슨 개발자인가? 주 도메인과 서브 도메인은 무엇인가?
    - 경험: 회사, 기간, 주력 포지션, 대표 구현 서비스, 경험 내용
    - 역량: 기여 주요 역할 / 상세한 기여 내용
    - 업무 진행 사용 기술 (언어, 프레임워크, 라이브러리, 플랫폼)
    - Confluence, Blog, Github 활용
    - 업무 프로젝트 (프로젝트 진행 이유 / 요구사항 + 기술 + 애로사항 극복 내용 + 유지보수 내용)
    - 교육 사이트 활용 → 교육 이후 Confluence / Blog에 정리하고 세미나 자료를 만드는 것이 효과적.
    - 작성한 문서의 카테고리화
    - 도서 / 기사 글
    - 협업 중 일어난 상황 정리 / 학습 중 발생한 어려움 / 이슈 처리 중 어려움
  - SaaS (Software as a Service, Saas)
  - Jenkins / SpringBatch
  - 기술 블로그
  - Ruby, Rails, ORM, N+1, fetchJoin, persistence context (Java)
  - Equals, HashCode, Generic, RDBMS Index
  - Three.js
  - 로그인 기능 / 페이지 구현, 사용자 구분은 어떻게 하는가? (세션 관리법)
  - 쉘 스크립트 배포 스크립트, 무중단 배포환경, 리턴문 차이점
  - JPA N+1, fetchJoin, 실제 쿼리 결과물
  - 레퍼런스 타입, 원시 타입 차이 / 특징
  - 단방향, 양방향 바인딩
  - 쿠키가 HTTP 어느 파트에 있는가?
  - 네트워크 예외처리 방법
  - 헤더, 바디에 대한 내용
  - 장애상황 대처 (화면이 안뜰때 확인할 수 있는 포인트, JS 다운로드가 느릴때 확인 포인트)
- VsCode
  - Shift + CMD + P : All Command (모든 명령 표시)
  - CMD + O (File - Open)
  - Purple Status Bar --> Project Init --> Blue Status Bar
  - ! --> tab or enter --> html standard code generation.
  - Korean Plugin (Option)
  - OPT + Shift + F
  - CMD + K -> F (원하는 영역만 코드 정리)
  - Auto Rename Tag Plugin (태그 이름 자동 수정 플러그인)
  - 탭 우측에 흰색 아이콘은 현재 수정 후 저장이 되지 않은 상태임을 뜻함.
  - CMD + OPT + S : 모두 저장
  - Live Server Plugin: HTML 파일에서 'Open With Live Server' 로 HTML 내용 확인 가능
    - 라이브 서버는 개발을 위해 임시로 로컬 서버를 오픈하는 것. 나중에 실제 제품은 실제 호스팅 즉, 사용자들이 접근 가능한 서버에 업로드해야 함.
  - CMD + B: 사이드 바 열고 닫기
  - CMD + P: 검색한 이름에 해당하는 파일 보기
  - CMD + W: 탭 닫기
  - CMD + F: 찾기
  - CMD + OPT + F: 찾기 + 바꾸기
  - CMD + F: 찾기
  - OPT + UP/Down: 라인 이동
  - OPT + Shift + Up/Down: 라인 복사
  - TAB, 권장 탭 공백 개수: 2 칸
  - Shift + TAB : 내어쓰기 (아웃덴트)
    - Indent Using Spaces 메뉴에서 설정 가능
  - Beautify 기능도 고려.
  - 탭 이동: CMD + Shift + [ / ]
  - CMD + \: 분할 창 모드
- 참고. index.html --> 브라우저가 프로젝트 단위로 화면에 출력될 때 index 라는 이름을 가진 html 파일을 찾아서 우선적으로 연다.
  - 브라우저가 시작하는 파일을 잘 찾을 수 있게 index.html로 지정한다.
- !DOCTYPE html <-- 문서의 HTML 버전을 지정
  - DTD, Document Type Definition 은 마크업 언어에서 문서 형식을 정의, 웹 브라우저가 어떤 HTML 버전의 해석 방식으로 페이지를 이해하면 되는 지를 알려주는 용도. (개발자가 브라우저에게 알려주는 것)
  - HTML1 ~ 4, XHTML, HTML5 (표준)
  - ex. !DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Trans ..." <-- 표준이 아닌 과거 버전
  - html <-- 문서의 전체 범위를 지칭하는 태그
  - head <-- 문서의 정보를 나타내는 범위, 웹 브라우저가 해석해야 하는 정보 (제목, 설명, 파일 위치, CSS, 비가시적인 정보를 작성하는 범위)
  - body <-- 문서의 구조를 나타내는 범위, 사용자의 화면을 통해 보여지는 로고, 헤더, 푸터, 내비게이션, 메뉴, 버튼, 이미지같은 웹페이지의 보여지는 구조를 작성하는 범위.
  - lang: 지정할 문서의 언어(ISO 639-1)를 명시하는 HTML 속성. (ex. lang="ko" 로 하면 구글 번역기 동작 X)
- head 안에 추가 가능한 내용
  - CSS 파일 추가: link <-- 대부분 CSS 파일을 가져와 연결할 때 사용, rel="stylesheet" / "icon"
    - rel: 가져올 문서와의 관계, relationship
    - href: 가져올 문서의 경로, hyper text reference
    - 참고: 보통 웹페이지 Favicon 적용할 때는 이름을 favicon이라고 지정하는 것이 관례, favicon.ico / favicon.png 파일이 주로 사용된다.
  - JS 파일 추가: script (html 문서 안에서 직접적으로 Javascript 작성도 가능)
  - CSS 스타일 직접 적용: style (html 문서 안에서 직접적으로 작성하는 경우)
  - 문서 제목 정의: title <-- 웹 브라우저의 탭에 표시됨.
  - meta: html 문서(웹페이지)의 제작자, 내용, 키워드 같은 여러 정보를 검색엔진이나 브라우저에게 제공
    - name: 정보의 종류
    - content: 정보의 값
  - (참고) viewport: 웹페이지가 출력되는 영역, 모바일에만 해당하는 속성
    - initial-scale=1.0 <--- 초기 줌 레벨 (모바일에서는 줌 인/아웃으로 컨텐츠를 보므로)
  - charset, 문자 인코딩 방식: 브라우저에서는 주로 UTF-8 사용이 권장 (EUC-KR --> UTF-8)
    - EUC-KR: 구, UTF-8: ㄱ ㅜ (Character Set으로 처리)
- img: 이미지 태그, alt (alternative) 는 이미지가 출력되지 못하는 경우 대신 출력할 텍스트를 지정, 대체 텍스트, 이미지 경로 및 네트워크 상태 불안정 등으로 인해 이미지 출력이 어려운 경우 이미지 대신 출력되는 글자. (필수 속성)
- 사이트 접속하여 개발자 도구 연 다음 Element 탭 왼쪽에 있는 선택 아이콘을 눌러 이미지 경로를 파악한다.
- 상대경로 / 절대경로
- http://127.0.0.1:5500/index.html <-- 라이브 서버 5500포트 (== http://localhost:5500)
  - localhost => 127.0.0.1
  - localhost: 우리의 컴퓨터 환경, 루트 경로에 있는 index.html 파일을 연다.
- . 이 있는 것과 없는 것 (예. ./images/xxx, images/xxx)
- 루트(/) <-- 최상위 경로, 프로젝트의 최상위 루트 경로
- 다른 사이트로부터 이미지를 가져오는 것: 절대 경로의 개념
- /images: (http://localhost:5500)/images 와 동일 개념
- ./ <-- 생략가능
- a href 태그 (글자 보라색, 파란색 의미)
  - hyper text reference
- 폴더로 접근하면 브라우저는 기본적으로 index.html 이라는 파일을 최우선으로 찾는다. (명시적인 html 파일 경로 지정이 없으면)
- 주소창에 xxx:5500/login 이라고 해서 꼭 폴더는 아니다. (라우터라는 것이 있다.)
- css 파일 안에서 background url 할 때 상대경로 기준은 css 파일 기준이므로 images 폴더 접근 시 html에서 하듯이 동일하게 하면 안된다.
  - ex. ../images/logo.png
- VsCode 환경설정
  - Code -> 기본설정 -> 설정 -> tab size 입력
    - 전체 찾기 / 실행: (CMD + Shift + P -> 설정 입력)
- 크롬 - 개발자도구 - Elements - element.style: CSS의 인라인 선언 방식으로 스타일이 삽입됨. (새로고침하면 다시 복구)
- CSS 선택자 개념
- HTML, CSS 는 크롬 인스펙터 통해 비교적 쉽게 분석 가능하나 자바스크립트는 보통 비즈니스 로직이 들어가기 때문에 난독화 과정을 거치므로 분석하기에는 어려움이 있음.
- :hov 내 :hover를 체크해보면 마우스 올렸을 때의 효과를 볼 수 있음.
- 실제로 적용된 CSS 내용만을 보려면 Computed 탭을 참고.
- 프로젝트 구성 방법
  - codepen.io (HTML 란은 body 태그 안을 의미)
- HTML / CSS / JS 전처리기 ( Preprocessor )
- 브라우져 기본 설정
  - 크롬에서 body 에 기본 8px이 들어감.
  - 다른 브라우저로 가면 유사하지만 다른 값들을 가짐.
  - 각각의 벤더사들, 애플, 구글, 크로스 브라우징
  - 브라우저에서 기본적으로 제공하는 CSS 스타일을 기본적으로 초기화하고 작업을 시작하는 것이 권장됨. (reset.css cdn)
    - "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css" <-- stylesheet 관계, link 태그 작성 --> 브라우저에서 기본적으로 제공하는 마진 삭제됨.
    - Codepen 에서 적용하려면 CSS Base 를 Reset으로 설정
- div.test --> test class를 사용하는 div 코드 자동완성. (자동완성 --> Emmet (에밋) 문법의 도움)
- h: 200 --> height: 200px
- bc: orange --> background-color: orange
- div>ul>li\*4{\$} <-- CSS 선택자와 관련 있는 내용.
- HTML
  - 열린/시작 태그 - 닫힌/종료 태그
  - 태그 중첩하면서 부모와 자식 관계 형성
  - Shift + Tab: Outdent / Tab: Indent
  - 하위(후손)요소 <-> 상위(조상)요소
    웹페이지 구상 순서 (만약 자기 자신을 설명하는 웹페이지를 만들 계획이라면?)
  - 기획, Design -> Git, GitHub -> HEAD -> HTML -> CSS -> Styling -> Javascript -> Publish
  - Design Requirment
    - Single page.
    - 최대한 사용자 편의성을 증가 (최소한의 클릭 / 스텝)
    - 전문 지식, 개발
    - Skill 스택 (기술, 언어, 툴)
    - 카테고리화, 입상 경력
    - Contact, LinkedIn, Github 등
  - Contents 구성
    - Author 소개
    - 주요 스택 (Front / BackEnd / Mobile)
      - Web basic HTML + CSS + JS
      - React / Vue
    - Career
      - Company, Scholl, Period 등
    - Skill
      - Language
      - Tool
      - Etc (Other Tools (Not related programming tool, ex. Photoshop etc) / Pure science 등)
    - Project
      - 중요 Project 먼저 기술 / 무엇인지? / 주요 기능 / Github (README <-- 주요기능 스크린샷)
      - Skill 정리 / Study
    - 장점, Skill, Link, 입상 경력
    - Contact: E-mail / Github / LinkedIn / 등등
  - Wireframing
    - 전반적인 레이아웃 구상
  - GUI 제작
    - Font Awesome / Color picker 로 색상코드 얻는다.
      - svg: fill 부분에 currentColor 부분에 색상 코드 삽입 가능.
    - canva.com (Image design) -> png download -> remove.bg etc
- 닫히지 않은 태그, 빈 태그, Empty Tag
- XHTML, XML (Strict)
- 열린 태그, Attribute, Value, 필수 Attribute (img 태그의 src, alt 엑박 속성 등)
- 글자와 상자: 요소가 화면에 출력되는 특성, 글자 개념, 상자 개념 2가지, 인라인 vs 블록 요소
- 인라인 요소: span, 콘텐츠 영역 설정 용도, 수평으로 쌓이는 특성, 줄바꿈 = 띄어쓰기로 해석
  - span, img, a(anchor, 닻, 링크를 건다, 고정시킨다의 느낌) - href 링크 URL 설정, target="\_blank" <-- 새탭에서 링크 이동 (브라우저 탭 위치), br (Break), label
  - 포함한 컨텐츠 크기만큼 자동으로 줄어듬. (가로, 세로 길이)
  - 글자 요소는 가로, 세로 사이즈 지정 불가, padding, margin은 세로 지정 불가
  - 글자 요소 안에 상자 (블록) 요소 포함 불가
- 블록 요소: div (division), 상자의 개념
  - div, h1~6(heading) - 헤더, p(paragraph) - 문장, ul(Unordered list), li(List item), ol(ordered list)
  - ul, li는 세트
  - 요소들이 수직으로 쌓임.
  - 부모 요소의 크기만큼 자동으로 늘어남.(가로) / 세로 넓이는 컨텐츠 크기 만큼.
  - 가로, 세로 사이즈 지정 가능 (상자 개념이므로)
  - 블록, 글자 요소 포함 가능
- 인라인 블록 (inline-block) 요소
  - input: 수평으로 쌓이는 특성, 가로, 세로 크기 지정도 가능
    - disabled (인풋창 비활성화), placeholder, value, checked (미리 체크), radio (선택 1개) - name 속성으로 그룹화 가능
    - label 안에 포함 가능 (라벨링)
- 테이블 요소, Table-Cell (블록 요소, 세부적인 블록 요소라 보면 됨.)
  - Row + Column Set
  - tr: 행 (Table Row), td: 열 (Table Data)
  - HTML 로는 구조만 나타내는 것 (테이블 구조를 만든다에 초점)
- localStorage / sessionStorage 차이점.
- Route, Switch, Redirect
- Git / GitHub
  - Google Docs - Version history
  - 소스 버전 관리
  - Local 관리 위험성 극복 -> Github, Bitbucket 서버 내 저장
    - Distributed Version Control
  - Branch
- VsCode
  - Settings - Json 검색 - Edit in settings.json
  - Live Server Install
  - 북마크 (HEAD 내 title 내용이 표시)
  - defer: 페이지가 모두 로드된 후에 해당 외부 스크립트가 실행됨을 명시. (명시하지 않으면 기본 false, 명시하면 true)
    - async 속성만 명시: 브라우저가 페이지를 파싱하는 동안에도 스크립트가 실행
    - async 속성 명시 X, defer만 명시: 브라우저가 페이지의 파싱을 모두 끝내면 스크립트가 실행.
    - async 속성 + defer 속성 모두 명시: 브라우저가 페이지를 파싱하기 전에 스크립트를 가져와 바로 실행.
- Custom Property
  - --background-color: blue; <-- 이런 식으로 사용가능
  - var(--background-color)
  - https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties
- Data Attribute
  - div[data-display-name='koo'] { color: red }
  - DOMStringMap 에서 보면 data- prefix는 제거되어 있음. (Snake -> CamelCase)
  - 보안 상관없는 데이터만 정의하여 사용
  - const temp = document.querySelector('div[data-display-name="koo"]');
    - console.log(temp.dataset) / console.log(temp.dataset.displayName) / console.log(temp.dataset.index)
- Media Query
- BEM (CSS 방법론)
  - Block Element Modifier
    - .card <-> .card--black
    - https://getbem.com/introduction/
    - Ref Link: https://nykim.work/15
    - 이름을 작성하는 방법에 대한 규칙.
      - card ui : Block
        - card 내 이미지, 버튼 등은 Element.
          - block\_\_element--modifier
            - .card
            - .card**image / .card**title / .card**description / .card**button
            - .card--darkversion
            - .card\_\_button--blue
- Homepage Section 구상 (주제 맞게 구상)
- HTML
  - i 태그: 이탤릭 폰트 스타일 글자
  - ul.navbar**menu>li.navbar**menu\_\_item\*6
  - href="#" <-- 해당 페이지의 최상단으로 이동.
  - progress 태그 존재
    - 보통 검색 시 mdn html progress 의 형식으로 검색 시도.
- CSS
  - box-sizing: content-box / border-box
  - position
    - static (기본값)
      - top, left 영향 X
    - relative (원래있던 자리 유지하면서 상대적으로 이동)
    - absolute (body 기준으로 움직임. 근접한 부모 중에 기본값이 static 이 아닌 부모 기준으로)
    - Sticky / Fixed
      - Sticky: 스크롤링 할 때 지정한 위치에 계속 유지
      - fixed: viewport 기준 (브라우저 창 기준) 으로 지정한 위치에 유지
  - Centering 기술
    - flexbox 일 때 중심축에서의 정렬은 justifyContent / 반대축에서의 정렬은 alignItems 사용
    - 블럭은 한줄에 하나씩 들어가므로 margin: auto 로 주면 브라우저에서 마진을 골고루 설정해준다. (수직은 불가)
    - textAlign: 블럭 레벨은 적용 안됨 (적용하려면 inner box, div의 마진을 auto로 설정해야 한다.)
    - transform: translate(50%, 50%) <-- X, Y 축으로부터 각각 50%를 준다는 개념, 수평/수직 중앙 정렬 가능
      - 자기 자신의 50% 라는 의미
      - 화면 중앙에 div 위치시키려면?
        - position: absolute, top, left: 50%, transform: translate(-50%, -50%)
    - textAlign과 lineHeight을 같이 설정하는 방법
      - text-align: center, line-height: 부모의 height 값으로 설정하면 수평/수직 중앙 정렬 가능
  - Background 속성
    - background-image: url
    - background-repeat: no-repeat
    - background-position: center
    - background-size: cover (반응형으로 구현 가능)
    - background: center/cover no-repeat url('') <-- 이렇게도 가능
  - 동적인 요소
    - Transformation
      - transform: translateX(100px) - X, Y, Z 값 이동하는 것 가능
      - scale(1.2) - 1.2배
      - rotate(45deg)
      - transform: translate(100px, 100px) scale(2) rotate(46deg)
    - Transition
      - transition-property: background-color
      - transition-duration: 300ms
      - transition-timing-function: linear
      - transition: background-color 300ms linear
      - transition: all 2s ease
      - cubic-bezier (cubic-beizer.com)
  - margin
    - margin: 1px 0 (위 + 아래 / 왼쪽 + 오른쪽)
    - margin: 0 0 0 0 (위, 오른쪽, 아래, 왼쪽)
  - ease, ease in, ease in out, ease out
- 통상적으로 넓이 1000 ~ 1200px 정도가 데스크탑에서 편하게 볼 수 있는 값.
- Media Query
  - 스크린 사이즈가 작을때만 적용되는 부분
  - 가능하면 최소의 정보만을 작성하는 것이 권장
- 평소에는 보여지지 않으려면 display: none
- display: inline
- 웹 소켓 (WebSocket)
  - TCP 연결에 완전한 이중 통신 채널을 제공하는 프로토콜.
  - MDN: https://developer.mozilla.org/ko/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications
  - ws, wss (https)
  - 송신 가능 데이터 타입은 String, Blob, ArrayBuffer
- flex-grow: 알아서 화면을 메꿔준다.
- javascript scroll position
  - scrollY
- use strict
- Arrow function.
- getBoundingClientRect()
- querySelector('#bar')
- data-link
- scrollIntoView()
- display none --> block : display 의 경우는 완전히 없어졌다가 나타나는 것이라 애니매이션 적용이 안된다. (transition)
- pointer-events: none;
- chrome inspector
  - Sources 탭
  - break point => Issue가 되는 부분 클릭 => Scope -> Local -> e: MouseEvent 내 내용 확인
  - Watch
    - e.target
    - e.target.parentNode
    - e.target.parentNode.dataset.filter
- forEach((item) => {}) ==== for (let item of itemList) {} === for(let i =0; i< items.length; i++) {project = projects[i]})
- if (false) {} === false || logic 방식
- git
  - add, commit, --amend, stash, stash pop, merge, cherry-pick, rebase
  - fetch, log, show, log -p
- overflow
- 기본 order는 0으로 지정되어 있음.
- ScrollSpy (JQuery)
- Intersection Observer API
  - root <--- Viewport.
  - const options = { root: null, rootMargin: '0px', threshold: 1}
    - threshold: 1이면 완전히 들어와야 변화되고 나갈때는 조금만 나가도 변화된다.
    - root: null <== view port, 내가 어떤것을 기준으로 요소들이 들어오고 나가는지를 확인하고 싶을 때 그 부모 컨테이너를 지정할 수 있다.
      - ex. root: document.querySelector('.container')
  - const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
    console.log(entry.target);
    // 들어오는 것과 나가는 것 따로 처리
    if (entry.isIntersecting) {
    entry.target.classList.add('active');
    console.log(entry.target);
    } else {
    console.error(entry.target);
    }
    });
    }, option)
  - boxes.forEach(box => observer.observe(box));
    - boundingClientRect
    - intersectionRatio
    - intersectionRect
    - isIntersecting
    - isVisible
    - rootBounds <== option과 관계, 디폴트는 ViewPort 기준
    - target
- wheel, scroll event
  - scroll: 브라우저에서 인식하는 스크롤에 대한 모든 이벤트
  - wheel: 사용자가 조작하는 휠 이벤트
- Webpage Pulish
  - Github - Settings - Github page.
  - Custom Domain
    - Google domain
      - http://domains.google.com
      - Search domain you want to use.
      - $12 ~ $100000
      - My domains
      - Github -> Custom domain -> www.aidenkoog.com -> save
      - Custom domain section's learn more.
      - Managing a custom domain for your GitHub Pages site
      - Register DNS ip address provided by GitHub.
      - Google domain -> my domain -> DNS -> Register DNS of GitHub.
        - A type. (possible to add an additional DNS)
      - www, CNAME ==> aidenkoog.github.io. <-- dot mandantory.
- iOS
  - cocoapod
  - pod


## 미정리 내용

인터넷 전문 은행과 핀테크 설명

1. 인터넷 전문 은행 (Internet-Only Bank)

인터넷 전문 은행은 오프라인 지점 없이 온라인 및 모바일 플랫폼을 통해 금융 서비스를 제공하는 은행을 의미합니다. 기존의 전통적인 은행과 달리 모든 업무를 디지털 방식으로 처리하며, 비용 절감과 빠른 서비스 제공이 주요 특징입니다.

인터넷 전문 은행의 특징
	•	비대면 서비스: 계좌 개설, 대출 신청, 송금 등 모든 금융 거래를 온라인에서 진행
	•	낮은 운영 비용: 오프라인 지점이 없기 때문에 인건비, 임대료 등의 비용이 절감되어 높은 금리를 제공하거나 수수료를 낮출 수 있음
	•	편리한 사용자 경험 (UX/UI): 모바일 앱 중심의 직관적인 인터페이스 제공
	•	빅데이터 및 AI 활용: 고객 데이터 분석을 통해 맞춤형 금융 상품 추천 및 신용 평가 진행

대표적인 인터넷 전문 은행
	•	한국: 카카오뱅크, 케이뱅크, 토스뱅크
	•	미국: 찰스 슈왑 뱅크(Charles Schwab Bank), 치메(Chime)
	•	유럽: N26(독일), 레볼루트(Revolut, 영국)

2. 핀테크 (Fintech: Financial Technology)

핀테크는 “금융(Finance)“과 “기술(Technology)“의 합성어로, IT 기술을 활용하여 혁신적인 금융 서비스를 제공하는 산업을 의미합니다. 핀테크는 모바일 결제, 블록체인, AI 기반 투자, 로보어드바이저 등 다양한 분야에서 발전하고 있습니다.

핀테크의 주요 분야
	1.	모바일 결제 및 송금: 삼성페이, 카카오페이, 네이버페이, 페이팔(PayPal)
	2.	디지털 뱅킹: 카카오뱅크, 토스뱅크
	3.	P2P 대출 및 크라우드 펀딩: 렌딧, 피플펀드, 와디즈
	4.	블록체인 및 암호화폐: 비트코인, 이더리움, 업비트, 빗썸
	5.	로보어드바이저 (AI 기반 자산관리 서비스): 파운트, 에이트라이드, 웰스프론트
	6.	인슈어테크 (보험 + 기술): 레몬에이드(Lemonade), 캐롯손해보험

핀테크의 장점
	•	금융 서비스 접근성 향상: 기존 금융권의 문턱을 낮추어 누구나 쉽게 금융 서비스를 이용 가능
	•	비용 절감 및 효율성 증대: 자동화된 금융 서비스로 운영 비용 절감
	•	맞춤형 금융 서비스 제공: AI 및 빅데이터를 활용하여 고객 맞춤형 상품 추천

핀테크의 단점
	•	보안 리스크: 해킹 및 개인정보 유출 위험
	•	규제 문제: 금융 당국의 규제 강화로 사업 확장에 어려움
	•	기술 의존성: 시스템 장애 및 해킹 발생 시 큰 피해 가능

인터넷 전문 은행 vs 핀테크

구분	인터넷 전문 은행	핀테크
개념	온라인 전용 은행	금융 + IT 기술 융합 산업
주요 서비스	계좌 개설, 대출, 예금, 송금 등 전통 은행 업무	모바일 결제, P2P 대출, 암호화폐, 로보어드바이저 등
대표 기업	카카오뱅크, 케이뱅크, 토스뱅크	카카오페이, 네이버페이, 렌딧, 업비트
운영 방식	기존 은행의 업무를 디지털화	새로운 기술 기반의 금융 서비스 제공

인터넷 전문 은행도 넓은 의미에서 핀테크의 일부로 볼 수 있지만, 핀테크는 더 광범위한 금융 기술 혁신을 포함하는 개념입니다.

현재 인터넷 전문 은행과 핀테크 기업 간 협력이 활발하게 이루어지고 있으며, 앞으로도 금융 시장에서 지속적인 혁신이 기대됩니다.


## 크라우드소싱, 아웃소싱 비교 및 설명

크라우드소싱(Crowdsourcing)과 아웃소싱(Outsourcing)은 모두 외부 자원을 활용하는 방식이지만, 그 개념과 활용 방식이 다릅니다. 아래에서 각각의 개념과 차이점을 설명하겠습니다.

1. 크라우드소싱(Crowdsourcing)

크라우드소싱은 다수의 사람(대중, Crowd)에게 작업을 공개적으로 의뢰하는 방식입니다. 특정한 집단이 아닌, 불특정 다수의 개인이나 그룹이 참여할 수 있습니다.

특징
	•	공개 참여: 기업이나 조직이 특정 작업을 웹 플랫폼 등을 통해 일반 대중에게 공개하여 참여를 유도함.
	•	다양한 아이디어와 창의성: 여러 사람이 참여하여 다양한 해결책을 제시할 수 있음.
	•	보상 방식 다양: 참가자에게 금전적 보상, 명예, 경험 등 다양한 형태로 보상 제공.
	•	디지털 기술 활용: 온라인 플랫폼(예: Kaggle, Freelancer, Upwork, CrowdWorks 등)을 통해 진행되는 경우가 많음.

예시
	•	구글 reCAPTCHA: 보안 문자 입력을 통해 사용자가 책, 신문, 문서를 디지털화하는 데 도움을 줌.
	•	위키백과(Wikipedia): 불특정 다수가 참여하여 콘텐츠를 작성하고 검토함.
	•	로고 디자인 공모전: 여러 디자이너가 참여하여 디자인을 제안하고 기업이 선택.

2. 아웃소싱(Outsourcing)

아웃소싱은 특정 업무를 외부 기업이나 전문가에게 위탁하여 수행하는 방식입니다. 주로 비용 절감과 효율성 향상을 목적으로 이루어집니다.

특징
	•	전문 기업 또는 개인에게 위탁: 특정 업무를 전문적으로 수행할 수 있는 외부 조직에 맡김.
	•	비용 절감: 내부 인력을 채용하는 것보다 저렴한 경우가 많음.
	•	핵심 역량 집중: 기업이 본연의 핵심 업무에 집중할 수 있도록 비핵심 업무를 외주 처리.
	•	계약 기반: 일정한 계약을 통해 일정, 품질, 가격 등을 명확하게 정함.

예시
	•	콜센터 운영: 기업이 고객 서비스 업무를 외부 전문 콜센터 업체에 위탁.
	•	소프트웨어 개발: 기업이 IT 프로젝트나 앱 개발을 외부 개발사에 의뢰.
	•	물류 및 배송 서비스: 온라인 쇼핑몰이 물류와 배송을 전문 업체(CJ대한통운, FedEx 등)에 위탁.

3. 크라우드소싱 vs 아웃소싱 비교

비교 항목	크라우드소싱 (Crowdsourcing)	아웃소싱 (Outsourcing)
참여 주체	불특정 다수의 대중	특정 기업 또는 전문가
업무 방식	개방형 공모 또는 과제 수행	계약 기반으로 업무 위탁
비용 구조	보상 제공 (경쟁 방식도 가능)	계약에 따른 비용 지불
장점	창의적인 아이디어, 신속한 문제 해결	비용 절감, 전문 인력 활용
단점	품질 보장 어려움, 보안 문제 발생 가능	장기 계약 시 유연성 부족

4. 활용 방식의 차이
	•	크라우드소싱은 다수의 창의적인 해결책이 필요한 경우 유용
→ 예: 아이디어 공모전, 데이터 라벨링, 번역 작업 등
	•	아웃소싱은 전문성이 필요한 작업을 효율적으로 처리하고 싶을 때 사용
→ 예: IT 개발, 고객 서비스, 제조업 생산 아웃소싱 등

크라우드소싱은 개방적이고 참여형 방식이라 창의성과 혁신이 필요한 분야에서 강점을 가지며, 아웃소싱은 신뢰성과 전문성을 요구하는 업무에 적합합니다.

- 유스케이스, 액터, 시스템 바운더리 (개발 범위), 어떤일을 실행하는 게 유스케이스
- 스테레오 타입, include, extend
- Validation: Review, 테스트
- WBS (Work Breakdown Structure): 업무 분업 구조 / 작업 분해 구조, 업무 일정 세분화하여 체크하는 목적
- 유사추정: 소프트웨어 개발비 산정
- 프레임워크, Proframe, 전자 정부 Framework, ORM
- MainFrame, 선진 Process, 업무 개선, 패트리넷 (요구사항 명세화 기법)
- 솔루션, 패턴, 해결책
- SQL Injection, XSS, TCP SYN Flooding
- 파일 업로드 취약점
  - 서버 사이드 화이트리스트 필터링
  - 파일명을 난수로 변경, 확장자 제거
  - 업로드 디렉토리, 다운로드 디렉토리 분리
  - 파일 시그니처(헤더) 읽어서 파일에 문제가 없는지 확인
  - Web Shell (서버에서 실행되는 악성 스크립트, 서버를 원격으로 제어할수 있도록 하는 일종의 백도어)
    - PDF, 매크로, DDE, cmd.php^jpg
- CSRF
- 개발보안 방법론
  - CLASP, 7-TouchPoint, MSSDN, 입력값 검증, 보안기능, 에러처리, 세션통제
- Buffer overflow
- Format String
- HTTP 분할응답
- OTP, Web shell, DrDoS
- TCP Max Backlog
- SQL 파싱트리, syn cookie
- DDoS 공격기법 3가지, 대응방법
- 개발 보안 설명, CC인증, APT 공격 기법 (절차 4가지), Spear Phishing, Watering Hole
- GDPR, ISMSP
- 객체 > 객체지향을 어떻게 모델링 > UML
- 소프트웨어 공학 (개발방법론 + 프로젝트 관리 + 품질)
- SCM (Supply Chain Management)
- BOM, 원칙, 단가 자체만, 물류, 부가세 제외, 최종액 산정 방법
- 데이터와 기능 등의 용어 (같지만 다른 표현들)
  - 필드, 애트리뷰트, 프로퍼티, 메소드, 펑션, 오퍼레이션, 행위, 속성, 객체, 오브젝트, 인스턴스화, 실행중
  - 동적 구조화 (시퀀스 다이어그램) - 사용자가 예약 시스템을 통해 물건을 주문하는 과정에 대한 흐름
- UseCase > Class > Sequence > Component > Deployment (시스텀 구성도)
- Request For Proposal, 제안 요청서. 프로젝트 담당할 최종 업체를 선정하기 전, 1차로 선별된 업체들에게 보내는 문서
  - 원하는 요구 사항을 체계적으로 정리한 문서라고 볼 수 있습니다. 
  - 제안 요청서에는 프로젝트의 주제, 목적, 목표, 내용, 기대성과 등 진행할 업무 내용에 대한 자세한 사항 포함
- 프로젝트 관리 계획서, 사업수행 계획서 (맨 처음 만들어야 하고 고객과 소통, 최소한 자원, 인력있어야 함, 방법론도 있어야 하고 검수기준 필요), 과업대비표, 착수보고서
- 일정 단축 기법, PMBOK
- Function Point를 MM (맨먼스)로 어떻게 산정
- 공공데이터 개방 > 통계 분석이 끝난 결과 데이터를 개방 > 분석을 한다면 원 데이터를 받아야 함
- On-premise 전환 방법, On-Premise 는 클라우드와 반대되는 말
- TPMC, 분당 CPU 처리
- 클라우드 보안, APT 공격, ISMS-P 애자일 프로세스, 스크럼, TDD
- 협의 알고리즘, 블록체인, 머신러닝
- PCM 변조
- GFS, Scale Up, Scale Down, Json
- HDFS (계층형 분산 파일 시스템), Map Reduce, Pig, Hive, HBase
- BigData 분석, 통계, 샘플링, 표본, 온톨로지
- Public / Private Cloud Computing, ISMS-P 인증 모델, 클라우드 보안 검사, Hybrid Cloud
- Private Cloud Computing
  - 통합 서버 관리, 가상화 -> n개의 물리적 자원을 하나의 통합된 툴로 만들어 주는것, 기기가 1대인데 여러대 있는것처럼 관리해주는것도 가상화
  - OpenStack을 각각에 다 설치해서 가상화 실현
- QoS, SLA (Service Level Agreement, 사용한 만큼 비용 지불)
  - On-Demand, 유틸리티 컴퓨팅
- 클라우드에서 인스턴스는 서버, 컴퓨터, 네트워크라 인지
- 세그먼트, 대역폭
- 클라우드 컴퓨팅 주변으로 머신러닝 + 빅데이터 + IoT + 블록체인
- 지도학습 (사람이 결과를 안다), 자율학습 (사람이 결과를 모름)
- 샘플링, 전수데이터
- Scale Out, Scale Up, Scale Down
- IaaS, 서버만 빌려준다
- PaaS, 윈도우까지도 설치해준다
- SaaS, 앱까지도 설치해준다, 유틸리티 프로그램 (노트패드, Office 365 등)
- CRM 고객관리 프로그램
- Host OS > Guest OS > (Virtualization) > USB 드라이버, 하이퍼바이저 개념
- 목표(전략, 실행) > 컨설팅 (문제에 대한 해결책) > 비즈니스 프로세스 자동화, 업무체계 정립 (Mega > Major > Process > Activity > Task), End To End 서비스 (고객)
  - 컨설팅
    - ISP
    - BPR(workflow)
    - EA (Enterprise Architecture)
    - 6 Sigma
    - 보안컨설팅
- 업무체계 정립: 1 업무프로세스, 2 조직(도)
- 폰노이만
- 임시 기억: 레지스터, 버퍼, 스풀
- CPU: 연산장치, 레지스터, 제어장치, 버스
- 0주소, OPCode, 인터럽트 벡터 테이블, 시스템 콜
- 모놀리티 커널, 마이크로 커널 (유저모드 -> 시스템 콜)
- 1주소, Operand (1. Register, 2. Mode, 3. Address) 
- FailOver
- Zookeeper
- 메모리 데이터베이스, MMDB, SSL, 인증서, AES
- 적시성 (원하는 시점에 정보 제공 및 물품/활동 제공하는 것)
- 무결성(변조, 중복 등이 없는 것, 데이터의 정확성, 일관성 그리고 신뢰성 의미)
- 소프트웨어 리엔지니어링: 소프트웨어 품질 문제 해결
- 소프트웨어 위기: 비용지연, 생산성 저하, 품질 저하를 체계적인 방법으로 해결
- Unified Process (UP)
- 누구 입장에서 좋은가? 나쁜가? 에 대해 생각
- T센서 : 패킷 복제하는 도구
- 프로세스 모델, 방법론 개념 비교 설명
- Tailering
- 문제점 (등장인물, 성능보안, 기술적인 것 관례한 문제점)
- 제안 PM, 사업수행 PM
- 넓이 개념으로 암기
- 알파테스트, 베타테스트
- SQPM
- SLA, 계약서
- SLA 평가기준
- PA