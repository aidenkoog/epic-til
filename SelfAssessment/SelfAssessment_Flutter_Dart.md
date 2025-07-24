# Concepts, Features, Types and Pros and Cons

Organize concepts, features, types and Pros and Cons

## Flutter, Dart

- Flutter의 StatefulWidget과 StatelessWidget의 차이점
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
        - StatefulWidget 사용의 효과적인 시기
            - 일회성 UI 변경이 필요한 경우
                - 애니메이션, 버튼 클릭 등의 UI 효과를 관리할 때 (ex. AnimatedContainer, PageView 등)
            - 초기화가 필요한 데이터가 있을 때
                - 예: initState()에서 Future를 실행하는 경우 (API 요청 등)
            - 외부 상태 관리가 필요하지 않은 경우
                - 간단한 UI 상태 변경 (예: TextField 입력 감지)

- Flutter의 BuildContext 설명
  - 위젯 트리에서 현재 위젯의 위치를 나타내는 객체
  - 위젯 트리를 탐색하고, 부모 또는 자식 위젯과 상호작용하는 데 사용
  - BuildContext의 역할
    - 위젯의 트리 구조에서 현재 위치를 나타냄
    - 부모/자식 위젯과 상호작용할 때 사용됨
    - Theme, MediaQuery, Navigator 등과 같은 상위 위젯 정보를 가져올 때 사용됨
    - 위젯의 build() 함수에서 제공되며, setState() 등과 함께 UI를 업데이트하는 역할.

- Flutter에서 FutureBuilder와 StreamBuilder의 차이점
    - 공통
        - FutureBuilder와 StreamBuilder는 비동기 데이터를 UI에 반영하는 위젯
        - 둘 다 비동기 작업을 기다려서 결과를 UI에 표시
    - 차이점
        - FutureBuilder (단일 Future 비동기 작업)
	        - 한 번만 실행되는 비동기 작업을 처리할 때 사용
            - Future<T>를 받고, 작업이 완료되면 UI를 업데이트
            - 한 번 실행되면 다시 실행되지 않음 (새로운 Future를 제공하지 않는 이상)
            - API 호출, DB 조회 시 사용
            - FutureBuilder 동작 방식
                - 비동기 작업 실행
                - 비동기 작업 완료 전 → CircularProgressIndicator() 표시
	            - 작업 완료 후 → Text(snapshot.data)로 UI 업데이트
	            - 한 번 완료된 이후 다시 실행되지 않음 (새 Future 제공해야 함)
        - StreamBuilder (연속적인 데이터 스트림)
	        - 지속적으로 변화하는 데이터를 UI에 반영할 때 사용
	        - Stream<T>를 받고, 새로운 데이터가 발생할 때마다 UI를 업데이트
	        - 웹소켓, 센서 데이터, Firebase Firestore 등의 실시간 데이터와 함께 사용
            - StreamBuilder 동작 방식
                - Stream()이 실행
	            - 새로운 값이 도착할 때마다 UI 업데이트 (Text(snapshot.data))
	            - 스트림이 종료되면 마지막 데이터가 유지
	            - 새로운 이벤트가 발생하면 UI가 다시 렌더링
    - 결론
	    - FutureBuilder → 한 번만 실행되는 비동기 작업 처리 (Future<T>)
	    - StreamBuilder → 지속적으로 변화하는 데이터 처리 (Stream<T>)

- Flutter에서 Hot Reload와 Hot Restart의 차이점은?
  - Hot Reload
    - 개념
      - 상태(State)를 유지하면서 코드 변경 사항을 UI에 즉시 반영 (UI 수정 & 로직 변경 반영 가능)
    - 특징
      - 앱의 상태를 유지한 채 변경 사항을 반영
	  - 위젯 트리를 다시 그리지만 앱을 재시작하지 않음
	  - 주로 UI 변경 사항을 빠르게 확인할 때 사용
    - Hot Reload 적용 가능 변경 사항
      - UI 변경 (Text, Color, Padding 등)
      - 메서드 또는 함수 수정
      - 새로운 위젯 추가
    - Hot Reload 적용 안 되는 변경 사항
      - main() 함수 내 코드 수정
      - initState() 내부 코드 변경
      - 전역 변수 또는 static 변수 변경
  - Hot Restart
    - 개념
      - 앱을 완전히 재시작하여 모든 상태를 초기화 (앱의 모든 변수를 초기화하고 다시 실행)
    - 특징
      - 앱을 처음부터 다시 실행 (초기 상태로 돌아감)
	  - UI뿐만 아니라 모든 코드가 다시 실행됨
	  - StatefulWidget의 상태(setState)가 초기화
	  - 앱 로직을 변경할 때 필요함 (예: 전역 변수, initState 변경)
    - Hot Restart가 필요한 경우
      - main() 함수 변경
      - initState()에서 실행되는 코드 변경
      - 전역 변수 또는 static 변수 변경

- Flutter에서 플랫폼별 코드(Android/iOS)를 다르게 적용하는 방법은?
  - 결론
    - UI 위젯을 플랫폼별로 다르게 적용
      - Platform.isAndroid, Platform.isIOS, Theme.of(context).platform
    - 특정 로직을 플랫폼별로 분기
      - defaultTargetPlatform, kIsWeb
        - defaultTargetPlatform 사용 시에는 kIsWeb을 먼저 사용하여 체크 필요
    - Android/iOS 네이티브 코드 실행
      - MethodChannel
    - Android/iOS에서 다른 패키지 사용
      - Platform.isAndroid로 분기

- Future.microtask 의미
    - 정의
        - 마이크로태스크 큐에 작업을 추가하여 즉시 실행하는 다트의 비동기 처리 메커니즘
        - 즉시 실행해야 하는 비동기 작업 예약 함수
        - 현재 실행 중인 코드가 끝난 후 이벤트 루프에서 가장 먼저 실행됨
        - UI 프레임 드롭을 방지하면서 UI 업데이트 후 빠르게 실행할 때 유용
    - Future.microtask와 Future.delayed 비교
        - 실행시점: 현재 코드 실행이 끝난 직후 / 지정한 시간이 지난 후 실행
        - UI 영향: 영향 없음 (즉시 실행) / 일정 시간이 지나야 실행
        - 우선 순위: 마이크로태스크 큐 (우선 실행) / 일반 이벤트 루프(대기)
    - 동작 방식
        - 다트의 이벤트 루프는 두가지 큐를 가짐
            - 마이크로태스크 큐
                - 현재 실행 중인 코드가 끝나면 가장 먼저 실행
            - 이벤트 큐
                - UI 이벤트, 네트워크 응답, Future.delayed, setState() 등 실행 대기 
    - UI 최적화
        - 마이크로태스크 사용하지 않는 경우 UI 지연 발생 가능성 존재
        - initState 내에서 delayed로 처리할 경우 UI 느려질 가능성 존재 

- Flutter에서 Web과 Mobile 개발의 차이점
    - 공통
        - Web과 Mobile(iOS/Android)에서 동일한 코드베이스를 사용할 수 있는 크로스플랫폼 프레임워크
    - Flutter Web과 Mobile 개발의 주요 차이점
        - 렌더링 방식 차이
            - Flutter Web
	            - HTML + CSS + CanvasKit(옵션)으로 렌더링
	            - CanvasKit 사용 시 성능 향상 가능 (WebGL 기반)
	        - Flutter Mobile (iOS/Android)
	            - Skia 엔진을 사용하여 네이티브 수준의 성능 제공
	            - 모든 위젯을 픽셀 단위로 직접 렌더링
            - 차이점
	            - 웹은 브라우저 기반 렌더링 방식 사용 → 성능이 제한될 수 있음
	            - 모바일은 직접 Skia 엔진을 사용하여 더 부드럽고 빠름
        - 성능 차이
	        - Flutter Web
	            - HTML, CSS, JavaScript의 DOM 구조를 사용해야 해서 성능 저하 가능
	            - 복잡한 애니메이션이나 고해상도 그래픽 작업이 모바일보다 느릴 수 있음
	            - CanvasKit 사용 시 성능 개선 가능하지만, 로드 시간이 증가
	        - Flutter Mobile
	            - Skia 그래픽 엔진 덕분에 네이티브 수준의 성능 제공
	            - 모든 위젯을 직접 그려서 GPU를 최대한 활용 가능
            - 차이점
	            - Flutter Web은 HTML 기반이라 모바일보다 성능이 떨어질 수 있음
	            - 복잡한 애니메이션이나 그래픽이 많은 경우 모바일이 더 부드럽게 동작
        - 플랫폼 API 접근 차이
            - Flutter Web
	            - 웹 브라우저 환경에서 동작하므로, 파일 시스템, 블루투스, 센서, 네이티브 API 접근 제한
	            - 브라우저에서 지원하는 API(WebRTC, LocalStorage 등)만 사용 가능
	        - Flutter Mobile
	            - 네이티브 API 완전 접근 가능 (카메라, GPS, 블루투스, 센서 등)
	            - MethodChannel을 통해 네이티브(Android, iOS) 기능 확장 가능
            - 차이점
	            - 웹에서는 브라우저 보안 정책(CORS, 파일 접근 제한)으로 네이티브 기능 접근이 제한됨
	            - 모바일에서는 네이티브 API를 자유롭게 활용 가능
        - 상태 관리(State Management)
	        - Flutter Web
	            - 새로고침(F5) 시 상태가 초기화됨 (앱의 상태가 사라짐)
	            - URL을 통한 네비게이션 필요 (페이지 이동 시 상태 유지 어려움)
	        - Flutter Mobile
	            - 앱이 백그라운드로 가도 상태 유지 가능
                - 네비게이션이 Stack 기반이므로 자연스럽게 상태 유지
            - 차이점
	            - 웹에서는 페이지 새로고침 시 상태가 초기화될 수 있으므로, SharedPreferences, Firebase 등을 활용하여 상태 저장 필요
	            - 모바일에서는 네비게이션과 상태 관리가 더 자연스럽게 동작
        - 네비게이션 방식 차이
            - Flutter Web
	            - URL 기반 네비게이션 사용 가능 (Flutter 2.0부터 go_router 지원)
	            - 브라우저의 “뒤로 가기” 버튼과 연동 가능
	        - Flutter Mobile
	            - Stack 기반 네비게이션 사용 (Navigator API)
	            - URL 기반 네비게이션이 기본적으로 필요하지 않음
            - 차이점
	            - 웹에서는 URL을 기반으로 페이지 전환을 고려해야 함
	            - 모바일에서는 Navigator를 통한 Stack 방식이 기본
        - 네이티브 기능 연동 차이
	        - Flutter Web
                - 웹 브라우저 환경에서 실행되므로, 네이티브 기능(카메라, 블루투스 등) 사용이 제한적
                - flutter_web_plugins 패키지를 사용하여 일부 기능 지원 가능
            - Flutter Mobile
                - MethodChannel을 활용하여 네이티브(Android/iOS) 기능과 완전한 연동 가능
	            - 카메라, GPS, 바이오메트릭 인증, NFC 등 모든 네이티브 기능을 사용할 수 있음
            - 차이점
	            - 웹은 브라우저에서 지원하는 API만 사용 가능
	            - 모바일은 네이티브 API까지 활용 가능하여 확장성이 뛰어남
        - 앱 배포 방식 차이
	        - Flutter Web
	            - 배포 방식 → 정적 웹 사이트로 배포 가능 (Firebase Hosting, Netlify, AWS S3)
	            - 사용자는 브라우저에서 실행 가능
	        - Flutter Mobile
	            - 배포 방식 → App Store, Google Play에 업로드 필요
	            - 사용자는 앱을 설치해야 사용 가능
            - 차이점
	            - 웹은 배포가 간편하고 URL을 통해 접속 가능
	            - 모바일은 스토어 등록 과정이 필요하지만 네이티브 경험 제공


- Flutter에서 Adaptive UI를 구현하는 방법
  - Adaptive UI 개요
	  - Adaptive UI는 다양한 디바이스(스마트폰, 태블릿, 데스크톱, 웹)에 따라 자동으로 UI가 적응하는 인터페이스
	  - 반응형(Responsive UI)과 차이점
	    - Responsive UI: 같은 UI 구성 요소를 크기만 조정하여 화면에 맞춤
	    - Adaptive UI: 플랫폼과 디바이스 종류에 따라 완전히 다른 UI 구성을 사용

  - Flutter의 Adaptive UI 특징
	  - 단일 코드베이스로 Android, iOS, 웹, 데스크톱, 태블릿 등 다양한 플랫폼을 지원
	  - MediaQuery, LayoutBuilder, OrientationBuilder, AdaptiveLayout, Platform.isAndroid 등의 API를 활용하여 구현

  - Adaptive UI를 구현하는 방법
    - 방법 1: MediaQuery 사용 (디바이스 크기 기반)
    - 방법 2: LayoutBuilder 사용 (위젯 크기 기반)
    - 방법 3: OrientationBuilder 사용 (가로/세로 모드 대응)
    - 방법 4: Platform.isAndroid & Platform.isIOS (플랫폼별 UI 차별화)
    - 방법 5: AdaptiveLayout 패키지 사용 (멀티 디바이스 대응)

  - 결론
    - Flutter에서 Adaptive UI를 구현하는 방법
      - MediaQuery: 디바이스의 화면 크기 기반, 화면 크기에 따라 UI 변경
      - LayoutBuilder: 부모 위젯 크기 기반, 동적 UI 조정
      - OrientationBuilder: 가로/세로 모드 대응, 세로/가로 모드별 UI 변경
      - Platform.isAndroid / isIOS:	운영체제 기반 UI 변경, Android와 iOS에서 다른 UI 적용
      - AdaptiveLayout: 패키지	자동 크기 대응, 스마트폰/태블릿/데스크탑 UI 자동 조정

  - 추천 조합
	  - 반응형 UI: MediaQuery + LayoutBuilder
	  - 플랫폼별 UI 변경: Platform.isAndroid / isIOS
	  - 다양한 디바이스 지원: AdaptiveLayout 패키지 사용
    - Adaptive UI를 사용하면 다양한 기기에서 최적의 사용자 경험을 제공할 수 있으며, Flutter에서는 여러 방법을 조합하여 효과적으로 구현 가능

- Isolate 설명
  - 개요
    - Isolate.run() – Flutter 3.7부터 도입된 간단한 비동기 Isolate 실행 방법
    - Flutter 3.7부터 새로운 API Isolate.run()이 도입됨
    - compute()와 유사하지만 더 직관적이고 사용이 편리한 방식

  - Isolate.run()이란?
    - 기존 compute()와 비슷한 방식으로 백그라운드에서 무거운 연산을 실행하는 기능을 제공
    - Isolate.run()을 사용하면 별도의 Isolate를 생성하여 코드 실행 후 결과를 반환받을 수 있음

  - 장점
	  - compute()보다 더 직관적인 문법
	  - async/await을 지원하여 비동기 방식으로 사용 가능
	  - 일회성 작업에 적합 (사용 후 자동 종료)

2. Isolate.run() 기본 사용법
  - 예제 (기존의 compute()와 비슷하지만, async/await을 직접 사용할 수 있어서 코드가 더 간결)
    ```dart
    Future<void> runHeavyTask() async {
      int result = await Isolate.run(() => heavyCalculation(1000000000));
      setState(() {
        _result = "결과: $result";
      });
    }
    ```
  - 코드 설명
	  - Isolate.run(() => heavyCalculation(1000000000))
    - 백그라운드에서 heavyCalculation 실행 후 결과 반환
	    - UI가 멈추지 않고 정상적으로 작동
	    - async/await을 활용하여 코드를 깔끔하게 작성 가능

  - 정리
	  - Isolate.run() → compute()보다 더 직관적인 방식, async/await 지원, compute의 진화판
	  - compute() → 기존 방식, 단순한 연산에 적합
	  - Isolate.spawn() → SendPort/ReceivePort를 이용해 데이터 송수신이 필요한 경우 사용
    - Isolate.run() 사용 시 주의할 점
      - UI 관련 코드를 실행할 수 없음
	      - Isolate.run()은 메인 스레드에서 실행되지 않으므로 setState() 호출 불가
	      - UI 업데이트는 반환된 값으로 메인 스레드에서 실행해야 함

      - 데이터 공유 불가
	      - Isolate는 메모리를 공유하지 않음 → 복사된 데이터만 사용 가능
	      - 대용량 데이터 전달 시 성능 저하 가능

  - 결론
    - Flutter 3.7 이상에서는 Isolate.run()을 적극 활용
    - compute()보다 직관적이며, async/await 지원으로 코드가 간결
    - 장기 실행 작업이 아니라면 Isolate.spawn()보다 간편하게 사용 가능

