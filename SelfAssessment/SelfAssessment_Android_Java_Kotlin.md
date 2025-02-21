# Expected Questions

Organized expected questions & answers

## Android (+Java, Kotlin, Coroutine)

- Jetpack Compose와 기존 XML 기반 UI의 차이점
    - Jetpack Compose (선언적 UI)
        - UI를 함수로 선언하여 상태(state)에 따라 UI를 자동 갱신
        - 데이터가 변경되면 UI가 자동으로 다시 그려짐(Recomposition)
    - XML 기반 UI (명령형 UI)
        - XML에서 UI를 정의하고, 변경이 필요할 때 findViewById 또는 ViewBinding을 사용하여 직접 조작
        - UI 변경 시 setText() 등 명령어로 상태 변경을 직접 반영해야 함
    - 코드 단순성 및 유지보수성
        - Jetpack Compose: XML과 Activity/Fragment 간의 분리가 필요 없음. UI를 Kotlin 코드에서 직접 작성 가능.
        - XML 기반 UI: XML과 Kotlin(Java) 코드가 분리되어 있어, UI 변경 시 코드 수정이 더 많아질 수 있음.
    - UI 업데이트 방식
        - Jetpack Compose: UI가 상태 변화에 따라 자동으로 다시 그려짐.
        - XML 기반 UI: UI 변경 시 notifyDataSetChanged(), invalidate() 등의 메서드를 직접 호출해야 함.
    - 퍼포먼스
        - Jetpack Compose: Recomposition(변경된 부분만 다시 그림) 최적화.
        - XML 기반 UI: View Hierarchy가 복잡해질수록 성능 저하 가능성이 높음
    - 테마 및 스타일 관리
        - Jetpack Compose: MaterialTheme을 사용해 테마 적용이 간편.
        - XML 기반 UI: styles.xml을 사용해야 하며, 다크모드 지원 등에서 추가 설정이 필요.
    - 애니메이션
        - Jetpack Compose: animate*AsState() 등을 활용해 간단한 코드로 애니메이션 구현 가능.
        - XML 기반 UI: ObjectAnimator, Lottie, Animation XML을 사용해야 함.
    - 기존 코드와의 호환성
        - Jetpack Compose: 기존 XML UI와 혼용 가능 (ComposeView 사용).
        - XML 기반 UI: Jetpack Compose 사용하려면 ComposeView로 포함해야 함.
            - ComposeView
                - Jetpack Compose를 기존 XML 기반의 Android UI(View 시스템)와 혼합할 수 있도록 해주는 Bridge View
                - 기존 XML 기반 UI 프로젝트에서 Jetpack Compose UI를 포함할 때 사용하는 View

- Android의 ViewModel과 LiveData의 차이점
    - 공통
        - ViewModel과 LiveData는 Android 앱의 상태 관리 및 UI 데이터 처리를 돕는 컴포넌트
    - ViewModel
        - ViewModel은 화면 회전이나 구성 변경(Configuration Changes) 시에도 데이터를 유지할 수 있는 컴포넌트
        - UI 관련 데이터를 저장하고 관리
        - 액티비티/프래그먼트가 소멸되어도 데이터 유지
        - 수명 주기를 인식하여 메모리 누수를 방지
        - 데이터 로직과 UI를 분리하여 클린 아키텍처 구현 가능
    - LiveData
        - LiveData는 관찰 가능한 데이터 홀더(Observable)로, 데이터가 변경될 때 자동으로 UI에 반영되는 컴포넌트
        - Lifecycle-aware: 액티비티/프래그먼트가 활성 상태일 때만 데이터 업데이트를 수신
        - 자동 UI 업데이트: 값이 변경되면 UI가 자동으로 업데이트
        - 메모리 누수 방지: 비활성 상태인 UI에는 업데이트를 전달하지 않음

- Android에서 Coroutine과 RxJava의 차이점
    -  Coroutine
        - 단순한 비동기 작업 (네트워크 요청, 데이터베이스 호출 등)
        - 코드를 동기처럼 간결하게 유지 가능
        - Android에서 공식적으로 지원하는 비동기 처리 방식
        - 간단한 비동기 작업, 가독성이 좋은 코드 작성, 최신 Android 공식 추천 방식
        - 경량 스레드(Coroutine)로 메모리 소비 적음
        - Kotlin 전용
        - Flow (buffer, conflate) 사용한 백프레셔 처리
    - RxJava
        - 복잡한 데이터 흐름 처리, 다중 스트림 관리, 강력한 비동기 프로그래밍
        - 이벤트 기반 프로그래밍이 필요한 경우 (예: UI 이벤트, 스트리밍 데이터)
        - 데이터 흐름을 적극적으로 변형(map, flatMap, filter 등)필요 시
        - Observable 체이닝 방식으로 비동기 흐름 관리
        - 여러 개의 비동기 데이터 소스를 결합 필요 시
        - 강력한 스트림 처리 기능 제공하지만 스레드 비용 증가
        - Java, Kotlin 지원
        - Flowable 사용한 백프레셔 처리

- Android Coroutine과 RxJava에서 백프레셔 처리 방법
    - 백프레셔(Backpressure) 개념
        - 백프레셔(Backpressure)란 데이터 생산 속도와 소비 속도의 불균형으로 인해 발생하는 문제
        - 생산자(Producer)가 데이터를 너무 빨리 생성하여 소비자(Consumer)가 처리하지 못하는 문제
        - 생산자가 데이터를 너무 빠르게 방출하면, 소비자가 이를 처리하지 못하는 경우 발생
        - 생산자(Producer): 데이터를 생성하는 측 (예: 네트워크 응답, 센서 데이터, 이벤트 스트림 등)
        - 소비자(Consumer): 데이터를 소비하는 측 (예: UI 업데이트, 파일 저장 등)
    - 백프레셔 문제가 발생 시 이슈
        - 메모리 과부하 (버퍼에 데이터가 쌓임)
        - 애플리케이션 성능 저하 (CPU 과부하, ANR 발생 가능)
        - 데이터 손실 (처리되지 못한 데이터가 버려짐)
    - 백프레셔 구현
        - 10,000개의 데이터를 딜레이 없이 방출
        - 소비자 측에서는 딜레이 적용해서 데이터를 천천히 처리
        - 느리게 소비하기 때문에 버퍼가 가득차는 문제 발생
    - Coroutine, RxJava에서의 백프레셔 처리 방법
        - Coroutine
            - buffer(): 생산자가 빠르게 데이터를 방출해도 버퍼를 사용하여 소비자가 처리할 때까지 대기
            - conflate(): 최신 데이터만 유지하고 이전 데이터는 삭제 (속도 우선)
            - collectLatest(): 소비자가 새로운 데이터를 받을 때, 이전 처리 중인 데이터를 취소하고 최신 데이터만 처리
        - RxJava
            - Flowable 사용
                - onBackpressureDrop(): 오래된 데이터를 버리고 최신 데이터만 유지
                - onBackpressureLatest(): 가장 최근 데이터만 유지

- Android의 Room Database와 SQLite의 차이점
    - SQL 쿼리 작성 방식
        - SQLite: 직접 SQL 쿼리를 사용해야 하며, 문법 오류를 개발자가 직접 해결해야 함 (rawQuery)
        - Room: @Query 어노테이션을 사용하여 간결한 SQL 작성 가능, 컴파일 타임에 문법 오류 체크 가능
    - 보일러플레이트 코드
        - SQLite: Cursor를 사용해야 하며, 데이터를 수동으로 매핑해야 함
        - Room: 자동으로 객체 매핑을 수행하며, 개발자의 부담을 줄임
    - 데이터 무결성 및 타입 안정성
        - SQLite: 타입 안정성 보장 없음 (동적 SQL 실행)
        - Room: Kotlin의 data class와 함께 사용하여 타입 안정성을 보장
    - LiveData 및 Flow 지원
        - SQLite: 직접 구현 필요 (콜백 등)
        - Room: LiveData, Flow를 지원하여 데이터 변경 사항을 자동 감지 가능
    - 트랜잭션 및 비동기 처리
        - SQLite: 개발자가 BEGIN TRANSACTION, END TRANSACTION을 직접 관리 필요
        - Room: @Transaction 어노테이션으로 간편하게 트랜잭션 처리 가능
            - 데이터 삭제 > 데이터 삽입 두가지의 트랜잭션을 나열만 하면 됨
    - Migration (데이터베이스 스키마 변경)
        - SQLite: 기존 테이블을 삭제하고 새로 생성하는 방식이 일반적
        - Room: Migration 클래스를 사용하여 데이터 유지하면서 스키마 변경 가능
            - 데이터 유지 상태에서 컬럼만 추가 가능

- DAO 설명
    - DAO 개념 설명
        - Data Access Object
        - 데이터베이스와 애플리케이션 사이의 데이터 접근을 추상화하는 객체
            - 데이터베이스 - DAO - 애플리케이션
        - DAO를 사용하면 SQL 쿼리를 직접 작성하지 않고, 데이터베이스 작업을 객체지향적인 방식으로 처리 가능
        - Entity(Table 이름) 데이터 모델 정의, DAO 인터페이스 정의, Room 데이터베이스 정의 순으로 구현 필요
        - Room Database에서 DAO는 인터페이스로 정의되며, 데이터베이스에서 데이터를 조회, 삽입, 삭제, 업데이트하는 역할
    - DAO 역할과 장점
        - SQL 쿼리를 캡슐화: 데이터 접근 로직을 분리하여 코드의 유지보수성을 높임
        - 객체 지향적인 데이터 처리: SQL을 직접 사용하지 않고, 엔티티 클래스를 이용하여 데이터를 조회/수정
        - 비즈니스 로직과 데이터베이스 로직 분리: 데이터베이스 변경이 있어도 앱 로직에 미치는 영향을 최소화
        - Room이 SQL 쿼리 오류를 컴파일 타임에 체크: @Query 어노테이션을 사용하여 SQL 문법 오류를 방지

- Android에서 Dependency Injection을 구현하는 방법
    - DI(Dependency Injection) 개념
        - 객체가 직접 의존성을 생성하는 것이 아니라, 외부에서 필요한 객체를 주입(Inject)받는 방식을 의미
        - 이를 통해 코드의 재사용성, 유연성, 단위 테스트 용이성이 증가
    - Android에서 DI를 구현하는 방법
        - 수동 의존성 주입 (Constructor Injection)
        - Dagger/Hilt (Google 공식 DI 프레임워크)
            - Hilt: Dagger 기반의 Android 공식 DI 라이브러리로, 생성자 주입 및 자동 의존성 주입을 지원
        - Koin (Kotlin DSL 기반 DI 라이브러리)
    - Hilt 적용 방법
        - 모든 Hilt 주입 객체는 @HiltAndroidApp을 사용하여 초기화 필수
        - Module 사용, @Module과 @InstallIn을 사용하여 의존성을 제공
        - ViewModel에 의존성을 자동으로 주입
            - @Inject constructor(...) : 생성자를 통해 의존성 자동 주입
            - @HiltViewModel : ViewModel에 Hilt 적용
        - Activity: @AndroidEntryPoint를 사용하여 자동으로 의존성을 주입 가능
    - Hilt 단점
        - 빌드 속도 증가 (Annotation Processor 사용)
    - Koin 설명
        - Kotlin DSL 기반의 가볍고 직관적인 DI 라이브러리
        - XML이나 Annotation 없이 간단한 DSL 문법으로 DI를 설정 가능
        - 모듈 정의
            - single {} → 싱글톤 객체 생성
            - viewModel {} → ViewModel 객체 생성
        - Koin 초기화
            - startKoin { androidContext() modules() }
        - Koin 장점
            - Kotlin DSL을 활용한 간결한 문법
            - Reflection이 없어 빠른 실행 속도
            - 초기 설정이 간단하며 빌드 속도 빠름
        - Koin 단점
            - Hilt보다 공식 지원이 부족함
            - 대규모 프로젝트에서는 Hilt보다 관리가 어렵다는 의견 있음

