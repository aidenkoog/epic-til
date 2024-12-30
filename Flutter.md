# Flutter

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

- List, Set, Map
- final, const, Nullable / NotNull Variable
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
- 세이프 영역 처리: iOS X 이상에서만 처리 가능, 물리 영역 침범하지 않도록 처리 가능
- 가시화 여부: Visibility

## 로컬 노티피케이션

- Local Notification (단순 알람 추가 / 알람 스케쥴링)

## 로컬 데이터베이스

- hive (로컬 데이터 베이스), 빠르고 Secure NoSQL (Key - Value)
  - AES-256 암호화
  - hive 에서 저장된 모든 데이터는 Box로 구성
  - 구조가 없으며 무엇이든 포함 가능
  - hive, hive_flutter, hive_generator, build_runner
  - HiveType, HiveField Annotation
  - HiveObject extends 해줘야 키 사용 가능

## 프로젝트 폴더 구조

- components
- config
- models
- repositories
- pages
- services

## 린트

- linter (동일 코딩 스타일 등)
  - analysis_options.yaml
- 표준 린트 세트
- 정적 분석 (프로그램 실행 없이 코드 분석)
- linter 내 rules 가 명시되어 있음
- severity: ignore / info / warning / error

## 커스텀 폰트 사용

- 프로젝트 루트 위치에 assets 폴더 추가
- font 하위 디렉토리 생성 후 폰트 파일 삽입
- pubspec.yaml 내 fonts: 추가
- ThemeData 내 폰트 패밀리 지정 시 앱 전체적으로 지정
- 기기 폰트 사이즈에 의존 제거 방법: MaterialApp 내 builder 에 MediaQuery 지정 후 textScaleFactor를 1.0d으로 고정

## 테마 설정

- 컬러셋 지정
- ThemeData 분리 후 커스터마이징
- scaffoldBackgroundColor, backgroundColor 차이
- splashColor (리플효과)

## 페이지 구조

- Scaffold 내 bottomNavigationBar, BottomAppBar
  - child: 내 아이콘, 텍스트, 클릭 이벤트 처리 등 설정 가능
- floatingActionButton, FloatingActionButton 추가 가능
- 클릭에 따른 동적 처리 setState 활용
- 새 페이지로 이동하려고 할 때: Navigator.push 활용
- Scaffold leading, body 활용
- Input 창 포커스 처리 > 아무 영역 눌렀을 때 키보드 제거
  - Scaffold body를 GestureDectector로 Wrapping 후 onTap 내 FocusScope.of(context).unfocus() 처리 추가

## 앱 개발 프로젝트 진행 관련 내용

- 화면 UI 제작
- 서비스 로직 분리
- 서비스 내 데이터 변경 시 UI 갱신, ChangeNotifier, notifyListeners(), AnimatedBuilder
- 알림 추가, 예외처리
- 데이터 (텍스트, 이미지) 영구 저장
- 객체 타입 로컬 데이터 추가
- 화면 전환 시 pop / popUntil (pop, pop)
- ListView, ListTile (without Designer), ListView.separated, separatedBuilder, itemBuilder
- CupertinoButton (자체 패딩)
- 글자가 길어서 오버플로우 발생하는 경우 > Wrap 위젯 처리
- 갤러리 사진 로드, 촬영 기능, 사진 크게 보기, 작게 보기
- 팝업 / 바텀 시트 구성 및 기능 연결
- 개발 중 나머지 영역을 채우도록 처리하기 위해서는 Expanded 사용 (Expanded(child: ListView...))
- Navigator.pop(context, [데이터])
  - 예) showModalBottomSheet().then((value) { service.setAlaram() })
- 로컬 데이터베이스 사용 시 객체 타입 저장을 위한 모델 정의
- 해당하는 모델에 해당하는 Hive Adapter 등록 (예: 결제 내역 / 결제 상세 내역 데이터 모델)
- 속성 오버라이드 textStyle.copyWith(fontWeight: w500)
- CustomObj get myObject => values.singleWhere((item) => item.id == id)
- sort
- 앱 이름, 아이콘 설정, 앱 아이디 설정
  - iOS: Runner > Display Name / 1024 * 1024 규격의 아이콘 준비
  - AOS: AndroidManifest.xml > label, res/mipmap