- Flutter에서 BLoC 패턴 사용 이유
  - BLoC (Business Logic Component) 패턴은 Flutter 앱의 상태 관리를 효율적으로 하기 위해 사용되는 아키텍처 패턴
  - 이유
    - UI와 비즈니스 로직을 분리하여 코드의 재사용성과 유지보수성을 향상
    - 이벤트 기반(Streams)을 활용하여 UI 상태 변화를 효율적으로 관리
    - Flutter의 선언형(Declarative) UI 방식과 자연스럽게 연동 가능

  - BLoC 패턴이 필요한 이유
    - (1) UI와 비즈니스 로직의 분리
      - 일반적인 Flutter 위젯 내부에서 setState()를 사용하면 비즈니스 로직과 UI 코드가 섞여 복잡한 코드가 됨
      - BLoC을 사용하면 UI 로직과 상태 관리가 분리되므로 코드의 가독성이 향상됨

    - (2) 상태 관리의 최적화
      - setState()를 사용하면 위젯 트리가 불필요하게 다시 빌드됨
      - BLoC은 Stream을 활용하여 필요한 위젯만 다시 빌드
      - 불필요한 UI 업데이트를 방지하여 앱 성능 향상
  
    - (3) 이벤트 기반 상태 관리 (Event → State)
      - BLoC 패턴은 이벤트(Event) → 상태(State) 변화를 관리
      - 비즈니스 로직이 이벤트를 받고 새로운 상태를 방출(emit)
      - UI는 이 새로운 상태를 구독(Subscribe)하여 자동으로 업데이트됨

  - BLoC 흐름
    - UI에서 이벤트 발생 (사용자의 액션: 버튼 클릭 등)
    - BLoC에서 이벤트를 받아 처리하고 새로운 상태를 생성
    - Stream을 통해 UI에 새로운 상태 전달
    - UI는 새로운 상태를 반영하여 업데이트됨

  - BLoC 패턴의 핵심 개념
    - Event: 사용자의 액션 (버튼 클릭, API 요청 등)
    - State: 현재 UI의 상태
    - Bloc: Event를 받아 처리하고 새로운 State를 방출
    - Stream: 이벤트 흐름을 비동기적으로 관리

  - BLoC 패턴 적용 예제
    - Step 1: BLoC 패키지 설치
      - flutter_bloc: ^8.1.3  # 최신 버전 확인 후 적용
    - Step 2: 이벤트 정의
      - 이벤트(Event)는 사용자의 액션을 정의 (예: 증가 버튼 클릭)
      ```dart
      abstract class CounterEvent {}

      class Increment extends CounterEvent {}  // 증가 버튼 클릭 이벤트
      ```

    - Step 3: 상태(State) 정의
      - 상태(State)는 UI가 표시해야 할 데이터 (예: 현재 숫자 값)
      ```dart
      abstract class CounterState {
        final int counter;
        CounterState(this.counter);
      }

      class CounterInitial extends CounterState {
        CounterInitial() : super(0);  // 초기값 0
      }

      class CounterUpdated extends CounterState {
        CounterUpdated(int counter) : super(counter);
      }
      ```

    - Step 4: BLoC 로직 구현
      - BLoC은 이벤트를 받고 새로운 상태를 방출(emit)
      - on<Increment>()를 통해 Increment 이벤트 발생 시 counter +1 실행
      ```dart
      import 'package:flutter_bloc/flutter_bloc.dart';

      class CounterBloc extends Bloc<CounterEvent, CounterState> {
        CounterBloc() : super(CounterInitial()) {
          on<Increment>((event, emit) {
            emit(CounterUpdated(state.counter + 1));  // 새로운 상태 방출 (emit)
          });
        }
      }
      ```

    - Step 5: UI에서 BLoC 적용
      ```dart
      import 'package:flutter/material.dart';
      import 'package:flutter_bloc/flutter_bloc.dart';

      void main() {
        runApp(MyApp());
      }

      class MyApp extends StatelessWidget {
        @override
        Widget build(BuildContext context) {
          return MaterialApp(
            home: BlocProvider(
              create: (context) => CounterBloc(),
              child: CounterScreen(),
            ),
          );
        }
      }

      class CounterScreen extends StatelessWidget {
        @override
        Widget build(BuildContext context) {
          final counterBloc = context.read<CounterBloc>();

          return Scaffold(
            appBar: AppBar(title: Text("Flutter BLoC Counter")),
            body: Center(
              child: BlocBuilder<CounterBloc, CounterState>(
                builder: (context, state) {
                  return Text("Count: ${state.counter}", style: TextStyle(fontSize: 30));
                },
              ),
            ),
            floatingActionButton: FloatingActionButton(
              onPressed: () => counterBloc.add(Increment()),  // 이벤트 발생
              child: Icon(Icons.add),
            ),
          );
        }
      }
      ```
      - BlocProvider 를 사용하여 CounterBloc을 앱에 주입
      - BlocBuilder 를 사용하여 상태(State) 가 변경될 때만 UI 업데이트
      - counterBloc.add(Increment()) 를 통해 이벤트(Event) 발생

  - BLoC 패턴을 사용하는 이유
    - UI와 비즈니스 로직 분리: UI 코드와 상태 관리 코드가 분리되어 유지보수 용이
    - Flutter의 선언형 UI 방식과 자연스럽게 연결: 이벤트 기반 상태 관리로 UI 자동 업데이트
    - 메모리 효율적 & 퍼포먼스 최적화: setState()보다 성능이 뛰어나며, 필요한 부분만 다시 빌드
    - 코드 재사용성 증가: BLoC을 여러 위젯에서 재사용 가능
    - 비동기 처리 최적화 (API, DB, Stream): Stream을 기반으로 상태를 효율적으로 관리

  - 결론
    - BLoC 패턴을 사용하면 Flutter 앱의 상태 관리를 효율적으로 할 수 있음
    - 이벤트(Event) → BLoC에서 상태(State) 변환 → UI 업데이트 흐름이 명확함
    - 대규모 프로젝트에서는 BLoC을 적용하면 유지보수가 용이하고, 성능이 향상됨
    - Flutter 공식 추천 패턴 중 하나이며, Google이 지원하는 강력한 상태 관리 솔루션
    - BLoC 패턴은 Flutter에서 "확장성, 성능, 유지보수성"을 동시에 해결하는 강력한 아키텍처 패턴

- Flutter 공식 추천 및 지원하는 상태 관리 라이브러리 (2024년 기준)
  - Flutter 공식 문서 및 커뮤니티에서 가장 많이 사용되고, 유지보수되는 라이브러리들 정보
    - Riverpod: Flutter 공식 문서에 소개됨, Google I/O에서 언급됨
    - Provider:	Flutter 공식 문서에서 소개됨,	Flutter 팀이 초기에 지원한 패턴
    - BLoC (flutter_bloc): Flutter 공식 문서에서 소개됨, Google I/O에서 언급됨
    - GetX: Flutter 공식 문서에서 소개되지 않음, Google 공식 컨퍼런스에서 언급되지 않음

  - Flutter 공식 문서에서 추천하는 상태 관리 라이브러리
    - Riverpod
    - Provider
    - BLoC (flutter_bloc)

  - Flutter 공식 문서: State Management
    - 현재 가장 많이 사용되는 상태 관리 라이브러리
      - (1) Riverpod (Flutter 공식 문서에서 적극 추천)
        - Riverpod은 Provider의 단점을 개선한 상태 관리 라이브러리
        - Flutter 공식 문서에서도 추천하는 패턴 중 하나
        - Flutter 공식 문서에서 소개됨
        - Provider의 단점을 개선
        - Flutter 독립 실행형(Standalone) 상태 관리 가능 (위젯과 분리)
        - 컴파일 타임에서 오류 감지 가능 (안전한 상태 관리)
        - Provider보다 성능 최적화, 위젯 독립성 증가
        - Riverpod 사용 예제
          ```dart
          import 'package:flutter_riverpod/flutter_riverpod.dart';

          final counterProvider = StateProvider<int>((ref) => 0);

          class CounterScreen extends ConsumerWidget {
            @override
            Widget build(BuildContext context, WidgetRef ref) {
              final counter = ref.watch(counterProvider);

              return Scaffold(
                body: Center(child: Text('$counter')),
                floatingActionButton: FloatingActionButton(
                  onPressed: () => ref.read(counterProvider.notifier).state++,
                  child: Icon(Icons.add),
                ),
              );
            }
          }
          ```

      - (2) Provider (초기 Flutter 공식 추천, 여전히 많이 사용됨)
        - Provider는 Flutter 팀이 공식적으로 지원했던 상태 관리 라이브러리로, 가장 많이 사용되었음
        - Riverpod이 등장하면서 단점(위젯 의존성, DI 어려움 등)이 개선
        - Flutter 공식 문서에서 여전히 추천하지만, 최신 프로젝트에서는 Riverpod으로 이동하는 추세
        - Provider는 기존 코드베이스에서 유지보수할 때 유용
        - Provider 사용 예제
          ```dart
          final counterProvider = ChangeNotifierProvider((_) => CounterModel());

          class CounterModel extends ChangeNotifier {
            int count = 0;

            void increment() {
              count++;
              notifyListeners();
            }
          }
          ```

      - (3) BLoC (flutter_bloc) - 대규모 프로젝트에서 추천
        - BLoC 패턴은 Google의 공식 컨퍼런스 (Google I/O)에서 소개된 상태 관리 패턴
        - 이벤트(Event) → 상태(State)로 변환하여 UI를 업데이트하는 방식이며, 대규모 프로젝트에서 가장 많이 사용
        - 대규모 앱(기업용, 복잡한 앱)에서 강력한 상태 관리 기능 제공
        - Flutter 공식 문서 & Google I/O에서 추천됨
        - 작은 앱에서는 코드가 복잡해질 수 있음 (Riverpod보다 코드량 많음)
        - BLoC 사용 예제
          ```dart
          class CounterBloc extends Bloc<CounterEvent, CounterState> {
            CounterBloc() : super(CounterInitial()) {
              on<Increment>((event, emit) => emit(CounterUpdated(state.counter + 1)));
            }
          }
          ```

      - (4) GetX (Flutter 공식 문서에서는 추천하지 않음)
        - GetX는 가장 간결한 상태 관리 라이브러리이지만, 공식적으로 추천되지 않는 이유가 있음.
        - Flutter 공식 문서에서 소개되지 않음
        - Google I/O 등 공식 컨퍼런스에서 언급되지 않음
        - 설계 방식이 일반적인 상태 관리 패턴과 다름 (의존성 관리와 상태 관리가 혼합됨)
        - 메모리 누수 및 유지보수 어려움이 보고됨
        - Flutter 공식 문서에서 언급되지 않으며, 장기적인 유지보수가 어려운 편
        - 기업 및 대규모 프로젝트에서 추천되지 않음 (메모리 누수 이슈 존재)
        - 작은 프로젝트에서는 코드가 간결해 빠르게 개발 가능
        - GetX 사용 예제
          ```dart
          class CounterController extends GetxController {
            var count = 0.obs;

            void increment() => count++;
          }

          class CounterScreen extends StatelessWidget {
            final CounterController controller = Get.put(CounterController());

            @override
            Widget build(BuildContext context) {
              return Scaffold(
                body: Center(child: Obx(() => Text("${controller.count}"))),
                floatingActionButton: FloatingActionButton(
                  onPressed: controller.increment,
                  child: Icon(Icons.add),
                ),
              );
            }
          }
          ```

  - 결론: 2024년 가장 추천되는 Flutter 상태 관리 라이브러리
    - Riverpod (최신 추천), 가장 추천됨 (Flutter 공식 문서 추천),	Provider 개선, 성능 최적화, 유지보수 용이
    - Provider (기존 추천), 여전히 많이 사용됨, 초기 Flutter 공식 추천 방식, 유지보수 용이
    - BLoC (대규모 앱 추천), Google I/O에서 추천됨, 대규모 프로젝트에서 강력한 상태 관리
    - GetX (공식 추천 아님), Flutter 공식 문서 미포함, 빠른 개발 가능하지만 유지보수 어려움

  - 결론 요약
    - 최신 Flutter 프로젝트에서는 Riverpod을 사용하는 것이 가장 적절함
    - 기존 코드베이스에서 Provider를 유지보수하는 것은 문제 없음
    - 대규모 프로젝트에서는 BLoC이 강력한 상태 관리 솔루션 제공
    - GetX는 Flutter 공식 문서에서 추천되지 않으며, 장기적인 유지보수에 어려움이 있음

  - 개인/기업용 Flutter 프로젝트 상태 관리 선택 가이드
    - 소규모 앱 (빠른 개발): Riverpod / GetX (Riverpod은 유지보수 용이, GetX는 간결함)
    - 중규모 앱 (스타트업, 개인 프로젝트): Riverpod / Provider (Provider는 사용법이 간단하고 안정적)
    - 대규모 앱 (기업, 금융, 커머스 등): BLoC / Riverpod (복잡한 상태 관리 최적화 가능)
    - 기존 Provider 프로젝트 유지보수: Provider 유지, 큰 문제 없으면 유지
    - 새로운 Flutter 프로젝트: Riverpod 추천 (최신 기술, 안정적인 구조)
    - 2024년 Flutter 상태 관리는 Riverpod이 가장 유망한 선택이라 생각됨

- Flutter에서 Sliver Widgets을 사용하는 이유
  - Sliver 개념
    - CustomScrollView 안에서 유연하게 동작하는 스크롤 가능한 영역.
    - Sliver는 영어로 '얇은 조각'이라는 뜻이며, 스크롤 영역을 조각 단위로 조립하듯 구성함.

  - 사용하는 이유
    - 고성능 커스터마이징된 스크롤 UI 구현 가능
    - AppBar가 스크롤되며 사라지거나 나타나는 Flexible AppBar
    - 리스트, 그리드, 고정 헤더 등 다양한 컴포넌트를 조합 가능

  - 대표 위젯
    - SliverAppBar: 스크롤에 따라 확장/축소되는 앱바
    - SliverList, SliverGrid: 커스텀 스크롤 리스트/그리드
    - SliverPersistentHeader: 고정 헤더 영역 구현

  - 예시 코드
    ```dart
    CustomScrollView(
      slivers: [
        SliverAppBar(...),
        SliverList(delegate: ...),
      ],
    )
    ```
    - 일반적인 ListView보다 더 복잡하고 유연한 스크롤 레이아웃을 구성할 수 있음.

- Flutter에서 Navigator 1.0과 2.0의 차이점
  - Navigator 1.0
    - 방식: 명령형 (Imperative)
    - 사용법: Navigator.push, Navigator.pop
    - URL 동기화: 불완전
    - 상태관리 통합: 수동 처리 필요
    - 복잡한 구조: 구현 어려움
    
  - Navigator 2.0
    - 방식: 선언형 (Declarative)
    - 사용법: Router, RouteInformaionParser, RouterDelegate
    - URL 동기화: 브라우저 주소창과 연동 가능
    - 상태관리 통합: 앱 상태와 네비게이션 통합 용이
    - 복잡한 구조: 복잡한 UI 상태 반영 쉬움

  - 요약
    - Navigator 1.0 -> 간단한 앱
    - Navigator 2.0 -> 웹/복잡한 플로우 앱 유리
      - (예: 로그인 -> 대시보드 -> 설정 등 상태 기반 라우팅)

- Flutter에서 Riverpod과 Provider의 차이점
  - 차이점
    - Provider
      - 작성 방식: Flutter 위젯에 의존
      - 전역 접근: BuildContext 필요
      - 테스트: 상대적으로 복잡
      - 상태 추적: context.watch 등 의존
      - 안전성: runtime 오류 가능
      - 성능 및 기능: 적절하지만 제한 존재

    - Riverpod
      - 작성 방식: 완전히 독립적인 선언형 코드 가능
      - 전역 접근: 어디서든 접근 가능 (context 불필요)
      - 테스트: 독립적인 테스트 용이
      - 상태 추적: 자동 상태 추적 (ref.watch)
      - 안전성: 컴파일 타임 타입 안정성 우수
      - 성능 및 기능: 캐시, Lazy 초기화 등 고급 기능 내장

  - 요약
    - Provider: 가볍고 기본적인 상태 관리. 초보자에게 적합.
    - Riverpod: 더 모듈화, 안전성, 확장성이 뛰어난 최신 상태 관리 솔루션

- Flutter에서 InheritedWidget의 역할
  - 정의
    - 트리 구조 상의 하위 위젯들에게 데이터를 효율적으로 전달하기 위한 Flutter의 기본적인 상태 전달 메커니즘.

  - 주요 특징
    - 위젯 트리 상에서 context를 통해 데이터를 공유할 수 있음
    - 특정 위젯이 변경되면 이를 구독하는 하위 위젯들만 선택적으로 리빌드됨
    - Provider, Theme, MediaQuery 등 많은 Flutter 기본 기능이 내부적으로 InheritedWidget을 사용

  - 예시
    ```dart
    class MyInherited extends InheritedWidget {
      final int counter;

      const MyInherited({required this.counter, required Widget child})
          : super(child: child);

      static MyInherited? of(BuildContext context) {
        return context.dependOnInheritedWidgetOfExactType<MyInherited>();
      }

      @override
      bool updateShouldNotify(MyInherited oldWidget) => oldWidget.counter != counter;
    }
    ```
    - 직접 사용은 복잡, 보통은 Provider 같은 라이브러리로 추상화하여 사용

- Flutter에서 Provider와 Bloc의 차이점
  - Provider
    - 아키텍쳐 성격: 단순한 상태 공유 및 리빌드 제어
    - 학습 난이도: 낮음 (간결하고 직관적)
    - 상태 변경 방식: notifyListeners()로 직접 통지
    - 의존성 주입: 지원 (via Provider.of)
    - 테스트 용이성: 쉬움
  - Bloc
    - 아키텍쳐 성격: 명확한 계층 구조의 상태 관리 패턴
    - 학습 난이도: 높음 (스트림과 이벤트 기반)
    - 상태 변경 방식: 이벤트 -> 비즈니스 로직 처리 -> 상태 전파 (스트림 기반)
    - 의존성 주입: BlocProvider로 관리
    - 테스트 용이성: 매우 뛰어남 (로직 분리 가능)

  - 요약
    - Provider: 간단한 앱에서 UI와 상태를 손쉽게 관리 가능
    - Bloc: 복잡한 앱 구조, 명확한 Event-Driven 구조가 필요할 때 적합
      - Bloc은 공식적으로 flutter_bloc 패키지와 함께 사용
      - 상태 흐름을 명확하게 추적하고 테스트하기 좋음

- Flutter에서 Isolates를 활용하는 이유
  - 정의
    - Dart의 병렬 처리 유닛.
    - Isolate는 각각 별도의 메모리 공간과 이벤트 루프를 가지며, 서로 메시지를 통해 통신
  
  - 사용 이유
    - 플러터는 단일 스레드 UI 모델을 사용하므로, 무거운 연산 작업이 메인쓰레드를 막아 UI가 멈출 수 있음.
    - 예: JSON 파싱, 이미지 디코딩, 파일 I/O 등 -> Isolate에서 수행

  - 기본 사용 예
    ```dart
    import 'dart:isolate';

    void heavyComputation(SendPort sendPort) {
      int result = 0;
      for (int i = 0; i < 100000000; i++) result += i;
      sendPort.send(result);
    }
    ```

  - 대체 옵션
    - compute() 함수: Isolate를 간편하게 사용하는 고수준 API
      ```dart
      int sumUpTo(int n) {
        return List.generate(n, (i) => i).reduce((a, b) => a + b);
      }
      final result = await compute(sumUpTo, 100000000);
      ```
      - UI 프레임이 끊기지 않도록 비동기 작업을 분리할 때 매우 유용

- InheritedWidget 기반 Provider 직접 구현 방법
  - 목표
    - Flutter의 Provider 없이 InheritedWidget으로 상태 공유 구조를 직접 만든다.

  - 예제 (Counter 상태 공유)
    ```dart
    // Step 1: 상태 클래스 정의
    class Counter extends ChangeNotifier {
      int _count = 0;
      int get count => _count;

      void increment() {
        _count++;
        notifyListeners();
      }
    }

    // Step 2: InheritedWidget 정의
    class CounterProvider extends InheritedWidget {
      final Counter counter;

      const CounterProvider({
        Key? key,
        required this.counter,
        required Widget child,
      }) : super(key: key, child: child);

      static CounterProvider? of(BuildContext context) {
        return context.dependOnInheritedWidgetOfExactType<CounterProvider>();
      }

      @override
      bool updateShouldNotify(CounterProvider oldWidget) =>
          counter != oldWidget.counter;
    }
    ```

  - 사용 예제
    - IngeritedWidget + ChangeNotifier + AnimatedBuilder 조합으로 Provider 유사 기능 구현
    ```dart
    void main() {
      final counter = Counter();
      runApp(CounterProvider(counter: counter, child: MyApp()));
    }

    class MyApp extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        final counter = CounterProvider.of(context)!.counter;

        return MaterialApp(
          home: Scaffold(
            appBar: AppBar(title: Text('Custom Provider')),
            body: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  AnimatedBuilder(
                    animation: counter,
                    builder: (_, __) => Text('Count: ${counter.count}'),
                  ),
                  ElevatedButton(
                    onPressed: () => counter.increment(),
                    child: Text('Increment'),
                  ),
                ],
              ),
            ),
          ),
        );
      }
    }
    ```