- 리플렉션(Reflection) 설명
    - 프로그램이 실행 중(Run-time)에 클래스, 메서드, 변수 등의 정보를 동적으로 분석하고 수정/조작할 수 있는 기능
    - 실행 중에 클래스 타입을 확인하거나, 동적으로 객체를 생성하고, 메서드를 호출 가능
    - 보통 정적인 코드에서는 컴파일 시점에 클래스와 메서드가 결정되지만, 리플렉션을 사용하면 실행 중에 동적으로 접근 가능
    - 리플렉션의 주요 기능
        - 클래스 정보 확인 → 클래스 이름, 패키지명, 메서드, 필드 조회
        - 객체 생성 → 클래스 이름을 문자열로 받아 인스턴스 동적 생성
        - 메서드 호출 → 특정 메서드를 동적으로 실행
        - 필드 값 변경 → private 필드 포함 동적으로 값 변경
    - 장점
        - 유연성 증가 → 실행 중에 객체를 다룰 수 있음.
        - 동적 객체 생성 가능 → 컴파일 시점에 알 수 없는 클래스를 동적으로 생성 & 실행 가능
        - DI(의존성 주입), ORM (객체-관계 매핑)에 활용
            - Room, Hibernate 같은 ORM에서 리플렉션을 사용하여 데이터베이스 엔티티를 자동 매핑
            - ORM: Object Relational Mapping
    - 단점
        - 성능 저하 → 일반 코드보다 느림 (동적 호출이기 때문)
        - 안전성 문제 → private 필드, 메서드 접근 가능하여 보안 위험 발생 가능.
            - isAccessible = true
        - 복잡성 증가 → 유지보수 어려움
    - 리플렉션이 사용되는 대표적인 사례 (내부 구현부에서 리플렉션 기법 적용)
        - 의존성 주입 (DI)
            - Dagger, Hilt, Koin 같은 DI 프레임워크에서 리플렉션을 사용하여 의존성을 자동 주입
        - 객체-관계 매핑(ORM)
            - Room, Hibernate 같은 ORM에서 리플렉션을 사용하여 데이터베이스 엔티티를 자동 매핑.
        - JSON 직렬화/역직렬화
            - Gson, Moshi, Jackson 같은 라이브러리가 리플렉션을 사용하여 객체를 JSON으로 변환 및 복원
        - 테스트 프레임워크
            - JUnit, Mockito에서 리플렉션을 사용하여 private 메서드/필드를 테스트
    - 리플렉션을 최소화하는 방법
        - 성능을 위해 필요할 때만 리플렉션을 사용하는 것이 중요
        - 대체 방법 1: 인터페이스 + 생성자 주입 (DI 프레임워크 활용)
            - 클래스 생성자 인자로 인터페이스 타입 변수 설정
        - 대체 방법 2: 코틀린의 sealed class 활용하여 타입 안전성을 높임

- Retrofit과 Volley의 차이점
    - 개요
        - Retrofit
            - RESTful API 호출을 쉽게 할 수 있도록 설계된 HTTP 클라이언트
            - Gson, Moshi 등을 활용하여 JSON을 자동 직렬화/역직렬화 지원
            - 코루틴(Coroutine) 및 RxJava 지원
        - Volley
            - Google이 개발한 네트워크 라이브러리로, 간단한 HTTP 요청과 이미지 로딩을 빠르게 수행
            - Android SDK에 내장
            - 내장 캐싱 기능 제공 → 같은 요청 반복 시 빠른 응답
            - 이미지 로딩 기능 포함 (ImageLoader, NetworkImageView 사용 가능)
            - 다양한 요청 지원 (StringRequest, JsonRequest, ImageRequest 등)
    - Retrofit 단점
        - 이미지 로딩 기능 없음 (Glide, Picasso 필요)
    - Volley 단점
        - JSON 변환을 직접 수행해야 함
        - 코루틴, RxJava 미지원 (Callback 기반)
        - 요청이 많을 경우 성능 저하 (메모리 사용 증가)
    - 목적에 맞는 추천 라이브러리
        - REST API 요청, JSON 변환 필요: Retrofit
        - 빠른 네트워크 요청, 이미지 로딩: Volley
        - 큰 데이터, 멀티파트 업로드: Retrofit
        - 캐싱이 중요한 경우: Volley
        - RxJava, Coroutine 연동 필요: Retrofit

- Android에서 Jetpack Paging 라이브러리를 사용하는 이유
  - 개요
    - Android에서 대량의 데이터를 효율적으로 로드하고 표시하기 위해 사용
    - 특히 RecyclerView에서 대량의 리스트 데이터를 페이징 방식으로 로드할 때 성능을 최적화 가능
  - 사용이유
    - 대량 데이터 로딩 성능 향상
	  - 한 번에 모든 데이터를 불러오지 않고 부분적으로 가져와서 메모리 사용을 최적화
	  - 네트워크 또는 데이터베이스에서 필요한 데이터만 가져옴
    - 자동 페이징 처리
	  - PagingSource를 사용하여 자동으로 추가 데이터를 요청
	  - 사용자가 스크롤하면 필요한 페이지를 불러오는 방식
    - 메모리 효율성 증가
	  - 필요한 데이터만 로드하고, 오래된 데이터를 자동으로 제거하여 메모리 과부하 방지
    - LiveData, Flow, RxJava 연동 가능
	  - MVVM 패턴과 함께 LiveData, Flow, RxJava를 지원하여 상태 관리를 쉽게 할 수 있음.
    - 네트워크 & 데이터베이스와 통합 가능
	  - 네트워크(API) 데이터 + 로컬(Room DB) 데이터 결합 가능 (RemoteMediator 사용).
	  - 오프라인에서도 캐싱된 데이터를 사용할 수 있도록 지원.

- Android 모바일 앱 개발과 안드로이드 Set-top/OTT/Embedded 앱 개발 차이점
  - 개요
    - 모바일 앱(Android Phone/Tablet App) 개발과 Android Set-top/OTT/Embedded 앱 개발은 동일한 Android 플랫폼을 사용
    - UI/UX, 입력 방식, 성능 최적화, 마켓 배포 방식 등에 차이
  - 결론 (고려해야 될 내용)
    - UI/UX 최적화 필수
	  - TV 앱은 리모컨 중심(DPAD, Focus Navigation) 으로 동작해야 함
	  - 모바일 앱처럼 터치 기반 UI를 그대로 사용하면 안 됨
    - 미디어 재생 & DRM 대응 필요
	  - OTT 앱은 ExoPlayer + Widevine DRM을 활용하여 4K, HDR 스트리밍 최적화 필요
    - 앱 실행 방식 차이
	  - TV 앱은 싱글 앱 모드(한 번에 하나의 앱 실행) → 백그라운드 실행 제한 고려
    - Google Play for TV 요구 사항 준수
	  - android.hardware.touchscreen=false 설정 필수
	  - TV 전용 UI 요구 사항 맞춰야 등록 가능
    - 입력 방식 고려
	  - 모바일: 터치스크린 중심
	  - OTT,Set-top/TV: 리모컨 + 음성 명령 기반의 조작 방식 적용해야 함

- Embedded (OTT, STB etc) 플랫폼에서 DRM(Digital Rights Management)이 중요한 이유
  - DRM이 필수적인 이유
    - 고품질 콘텐츠 보호 (HD, 4K, HDR)
	  - 모바일에서는 저해상도(720p, 1080p) 콘텐츠가 일반적이지만, TV 앱에서는 4K, 8K, HDR 콘텐츠가 기본이기 때문에 해킹 및 불법 복제 위험이 높음.
	  - DRM이 없으면 고화질 콘텐츠가 쉽게 캡처되거나 복제될 수 있음.
    - 콘텐츠 불법 복제 방지
	  - PC나 모바일에서는 화면 녹화(Screen Recording) 기능이 제한되지만, 셋톱박스(TV)는 HDMI를 통해 쉽게 외부 장치로 녹화 가능
	  - DRM을 사용하면 HDMI 출력 자체를 차단할 수 있어 불법 녹화를 방지
    - 콘텐츠 제공업체(Netflix, Disney+ 등)의 필수 요구사항
	  - 넷플릭스, 유튜브, 디즈니+ 같은 서비스는 TV에서 4K 콘텐츠를 제공하기 위해 DRM을 필수적으로 요구
	  - Netflix 4K 콘텐츠를 재생하려면 Widevine L1 또는 PlayReady 같은 DRM 인증이 필수
    - 라이선스 정책 준수
	  - 영화, 스포츠, 방송 콘텐츠는 스튜디오 및 저작권 소유자의 보호 정책을 따라야 함
	  - DRM 없이 콘텐츠를 제공하면 법적 문제 발생 가능
    - OTT 및 VOD 스트리밍 서비스 최적화
	  - OTT 서비스(예: 넷플릭스, 티빙, 웨이브, 쿠팡플레이)에서는 DRM이 적용되지 않으면 고화질 영상 지원이 불가능
	  - DRM이 적용되지 않은 기기에서는 화질 제한(480p, 720p) 발생 가능

- Android TV 앱 개발 시 고려해야 할 사항

Android TV 앱 개발 시 고려해야 할 사항

Android TV 앱을 개발할 때는 모바일 앱과의 차이점을 이해하고, TV 환경에 최적화된 UI/UX 및 기능을 고려해야 합니다. 아래는 주요 고려 사항을 정리한 내용입니다.

1. UI/UX 디자인

✅ 1) D-Pad(방향키) 네비게이션 지원
	•	Android TV에는 터치스크린이 없고, 리모컨으로 조작하기 때문에 방향키(D-Pad) 및 이벤트 처리가 중요함.
	•	focusable, nextFocusUp, nextFocusDown, nextFocusLeft, nextFocusRight 속성을 설정하여 UI 포커스 이동을 제어.
	•	onKeyDown(), onKeyUp(), dispatchKeyEvent()를 활용하여 리모컨 이벤트 처리.

🔹 예제

<Button
    android:id="@+id/btn_play"
    android:focusable="true"
    android:nextFocusRight="@+id/btn_pause"
    android:nextFocusDown="@+id/btn_settings"/>

✅ 2) TV 전용 레이아웃 사용 (Leanback Library)
	•	Android TV는 Leanback 라이브러리를 제공하여 TV UI 최적화된 레이아웃을 쉽게 구현 가능.
	•	BrowseFragment, DetailsFragment, PlaybackFragment 등 제공.

🔹 예제

dependencies {
    implementation 'androidx.leanback:leanback:1.0.0'
}

class MainFragment : BrowseSupportFragment() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setupUI()
    }

    private fun setupUI() {
        title = "Android TV App"
    }
}

✅ 3) TV 해상도 및 안전 영역(Safe Area) 고려
	•	TV는 다양한 해상도를 가짐 (1920x1080, 4K, 8K 등).
	•	UI 요소가 TV 화면 가장자리로 잘리지 않도록 **Safe Area(안전 영역)**를 고려.

🔹 해결 방법
	•	android:layout_margin을 활용하여 UI 여백 설정.
	•	Overscan 처리 (android:padding="16dp").

✅ 4) 큰 화면에 적합한 UI 구성
	•	가독성이 좋은 큰 글씨체 (sp 단위 사용).
	•	선명한 아이콘 및 이미지 (xxxhdpi 이상 지원).
	•	컬러 대비 강조 (어두운 배경 + 밝은 글씨).

🔹 예제

<TextView
    android:text="TV 앱 제목"
    android:textSize="24sp"
    android:textColor="#FFFFFF"/>

2. 입력 및 컨트롤

✅ 1) 리모컨 버튼 지원
	•	D-Pad(방향키), ENTER, BACK, HOME, MENU, PLAY, PAUSE 등 리모컨 이벤트 처리 필요.
	•	KeyEvent.KEYCODE_DPAD_UP, KeyEvent.KEYCODE_MEDIA_PLAY_PAUSE 등을 활용.

🔹 예제

override fun onKeyDown(keyCode: Int, event: KeyEvent?): Boolean {
    return when (keyCode) {
        KeyEvent.KEYCODE_DPAD_LEFT -> {
            moveLeft()
            true
        }
        KeyEvent.KEYCODE_MEDIA_PLAY_PAUSE -> {
            togglePlayPause()
            true
        }
        else -> super.onKeyDown(keyCode, event)
    }
}

