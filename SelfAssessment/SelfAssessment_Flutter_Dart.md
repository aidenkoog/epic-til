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

- Flutter에서 Singleton 패턴을 활용하여 상태를 관리하는 방법은?
- Flutter에서 App Lifecycle을 관리하는 방법은?
- Flutter에서 상태 관리 선택 기준은 무엇인가?
- Flutter에서 AnimatedBuilder를 활용한 상태 관리는 어떤 장점을 가지는가?


- Flutter에서 OverlayEntry를 활용한 UI 상태 관리는 어떻게 하는가?
- Flutter에서 StatefulWidget이 필요한 경우는?
- Flutter에서 ChangeNotifier와 StateNotifier의 차이점은?
- Flutter에서 FutureProvider와 StreamProvider의 차이점은?
- Flutter에서 MultiProvider를 활용하는 이유는?
- Flutter에서 CustomPainter를 활용한 그래픽 구현 방법은?
- Flutter에서 SliverWidgets를 사용하는 이유는?
- Flutter에서 RepaintBoundary를 활용하여 성능을 최적화하는 방법은?
- Flutter에서 const 생성자를 활용하면 성능이 향상되는 이유는?
- Flutter에서 Image.memory()와 Image.asset()의 차이점은?
- Flutter에서 Hero 애니메이션을 구현하는 방법은?
- Flutter에서 ShaderMask를 활용하는 방법은?
- Flutter에서 AspectRatio 위젯을 활용하는 이유는?
- Flutter에서 AnimatedList를 사용할 때의 장점은?
- Flutter에서 ListView와 GridView의 차이점은?
- Flutter에서 Lottie를 활용한 애니메이션 적용 방법은?
- Flutter에서 NestedScrollView를 사용할 때 고려해야 할 점은?
- Flutter에서 Cupertino 디자인 시스템을 적용하는 방법은?
- Flutter에서 AppBar의 PreferredSizeWidget을 활용하는 이유는?
- Flutter에서 LayoutBuilder를 활용하여 반응형 UI를 구축하는 방법은?
- Flutter에서 AutoSizeText를 활용하여 가변 폰트 크기를 적용하는 방법은?
- Flutter에서 ClipRRect와 ClipPath의 차이점은?
- Flutter에서 ImageFilter를 활용한 블러 효과 구현 방법은?
- Flutter에서 RenderObject를 직접 구현하는 이유는?
- Flutter에서 GestureDetector와 InkWell의 차이점은?
- Flutter에서 Drawer 위젯을 활용한 내비게이션 방법은?
- Flutter에서 FloatingActionButton을 커스터마이징하는 방법은?
- Flutter에서 PageView 위젯을 활용하는 방법은?
- Flutter에서 커스텀 Shimmer 효과를 구현하는 방법은?
- Flutter에서 TabBar와 BottomNavigationBar의 차이점은?
- Flutter에서 기본적인 Theming을 적용하는 방법은?
- Flutter에서 SafeArea 위젯의 역할은?
- Flutter에서 BackdropFilter를 활용하여 UI를 디자인하는 방법은?
- Flutter에서 MaterialStateProperty를 활용하는 방법은?
- Flutter에서 Wrap과 Row, Column의 차이점은?
- Flutter에서 Dio와 http 패키지의 차이점은?
- Flutter에서 GraphQL을 활용하여 데이터를 불러오는 방법은?
- Flutter에서 REST API 호출 시 예외 처리를 구현하는 방법은?
- Flutter에서 Firebase Authentication을 연동하는 방법은?
- Flutter에서 JWT 토큰을 활용한 인증 구현 방법은?
- Flutter에서 WebSockets을 활용한 실시간 통신 방법은?
- Flutter에서 OAuth 2.0 인증을 구현하는 방법은?
- Flutter에서 API 호출을 위한 Rate Limiting을 적용하는 방법은?
- Flutter에서 SSL Pinning을 적용하는 방법은?
- Flutter에서 FlutterFire를 활용하여 Firebase 연동 방법은?
- Flutter에서 Clean Architecture를 적용한 네트워크 계층 설계 방법은?
- Flutter에서 Retrofit을 활용한 네트워크 요청 관리 방법은?
- Flutter에서 Refresh Token을 활용한 자동 로그인 구현 방법은?
- Flutter에서 Firebase Firestore와 Realtime Database의 차이점은?
- Flutter에서 GraphQL의 Query와 Mutation의 차이점은?
- Flutter에서 FormData를 활용한 파일 업로드 방법은?
- Flutter에서 Multi-part Request를 활용한 이미지 업로드 방법은?
- Flutter에서 API 응답을 캐싱하는 방법은?
- Flutter에서 에러 핸들링을 위한 Global Error Handler를 구현하는 방법은?
- Flutter에서 Web과 Mobile 개발의 차이점은?
- Flutter에서 Desktop 앱을 개발할 때 고려해야 할 점은?
- Flutter에서 Tizen 및 Embedded 기기용 앱을 개발할 때 필요한 사항은?
- Flutter에서 PWA(Progressive Web App)를 구현하는 방법은?
- Flutter에서 Native Code(Android/iOS)를 호출하는 방법은?
- Flutter에서 isolate를 활용한 병렬 처리 방법은?
- Flutter에서 FFI(Foreign Function Interface)를 활용하는 이유는?
- Flutter에서 ML Kit을 활용한 이미지 인식 기능을 구현하는 방법은?
- Flutter에서 WebRTC를 활용한 영상 통화 기능을 구현하는 방법은?
- Flutter에서 Background Task를 수행하는 방법은?
- Flutter에서 Firebase Analytics를 활용하는 방법은?
- Flutter에서 Background Fetch를 활용하는 방법은?
- Flutter에서 OpenAI API를 활용한 챗봇 기능을 구현하는 방법은?
- Flutter에서 Dynamic Link를 활용한 딥링크 구현 방법은?
- Flutter에서 FlutterFlow와 같은 Low-Code 개발 도구를 활용하는 방법은?
- Flutter에서 Flare 애니메이션을 적용하는 방법은?
- Flutter에서 Riverpod의 AutoDispose 기능을 활용하는 방법은?
- Flutter에서 플랫폼별 코드(Android, iOS)를 다르게 적용하는 방법은?
- Flutter에서 Dart의 null-safety 기능을 활용하는 방법은?
- Flutter에서 CI/CD 파이프라인을 구축하는 방법은?
- Flutter에서 FFI(Foreign Function Interface)를 활용하여 네이티브 모듈과 상호작용하는 방법은?
- Flutter의 Platform Channels과 FFI의 차이점 및 활용 방법은?
- Flutter 3.22에서 추가된 주요 기능과 최적화 기법은?
- Flutter에서 CustomRenderObjects를 활용하여 UI 성능을 최적화하는 방법은?
- Flutter에서 Skia 및 Impeller 렌더링 엔진을 활용한 그래픽 최적화 기법은?
- Flutter의 주요 특징과 장단점은 무엇인가요?
- Dart 언어의 특징을 설명해주세요.
- Flutter에서의 상태 관리 방법을 설명해주세요. (Provider, Riverpod, Bloc 등)
- Flutter의 Hot Reload와 Hot Restart의 차이점은 무엇인가요?
- Flutter의 Widget Tree와 Element Tree의 차이점은 무엇인가요?
- Flutter의 렌더링 프로세스에 대해 설명해주세요.
- Dart의 Isolate와 멀티스레딩 처리 방법을 설명해주세요.
- Flutter의 Skia 그래픽 엔진에 대해 설명해주세요.
- Dart의 Sound Null Safety와 Migration 전략을 설명해주세요.
- Flutter에서 Navigator 2.0의 장점과 기존 방식과의 차이점은?
- Flutter의 InheritedWidget과 Provider 패턴의 차이점은?
- Flutter에서 setState()가 불필요한 리빌드를 초래하는 이유는?
- Flutter에서 Isolate를 활용하는 이유는?
- Flutter에서 FFI(Foreign Function Interface)를 활용하는 이유는?
- Flutter에서 AnimatedList와 ListView.builder의 차이점은?
- Flutter에서 go_router와 기존 Navigator의 차이점은?
- Flutter에서 Canvas API를 활용하는 방법은?
- Flutter에서 SafeArea가 필요한 이유는?
- Flutter에서 ExpansionTile과 ListTile의 차이점은?
- Flutter에서 build() 함수의 역할과 성능 최적화 방법은?
- Flutter에서 SliverAppBar와 AppBar의 차이점은?
- Flutter에서 FutureBuilder와 StreamBuilder의 차이점은?
- Flutter에서 RepaintBoundary의 역할은?
- Flutter에서 const 키워드를 사용할 때 성능 최적화가 되는 이유는?
- Flutter의 State Restoration이란 무엇인가?
- Flutter에서 isolate를 사용하는 이유는?
- Flutter에서 navigator key를 사용하는 이유는?
- Flutter에서 Platform Channel을 활용한 네이티브 통신 방식은?
- Flutter에서 DevTools을 활용한 성능 최적화 방법은?
- Flutter에서 Platform Views를 사용하는 이유는?
- Flutter의 implicit animation과 explicit animation의 차이점은?
- Flutter의 State Management를 어떤 방식으로 사용했는가? (Provider, Riverpod, Bloc 등)
- Flutter에서의 네이티브 연동 (MethodChannel) 경험이 있는가?
- Flutter에서 성능 최적화를 위해 어떤 기법을 적용했는가?
- Flutter Web과 Mobile의 차이점은?
- Dart의 Null Safety 개념을 설명하라.
- Dart의 Future와 Stream의 차이점은?
- Dart의 late 키워드는 언제 사용하는가?
- Dart의 mixin과 abstract class의 차이는?
- Dart에서 async와 await은 어떻게 동작하는가?
- Dart에서 const와 final의 차이점은?
- Dart의 Isolates는 어떻게 동작하는가?
- Dart에서 factory constructor는 어떤 역할을 하는가?
- Flutter의 StatefulWidget과 StatelessWidget의 차이는?
- Flutter에서 상태 관리(State Management)를 어떤 방식으로 구현하는가? (Provider, Riverpod, Bloc 등)
- Flutter의 Widget 트리에서 BuildContext의 역할은?
- setState()는 언제 사용하는가?
- Flutter의 Hot Reload와 Hot Restart의 차이는?
- Flutter의 Navigator 1.0과 2.0의 차이점은?
- Flutter에서 Platform-specific 코드(Android, iOS)와 연동하는 방법은?
- Flutter의 애니메이션 시스템(AnimationController, Tween, CurvedAnimation)을 설명하라.
- Dart의 Zone은 무엇이며, 어떤 상황에서 유용하게 사용할 수 있는가?
- Dart의 mixin과 abstract class의 활용 방식과 차이점은?
- Dart에서 extension을 활용하여 기존 클래스를 확장하는 방법을 설명하라.
- Dart의 Isolates를 사용한 병렬 처리 기법을 설명하라.
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