- AnimatedBuilder 개념
  - 정의
    - Animation 값이 변할 때마다 위젯을 효율적으로 다시 빌드해주는 플러터 위젯
    - setState() 없이도 애니매이션에 따라 UI를 업데이트할 수 있음.
    - 불필요 리렌더링을 방지하고 성능 최적화

  - 기본 사용 예
    - AnimatedBuilder는 효율적으로 애니매이션에 따라 위젯을 변경할 수 있게 해 줌
    ```dart
    class MyAnimatedBox extends StatefulWidget {
      @override
      _MyAnimatedBoxState createState() => _MyAnimatedBoxState();
    }

    class _MyAnimatedBoxState extends State<MyAnimatedBox>
        with SingleTickerProviderStateMixin {
      late AnimationController _controller;
      late Animation<double> _sizeAnimation;

      @override
      void initState() {
        super.initState();
        _controller = AnimationController(
          duration: Duration(seconds: 2),
          vsync: this,
        )..repeat(reverse: true);

        _sizeAnimation = Tween<double>(begin: 100, end: 200).animate(_controller);
      }

      @override
      Widget build(BuildContext context) {
        return AnimatedBuilder(
          animation: _sizeAnimation,
          builder: (context, child) {
            return Container(
              width: _sizeAnimation.value,
              height: _sizeAnimation.value,
              color: Colors.blue,
            );
          },
        );
      }

      @override
      void dispose() {
        _controller.dispose();
        super.dispose();
      }
    }
    ```

- Bloc 구조도 설명
  - BLoC 아키텍처 핵심 구성
    ```scss
      [ UI Layer ]
          ↓ ↑ (BlocBuilder / BlocListener)
        [ Bloc ]
        ↓       ↑
    [ Event ] → [ State ]
        ↓       ↑
    [ Repository (API, DB 등) ]
    ```

  - 구성 요소
    - (1) UI (Widget)
      - BlocProvider로 Bloc 주입
      - BlocBuilder로 상태 수신
      - Bloc.add()로 이벤트 전송
    - (2) Event
      - 사용자 상호작용 또는 시스템 이벤트를 표현하는 클래스
    - (3) State
      - UI가 반응할 수 있는 단일 상태 값 클래스
    - (4) Bloc
      - on<Event> 핸들러로 이벤트 처리
      - 처리 결과를 emit(State)로 알림
    - (5) Repository
      - 외부 API, DB 등과의 데이터 통신 추상화

  - 예시
    ```dart
    // Event
    abstract class CounterEvent {}
    class IncrementEvent extends CounterEvent {}

    // State
    class CounterState {
      final int count;
      CounterState(this.count);
    }

    // Bloc
    class CounterBloc extends Bloc<CounterEvent, CounterState> {
      CounterBloc() : super(CounterState(0)) {
        on<IncrementEvent>((event, emit) {
          emit(CounterState(state.count + 1));
        });
      }
    }
    ```
    - UI는 BlocBuilder를 통해 상태를 받고, 사용자는 Bloc에 이벤트만 전달하면 됨. (Unidirectional)

- Isolate 고급 활용 패턴
  - 문제: compute()는 단일 인자만 가능하고 커스터마이징이 어렵다.
  - 직접 Isolate 제어 예제
    - 이 방식은 파라미터를 여러 개 넘기거나, long-running isolate를 관리하는 데 적합
    ```dart
    import 'dart:isolate';

    Future<int> runHeavyTask(int value) async {
      final receivePort = ReceivePort();
      await Isolate.spawn(_isolateEntry, [receivePort.sendPort, value]);

      return await receivePort.first as int;
    }

    void _isolateEntry(List<dynamic> args) {
      final SendPort sendPort = args[0];
      final int input = args[1];

      // 무거운 연산
      int result = 0;
      for (int i = 0; i < input; i++) result += i;

      sendPort.send(result);
    }
    ```

  - 별도의 Isolate lifecycle 관리 예
    ```dart
    class IsolateManager {
      Isolate? _isolate;
      ReceivePort? _receivePort;

      Future<void> start() async {
        _receivePort = ReceivePort();
        _isolate = await Isolate.spawn(_entryPoint, _receivePort!.sendPort);

        _receivePort!.listen((message) {
          print("Main received: $message");
        });
      }

      void stop() {
        _isolate?.kill(priority: Isolate.immediate);
        _receivePort?.close();
      }

      static void _entryPoint(SendPort sendPort) {
        sendPort.send("Isolate started");
      }
    }
    ```
    - 이 구조는 background 연산 작업을 장시간 수행하거나, 사용자 동작과 무관하게 지속적으로 처리해야 하는 작업에 적합

  - 전체 정리 요약
    - InheritedWidget Provider
      - 직접 구현시 context.dependOnInheritedWidgetOfExactType, ChangeNotifier + AnimatedBuilder로 리렌더링 처리
    - Bloc 구조
      - UI -> Event -> Bloc -> State -> UI로 흐름이 분리되어 유지보수성 증가
    - Isolate 고급 활용
      - compute() 외에도 ReceivePort, SendPort, Isolate.spawn을 통해 커스텀 Isolate 제어 가능

- Flutter에서 Custom Painter를 활용하는 방법
  - 정의
    - 캔버스를 직접 다루어 도형, 그래픽, 차트, 애니메이션 등 저수준 그래픽을 그릴 수 있는 방법.
    - CustomPaint 위젯과 함께 사용.

  - 사용 예
    ```dart
    class MyCirclePainter extends CustomPainter {
      @override
      void paint(Canvas canvas, Size size) {
        final paint = Paint()
          ..color = Colors.red
          ..style = PaintingStyle.fill;

        canvas.drawCircle(size.center(Offset.zero), 50, paint);
      }

      @override
      bool shouldRepaint(CustomPainter oldDelegate) => false;
    }

    // 사용
    CustomPaint(
      size: Size(200, 200),
      painter: MyCirclePainter(),
    )
    ```
    - 복잡한 UI, 차트, 곡선 애니메이션 등에 활용 가능

- Flutter에서 Native Code(Android, iOS)를 호출하는 방법
  - 방법: Platform Channels 사용
    - Flutter <-> Android(Java/Kotlin), iOS(Swift/Obj-C) 간 양방향 통신 가능
    - 표준 플랫폼 채널: MethodChannel, EventChannel, BasicMessageChannel

  - 예제 (Android)
    ```dart
    static const platform = MethodChannel('com.example/my_channel');

    Future<void> getBatteryLevel() async {
      final int batteryLevel = await platform.invokeMethod('getBatteryLevel');
    }
    ```
    ```kotlin
    class MainActivity : FlutterActivity() {
    private val CHANNEL = "com.example/my_channel"

        override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
            super.configureFlutterEngine(flutterEngine)

            MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL).setMethodCallHandler {
                call, result ->
                if (call.method == "getBatteryLevel") {
                    val level = getBatteryLevel()
                    result.success(level)
                }
            }
        }
    }
    ```
    - 실시간 센서, 시스템 API, BLE 등 네이티브 기능 호출에 활용

- Flutter에서 Firebase Analytics를 활용하는 방법
  - 설치
    ```bash
    flutter pub add firebase_core
    flutter pub add firebase_analytics
    ```

  - 초기화
    ```dart
    void main() async {
      WidgetsFlutterBinding.ensureInitialized();
      await Firebase.initializeApp();
      runApp(MyApp());
    }
    ```
    
  - 기본 사용
    ```dart
    import 'package:firebase_analytics/firebase_analytics.dart';

    FirebaseAnalytics analytics = FirebaseAnalytics.instance;

    // 사용자 정의 이벤트 전송
    await analytics.logEvent(
      name: 'purchase',
      parameters: {
        'item_id': '123',
        'value': 9.99,
      },
    );

    // 화면 추적
    await analytics.setCurrentScreen(
      screenName: 'HomePage',
    );
    ```

  - 주요 기능
    - 사용자 행동 추적 (버튼 클릭, 구매 등)
    - 자동 수집 이벤트 (앱 실행, 화면 전환 등)
    - 유저 속성 지정, 광고 성과 분석 등
      - 실시간 데이터는 Firebase 콘솔 > Analytics 대시보드에서 확인 가능

- 실시간 영상 처리 방법
  - RTSP 스트리밍
    - rtsp://xxx 형태로 영상을 스트리밍
    - 앱에서 이 RTSP 영상을 받아서 재생
    - 구현 방법
      - 플러그인 사용: flutter_vls_player (가장 대중적)
        - 내부적으로 VLC 라이브러리 사용
        - RTSP, HTTP, HLS 등 대부분의 스트리밍 포맷 지원
      - 주의 사항
        - 안드로이드에서는 비교적 잘 동작
        - iOS는 앱스토어 심사에서 VLC 기반 코덱 이슈로 거절될 수 있음 > 필요 시 WebRTC 방식 고려 필요
    - 장점
      - 실시간 영상에 가장 가까움, 딜레이 낮음
      - 표준 스트리밍 방식
      - 네트워크 환경에 따라 적응적 처리 가능
    - 단점
      - 일부 플러터 플랫폼(iOS)의 제약
      - RTSP가 방화벽 또는 모바일망에서 차단되는 경우 존재
      - 애플은 자체 코덱 외에는 민감함 > RTSP + VLC는 위험요소

  - 이미지 프레임을 주기적으로 전송 (MJPEG or Snapshot Polling)
    - 서버에서 정지 이미지를 일정 주기로 앱에 전송
    - 예: 1초에 5장씩 JPEG 이미지 > 애니매이션 처럼 보여주기
    - 구현 방법
      - Image.network()를 주기적으로 변경하여 표시
      - 또는 flutter_mjpeg 플러그인 사용 (이미지 Polling 기반)
      - 서버에서 MJPEG 형식으로 계속 스트림 전송 가능
    - 장점
      - 구현 단순
      - 보안 이슈, 앱 심사 이슈 거의 없음
      - 스트리밍 서버가 없다면 임시 대안으로 적합
    - 단점
      - 실시간성 낮음 (딜레이 큼)
      - 고해상도 이미지 전송 시 네트워크 부하 발생
      - 움직임 많은 영상에는 부적합
  
  - WebRTC 기반 스트리밍 (플러터 웹 + 모바일 모두 호환)
    - 영상 지연 최소화 목적일 때 가장 실시간성 좋은 방식
    - 구현 방법
      - 서버: WebRTC SFU(예: mediasoup, Janus, Kurento 등)
      - flutter_webrtc 플러그인 사용
    - 장점
      - 초저지연(100 ~ 300ms)
      - 브라우저/앱/IoT 등 다양한 환경과 호환
    - 단점
      - 초기 구축 복잡
      - 서버, 인증, 연결 관리가 어려움
      - 사내 네트워크/로컬 IP 환경에선 구성 난이도 높음

  - 실제 진행 시 실무적인 팁
    - 서버 측에서 어떤 포맷 지원하는 정보 입수 필요
      - (RTSP, MJPEG, 이미지 API, WebRTC 등)
    - 네트워크 환경 (내부망, 외부망), 프레인 수요(초당 몇장), 보안 요구사항 등도 같이 고려 필요
    - flutter_webrtc는 WebSocket + signaling 서버가 필요하므로 백엔드와 협업 필요
    - MJPEG 방식은 UI가 투박하긴 하나 심사, 배포, 유지보수 측면에서 가장 안전함
    - 고성능 요구가 없다면 MJPEG 방식 출시, 추후 WebRTC 업그레이드 방향의 단계적 전략 고려 필요

- Flutter에서 데이터 암호화를 위해 SecureStorage를 활용하는 방법은?
  - 개요
    - Flutter에서 암호화된 안전한 저장소를 제공하는 공식 추천 패키지로, Android Keystore / iOS Keychain을 이용하여 민감 정보를 저장

  - 기본 예제
    ```dart
    import 'package:flutter_secure_storage/flutter_secure_storage.dart';

    // 초기화
    final storage = FlutterSecureStorage();

    // 저장
    await storage.write(key: 'token', value: 'abc123');

    // 읽기
    String? token = await storage.read(key: 'token');

    // 삭제
    await storage.delete(key: 'token');

    // 전체 삭제
    await storage.deleteAll();
    ```

  - 정리
    - 내부적으로 안드로이드 키스토어, iOS 키체인 사용
    - 민감 정보 저장시 사용, 저장 속도는 기본 shared_preferences 보다는 느림
    - 저장용량 제한적 (키체인, 키스토어 용량 제약)

- Flutter에서 FFI(Foreign Function Interface)를 사용하는 이유
  - 정의
    - FFI는 Dart 코드에서 C, C++ 등의 네이티브 라이브러리를 직접 호출할 수 있게 해주는 기능.
    - Flutter 앱이 고성능 네이티브 코드와 직접 통신할 수 있도록 함 (플랫폼 채널 없이).

  - 사용하는 이유
    - 성능이 중요한 연산을 C/C++로 처리하고 싶을 때
    - 기존의 네이티브 라이브러리(C/C++)를 Flutter에 재사용할 때
    - 실시간, 고속 처리 (예: 이미지/영상 처리, 암호화, 수치 계산 등)

  - 사용 예
    ```dart
    // Dart: 함수 선언
    import 'dart:ffi';  // FFI import
    import 'dart:io';

    final DynamicLibrary nativeLib = Platform.isAndroid
        ? DynamicLibrary.open("libnative.so")
        : DynamicLibrary.process();

    typedef native_add_func = Int32 Function(Int32 a, Int32 b);
    typedef DartAddFunc = int Function(int a, int b);

    final add = nativeLib
        .lookup<NativeFunction<native_add_func>>("add")
        .asFunction<DartAddFunc>();

    void main() {
      print("Sum = ${add(3, 5)}");
    }
    ```
    - FFI는 플랫폼 채널보다 더 빠르고 경량화된 인터페이스를 제공

- Flutter에서 Riverpod의 Family Modifier를 사용하는 이유
  - 정의
    - family는 파라미터를 받아 동적으로 Provider를 생성할 수 있게 해주는 Riverpod의 기능.

  - 사용하는 이유
    - 사용자 ID, 게시글 ID 등 동적 데이터에 따라 Provider를 구성하고 싶을 때
    - 같은 구조지만 파라미터가 다른 여러 데이터를 독립적으로 관리할 때

  - 사용 예
    ```dart
    final userProvider = Provider.family<User, String>((ref, userId) {
      return fetchUser(userId); // userId에 따라 다른 User 반환
    });
    ```
    ```dart
    // 사용 시
    final user = ref.watch(userProvider("user_123"));
    ```

  - 특징
    - 캐싱 자동 지원
    - 고유 파라미터로 상태가 분리됨 → 불필요한 리렌더링 방지
      - 동일 구조의 상태를 매개변수로 구분된 여러 인스턴스로 관리하고 싶을 때 가장 강력한 기능

- Flutter에서 Drag and Drop을 구현하는 방법
  - 기본 개념
    - Flutter는 Draggable, DragTarget, LongPressDraggable 위젯을 통해 드래그 앤 드롭 인터랙션을 구성할 수 있음.

  - 주요 위젯
    - Draggable<T>
      - 드래그할 수 있는 컴포넌트 정의
    - DragTarget<T>
      - 드롭 가능한 영역 정의
  
  - 사용 예
    ```dart
    // 드래그 가능한 박스
    Draggable<String>(
      data: "Hello",
      feedback: Material(child: Text("Dragging")),
      child: Text("Drag me"),
      childWhenDragging: Text("..."),
    )

    // 드롭 대상
    DragTarget<String>(
      onAccept: (value) {
        print("Dropped: $value");
      },
      builder: (context, candidateData, rejectedData) {
        return Container(
          height: 100,
          width: 100,
          color: candidateData.isEmpty ? Colors.grey : Colors.green,
          child: Center(child: Text("Drop here")),
        );
      },
    )
    ```

  - 활용 예시
    - 카드 정렬
    - 아이템 이동
    - 위젯 배치 UI 구성
      - 기본 기능 외에도 커스텀 드래그 애니메이션, 다중 대상 지원 등 확장이 가능

- Flutter에서 StatelessWidget과 StatefulWidget의 차이점
  - 차이점
    - StatelessWidget
      - 상태 관리: 불가능 (불변)
      - 리렌더링: 외부 입력이 바뀔 때만 다시 빌드
      - 사용 용도: UI가 변하지 않는 정적 컴포넌트

    - StatefulWidget
      - 상태 관리: 가능 (변경 가능)
      - 리렌더링: setState() 호출 시 다시 빌드
      - 사용 용도: UI가 사용자 동작 등으로 바뀌는 동적 컴포넌트

  - 예시
    ```dart
    // StatelessWidget 예
    class MyText extends StatelessWidget {
      final String title;
      const MyText(this.title);

      @override
      Widget build(BuildContext context) {
        return Text(title);
      }
    }

    // StatefulWidget 예
    class MyCounter extends StatefulWidget {
      @override
      State<MyCounter> createState() => _MyCounterState();
    }

    class _MyCounterState extends State<MyCounter> {
      int count = 0;

      @override
      Widget build(BuildContext context) {
        return Column(
          children: [
            Text('$count'),
            ElevatedButton(onPressed: () => setState(() => count++), child: Text("Add"))
          ],
        );
      }
    }
    ```

- Flutter에서 setState()의 역할
  - StatefulWidget에서 UI를 다시 그리도록 요청하는 메소드
  - 내부 상태값을 변경하고 해당 상태에 의존하는 부분만 build()를 다시 실행
  - setState()를 호출해야 변경사항이 화면에 반영됨
  - setState()는 단순하지만 앱 규모가 커지면 전역 상태 관리가 어려워짐

- Flutter에서 상태 관리를 위해 Provider를 사용하는 이유
  - setState()의 한계
    - 여러 위젯에서 공유되는 데이터는 상위 위젯에 있어야 함 → Prop Drilling 발생
    - 위젯 계층이 깊어질수록 코드 복잡도 증가
    - 앱 전역에서 쉽게 접근/공유하기 어려움

  - Provider의 장점
    - 전역 상태 공유 및 의존성 주입 가능
    - context.watch, context.read를 통해 리액티브 UI 갱신
    - 구조 분리: 데이터 관리와 UI 로직을 분리할 수 있음

  - 사용 예
    ```dart
    final counterProvider = ChangeNotifierProvider((_) => Counter());

    class Counter with ChangeNotifier {
      int value = 0;
      void increment() {
        value++;
        notifyListeners();
      }
    }

    // UI
    final counter = context.watch<Counter>();
    Text('${counter.value}');
    ```
    - Provider는 단순하고 가볍게 전역 상태를 관리할 수 있어 Flutter 기본 권장 패턴

- Flutter에서 Riverpod과 Provider의 차이점
  - Riverpod
    - Flutter 의존성: 있음 (BuildContext 필요)
    - 선언 방식: 위젯 기반
    - 상태 추적: context.watch / read
    - 안전성: 런타임 오류 가능
    - 기능성: 기본 기능 위주
    - 테스트: 어렵거나 보일러플레이트 많음

  - Provider
    - Flutter 의존성: 없음 (완전한 Dart 기반, 테스트 용이)
    - 선언 방식: 함수 기반 (전역 선언 가능)
    - 상태 추적: ref.watch / ref.read
    - 안전성: Compile 타임 안전 (타입 안정성 증가)
    - 기능성: family, autoDispose, async 지원 등 고급 기능 다수
    - 테스트: 테스트 용이 (context 불필요)

  - Riverpod은 Provider의 단점을 개선한 차세대 상태관리 솔루션으로 안정성/성능/유연성 모두 향상됨

