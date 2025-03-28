# Flutter

정리될 내용들은 아래와 같습니다.

- 개념 / 용어 정의, 사용 이유
- 성능, 메모리 등 이슈 해결 방법

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

#### 플러터 개념

- 프레임워크
- Fuchsia의 사용자 인터페이스와 애플리케이션을 만들기 위해 사용
- 구글에서 만들어 오픈소스로 공개한 모바일 SDK (2017년 발표)
- 크로스 플랫폼 모바일 앱 및 다양한 플랫폼을 쉽게 개발할 수 있도록 구글에서 제공하는 무료 오픈소스
- 렌더링 엔진, UI 컴포넌트, 테스트 프레임워크, 도구, 라우터 등 기능을 모두 제공
- 웹, 모바일 환경, PC, Embedded 환경 지원
- SKIA 라는 그래픽 엔진 사용
  - 번역 작업 없이 작성 코드를 그대로 렌더링 => 속도가 네이티브 앱과 비슷 / 다른 플랫폼들에서 일관된 화면 표시 가능
- Material & Cupertino Component, Widget들을 가지고 있음
- Hummingbird: 플러터 웹 프로젝트

#### 크로스 플랫폼 (Cross-Platform Software) 설명

- 단일 코드로 둘 이상의 플랫폼에서 동작 가능

#### 다트 언어 사용 이유

- 구글에서 현재 유지 보수 진행 중인 언어
- JIT (Just-in-time) 과 AOT (Ahead-of-time) 컴파일 모두 지원
  - AOT: 다트 코드를 네이티브 코드로 변경
  - JIT: 핫 리로드 지원, 빠른 개발 속도와 반복을 가능하게 하여 생산성 증가
- 객체 지향 언어, 마크업 언어 없이 (리액트와 다르게) 시각적 사용자 경험을 쉽게 구현 가능
  - 위젯안의 위젯의 방식으로 코드 작성
- 자바, 자바스크립트와 유사
  - 자바의 기본 문법 + 자바스크립트의 일부 문법과 선언형 프로그래밍 방식 조합
- 간결한 문법

#### 플러터 장점 설명

- 기본 제공되는 많은 위젯, 풍부한 UI Widget
- 코드량 감소, 개발 시간 단축 (Hot Reload)
- 크로스 플랫폼 개발 가능
- Live and Hot Reloading 기능 제공
- 네이티브 앱과 비슷한 성능
  - IC(중간 코드)와 해석에 의존 X, 기계코드에 직접 내장되어 해석 프로세스와 관련된 성능문제를 제거
- 다양, 유연한 UI 제작 가능 (유연성)
- 활발한 커뮤니티와 질 좋은 문서 보유 (3.0으로 오면서 안정화)

#### 플러터 아키텍쳐 구조 설명

- Framework (최상위 레이어, Dart): Dart 기반 플랫폼
  - app Widgets, Gestures, Animations, Illustrations, Materials를 처리하는 Dart 기반 플랫폼.
    - Material, Cupertino
    - Widgets
    - Rendering
    - Animation, Painting, Gestures
    - Foundation
- Engine (C/C++): 새로 화면을 그릴 때마다 화면을 래스터화 (디스플레이 처리)
  - Service Protocol, Composition, Platform Channels
  - Dart isolate Setup, Rendering, System Events
  - Dart Runtime Mgmt, Frame Scheduling, Asset Resolution
  - Frame Pipelining, Text Layout
- Embedder (Platform-specific)
  - Render Surface Setup, Native Plugins, App Packaging
  - Thread Setup, Event Loop Interop

#### 플러터 단점 설명

- 타사 라이브러리 적고 플러터의 일부 위젯은 하나의 플랫폼에서만 동작
  - 리액트 네이티브에서도 비슷한 이슈들은 존재
- 타사 라이브러리에 제한적
- 릴리즈 사이즈 큼
- 다트 언어 (오직 플러터를 위해 숙달시켜야 하는 언어)
- 3D 모델링, Unity 통합 / 게임 엔진이 부족해 대부분의 광고 모바일 플랫폼도 지원하지 않음

#### 빌드 모드 설명

- 개발단계에 따라 3가지 모드로 코드 컴파일 가능
- 종류
  - Debug Mode: Hot Reload 기능을 제공하는 모드
  - Profile Mode: 성능을 분석할 때 사용하는 모드, flutter run --profile
  - Release Mode: 앱을 최적화 시키고 작은 크기로 만드는 모드, flutter run --release

#### 플러터에서 위젯 설명

- 플러터 = 위젯 모음
- 사용자에게 보이는 인터페이스를 결정하는 부품
- 위젯 조합으로 다양한 유저 인터페이스 구현 가능
- 화면에 보이지 않는 부분도 모두 위젯으로 이루어져 있음
- 빌드를 하려면 위젯 내부에 코드 작성 필요

#### 위젯 타입 나열

- StatelessWidget
  - 화면이 로드될 때 한 번만 그려지는 상태가 없는 위젯
  - 변경되지 않으며 이벤트 또는 사용자 상호 작용에 의해 동작하지 않음
- StatefulWidget
  - 이벤트 또는 사용자 상호 작용에 의해 위젯 모양 변경
  - State 개체에 상태 저장되며 위젯의 상태와 모양을 구분
  - 상태 변경 => setState() 호출 => Framework에 위젯을 다시 그리도록 지시