✅ 2) 음성 검색 지원 (Google Assistant)
	•	TV에서는 **음성 검색(Voice Input)**이 중요하며, Google Assistant와 통합 가능.
	•	android.speech.RecognizerIntent 사용.

🔹 예제

val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
startActivityForResult(intent, REQUEST_CODE)

3. 미디어 및 스트리밍

✅ 1) ExoPlayer 활용
	•	Android TV는 미디어 소비 중심이므로 ExoPlayer를 활용한 동영상 스트리밍 필수.
	•	HLS, DASH, MP4 등의 포맷 지원.

🔹 예제

dependencies {
    implementation 'com.google.android.exoplayer:exoplayer:2.18.1'
}

val player = ExoPlayer.Builder(context).build()
val mediaItem = MediaItem.fromUri("https://example.com/video.mp4")
player.setMediaItem(mediaItem)
player.prepare()
player.play()

✅ 2) 미디어 리모컨 & 재생 제어
	•	리모컨 Play/Pause 버튼 지원 (MediaSessionCompat 활용).
	•	PlaybackSupportFragment를 사용하여 TV 전용 미디어 UI 제공.

🔹 예제

val mediaSession = MediaSessionCompat(context, "TVApp")
mediaSession.setFlags(MediaSessionCompat.FLAG_HANDLES_MEDIA_BUTTONS)

4. 성능 최적화 및 기타 고려 사항

✅ 1) 성능 최적화
	•	Android TV의 하드웨어 성능이 제한적일 수 있음 (특히 저가형 셋톱박스).
	•	최적화된 이미지 및 비디오 사용 (.webp, 동적 로딩).
	•	네트워크 최적화 → 비디오 스트리밍 시 Adaptive Streaming 활용.

✅ 2) Google Play Store TV 인증
	•	Android TV 앱을 Google Play에 배포하려면 TV 인증 기준 충족 필요.
	•	android.hardware.type.television을 AndroidManifest.xml에 추가.

<uses-feature android:name="android.hardware.type.television"/>
<uses-feature android:name="android.software.leanback" />

	•	Google TV 리모컨 네비게이션 테스트 필수.

✅ 3) 광고 및 인앱 구매 지원
	•	TV 광고 및 인앱 구매 시 Google Ads 또는 Google Play Billing API 활용.

🔹 광고 예제

dependencies {
    implementation 'com.google.android.gms:play-services-ads:20.4.0'
}

MobileAds.initialize(this) {}
val adView = AdView(this)
adView.adUnitId = "YOUR_AD_UNIT_ID"

5. Android TV 앱 개발 체크리스트

항목	고려 사항
UI/UX	D-Pad 네비게이션, 큰 글씨, 안전 영역(Safe Area)
입력 지원	리모컨 버튼, 음성 검색(Google Assistant)
미디어 재생	ExoPlayer, HLS/DASH 스트리밍 지원
성능 최적화	저사양 TV 기기 최적화, 네트워크 최적화
TV 앱 배포	Google Play TV 인증, Leanback 지원

6. 결론

✅ Android TV 앱은 터치 기반이 아닌 리모컨 중심이므로, D-Pad 네비게이션을 최적화하는 것이 중요
✅ ExoPlayer를 활용하여 원활한 미디어 스트리밍 제공
✅ 성능 최적화, 네트워크 최적화, Google Play TV 인증 고려 필수
✅ Leanback 라이브러리를 적극 활용하여 TV 친화적인 UI 구현

➡ Android TV 앱 개발 시 모바일과 다른 점을 충분히 고려하여 최적화하는 것이 핵심!

- Android 앱의 백그라운드 작업을 효율적으로 수행하는 방법
- Android에서 WorkManager와 JobScheduler의 차이점
- Android TV 앱에서 Leanback 라이브러리의 역할
- Android TV 앱 개발 시 D-pad(방향키) 네비게이션을 처리하는 방법
- Android 개발 시 설정했던 HDMI CEC 에 대한 설명
  - HDMI CEC 개요
    - HDMI CEC (Consumer Electronics Control)
    - HDMI(High-Definition Multimedia Interface) 케이블을 통해 연결된 여러 기기를 하나의 리모컨으로 제어할 수 있도록 하는 기능
    - TV 리모컨으로 셋톱박스, 블루레이 플레이어, 사운드바 등을 동시에 컨트롤할 수 있는 기능을 제공
  - HDMI CEC의 주요 기능
    - 한 개의 리모컨으로 여러 기기 제어 가능
	  - 예: TV 리모컨으로 셋톱박스, 블루레이 플레이어, 게임 콘솔(PS5, Xbox) 제어 가능
    - 기기 자동 켜기/끄기 (One Touch Play & Standby)
	  - TV를 켜면 연결된 셋톱박스도 자동으로 켜짐
	  - TV를 끄면 연결된 장치(예: Fire TV, Chromecast)도 자동으로 꺼짐
    - 입력 소스 자동 전환
	  - 예: PlayStation 5를 켜면 TV가 자동으로 HDMI 입력을 PS5로 변경
    - 음량 조절 (Audio System Control)
	  - TV 리모컨으로 사운드바, AV 리시버의 볼륨을 직접 조절 가능
    - 리모컨 신호 전달 (Remote Control Pass-through)
	  - TV 리모컨의 화살표(←,→,↑,↓) 버튼으로 HDMI CEC를 지원하는 셋톱박스나 미디어 플레이어 조작 가능
  - HDMI CEC 작동 방식
	- HDMI CEC는 HDMI 케이블의 13번 핀을 사용하여 기기 간 신호를 주고받음
	- 각 기기에는 CEC Address가 할당되며, 최대 15개의 기기를 연결 가능
	- 기기 간 CEC 명령(예: 전원 On/Off, 입력 전환, 재생/일시정지 등)을 송수신
  - 브랜드별 HDMI CEC 명칭
    - 제조사는 HDMI CEC를 지원하지만, 브랜드마다 다른 명칭을 사용
    - 예시
      - Samsung: Anynet+
      - LG: SimpLink
      - Sony: BRAVIA Sync
      - Hitachi: HDMI-CEC
    - 기능은 동일하지만 브랜드마다 명칭이 다르므로, TV 설정에서 “HDMI CEC” 관련 옵션을 활성화해야 사용 가능
  - Android TV & HDMI CEC
    - Android TV, 셋톱박스, Chromecast, Fire TV 같은 장치에서도 HDMI CEC를 지원한다.
    - Android TV에서 HDMI CEC 활성화 방법 (예: Google TV)
      - 설정(Settings) → 장치 설정(Device Preferences) → HDMI → HDMI CEC 활성화
      - 연결된 기기의 CEC 기능도 활성화해야 함.
    - HDMI CEC를 이용한 Android TV 앱 개발
	  - HDMI CEC를 통해 Android TV 앱이 외부 장치(셋톱박스, 콘솔 등)와 상호 작용할 수 있음.
	  - BroadcastReceiver를 활용하여 CEC 신호 감지 가능.
  - HDMI CEC의 장점과 단점
    - 장점
      - 한 개의 리모컨으로 여러 기기 조작 가능
      - 기기 간 자동 전원 관리 (TV를 켜면 셋톱박스도 자동 켜짐)
      - 입력 소스 자동 전환으로 편리한 사용 가능
      - 추가 설정 없이 HDMI 케이블만 연결하면 동작
    - 단점
      - 브랜드별 호환성 문제 (예: 삼성 TV의 Anynet+가 LG의 SimpLink와 완벽히 호환되지 않을 수 있음)
      - 일부 기기는 CEC 기능이 제한적 (예: 특정 브랜드의 사운드바, HDMI 스위치)
      - 모든 HDMI 포트가 CEC를 지원하지 않을 수도 있음
  - 결론
    - HDMI CEC를 활용하면 셋톱박스/OTT/TV 앱의 전원 및 입력 전환을 자동화할 수 있어 사용자 편의성이 대폭 증가

- Android에서 RecyclerView의 DiffUtil이 중요한 이유
    - 개요
        - 데이터 변경을 효율적으로 반영하는 데 중요한 역할
    - 중요한 이유
        - 성능 최적화
            - RecyclerView는 기본적으로 notifyDataSetChanged()를 호출하면 전체 리스트를 무조건 갱신
            - 이는 불필요한 UI 렌더링과 애니메이션을 유발하여 성능 저하를 초래할 가능성 존재
            - DiffUtil을 사용하면 변경된 항목만 업데이트되므로 불필요한 UI 갱신 방지 가능
        - 부드러운 UI 애니메이션
            - DiffUtil은 변경된 항목을 자동으로 감지하여 notifyItemInserted(), notifyItemRemoved(), notifyItemChanged() 등의 적절한 메서드를 호출
            - 이를 통해 아이템 추가, 삭제, 변경 등의 애니메이션이 자연스럽게 적용
        - 리스트가 큰 경우 성능 차이 극대화
            - 대량의 데이터를 다룰 때 notifyDataSetChanged()를 사용하면 모든 아이템을 새로 바인딩해야 하므로 성능 저하가 발생
            - DiffUtil은 백그라운드 스레드에서 변경 사항을 계산한 후 UI 스레드에서 필요한 부분만 갱신하므로 큰 리스트에서도 성능이 우수
        - 변경 감지를 자동화하여 코드 간결화
            - 기존 방식에서는 리스트가 변경될 때 어떤 항목이 추가, 삭제, 변경되었는지 수동으로 비교하고, 적절한 notify 메서드를 호출해야 했음
            - DiffUtil을 사용하면 areItemsTheSame()과 areContentsTheSame()을 구현하는 것만으로 자동으로 변경 사항을 감지하는 것 가능
        - Paging 라이브러리와의 궁합
            - Android Jetpack의 Paging 라이브러리는 DiffUtil을 기본적으로 활용하여 페이징된 데이터를 효율적으로 업데이트
            - RecyclerView.Adapter가 ListAdapter(DiffUtil 내장)와 함께 사용되면 리스트가 페이징될 때도 부드러운 데이터 변경이 가능
    - DiffUtil을 사용하는 방법
        - DiffUtil.Callback 구현
            ```kotlin
            class MyDiffCallback : DiffUtil.ItemCallback<MyItem>() {
                override fun areItemsTheSame(oldItem: MyItem, newItem: MyItem): Boolean {
                    return oldItem.id == newItem.id // 고유 ID가 같으면 동일한 아이템으로 판단
                }

                override fun areContentsTheSame(oldItem: MyItem, newItem: MyItem): Boolean {
                    return oldItem == newItem // 내용까지 같은 경우만 변경 없음으로 처리
                }
            }
            ```
    - ListAdapter 활용
        - ListAdapter는 RecyclerView.Adapter를 상속받으며 DiffUtil을 자동으로 적용하는 Jetpack 라이브러리의 Adapter
            ```kotlin
            class MyAdapter : ListAdapter<MyItem, MyViewHolder>(MyDiffCallback()) {
                override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
                    val view = LayoutInflater.from(parent.context).inflate(R.layout.item_layout, parent, false)
                    return MyViewHolder(view)
                }

                override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
                    holder.bind(getItem(position)) // getItem() 사용 (ListAdapter에서 제공)
                }
            }
            ```
    - 데이터 변경 시 submitList() 호출
        ```kotlin
        val adapter = MyAdapter()
        recyclerView.adapter = adapter

        // 데이터 변경 시
        adapter.submitList(newList)
        // submitList()는 내부적으로 DiffUtil을 실행하여 변경된 부분만 업데이트
        ```
    - 결론
        - DiffUtil을 사용하면 불필요한 UI 갱신을 최소화하고, 부드러운 애니메이션을 적용하며, 대량의 데이터를 다룰 때 성능 최적화 가능
        - ListAdapter를 활용하면 DiffUtil을 자동 적용할 수 있어 더욱 간편한 코드 작성이 가능
        - RecyclerView에서 DiffUtil을 활용하는 것이 필수적인 이유는 성능, 애니메이션, 코드 유지보수 측면에서 강력한 장점을 제공하기 때문임.