- Flutter에서 Bloc 패턴을 사용할 때 얻을 수 있는 장점
  - 개요
    - BLoC (Business Logic Component) 패턴

  - UI와 비즈니스 로직의 분리
    - (1) UI와 비즈니스 로직의 분리
      - UI(View)와 로직(Bloc)이 명확하게 나뉘어 있어서 코드 구조가 깔끔하고 유지보수하기 쉬움
      - 디자인/기획 팀과 협업할 때 UI를 독립적으로 다루기 좋음

    - (2) 테스트 용이성 향상
      - Bloc은 단순히 이벤트를 받고 상태를 반환하는 구조이므로 단위 테스트(Unit Test)가 매우 쉬움
      - expect(bloc.state, emitsInOrder([...])) 등으로 명확한 상태 검증 가능

    - (3) 예측 가능한 상태 흐름 (Unidirectional Flow)
      - 모든 상태 변화는 Event → Logic → State 순으로 처리되며, 데이터 흐름이 한 방향으로만 이동함
      - 디버깅, 로깅, 상태 추적이 쉬움

    - (4) 명확한 상태 기반 UI 리렌더링
      - BlocBuilder, BlocListener를 통해 상태 변화에 반응하여 UI를 갱신
      - 상태 단위로 UI를 관리하므로 복잡한 UI에서도 불필요한 리렌더링 방지

    - (5) 대규모 프로젝트에 적합
      - 기능 모듈 단위로 Bloc을 분리할 수 있어서 팀 개발, 유지보수에 유리
      - 공통 패턴을 따르므로 프로젝트 규모가 커져도 일관성 유지 가능

    - (6) Flutter 공식 팀 지원
      - flutter_bloc은 공식 지원 라이브러리이며, 안정적이고 꾸준히 유지보수되고 있음

    - (7) 다양한 유틸 기능 제공
      - BlocProvider, BlocBuilder, BlocListener, MultiBlocProvider 등을 통해 DI, 상태 구독, UI 연결 등 유틸리티 기능 제공

  - 예시 흐름 요약
    ```scss
    [ UI ] 
      ↓ Bloc.add(Event)
    [ Bloc ]
      ↓ emit(New State)
    [ UI ]
      → BlocBuilder(State => UI 렌더링)
    ```

  - 정리
    - BLoC은 복잡한 앱의 상태를 체계적으로 관리하고, 테스트 가능하고 유지보수 쉬운 아키텍처를 제공하는 Flutter의 대표 패턴

- Flutter에서 InheritedWidget의 역할
  - 역할 및 개념
    - InheritedWidget은 Flutter에서 하위 위젯 트리에 데이터를 효율적으로 전달하기 위한 기본 메커니즘
    - 보통 위젯 트리 상단에서 공유하고 싶은 데이터를 정의한 뒤, 트리 하위의 여러 위젯들이 그 데이터를 필요할 때 접근할 수 있도록 해준다.
    - 컴포즈에서 XXXProvider와 유사

  - 특징
    - 트리 구조의 위에서 아래로만 데이터 전달 가능
    - of(context) 메서드를 통해 접근
    - 하위 위젯이 InheritedWidget이 제공하는 데이터에 의존하고 있고, 그 데이터가 변경되면 하위 위젯은 자동으로 재빌드됨
    - 상태 관리의 핵심 기반이 되며, Provider, Bloc, Riverpod 같은 고급 상태 관리 패키지도 내부적으로 이를 활용함

  - 예시 활용
    - 사용자 정보, 테마 설정, 로케일 정보 등을 여러 화면에 전달할 때 사용될 수 있다.

- Flutter에서 GetX 상태 관리 패턴을 사용하는 이유
  - 간결성과 생산성
    - GetX는 Flutter의 복잡한 상태 관리 로직을 간결하게 해주며, setState, InheritedWidget, Provider의 복잡성을 줄여준다. 
    - Controller라는 명확한 책임을 가진 객체에 상태를 집중시켜 관리하며, 뷰에서는 거의 로직이 없이 UI만 담당할 수 있게 한다.

  - 리액티브 프로그래밍 지원
    - GetX는 리액티브 상태 관리를 지원하기 때문에 .obs로 선언된 값이 변경되면 자동으로 UI가 갱신된다. 
    - Obx 위젯을 사용하여 데이터가 바뀔 때만 해당 UI만 리빌드되도록 최적화할 수 있다.

  - 의존성 주입과 라우팅까지 포함한 통합 솔루션
    - GetX는 상태 관리뿐만 아니라 의존성 주입, 라우팅, 로컬 스토리지, 번역 등 여러 기능을 제공하여 전체 앱 구조를 통일된 방식으로 관리할 수 있게 해준다.

  - 학습 곡선이 낮음
    - 단순한 문법과 적은 코드량으로도 강력한 기능을 제공하기 때문에 작은 프로젝트나 빠르게 프로토타입을 개발할 때 유리하다.

- Flutter에서 ChangeNotifier를 활용한 상태 관리는 구현 방법
  - 기본적인 구조
    - ChangeNotifier는 Flutter의 기본 상태 관리 클래스 중 하나
    - 관찰자 패턴을 구현하고 있음
    - 이 클래스를 상속받은 모델 클래스에서 notifyListeners()를 호출하면 이를 구독한 위젯들이 자동으로 리빌드된다.

  - 구현 방식
    - (1) 상태를 가지는 모델 클래스를 ChangeNotifier로 정의
    - (2) ChangeNotifierProvider를 사용하여 트리 상단에 모델을 주입
    - (3) Consumer 또는 Provider.of(context)를 통해 하위 위젯에서 상태에 접근
    - (4) 상태 변경 시 notifyListeners()를 호출하여 UI를 갱신

  - 장점과 단점
    - 구조가 명확하고 Flutter에 내장되어 있어 추가 의존성이 없다.
    - 그러나 상태가 많아지고 복잡해질수록 관리가 어려워질 수 있으며, 세분화된 리빌드 제어가 어렵다.

- Flutter에서 Flutter Hooks의 역할과 활용 방법
  - 개념과 목적
    - Flutter Hooks는 함수형 위젯에서 상태 관리 및 라이프사이클 로직을 더욱 간결하게 작성할 수 있도록 도와주는 라이브러리 
    - React의 Hooks와 유사한 개념을 도입하여 StatefulWidget의 반복적인 보일러플레이트를 줄이는 것을 목표로 한다.

  - 주요 기능
    - useState, useEffect, useMemoized, useTextEditingController 등 다양한 훅을 제공
    - 상태값, 컨트롤러, 애니메이션 등 여러 기능을 선언형 방식으로 간단하게 다룰 수 있다
    - 클래스 기반 StatefulWidget 없이도 상태 유지가 가능해 코드 가독성이 향상된다

  - 사용 방식
    - flutter_hooks 패키지를 설치한 뒤, HookWidget을 상속받아 훅을 사용할 수 있다
    ```dart
    final count = useState(0);
    ```

  - 장점
    - 코드량 감소, 가독성 향상
    - 불필요한 상태관리 클래스 제거
    - 유지보수성이 좋아짐

  - 주의사항
    - Hook 사용 시 위젯이 HookWidget 또는 HookConsumerWidget을 상속받아야 하며, BuildContext를 훅 외부에서 사용하면 오류가 발생할 수 있다.

- Flutter에서 ValueNotifier 사용 시점
  - 핵심 개념
    - ValueNotifier<T>는 특정 값이 변경될 때 이를 감지하여 리스너에게 알리는 가볍고 효율적인 상태 관리 도구
    - Flutter의 내장 클래스이며, 단일 값의 상태를 관리할 때 가장 적합하다.

  - 사용 시점
    - 상태가 단순한 단일 변수일 때 (bool, int, double, String, 리스트 등)
    - 별도의 Provider나 Bloc을 도입할 정도로 구조가 크지 않을 때
    - StatefulWidget 없이도 UI 갱신이 필요할 때

  - 장점
    - 코드가 간결하고 경량
    - 리스너를 직접 등록하거나 ValueListenableBuilder로 UI와 연동 가능
    - Flutter의 내부 위젯들에서도 활용됨 (예: TextEditingController 내부)

  - 예시
    - 카운터, 로딩 상태 표시, 선택된 인덱스 변경 등 매우 단순한 상태에 적합하다.

- Flutter에서 Redux와 MobX의 차이점
  - Redux의 특징
    - 불변성(immutability) 기반의 상태 관리 아키텍처
    - 앱의 상태를 Store에 중앙 집중화
    - 모든 상태 변경은 반드시 Action → Reducer → Store의 흐름을 따라야 하며, 예측 가능하고 디버깅이 쉬움
    - 상태 변경 로직이 명확하고 추적 가능하지만, 보일러플레이트 코드가 많음

  - MobX의 특징
    - 반응형(Reactive) 상태 관리 방식
    - 관찰 가능한 상태(@observable)와 반응형 표현식(@computed, @action)을 중심으로 상태 변경을 추적
    - 상태가 바뀌면 자동으로 UI가 갱신되며, 개발자는 선언형 코드에 집중
    - 설정은 간단하지만 내부 동작이 복잡하여 추적이 어려울 수 있음

  - 비교 요약
    - Redux는 함수형 사고 기반의 구조적 관리에 적합하고, MobX는 간결하고 직관적인 상태 반응성을 추구
    - Redux는 복잡한 앱에서 디버깅과 시간여행에 유리하며, MobX는 생산성과 빠른 개발에 강점이 있다.

- Flutter에서 setState()를 과도하게 사용하면 발생할 수 있는 문제
  - 과도한 setState()의 문제점
    - 불필요한 전체 위젯 리빌드가 발생
    - 특정 값만 바뀌었더라도 위젯 전체가 다시 그려지기 때문에 성능 저하로 이어질 수 있음
    - 상태 분리가 안된 경우 로직이 커질수록 유지보수 어려움
    - 여러 상태가 얽혀 있는 경우, UI와 로직이 뒤섞여 가독성과 테스트성이 떨어짐

  - 예시 상황
    - 하나의 StatefulWidget에서 수십 개의 위젯을 포함하고 있고, 특정 값 하나가 바뀌었을 뿐인데도 전체가 재렌더링되는 경우
    - 서로 다른 상태가 동일 위젯 내에 존재해 변경 시 예상치 못한 렌더링이 발생하는 경우

  - 해결 방안
    - 상태를 분리하여 InheritedWidget, Provider, ValueNotifier, Bloc 등을 사용
    - setState()는 작은 범위의 단순한 상태를 관리할 때만 사용하는 것이 이상적임

- Flutter에서 Freezed 패키지를 사용하는 이유
  - 핵심 개념
    - Freezed는 불변 데이터 클래스, 패턴 매칭, copyWith, JSON serialization, 동등성 비교 등을 자동으로 생성해주는 코드 생성 라이브러리

  - 사용 목적
    - Flutter 앱에서 모델 객체를 안전하게 불변(immutable)하게 관리
    - 수동으로 작성해야 할 코드(생성자, 복사, 비교 등)를 줄이고 생산성 향상
    - sealed class 형태로 모델을 구성하고, when 또는 map과 같은 패턴 매칭을 지원하여 복잡한 상태 표현을 구조화할 수 있음

  - 주요 기능
    - const 생성자 자동 생성
    - == 및 hashCode 오버라이드
    - copyWith() 메서드 자동 생성
    - union/sealed class 구현 지원 (LoginState.loading(), LoginState.success(), ... 처럼)

  - 활용 예시
    - Bloc/Cubit의 상태 클래스 정의
    - REST API의 응답 모델
    - 앱 내 상태 표현을 Enum보다 더 유연하게 표현하고자 할 때

- Flutter에서 Hydrated Bloc을 활용하여 상태를 유지하는 방법
  - 핵심 개념
    - Hydrated Bloc은 Bloc 또는 Cubit의 상태를 디스크에 자동 저장하고 앱 재시작 후 복원해주는 기능을 제공하는 라이브러리

  - 사용 방법
    - HydratedBloc 또는 HydratedCubit 클래스를 상속받아 상태를 관리
    - toJson/fromJson 메서드를 오버라이딩하여 상태를 JSON으로 직렬화/역직렬화
    - 앱 시작 시 HydratedBloc.storage를 초기화해야 하며, 일반적으로 main() 함수에서 HydratedStorage.build()를 사용하여 구현

  - 장점
    - 별도의 코드 없이도 상태가 자동으로 저장되고 복원되어 앱의 UX 개선에 유리
    - 로그인 상태, 테마 설정, 캐시 데이터 등에 적합

- Flutter에서 상태 관리 라이브러리 없이 상태를 관리하는 방법
  - 핵심 개념
    - Flutter는 기본적으로 StatefulWidget을 통해 상태 관리를 제공 
    - 외부 라이브러리를 사용하지 않고도 UI와 상태를 함께 다룰 수 있음

  - 방법
    - StatefulWidget과 setState()를 통해 간단한 상태 변경을 반영할 수 있음
    - 앱의 구조가 작거나 상태 공유 범위가 작을 경우 InheritedWidget 또는 InheritedModel을 사용하여 위젯 트리 상에서 데이터를 하위 위젯으로 전달할 수 있습니다.

  - 한계점
    - 앱이 커지면 상태가 여러 위치에 흩어지고, 코드 관리가 어려워짐.
    - 복잡한 의존성이나 비동기 처리가 어려워지므로 일정 규모 이상에서는 적절한 상태 관리 도구가 필요

- Flutter에서 FutureBuilder와 StreamBuilder의 차이점
  - FutureBuilder
    - 한 번만 결과를 반환하는 Future 객체를 기반으로 동작
    - 일반적으로 단발성 데이터 요청 (예: API 호출, 파일 읽기)에 사용
    - 상태는 ConnectionState.none, waiting, active, done 중 하나로 관리되며, 완료 시 UI를 갱신

  - StreamBuilder
    - 지속적으로 변화하는 데이터를 제공하는 Stream 객체를 기반으로 동작합니다.
    - 예: 실시간 채팅, 센서 데이터, WebSocket 등과 같은 스트림 데이터에 적합합니다.
    - 데이터가 올 때마다 UI가 자동으로 리빌드됩니다.

  - 비교
    - FutureBuilder는 1회성 작업, StreamBuilder는 지속적인 구독에 적합합니다.
    - FutureBuilder는 완료 후 값 변경이 없고, StreamBuilder는 새로운 이벤트마다 상태를 갱신합니다.

- Flutter에서 Cubit과 Bloc의 차이점
  - Cubit
    - Bloc보다 더 간단하고 경량화된 상태 관리 방식.
    - 상태 변화를 직접 메서드 호출을 통해 emit()하는 방식으로 구현됩니다.
    - 복잡한 이벤트-상태 매핑 없이 간단한 로직에 적합합니다.

  - Bloc
    - Event와 State를 명확히 분리하여, 이벤트 중심의 상태 전이를 구현합니다.
    - 이벤트 처리 로직은 mapEventToState() 또는 on<Event>()에서 정의되며, 복잡한 상태 흐름을 다룰 때 적합합니다.

  - 비교 요약
    - Cubit은 빠르고 간단한 상황에 적합한 방식.
    - Bloc은 이벤트 흐름이 명확한 복잡한 앱에 더 적합.
    - 둘 다 flutter_bloc 패키지에 포함되어 있으며, 필요에 따라 선택하면 됩니다.

- Flutter에서 State Restoration을 구현하는 방법
  - 개념 요약
    - State Restoration은 사용자가 앱을 종료하거나 백그라운드로 전환했다가 다시 돌아왔을 때, 이전 상태를 복원하여 사용자 경험을 유지하는 기능입니다.

  - 구현 방법
    - Flutter는 RestorationMixin을 사용해 상태 복원 기능을 제공합니다.
    - StatefulWidget의 State 클래스에서 RestorationMixin을 믹스인으로 추가하고, restoreState() 메서드를 오버라이딩합니다.
    - RestorationId를 통해 위젯 계층 간 상태 구분이 가능하며, RestorableInt, RestorableTextEditingController 등의 Restorable 객체를 사용해 자동 복원을 구현할 수 있습니다.

  - 예시 흐름
    - 위젯에서 RestorationMixin 적용
    - restorationId 설정
    - registerForRestoration()으로 상태 복원 대상 등록
    - 앱 재시작 시 자동으로 복원

  - 주의사항
    - Android에서만 자동 복원이 기본적으로 작동하며, iOS는 수동 구성 필요
    - 단순 상태 저장 이상으로, 사용자 상호작용 흐름까지 복원하고자 할 때 효과적

- Flutter에서 StateNotifier를 활용한 상태 관리
  - 개념 요약
    - StateNotifier는 Riverpod에서 제공하는 상태 관리 방식 중 하나로, 명시적이고 예측 가능한 상태 변경을 위해 사용됩니다.
    - ChangeNotifier보다 테스트하기 쉽고 명확한 상태 전이 구현이 가능합니다.

  - 사용 방법
    - 상태를 표현할 모델 클래스 작성
    - 이를 관리하는 StateNotifier<T>를 상속받는 클래스 구현
    - NotifierProvider 또는 StateNotifierProvider로 UI와 연결

  - 특징
    - 상태 변경은 state = newValue 형태로 단방향으로만 이루어집니다.
    - 상태 변경 시 전체 상태를 다시 할당해야 하며, 변경 감지를 위해 immutable한 데이터 구조 사용 권장
    - Provider의 컴포저블한 특성과 함께 사용되면 강력한 상태 분리 구조 구현 가능

  - 장점
    - 명확한 상태 전이 방식
    - 구조화된 앱 설계에 유리
    - 테스트 용이성

- Flutter에서 GetIt과 Injectable을 활용한 의존성 주입 방법
  - GetIt 개요
    - GetIt은 Flutter용 DI(Dependency Injection) 컨테이너로, 싱글톤 객체를 등록하고 어디서든 접근할 수 있게 도와줍니다.
    - UI 레이어에서 비즈니스 로직이나 서비스에 쉽게 접근할 수 있습니다.

  - Injectable 개요
    - Injectable은 GetIt과 함께 사용되며, DI 등록 코드를 자동 생성해줍니다.
    - @injectable, @singleton, @module 등의 애노테이션을 사용하여 필요한 객체를 선언하면, build_runner로 DI 설정을 자동화할 수 있습니다.

  - 사용 절차
    - get_it, injectable, build_runner 패키지 설치
    - DI 대상 클래스에 @injectable 또는 @singleton 애노테이션 부여
    - configureInjection(environment) 함수로 의존성 설정
    - getIt<YourService>()로 인스턴스를 주입 받아 사용

  - 장점
    - 테스트와 유지보수에 유리한 구조 설계 가능
    - 코드 중복 없이 DI 자동화 가능

- Flutter에서 useEffect와 유사한 기능을 구현 방법
  - React의 useEffect 역할
    - 컴포넌트가 마운트되거나 특정 값이 변경될 때 사이드 이펙트를 실행하는 훅

  - Flutter에서의 대응 방식
    - initState() → 컴포넌트 최초 생성 시 한 번 실행되는 훅
    - didUpdateWidget() → 부모 위젯의 변경으로 현재 위젯이 갱신될 때 호출
    - didChangeDependencies() → InheritedWidget 등 의존성 변경 시 호출됨
    - addPostFrameCallback() → 프레임이 렌더링된 이후에 특정 로직 실행 (즉, 빌드 완료 이후)

  - 예제 흐름
    ```dart
    @override
    void initState() {
      super.initState();
      WidgetsBinding.instance.addPostFrameCallback((_) {
        // 이곳이 useEffect와 유사하게 동작
        fetchDataOrDoSideEffect();
      });
    }
    ```

  - 요약
    - useEffect(() => {}, [])는 initState + addPostFrameCallback 조합과 유사
    - 값이 변경될 때마다 사이드 이펙트를 실행하려면 ValueNotifier나 StateNotifier 등을 활용한 관찰 구조 사용