#### Dart 설명

- Google에서 개발한 프로그래밍 언어
- JSX 또는 XML과 같은 별도의 선언적 레이아웃 언어 사용하지 않음
- 선언적인 특성으로 가독성 높음
- 클래스, 인터페이스, 함수 등의 기본 OOP 개념 지원
- 배열은 직접 지원하지 않음 (컬렉션으로 지원)
- 자바스크립트와 유사하나 코드 실행 속도가 더 빠름
- 성능 향상과 코드 실행 시간을 줄이기 위해 Dart 가상 머신(VM)은 JIT(Just-in-Time) 및 AOT(Ahead-of-Time) 컴파일러 모두 사용
- 객체 지향 프로그래밍 언어

#### Stateful Widget Lifecycle (생명주기) 설명

- 위젯 구축
  - createState()
  - initState(): 단 한번만 호출됨
  - didChangeDependencies()
- Re-Drawing
  - 화면 드로잉 (dirty): 위젯 트리 구축
  - build(): UI 구축
  - 화면 드로잉 (clean): 위젯 트리 구축
  - didUpdateWidget(): 위젯 구성이 변경될 때마다 호출됨
  - setState(): 상태가 변경되었을 때 프레임워크에 상태가 변경 됨을 알림
- 위젯 소멸
  - deactivate()
  - dispose()

#### main()과 runApp() 차이점

- main(): 프로그램 시작점 역할
  - 플러터는 해당 함수 없이 실행 불가능
- runApp(): 앱 위젯 트리의 루트로 사용될 최상위 위젯을 받아 화면에 보여주는 함수
  - 주어진 위젯을 화면에 부착하는 역할

#### 패키지와 플러그인에 대한 설명

- 개발에 필요한 위젯이나 화면 구현을 위해 직접 구현 작업없이 패키지와 플러그인을 사용해서 손쉽게 사용하는 것도 가능
- 패키지: 순수 다트 언어로만 구현된 코드
- 플러그인: 다른 언어가 포함된 코드

#### Key에 대한 설명

- ElementTree가 WidgetTree의 위젯을 식별할 때 사용
- 위젯 트리에서 위젯이 움직일 때마다 현상태를 보존하는 역할
- 로컬 키
  - 위젯 트리에서 특정 레벨에서 구별할 수 있는 키
- 글로벌 키
  - 앱 어디에서든 사용할 수 있는 고유 키

#### Container 클래스 설명

- 여러 다른 위젯을 담아서 크기, 패딩, 배경 등 다양한 설정을 할 수 있는 위젯

#### Container 와 SizedBox 차이점

- 공통: 다른 위젯들을 담을 수 있고 가로, 세로 크기 지정 가능
- SizedBox: 위젯을 담고 가로, 세로 크기 변경 / 배치만 가능
- Container: 위젯을 담고 가로, 세로 크기 변경 / 배치 + 꾸미기 기능

#### Mixins 용도 설명

- 다중상속 지원 X
- 자바에서 클래스, 인터페이스 활용한 유사 다중상속 구현을 하듯이 플러터에서는 Mixins를 사용해서 다중상속 구현이 가능

#### GetX 라이브러리 상태 관리 방식 설명

- 단순 상태 관리
  - 기존의 데이터와 변경되는 데이터가 같은지 확인하지 않음
- 반응형 상태 관리
  - 데이터 변화가 있을 때만 재랜더링 수행
  - 추가 기능 worker
    - Ever
    - Once
    - Interval
    - Debounce

#### Provider 라이브러리 상태 관리 방식 설명

- 상태 변화된 것이 여러 개인 경우 여러개의 Provider를 추가하여 처리 가능
- Provider 는 제공자 / Consumer 는 소비자
- 어떤 데이터를 제공할 때는 Provider로 제공

#### (참고) 앱 기획 과정 관련 정보

- 기획의 방향
  - 제작하고 싶은 서비스를 구체화 시켜나가는 기획 필요
  - 완성까지 속도를 높여주는 기획
- 서비스 기획
  - 문제를 정의하고 정의한 문제를 해결해 나가는 것
  - 대상: 서비스를 만드는 개발자, 기획자 그리고 디자이너 모두에게 해당
- 문제 정의 및 해결 방법
  - 불편함에 집중, 사용성 등에 대해 예민하게 생각
    - Pain Point 찾아내기, Pain Point 기반으로 문제 도출 시작, 좋은 문제를 정의하는 것이 해결 방안보다 중요
  - 최대한 많은 앱 서비스 경험 필요
    - 경험 + 다운로드 수 + 플랫폼(iOS/Android) + 평점 + 구매형태 + 평가 + 앱 이름 + 검색 키워드 + 단점 + 장점 + 특징
    - 스토어 설명에 대한 느낀점
    - 앱 실제 사용 시나리오 (스플래시 -> 권한 -> 온보딩/튜토리얼 -> 로그인 또는 메인)
    - 메뉴 바 또는 바텀 시트 다이얼로그 메뉴 구성 파악
    - UI의 계층 파악 (Depth1 => Depth2 ...)
    - 유저 스토어 리뷰 반응
  - 여러 앱들이 같은 문제를 어떻게 풀었는지에 포커스
    - 유사한 앱들에 대한 경험 테스트 및 기록
    - 같은 상황 또는 문제에 대한 해결법 검토
  - 자신이 첫번째 유저라고 생각하고 접근
    - 유저들이 어디에서 유입되고 어디에서 만족을 느낄 것인지 등이 예상되는 서비스인지 판단
  - 오프라인 행동 관찰
    - 반복적으로 하는 행위가 있다면 이 행동을 앱을 사용한 자동화가 가능할 지에 대해 생각
  - 자주 릴리즈 하는 것이 중요
    - 서비스의 주기능만 집중하여 작은 단위로 노출 필요
    - 최소한의 리소스로 가설 검증 후 개선하는 방향 (핵심 플로우에만 집중)
  - 작은 문제에 집중
    - Ex. 중고거래 중 모든 것을 풀려고 하지 말고 일단 직거래 문제부터 푸는 것