- Android에서 Jetpack DataStore를 사용하는 이유
- Android에서 Jetpack Hilt와 Dagger의 차이점
- Android에서 Shared Preferences보다 Encrypted Shared Preferences가 필요한 이유
- Android에서 CameraX와 기존 Camera API의 차이점
- Android에서 Jetpack WorkManager와 Foreground Service의 차이점
- Android에서 Jetpack Paging을 사용하는 이유
- Android에서 App Bundle과 APK의 차이점
- Android에서 Jetpack Compose와 기존 XML 기반 UI의 차이점
- Android에서 ViewModel과 SavedStateHandle의 차이점
- Android에서 LiveData와 Flow의 차이점
- Android에서 Kotlin Coroutines을 활용하는 방법
- Android에서 Room Database와 SQLite의 차이점
- Android에서 Data Binding을 사용하는 이유
- Android에서 Shared Preferences보다 Encrypted Shared Preferences가 필요한 이유
- Android에서 Jetpack Paging 라이브러리를 사용하는 이유
- Android에서 Dependency Injection을 구현하는 방법
- Android에서 Hilt와 Dagger의 차이점
- Android에서 WorkManager와 JobScheduler의 차이점
- Android에서 CameraX와 기존 Camera API의 차이점
- Android에서 Jetpack Security 라이브러리를 사용하는 이유
- Android에서 MVVM 패턴을 적용하는 방법
- Android에서 Jetpack Navigation Component를 사용하는 이유
- Android에서 Coroutine을 사용한 비동기 처리 방법
- Android에서 MutableLiveData와 StateFlow의 차이점
- Android에서 Jetpack ViewModel을 활용하는 방법
- Android에서 Jetpack Lifecycle Observer의 역할
- Android에서 ViewModelScope와 GlobalScope의 차이점
- Android에서 Coroutines의 Structured Concurrency 개념
- Android에서 BroadcastReceiver의 역할
- Android에서 IntentService와 Foreground Service의 차이점
- Android에서 Jetpack Compose의 State Hoisting 개념
- Android에서 Activity의 생명주기와 Fragment의 생명주기를 비교하시오.
- Android에서 RecyclerView의 ViewHolder 패턴을 사용하는 이유
- Android에서 Retrofit과 Volley의 차이점
- Android에서 FusedLocationProvider API를 사용하는 이유
- Android에서 앱 내 결제를 구현하는 방법
- Android에서 Fingerprint 및 Face ID 인증을 구현하는 방법
- Android에서 Firebase Crashlytics를 활용하는 방법
- Android에서 Jetpack WorkManager를 활용한 백그라운드 작업 수행 방법
- Android에서 AndroidX 라이브러리를 사용하는 이유
- Android에서 ConstraintLayout과 RelativeLayout의 차이점
- Android에서 Jetpack Navigation Component의 Safe Args를 사용하는 이유
- Android에서 ViewBinding과 DataBinding의 차이점
- Android에서 Parcelable과 Serializable의 차이점
- Compound Component 패턴고ㅏ Slot API 설명
- Media Player 자체 내부 로직 설명
- ExoPlayer 내부 구조 설명
- FFMpegPlayer 내부 구조 설명
- Android에서 Splash Screen을 구현하는 올바른 방법
- Android에서 ViewModel을 사용하여 데이터 저장을 최적화하는 방법
- Android에서 Jetpack Paging을 활용하여 대용량 데이터 처리하는 방법
- Android에서 App Bundle과 APK의 차이점
- Android에서 Livedata와 StateFlow 중 어떤 경우에 StateFlow를 선택하는 것이 좋은
- Android에서 Foreground Service를 활용하여 지속적인 작업을 수행하는 방법
- Android에서 Bluetooth LE를 사용하는 방법
- Android에서 Jetpack WorkManager와 Foreground Service의 차이점
- Android에서 Jetpack Paging을 사용하는 이유
- Android에서 UI Thread와 Worker Thread의 차이점
- Android에서 OpenGL ES를 활용하여 2D 및 3D 그래픽을 구현하는 방법
- Android에서 ProGuard를 활용한 코드 난독화 방법
- Android TV 앱 개발 시 Leanback 라이브러리의 역할
- Android TV 앱에서 DPAD 네비게이션을 구현하는 방법
- Android TV에서 VideoView와 ExoPlayer 중 어떤 것을 선택하는 것이 좋은
- Android TV에서 Focusable 요소를 적절하게 배치하는 방법
- Android TV에서 OTT 서비스를 구축할 때 고려해야 할 사항
- Android TV에서 Adaptive Streaming을 활용하는 방법
- Android TV에서 DRM(Digital Rights Management)이 중요한 이유
- Android TV에서 Google Cast API를 활용하는 방법
- Android TV에서 Leanback Showcase를 활용하는 방법
- Android TV에서 KeyEvent를 활용하여 사용자 입력을 처리하는 방법
- Android TV에서 Fire TV와 Android TV의 차이점
- Android TV에서 UI 최적화를 위해 Leanback Components를 활용하는 방법
- Android TV에서 홈 화면을 커스터마이징하는 방법
- Android TV에서 A/B 테스트를 수행하는 방법
- Android TV에서 Voice Input을 적용하는 방법
- Android TV에서 ExoPlayer를 활용한 재생 목록 구현 방법
- Android TV에서 OTT 앱을 개발할 때 UX 디자인 원칙
- Android TV에서 Fire TV Stick에서 동작하는 앱을 개발하는 방법
- Android TV에서 Android TV Input Framework(TIF)의 역할
- Android TV에서 Low Latency Mode를 구현하는 방법
- Android TV에서 In-App Purchase를 구현하는 방법
- Android TV에서 Fragment를 활용하여 Leanback UI를 구성하는 방법
- Android TV에서 Live TV 앱을 개발하는 방법
- Android TV에서 TV Remote Control API를 활용하는 방법
- Android TV에서 Google TV와 기존 Android TV의 차이점
- Android TV에서 HDR 콘텐츠를 재생하는 방법
- Android TV에서 ExoPlayer의 Cache 기능을 활용하는 방법
- Android TV에서 HLS와 DASH 스트리밍의 차이점
- Android TV에서 Real-time Analytics를 적용하는 방법
- Android TV에서 OTT 서비스의 광고 삽입(Ad Insertion) 방법
- Android TV에서 Data Saver Mode를 적용하는 방법
- Android TV에서 UX 성능 최적화를 위한 권장 사항
- Android TV에서 4K와 8K 콘텐츠를 지원하는 방법
- Android TV에서 Google Assistant를 통합하는 방법
- Android TV에서 Low Latency Streaming을 구현하는 방법
- Android TV에서 동적 콘텐츠 추천을 구현하는 방법
- Android TV에서 앱 크기를 최적화하는 방법
- Android TV에서 Firebase Analytics를 활용하는 방법
- Android TV에서 Voice Search 기능을 구현하는 방법
- Android TV에서 ExoPlayer의 Offline Download 기능을 활용하는 방법
- Android TV에서 TV 앱에서의 사용자 경험(UX)을 향상시키는 방법
- Android TV에서 ML 모델을 활용한 추천 시스템을 구축하는 방법
- Android TV에서 Custom Leanback Fragment를 구현하는 방법
- Android TV에서 VOD와 Live Streaming의 차이점
- Android TV에서 Play Billing Library를 활용하여 결제 기능을 구현하는 방법
- Android TV에서 OTT 서비스의 콘텐츠 보안 정책
- Android TV에서 프레임 속도 최적화를 수행하는 방법
- Android TV에서 Dynamic UI Elements를 활용하는 방법
- Android TV에서 Leanback Extensions의 활용 방법
- Android TV에서 Push Notification을 적용하는 방법
- Android에서 Kotlin을 기본 언어로 채택한 이유
- Android의 Application Class는 무엇이며, 어떻게 활용하는
- Android에서 Context의 역할과 종류 (ApplicationContext, ActivityContext 등)의 차이점
- Android에서 onSaveInstanceState()와 ViewModel의 차이점
- Android의 Parcelable과 Serializable의 차이점과 성능 비교
- Kotlin에서 View Binding과 Data Binding의 차이점
- Android의 Activity와 Fragment의 생명주기에서 주요 차이점
- Jetpack Lifecycle Observer의 역할과 활용 방법
- Android에서 ContentProvider의 역할과 사용 사례
- RecyclerView의 ViewHolder 패턴을 사용하는 이유와 성능 최적화 방법
- Android에서 Handler, Looper, MessageQueue의 동작 원리
- Android에서 BroadcastReceiver를 사용할 때 주의해야 할 점
- Android에서 권한 시스템(Permission Request)이 동작하는 방식
- Android의 Jetpack WorkManager와 JobScheduler의 차이점
- Android에서 Jetpack Navigation Component를 사용할 때의 장점
- Android에서 Jetpack DataStore와 SharedPreferences의 차이점
- Android에서 ViewModel과 Repository 패턴을 함께 사용하는 이유
- Android에서 ViewModelStoreOwner의 역할
- Android에서 Room Database와 SQLite의 차이점
- Jetpack Compose와 기존 View 기반 UI의 차이점
- Compose에서 State Hoisting 개념을 설명하고, 언제 사용해야 하는
- Jetpack Compose에서 remember와 rememberSaveable의 차이점
- Jetpack Compose에서 recomposition을 방지하는 방법
- Jetpack Compose의 SnapshotStateList와 일반 List의 차이점
- Jetpack Compose의 Side Effect API (LaunchedEffect, rememberCoroutineScope, SideEffect 등)의 차이점
- Compose에서 LazyColumn과 RecyclerView의 성능 차이
- Compose에서 Modifier의 역할과 주요 Modifier 예제를 설명하시오.
- Jetpack Compose에서 rememberScopedState가 필요한 이유
- Compose에서 Slot API를 활용하는 방법
- Compose에서 UI 성능을 최적화하는 방법
- Compose에서 정적인 상태와 동적인 상태를 관리하는 모범 사례
- Jetpack Compose의 Preview 기능을 활용하는 방법
- Compose에서 BottomSheet와 Dialog를 구현하는 방법
- Jetpack Compose에서 Navigation을 적용하는 방법
- Compose의 LazyColumn에서 성능을 최적화하는 방법
- Compose에서 GestureDetector를 활용한 제스처 처리 방법
- Jetpack Compose에서 Recomposition을 피하는 방법
- Compose에서 ConstraintLayout과 Box를 활용하는 방법
- Compose의 SnapshotFlow는 무엇이며, 언제 사용해야 하는
- Jetpack Compose에서 Skia 렌더링 엔진을 활용한 성능 최적화 기법
- Android Thermal API를 활용하여 배터리 및 성능 최적화를 수행하는 방법
- ExoPlayer에서 DRM(Digital Rights Management) 처리의 고급 기법
- Android 14에서 추가된 보안 기능과 권한 관리 변화
- Android에서 ART(Android Runtime) 최적화를 위한 AOT, JIT, PGO의 차이점
- Android에서 WorkManager의 내부 스케줄링 메커니즘
- Android에서 Jetpack CameraX API를 활용한 맞춤형 카메라 솔루션 구축 방법
- Android의 Foreground Service와 Background Service의 차이점 및 최적화 기법
- Android에서 TensorFlow Lite를 활용하여 ML 모델을 최적화하는 방법
- Android에서 Baseline Profiles을 활용한 앱 성능 개선 방법
- Android에서 Kotlin Coroutines를 사용하는 이유
- Android에서 Paging 3 라이브러리를 사용하는 이유
- Android에서 App Startup Library를 활용하는 방법
- Android에서 UI 렌더링 속도를 최적화하는 방법
- Android에서 OutOfMemory(OOM) 오류를 방지하는 방법
- Android에서 백그라운드 작업을 최적화하는 방법
- Android에서 Jetpack Compose의 Recompositions를 최적화하는 방법
- Android에서 Bitmap 메모리 관리를 최적화하는 방법
- Android에서 Custom View를 만들 때 고려해야 할 사항
- Android에서 CPU 및 메모리 사용량을 최적화하는 방법
- Android에서 StrictMode를 활용한 성능 분석 방법
- Android에서 TraceView와 Perfetto를 활용한 성능 분석 방법
- Android에서 RecyclerView의 DiffUtil을 활용하는 방법
- Android에서 Jetpack Compose의 UI 테스트를 수행하는 방법
- Android에서 Data Binding과 View Binding을 비교하시오.
- Android에서 Prefetching과 Lazy Loading의 차이점
- Android의 ART(Android Runtime) 최적화 방법
- Android에서 Firebase Performance Monitoring을 활용하는 방법
- Android 14에서 추가된 주요 기능과 변경 사항
- Android에서 Jetpack Macrobenchmark를 활용한 성능 측정 방법
- Android에서 Jetpack Compose로 SEO 대응 웹뷰를 구현하는 방법
- Android에서 TensorFlow Lite를 활용한 AI/ML 모델 적용 방법
- Android의 Low Latency Rendering을 구현하는 방법
- Android에서 Jetpack CameraX를 활용하는 방법
- Google Play 정책 변경이 앱 개발에 미치는 영향
- Android에서 WebRTC를 활용한 실시간 영상 통화 구현 방법
- Android에서 Multi-Window를 지원하는 방법
- Android에서 Foldable(접이식) 디바이스 대응 방법
- Android에서 OpenGL ES를 활용한 그래픽 렌더링 최적화 방법
- Android에서 Material 3 디자인 시스템을 적용하는 방법
- Jetpack Compose로 Widget을 만드는 방법
- Android에서 Jetpack Glance를 활용한 위젯 개발 방법
- Android에서 Dynamic Feature Module을 활용하는 방법
- Android에서 Baseline Profiles을 활용한 성능 최적화 방법
- Android 앱에서 Zero Trust Security를 구현하는 방법
- Android에서 AI 기반 추천 시스템을 구현하는 방법
- Android에서 Jetpack Compose로 Instant Apps를 만드는 방법
- Android에서 AI 기반 음성 인식을 활용하는 방법
- Jetpack Compose의 UI 트리 렌더링 방식은 기존 View 시스템과 어떻게 다른
- Jetpack Compose에서 Recomposition이 발생하는 원인
- Compose에서 remember와 rememberSaveable의 차이점
- Jetpack Compose의 Snapshot 시스템이 어떻게 상태를 관리하는
- Compose에서 LazyColumn과 RecyclerView의 내부 동작 차이점
- Jetpack Compose의 상태 관리에서 State Hoisting 패턴을 활용하는 방법
- Compose에서 derivedStateOf와 remember를 활용한 성능 최적화 방법
- Jetpack Compose에서 State와 Event를 분리하는 이유
- Jetpack Compose에서 key()를 사용하여 Recomposition을 최적화하는 방법
- Compose에서 UI 요소가 계속해서 Recomposition되는 문제를 해결하는 방법
- Jetpack Compose의 CompositionLocal이란 무엇이며, 언제 사용하는
- Jetpack Compose에서 custom Modifier를 활용한 성능 최적화 방법
- Compose에서 animation API를 활용할 때 발생할 수 있는 성능 문제와 해결책
- Jetpack Compose에서 rememberCoroutineScope를 사용할 때 주의해야 할 점
- Compose에서 LazyColumn의 성능을 최적화하는 방법
- Compose에서 MutableState와 ImmutableState의 차이점
- Jetpack Compose의 Layout 코드를 최적화하는 방법
- Jetpack Compose에서 동적 리스트 아이템을 효율적으로 렌더링하는 방법
- Jetpack Compose에서 SnapshotStateList와 일반 List의 차이점
- Jetpack Compose에서 ConstraintLayout을 활용하는 이유
- Compose의 Recomposer 내부 구조와 실행 방식
- Jetpack Compose의 produceState는 어떤 경우에 유용한
- Compose에서 Slot API를 활용하여 UI를 구성하는 방법
- Jetpack Compose에서 UI Test를 수행하는 방법과 Best Practice
- Jetpack Compose에서 Theme와 Material 3를 활용하는 방법
- Compose에서 Preview 기능을 활용할 때 발생할 수 있는 문제
- Jetpack Compose에서 SideEffect, DisposableEffect, LaunchedEffect의 차이점
- Jetpack Compose에서 LocalContext와 LocalLifecycleOwner의 활용 방법
- Compose에서 Layout Inspector를 활용하여 UI Debugging을 수행하는 방법
- Jetpack Compose에서 Accessibility를 개선하는 방법
- Jetpack Compose로 마이그레이션할 때 고려해야 할 사항
- Compose에서 XML 기반 View와 혼합하여 사용할 때 성능 문제를 해결하는 방법
- Jetpack Compose에서 ViewModel과 StateFlow를 결합하여 상태를 관리하는 방법
- Compose에서 Flow를 collect하여 UI를 업데이트하는 최적의 방법
- Android 14에서 Jetpack Compose와 관련된 주요 변경 사항
- Jetpack Compose의 새로운 Material 3 디자인 적용 시 고려해야 할 사항
- Jetpack Compose에서 터치 이벤트를 처리하는 방법
- Jetpack Compose에서 다크 모드를 지원하는 방법
- Compose에서 WebView를 사용할 때 발생하는 문제와 해결책
- Jetpack Compose에서 Edge-to-Edge UI를 구현하는 방법
- Compose에서 폴더블(Foldable) 디바이스를 대응하는 방법
- Jetpack Compose에서 Navigation Component를 활용하는 방법
- Compose에서 비동기 데이터 로딩 중 UI를 최적화하는 방법
- Jetpack Compose에서 ConstraintLayout을 사용할 때 주의할 점
- Compose에서 WorkManager와 Coroutines을 함께 활용하는 방법
- Jetpack Compose에서 ML Kit을 활용한 AI 기능을 추가하는 방법
- Compose의 Glance를 활용하여 Widget을 구현하는 방법
- Jetpack Compose에서 Jetpack CameraX를 활용하는 방법
- Jetpack Compose에서 Biometric API를 활용하는 방법
- Compose에서 Jetpack Hilt와 함께 DI를 활용하는 방법
- Android의 Binder IPC 메커니즘에 대해 설명해주세요.
- ListView와 RecylerView에 대해서 설명해보세요
- ListView는 재활용이 불가능할까요?
- Android의 View 렌더링 과정과 성능 최적화 방법을 설명해주세요.
- Android의 ProGuard와 R8의 차이점은 무엇인가
- Android의 ANR(Application Not Responding) 원인과 해결 방법은 무엇인가
- Android의 Jetpack Navigation Component 사용 경험을 설명해주세요.
- AOSP의 SELinux 정책과 보안 메커니즘에 대해 설명해주세요.
- AIDL에 대해 말씀해주세요
- HIDL에 대해 설명
- AOSP의 HAL(Hardware Abstraction Layer)에 대해 설명해주세요.
- AOSP의 시스템 서비스(SystemService) 추가 경험이 있다면 설명해주세요.
- Android의 RenderThread와 UI Thread의 상호작용을 설명해주세요.
- Android의 WindowManager와 SurfaceFlinger의 역할은 무엇인가
- Android의 ART(Android Runtime)와 Dalvik의 차이점은 무엇인가
- AOSP의 init 프로세스와 서비스 관리 방법을 설명해주세요.
- AOSP의 Binder 드라이버와 IPC 메커니즘에 대해 설명해주세요.
- Android MVI orbit 설명
- Java의 JVM, JRE, JDK의 차이점은?
- Java의 Garbage Collection 방식에는 어떤 것들이 있는가?
- Java에서 Multi-threading을 구현하는 방법은?
- Java에서 HashMap과 ConcurrentHashMap의 차이점은?
- Java에서 Stream API를 활용하는 방법은?
- Java에서 Reflection을 사용할 때 주의해야 할 점은?
- Java에서 Lombok 라이브러리를 사용할 때 장점과 단점은?
- Java에서 CompletableFuture를 활용하는 방법은?
- Java에서 메모리 누수를 방지하는 방법은?
- Java에서 Java Flight Recorder(JFR)를 사용하는 이유는?
- Java의 Optional 클래스를 사용하는 이유는?
- Java에서 Thread와 Executor의 차이점은?
- Java에서 WebSockets을 구현하는 방법은?
- Java에서 메모리 정리(Garbage Collection) 최적화 방법은?
- Java에서 Functional Interface를 활용하는 방법은?
- Java의 JVM, JRE, JDK의 차이점은?
- Java에서 equals()와 ==의 차이점은?
- Java에서 hashCode()와 equals()의 관계는?
- Java에서 String과 StringBuilder, StringBuffer의 차이점은?
- Java의 클래스 로딩 과정(Class Loading Process)은 어떻게 진행되는가?
- Java의 다형성(Polymorphism)이란 무엇이며, 어떻게 구현되는가?
- Java에서 오버로딩(Overloading)과 오버라이딩(Overriding)의 차이점은?
- Java에서 인터페이스(Interface)와 추상 클래스(Abstract Class)의 차이점은?
- Java에서 super 키워드와 this 키워드의 차이점은?
- Java에서 메모리 관리(Memory Management)와 가비지 컬렉션(Garbage Collection)은 어떻게 이루어지는가?
- Java에서 final 키워드를 사용할 수 있는 곳과 그 의미는?
- Java에서 static 키워드가 가지는 의미는?
- Java에서 객체를 clone()할 때 발생할 수 있는 문제는?
- Java에서 Serializable 인터페이스의 역할은?
- Java에서 transient 키워드를 사용하는 이유는?
- Java에서 try-with-resources를 사용하는 이유는?
- Java의 Optional 클래스를 활용하는 방법은?
- Java에서 varargs(가변 인자)를 사용할 때 주의할 점은?
- Java에서 enum을 활용하는 방법과 장점은?
- Java에서 default 메서드를 인터페이스에서 지원하는 이유는?
- Java에서 record 키워드를 사용하면 얻을 수 있는 장점은?
- Java의 Functional Interface와 Lambda Expression의 관계는?
- Java의 Stream API를 활용하는 방법은?
- Java의 Comparator와 Comparable 인터페이스의 차이점은?
- Java에서 switch 문을 개선한 switch expressions의 특징은?
- Java에서 synchronized 키워드를 사용할 때 주의할 점은?
- Java에서 ThreadLocal이란 무엇이며, 언제 사용하는가?
- Java에서 volatile 키워드를 사용하는 이유는?
- Java에서 AtomicInteger와 synchronized의 차이점은?
- Java에서 Semaphore, CountDownLatch, CyclicBarrier의 차이점은?
- Java의 ArrayList와 LinkedList의 차이점은?
- Java의 HashMap과 TreeMap의 차이점은?
- Java에서 ConcurrentHashMap과 Collections.synchronizedMap()의 차이점은?
- Java에서 WeakHashMap을 사용하는 이유는?
- Java에서 LinkedHashMap을 활용하여 캐시(Cache)를 구현하는 방법은?
- Java에서 PriorityQueue의 동작 방식은?
- Java에서 Deque와 Queue의 차이점은?
- Java에서 ArrayDeque와 LinkedList의 차이점은?
- Java의 HashSet과 TreeSet의 차이점은?
- Java에서 Iterator와 ListIterator의 차이점은?
- Java에서 CopyOnWriteArrayList의 사용 사례는?
- Java에서 EnumMap을 사용하는 이유는?
- Java에서 BlockingQueue의 역할과 사용 예제는?
- Java에서 Stream API와 for-each 루프의 차이점은?
- Java에서 Collectors.toMap()을 사용할 때 발생할 수 있는 문제는?
- Java에서 Spliterator의 역할과 활용 방법은?
- Java에서 Unmodifiable Collection을 생성하는 방법은?
- Java에서 Arrays.asList()를 사용할 때 주의할 점은?
- Java에서 Immutable Collections을 생성하는 방법은?
- Java에서 Map.computeIfAbsent()의 활용 사례는?
- Java에서 ConcurrentLinkedQueue와 LinkedBlockingQueue의 차이점은?
- Java의 ForkJoinPool을 활용한 병렬 처리는 어떻게 구현하는가?
- Java에서 NavigableMap과 NavigableSet의 차이점은?
- Java에서 TreeMap을 활용하여 정렬된 데이터를 관리하는 방법은?
- Java에서 PriorityBlockingQueue의 동작 원리는?
- Java에서 Thread-Safe Collection의 대표적인 구현체는 무엇인가?
- Java에서 Stream API의 parallelStream()을 사용할 때 주의해야 할 점은?
- Java에서 FlatMap()을 활용하는 방법은?
- Java에서 Collectors.groupingBy()를 활용한 데이터 분류 방법은?
- Java의 Stream.reduce()를 활용한 데이터 집계 방법은?
- Java에서 ExecutorService를 활용한 스레드 풀(Thread Pool) 구현 방법은?
- Java에서 Future와 CompletableFuture의 차이점은?
- Java에서 ScheduledExecutorService의 역할은?
- Java에서 ReentrantLock과 synchronized의 차이점은?
- Java에서 ForkJoinTask와 RecursiveTask를 활용한 병렬 처리는 어떻게 구현하는가?
- Java에서 Phaser와 CyclicBarrier의 차이점은?
- Java에서 Callable과 Runnable의 차이점은?
- Java에서 AsynchronousFileChannel의 역할은?
- Java에서 Non-blocking I/O(NIO)와 Blocking I/O(BIO)의 차이점은?
- Java에서 Netty를 활용한 네트워크 프로그래밍의 장점은?
- Java에서 Zero-Copy 기법을 활용하여 성능을 최적화하는 방법은?
- Java에서 WebSockets을 활용한 실시간 통신 구현 방법은?
- Java에서 gRPC와 REST API의 차이점은?
- Java에서 HttpClient와 URLConnection의 차이점은?
- Java에서 Thread Dump를 분석하는 방법은?
- Java에서 Deadlock이 발생하는 원인과 해결 방법은?
- Java에서 Thread.sleep()과 Object.wait()의 차이점은?
- Java에서 ScheduledThreadPoolExecutor의 활용 방법은?
- Java에서 ThreadLocal의 메모리 누수 문제를 방지하는 방법은?
- Java에서 CompletableFuture.supplyAsync()를 활용하는 방법은?
- Java의 Virtual Threads(프로젝트 Loom) 개념과 기존 Thread와의 차이점은?
- Java에서 GraalVM을 활용한 AOT(Ahead-of-Time) 컴파일 성능 최적화 방법은?
- Java에서 Panama Project를 활용하여 네이티브 코드와 상호작용하는 방법은?
- Java의 Structured Concurrency 개념과 기존 Thread 관리 방식과의 차이점은?
- Java에서 CDS(Class Data Sharing)를 활용하여 JVM 성능을 최적화하는 방법은?
- Kotlin과 Java의 주요 차이점은?
- Kotlin에서 var와 val의 차이점은?
- Kotlin에서 lateinit과 lazy의 차이점은?
- Kotlin에서 data class를 사용하는 이유는?
- Kotlin의 sealed class와 enum class의 차이점은?
- Kotlin에서 companion object와 object의 차이점은?
- Kotlin에서 open 키워드를 사용하는 이유는?
- Kotlin에서 inline 함수의 장점과 단점은?
- Kotlin에서 reified 키워드를 사용하는 이유는?
- Kotlin에서 extension function을 활용하는 방법은?
- Kotlin에서 operator overloading을 구현하는 방법은?
- Kotlin에서 delegation을 활용하는 방법은?
- Kotlin에서 typealias를 사용하는 이유는?
- Kotlin에서 Any, Unit, Nothing 타입의 차이점은?
- Kotlin에서 when 표현식과 switch 문법의 차이점은?
- Kotlin에서 vararg를 활용한 가변 인자 함수는 어떻게 동작하는가?
- Kotlin에서 generic을 사용할 때 out과 in 키워드의 차이점은?
- Kotlin에서 copy() 메서드를 사용하는 이유는?
- Kotlin에서 apply, let, run, also, with의 차이점은?
- Kotlin에서 object expression과 object declaration의 차이점은?
- Kotlin에서 sealed interface를 활용하는 방법은?
- Kotlin에서 break, continue, return의 차이점은?
- Kotlin의 context receivers 기능을 설명하시오.
- Kotlin에서 nullable 타입과 !! 연산자를 사용할 때 주의할 점은?
- Kotlin에서 @JvmStatic, @JvmOverloads, @JvmField 어노테이션의 역할은?
- Kotlin에서 is 키워드와 as 키워드의 차이점은?
- Kotlin에서 Collection과 Sequence의 차이점은?
- Kotlin에서 vararg를 사용한 함수 호출 시 배열을 전달하는 방법은?
- Kotlin에서 Enum class를 활용한 안전한 상태 관리는 어떻게 하는가?
- Kotlin에서 builder pattern을 활용하여 객체를 생성하는 방법은?
- Kotlin에서 inline class의 개념과 사용 예제는?
- Kotlin에서 suspend 함수와 일반 함수의 차이점은?
- Kotlin에서 context receivers가 도입된 이유는?
- Kotlin에서 JvmInline을 사용하는 이유는?
- Kotlin에서 contract API가 무엇이며, 어떻게 활용하는가?
- Kotlin에서 SAM(Single Abstract Method) Conversion이란 무엇인가?
- Kotlin에서 builder pattern을 DSL로 구현하는 방법은?
- Kotlin에서 type inference의 원리와 활용 방법은?
- Kotlin에서 spread operator(*)의 활용 방법은?
- Kotlin에서 tail recursion 최적화 기법을 설명하시오.
- Kotlin에서 Map을 destructuring하여 사용하는 방법은?
- Kotlin에서 bitwise operations을 수행하는 방법은?
- Kotlin에서 dynamic 키워드를 사용할 수 없는 이유는?
- Kotlin에서 KProperty와 Reflection API를 활용하는 방법은?
- Kotlin에서 @DslMarker 어노테이션을 사용하는 이유는?
- Kotlin에서 LazyThreadSafetyMode의 옵션들과 차이점은?
- Kotlin에서 CoroutineContext와 Job의 관계는?
- Kotlin에서 JvmStatic과 JvmOverloads를 활용하는 방법은?
- Kotlin에서 try-catch와 runCatching의 차이점은?
- Kotlin에서 @OptIn 어노테이션을 사용하는 이유는?
- Kotlin Coroutines의 핵심 개념은?
- suspend 함수란 무엇이며, 일반 함수와의 차이점은?
- launch와 async의 차이점은?
- GlobalScope를 사용하면 안 되는 이유는?
- coroutineScope와 supervisorScope의 차이점은?
- CoroutineContext의 구성 요소는?
- withContext()와 async-await의 차이점은?
- Dispatchers.IO, Dispatchers.Main, Dispatchers.Default의 차이점은?
- runBlocking을 사용하는 것이 위험한 이유는?
- Kotlin Coroutines에서 Structured Concurrency란?
- CoroutineExceptionHandler의 역할은?
- Job과 SupervisorJob의 차이점은?
- Flow와 Channel의 차이점은?
- StateFlow와 SharedFlow의 차이점은?
- Flow에서 buffer()와 conflate()의 차이점은?
- flowOn()을 사용할 때 발생할 수 있는 문제는?
- Cold Flow와 Hot Flow의 차이점은?
- MutableSharedFlow에서 replay 옵션을 설정하는 이유는?
- StateFlow에서 초기 값을 설정해야 하는 이유는?
- yield() 함수의 역할은?
- cancel()을 호출한 후에도 코루틴이 종료되지 않는 이유는?
- ensureActive() 함수의 역할은?
- select {} 블록을 활용하여 여러 채널을 동시에 처리하는 방법은?
- produce {}와 consumeEach {}의 차이점은?
- Mutex와 Atomic을 활용한 동시성 문제 해결 방법은?
- sequence {}와 Flow {}의 차이점은?
- combine() 연산자를 활용한 데이터 스트림 결합 방법은?
- retry()와 catch() 연산자의 차이점은?
- debounce()와 throttleFirst()의 차이점은?
- Kotlin Coroutines에서 테스트를 수행하는 방법은?
- ViewModelScope를 활용하여 네트워크 요청을 수행하는 방법은?
- Retrofit과 Coroutines을 함께 사용할 때의 장점은?
- Room Database에서 Coroutines을 사용하는 이유는?
- Android에서 LiveData와 StateFlow를 함께 사용할 때의 고려사항은?
- WorkManager와 Coroutines을 함께 사용할 때의 주의점은?
- Android에서 코루틴을 활용한 백그라운드 작업 최적화 방법은?
- Paging 3 라이브러리에서 Flow를 활용하는 방법은?
- Android에서 네트워크 요청 중간에 코루틴을 취소하는 방법은?
- 코루틴이 과도하게 생성되었을 때 발생할 수 있는 문제는?
- Kotlin에서 Coroutines을 활용한 효율적인 병렬 처리 방법은?
- Kotlin에서 Job과 Deferred를 활용한 작업 스케줄링 방법은?
- Android에서 Flow를 활용한 실시간 데이터 처리 방법은?
- 코루틴을 활용한 이벤트 기반 아키텍처 설계 방법은?
- Coroutines에서 CoroutineScope를 올바르게 관리하는 방법은?
- Coroutines에서 Flow.collectLatest()를 활용한 최신 데이터 유지 방법은?
- Kotlin에서 StateFlow와 LiveData를 변환하는 방법은?
- Android에서 Jetpack Compose와 Coroutines을 함께 사용하는 방법은?
- Kotlin Coroutines을 활용한 Custom Thread Pool 구성 방법은?
- 코루틴에서 예외 처리를 효과적으로 수행하는 방법은?
- Kotlin Coroutines과 Kotlin Multiplatform(KMP)에서의 활용 방법은?
- Kotlin의 바이트코드 최적화 과정을 설명하시오.
- Kotlin의 escape analysis가 어떻게 동작하는지 설명하시오.
- Kotlin의 inline function이 내부적으로 어떻게 동작하는가?
- Kotlin에서 tail recursion이 동작하는 방식을 설명하시오.
- Kotlin의 delegate 패턴을 사용하는 이유와 성능적 이점은?
- Kotlin의 스마트 캐스팅(Smart Casting)이 내부적으로 어떻게 처리되는가?
- Kotlin의 reified 키워드가 동작하는 원리를 설명하시오.
- Kotlin의 sealed interface와 sealed class의 차이점 및 내부 구현 차이는?
- Kotlin의 default parameter와 Java의 method overloading 차이점은?
- Kotlin에서 String interpolation이 내부적으로 어떻게 최적화되는가?
- Kotlin의 메모리 관리 방식과 Java의 GC(Garbage Collector) 차이점은?
- Kotlin에서 가변 객체(mutable object)의 성능 최적화 방법은?
- Kotlin에서 immutable 객체를 구현하는 방법과 효과적인 활용 사례는?
- Kotlin에서 객체 풀(Object Pool)을 활용하여 성능을 개선하는 방법은?
- Kotlin에서 람다(Lambda)의 capture 비용을 줄이는 방법은?
- Kotlin에서 JVM의 Code Cache를 활용한 최적화 기법은?
- Kotlin에서 value class(구 inline class)를 활용할 때 성능적인 장점은?
- Kotlin의 동적 바인딩과 정적 바인딩의 차이점 및 실행 성능 비교는?
- Kotlin에서 reflection을 사용할 때 발생하는 오버헤드는 어떻게 줄일 수 있는가?
- Kotlin에서 Lazy initialization을 성능적으로 최적화하는 방법은?
- Kotlin에서 Coroutines과 Java의 Thread Pool의 차이점은?
- Kotlin의 Coroutines에서 Structured Concurrency 개념이 중요한 이유는?
- Kotlin의 Coroutines에서 GlobalScope 사용이 위험한 이유는?
- Kotlin Coroutines에서 Dispatchers.IO와 Dispatchers.Default의 내부 구현 차이는?
- Kotlin에서 Job과 SupervisorJob의 차이점과 예제 코드를 설명하시오.
- Kotlin에서 Flow의 Backpressure(역압) 문제를 해결하는 방법은?
- Kotlin의 StateFlow와 SharedFlow의 차이점과 실전 활용법은?
- Kotlin에서 채널(Channel)과 Flow의 차이점은?
- Kotlin에서 Coroutines의 동시성 제어를 위해 Mutex와 Semaphore를 어떻게 활용하는가?
- Kotlin에서 Thread Safety를 보장하는 방법은?
- Kotlin의 Atomic 변수를 활용한 동시성 제어 방법은?
- Kotlin에서 코루틴을 활용하여 Concurrent Processing을 구현하는 방법은?
- Kotlin에서 runBlocking이 주는 성능적 부담과 이를 피하는 방법은?
- Kotlin Coroutines에서 launch와 async의 차이점과 내부 동작 원리는?
- Kotlin의 yield() 함수가 비동기 작업에서 어떤 역할을 하는가?
- Kotlin에서 CoroutineScope의 메모리 누수를 방지하는 방법은?
- Kotlin의 select {} 문법을 활용한 비동기 작업 최적화 방법은?
- Kotlin에서 CoroutineExceptionHandler가 실행되는 조건은?
- Kotlin에서 ensureActive()의 역할과 사용 예제는?
- Kotlin에서 coroutineScope와 supervisorScope의 내부적인 동작 차이는?
- Kotlin에서 다중 모듈 프로젝트를 효율적으로 구성하는 방법은?
- Kotlin에서 Dependency Injection(DI)을 적용할 때 Koin과 Hilt의 차이점은?
- Kotlin에서 JUnit5와 MockK를 활용한 단위 테스트 전략은?
- Kotlin에서 비동기 네트워크 요청을 최적화하는 방법은?
- Kotlin의 Coroutines과 RxJava의 차이점 및 선택 기준은?
- Kotlin에서 Dagger-Hilt와 Koin을 함께 사용할 때의 장점과 단점은?
- Kotlin의 Multiplatform 프로젝트에서 Coroutines을 활용하는 방법은?
- Kotlin에서 Jetpack Compose와 Coroutines을 함께 사용할 때 고려해야 할 점은?
- Kotlin에서 GraphQL API를 활용할 때 최적화하는 방법은?
- Kotlin에서 Room Database와 Coroutines을 함께 사용할 때의 주의점은?
- Kotlin에서 Paging 3 라이브러리를 활용한 비동기 데이터 로딩 방식은?
- Kotlin의 KMM(Kotlin Multiplatform Mobile)에서 네트워크 요청을 처리하는 방법은?
- Kotlin에서 DI 프레임워크 없이 Factory 패턴을 활용한 객체 관리는 어떻게 하는가?
- Kotlin에서 Retrofit과 Coroutines을 함께 사용할 때의 베스트 프랙티스는?
- Kotlin에서 JSON Parsing을 최적화하는 방법은?
- Kotlin에서 Domain Layer와 Data Layer를 분리할 때의 원칙은?
- Kotlin의 Anvil을 활용한 DI 성능 최적화 방법은?
- Kotlin에서 ViewModelScope를 사용할 때 발생할 수 있는 문제는?
- Kotlin에서 Singleton 객체를 Thread-Safe하게 생성하는 방법은?
- Kotlin의 Anvil을 사용한 Dependency Injection의 성능 최적화 방법은?
- Kotlin 1.9에서 새롭게 추가된 기능과 성능 최적화 요소는?
- Kotlin의 Compiler Plugin을 활용하여 코드 최적화를 수행하는 방법은?
- Kotlin에서 JIT과 AOT의 차이점과 각각의 활용 사례는?
- Kotlin에서 JetBrains의 Ktor를 활용한 비동기 웹 서버 구축 방법은?
- Kotlin에서 새로운 Concurrent Garbage Collector의 장점과 활용 방안은?
- Kotlin의 최신 정적 분석 도구(Detekt, Ktlint)를 활용하는 방법은?
- Kotlin에서 Memory Leak을 방지하는 패턴은?
- Kotlin의 Context Receivers 기능이 필요한 이유는?
- Kotlin에서 Native Image를 활용한 성능 최적화 방법은?
- Kotlin에서 Compiler Intrinsics을 활용한 성능 최적화 기법은?
- Kotlin과 Java의 주요 차이점은 무엇인가?
- CoroutineScope를 올바르게 관리하는 방법은?
- Coroutine의 Structured Concurrency란 무엇이며, 왜 중요한가?
- GlobalScope를 사용하면 안 되는 이유는?
- launch와 async의 차이점은?
- runBlocking을 사용할 때의 문제점은?
- withContext()와 launch의 차이점은?
- CoroutineContext의 주요 요소(Job, Dispatcher, ExceptionHandler 등)를 설명하시오.
- Flow와 LiveData의 차이점은?
- SharedFlow와 StateFlow의 차이점은?
- suspend function 내부에서 try-catch를 올바르게 사용하는 방법은?
- Coroutine의 Dispatchers.Default, IO, Main의 차이점은?
- supervisorScope와 coroutineScope의 차이점은?
- Kotlin Coroutine에서 cancel()을 호출했을 때 실행 흐름은?
- Job과 SupervisorJob의 차이점은?
- Flow에서 buffer()와 conflate()의 차이점은?
- Coroutine에서 Mutex와 Semaphore의 차이점은?
- CoroutineExceptionHandler가 실행되는 경우는?
- Android에서 Coroutine을 활용한 네트워크 요청 최적화 방법은?
- Jetpack WorkManager와 Coroutines을 함께 사용할 때의 주의점은?
- MVVM과 MVI의 차이점은?
- Clean Architecture를 Android 프로젝트에 적용하는 방법은?
- DI(Dependency Injection)에서 Hilt와 Koin의 차이점은?
- Kotlin에서 컴파일 시 생성되는 바이트코드는 어떻게 최적화되는가?
- Kotlin의 escape analysis와 stack allocation이 성능에 미치는 영향은?
- Kotlin에서 smart casting이 내부적으로 어떻게 동작하는가?
- Kotlin의 inline class(value class)와 일반 class의 차이점 및 성능 비교는?
- Kotlin의 companion object는 언제 메모리에 로드되는가?
- Kotlin에서 data class의 copy() 메서드는 어떻게 동작하며, deep copy를 구현하는 방법은?
- Kotlin에서 typealias의 내부적인 동작 방식과 활용 사례는?
- Kotlin의 sealed interface와 sealed class의 차이점 및 내부 구현 방식은?
- Kotlin의 contract API는 무엇이며, 최적화에 어떻게 기여하는가?
- Kotlin에서 reflection이 성능에 미치는 영향과 이를 줄이는 방법은?
- Kotlin에서 inline function이 성능을 개선하는 이유는?
- Kotlin에서 reified 키워드가 컴파일러 최적화에 미치는 영향은?
- Kotlin의 null-safety가 JVM에서 어떻게 구현되는가?
- Kotlin의 default arguments는 Java와 어떻게 다르게 처리되는가?
- Kotlin에서 lazy initialization의 내부 동작 방식과 성능 고려 사항은?
- Kotlin에서 tail recursion 최적화(TCO)가 적용되지 않는 경우는?
- Kotlin에서 synchronized 블록과 volatile 키워드의 차이점은?
- Kotlin에서 companion object가 싱글톤처럼 동작하는 이유는?
- Kotlin에서 함수형 프로그래밍 패러다임을 적용할 때 고려해야 할 사항은?
- Kotlin에서 inline class를 활용한 메모리 최적화 기법은?
- Kotlin에서 JVM과 Native 컴파일 시 최적화 차이점은?
- Kotlin에서 Serialization을 최적화하는 방법은?
- Kotlin에서 suspend function이 컴파일될 때 생성되는 내부 코드 구조는?
- Kotlin에서 코루틴을 사용한 비동기 네트워크 요청 시 성능 최적화 방법은?
- Kotlin의 CoroutineContext 내부 구조와 Job, Dispatcher, ExceptionHandler의 역할은?
- Kotlin에서 CoroutineExceptionHandler를 활용한 예외 처리 방법은?
- Kotlin에서 collectLatest()와 collect()의 차이점은?
- Kotlin의 StateFlow와 SharedFlow의 차이점 및 활용 방법은?
- Kotlin에서 Immutable Data Structure를 활용한 성능 최적화 방법은?
- Kotlin의 Compiler Intrinsics을 활용한 성능 최적화 기법은?
- 다이나믹 아일랜드 구현 방법 및 실시간 업데이트 처리 방법
- Java의 메모리 관리 방식에 대해 설명해주세요. (GC, Heap, Stack)
- Java 8에서 추가된 기능들(Lambda, Stream API 등)에 대해 설명해주세요.
- OOP의 4대 원칙과 SOLID 원칙에 대해 설명해주세요.
- 멀티스레딩과 동시성 처리에 대해 설명해주세요. (Thread, ExecutorService, Synchronized, Volatile 등)
- Java의 컬렉션 프레임워크에 대해 설명해주세요. (List, Set, Map 등)
- 예외 처리의 종류와 차이점을 설명해주세요. (Checked Exception vs Unchecked Exception)
- Kotlin의 주요 특징과 Java와의 차이점은 무엇인가요?
- Null Safety를 어떻게 구현했는지 설명해주세요.
- Kotlin의 Coroutine과 Java의 Thread의 차이점은 무엇인가요?
- Kotlin에서의 확장 함수(Extension Function)에 대해 설명해주세요.
- Data Class의 장점과 사용 사례를 설명해주세요.
- Coroutine이란 무엇이고, 어떤 상황에서 사용하나요?
- Coroutine의 Dispatcher 종류와 각각의 사용 사례를 설명해주세요.
- Coroutine의 Cancellation과 Exception Handling에 대해 설명해주세요.
- Coroutine과 RxJava의 차이점은 무엇인가요?
- Coroutine을 사용해본 프로젝트에서의 경험을 공유해주세요.
- Android의 생명주기(Lifecycle)에 대해 설명해주세요.
- Activity와 Fragment의 차이점은 무엇인가요?
- ViewModel과 LiveData의 역할과 장점은 무엇인가요?
- Android에서의 메모리 관리와 LeakCanary 사용 경험에 대해 설명해주세요.
- Jetpack Compose를 사용해본 경험이 있다면 설명해주세요.
- Android에서의 DI(Dependency Injection) 사용 경험을 공유해주세요. (Dagger, Hilt 등)
- Android의 백그라운드 작업 처리 방법을 설명해주세요. (WorkManager, JobScheduler 등)
- AOSP 빌드 과정에 대해 설명해주세요.
- Android 시스템의 주요 컴포넌트에 대해 설명해주세요. (Binder, Zygote, SystemServer 등)
- 커스텀 ROM을 제작한 경험이 있다면 설명해주세요.
- Java의 Garbage Collection 알고리즘에 대해 설명해주세요. (CMS, G1, ZGC 등)
- Java의 ClassLoader와 동적 로딩에 대해 설명해주세요.
- Java의 Reflection API 사용 사례와 주의점은 무엇인가요?
- Java의 Concurrent Collections(ConcurrentHashMap, CopyOnWriteArrayList 등)에 대해 설명해주세요.
- Java의 Functional Interface와 Lambda 표현식의 내부 동작 원리를 설명해주세요.
- 다이나믹 프록시 정의와 사용이유 그리고 사용 방법
- Kotlin의 Inline 함수와 Reified 타입에 대해 설명해주세요.
- Kotlin의 Sealed Class와 Enum Class의 차이점은 무엇인가요?
- Kotlin의 Delegated Properties 사용 사례를 설명해주세요.
- Kotlin의 Coroutine 내부 동작 원리(Continuation, Dispatcher 등)에 대해 설명해주세요.
- Coroutine의 Structured Concurrency 개념에 대해 설명해주세요.
- Coroutine의 Flow와 Channel의 차이점은 무엇인가요?
- Coroutine의 SupervisorJob과 일반 Job의 차이점은 무엇인가요?
- Coroutine의 Cancellation과 Exception Handling을 어떻게 구현하셨나요?
- Coroutine의 테스트 전략을 설명해주세요. (TestCoroutineDispatcher 등)
- Java의 JIT(Just-In-Time) 컴파일러와 AOT(Ahead-Of-Time) 컴파일러의 차이점은 무엇인가요?
- Java의 VarHandle과 Atomic 클래스의 사용 사례를 설명해주세요.
- Java의 Module System(JPMS)에 대해 설명해주세요.
- Java의 Bytecode 조작 라이브러리(ASM, ByteBuddy 등) 사용 경험이 있다면 설명해주세요.
- Kotlin의 Type Alias와 Inline Class의 차이점은 무엇인가요?
- Kotlin의 Contracts API 사용 사례를 설명해주세요.
- Kotlin의 Multiplatform 프로젝트 경험이 있다면 설명해주세요.
- Coroutine의 Flow에서의 Backpressure 처리 방법을 설명해주세요.
- Coroutine의 StateFlow와 SharedFlow의 차이점은 무엇인가요?
- Coroutine의 Channel과 Actor의 차이점은 무엇인가요?
- Jetpack Compose에서 State Hoisting의 개념을 설명하시오.
- Kotlin에서 inline, noinline, crossinline 키워드의 차이점은?
- Kotlin에서 suspend 함수와 CoroutineScope의 차이점은?
- Kotlin의 Flow와 LiveData의 차이점은?
- Kotlin에서 Channel과 SharedFlow의 차이점은?
- Jetpack Compose에서 remember와 rememberSaveable의 차이점은?
- Jetpack Compose에서 CompositionLocal을 사용하는 이유는?
- Jetpack Compose에서 LazyColumn과 RecyclerView의 차이점은?
- Jetpack Compose에서 Modifier의 역할과 best practice는?
- Android에서 WorkManager와 AlarmManager의 차이점은?
- Android에서 DataStore와 SharedPreferences의 차이점은?
- Android에서 Scoped Storage란 무엇이며, 기존 저장 방식과 차이점은?
- Android에서 ViewBinding과 DataBinding의 차이점은?
- Android에서 CameraX를 사용할 때의 장점은?
- Android에서 Activity Result API를 활용하는 방법은?
- Android에서 LifecycleOwner와 ViewModel의 관계를 설명하시오.
- Android에서 Hilt와 Koin의 차이점은?
- Android에서 Firebase Cloud Messaging(FCM)과 OneSignal의 차이점은?
- Android에서 ExoPlayer와 MediaPlayer의 차이점은?
- Android에서 Jetpack Paging 3 라이브러리의 개념과 사용법은?
- Android에서 Service와 JobIntentService의 차이점은?
- Jetpack Compose에서 recomposition이 발생하는 조건은?
- Jetpack Compose에서 remember와 rememberSaveable의 차이점은?
- Kotlin Coroutines에서 Structured Concurrency가 왜 중요한가?
- Kotlin에서 suspend function이 호출되는 스레드는 어떻게 결정되는가?
- Kotlin에서 inline functions을 사용할 때의 장점과 단점은?
- Kotlin에서 Flow와 LiveData의 차이점은?
- Kotlin에서 coroutineScope와 supervisorScope의 차이점은?
- Kotlin에서 backing field와 backing property란?
- Kotlin에서 deep copy와 shallow copy의 차이점은?
- Kotlin에서 sealed class와 enum class의 차이점은?
- Jetpack Compose에서 Slot API란?
- Jetpack Compose에서 derivedStateOf를 사용하는 이유는?
- Jetpack Compose에서 LazyColumn의 성능을 최적화하는 방법은?
- Kotlin Multiplatform을 사용해본 경험이 있는가?
- Android 앱의 크기를 줄이기 위해 적용할 수 있는 최적화 기법은?
- Android에서 Inline Class의 장점은?
- 아이템 100개 와 ViewHolder 1개를 가진 RecyclerView의 동작원리를 설명 해주세요.
- RecyclerView or ListView 의 Pagination 구현 방법을 설명 해주세요.
- 네트워크 통신을 통해 이미지를 가져오는 뷰가 포함된 ListView 또는 RecyclerView에서 빠르게 스크롤 시 생길 수 있는 이슈가 무엇이고 어떻게 수정 및 최적화를 할 수 있을까요?
- with, run 의 차이점은 무엇일까요?
- run, let 의 차이점은 무엇일까요?
- let, also 의 차이점은 무엇일까요?
- Immutable 변수와 Mutable 변수를 쓰면 좋은점은 무엇일까요?
- 안드로이드에서 RxJava2 메모리 관리 하는 법은 무엇일까요?
- Parcel 과 Serializable의 차이는 무엇일까요?
- 안드로이드에서 Unit Test가 필요 한 이유는 무엇일까요?
- 기존 프로젝트에서 “개발 서버를 바라보는 어플” 과 “프로덕션 서버를 바라보는 어플”을 나눠서 관리해야 한다고 했을 때 본인의 계획을 말씀 해주세요.
- 인플레이션(inflation)이란 무엇인가요?
- Intent를 통해 데이터 전달하는 과정에서 클래스 객체를 바로 전달하지 못하는 이유는 무엇이고 전달하기 위해서는 어떤 처리가 필요한가요? 그리고 Activity 간 데이터 전달을 위해 Intent 방법을 사용하는 이유가 무엇인가요?
- 복수의 Fragment 간 데이터 전달 방법을 설명 해주세요.
- Width가 1000px Height가 20000px인 이미지가 있고 해당 이미지를 보여주려고 했을 때 아래와 같은 에러가 떴다. 이를 이미지 라이브러리를 사용하지 않고 해결하는 방법에 대해 설명 해주세요.
- W/OpenGLRenderer: Bitmap too large to be uploaded into a texture (max=2048x2048)
- Jetpack Compose를 사용해본 경험이 있는가? 기존 XML 방식과 비교했을 때 어떤 장점과 단점이 있는가?
- Android Lifecycle에 대해 설명하고, ViewModel이 어떻게 메모리 관리를 도와주는지 설명해보라.
- Coroutine과 LiveData의 차이를 설명해보라.
- Flow와 StateFlow, SharedFlow의 차이점은?
- Android 앱의 성능 최적화를 위해 어떤 기법을 사용했는가?
- ProGuard와 R8의 차이를 설명해보라.
- WorkManager, AlarmManager, Foreground Service의 차이점은?
- Jetpack Paging3 라이브러리를 사용해 본 경험이 있는가? 어떻게 동작하는가?
- 앱의 메모리 릭을 찾고 해결하는 방법은?
- 앱이 갑자기 크래시가 발생했을 때 어떻게 디버깅할 것인가?
- Android 앱의 생명주기(Lifecycle)에 대해 설명하라.
- Service와 Foreground Service의 차이점은?
- ViewBinding과 DataBinding의 차이는?
- Jetpack Compose와 기존 View 시스템의 차이점은?
- RecyclerView에서 ViewHolder 패턴이 중요한 이유는?
- 안드로이드의 권한 요청(Permission) 방식이 Android 6.0 이후 어떻게 변경되었는가?
- 멀티 모듈(Multi Module) 프로젝트를 구성할 때 장점과 단점은?
- Dagger, Hilt, Koin 같은 DI(Dependency Injection) 라이브러리를 사용해본 경험이 있는가?
- Android 앱의 ANR(Application Not Responding) 이슈를 해결하는 방법은?
- Java의 OOP(객체지향 프로그래밍) 특징을 설명하라.
- JVM, JRE, JDK의 차이점은?
- Retrofit과 Volley의 차이점은?
- Firebase Crashlytics를 사용한 경험이 있는가? 어떻게 활용했는가?
- Java의 가비지 컬렉션(GC)은 어떻게 동작하는가?
- String, StringBuilder, StringBuffer의 차이는?
- Java에서 volatile, synchronized, Atomic의 차이를 설명하라.
- Java 8에서 추가된 주요 기능(람다, 스트림, Optional 등)에 대해 설명하라.
- Checked Exception과 Unchecked Exception의 차이는?
- HashMap과 ConcurrentHashMap의 차이점은?
- Java에서 Reflection을 사용할 때 주의할 점은?
- Kotlin과 Java의 주요 차이점은?
- Kotlin의 data class와 일반 클래스의 차이는?
- suspend 함수와 Coroutine의 작동 방식은?
- Kotlin에서 lateinit과 lazy의 차이는?
- Kotlin의 sealed class는 어떤 경우에 사용하는가?
- Kotlin의 companion object의 역할은?
- inline 함수와 일반 함수의 차이는?
- Kotlin의 extension function을 설명하라.
- Kotlin의 flow와 channel의 차이점은?
- Jetpack Compose에서 Composition이란 무엇인가? Recomposition은 언제 발생하는가?
- WorkManager와 AlarmManager의 차이점과 사용 사례는?
- Android의 StrictMode를 활용한 성능 개선 방법을 설명하라.
- ViewModel을 Scope별로 관리하는 최적의 방법은?
- 프로세스가 종료된 후에도 데이터가 유지되도록 하는 방법은? (DataStore, Room, SharedPreferences 비교)
- Android에서 Parcelable과 Serializable의 차이를 설명하고, Parcelable을 사용하는 이유는?
- MotionLayout을 활용한 애니메이션 구현 방법을 설명하라.
- Jetpack Navigation Component의 Deep Link 동작 방식과 활용 사례는?
- Android 앱에서 보안 강화를 위한 ProGuard, R8, App Integrity 적용 방법은?
- Java에서 ClassLoader는 어떻게 동작하는가? (Bootstrap, System, Custom ClassLoader)
- ThreadLocal은 어떤 상황에서 유용하게 사용할 수 있는가?
- Java의 CompletableFuture와 ExecutorService의 차이점은?
- JVM의 Garbage Collection(GC) 알고리즘(G1, CMS, ZGC 등)의 차이점과 최적화 방법은?
- synchronized, Lock, ReentrantLock의 차이점과 각각의 장단점은?
- Java의 ForkJoinPool은 어떤 경우에 사용하는가?
- Java에서 Immutable 객체를 설계하는 방법과 장점은?
- Java 17의 최신 기능과 주요 변경 사항을 설명하라.
- Spring Boot의 IoC 컨테이너에서 Bean Lifecycle과 @PostConstruct, @PreDestroy의 역할은?
- Kotlin의 inline, noinline, crossinline 키워드는 언제 사용하는가?
- Coroutine의 Structured Concurrency 개념을 설명하라.
- Coroutine에서 SupervisorJob과 일반 Job의 차이는?
- Kotlin의 Flow에서 SharedFlow와 StateFlow의 차이는?
- Kotlin의 Delegation 패턴은 어떤 경우에 유용한가?
- Jetpack Compose의 Slot API 개념과 활용 사례는?
- invoke operator를 활용한 고급 함수형 프로그래밍 예제를 설명하라.
- Kotlin Multiplatform에서 JVM, Native, JS 타겟을 함께 사용할 때의 문제점과 해결 방법은?
- Zygote 에 대해서 말해보세요.
- JVM과 Dalvik 가상 머신에 대해서 설명해보세요
- SharedPreferences 에서 commit() 과 apply() 의 다른점에 대해 말해주세요.
- 안드로이드에서 메모리 누수를 줄일 수 있는 방법에 대해 말해주세요.
- 안드로이드 APK 파일의 크기를 줄일 수 있는 방법들을 말해주세요.
- 비트맵보다 용량이 작으면서 XML로 작성 가능한 방법
- 안드로이드 어플리케이션의 빌드 시간을 줄일 수 있는 방법들을 말해주세요.
- aaptOptions.cruncherEnabled=false 설명
- Ext.alwaysUpdateBuildId = false 설명
- Gradle은 맨 뒤에 ‘+’를 추가하면 자동으로 최신 버전으로 업데이트, 자동 업데이트하게 하는 방법
- 바이트 코드를 안드로이드에서 바로 실행할 수 있나요?
- 채팅 기능 구현 경험이 있는가?
- Annotation이란?
- AsyncTask Deprecated된 이유는 무엇인가?
- JAR, AAR, DEX, APK에 대해 설명해보아라?
- 프래그먼트는 기본 생성자를 왜 사용해야 할까?
- Gradle / Ant / Maven이 무엇인가?
- String vs StringBuffer vs StringBuilder 에 대해 설명해보아라?
- 직렬화 vs 역직렬화 개념에 대해 설명해보아라?
- Parcelable, Serializable 차이점은 무엇입니까?
- var, val차이
- 코틀린에서 두드러지는 특징
- 코루틴 설명
- 엘비스 연산자