- Flutter에서 Singleton 패턴을 활용하여 상태를 관리하는 방법
  - 개요
    - 싱글톤 패턴은 앱 전체에서 하나의 인스턴스를 공유하는 방식
    - 플러터에서 주로 Service, Manager, Controller 클래스 등에 사용됨
    - 상태를 글로벌하게 유지 가능

  - 예시
    ```dart
    class UserManager {
  static final UserManager _instance = UserManager._internal();
      String? userName;

      factory UserManager() {
        return _instance;
      }

      UserManager._internal();
    }

    // 사용 예
    UserManager().userName = "Aiden";
    print(UserManager().userName); // "Aiden"
    ```

  - 장점:
    - 전역 접근성
    - 메모리 절약 (인스턴스 1개만 유지)

  - 단점:
    - 테스트가 어려움
    - 복잡한 앱에서 의존성 주입 없이 남용 시 유지보수 어려움

- Flutter에서 App Lifecycle을 관리하는 방법
  - 앱 라이프사이클 관리 방법
    - WidgetsBindingObserver 활용하여 앱 라이프사이클 상태 감지 가능

  - 예시
    ```dart
    class MyAppState extends State<MyApp> with WidgetsBindingObserver {
      @override
      void initState() {
        super.initState();
        WidgetsBinding.instance.addObserver(this);
      }

      @override
      void dispose() {
        WidgetsBinding.instance.removeObserver(this);
        super.dispose();
      }

      @override
      void didChangeAppLifecycleState(AppLifecycleState state) {
        switch (state) {
          case AppLifecycleState.resumed:
            print('앱 다시 활성화');
            break;
          case AppLifecycleState.paused:
            print('앱 백그라운드로');
            break;
          default:
            break;
        }
      }
    }
    ```

  - 주요 상태:
    - resumed: 앱이 포그라운드 상태로 복귀
    - inactive: 앱이 비활성 (전화 수신 등)
    - paused: 앱이 백그라운드로 이동
    - detached: 앱이 분리됨 (플랫폼 View에서 분리됨)

- Flutter에서 상태 관리 선택 기준
  - 소규모, 간단한 상태: setState, InheritedWidget
  - 중간 규모, 구조화된 상태 분리: Provider, Riverpod, Bloc, GetX
  - 대규모 앱, 테스트/DI 필요: Riverpod, Bloc (Clean Architecture)
  - 단순한 비동기 처리: FutureBuilder, StreamBuilder
  - 복잡한 애니매이션 연동: ValueNotifier, ChangeNotifier

- Flutter에서 AnimatedBuilder를 활용한 상태 관리의 장점
  - 개요
    - AnimatedBuilder는 애니매이션을 효율적으로 재렌더링 할 수 있게 해주는 위젯 리렌더링 최적화 도구
    - 전체 위젯 리빌드가 아닌, 애니매이션 대상만 다시 빌드

  - 예시
    ```dart
    class Spinner extends StatefulWidget {
      @override
      _SpinnerState createState() => _SpinnerState();
    }

    class _SpinnerState extends State<Spinner> with SingleTickerProviderStateMixin {
      late AnimationController _controller;

      @override
      void initState() {
        _controller = AnimationController(
          duration: const Duration(seconds: 2),
          vsync: this,
        )..repeat();
        super.initState();
      }

      @override
      Widget build(BuildContext context) {
        return AnimatedBuilder(
          animation: _controller,
          builder: (_, child) {
            return Transform.rotate(
              angle: _controller.value * 2 * 3.1415,
              child: child,
            );
          },
          child: Icon(Icons.refresh),
        );
      }
    }
    ```

  - 장점:
    - 위젯 리빌드 최적화: animation 대상만 rebuild
    - 구조 분리: animation 외부 위젯과의 decoupling 가능
    - setState보다 성능 우수

- Flutter에서 OverlayEntry를 활용한 UI 상태 관리 방법
  - 개요
    - OverlayEntry는 현재의 위젯 트리와는 별개로, 화면 위에 UI 요소를 동적으로 띄울 수 있는 기능
    - 예: 커스텀 툴팁, 드롭다운, 로딩 인디케이터 등.

  - 사용 절차:
    - OverlayState를 가져온다: Overlay.of(context)
    - OverlayEntry를 생성한다.
    - overlay.insert(entry)로 삽입한다.
    - UI 상태 변화에 따라 entry.markNeedsBuild()로 갱신하거나, entry.remove()로 제거

  - 예시
    ```dart
    late OverlayEntry _entry;

    void _showOverlay(BuildContext context) {
      final overlay = Overlay.of(context);
      _entry = OverlayEntry(
        builder: (context) => Positioned(
          top: 100,
          left: 100,
          child: Material(
            child: Text('Hello Overlay'),
          ),
        ),
      );
      overlay.insert(_entry);
    }

    void _hideOverlay() {
      _entry.remove();
    }
    ```
    - 상태를 StatefulWidget, StateNotifier, Riverpod, Provider, Bloc 등으로 관리하고
    - setState 혹은 notifyListeners()로 상태 변경 시 OverlayEntry를 갱신할 수 있음.

- Flutter에서 StatefulWidget이 필요한 경우
  - 필요 케이스
    - StatefulWidget은 내부에 상태(state)가 변경되며 UI가 다시 빌드되어야 하는 경우에 사용

  - 예시 상황:
    - 텍스트 필드의 입력값을 추적할 때
    - 버튼 클릭 여부
    - 애니메이션 컨트롤
    - 타이머/카운트다운 등 반복적으로 값이 변할 때
    - ScrollController, TabController 등 컨트롤러 유지가 필요할 때

  - 예외 상황
    - 반대로, 상태가 없거나 고정된 UI만을 그릴 때는 StatelessWidget을 사용

- Flutter에서 ChangeNotifier와 StateNotifier의 차이점
  - 차이점
    - ChangeNotifier
      - 플러터 기본 제공
      - 내부 필드를 직접 mutate
      - 클래스 내부에서 notifyListeners() 호출
      - 상대적으로 테스트 용이성은 떨어짐
      - 복잡한 구조
    - StateNotifier
      - Riverpod 라이브러리
      - 단일 state를 불변 객체로 관리
      - state = newValue 방식
      - ChangeNotifier보다 명확하며 testable
      - 명확한 단방향 흐름 설계 가능

  - 예시:
    - ChangeNotifier
      ```dart
      class Counter with ChangeNotifier {
        int count = 0;

        void increment() {
          count++;
          notifyListeners();
        }
      }
      ```

    - StateNotifier
      ```dart
      class CounterNotifier extends StateNotifier<int> {
        CounterNotifier() : super(0);

        void increment() => state++;
      }
      ```
      - 복잡한 상태나 불변 상태 관리를 하려면 StateNotifier가 적합 (단방향, 관리 용이성)

- Flutter에서 FutureProvider와 StreamProvider의 차이점
  - 차이점
    - FutureProvider
      - 한 번만 비동기 처리 (예: API 요청)
      - 반환값 Future<T>
      - 자동 갱신 안됨 (명시적 다시 호출 필요)
    - StreamProvider
      - 여러 값의 비동기 흐름 (예: 실시간 데이터)
      - Stream<T>
      - 자동 갱신 가능 (스트림에 새 이벤트가 Emit되면 갱신)
  - 예시
    - FutureProvider
      ```dart
      final userProvider = FutureProvider((ref) async {
        return await fetchUser();
      });
      ```
    - StreamProvider
      ```dart
      final messagesProvider = StreamProvider((ref) {
        return FirebaseFirestore.instance.collection('chats').snapshots();
      });
      ```

- Flutter에서 MultiProvider를 활용하는 이유
  - 사용 이유
    - MultiProvider는 여러 개의 Provider를 계층적으로 선언할 때 코드 가독성을 높이기 위해 사용

  - 일반적 방식 (비효율적)
    ```dart
    return ProviderA(
      create: (_) => A(),
      child: ProviderB(
        create: (_) => B(),
        child: ProviderC(
          create: (_) => C(),
          child: MyApp(),
        ),
      ),
    );
    ```

  - MultiProvider 방식 (추천)
    ```dart
    return MultiProvider(
      providers: [
        Provider<A>(create: (_) => A()),
        Provider<B>(create: (_) => B()),
        Provider<C>(create: (_) => C()),
      ],
      child: MyApp(),
    );
    ```
    - 특히 앱 전체에서 사용하는 여러 의존성 객체를 깔끔하게 주입할 때 유리

- Flutter에서 CustomPainter를 활용한 그래픽 구현 방법
  - 개요
    - CustomPainter는 Flutter에서 캔버스 위에 직접 그림을 그리는 저수준 API
    - 이걸 활용하면 기본 위젯으로는 어려운 커스텀 그래픽, 애니메이션, 차트, 경로 등 복잡한 UI를 그릴 수 있음

  - 기본 구조
    ```dart
    class MyPainter extends CustomPainter {
      @override
      void paint(Canvas canvas, Size size) {
        final paint = Paint()
          ..color = Colors.blue
          ..strokeWidth = 4
          ..style = PaintingStyle.stroke;

        canvas.drawRect(
          Rect.fromLTWH(0, 0, size.width, size.height),
          paint,
        );
      }

      @override
      bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
    }
    ```
    ```dart
    CustomPaint(
      size: Size(200, 200),
      painter: MyPainter(),
    )
    ```

  - 주요 메서드 및 속성 설명
    - paint(Canvas, Size): 그림을 그리는 핵심 메서드
    - shouldRepaint: 상태가 바뀔 때 다시 그려야 하는지 결정
    - Paint(): 색상, 두께, 스타일 지정
    - canvas.drawXXX: 도형, 텍스트, 이미지 그리기 (drawRect, drawCircle, drawLine, drawPath 등)

  - 간단한 예: 원 그리기
    ```dart
    class CirclePainter extends CustomPainter {
      @override
      void paint(Canvas canvas, Size size) {
        final paint = Paint()
          ..color = Colors.orange
          ..style = PaintingStyle.fill;

        final center = Offset(size.width / 2, size.height / 2);
        final radius = size.width / 3;

        canvas.drawCircle(center, radius, paint);
      }

      @override
      bool shouldRepaint(CustomPainter oldDelegate) => false;
    }
    ```

  - 애니메이션과 함께 사용 (예: CustomPainter + AnimationController)
    ```dart
    class AnimatedCirclePainter extends CustomPainter {
      final double progress;
      AnimatedCirclePainter(this.progress);

      @override
      void paint(Canvas canvas, Size size) {
        final paint = Paint()
          ..color = Colors.blue
          ..style = PaintingStyle.stroke
          ..strokeWidth = 4;

        final rect = Rect.fromLTWH(0, 0, size.width, size.height);
        canvas.drawArc(rect, -pi / 2, 2 * pi * progress, false, paint);
      }

      @override
      bool shouldRepaint(covariant AnimatedCirclePainter old) =>
          old.progress != progress;
    }
    ```
    ```dart
    CustomPaint(
      painter: AnimatedCirclePainter(animation.value),
    )
    ```

  - 주의할 점
    - CustomPainter는 성능이 좋은 대신 직접 그려야 하므로 좌표계, 레이아웃 계산, 반응 처리(UI 입력) 등을 수동으로 관리해야 함
    - 복잡한 UI일수록 shouldRepaint 조건을 정확하게 지정해야 리렌더링 성능 유지됨

  - 활용 예시
    - 게이지/차트/그래프
    - 다각형/도형 UI
    - 비동기 애니메이션 효과
    - 경로 기반의 그래픽 인터랙션
    - 이미지와 텍스트의 캔버스 합성

- Flutter에서 SliverWidgets를 사용하는 이유
  - 개요
    - Sliver(조각) 위젯은 플러터의 스크롤 가능한 영역을 더 정교하게 제어할 수 있게 해주는 구성 요소
  - 사용 이유
    - 고성능 스크롤 리스트 구성: Sliver는 스크롤 시 필요한 부분만 렌더링해 메모리 사용을 줄임.
    - 다양한 레이아웃 통합: SliverAppBar, SliverList, SliverGrid 등을 조합하여 동적 UI (예: 스크롤에 따라 앱바 축소/고정) 를 만들 수 있음.
    - CustomScrollView에 통합 가능: 여러 종류의 스크롤 위젯을 하나의 스크롤 뷰로 통합 가능.
  - 예시
    ```dart
    CustomScrollView(
      slivers: [
        SliverAppBar(...),
        SliverList(delegate: ...),
        SliverGrid(delegate: ...),
      ],
    )
    ```

- Flutter에서 RepaintBoundary를 활용하여 성능을 최적화하는 방법
  - 개요
    - RepaintBoundary는 화면의 일부분이 다시 그려질 때 해당 영역만 리렌더링하도록 분리하는 위젯
  - 활용 이유 및 효과
    - 불필요한 전체 리렌더링 방지: 자식 위젯이 자주 변경될 때, 부모까지 리렌더링 되지 않도록 막아줌
    - 애니메이션 등 일부 위젯만 업데이트 될 때 유용
    - 플러터 DevTools의 Repaint Rainbow 기능으로 repaint영역 디버깅 가능
  - 사용 예
    ```dart
    RepaintBoundary(
      child: SomeWidgetThatChangesFrequently(),
    )
    ```

- Flutter에서 const 생성자를 활용하면 성능이 향상되는 이유
  - 개요
    - const 생성자를 사용하면 컴파일 타임에 객체를 미리 생성하여 재사용할 수 있습니다.

  - 이점:
    - 불변 객체를 캐싱함으로써 메모리 절약 및 생성 비용 감소.
    - 위젯 트리 비교 시 동일 객체로 간주되어 rebuild를 방지.
    - Hot reload 시 불필요한 리렌더링 최소화.

  - 추가 설명: const 사용 시 매번 새 객체 생성하지 않음

- Flutter에서 Image.memory()와 Image.asset()의 차이점
  - Image.memory()
    - 메모리의 바이트 배열(Uint8List)로 로드
    - base64, 다운로드된 이미지, 실시간 이미지 때 사용
    - 기본적으로 캐시 없음, 매번 그려야 함
    - Image.memory(bytes) 로 선언
  - Image.asset()
    - 앱의 asset 폴더에서 이미지 로드
    - 정적 리소스, 앱 내 포함된 이미지 로드 때 사용
    - 플러터 자체 캐시 적용 (성능 우수)
    - Image.asset('assets/image.png')
  - 핵심 차이
    - 정적/동적 이미지
    - 성능 및 캐싱 유무

- Flutter에서 Hero 애니메이션을 구현하는 방법
  - 개요
    - Hero 위젯은 두 화면 간에 공통 요소를 애니메이션으로 자연스럽게 전환해주는 위젯
  - 사용 방법
    - Hero 위젯에 동일한 태그를 부여한 두 위젯을 각각의 화면에 배치
    - Navigator를 통해 화면 전환 시 자동으로 애니메이션이 실행됨
  - 예
    ```dart
    // 첫 번째 화면
    Hero(
      tag: 'profile',
      child: Image.asset('assets/profile.png'),
    );

    // 두 번째 화면
    Hero(
      tag: 'profile',
      child: Image.asset('assets/profile.png'),
    );

    // 화면 전환 예시
    Navigator.push(context, MaterialPageRoute(builder: (_) => SecondPage()));
    ```

- Flutter에서 ShaderMask를 활용하는 방법
  - 개요
    - ShaderMask는 자식 위젯에 그래디언트나 쉐이더 효과를 적용할 때 사용됩니다.

  - 주요 활용 예:
    - 텍스트나 이미지에 그라디언트 색상 효과 적용
    - 마스킹/블렌딩 효과

  - 예:
    ```dart
    ShaderMask(
      shaderCallback: (bounds) => LinearGradient(
        colors: [Colors.purple, Colors.blue],
      ).createShader(bounds),
      child: Text(
        'Gradient Text',
        style: TextStyle(fontSize: 40, color: Colors.white),
      ),
    )
    ```

- Flutter에서 AspectRatio 위젯을 활용하는 이유
  - 개요
    - AspectRatio는 자식 위젯의 가로:세로 비율을 고정하기 위해 사용

  - 활용 이유:
    - 화면 크기에 따라 크기를 자동으로 조정하면서 비율 유지
    - 정사각형/4:3/16:9 등 미디어 콘텐츠 표시 시 유용

  - 예시
    ```dart
    AspectRatio(
      aspectRatio: 16 / 9,
      child: Container(color: Colors.blue),
    )
    ```

- Flutter에서 AnimatedList를 사용할 때의 장점
  - 개요
    - AnimatedList는 아이템 추가/삭제 시 애니매이션을 자동 적용할 수 있는 리스트 위젯
  - 장점
    - 항목 추가/삭제 시 부드러운 애니메이션 제공
    - 리스트 변경사항을 시각적으로 더 자연스럽게 표현
    - 별도 애니메이션 구현 없이도 효율적인 UX 제공
  - 예시
    ```dart
    AnimatedList(
      key: listKey,
      initialItemCount: items.length,
      itemBuilder: (context, index, animation) {
        return SizeTransition(
          sizeFactor: animation,
          child: ListTile(title: Text(items[index])),
        );
      },
    )
    ```
- Flutter에서 ListView와 GridView의 차이점
  - 차이점
    - ListView
      - 1차원 수직/수평 스크롤 목록
      - 일반 텍스트, 이미지 목록 등 단순 리스트
      - 기본은 수직 (scrollDirection 변경 가능)
      - ListView.builder 제공
    - GridView
      - 2차원 격자형 목록
      - 갤러리, 카드형 UI 등 그리드 형식 UI
      - 기본은 수직, 설정으로 수평도 가능
      - GridView.builder 제공
  - 예시
    ```dart
    ListView.builder(
      itemCount: 10,
      itemBuilder: (context, index) => ListTile(title: Text('Item $index')),
    );

    GridView.count(
      crossAxisCount: 2,
      children: List.generate(4, (index) => Text('Grid $index')),
    );
    ```

- Flutter에서 Lottie를 활용한 애니메이션 적용 방법
  - 개요
    - JSON 기반 벡터 애니매이션, After Effects 애니메이션을 플러터에 적용 가능하게 해줌
  - 사용법
    ```dart
    Lottie.asset('assets/xxx.json'); // OR Lottie.network(url)
    ```

- Flutter에서 NestedScrollView를 사용할 때 고려해야 할 점
  - 개요
    - NestedScrollView는 AppBar와 Body가 함께 스크롤되도록 구성할 수 있는 위젯입니다.

  - 고려사항:
    - headerSliverBuilder로 SliverAppBar 등을 정의
    - 내부 Body에는 반드시 ScrollController가 일치하도록 해야 함
    - 내부에 ListView 대신 CustomScrollView 또는 ScrollView + shrinkWrap 설정 필요

- Flutter에서 Cupertino 디자인 시스템을 적용하는 방법
  - 개요
    - Cupertino는 iOS 스타일의 UI 컴포넌트를 제공
  - 사용법
    ```dart
    import 'package:flutter/cupertino.dart';

    CupertinoApp(
      home: CupertinoPageScaffold(
        navigationBar: CupertinoNavigationBar(
          middle: Text('Title'),
        ),
        child: Center(child: CupertinoButton(child: Text("iOS"), onPressed: () {})),
      ),
    )
    ```
  - 전체 앱을 Cupertino 스타일로 구성하거나, Theme.of(context).platform 으로 iOS/Android 스타일을 조건 분기할 수도 있음