#### 플랫폼 비즈니스 모델

- 공급자 (사업자) 그룹과 사용자 그룹을 서로 연결해주는 서비스
  - 서버 환경 구축 필수

#### 앱 기획 아이디어 도출 과정 설명

- 타겟유저 설정 / 정의
- 앱의 핵심 기능
- 앱의 차별성
- 목표 수립 (유저 목표, 비즈니스 목표)
- 앱 서비스를 한마디로 정의

#### 프로젝트 이름 정하는 방법

- 서비스 이름
  - 앱 이름
  - 웹 이름
  - 보통 브랜딩 디자인으로 결정 / 앱 출시 전, 앱을 거의 다 제작한 시점에 작명
- 프로젝트 이름
  - 개발 프로그램에서 불릴 이름
  - 앱 개발 시작할 때 이름이 결정됨
  - 타이핑 수월하고 발음에 용이한 간단한 영문 이름 채택 (Ex. Dox, Dog, Candy 등)
    - 일명 코드명 같은 느낌

#### 프로젝트 구축

- homebrew / brew install git 명령 실행
- flutter SDK 설치
  - https://www.flutter.dev
  - visit https://docs.flutter.dev/development/tools/sdk/releases?tab=macos
  - download the latest flutter of stable channel.
  - execute export PATH="\$PATH:`pwd`/flutter/bin" on console or Modify bash_profile. (Add export PATH="\$PATH:/Users/admin/flutter/bin to .bash_profile or .zshrc)
  - flutter precache
  - flutter doctor
  - if you encounter this error ---> Flutter - Unable to find bundled Java version.
  - cd /Applications/Android\ Studio.app/Contents/jre
  - [Not Electric Eel] ln -s ../jre jdk
  - [Not Electric Eel] ln -s "/Library/Internet Plug-Ins/JavaAppletPlugin.plugin" jdk
  - [Electric Eel] cd /Applications/Android\ Studio.app/Contents
  - [Electric Eel] ln -s jbr jre
  - 안드로이드 라이센스 동의 에러 발생하면 flutter doctor --android-licenses 명령 실행
  - flutter doctor
    - 신형 모델 맥북에서 에러 발생 시 터미널 & 컴퓨터 껐다가 켜고 터미널에 softwareupdate --install-resetta
  - flutter doctor --android-licenses
- Visual Studio Code 설치
  - Flutter, Flutter Intl, Dart, dart-import
- Xcode 설치
  - open a Simulator 명령으로 시뮬레이터 실행 가능
- Android Studio 설치
  - (참고) Android Platform 종속성을 제공하기 위해 Android Studio의 전체 설치에 의존
  - flutter 설치 (플러그인)
  - atom one dark 설치 (옵션 플러그인)
- flutter run 명령으로 플러터 앱 실행
- Android 기기에서 USB 설정을 '파일 전송' 모드로 설정
- 참고. 스마트폰 미러링 위한 설치
  - brew install scrcpy
  - brew install --cask android-platform-tools
  - scrcpy (scrcpy -s SERIAL_NUMBER)
- iOS 빌드 시 3가지 버전 관리
  - flutter
  - Xcode
  - Cocoapods
- iOS 는 QuickTime Player 로 화면 미러링
- Flutter 앱을 실제 iOS 기기에 Deploy 하려면 Apple 계정 필요. 또한 Xcode 에서 실제 기기 Deploy 설정 필요. 앱이 Flutter Plugin을 사용하는 경우 써드 파티 Cocoapods 의존성 관리도 필요
- 환경변수
  - 윈도우: C:\FLUTTER/BIN
  - Mac: touch ~/.zshrc, export PATH="$PATH:/Users/koo/Documents/flutter/bin"

#### 변수 선언 관련 설명

- var 사용한 변수 선언 시 초기화 된 값 형태에 따라 자동적으로 타입 추론이 이루어짐
- int 형 변수값에 double 값 연산 불가능 (Ex. double test = 23.444, test += 1)
- double 형 변수값에 int 값 연산 가능 (double 형 값들은 int 형 값들보다 범위가 넓음)
- double 형 변수에 int 타입 값이 초기화될 때 double 형 변수는 그 값을 double 형으로 인식
  - Ex. double num1 = 30 <== 30.0
- 4 == 4.0 <== true
- 변수 중복 선언 불가능
- 변수명은 소문자로 시작, 띄어쓰기 불가능, 띄어쓰기가 필요하다면 카멜표기법으로 작성
- List 는 순서가 보장됨 / Set 은 순서 보장 안됨
  - Set[0] 이런 식의 접근이 안되는 이유는 순서 보장 안되는 열거 타입이므로 안됨
  - Set은 위치 기반의 인덱스 접근 안됨
  - Set은 중복 허용하지 않음, Ex. 1, 2, 3, 2 ==> 1, 2, 3
  - Set은 리스트보다 접근 속도 빠름 (처리 속도 빠름)
- 맵에서 존재하지 않는 키로 접근했을 때 null 값 출력
- Any 타입에 해당하는 것은 dynamic, Object
- 맵 선언, 초기화 그리고 사용법
  - Ex. Map<String, dynamic> testMap = { 'name': 'Koo' } / testMap['name']
- toList(), toSet()의 결과값은 각각 [ ... ], { ... }
- 타입 추론이 아닌 타입을 명시하는 것이 권장 사항
- ? 유무에 따른 Non-nullable, Nullable 처리
  - 일반적으로 타입을 가진 변수 선언 시 초기화를 하지 않으면 에러 발생, Null을 허용하지 않으므로.
- 멤버 변수에 \_ 설정 => private
  - 클래스 단위로 private 처리가 되는 것이 아니라 파일 단위로 처리
  - A라는 파일에서 B 클래스의 private 멤버 변수에 접근이 안되게 하고 싶으면 B 클래스 정의를 다른 파일로 이동시켜야 함
- 언더바로 해당 변수 사용하지 않음을 표시하기도 함

#### Object, dynamic, var 설명

- Object
  - 모든 타입의 공통 부모
  - 다른 타입 대입 가능
- dynamic
  - 컴파일 시간에 오류를 잡아내는 Static Checking을 하지 않음
  - 컴파일 시간에 오류를 잡아내지 않으므로 어떤 값이 들어오는지 정확히 알 때만 사용해야 함
- var
  - 모든 타입이 될 수 있지만 초기화 값에 따라 타입이 정해짐

#### final, const 차이점

- **final**
  - 한번 값을 대입하면 변경 불가능
  - 런타임에 값이 할당
- **const**
  - 한번 값을 대입하면 변경 불가능
  - 컴파일 타임에 값이 할당
- 차이점 예
  - DateTime.now()
    - 코드 빌드 시 현재 시간을 정확히 나타내는데 코드가 언제 빌드될 지 코드 작성 당시에 알 수 없음
    - 실행 시에 시간이 결정되므로 final 키워드는 사용가능
    - 실행 시에 시간이 결정되는 기능이므로 const 키워드는 사용 불가능

#### if, switch 설명

- switch가 if 보다 가독성 및 처리 속도가 더 빠름

#### 함수 설명

- 반환타입 + 함수명 + 매개변수 + 실행문 으로 구성

#### 연산자 설명

- **?.** : 앞의 객체가 null 이면 null 출력, null이 아니면 . 뒤의 코드 실행
  - 변수값이 null 값이 아닐 때만 뒤에 있는 연산자 실행
- **!.** : 앞의 객체가 null 아님을 명시적으로 알리는 용도
  - 앞의 변수 값이 null 값이 아니니 다음 연산자 실행
- **is** : 타입 비교 (Ex. 'Test' is String)
- **??** : 변수값이 null 값이면 ?? 뒤에 값을 넣어줌
  - var name = temp ?? "no-data";
- **??=** : 변수값이 null 값일 때 삽입할 값을 지정
  - String? name;
  - name ??= 'no-data';
- [int? b] <== 옵션 파라미터
- 네임드 파라미터 작성은 중괄호로 감싸줘야 함. (네임드 파라미터들은 옵셔널 속성)

#### for (for ~ in loop)문, while문 차이

- for문
  - 반복 횟수가 정해진 경우
  - 주로 배열과 함께 많이 사용
  - 구하고자 하는 값의 조건이 무엇인지 정확할 경우 사용
  - 초기값, 조건식, 증감 연산이 while 문과 달리 블록에서 바로 찾을 수 있기 때문에 가독성 좋음
- while문
  - 무한루프나 특정 조건에 만족할 때까지 반복해야 하는 경우
  - 주로 파일을 읽고 쓰기에 많이 사용
  - 조건식이 false 될 때까지 무한 실행
  - 무한 루프 동작 과부하를 막기 위해 반드시 종료를 위한 조건 필요
  - 내가 구하고자 하는 값의 조건이 무엇인지 정확히 모를 경우, 유동적인 경우에 사용

#### 함수 포지셔널, 옵셔널, 네임드 파라미터 관련 설명

- **포지셔널** 파라미터 (Positional Parameter)
  - 매개변수의 순서가 중요한 파라미터
- **옵셔널** 파라미터 (Optional Parameter)
  - 괄호 []를 통해 지정해 줄 수 있으며 []안에 들어간 매개 변수는 설정되지 않아도 문제 없이 코드 실행 가능
- **네임드** 파라미터 (Named Parameter)
  - {}를 통해 생성 가능
  - 이름으로 지정하기 때문에 순서는 중요하지 않음
  - required 가 사용된 파라미터는 기본적으로 매개변수를 넘겨줘야 하는데 required를 지우고 기본값을 지정해 준다면 옵셔널 파라미터처럼 사용 가능

#### static 변수 설명

- 클래스 객체 참조 통한 접근은 불가능
- 클래스 이름.변수로 바로 접근 가능
- static 키워드가 붙은 함수나 변수끼리만 서로 참조 가능

#### 위젯 설명

- MaterialApp
  - ThemeData primarySwatch
  - Scaffold
  - AppBar
  - Center
  - Text
- StatelessWidget
  - constructor
  - build
  - public / private
- Container
  - **Container**
    - color / alignment / padding / margin / width / height / child
    - center: Alignment(0, 0) / x = 0, y = 0 => center
    - 가운데가 0, 0이고 우측 또는 상단 쪽이 1, 좌측 또는 아래 쪽이 -1, 컨테이너 바깥에도 그림 그리기 가능
    - Alignment(0.7, 1.3)와 같이 더 자세한 값 지정도 가능
    - height나 width가 지정되지 않으면 최대 크기로 지정
  - **SizedBox**
    - 자식 사이즈 지정, 주로 텍스트의 가로/세로 길이를 지정할 때 사용 (텍스트 글꼴 사이즈는 텍스트의 style 속성 사용하여 지정)
    - width / height / child
    - 하나의 child 위젯만 가질 수 있음
    - height나 width가 지정되지 않으면 child widget의 크기에 맞춤
  - **Center**
    - Container 에서 alignment: Alignment.center를 설정한 것과 동일
  - **Padding**
    - padding / child
    - EdgeInsets.symmetric(hotizontal: 100, vertical: 100)
    - EdgeInsets.all(40)
    - EdgeInsets.fromLTRB(10, 70, 50, 50)
    - EdgeInsets.only(bottom: 50, top: 20)
    - EdgeInsets.zero <== 특정 위젯은 기본적으로 패딩을 가지고 있는 경우가 있음, 여백 값을 없애고 싶을 때 사용
  - **Align**
    - alignment / child
- Multiple Item Container
  - **Column**
    - children: [ Container(), Container() ]
  - **Row**
    - children: [ Container(), Container() ]
    - mainAxisAlignment
    - crossAxisAlignment
    - mainAxisSize: MainAxisSize.min
  - **Wrap**
    - Overflow 발생 시 알아서 줄을 변경
    - direction: Axis.vertical / Axis.horizontal
  - **Stack**
    - 위젯을 겹칠 때 사용
    - alignment: Alignment.center
    - children
  - **Spacer**
    - Spacer() 형태로 사용
    - 위젯 아이템들 사이의 공간을 주고 싶을 때 사용
    - flex 속성 (비율)
    - 공간 차지 비율: flex값 / 각각의 스페이서들의 flex 값 총합
  - **Expanded**
    - child 속성 존재
    - 나머지 영역 안에서 위젯을 그리고 싶을 때 사용
    - 예를 들어 텍스트 값이 길어지는 경우 알아서 줄바꿈 처리
- Button
  - ElevatedButton, OutlinedButton, TextButton
    - 생성자 형태(속성값) 동일
    - styleForm 사용
    - disable 방법 (onPressed: null)
  - ElevatedButton
    - onPrimary, primary 속성 존재
  - OutlineButton
    - primary 속성 존재
    - backgroundColor
    - side (BorderSide)
  - TextButton
    - primary 속성 존재
  - GestureDetector
    - onTap
    - onTapDown
  - Button 내 차일드 아이템에 대한 스타일을 직접적으로 지정하는 방향은 지양 => 버튼이 비활성화 임에도 불구하고 텍스트 색상이 다른 색상으로 설정되는 문제 발생 등 => Button의 styleForm 에서 설정하는 것 권장
  - onPressed: null 설정하면 버튼 비활성화
  - onSurface와 onPressed: null 함께 사용시의
  - Scaffold 안의 FloatingActionButton
    - onPressed
    - toolItip
- BoxFit 속성
- BottomNavigationBars

#### 위젯 클래스 관련 설명

- 특정 파일 내 특정 클래스를 외부에서는 사용을 하지 않고 파일 내부에서만 사용 가능하게 만들려면 클래스와 생성자 이름 앞에 언더바를 추가하면 됨
  - Ex. \_MyHomeWidget

#### MediaQuery 사용 예 설명

- 가로 스크린 사이즈를 가져오는 예제
  - width: (MediaQuery.of(context).size.width) - (30 \* 5)

#### 위젯 가운데 정렬 예 설명

- Align 내 Container 위젯 배치 / alignment 설정
- Center 내 Container 위젯 배치
- Container 위젯 내 텍스트 위젯 배치 / alignment 설정

#### Stream 설명

- 데이터나 이벤트가 들어오는 통로
- 비동기 프로그래밍에서 데이터 시퀀스를 제공하는 데에 사용
- 한 쪽에서 값을 넣고 반대쪽에서 리스너가 값을 받는 구조
- 하나의 스트림에 여러 리스너 존재 가능하며 모두 동일 값 획득
- Stream Controller를 통해 스트림 생성 / 관리 가능

#### Stream 유형 설명

- Single Subscription Streams (단일 구독 스트림)
  - 이벤트를 순차적으로 전달 (수신 순서가 중요한 경우 사용)
  - 수신자는 한명, 수신자가 없으면 이벤트 트리거 되지 않음
  - 한번만 수신 가능
- Broadcast Stream
  - 여러 수신자가 동시에 구독할 수 있는 다용도 스트림
  - 이전 구독을 취소한 후에도 다시 이벤트 수신 가능

#### Hot Reload와 Restart 차이점

- Hot Reload
  - Dart VM에 변경된 코드를 불러오고 위젯트리를 재빌드
  - 앱의 상태를 보전
  - main(), initState() 재실행 하지 않음
  - Reload 가능한 경우
    - 새로운 라이브러리의 사용 / 변경
    - 위젯의 구조변경 / 수정
    - 이미지나 Assets 파일의 추가 사용
- Hot Restart
  - Dart VM에 변경된 코드를 불러오고 앱 재시작
  - Full Restart 보다는 빠름
  - 앱의 모든 상태 소실
  - main()부터 호출
  - Restart 필요한 경우
    - initState() 변경
    - 폰트 변경 / 추가
    - 제네릭과 열거형 클래스 추가
    - 코틀린, 자바, 스위프트 등의 네이티브 코드 변경
    - 그 외에 앱 상태에 변경을 주는 코드 수정 시

#### Build Context 설명

- 위젯 트리에서 현재 위젯의 위치를 알 수 있는 정보
- 각 위젯에는 고유한 BuildContext가 존재하며 이는 StatelessWidget.build 또는 State.build에 의해서 반환된 위젯의 상위 컨텍스트가 됨
- 상위 위젯과 상호 작용하고 위젯 데이터에 접근하는데 사용 가능

#### 위젯 테스팅

- 단위 테스트 (Unit Tests)
- 위젯 테스트 (Widget Tests)
- 통합 테스트 (Integration Tests)

#### pubspec.yaml 파일 설명

- 프로젝트에 필요한 패키지 / 해당 버전, 글꼴 등과 같은 종속성에 대한 정보를 가진 파일
- 포함된 내용
  - 프로젝트 이름 / 버전 / 설명
  - 종속성
  - Assets (이미지 / 오디오 등)
- 런타임에 사용할 패키지는 dependencies 블록에 작성

#### Provider 상태 관리 설명

- 상태 관리 매니저
- 생성 부분에서는 사용할 데이터 타입을 결정하고 해당 데이터에 대한 Provider를 만들고 소비 부분에서는 Provider를 통해 데이터를 불러오거나 수정 등의 작업 진행
- 상세 정보
  - ChangeNotifier: 데이터가 변경되면 Consumer에게 Notify
  - ChangeNotifierProvider: 하위 위젯에 "ChangeNotifier"를 제공해주는 클래스
  - Consumer: Provider의 데이터를 받아서 사용하는 클래스

#### FutureBuilder와 StreamBuilder 설명

- FutureBuilder
  - 비동기처리
  - 일회성 응답에 사용
- StreamBuilder
  - 비동기처리
  - 데이터를 여러번 가져오는 데에 사용
  - 계속해서 데이터의 변화를 모니터링하면서 처리할 때 적합

#### 화면 Navigation 방법 (Code Level)

- 각각의 화면 생성
- 전환을 위한 코드 생성
  - Navigator.push(context, MaterialPageRoute(builder: (context) => const Page2(),),);
- push를 하면 push된 화면에서는 자동으로 AppBar에 뒤로가기 UI를 표시
- AppBar 내 leading 속성 오버라이딩하면 자동 뒤로가기 기능 안됨
  - Navigator.pop(context); 작성하면 뒤로가기 가능

#### pub.dev

- Dart / Flutter 앱을 위한 공식 패키지 저장소
- 처음부터 모든 것을 개발하지 않아도 되기 때문에 앱 개발 속도를 올릴 수 있음

#### Scaffold 설명

- 최상단, 중간, 최하단 그리고 떠 있는 버튼 등을 지원해주는 클래스
- 플러터에서 제공하는 기본적인 디자인적 뼈대를 구성하는 위젯
- 기본적인 material design(구글식 디자인 컨셉)의 시각적인 레이아웃 구조를 실행
  - 구글에서 자주 쓰는 디자인 양식이나 아이콘들을 Material Design이라 부름

#### 라이프사이클 설명

- State의 initState()는 화면이 처음 호출될 때만 한번만 수행
- build는 화면 변경 감지시 매번 호출
- initState() 호출을 하게 만들기 위해서는 Hot reload 말고 Hot restart가 필요

#### 알림 메세지 설명

- Cloud Push Message
- Local Alarm Message
  - flutter_local_notifications
  - Android 4.1+ / iOS 8.0+
  - 주기적 알림 가능
  - 매일 / 매주 지정된 날짜와 시간에 알림 표시 가능
  - 예약된 보류 중이 알림 요청 목록 검색 가능
  - ID 별 알림 취소 / 제거
  - ID는 고유해야 함
  - 알림 탭 했을 때 앱이 포그라운드, 백그라운드, 종료되었을 때 처리하는 기능 존재

#### WidgetsFlutterBinding.ensureInitialized() 설명

- Flutter Engine 과의 상호작용을 위해 사용

#### await, async 관련 설명

- await을 사용해야 하는 함수가 있다면 그것을 감싸고 있는 영역의 함수에 async 키워드를 추가해줘야 함
- 비동기 함수에 대해 await 키워드를 붙였을 때와 안붙였을 때 반환값이 상이
  - ex. bool or Future<bool>

#### Provider, BLoC 그리고 GetX 비교

- Provider
  - Consumer를 이용해 상태값을 가져오고 Provider와 Context를 이용해 Controller의 비즈니스 로직을 불러옴
  - Stateful 위젯을 사용하거나 Context를 사용해야 함
  - MVVM 패턴 사용
  - Notifier ==>
  - 내부적으로 bloc과 Provider 패턴을 구현
- GetX
  - GetBuilder를 통해 상태값을 가져오고 Get.find를 통해 Controller의 비즈니스 로직을 가져옴
  - Context를 사용하지 않는 GetX 방식은 위젯으로 분리하여 사용 가능
  - 부모에서 Controller를 선언해줄 필요 없음
  - UI 부분에서 바로 사용 가능 / 클래스가 생성될 때 바로 사용 가능
  - 특정 Controller에 아이디를 부여함으로서 관리 가능
  - MVVM 패턴 사용
  - GetXController ==> bloc
- BLoC
  - MVVM 패턴 사용
  - Business Logic Component
  - 비즈니스 로직과 UI를 분리해서 유지보수하기 쉬운 앱을 만드는데에 목적

#### Dartz 라이브러리

- Dart 데이터 타입 외 확장된 데이터 타입도 지원
- Either, right, left 개념
- API 호출하여 데이터 반환받고 .fold 형태로 처리 가능 (.fold((left){}, (right){}))
- .fold / foldLeft / foldRight / all / every / getOrElse 존재

#### Equatable

- 인스턴스가 서로 같은 인스턴스인지 판단을 쉽게 할 수 있게 해주는 플러그인
- (Ref.) OOP 세계 내 모든 클래스는 기본적으로 Object를 상속.
  - 대부분의 언어에서는 이 Object 라는 클래스에 한 인스턴스와 다른 인스턴스를 비교하는 알고리즘이 정의되어 있음
- Dart에서는 operator라는 함수에 정의, 이를 오버라이딩하여 비교 알고리즘을 자유롭게 변경 가능
- operator 오버라이딩 통한 수정은 필드가 많아질수록 작성해야될 코드도 많아지고 hashcode는 절대적으로 int 값을 반환해줘야 하는데 String같은 int로 환산되기 어려운 값들은 정의 방법이 애매
  - 이러한 이유로 Equatable 이 필요

#### InkWell 설명

- 컨테이너와 같이 별도의 제스쳐 기능을 제공하지 않는 위젯에 제스쳐 기능을 추가하고자 할 때 InkWell 위젯을 사용

#### GetX 사용법 정리

- GetConnect: 네트워크 통신
- 상태관리 방식
  - 단순 상태 관리
  - 반응형 상태 관리
- Get Controller 사용하기 위해서는 Get.put()으로 컨트롤러를 등록
- GetBuilder() 아래의 모든 위젯은 컨트롤러에서 변경되는 데이터를 실시간으로 반영 가능한 상태가 됨
  - GetBuilder() 사용하지 않는다면 Get.find<XXXController>(). 방식으로 데이터 변경 / 반영 가능
- 반응형 상태 관리의 경우 변수 타입 Prefix로 Rx를 추가하고 변수값은 .obs를 추가
- Obx() 아래의 모든 위젯은 GetX와 마찬가지로 컨트롤러에서 변경되는 데이터를 실시간으로 반영 가능한 상태가 됨
  - 사용 방식은 비슷하나 컨트롤러 이름 지정이 불가능하여 Get.find()의 형식으로 사용 필요
- 그리고 추가적으로 worker 라는 것이 있음
  - 컨트롤러 안에서 onInit() 함수를 오버라이드하고 그 안에 추가해서 사용
  - Ever: 매번 변경될 때 실행
  - Once: 처음 변경되었을 때만 실행
  - Interval: 계속 변경이 있는 동안 특정 지정 시간 인터벌이 지나면 실행
  - Debounce: 인터벌이 끝나고 나서 특정 지정 시간 이후에 한번만 실행
- 사용법 관련 개선안
  - Get.find<>(). 에서 간단하게 사용하려면 컨트롤러 내부에 getter를 생성해주면 간단해짐
    - static SimpleController get to => Get.find(); => SimpleController.to.increase() 의 형태로 사용 가능
  - Get.find() 사용하는 클래스에 StatelessWidget 대신 GetView를 상속하는 방식 사용
    - extends GetView<SimpleController> 의 방식

#### Flutter Responsive UI

- 화면 사이즈를 읽는 방법은 여러가지가 존재
- MediaQuery
- MediaQueryData.fromWindow
- WidgetsBinding.instance.window.physicalSize
- Flexible / Expanded Widgets
- LayoutBuilder Widget

#### Flutter 3.10 / Dart 3

- 2023 Google I/O
  - 개발자 경험 (얼마나 쉽게 개발 가능한지)
    - Material3 Kit
  - 광고 삽입 방법
    - 다트 언어만 사용해서 광고 삽입 가능
  - 퍼포먼스 업데이트
    - 개발자가 해야할 것 없으며 플러터만 업그레이드 하면 퍼포먼스 업데이트가 가능
  - 다트 3.0
    - Patterns, sealed class, class modifiers
  - Shader support for Web
  - WASM for web (Web Assembly)
    - 개발
    - Deploy
    - 다트 언어를 자바스크립트로 변경 (나중에는 Web Assembly 로 변경)
      - 자바 스크립트 뿐만 아니라 거의 모든 언어들이 웹 어셈블리 바이너리를 가져와서 사용 가능
      - 다이나믹함 증대
    - Deploy

#### Google Fuchsia OS

- 리눅스 커널 문제 (파편화 시작의 원인)
  - 커널: HW, SW를 연결해주는 역할
  - 마이크로 커널 ==> Fuchsia
  - 단일형 커널
- 통합 OS의 필요성
- 오라클 자바 특허 싸움
- 안드로이드 OS의 한계 (터치 기반에 최적화된 상황)
- 플러터와의 연관성
  - 플러터는 크로스 플랫폼 모바일 프레임워크
  - 모든 플랫폼 커버 가능
  - Fuchsia 생태계 완성
- 삼성이 안드로이드 대신 Fuchsia 로 대체할 가능성
  - 업데이트 주도권을 구글이 쥐고 있지 않음
  - 제조사가 업데이트를 하지 않으면 의미가 없으므로
- Xianyu (시안류) 플러터를 사용하는 중고물품 판매 플랫폼
  - 플러터 개발하면서 어려움이 있었음
  - 플러터 초기 엔진 안정성에 문제가 있었음
  - 이로 인해 구글이 플러터를 사용하지 않을 수 있다는 이야기가 나왔었음
    - 과거 구글이 폐기한 프로젝트들이 많음? (그러나 대부분 생산성 담당용 앱들)

#### Fuchsia OS - Why flutter?

- 2016.8 Github 에 코드 게시
- Zircon 이라는 마이크로 커널 기반 (지르콘)
  - 음성 명령에 중점 두고 개발됨
- 2017. 11 swift 지원 계획
- 2018. 1 픽셀북을 공식 퓨시아 테스트 디바이스로 추가
- 2019. 1. 안드로이드앱 구동 가능성
- 2019. 5. 구글 i/o에서 퓨시아 언급
- 2019. 7. 1 퓨시아 공식 홈페이지 오픈
  - https://fuchsia.dev 
- 참고 설명
  - 구글 트레블 프로젝트

#### Flutter 개발 시 필요한 부분

- Method or Function
- If else
- For loop
- List
- Class
- Constructor
- Data type

#### toolchain 에러 (cmdline-tools component is missing) 처리 방법

- AndroidStudio 내 Android SDK Command-Line Tools (Latest) 설치
- 위 내용 적용해도 에러 발생하는 경우 아래 스텝 수동으로 진행
  - flutter config --android-sdk "C:\Users\k0376\AppData\Local\Android\Sdk"
  - flutter config --android-studio-dir "C:\Program Files\Android\Android Studio"
 
#### Flutter의 StatefulWidget과 StatelessWidget의 차이점 및 권장사항

- StatelessWidget
  - 변경되지 않는 UI를 가진 위젯
  - 한 번 생성되면 다시 빌드될 때 내부 상태가 변경되지 않음, 내부 상태 보관 없음
  - build() 함수가 한 번 실행되고 나면, 위젯이 변경되지 않는 한 다시 호출되지 않음 (정적 화면)
  - 재랜더링 트리거 포인트: 부모 위젯의 변경
  - 주로 UI만 렌더링하는 단순한 위젯을 만들 때 사용
  - 사용 시기
    - 화면에 표시되는 정보가 변경되지 않는 경우
    - API 호출 없이 정적인 화면을 만들 때
    - 부모 위젯에서 전달된 값만을 사용해야 할 때
- StatefulWidget
  - 내부 상태(State)를 변경할 수 있는 UI를 가진 위젯
  - State 객체를 가지고 있으며, setState()를 호출하면 UI를 다시 렌더링
  - StatefulWidget 자체는 immutable(불변)하지만, State 객체는 변경이 가능
  - 사용 시기
    - 버튼 클릭, 입력 필드, 애니메이션 등 UI의 변경이 필요한 경우
    - API 데이터를 받아와 화면을 업데이트해야 할 때
    - 사용자 입력(텍스트, 스크롤, 드래그 등)을 처리할 때
- 권장사항
  - StatelessWidget을 최대한 사용하고, 상태를 관리해야 할 때 StatefulWidget 또는 Provider, Riverpod 같은 상태 관리 패턴을 활용하는 것이 좋은 방향
  - StatefulWidget은 내부 상태(State)를 가지며, setState()를 호출하면 해당 위젯과 그 하위 위젯들이 전체 다시 빌드(Rebuild), 불필요한 렌더링이 발생
  - 만약 StatefulWidget을 써야한다고 하면 전체를 StatelessWidget으로 구성하고 일부 위젯을 StatefulWidget으로 만드는 방향 추천
    - StatefulWidget의 State 최소화
  - StatelessWidget으로 구성, Provider, Riverpod, GetX, Bloc 상태관리라이브러리 사용하는 것이 좋은 방향
- 언제 StatefulWidget을 사용하는 것이 효과적인가?
  - 일회성 UI 변경이 필요한 경우
    - 애니메이션, 버튼 클릭 등의 UI 효과를 관리할 때 (e.g., AnimatedContainer, PageView 등)
  - 초기화가 필요한 데이터가 있을 때
    - 예: initState()에서 Future를 실행하는 경우 (API 요청 등)
  - 외부 상태 관리가 필요하지 않은 경우
    - 간단한 UI 상태 변경 (예: TextField 입력 감지)
