# Flutter
## Flutter TIL

정리될 내용들은 아래와 같습니다.

- 개념 / 용어 정의, 사용 이유
- 성능, 메모리 등 이슈 해결 방법
- Interview Question, Answer

## Flutter 사용 이유

- 하나의 코드 베이스로 여러 플랫폼 커버
- 플러터 프레임워크는 네이티브에 가까운 속도 제공, 위젯 단위로 개발 가능한 수월한 앱 개발 인터페이스 제공
- 매터리얼, 쿠퍼티노 스타일 UI 자유롭게 사용 가능

## 서비스 기획

- 문제를 정의하고 정의한 문제를 해결해 나가는 것
- 대상: 기획자, 개발자, 디자이너
- 서비스 기획 시 중요 포인트
  - 주요 Pain Point 발견 후 집중
  - 많은 앱 서비스 경험
  - First User 라 가정하고 접근
  - 실제 사용자 행동 기반 접근 (온라인 & 오프라인)
  - 실제 반응에 따라 계속 UX,UI, 기능 추가 / 수정 / 개선
  - 핵심 메인 기능에 집중
- 내가 느끼는 불편함에서부터 시작
- 아이디어 구체화
  - 프로젝트 구상
  - 아이디어 도출, 마인드맵
  - 앱 레퍼런스 조사
  - 앱 내 기능 나열

## 크로스 플랫폼

- 단일 코드 베이스로 두가지 이상의 플랫폼에서 동작 가능
- 여러 환경에서 동시 개발이 가능한 프레임워크

## 다트 문법

- main() / String, int, double, bool
- List, Set
- Map
- final, const, Nullable Variable (변수)
  - final 값 할당 한번만 가능, 변수 선언과 생성자 통해 할당, 런타임 때 할당
  - const 는 상수, 빌드 타임때 값 할당, 컴파일 타임 때 값 할당
- Getter / Setter / 접근 제한자 (set, get, _)
- 상속, Super, Override
- 추상화 클래스, 인터페이스

## 위젯 사용

- 프로젝트 구조
- 화면 레이아웃 구성 위젯: MaterialApp, Text, Scaffold, Appbar
- 위젯 추출 코드 분리: StatelessWidget
- Public / Private 위젯
- 단일 컨테이너: Container / SizedBox / Center
- 복수 위젯 컨테이너: Column / Row / Stack
- 여백 스타일: Padding, EdgeInsets
- 배치 및 공간 제어 위젯: Align, Spacer, Flexible, Expanded (남은 영역 차지)
- 버튼: ElevatedButton, OutlineButton, TextButton, GestureDetector
- 동적 업데이트 화면: StatefulWidget
- 플로팅 버튼 작성: FloatingActionButton
- 위젯 간 데이터 전달 (생성자)
- 이미지 출력: AssetImage, NetworkImage
- 플랫폼 스타일 위젯: Material / Cupertino
- 화면 전환: Navigator
- 입력 창: TextField, TextEditingController
- 구분선: Divider
- 스위치: Switch, CupertinoSwitch
- 값 변경될 때 마다 자동으로 UI 갱신: ValueListenableBuilder (DbObserver와 유사)

## 자주 사용되는 기능

- Local Notification (단순 알람 추가 / 알람 스케쥴링)
- hive (로컬 데이터 베이스), 빠르고 Secure NoSQL (Key - Value)
  - AES-256 암호화
- hive 에서 저장된 모든 데이터는 Box로 구성
  - 구조가 없으며 무엇이든 포함 가능
- hive, hive_flutter, hive_generator, build_runner
- HiveType, HiveField Annotation

## 키워드

- UTC
- Timezone