- Flutter에서 AppBar의 PreferredSizeWidget을 활용하는 이유
  - 개요
    - AppBar는 기본적으로 PreferredSizeWidget을 구현하고 있어야 함
    - 커스텀 앱 바를 만들 때도 이 인터페이스를 구현해야 정확한 높이 지정이 가능
  - 예시
    ```dart
    class MyCustomAppBar extends StatelessWidget implements PreferredSizeWidget {
      @override
      Size get preferredSize => const Size.fromHeight(60);

      @override
      Widget build(BuildContext context) {
        return AppBar(title: Text('Custom'));
      }
    }
    ```

- Flutter에서 LayoutBuilder를 활용하여 반응형 UI를 구축하는 방법
  - 개요
    - LayoutBuilder는 부모 위젯의 크기를 기준으로 조건 분기 UI를 구성할 때 유용
  - 예시
    ```dart
    LayoutBuilder(
      builder: (context, constraints) {
        if (constraints.maxWidth > 600) {
          return LargeScreenWidget();
        } else {
          return SmallScreenWidget();
        }
      },
    )
    ```

- Flutter에서 AutoSizeText를 활용하여 가변 폰트 크기를 적용하는 방법
  - 개요
    - AutoSizeText는 텍스트가 공간을 초과할 경우 자동으로 폰트 크기를 줄여서 overflow를 방지합니다.

  - 사용법:
    ```yaml
    auto_size_text: ^3.0.0
    ```
    ```dart
    AutoSizeText(
      '................',
      maxLines: 2,
      style: TextStyle(fontSize: 40),
    )
    ```

- Flutter에서 ClipRRect와 ClipPath의 차이점
  - ClipRRect
    - 둥근 사각형으로 자르기
    - 미리 정의된 borderRadius로 간단
    - 성능 빠름
  - ClipPath
    - 커스텀 경로(Path)로 자르기
    - 복잡한 도형/형태 클리핑 가능
    - Path 계산 필요로 약간 느릴 수 있음
  - 예시
    ```dart
    ClipRRect(
      borderRadius: BorderRadius.circular(16),
      child: Image.asset('img.jpg'),
    )

    ClipPath(
      clipper: MyCustomClipper(),
      child: Image.asset('img.jpg'),
    )
    ```

- Flutter에서 ImageFilter를 활용한 블러 효과 구현 방법
  - 개요
    - ImageFilter.blur는 위젯에 블러(흐림) 효과를 줄 수 있음
    - BackdropFilter와 함께 사용
  - 예시
    ```dart
    BackdropFilter(
      filter: ImageFilter.blur(sigmaX: 5, sigmaY: 5),
      child: Container(
        color: Colors.black.withOpacity(0.1),
      ),
    )
    ```

- Flutter에서 RenderObject를 직접 구현하는 이유
  - 개요
    - 기본 위젯으로 표현할 수 없는 복잡한 레이아웃이나 성능 최적화가 필요한 경우, Flutter의 렌더링 파이프라인 하단의 RenderObject를 직접 구현

  - 주요 목적:
    - 매우 커스텀된 UI
    - 성능 극대화
    - 저수준 위치 계산, 제스처 처리 등

  - 하지만 대부분의 경우는 RenderBox나 CustomPaint, CustomMultiChildLayout 등으로 충분함

- Flutter에서 GestureDetector와 InkWell의 차이점
  - GestureDetector
    - 클릭 효과 없음 (리플 없음)
    - 더 다양한 제스쳐 처리 가능 (드래그 등)
    - 어느 부분에서나 사용 가능
  - InkWell
    - Ripple 효과 (머터리얼 스타일) 제공
    - 기본 tap, long press 등 제한적
    - Material 위젯 트리 내에서만 ripple 효과
  - 예시
    ```dart
    GestureDetector(
      onTap: () => print('Tapped'),
      child: Container(color: Colors.red),
    )

    InkWell(
      onTap: () => print('Tapped'),
      child: Container(color: Colors.red),
    )
    ```

- Flutter에서 Drawer 위젯을 활용한 내비게이션 방법
  - 좌측 또는 우측에서 슬라이드로 나타나는 내비게이션 메뉴
  - 사용법
    ```dart
    Scaffold(
      appBar: AppBar(title: Text('Drawer Example')),
      drawer: Drawer(
        child: ListView(
          children: [
            DrawerHeader(child: Text('Header')),
            ListTile(
              title: Text('Home'),
              onTap: () => Navigator.pushNamed(context, '/home'),
            ),
          ],
        ),
      ),
    );
    ```
    - Scaffold의 drawer: 속성에 삽입.
    - Scaffold.of(context).openDrawer()로 프로그래밍 방식으로 열 수도 있음.

- Flutter에서 FloatingActionButton을 커스터마이징하는 방법
  - 개요
    - FAB은 주로 화면 우하단에 표시되는 주요 액션 버튼
  - 커스터 마이징 예시
    ```dart
    FloatingActionButton(
      onPressed: () {},
      backgroundColor: Colors.purple,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: Icon(Icons.add, size: 32),
    )
    ```
    - shape, backgroundColor, elevation, child 등을 이용해 완전히 커스터마이징 가능

- Flutter에서 PageView 위젯을 활용하는 방법
  - 개요
    - PageView는 가로(또는 세로)로 스와이프 가능한 페이지 구조 제공
  - 예시
    ```dart
    PageView(
      controller: PageController(),
      children: [
        Container(color: Colors.red),
        Container(color: Colors.green),
        Container(color: Colors.blue),
      ],
    )
    ```
    - PageController를 이용해 animateToPage() 등 제어 가능.
    - onPageChanged로 현재 페이지 인덱스 확인 가능.

- Flutter에서 커스텀 Shimmer 효과를 구현하는 방법
  - Shimmer: 로딩 중인 상태를 시각적으로 보여주는 효과
  - 구현 방법
    ```dart
    Shimmer.fromColors(
      baseColor: Colors.grey[300]!,
      highlightColor: Colors.white,
      child: Container(width: 200, height: 20, color: Colors.grey),
    )
    ```
    - 커스텀 구현도 가능: ShaderMask + AnimatedBuilder 조합.

- Flutter에서 TabBar와 BottomNavigationBar의 차이점
  - TabBar
    - 주로 상단에 위치
    - TabBarView와 함께 사용
    - 뷰 내부의 탭 구분
  - BottomNavigationBar
    - 화면 하단에 위치
    - 직접 상태 관리 (setState)등 필요
    - 주요 화면 간의 내비게이션
  - 예시(TabBar)
    ```dart
    DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(bottom: TabBar(tabs: [Tab(text: 'A'), Tab(text: 'B')])),
        body: TabBarView(children: [Text('A'), Text('B')]),
      ),
    );
    ```

- Flutter에서 기본적인 Theming을 적용하는 방법
  - ThemeData를 사용하여 전체 앱의 색상, 글꼴, 버튼 스타일 등을 설정
  - 예시
    ```dart
    MaterialApp(
      theme: ThemeData(
        primarySwatch: Colors.indigo,
        textTheme: TextTheme(bodyMedium: TextStyle(fontSize: 16)),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(backgroundColor: Colors.indigo),
        ),
      ),
    )
    ```
    - Theme.of(context)로 위젯에서 접근 가능.

- Flutter에서 SafeArea 위젯의 역할
  - 개요
    - SafeArea는 노치, 상태바, 홈 인디케이터 등 시스템 UI로부터 안전한 영역을 보장
  - 예시
    ```dart
    SafeArea(
      child: Column(
        children: [Text('안전하게 보이는 텍스트')],
      ),
    )
    ```
    - top, bottom 속성으로 부분 지정도 가능.

- Flutter에서 BackdropFilter를 활용하여 UI를 디자인하는 방법
  - BackdropFilter는 해당 위젯 뒤에 있는 콘텐츠에 블러(흐림)효과 적용
  - 예시
    ```dart
    Stack(
      children: [
        Image.asset('bg.jpg'),
        BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
          child: Container(color: Colors.black.withOpacity(0.2)),
        ),
      ],
    )
    ```
    - 투명한 Container가 꼭 있어야 효과 적용됨.

- Flutter에서 MaterialStateProperty를 활용하는 방법
  - 버튼 등의 위젯에서 상태(hovered, pressed, disabled 등)에 따른 스타일을 지정할 때 사용
  - 예시
    ```dart
    ElevatedButton(
      style: ButtonStyle(
        backgroundColor: MaterialStateProperty.resolveWith((states) {
          if (states.contains(MaterialState.pressed)) return Colors.red;
          return Colors.blue;
        }),
      ),
      onPressed: () {},
      child: Text('버튼'),
    )
    ```

- Flutter에서 Wrap과 Row, Column의 차이점
  - Row/Column
    - 한 줄(열)로만 배치
    - 컨텐츠가 넘칠 때 오류 (overflow)
    - 고정 개수 아이템일 때 사용
  - Wrap
    - 넘치면 자동 줄바꿈 가능
    - 컨텐츠가 넘칠 때 자동으로 줄바꿈 또는 래핑
    - 동적으로 아이템이 많거나 줄바꿈 필요 시
  - Wrap 예시
    ```dart
    Wrap(
      spacing: 8,
      runSpacing: 4,
      children: List.generate(10, (i) => Chip(label: Text('Item $i'))),
    )
    ```

- Flutter에서 Dio와 http 패키지의 차이점
  - http 패키지
    - 단순 REST API 호출
    - 간단한 요청/응답 지원
    - try-catch 수동 구현 필요 (에러 핸들링)
    - FormData 지원 제한적 (multipart)
    - Timeout, Cancel 등 수동 설정 필요
  - dio 패키지
    - 고급 기능 포함
    - 요청/응답 인터셉터, 글로벌 설정 가능
    - DioError로 정리된 예외 제공
    - 강력한 FormData 및 파일 업로드 지원
    - Timeout, Cancel 등 내장 지원
  - 정리
    - http: 간단한 API 호출용
    - dio: 인터셉터, 토큰 갱신, 에러 처리 등 복잡한 네트워크 로직이 필요한 경우 추천

- Flutter에서 GraphQL을 활용하여 데이터를 불러오는 방법
  - 설치 패키지: graphql_flutter
  - 기본 예시
    ```dart
    final HttpLink httpLink = HttpLink('https://api.example.com/graphql');

    ValueNotifier<GraphQLClient> client = ValueNotifier(
      GraphQLClient(
        link: httpLink,
        cache: GraphQLCache(),
      ),
    );

    GraphQLProvider(
      client: client,
      child: Query(
        options: QueryOptions(document: gql('''
          query GetUser { user { id name } }
        ''')),
        builder: (result, {fetchMore, refetch}) {
          if (result.isLoading) return CircularProgressIndicator();
          return Text(result.data!['user']['name']);
        },
      ),
    )
    ```
    - Mutation 위젯도 사용 가능.
    - GraphQLClient 직접 생성해서 client.query(...) 방식으로도 사용 가능.

- Flutter에서 REST API 호출 시 예외 처리를 구현하는 방법
  - 예시 (http 사용)
    ```dart
    try {
      final response = await http.get(Uri.parse('https://api.example.com'));
      if (response.statusCode == 200) {
        // 정상 처리
      } else {
        throw Exception('서버 오류: ${response.statusCode}');
      }
    } catch (e) {
      print('네트워크 오류 발생: $e');
    }
    ```

  - 예시 (dio 사용)
    ```dart
    try {
      final response = await dio.get('/users');
    } on DioException catch (e) {
      if (e.type == DioExceptionType.connectionTimeout) {
        // 연결 시간 초과 처리
      } else if (e.response?.statusCode == 401) {
        // 인증 오류 처리
      }
    }
    ```
    - DioError는 다양한 type으로 구분 가능 (timeout, cancel, response 등)

- Flutter에서 Firebase Authentication을 연동하는 방법
  - 패키지 설치: firebase_core, firebase_auth
  - 초기화 (main.dart)
    ```dart
    void main() async {
      WidgetsFlutterBinding.ensureInitialized();
      await Firebase.initializeApp();
      runApp(MyApp());
    }
    ```
  - 로그인 예시
    ```dart
    final credential = await FirebaseAuth.instance.signInWithEmailAndPassword(
      email: 'test@example.com',
      password: 'password123',
    );
    ```
  - 인증 상태 감지
    ```dart
    FirebaseAuth.instance.authStateChanges().listen((User? user) {
      if (user != null) print('로그인됨: ${user.email}');
    });
    ```
    - Google, Apple, Anonymous, Phone 등 다양한 인증 방식 제공

- Flutter에서 JWT 토큰을 활용한 인증 구현 방법
  - 로그인 요청 시 JWT 발급
    ```dart
    final response = await dio.post('/login', data: {
      'email': email,
      'password': password,
    });
    final token = response.data['access_token'];
    ```
  - 저장
    - await prefs.setString('jwt_token', token);
  - 인증 요청 시 헤더에 포함
    ```dart
    final token = await prefs.getString('jwt_token');
    dio.options.headers['Authorization'] = 'Bearer $token';
    ```
  - 자동 토큰 갱신 (RefreshToken) 전략
    - Dio의 Interceptor를 사용하여 401 에러 시 토큰 재발급 요청 후 재시도 구현 가능

- Flutter에서 WebSockets을 활용한 실시간 통신 방법
  - 설치 패키지: web_socket_channel
  - 사용 예시
    ```dart
    import 'package:web_socket_channel/web_socket_channel.dart';

    final channel = WebSocketChannel.connect(
      Uri.parse('wss://example.com/socket'),
    );

    // 메시지 수신
    channel.stream.listen((message) {
      print('Received: $message');
    });

    // 메시지 전송
    channel.sink.add('Hello server!');

    // 연결 종료
    channel.sink.close();
    ```
    - 실시간 채팅, 알림, 센서 데이터 전송 등에서 활용됨
    - stream.listen 기반이므로 StreamBuilder와 연계도 쉬움

- Flutter에서 OAuth 2.0 인증을 구현하는 방법
  - 패키지: oauth2, flutter_appauth
  - OAuth 흐름 요약 (Authorization Code Flow)
    - 사용자 인증 페이지로 리다렉션
    - Authorization code 발급
    - Backend 서버에서 액세스 토큰, 리프레쉬 토큰 교환
    - 액세스 토큰 사용하여 API 호출
  - AppAuth 사용 예
    ```dart
    final AuthorizationTokenResponse? result =
    await appAuth.authorizeAndExchangeCode(
      AuthorizationTokenRequest(
        clientId,
        redirectUrl,
        serviceConfiguration: AuthorizationServiceConfiguration(
          authorizationEndpoint: authUrl,
          tokenEndpoint: tokenUrl,
        ),
        scopes: ['openid', 'profile', 'email'],
      ),
    );
    ```
    - Google, Kakao, Naver, GitHub 로그인 등에 활용
    - redirect URI 등록 필수 (iOS/Android 플랫폼별 설정 필요)

- Flutter에서 API 호출을 위한 Rate Limiting을 적용하는 방법
  - 개요
    - Rate Limiting은 특정 시간 내에 API 호출 횟수를 제한하는 기능
    - 클라이언트 측에서는 주로 디바운싱 또는 타이머 기반 제어를 활용함
  - 디바운싱 예
    ```dart
    Timer? _debounce;

    void onSearchChanged(String value) {
      if (_debounce?.isActive ?? false) _debounce!.cancel();
      _debounce = Timer(const Duration(milliseconds: 500), () {
        fetchApi(value);
      });
    }
    ```
  - 고급 패키지 예:
    - rxdart 의 debounceTime
    - custom throttler (throttle(), throttleLatest())

  - 사용 이유
    - 서버와 중복 요청을 줄이고, 쿼리 비용을 절감
    - 실시간 검색, 자동완성 등에 매우 유용

- Flutter에서 SSL Pinning을 적용하는 방법
  - 개요
    - SSL Pinning은 HTTPS 연결 시 서버의 공개 키 또는 인증서를 미리 앱에 저장해 검증하는 보안 기법
  - 패키지: dio, http_certificate_pinning
  - Dio + SSL Pinning 예시
    ```dart
    (dio.httpClientAdapter as DefaultHttpClientAdapter).onHttpClientCreate = (client) {
      SecurityContext context = SecurityContext(withTrustedRoots: false);
      context.setTrustedCertificates('assets/cert.pem');
      return HttpClient(context: context);
    };
    ```
  - 또는 http_certificate_pinning 패키지 활용
    ```dart
    await HttpCertificatePinning.check(
      serverURL: "example.com",
      headerHttp: {},
      sha: SHA.SHA256,
      allowedSHAFingerprints: ["..."],
    );
    ```
  - SSL Pinning
    - 중간자 공격 방지, 인증서 위조 차단
    - 주기적으로 인증서 갱신 필요

- Flutter에서 FlutterFire를 활용한 Firebase 연동 방법
  - 개요
    - FlutterFire는 Flutter용 Firebase 공식 SDK
  - 패키지
    - firebase_core, firebase_auth
    - cloud_firestorew, firebase_messaging
    - firebase_crashlytics
  - 초기화
    ```dart
    void main() async {
      WidgetsFlutterBinding.ensureInitialized();
      await Firebase.initializeApp();
      runApp(MyApp());
    }
    ```
  - 주요 기능 예시
    - FirebaseAuth.instance.signInWithEmailAndPassword(...)
    - FirebaseFirestore.instance.collection('users').doc('id').get()
    - FirebaseMessaging.instance.getToken() (푸시 토큰)
    - FirebaseCrashlytics.instance.recordError(e, stack)

  - Analytics, Storage, Remote Config, Functions 등도 확장 가능
  - 플랫폼별 GoogleService-Info.plist / google-services.json 필요

- Flutter에서 Clean Architecture를 적용한 네트워크 계층 설계 방법
  - 기존 구조 (레이어 기준)
    ```bash
    lib/
      core/         # 공통 유틸, 에러, 타입
      data/         # DTO, API Service (Retrofit), Impl Repository
      domain/       # Entity, UseCase, Abstract Repository
      presentation/ # View, ViewModel
    ```
  - 예시 흐름
    - ApiService > HTTP 호출 (Dio/Retrofit 등)
    - MyRepositoryImpl implements MyRepository (도메인 레이어)
    - GetUserUseCase > MyRepository.getUser()
    - ViewModel에서 UseCase 호출 > UI 갱신
  - 장점
    - 테스트 용이, 관심사 분리, DI 가능
    - 관련 도구: freezed, json_serializable, hooks_riverpod, get_it 등

- Flutter에서 Firebase Firestore와 Realtime Database의 차이점
  - FireStore
    - 문서/컬렉션 기반 (NoSQL)
    - 강력한 필터링/정렬 지원
    - 실시간 지원 (효율적)
    - 구조화된 문서 저장에 적합
    - 사용량 기반, 다소 비싼 가격
  - Realtime Database
    - 트리 기반 (JSON 트리)
    - 단순 쿼리만 지원
    - 실시간 지원 (더 빠르지만 구조적 제한 존재)
    - 빠른 실시간 동기화에 적합
    - 저렴하나 최적화 필수
  - 정리: 일반적으로 FireStore가 더 권장됨 (구조 / 확장성 측면)

- Flutter에서 GraphQL의 Query와 Mutation의 차이점
  - Query
    - 데이터 조회 (Read)
    - 캐싱 가능, 재요청 안전
  - Mutation
    - 데이터 변경 (create/update/delete)
    - 변경이므로 상태 변화 발생 가능
  - graphql_flutter에서 Query/Mutation 위젯 혹은 client.query(), client.mutate() 사용

- Flutter에서 FormData를 활용한 파일 업로드 방법 (dio)
  ```dart
  final formData = FormData.fromMap({
    "file": await MultipartFile.fromFile(filePath, filename: "image.png"),
    "userId": "1234"
  });

  final response = await dio.post('/upload', data: formData);
  ```
  - Content-Type은 자동 설정
  - 여러 파일 업로드도 .fromMap에 리스트로 가능

- Flutter에서 Multi-part Request를 활용한 이미지 업로드 방법 (http)
  ```dart
  final request = http.MultipartRequest("POST", Uri.parse(url));
  request.files.add(await http.MultipartFile.fromPath('file', filePath));
  final response = await request.send();
  ```
  - http 패키지로도 multipart/form-data 업로드 가능
  - 다만 dio가 더 유연하고 고급 기능 제공

- Flutter에서 에러 핸들링을 위한 Global Error Handler를 구현하는 방법
  ```dart
  void main() {
    FlutterError.onError = (FlutterErrorDetails details) {
      FirebaseCrashlytics.instance.recordFlutterError(details);
    };

    runZonedGuarded(() {
      runApp(MyApp());
    }, (error, stack) {
      FirebaseCrashlytics.instance.recordError(error, stack);
    });
  }
  ```
  - Crashlytics 연동 필수
  - 비동기 에러도 전역 처리 가능

- Flutter에서 Web과 Mobile 개발의 차이점
  - Mobile(iOS/Android)
    - Skia 엔진 렌더링 방식
    - SharedPref, SecureStorage
    - 기기 파일 접근 가능
    - 카메라, 위치 등 풍부한 플랫폼 API 접근 가능
    - 스토어 배포
  - Web
    - HTML/CSS or CanvasKit 렌더링
    - localStorage, IndexedDB
    - 브라우저 제한 (업로드/다운로드 중심)
    - Web API 제한 (권한 필요)
    - URL 기반 배포 가능 (Firebase Hosting 등)
    
  - Platform check: kIsWeb, Platform.isAndroid 등을 활용
  - UI, 기능 분기 필요할 수 있음

- Flutter에서 API 응답을 캐싱하는 방법
  - 패키지: dio_cache_interceptor
    ```dart
    DioCacheInterceptor dioCache = DioCacheInterceptor(options: CacheOptions(...));
    dio.interceptors.add(dioCache);
    ```

  - Local DB 활용 (hive, shared_preferences, sqflite 등)
    - API 응답을 JSON으로 저장 후 TTL 기반으로 로컬 캐시 사용

  - 리소스 절약, 오프라인 대응 가능
  - TTL, 조건부 캐시 전략 적용 가능
  - 실질적인 이점
    - 성능향상 (속도개선)
      - 서버 응답 기다리지 않고 로컬 캐시된 데이터를 즉시 표현 가능
      - 느린 네트워크 환경에서 UX가 훨씬 매끄러워짐
      - 예: 뉴스 앱, 쇼핑 앱에서 이전에 조회한 목록이 즉시 보여짐
    - 데이터 사용량 절감
      - 동일한 API 요청을 여러번 서버로 보내지 않으므로 불필요한 트래픽 감소, 모바일 데이터 요금 절감에도 도움
    - 서버 부하 감소
      - 캐시된 응답을 재사용하면 서버 호출 횟수가 줄어들어 백엔드 리소스 절약
      - 인기있는 API 엔드포인트에 대해 효과적
    - 오프라인 지원
      - 지하철에서도 마지막으로 본 정보를 계속 확인 가능, 네트워크 불량인 상태일 때도 UI 유지 가능
    - 더 나은 사용자 경험 (UX)
      - 앱 실행 시 빠른 데이터 로딩, 스크롤 할 때 로딩 지연 없음
      - 더 빠르고 부드러운 앱처럼 느껴짐
    - 지능적인 업데이트 전략 가능
      - 일정 시간(1분, 5분 등) 동안은 캐시, 이후에는 갱신
      - 예: 스와이프 리프레시 시 서버 데이터 우선, 평상 시에는 캐시 데이터 우선
    - 적용 예시
      - dio_cache_interceptor, flutter_cache_manager 같은 라이브러리 사용
      - 또는 직접 shared_preferences, hive, sqflite 등 이용한 캐시 전략 구성

    - 캐시 사용 시 주의점
      - 데이터 일관성: 오래된 데이터가 남아있을 수 있음 > TTL, Manual Refresh 필요
      - 보안 문제: 민감 데이터는 캐시 금지
      - 캐시 사이즈 관리: 용량 무한정 증가 방지 필요 (오래된 캐시 삭제)


- Flutter에서 Desktop 앱을 개발할 때 고려해야 할 점
  - 주요 고려 사항
    - UI 스케일링
      - 마우스, 키보드 기반 UX에 맞게 Hover, Right-Click, Tooltip 등 처리 필요
    - 폰트 & DPI
      - 고해상도 DPI 대응 필요 (MediaQuery.deivcePixelRatio)
    - 창 크기 조절
      - 화면 Resize 및 Min/Max Size 대응 (WindowManger 패키지)
    - 파일 시스템 접근
      - file_picker, path_provider 등 데스크탑 전용 구현 고려
    - 마우스/키보드 이벤트
      - Focus, KeyboardListener, MouseRegion 등 명확한 이벤트 분리 필요
    - 플랫폼 제한
      - 일부 라이브러리는 Desktop 미지원 (예: permission_handler 등)
  - 플러그인 예시
    - window_manager (창 제어)
    - bitsdojo_window (창 프레임 커스터마이징)

- Flutter에서 Tizen 및 Embedded 기기용 앱을 개발할 때 필요한 사항
  - 플랫폼 지원
    - 타이젠용 플러터는 삼성 주도로 개발된 fork (공식 플러터 SDK와 별도 관리)
  - SDK 설치
    - flutter-tizen CLI 사용
  - 디바이스 연결
    - sdb 명령어로 Tizen 기기 연결 후 flutter-tizen run
  - UI 성능 최적화
    - 리소스가 제한된 환경에서는 렌더링 최적화, 애니메이션 제한 필요
  - 입력 처리
    - 리모컨, 키패드 기반 입력 대응 필요 (RawKeyboardListener, FocusNode)
  - 패키지 호환성
    - 일부 패키지는 Embedded 환경에서 미지원
  - Embedded 환경에서는 직접 Platform Channel 구현이 필요할 가능성이 큼

- Flutter에서 PWA(Progressive Web App)를 구현하는 방법
  - 지원 플랫폼: Flutter Web
  - 설정
    - flutter build web 실행 시 기본적으로 PWA 템플릿 포함
    - web/manifest.json, web/index.html, web/icons/ 등 자동 생성
  - 서비스 워커: flutter_service_worker.js 자동 포함
  - 호스팅: Firebase Hosting, Vercel, GitHub Pages 등 가능
  - 주의점: iOS 사파리는 PWA 일부 기능 제한 존재 (백그라운드 동작 등)

- Flutter에서 Native Code(Android/iOS)를 호출하는 방법
  - 방법
    - Platform Channels 사용 (플러터 <> 네이티브 간 메시지 전달)
  - 플러터 측
    ```dart
    const platform = MethodChannel('com.example/native');
    final result = await platform.invokeMethod('nativeFunction');
    ```
  - Android (Kotlin/Java): MethodChannel 등록 후 setMethodCallHandler로 처리
  - iOS (Swift): FlutterMethodChannel 사용해 동일하게 구현
  - 예시 활용: 센서, GPS, BLE, 영상 처리, SDK 호출 등

- Flutter에서 isolate를 활용한 병렬 처리 방법
  - 이유
    - 플러터 메인 스레드는 단일 스레드이므로 CPU 작업을 isolate로 분리 필요
  - 기본 사용
    ```dart
    final result = await compute(heavyFunction, inputData);
    ```
  - 직접 제어
    ```dart
    final ReceivePort receivePort = ReceivePort();
    await Isolate.spawn(isolatedFunction, receivePort.sendPort);
    ```
  - 주의 사항
    - isolate 간 메모리 공유 불가 > 메시지 기반 통신 사용

- Flutter에서 FFI(Foreign Function Interface)를 활용하는 이유
  - 목적: C/C++ 라이브러리 등을 Flutter에서 직접 호출
  - 활용 예: 고성능 연산, 이미지/오디오 처리, OpenCV, FFmpeg, Metal 등
  - 구현 방식:
    - dart:ffi 사용
    - .so(Android), .dylib(macOS/iOS), .dll(Windows) 등 바인딩
    - ffi 및 ffi_helper 패키지 사용 시 편리
  - 주의: 메모리 관리와 플랫폼 별 바이너리 분리 필요

- Flutter에서 ML Kit을 활용한 이미지 인식 기능을 구현하는 방법
  - 방법: Firebase ML Kit + google_ml_kit 패키지 활용
  - 기능: 텍스트 인식, 얼굴 인식, 바코드 스캔, 라벨링 등
  - 기본 흐름:
    - InputImage.fromFile 또는 InputImage.fromBytes 생성
    - MLKit Processor(ex. TextRecognizer, FaceDetector)로 분석
    - 결과 객체(RecognizedText, Face) 반환
  - 주의사항: 카메라 연동은 camera 패키지와 병행

- Flutter에서 WebRTC를 활용한 영상 통화 기능을 구현하는 방법
  - 패키지: flutter_webrtc
  - 기본 구성:
    - MediaStream (카메라/마이크)
    - RTCVideoRenderer (화면 표시)
    - RTCPeerConnection (신호 교환, ICE 후보 등)
    - signaling 서버 필요 (WebSocket or Firebase 등)

  - 예시 흐름:
    - 로컬 미디어 초기화
    - offer/answer 교환
    - ICE candidate 처리
    - 스트림 연결 및 표시

- Flutter에서 Background Task를 수행하는 방법
  - 안드로이드/아이폰에 따라 처리 방식 다름
  - 옵션별 방법:
    - workmanager → 일정 간격 작업 (iOS/Android 지원)
    - android_alarm_manager_plus → Android 백그라운드 알람
    - flutter_background_service → 백그라운드 상태 유지 + 주기적 로직
    - Isolate + Timer → 앱 열려 있을 때 백그라운드 루프 실행
  - iOS 주의: 백그라운드 제한 강함 → 백그라운드 fetch 또는 알림 기반으로 처리 필요

- Flutter에서 Firebase Analytics를 활용하는 방법
  - 설정:
    - Firebase 연동 (firebase_core, firebase_analytics)
    - GoogleService-Info.plist / google-services.json 포함
  - 사용법:
    ```dart
    FirebaseAnalytics.instance.logEvent(
      name: 'purchase',
      parameters: {'item': 'beer', 'value': 1},
    );
    ```
  - 자동 수집 항목: 앱 열기, 첫 실행, 인앱 결제 등
  - 커스텀 이벤트: 앱 사용 패턴 분석용으로 logEvent 정의

- Flutter에서 Background Fetch를 활용하는 방법
  - 패키지: background_fetch
  - 지원 플랫폼: Android, iOS
  - 기능: 주기적으로 백그라운드에서 작업 수행
    - 서버 폴링, 상태 동기화 등
  - 구현
    ```dart
    BackgroundFetch.configure(
      BackgroundFetchConfig(
        minimumFetchInterval: 15,
        stopOnTerminate: false,
        enableHeadless: true,
      ),
      onBackgroundFetch,
    );
    ```
  - 주의:
    - Android: AndroidManifest.xml에 퍼미션 추가
    - iOS: UIBackgroundModes에 fetch 등록 필요

- Flutter에서 OpenAI API를 활용한 챗봇 기능을 구현하는 방법
  - HTTP 방식: dio 또는 http 사용
  - API 호출 예 (gpt-3.5-turbo 기준)
    ```dart
    final response = await dio.post(
      'https://api.openai.com/v1/chat/completions',
      data: {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "안녕"}],
      },
      options: Options(headers: {
        "Authorization": "Bearer YOUR_API_KEY",
      }),
    );
    ```
  - UX 개선: 타이핑 애니매이션, 대기중 인디케이터, 챗버블 UI 적용 등

- Flutter에서 Dynamic Link를 활용한 딥링크 구현 방법
  - Firebase Dynamic Links를 통해 딥링크를 생성
  
  - 앱 실행 시 FirebaseDynamicLinks.instance.onLink.listen 또는 getInitialLink()를 사용해 딥링크 데이터를 처리
  
  - 앱이 종료되어 있든 백그라운드에 있든 모두 대응 가능하도록 초기 처리와 리스닝을 분리해 구성

- Flutter에서 FlutterFlow와 같은 Low-Code 개발 도구를 활용하는 방법
  - Flutter 기반의 UI를 시각적으로 구성할 수 있는 Low-Code 툴로, Firebase 연동, API 연결, 상태 관리까지 GUI 환경에서 구현 가능

  - 구성한 앱은 Flutter 코드로 export가 가능하여, 복잡한 비즈니스 로직은 VSCode 또는 Android Studio에서 이어서 커스터마이징 가능

  - 단점은 복잡한 커스터마이징이 어렵고, 성능 튜닝/상태 관리 제한이 있으므로 MVP, 프로토타입, 관리 앱 등에 적합

- Flutter에서 Flare 애니메이션을 적용하는 방법
  - Flare(Rive)는 .riv 파일로 벡터 기반 애니메이션을 제작하여 앱에 경량으로 삽입할 수 있는 툴

  - rive 패키지를 사용해 RiveAnimation.asset('assets/example.riv')로 로드하고, 상태 제어가 필요한 경우 StateMachineController를 통해 트리거나 파라미터로 조작

  - FPS에 영향이 적고, Flutter UI와 자연스럽게 결합되므로 로딩 애니메이션, 전환 효과 등에 적합

- Flutter에서 Riverpod의 AutoDispose 기능을 활용하는 방법
  - 위젯이 dispose 될 때 provider도 자동으로 메모리 해제되도록 도와주는 기능
  - 예제
    ```dart
    final userProvider = FutureProvider.autoDispose((ref) async => fetchUser());
    ```
  - 정리
    - 메모리 누수, 오래된 상태 유지 문제 예방 가능
    - ref.keepAlive() 활용 시 조건부 유지도 가능
    - PageView, TabView, Navigator 전환 시 자주 사용됨

- Flutter에서 플랫폼별 코드(Android, iOS)를 다르게 적용하는 방법
  - Platform.isAndroid, isIOS 통해 조건 분기 가능
  - MethodChannel을 통해 안드로이드 또는 iOS 코드와 직접 통신 가능
  - 예: if (Platform.isAndroid) showAndroidToast(); else showiOSToast();

- Flutter에서 Dart의 null-safety 기능을 활용하는 방법
  - 컴파일 타임에 널 오류를 방지
  - ?(nullable), !(non-null) 등의 키워드 활용
  - late 키워드는 선언 후 반드시 초기화 보장되는 값에 사용

- Flutter에서 CI/CD 파이프라인을 구축하는 방법
  - GitHub Actions, Bitrise, Codemagic 등을 사용하여 빌드, 테스트, 배포 자동화 구현
  - 예시
    - GitHub Actions 에서 flutter pub get, flutter test, flutter build apk, firebase deploy 단계로 구성 가능
  - Firebase App Distribution, TestFlight, Play Store 등과 연동하여 지속적 배포 구현 가능

- Flutter에서 FFI(Foreign Function Interface)를 활용하여 네이티브 모듈과 상호작용하는 방법
  - Dart FFI
    - C/C++로 작성된 native 라이브러리와 직접 바인딩할 수 있게 해주는 기능
    - .so, .dylib 등을 직접 불러와 DynamicLibrary.open() 으로 연동하며, 주로 성능이 중요한 연산 처리에 사용
  - 예시
    - 이미지 처리, 머신러닝, 디코딩 로직 등을 native로 작성하고 Dart에서 호출

- Flutter의 Platform Channels과 FFI의 차이점 및 활용 방법
  - Platform Channels
    - Dart <> Android/iOS 고급 API 호출 시점에 사용 
    - 예: 카메라, GPS
  - FFI
    - Dart <> Native C 라이브러리 직접 호출
    - 예: 빠른 수치 계산, 압축 해제 등
  - Platform Channels는 플랫폼 종속적이며, FFI는 공통 C 계열 라이브러리에 적합

- Flutter 3.22에서 추가된 주요 기능과 최적화 기법
  - Impeller 렌더러의 안드로이드 지원 (정식 출시)
  - WebAssembly(Wasm) 빌드 미리보기 제공
  - DevTool 성능 개선 및 핫 리로드 속도 향상
  - flutter build 시 압축률 개선, Flutter Web 에서 CanvasKit 성능 향상 등이 포함

- Flutter에서 CustomRenderObjects를 활용하여 UI 성능을 최적화하는 방법
  - RenderObject를 직접 상속하여 맞춤형 레이아웃 또는 페인팅 구현 시 성능 극대화 가능
  - 예
    - 복잡한 리스트뷰 또는 커스텀 페인터보다 더 정교한 픽셀 제어가 필요할 때 사용
    - 높은 난이도와 메모리 관리 주의 필요

- Flutter에서 Skia 및 Impeller 렌더링 엔진을 활용한 그래픽 최적화 기법
  - Skia
    - 기존 플러터의 디폴트 엔진, GPU 기반 벡터 렌더링 제공
  - Impeller
    - shader pre-compilation 기반의 최신 렌더러로 iOS/Android 에서 더 빠른 프레임 렌더링 가능
    - 최적화를 위해서는 repaintBoundary, const 위젯, CustomPaint 최적화 등을 병행해야 함

- Flutter의 주요 특징과 장단점
  - 장점
    - 하나의 코드 베이스로 iOS/Android/Web/Desktop 모두 대응, 높은 생산성, 핫 리로드 성능 우수
  - 단점
    - 빌드 사이즈 큼
    - 고급 네이티브 기능 접근 시 플랫폼 채널 필요
    - iOS 최신 API 대응 느림, UI 일관성과 빠른 MVP 제작에 매우 적합

- Dart 언어의 특징
  - 정적 타입 언어이면서 동적 언어처럼 간결한 문법
  - 널 안정성, async/await, FFI, 확장 메서드 등 최신 기능 제공
  - AOT & JIT 컴파일 모두 지원
  - 플러터와 결합하여 높은 성능과 생산성 제공

- Flutter에서의 상태 관리 방법 (Provider, Riverpod, Bloc 등)
  - Provider
    - 가장 보편적인 관리 방식, 간단한 구조에 적합
  - Riverpod
    - 프로바이더 단점 개선한 구조적 상태관리 라이브러리
    - 테스트 및 DI에 장점
  - Bloc
    - Event-State 기반의 명확한 흐름이 특징
    - 복잡한 앱에 적합

- Flutter의 Hot Reload와 Hot Restart의 차이점
  - Hot Reload
    - 코드 변경 사항을 즉시 반영하나 상태는 유지
  - Hot Restart
    - 앱을 완전히 재시작하여 모든 상태 초기화
  - 개발 중 UI 수정 시 핫리로드 / 구조 변경시 핫 리스타트 사용

- Flutter의 Widget Tree와 Element Tree의 차이점
  - Widget Tree
    - 선언적인 UI 구조, Immutable
  - Element Tree
    - 위젯의 실제 인스턴스 관리
    - 렌더링과 상태를 포함
  - 위젯은 블루프린트, 엘리먼트는 그 실행체
    - 구조, 구현체라는 의미

- Flutter의 렌더링 프로세스
  - 위젯 > 엘리먼트 > 렌더 객체로 구성
  - 빌드 > 레이아웃 > 페인트 > 컴포지팅 > Raster 단계
  - Skia 엔진이 GPU와 통신 > 화면 렌더링 구성

- Dart의 Isolate와 멀티스레딩 처리 방법
  - 다트 자체는 단일 스레드 기반
  - isolate 로 병렬 처리
    - 서로 독립된 메모리 영역을 사용하여 메시지로 통신
    - 복잡한 연산이나 백그라운드 작업에서 UI Thread 차단을 방지

- Flutter의 Skia 그래픽 엔진
  - 구글의 오픈소스 2D 렌더링 엔진
  - 플러터의 핵심 그래픽 백엔드
  - 벡터 기반
  - OpenGL 또는 Vulkan을 통해 GPU 가속 렌더링을 수행
  - 빠른 UI 성능과 플랫폼 일관성을 제공

- Dart의 Sound Null Safety와 Migration 전략
  - Sound Null Safety는 널 가능성을 컴파일 타임에 체크하여 안정성 향상
  - String?, late, ! 등 문법 활용
  - 기존 프로젝트는 dart migrate 명령어로 점진적 전환 가능
  - 런타임 오류를 줄이고 유지보수 측면 향상

- Flutter에서 Navigator 2.0의 장점과 기존 방식과의 차이점
  - Navigator 1.0은 Stack 기반의 imperative 방식 (push/pop)
    - 명령형 방식

  - Navigator 2.0은 declarative 방식으로 URL 기반 라우팅 및 브라우저 히스토리 지원에 유리
    - 선언형 방식
    - 복잡한 앱 또는 웹 지원에 필수적인 구조

- Flutter의 InheritedWidget과 Provider 패턴의 차이점
  - InheritedWidget은 플러터 내장 상태 전달 방식이나 사용과 유지보수가 어려움
  - Provider는 이를 더 추상화해 더 간편하게 상태를 전달하고 구독 가능하게 함
    - Provider는 InheritedWidget 위에 만들어진 래퍼 라이브러리

- Flutter에서 setState()가 불필요한 리빌드를 초래하는 이유
  - 해당 StatefulWidget 전체를 다시 빌드하므로, 리빌드 범위 넓음
  - 세분화된 상태 관리를 하지 않으면 작은 변화에도 전체 위젯 재구성되어 성능에 악영향
    - 개선책
      - ValueNotifier, Provider, Riverpod 등 사용

- Flutter에서 Isolate를 활용하는 이유
  - UI 메인 스레드가 차단되지 않도록 무거운 연산을 별도 스레드에서 처리하기 위한 목적
    - 예: 이미지 디코딩, 압축, JSON 파싱
  - compute()함수는 가장 간단한 Isolate 활용 방법
    - 앱의 응답성 유지, 복잡한 작업 동시에 수행 가능

- Flutter에서 FFI(Foreign Function Interface)를 활용하는 이유
  - FFI는 C/C++ 등 네이티브 코드와 직접 연동 가능하게 해줌
  - 성능이 중요한 로직 (이미지 처리, 암호화 등)을 직접 호출할 때 사용

- Flutter에서 AnimatedList와 ListView.builder의 차이점
  - AnimatedList
    - 아이템 추가/삭제 시 애니매이션 제공
  - ListView.builder
    - 정적 리스트를 효율적으로 렌더링할 때 적합

- Flutter에서 go_router와 기존 Navigator의 차이점
  - go_router
    - 선언적 라우팅 방식
    - URL 동기화, 리다이렉트, 쉘 라우트 같은 기능이 강화
  - 기존 Navigator
    - 명령형 방식의 푸시/팝 구조

- Flutter에서 Canvas API를 활용하는 방법
  - CustomPainter를 사용해 캔버스에 직접 그리기 가능
  - 선, 원, 텍스트 등 복잡한 커스텀 그래픽을 구현

- Flutter에서 SafeArea가 필요한 이유
  - 디바이스의 노치, 상태바, 홈 인디케이터 등 시스템 UI 영역을 피해서 콘텐츠 표시
  - 화면 요소가 잘리지 않도록 보호하는 용도로 사용

- Flutter에서 ExpansionTile과 ListTile의 차이점
  - ExpansionTile
    - 열고 닫을 수 있는 목록 구조로 하위 항목 포함 가능
  - ListTile
    - 단일 행 항목 표현할 때 사용

- Flutter에서 build() 함수의 역할과 성능 최적화 방법
  - build() 함수 역할
    - 위젯 UI를 그리는 메인 함수
    - 상태 변경 시 호출됨
  - 성능 최적화 방법
    - 리빌드를 최소화하기 위해 const, shouldRebuild, memoization 등을 활용할 수 있음

- Flutter에서 SliverAppBar와 AppBar의 차이점
  - AppBar
    - 고정된 헤더
  - SilverAppBar
    - 스크롤에 따라 축소/확장/고정 동작 가능
    - CustomScrollView 에서 유연한 UI 구성 가능

- Flutter에서 FutureBuilder와 StreamBuilder의 차이점
  - FutureBuilder
    - 단일 비동기 결과 처리
  - StreamBuilder
    - 여러 이벤트를 지속적으로 수신하는 스트림을 처리
  - API 요청, 실시간 데이터 구독처럼 용도에 따라 선택됨

- Flutter에서 RepaintBoundary의 역할
  - 해당 위젯을 별도 레이어로 분리해 불필요한 리렌더링 방지
  - 스크롤 리스트나 애니매이션에서 성능 최적화에 유리

- Flutter에서 const 키워드를 사용할 때 성능 최적화가 되는 이유
  - const는 빌드 시점에 인스턴스를 고정
  - 위젯 트리 재구성 시 재생성되지 않음
  - 리렌더링 비용을 줄이고 불필요한 리빌드 방지

- Flutter의 State Restoration
  - 정의
    - 앱 종료나 백그라운드에서 제거되었을 때 이전 상태를 복원하는 기능
  - 사용자 인터랙션을 잃지 않고 앱 복구 가능 > UX 향상

- Flutter에서 navigator key를 사용하는 이유
  - GlobalKey<NavigatorState>를 사용 시 컨텍스트 없이도 전역에서 라우팅 제어 가능
  - 예시
    - 알림 클릭 시 특정 화면으로 이동하는 등의 상황에서 유용

- Flutter에서 Platform Channel을 활용한 네이티브 통신 방식
  - 플러터와 안드로이드, iOS 간에 메서드 호출을 주고받기 위해 MethodChannel 사용
  - 네이티브 기능 (예: 블루투스, 센서)을 직접 제어 가능

- Flutter에서 DevTools을 활용한 성능 최적화 방법
  - DevTools는 렌더링 시간, 위젯 리빌드, 메모리 사용량 등을 시각화해 성능 병목을 분석하는 도구
  - Timeline, Repaint Rainbow, Widget Inspector 등을 자주 활용

- Flutter에서 Platform Views를 사용하는 이유
  - 플러터 위에 네이티브 뷰 (안드로이드 뷰, iOS UIView)를 직접 삽입할 수 있는 기능
  - 예: 웹뷰, 구글 맵스 등 네이티브 UI가 필요한 경우에 사용

- Flutter의 implicit animation과 explicit animation의 차이점
  - Implicit Animation(AnimatedContainer 등)은 상태 변경 시 자동 애니매이션 제공
  - Explicit Animation(AnimatedController)은 더 세밀한 타이밍과 제어 가능

- Flutter Web과 Mobile의 차이점
  - 웹은 SEO, 초기 로딩 속도, 브라우저 호환성 등 한계 존재
  - 모바일은 네이티브 성능과 다양한 플랫폼 API 접근 유리
    - 즉, 위젯 호환성과 제약 사항이 다름

- Dart의 Null Safety 개념
  - 정적 분석을 통해 NULL 오류 방지
  - String? -> NULL 허용 / String -> NULL 허용 안됨
  - 변수 초기화 전 사용 방지, 컴파일 타임 오류로 잡아줌

- Dart의 Future와 Stream 차이점
  - Future
    - 한번만 반환
    - 비동기 작업 결과 (1회성)
    - API 응답에 주로 사용
  - Stream
    - 여러번 반환
    - 이벤트나 데이터 흐름 (다회)
    - 센서 데이터, 버튼 클릭 등에 사용
  - 예시
    ```dart
    Future<String> getData() async => 'value';
    Stream<int> numberStream() => Stream.periodic(Duration(seconds: 1), (i) => i);
    ```

- Dart의 late 키워드 사용 시점
  - 초기화 지연이 필요할 때 사용
  - Null Safety에서 Non-Null 변수를 선언하지만, 초기화는 나중에 진행
  - 예시
    ```dart
    late String name;
    void init() {
      name = 'Aiden'; // 나중에 할당
    }
    ```
  - 초기화 전에 사용 시 LateInitializationError 발생

- Dart의 mixin과 abstract class의 차이
  - mixin
    - 기능 재사용 목적
    - 생성자 사용 불가
    - 상태 없음 (권장 사항)
    - 여러 mixin 조합 가능 (다중 상속 가능)
  - abstract class
    - 상속 구조 및 규격 정의
    - 생성자 사용 가능
    - 상태 가짐 가능
    - 다중 상속 불가
  - 예시
    ```dart
    mixin Logger {
      void log(String msg) => print(msg);
    }

    abstract class Animal {
      void makeSound();
    }
    ```

- Dart에서 async와 await 동작 방식
  - async > Future 반환
  - await > Future 완료까지 기다림 (Non-Blocking)
  - 예시
    ```dart
    Future<void> loadData() async {
      final data = await fetchFromApi(); // fetch가 끝날 때까지 기다림
    }
    ```
  - 추가 설명
    - Non-Blocking
      - 번호표 받고 기다리는 동안 다른 일 하다가 호출되면 반응
        - 다른 일을 하다가 결과 오면 그때 반응
    - Blocking
      - 식당 앞에서 줄 서서 음식 나오기만 기다리는 것
        - 아무 일도 못하고 대기
    - Non-Blocking 예제
      ```dart
      void main() {
        print('A: 시작');
        waitSomething();
        print('C: 다음 작업 계속함');
      }

      Future<void> waitSomething() async {
        print('B: 대기 시작');
        await Future.delayed(Duration(seconds: 2)); // 2초 기다림
        print('D: 대기 끝, 후속 작업');
      }
      ```
      ```makefile
      A: 시작
      B: 대기 시작
      C: 다음 작업 계속함 <- 이 부분이 핵심
      D: 대기 끝, 후속 작업
      ```
      - await 는 2초 동안 해당 함수 (waitSomething)의 후속 코드(D)를 보류하지만
      - main 함수 전체를 멈추지는 않음
      - 그래서 C가 먼저 출력됨 -> 넌 블럭킹
    - 핵심 요약 정리
      - await는 해당 함수의 다음 줄을 잠깐 멈춤 시키지만 전체 프로그램의 실행을 막지는 않음
      - Flutter UI에서 await은 UI를 멈추지 않도록 보장함 (사용자가 앱을 계속 사용할 수 있음)

- Dart에서 const와 final의 차이점
- Dart에서 factory constructor 역할
- Flutter의 StatefulWidget과 StatelessWidget의 차이
- Flutter의 Widget 트리에서 BuildContext의 역할
- Flutter의 애니메이션 시스템(AnimationController, Tween, CurvedAnimation)을 설명
- Dart의 Zone은 무엇이며, 어떤 상황에서 유용한가?
- Dart에서 extension을 활용하여 기존 클래스를 확장하는 방법


- Future와 Completer의 차이점과 활용법은?
- Dart의 typedef를 활용한 함수 타입 정의 방식은?
- dart:ffi를 활용하여 Native 코드와 상호작용하는 방법을 설명하라.
- Flutter에서 setState를 많이 사용하면 성능 문제가 발생하는 이유는?
- InheritedWidget과 Provider의 차이점과 성능 차이를 비교하라.
- Flutter에서 RenderObject의 역할과 커스텀 위젯 제작 방법은?
- Flutter의 Platform Channels를 활용한 네이티브 코드 연동 방식은?
- Flutter 앱에서 메모리 관리를 최적화하는 방법은?
- Flutter에서 Hero 애니메이션이 동작하는 방식과 제약 사항은?
- Flutter에서 Sliver 위젯을 활용한 고급 리스트 렌더링 기법을 설명하라.


- Flutter의 새로운 impeller 렌더링 엔진이 기존 엔진 대비 갖는 장점은?
- 플러터에서 디자인 스타일 구현 방법, 위치, 통상적인 방법
- Flutter의 StatelessWidget이 내부적으로 StatefulWidget보다 성능이 좋은 이유는?
- StatefulWidget의 dispose() 메서드는 언제 호출되는가?
- didUpdateWidget()은 언제 호출되는가?
- GlobalKey는 언제 필요하며, LocalKey와의 차이점은?
- CustomPainter와 RenderObject의 차이는?
- PreferredSizeWidget을 활용하는 시나리오는?
- CustomScrollView를 활용하여 SliverList와 SliverGrid를 함께 사용하는 방법은?
- RepaintBoundary를 사용할 때의 장점과 주의할 점은?


- Constraints 객체의 역할과 BoxConstraints를 직접 설정해야 하는 이유는?
- IntrinsicHeight과 IntrinsicWidth 위젯을 사용할 때 성능에 미치는 영향은?
- ScrollController와 NotificationListener를 활용하여 스크롤 이벤트를 감지하는 방법은?
- AutofillGroup 위젯을 사용해야 하는 경우는?
- NestedScrollView를 사용할 때 SliverAppBar와 body가 올바르게 동작하지 않는 경우 해결 방법은?
- TickerProviderStateMixin과 SingleTickerProviderStateMixin의 차이점은?
- AnimatedBuilder와 AnimatedContainer 중 어떤 것이 더 성능이 좋은가?
- CurvedAnimation에서 Curves.easeInOut과 Curves.bounceOut의 차이점은?
- Hero 애니메이션이 정상적으로 동작하지 않는 경우 해결 방법은?
- ShaderMask를 활용하여 텍스트나 이미지에 그라디언트 효과를 적용하는 방법은?


- AnimatedSwitcher를 활용하여 리스트 항목 변경 애니메이션을 적용하는 방법은?
- ImageShader를 활용하여 커스텀 효과를 구현하는 방법은?
- dart:developer 패키지를 활용하여 디버깅을 최적화하는 방법은?
- Performance Overlay에서 Raster Thread가 병목이 되는 이유와 해결 방법은?
- Flutter Inspector에서 RepaintBoundary 색상이 계속 변하는 경우 해결 방법은?
- Flutter DevTools의 Timeline을 활용하여 프레임 드랍을 분석하는 방법은?
- Dart Garbage Collector(GC)가 Flutter에서 메모리 관리를 하는 방식은?
- Flutter에서 메모리 릭이 발생하는 주요 원인과 해결 방법은?
- Profile Mode와 Release Mode에서 성능 차이가 발생하는 이유는?
- Dart VM의 JIT(Just-In-Time)와 AOT(Ahead-Of-Time) 컴파일 차이는?
- ListView.builder에서 itemCount를 설정하지 않으면 성능에 어떤 영향을 미치는가?


- SliverPersistentHeaderDelegate를 활용하여 성능을 최적화하는 방법은?
- StatefulWidget에서 didChangeDependencies()와 initState()의 차이점은?
- InheritedWidget을 사용해야 하는 경우는?
- ChangeNotifier와 StateNotifier 중 어떤 것이 성능적으로 더 우수한가?
- BLoC에서 Cubit을 사용하면 어떤 장점이 있는가?
- 상태관리 라이브러리 없이 전역적인 상태 관리가 가능한가? 가능하다면 어떻게 구현하는가?
- StreamController.broadcast()를 사용할 때 발생할 수 있는 문제는?
- GetX에서 Bindings를 활용하여 의존성 주입을 최적화하는 방법은?
- Flutter Hooks에서 useEffect를 사용할 때 발생할 수 있는 문제점은?
- Riverpod에서 ScopedProvider와 Override 기능을 활용하는 방법은?
- State Restoration이 필요한 경우는?


- Dio 패키지에서 Interceptors를 활용하는 방법은?
- Flutter에서 GraphQL을 사용할 때 cache policy를 설정하는 방법은?
- WebSockets을 사용할 때 StreamTransformer를 활용하는 이유는?
- Flutter에서 Rate Limiting을 구현하는 방법은?
- Retrofit을 활용하여 REST API 호출을 최적화하는 방법은?
- Dart에서 Future.wait()와 Future.forEach()의 차이점은?
- Dart에서 Completer를 활용하여 Future를 제어하는 방법은?
- Firebase Remote Config를 활용하여 앱의 동적 업데이트를 적용하는 방법은?
- SQLite와 Hive, Drift의 차이점은?
- Flutter에서 SSL Pinning을 적용하는 방법은?
- Flutter Secure Storage와 SharedPreferences의 차이점은?
- AES 암호화를 활용하여 데이터를 암호화하는 방법은?


- Dart에서 RSA 키 쌍을 생성하고 이를 활용하여 데이터를 암호화하는 방법은?
- Flutter에서 App Tracking Transparency (ATT)를 적용하는 방법은?
- Flutter에서 Firebase App Check를 활용하여 API 보안을 강화하는 방법은?
- Flutter에서 패스워드 필드의 자동 완성을 방지하는 방법은?
- Flutter에서 Accessibility Inspector를 활용하여 접근성을 개선하는 방법은?
- Flutter Web과 Flutter Mobile에서 Navigator 2.0을 사용할 때 차이점은?
- Flutter에서 Tizen 및 Embedded Linux를 지원하는 방식은?
- Flutter에서 MacOS 및 Windows 지원을 위한 주요 고려사항은?
- Flutter에서 FlutterFlow 같은 Low-Code 툴을 활용하여 개발을 최적화하는 방법은?
- Flutter에서 PWA(Progressive Web App)를 구현하는 방법은?
- Flutter에서 Desktop 앱을 개발할 때 고려해야 할 점은?


- Flutter에서 WebRTC를 활용하여 화상 채팅을 구현하는 방법은?
- Flutter에서 Skia 및 Impeller 렌더링 엔진을 활용한 최적화 방법은?
- Flutter 3.22에서 추가된 주요 기능과 개선 사항은?
- Flutter 4.0에서 기대할 수 있는 변화는?
- Impeller 렌더링 엔진이 기존 Skia 대비 성능적으로 어떤 이점을 제공하는가?
- Flutter DevTools에서 memory leak을 탐지하는 방법은?
- Flutter에서 openAI API를 활용한 ChatGPT 챗봇 기능을 구현하는 방법은?
- Flutter에서 Live Activities를 활용하여 실시간 업데이트를 구현하는 방법은?
- Flutter에서 Dynamic Island를 지원하는 방법은?