# Concepts, Features, Types and Pros and Cons

Organize concepts, features, types and Pros and Cons

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
    - UI/UX 디자인
        - (1) D-Pad(방향키) 네비게이션 지원
	        - Android TV에는 터치스크린이 없고, 리모컨으로 조작하기 때문에 방향키(D-Pad) 및 이벤트 처리가 중요
	        - focusable, nextFocusUp, nextFocusDown, nextFocusLeft, nextFocusRight 속성을 설정하여 UI 포커스 이동을 제어
	        - onKeyDown(), onKeyUp(), dispatchKeyEvent()를 활용하여 리모컨 이벤트 처리

        - (2) TV 전용 레이아웃 사용 (Leanback Library)
	        - Android TV는 Leanback 라이브러리를 제공하여 TV UI 최적화된 레이아웃을 쉽게 구현 가능.
	        - BrowseFragment, DetailsFragment, PlaybackFragment 등 제공.

        - (3) TV 해상도 및 안전 영역(Safe Area) 고려
	        - TV는 다양한 해상도를 가짐 (1920x1080, 4K, 8K 등)
	        - UI 요소가 TV 화면 가장자리로 잘리지 않도록 Safe Area(안전 영역)를 고려
            - 해결 방법
	            - android:layout_margin을 활용하여 UI 여백 설정.
	            - Overscan 처리 (android:padding="16dp").

        - (4) 큰 화면에 적합한 UI 구성
	        - 가독성이 좋은 큰 글씨체 (sp 단위 사용).
	        - 선명한 아이콘 및 이미지 (xxxhdpi 이상 지원).
	        - 컬러 대비 강조 (어두운 배경 + 밝은 글씨).

    - 입력 및 컨트롤
        - (1) 리모컨 버튼 지원
	        - D-Pad(방향키), ENTER, BACK, HOME, MENU, PLAY, PAUSE 등 리모컨 이벤트 처리 필요
	        - KeyEvent.KEYCODE_DPAD_UP, KeyEvent.KEYCODE_MEDIA_PLAY_PAUSE 등을 활용

        - (2) 음성 검색 지원 (Google Assistant)
	        - TV에서는 음성 검색(Voice Input)이 중요하며, Google Assistant와 통합 가능
	        - android.speech.RecognizerIntent 사용

    - 미디어 및 스트리밍
        - (1) ExoPlayer 활용
	        - Android TV는 미디어 소비 중심이므로 ExoPlayer를 활용한 동영상 스트리밍 필수.
	        - HLS, DASH, MP4 등의 포맷 지원.

        - (2) 미디어 리모컨 & 재생 제어
	        - 리모컨 Play/Pause 버튼 지원 (MediaSessionCompat 활용).
	        - PlaybackSupportFragment를 사용하여 TV 전용 미디어 UI 제공.

    - 성능 최적화 및 기타 고려 사항
        - (1) 성능 최적화
	        - Android TV의 하드웨어 성능이 제한적일 수 있음 (특히 저가형 셋톱박스)
	        - 최적화된 이미지 및 비디오 사용 (.webp, 동적 로딩).
	        - 네트워크 최적화 → 비디오 스트리밍 시 Adaptive Streaming 활용.

        - (2) Google Play Store TV 인증
	        - Android TV 앱을 Google Play에 배포하려면 TV 인증 기준 충족 필요.
	        - android.hardware.type.television을 AndroidManifest.xml에 추가.
            - Google TV 리모컨 네비게이션 테스트 필수
                ```xml
                <uses-feature android:name="android.hardware.type.television"/>
                <uses-feature android:name="android.software.leanback" />   
                ```
        - (3) 광고 및 인앱 구매 지원
	        - TV 광고 및 인앱 구매 시 Google Ads 또는 Google Play Billing API 활용

    - Android TV 앱 개발 체크리스트
        - UI/UX: D-Pad 네비게이션, 큰 글씨, 안전 영역(Safe Area)
        - 입력 지원: 리모컨 버튼, 음성 검색(Google Assistant)
        - 미디어 재생: ExoPlayer, HLS/DASH 스트리밍 지원
        - 성능 최적화: 저사양 TV 기기 최적화, 네트워크 최적화
        - TV 앱 배포: Google Play TV 인증, Leanback 지원

    - 결론
        - Android TV 앱은 터치 기반이 아닌 리모컨 중심이므로, D-Pad 네비게이션을 최적화하는 것이 중요
        - ExoPlayer를 활용하여 원활한 미디어 스트리밍 제공
        - 성능 최적화, 네트워크 최적화, Google Play TV 인증 고려 필수
        - Leanback 라이브러리를 적극 활용하여 TV 친화적인 UI 구현
        - Android TV 앱 개발 시 모바일과 다른 점을 충분히 고려하여 최적화하는 것이 핵심

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

- 안드로이드 파편화
    - 구글이 아무리 업데이트를 발 빠르게 한다할지라도 해당 단말 제조사에서 업데이트를 해주지 않게 되면
    - 안드로이드 플랫폼 버전의 파편화가 발생
    - iOS는 애플이 모든것을 관리하므로 파편화가 적음

- Android 앱의 백그라운드 작업을 효율적으로 수행하는 방법
    - Android 앱 개발에서 백그라운드 작업을 효율적으로 수행하는 것은 배터리 최적화, 성능, 사용자의 원활한 경험을 위해 필수적
    - Android는 Doze 모드, 백그라운드 제한 등의 정책이 강화되었기 때문에 최신 기술과 베스트 프랙티스를 적용하는 것이 중요
        - Doze모드: Android 6.0 (Marshmallow, API 23) 부터 도입된 기능으로, 기기의 배터리 소모를 줄이기 위해 백그라운드 작업을 제한하는 절전 모드

    - 최신 Android 백그라운드 작업 개요
        - 백그라운드 제한 강화: Android 8.0 (Oreo, API 26)부터 백그라운드 실행 제한 도입
        - Doze 모드 & 앱 대기(App Standby): 일정 시간 후 CPU 및 네트워크 제한
        - 포그라운드 서비스 권장: 장시간 실행하는 작업은 백그라운드 서비스보다 포그라운드 서비스 사용
        - WorkManager, Coroutine, JobScheduler 등 최신 기술 활용 필요

    - 최신 Android 백그라운드 작업 처리 기법
        - WorkManager (권장)
            - 백그라운드에서 지속적으로 실행되어야 하는 작업 (예: 데이터 동기화, 로그 업로드, 백업 등)
            - Doze 모드 및 앱 종료 후에도 실행 가능
            - JobScheduler, AlarmManager, Firebase JobDispatcher 통합한 최신 API
            - 백그라운드 실행 제한을 우회하여 작업 실행 보장

        - WorkManager 사용 예제
            ```kotlin
            class MyWorker(appContext: Context, workerParams: WorkerParameters) : Worker(appContext, workerParams) {
                override fun doWork(): Result {
                    // 백그라운드에서 실행할 작업
                    Log.d("WorkManager", "백그라운드 작업 수행 중...")
                    return Result.success()
                }
            }

            // WorkManager 실행 코드
            val workRequest = OneTimeWorkRequestBuilder<MyWorker>().build()
            WorkManager.getInstance(context).enqueue(workRequest)
            ```
            - OneTimeWorkRequest: 한 번만 실행
            - PeriodicWorkRequest: 반복 실행 (예: 15분마다 데이터 동기화)

        - WorkManager 장점
            - Doze 모드에서도 동작 가능
            - 앱이 종료되어도 작업 수행 보장
            - Android 6.0(API 23) 이상 모든 기기에서 사용 가능

        - Foreground Service (포그라운드 서비스)
            - 사용자가 인지해야 하는 장시간 작업 (예: 음악 재생, 위치 추적, 파일 다운로드)
            - 포그라운드에서 지속적으로 실행되는 서비스

        - Foreground Service 구현 예제
            ```kotlin
            class MyForegroundService : Service() {
                override fun onCreate() {
                    super.onCreate()
                    val notification = NotificationCompat.Builder(this, "CHANNEL_ID")
                        .setContentTitle("Foreground Service")
                        .setContentText("작업 실행 중...")
                        .setSmallIcon(R.drawable.ic_launcher_foreground)
                        .build()

                    startForeground(1, notification) // 서비스 실행
                }

                override fun onBind(intent: Intent?): IBinder? = null
            }
            ```
            - startForeground()를 호출하면 백그라운드 실행 제한 없이 작업 수행 가능
            - Android 9.0(API 28) 이상에서는 Foreground Service Type을 명시해야 함

        - Foreground Service 장점
            - 강제 종료되지 않고 지속적으로 실행 가능
            - 사용자에게 진행 상황을 알릴 수 있음 (알림 표시 필수)
            - 배터리 최적화 정책에 영향 받지 않음

        - Coroutine + LifecycleScope (단기 작업)
            - 백그라운드에서 빠르게 실행해야 하는 단기 작업 (예: 네트워크 요청, 데이터베이스 쿼리)
            - LifecycleScope을 활용하여 메모리 누수 방지
            - Coroutine 사용 예제
                ```kotlin
                lifecycleScope.launch(Dispatchers.IO) {
                    val response = api.getData()
                    withContext(Dispatchers.Main) {
                        textView.text = response.data
                    }
                }
                ```
                - Dispatchers.IO: 네트워크 요청, 데이터베이스 작업에 적합
                - Dispatchers.Main: UI 업데이트는 Main Thread에서 실행

        - Coroutine 장점
            - 비동기 처리 최적화 (Thread 관리 불필요)
            - LifecycleScope을 활용하면 자동으로 메모리 관리 가능

        - JobScheduler (Android 5.0 이상, API 21+)
            - 네트워크 상태, 배터리 상태 등 특정 조건에서 실행해야 하는 작업
            - OS가 자동으로 Job을 스케줄링하여 실행 최적화

        - JobScheduler 사용 예제
            ```kotlin
            val jobScheduler = getSystemService(JobScheduler::class.java)
            val jobInfo = JobInfo.Builder(1, ComponentName(this, MyJobService::class.java))
                .setRequiredNetworkType(JobInfo.NETWORK_TYPE_UNMETERED) // WiFi 상태에서만 실행
                .setRequiresCharging(true) // 충전 중일 때 실행
                .build()

            jobScheduler.schedule(jobInfo)
            ```

        - JobScheduler의 특징
            - Doze 모드에서 실행 가능
            - 배터리 상태, 네트워크 상태 등에 따라 작업을 지연 가능

    - 백그라운드 작업 선택 가이드
        - 긴 작업 (배터리 영향 있음): WorkManager
        - 사용자가 인식해야 하는 작업 (음악, 위치 추적 등): Foreground Service
        - 짧은 네트워크 요청, DB 작업: Coroutine + Dispatchers.IO
        - 특정 조건에서 실행 (WiFi, 충전 중 등): JobScheduler

    - 백그라운드 최적화를 위한 추가 고려 사항
        - (1) Doze 모드 및 백그라운드 제한 대응
            - Android 6.0 이상에서 Doze 모드에 의해 백그라운드 작업이 지연될 수 있음
            - setExactAndAllowWhileIdle() (AlarmManager) 또는 WorkManager를 사용해야 함
        - (2) 백그라운드 위치 추적 제한
            - Android 10(API 29) 이상에서는 백그라운드에서 GPS 추적 제한
            - Foreground Service에서 위치 추적을 수행해야 함
        - (3) Battery Optimization 예외 처리
            ```kotlin
            val intent = Intent(Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS)
            intent.data = Uri.parse("package:$packageName")
            startActivity(intent)
            ```
            - 사용자가 직접 배터리 최적화 예외 처리 가능

    - 결론
        - 최신 Android 버전에서는 백그라운드 실행이 제한되므로 적절한 솔루션 선택 필수
        - 반복적이거나 장기적인 작업은 WorkManager를 활용
        - UI와 연결된 단기 작업은 Coroutine + LifecycleScope 사용
        - 포그라운드에서 지속적으로 실행해야 하는 작업은 Foreground Service 사용
        - 네트워크 상태, 배터리 조건에 따라 실행해야 하는 작업은 JobScheduler 사용
        - 최신 Android 백그라운드 작업은 WorkManager + Coroutine을 적극 활용하는 것이 핵심

- Android에서 WorkManager와 JobScheduler의 차이점
    - 개요
        - Android에서 백그라운드 작업을 수행할 때 가장 많이 사용되는 두 가지 API는 WorkManager와 JobScheduler
        - 두 API는 작업(Job)을 예약하고 실행하는 기능을 제공하지만, 몇 가지 차이점 존재

    - WorkManager vs JobScheduler 개념 비교
        - 주요 목적	
            - WorkManager: 장기 실행 백그라운드 작업 (데이터 동기화, 로그 전송 등)
            - JobScheduler: 특정 조건에서 실행되는 작업 (WiFi 연결 시 데이터 업로드 등)
        - Android 지원 버전
            - WorkManager: API 14 (Android 4.0) 이상
            - JobScheduler: API 21 (Android 5.0) 이상
        - Doze 모드 대응
            - WorkManager: 자동 지원 (OS가 최적화)
            - JobScheduler: 자동 지원 (OS가 최적화)
        - 네트워크 및 충전 조건 제어
            - WorkManager: 가능 (Constraints.Builder())
            - JobScheduler: 가능 (setRequiredNetworkType(), setRequiresCharging())
        - 작업 스케줄링 방식
            - WorkManager: 내부적으로 JobScheduler & AlarmManager 사용
            - JobScheduler: JobScheduler 사용
        - 앱이 종료된 경우
            - WorkManager: 다시 실행 보장
            - JobScheduler: 일부 조건에서 재실행 보장 X
        - 즉시 실행 가능 여부
            - WorkManager: 가능 (OneTimeWorkRequest)
            - JobScheduler: 즉시 실행 불가능
        - 주기적 실행 가능 여부	
            - WorkManager: 가능 (PeriodicWorkRequest)
            - JobScheduler: 가능 (setPeriodic())
        - 백그라운드 제한 영향
            - WorkManager: 제한 적음
            - JobScheduler: 제한이 많음 (Doze 모드 & 앱 대기 영향)

    - WorkManager vs JobScheduler 사용 시점
        - WorkManager를 사용해야 하는 경우 (권장)
            - 반복적으로 실행해야 하는 작업 (주기적인 데이터 동기화, 로그 저장)
            - 앱이 종료되더라도 반드시 실행해야 하는 작업
            - 저장소에 데이터 백업, 네트워크 연결 시 데이터 업로드
            - 모든 Android 버전에서 동작해야 하는 경우 (API 14 이상 지원)
        - JobScheduler를 사용해야 하는 경우
            - Android 5.0 (API 21) 이상을 대상으로 특정 조건에서 실행할 때
            - 네트워크 연결, 충전 중, 기기 유휴 상태에서 실행해야 하는 경우
            - 즉시 실행이 필요하지 않은 예약된 작업

    - WorkManager와 JobScheduler 선택 가이드
        - 앱이 종료되어도 작업을 유지해야 함: WorkManager
        - Wi-Fi, 충전 중 등 특정 조건에서만 실행: JobScheduler
        - 특정 시간 간격으로 반복 실행: WorkManager
        - Android 4.0(API 14) 이상 지원 필요: WorkManager
        - 즉시 실행 가능해야 함: WorkManager
        - 앱이 백그라운드 실행 제한을 받지 않아야 함: WorkManager
    - 결론
        - WorkManager는 Android 4.0(API 14) 이상 지원 + JobScheduler & AlarmManager를 내부적으로 활용하는 최신 API로, 대부분의 경우 WorkManager가 권장됨
        - JobScheduler는 특정 네트워크, 충전 상태 조건이 필요한 작업을 예약할 때 유용하지만, 즉시 실행이 필요하거나 앱이 종료된 후 작업이 유지되어야 하는 경우에는 WorkManager가 더 적합
        - 최신 Android 앱 개발에서는 대부분 WorkManager를 활용하는 것이 가장 좋은 선택

- Android TV 앱에서 Leanback 라이브러리의 역할
    - 개요
        - Leanback 라이브러리는 Android TV 앱을 개발할 때, TV 환경에 최적화된 UI 및 기능을 쉽게 구현할 수 있도록 도와주는 라이브러리
        - Android TV에서는 리모컨 기반의 탐색(Navigation)과 10-foot UI(멀리서도 쉽게 보이는 UI)가 중요하기 때문에, Leanback 라이브러리는 TV 환경에 맞는 UI 컴포넌트와 탐색 기능을 제공

    - Leanback 라이브러리의 주요 역할
        - TV에 최적화된 UI 제공
            - Android TV는 모바일과는 다른 화면 크기와 입력 방식(리모컨, 게임패드 등)을 사용하기 때문에, Leanback 라이브러리는 TV 친화적인 UI 컴포넌트를 제공
            - 대표적인 UI 컴포넌트
                - BrowseSupportFragment: TV의 메인 화면에서 카테고리별 콘텐츠(예: 영화, 드라마)를 표시하는 UI
                - RowsSupportFragment: BrowseSupportFragment 내부에서 콘텐츠를 가로 행(Row) 형태로 배치하는 UI
                - DetailsSupportFragment: 특정 콘텐츠를 선택했을 때 상세 정보를 보여주는 UI
                - PlaybackSupportFragment: 동영상 재생을 위한 UI
                - SearchSupportFragment: TV에서 키보드 입력 없이 음성 검색을 지원하는 UI

        - 리모컨 네비게이션 지원
            - Leanback 라이브러리는 D-Pad(방향키), OK 버튼, 백 버튼 등을 활용한 리모컨 탐색을 쉽게 구현할 수 있도록 함
            - Leanback에서 제공하는 포커스 관리 시스템
                - TV 앱에서는 터치 대신 방향키(↑ ↓ ← →)로 이동해야 함
                - Leanback의 UI 컴포넌트는 자동으로 포커스를 관리해주므로 개발자가 직접 UI 포커스를 조정할 필요 없음
                - 사용자가 방향키를 눌렀을 때 자동으로 다음 UI 요소로 이동하는 기능을 기본 지원

        - 추천 및 검색 기능 (Recommendations & Search)
            - Leanback 라이브러리는 Android TV의 기본 홈 화면과 연동하여 콘텐츠를 추천하고, 검색 기능을 구현할 수 있도록 지원
            - 추천(Recommendations) API
                - TvRecommendationManager를 사용하여 사용자 맞춤 추천 콘텐츠를 Android TV 홈 화면에 표시할 수 있음.
            - 음성 검색 지원
                - SearchSupportFragment를 활용하여 음성 검색 기능을 추가할 수 있음
                - Android TV에서는 리모컨의 마이크 버튼을 통해 음성 검색 가능
                - onSearchRequested()를 사용하여 검색 실행 가능

        - 미디어 재생 기능 강화
            - Leanback 라이브러리는 TV 환경에서 동영상 재생을 쉽게 구현할 수 있도록 미디어 플레이어 관련 UI와 API를 제공
            - PlaybackSupportFragment
                - Android TV에서 비디오 플레이어 UI를 쉽게 구현할 수 있음.
                - 미디어 컨트롤(재생, 일시정지, 빨리 감기, 뒤로 감기)을 기본 제공.
            - VideoSupportFragment
                - ExoPlayer 또는 MediaPlayer와 연동하여 비디오 스트리밍을 쉽게 지원

        - TV 스타일 애니메이션 및 UI 트랜지션 지원
            - Leanback 라이브러리는 TV 환경에 적합한 UI 애니메이션과 트랜지션을 기본 제공하여, 부드러운 사용자 경험을 보장
            - 대표적인 UI 트랜지션
                - Slide, Fade, Explode 등의 애니메이션 효과를 활용하여 화면 전환을 부드럽게 처리 가능

    - Leanback 라이브러리의 핵심 컴포넌트
        - BrowseSupportFragment: TV 앱의 메인 화면 구성 (카테고리별 콘텐츠 목록)
        - RowsSupportFragment: 가로로 정렬된 콘텐츠 리스트
        - DetailsSupportFragment: 특정 콘텐츠의 상세 정보 화면
        - PlaybackSupportFragment: 동영상 재생을 위한 UI
        - SearchSupportFragment: 음성 및 텍스트 검색 기능
        - HeadersSupportFragment: 좌측 메뉴 (카테고리, 설정 등)
        - VerticalGridSupportFragment: 세로형 그리드 UI 지원
        - GuidedStepSupportFragment: TV 설정 화면 또는 단계별 가이드 화면

    - Leanback 라이브러리 사용 예제
        - BrowseSupportFragment를 활용하여 카테고리별 콘텐츠 목록을 가로로 표시하는 TV UI를 구성하는 예제
        ```kotlin
        class MainFragment : BrowseSupportFragment() {
            override fun onCreate(savedInstanceState: Bundle?) {
                super.onCreate(savedInstanceState)

                title = "My TV App"
                headersState = HEADERS_ENABLED
                isHeadersTransitionOnBackEnabled = true

                loadRows()
            }

            private fun loadRows() {
                val rowsAdapter = ArrayObjectAdapter(ListRowPresenter())
                val cardPresenter = CardPresenter()

                val movieList = listOf("Movie 1", "Movie 2", "Movie 3")
                val movieAdapter = ArrayObjectAdapter(cardPresenter)
                movieList.forEach { movieAdapter.add(it) }

                val header = HeaderItem(0, "Movies")
                rowsAdapter.add(ListRow(header, movieAdapter))

                adapter = rowsAdapter
            }
        }
        ```
    - Leanback 라이브러리의 장점
        - TV UI에 최적화된 디자인을 제공 → 별도로 UI를 개발할 필요 없이 기본 제공되는 UI 컴포넌트를 활용 가능
        - 리모컨 네비게이션을 기본 지원 → 포커스 이동 및 버튼 입력을 직접 처리할 필요 없음
        - 추천 및 검색 기능 쉽게 구현 가능 → Android TV의 홈 화면과 연동하여 추천 콘텐츠 제공 가능
        - 미디어 재생 기능 강화 → PlaybackSupportFragment를 활용하여 동영상 재생 UI를 쉽게 구성 가능
        - 애니메이션 및 전환 효과 제공 → TV 앱에 적합한 부드러운 화면 전환을 기본 제공

    - 결론
        - Android TV 앱을 개발할 때 Leanback 라이브러리를 사용하면, TV 환경에 적합한 UI/UX를 쉽게 구현 가능
        - 리모컨 탐색, 콘텐츠 추천, 음성 검색, 동영상 재생 UI 등의 기능을 최소한의 코드 변경으로 구현할 수 있기 때문에, 효율적인 개발이 가능
        - Leanback은 Android TV 앱 개발을 쉽게 해주는 TV 최적화 UI 라이브러리

- Android TV 앱 개발 시 D-pad(방향키) 네비게이션을 처리하는 방법
    - 개요
        - Android TV 앱을 개발할 때, D-pad(방향키) 네비게이션을 올바르게 처리하는 것이 중요
        - Android TV는 터치스크린이 아닌 리모컨의 방향키(D-pad)와 Enter 버튼을 활용한 조작 방식이므로, 앱 내 UI 요소가 원활하게 이동하고 선택될 수 있도록 처리해야 함
    - D-Pad 네비게이션 개요
        - D-pad는 방향키(Up, Down, Left, Right) 및 선택(Enter, OK 버튼)으로 구성Android TV 앱에서는 기본적으로 포커스(focus) 기반 UI 시스템을 사용하며, RecyclerView, Button, ImageView 등 다양한 뷰에 대한 포커스 이동 제어 필요

        - D-pad 입력 이벤트
            - Android TV에서 D-pad 입력 이벤트는 KeyEvent를 통해 감지 가능
                - KeyEvent.KEYCODE_DPAD_UP → 위 방향키
                - KeyEvent.KEYCODE_DPAD_DOWN → 아래 방향키
                - KeyEvent.KEYCODE_DPAD_LEFT → 왼쪽 방향키
                - KeyEvent.KEYCODE_DPAD_RIGHT → 오른쪽 방향키
                - KeyEvent.KEYCODE_DPAD_CENTER → 선택(Enter)
                - KeyEvent.KEYCODE_ENTER → Enter 버튼

    - 기본적인 포커스 처리
        - 개요
            - Android TV에서는 기본적으로 포커스를 자동으로 관리
            - android:focusable="true" 속성을 설정하면 기본적인 포커스 이동이 가능

        - XML에서 포커스 설정
            ```xml
            <Button
                android:id="@+id/myButton"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Select"
                android:focusable="true"
                android:focusableInTouchMode="true"/>
            ```
            - android:focusable="true" → 뷰가 포커스를 받을 수 있도록 설정
            - android:focusableInTouchMode="true" → 터치 모드에서도 포커스를 받을 수 있도록 설정
        - Button, TextView, ImageView 같은 뷰는 기본적으로 포커스를 받을 수 있지만, LinearLayout, FrameLayout 같은 레이아웃은 기본적으로 포커스를 받지 않음
            - 포커스 이동을 원할 경우 android:focusable="true" 속성을 명시적으로 추가 필요

    -  커스텀 D-pad 네비게이션 처리
        - 개요
            - 기본적으로 Android의 포커스 자동 이동 기능을 사용할 수 있지만, 커스텀 네비게이션을 적용해야 할 경우 setOnKeyListener 또는 dispatchKeyEvent() 활용 가능

        - setOnKeyListener를 활용한 방향키 이벤트 처리
            ```java
            myButton.setOnKeyListener { v, keyCode, event ->
                if (event.action == KeyEvent.ACTION_DOWN) {
                    when (keyCode) {
                        KeyEvent.KEYCODE_DPAD_UP -> {
                            Log.d("D-pad", "위 방향키 눌림")
                            return@setOnKeyListener true
                        }
                        KeyEvent.KEYCODE_DPAD_DOWN -> {
                            Log.d("D-pad", "아래 방향키 눌림")
                            return@setOnKeyListener true
                        }
                        KeyEvent.KEYCODE_DPAD_LEFT -> {
                            Log.d("D-pad", "왼쪽 방향키 눌림")
                            return@setOnKeyListener true
                        }
                        KeyEvent.KEYCODE_DPAD_RIGHT -> {
                            Log.d("D-pad", "오른쪽 방향키 눌림")
                            return@setOnKeyListener true
                        }
                        KeyEvent.KEYCODE_DPAD_CENTER, KeyEvent.KEYCODE_ENTER -> {
                            Log.d("D-pad", "Enter(선택) 버튼 눌림")
                            return@setOnKeyListener true
                        }
                    }
                }
                return@setOnKeyListener false
            }
            ```
            - KeyEvent를 활용하여 방향키 입력을 감지하고, 원하는 동작을 정의할 수 있음.
            - (중요) return true를 사용하면 이벤트가 소비되고, return false를 사용하면 다른 UI 요소로 이벤트가 전달

    - 포커스 이동 방향 지정하기
        - 개요
            - D-pad를 사용할 때 UI 요소 간 포커스 이동 방향을 명확하게 지정해야 함
                - android:nextFocusUp, android:nextFocusDown, android:nextFocusLeft, android:nextFocusRight 속성 활용 가능

        - XML에서 포커스 이동 방향 지정
            ```xml
            <Button
                android:id="@+id/button1"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Button 1"
                android:focusable="true"
                android:nextFocusDown="@id/button2"/>

            <Button
                android:id="@+id/button2"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Button 2"
                android:focusable="true"
                android:nextFocusUp="@id/button1"/>
            ```
            - button1에서 아래 방향키(↓)를 누르면 button2로 이동
            - button2에서 위 방향키(↑)를 누르면 button1으로 이동
                - 명시적인 포커스 이동을 설정하면 불필요한 포커스 이동 문제 방지 가능

    - RecyclerView에서 D-pad 네비게이션 처리
        - 개요
            - Android TV에서는 RecyclerView에서 방향키 이동을 최적화하는 것이 중요

        - RecyclerView의 포커스 처리 방법
            - 뷰 홀더(ViewHolder)에 focusable 속성을 추가
            - descendantFocusability="afterDescendants" 설정
            - 포커스 이동을 위해 requestFocus() 사용
                ```xml
                <androidx.recyclerview.widget.RecyclerView
                android:id="@+id/recyclerView"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:focusable="true"
                android:descendantFocusability="afterDescendants"/>
                ```
                - descendantFocusability="afterDescendants" → 리스트 아이템 내부 뷰에 포커스를 우선 부여

                ```java
                override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
                    val item = items[position]
                    holder.itemView.isFocusable = true
                    holder.itemView.setOnFocusChangeListener { v, hasFocus ->
                        if (hasFocus) {
                            Log.d("RecyclerView", "포커스 이동: $position")
                        }
                    }
                }
                ```
                - itemView.isFocusable = true → 각 아이템이 포커스를 받을 수 있도록 설정
                - setOnFocusChangeListener → 포커스가 이동할 때 이벤트 감지

    - Android TV Leanback 라이브러리를 활용한 D-pad 네비게이션
        - 개요
            - Android TV 앱에서는 Leanback 라이브러리를 활용하면 더 쉽게 D-pad 네비게이션 구현 가능

        - Leanback 라이브러리 사용
            - BrowseSupportFragment, RowsSupportFragment, GuidedStepFragment 등을 제공하여 자동으로 D-pad 네비게이션을 지원
            - Presenter 클래스를 활용하여 UI 요소 렌더링 가능
                ```groovy
                dependencies {
                    implementation 'androidx.leanback:leanback:1.2.0'
                }
                ```
                - RecyclerView를 직접 제어하는 것보다 더 최적화된 방식으로 포커스를 관리할 수 있음

    - 결론
        - D-pad(방향키) 입력을 처리하는 주요 방법
            - KeyEvent를 활용하여 방향키 이벤트 감지
            - android:focusable="true"를 사용하여 포커스 가능하게 설정
            - android:nextFocusUp / nextFocusDown / nextFocusLeft / nextFocusRight 속성을 활용하여 포커스 이동 제어
            - RecyclerView에서 isFocusable=true 설정하여 리스트 아이템이 포커스를 받을 수 있도록 처리
            - Android TV의 Leanback 라이브러리를 활용하면 더 쉽게 TV 앱을 개발할 수 있음
        - 올바른 포커스 이동을 구현하면 Android TV 앱의 사용자 경험(UX)을 크게 향상시킬 수 있음

- Android에서 Jetpack DataStore를 사용하는 이유
    - Jetpack DataStore 개념
        - Jetpack DataStore는 Android에서 데이터를 저장 및 관리하기 위한 최신 라이브러리
        - 기존 SharedPreferences의 단점을 해결하고 더 나은 성능과 안정성을 제공
        - DataStore는 두 가지 방식으로 데이터를 저장 가능
            - Preferences DataStore → Key-Value 기반 데이터 저장 (SharedPreferences 대체)
            - Proto DataStore → Protobuf을 사용한 구조화된 데이터 저장 (타입 안정성 제공)

    - DataStore를 사용하는 주요 이유
        - (1) SharedPreferences의 단점 해결
            - 기존 SharedPreferences는 동기식(I/O Blocking)으로 동작하며, 다음과 같은 문제점 존재
                - ANR(Application Not Responding) 발생 가능: apply()와 commit()은 메인 스레드에서 실행될 경우 성능 저하 및 UI 지연을 초래
                - 비동기 저장 시 데이터 손실 가능: apply()는 비동기 저장을 수행하므로, 강제 종료 시 데이터가 저장되지 않을 수 있음
                - 읽기/쓰기 성능 저하: 데이터를 XML 파일로 저장하기 때문에 대량의 데이터를 다룰 때 속도가 느림
                - DataStore는 비동기 처리와 코루틴(Flow)을 활용하여 이러한 문제를 해결

        - (2) 비동기(Asynchronous) & 코루틴(Flow) 지원
            - DataStore는 Kotlin Coroutine과 Flow를 사용하여 비동기적으로 데이터 저장 및 로드할 수 있음

            - 메인 스레드에서 블로킹 없이 데이터 처리 가능
            - Flow 기반 데이터 스트림 제공 → 데이터 변경 시 자동 업데이트됨
                ```java
                val exampleCounterFlow: Flow<Int> = dataStore.data
                .map { preferences ->
                    preferences[EXAMPLE_COUNTER] ?: 0
                }
                ```
                - Flow를 통해 데이터를 실시간으로 감지하고 자동으로 업데이트할 수 있음

        - (3) 트랜잭션(Atomic Operation) 지원
            - SharedPreferences에서는 데이터 업데이트가 중간에 실패할 경우 데이터가 일관되지 않을 수 있음
            - DataStore는 트랜잭션을 보장하는 API를 제공하여 데이터가 안전하게 저장
                ```java
                suspend fun incrementCounter() {
                    dataStore.edit { preferences ->
                        val currentCounterValue = preferences[EXAMPLE_COUNTER] ?: 0
                        preferences[EXAMPLE_COUNTER] = currentCounterValue + 1
                    }
                }
                ```
                - edit {} 블록 내부에서 원자적(Atomic)으로 데이터가 변경되므로 데이터 정합성이 보장

        - (4) 데이터 변환과 검증 가능 (Proto DataStore)
            - Proto DataStore는 Protobuf을 사용하여 데이터를 저장하므로, 데이터의 타입 안정성(Type Safety)을 보장
            - SharedPreferences는 String, Int, Boolean 등 기본 타입만 저장할 수 있지만, Proto DataStore를 사용하면 객체 데이터를 정의하고 변환하여 저장 가능
                ```java
                syntax = "proto3";

                message UserPreferences {
                int32 user_id = 1;
                string username = 2;
                bool notifications_enabled = 3;
                }
                ```
                - 기존 SharedPreferences는 Key-Value만 저장할 수 있었지만, Proto DataStore를 사용하면 구조화된 데이터를 저장할 수 있음

        - (5) LiveData가 아닌 Flow를 활용하여 실시간 데이터 변경 감지
            - SharedPreferences에서는 값이 변경될 때 SharedPreferences.OnSharedPreferenceChangeListener를 사용해야 했지만, DataStore는 Flow를 사용하여 자동으로 UI가 업데이트
                ```java
                val usernameFlow: Flow<String> = dataStore.data
                    .map { preferences -> preferences[USERNAME_KEY] ?: "Unknown" }
                ```
                - UI에서 Flow를 collectAsState()로 감지하면 자동으로 변경 사항을 적용할 수 있음.

    - 결론
        - Jetpack DataStore는 기존 SharedPreferences의 단점을 보완하며, 비동기 데이터 저장, 트랜잭션 보장, Flow 기반 실시간 데이터 감지 등의 이점을 제공
        - 특히 Proto DataStore를 활용하면 타입 안정성이 보장되는 구조화된 데이터 저장이 가능하므로, 안드로이드에서 로컬 데이터 저장을 할 때 가장 권장되는 솔루션


- Android에서 Jetpack Hilt와 Dagger의 차이점
    - 개요
        - Jetpack Hilt와 Dagger는 모두 의존성 주입(Dependency Injection, DI)을 위한 프레임워크이지만, Hilt는 Dagger를 기반으로 한 Android 전용 DI 라이브러리

    - 개념적인 차이
        - 개발 목적
            - Hilt: Android 전용 DI 프레임워크
            - Dagger: 범용 DI 프레임워크
        - 구글 공식 지원
            - Hilt: Jetpack 라이브러리로 공식 지원	- Dagger: 구글이 지원하지만 Android에 최적화되지 않음
        - 사용 편의성
            - Hilt: 간결한 문법과 자동 구성
            - Dagger: 복잡한 설정이 필요
        - 생산성
            - Hilt: 코드 양이 적고, 간편한 사용 가능	- Dagger: Boilerplate 코드가 많고, 관리가 어렵지만 유연성 제공

    - Jetpack Hilt의 특징
        - 개요
            - Hilt는 Dagger 기반으로 만들어졌지만, Android 앱 개발을 쉽게 할 수 있도록 설계된 Jetpack 라이브러리

        - Hilt의 주요 특징
            - Android Lifecycle과 통합 → Application, Activity, Fragment, ViewModel, Service, WorkManager 등과 호환
            - 자동적으로 Android 진입점(Entry Points) 제공 → @AndroidEntryPoint로 간단히 DI 설정 가능
            - 모듈 정의가 간편함 → @Module과 @InstallIn을 사용하여 구성
            - ViewModel 지원 → @HiltViewModel을 사용하여 ViewModel 내에서 DI 가능
            - Application Scope 제공 → 전역적으로 사용할 객체를 @Singleton으로 관리

    - Dagger의 특징
        - 개요
            - Dagger는 Android뿐만 아니라 Java, Kotlin 프로젝트 전반에서 활용할 수 있는 DI 프레임워크

        - Dagger의 주요 특징
            - 강력한 의존성 관리 기능 → 사용자가 세부적으로 DI를 제어할 수 있음
            - 컴파일 타임 의존성 주입 → 런타임 오버헤드가 적고 빠름
            - 안정성과 최적화된 성능 → Reflection 없이 컴파일 시점에서 코드 생성
            - 커스텀 스코프 지원 → Hilt보다 더 유연한 스코프를 설정 가능
            - 수동 구성 필요 → Component, Module, Provides 등을 직접 정의해야 하므로 코드가 길어질 수 있음

    - 예제 코드 비교
        - Hilt 사용 예제
            - @HiltAndroidApp, @AndroidEntryPoint를 사용하여 간단하게 DI 적용 가능
            ```java
            @HiltAndroidApp
            class MyApplication : Application()

            @AndroidEntryPoint
            class MainActivity : AppCompatActivity() {
                @Inject lateinit var repository: UserRepository
            }
            ```

        - Dagger 사용 예제
            ```java
            /* Component, inject 함수 직접 정의 필요 */
            @Component
            interface AppComponent {
                fun inject(activity: MainActivity)
            }

            class MainActivity : AppCompatActivity() {
                @Inject lateinit var repository: UserRepository

                override fun onCreate(savedInstanceState: Bundle?) {
                    super.onCreate(savedInstanceState)
                    DaggerAppComponent.create().inject(this)
                }
            }
            ```

    - 결론
        - Hilt는 Android 개발에서 DI를 간편하게 적용할 수 있도록 만든 Jetpack 라이브러리이
        - 일반적인 Android 개발에서는 Hilt를 사용하는 것이 권장
        - 보다 정교한 의존성 관리를 원하거나, Android 외 환경에서도 사용하려면 Dagger를 선택하는 것이 좋음

- Android에서 Shared Preferences보다 Encrypted Shared Preferences가 필요한 이유
    - 개요
        - Android의 Shared Preferences는 간단한 Key-Value 형태의 데이터를 로컬 저장소에 저장하는 기능을 제공
        - 기본적으로 암호화되지 않은 상태로 저장되기 때문에 민감한 데이터를 저장하는 데 보안적인 문제 존재
        - 보안 문제 해결을 위해 Encrypted Shared Preferences가 제공되며, 보안 강화를 위해 데이터 암호화 기능을 포함하고 있음

    - Shared Preferences의 문제점
        - 데이터가 평문(Plaintext)으로 저장
            - 일반적인 Shared Preferences 파일(.xml)은 Android 파일 시스템 내부에 저장되지만, 루팅된 기기나 악성 앱이 접근하면 데이터가 그대로 노출될 위험이 있음.
        - 보안 규정 준수 문제
            - 금융, 헬스케어, 기업 애플리케이션에서는 데이터 암호화가 필수적.
            - GDPR, HIPAA, PCI-DSS 같은 보안 규정을 준수해야 하는 경우, Shared Preferences를 그대로 사용할 수 없음
        - 앱 백업 및 마이그레이션 시 데이터 유출 가능성
            - 앱을 백업하거나 마이그레이션할 때, 암호화되지 않은 Shared Preferences 데이터가 외부로 노출될 수 있음

    - Encrypted Shared Preferences의 필요성
        - Jetpack Security 라이브러리에서 제공하는 EncryptedSharedPreferences
        - Encrypted Shared Preferences의 주요 특징
            - AES-256 암호화
                - 저장된 데이터는 AES-256-GCM 알고리즘으로 암호화되어 보안성이 높음
            - 자동 키 관리
                - MasterKey를 사용하여 암호화 키를 자동으로 생성 및 관리 (Android Keystore System 활용).
            - 이전 Shared Preferences와 호환 가능
                - 기존 Shared Preferences API와 사용법이 거의 동일하여 쉽게 적용 가능.
            - 데이터 보호 강화
                - 앱 백업/복구 시 암호화된 상태로 저장되므로 보안성을 유지할 수 있음

    - 적용 예제
        ```java
        import androidx.security.crypto.EncryptedSharedPreferences
        import androidx.security.crypto.MasterKey

        val masterKey = MasterKey.Builder(this)
            .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
            .build()

        val encryptedSharedPreferences = EncryptedSharedPreferences.create(
            this,
            "secure_prefs",
            masterKey,
            EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
            EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
        )

        val editor = encryptedSharedPreferences.edit()
        editor.putString("username", "myUser123")  // 암호화된 데이터 저장
        editor.apply()
        ```
        - AES-256-GCM 암호화를 사용하여 데이터를 안전하게 저장
        - 루팅된 기기에서도 데이터가 암호화된 상태로 저장되므로, 해킹 위험이 줄어듬

    - 결론
        - Encrypted Shared Preferences를 사용해야 하는 경우
            - 로그인 정보 (JWT 토큰, 사용자 ID 등)를 저장할 때
            - API 키, 암호 등 민감한 데이터를 저장할 때
            - 사용자의 금융, 헬스케어 데이터를 저장할 때
            - 루팅된 기기에서도 데이터를 보호해야 할 때
            - 앱이 보안 규정을 준수해야 할 때 (GDPR, PCI-DSS, HIPAA 등)
        - Shared Preferences만 사용해도 되는 경우
            - 단순한 앱 설정 값 (ex: 다크 모드 ON/OFF, 언어 설정 등) 저장 시
            - 민감하지 않은 일반적인 UI 상태 저장 시
        - 최종 정리
            - 기존 Shared Preferences는 보안성이 낮아 중요한 정보를 저장하면 안 됨
            - Encrypted Shared Preferences는 AES-256 암호화를 사용하여 데이터를 보호할 수 있음
            - Jetpack Security 라이브러리를 활용하여 기존 Shared Preferences와 유사한 방식으로 사용 가능
            - 보안이 중요한 데이터(로그인 정보, API 키 등)는 반드시 Encrypted Shared Preferences를 활용하여 보호해야 함
            - 민감한 데이터를 저장해야 한다면, 반드시 Encrypted Shared Preferences를 사용 권장

- Android에서 CameraX와 기존 Camera API의 차이점
    - CameraX vs Camera2 API
        - 개발 난이도
            - CameraX: 매우 간단 (Jetpack 라이브러리)
            - Camera2 API: 복잡한 설정 필요
        - 호환성		
            - CameraX: 다양한 기기에서 일관된 성능 제공
            - Camera2 API: 기기별로 동작이 다를 수 있음
        - 라이프사이클 관리		
            - CameraX: LifecycleOwner와 통합되어 자동 관리
            - Camera2 API: 수동으로 상태 관리 필요
        - 자동 기능 지원		
            - CameraX: 자동 노출, 화이트 밸런스, 포커스 등 지원
            - Camera2 API: 직접 구현해야 함
        - 성능		
            - CameraX: 최적화된 내부 동작으로 높은 성능 제공
            - Camera2 API: 성능 최적화를 직접 해야 함
        - 미리보기(Preview)		
            - CameraX: PreviewView 지원으로 간편 구현
            - Camera2 API: Surface 처리, TextureView 사용 필요
        - 이미지 캡처		
            - CameraX: ImageCapture API 제공
            - Camera2 API: 직접 캡처 및 후처리 필요
        - 영상 녹화		
            - CameraX: VideoCapture API 제공
            - Camera2 API: 직접 MediaRecorder 설정 필요
        - ML Kit 및 AI 기능		
            - CameraX: 쉽게 통합 가능
            - Camera2 API: 직접 프레임을 처리해야 함

    - CameraX vs Camera1 API
        - Camera1 API는 Android 5.0(Lollipop) 이전 버전에서 사용되던 API로, 현재는 거의 사용되지 않음
        - 지원 Android 버전		
            - CameraX: Android 5.0 이상
            - Camera1 API: Android 4.x 이하에서 사용 가능
        - 멀티 카메라 지원		
            - CameraX: 기본 지원
            - Camera1 API: 직접 처리해야 함
        - 자동 기능 지원		
            - CameraX: 자동 초점, 노출 조절 등 지원
            - Camera1 API: 직접 제어 필요
        - 미리보기 처리		
            - CameraX: PreviewView 사용 가능
            - Camera1 API: SurfaceView, TextureView 직접 처리 필요
        - 성능 및 유지보수		
            - CameraX: 최신 기기 최적화
            - Camera1 API: 오래된 API, 유지보수 어려움

    - CameraX의 주요 장점
        - 간편한 개발 → PreviewView, ImageCapture, VideoCapture API 제공
        - 기기 호환성 개선 → 다양한 제조사의 기기에서 일관된 동작 보장
        - Jetpack 라이브러리 통합 → LifecycleOwner, ViewModel 등과 쉽게 연동 가능
        - ML Kit 등과 쉽게 연동 → 얼굴 인식, 바코드 스캔 등 다양한 기능 활용 가능
        - 자동 조정 기능 지원 → 자동 초점(AF), 자동 노출(AE), 자동 화이트 밸런스(AWB)
    - 결론
        - 새로운 프로젝트라면 → CameraX 사용 추천 (간편한 개발 & 최적화된 성능)
        - 고급 기능이 필요하거나 특정 기기 최적화가 필수라면 → Camera2 API 고려
        - 아주 오래된 기기(Android 4.x 이하) 지원이 필요하다면 → Camera1 API 사용 가능

- Android에서 Jetpack WorkManager와 Foreground Service의 차이점
    - Jetpack WorkManager
        - 개념
            - 백그라운드 작업을 일정한 조건(네트워크 연결, 충전 중 등)에 따라 실행할 수 있도록 하는 Jetpack 라이브러리
            - 오래 실행되는 비동기 작업을 OS의 제약 없이 보장
            - 앱이 종료되거나 기기가 재부팅되더라도 작업을 지속할 수 있음
        - 주요 특징 
            - 백그라운드에서 실행 (UI와 무관한 작업)
            - 앱이 종료되거나 기기가 재부팅되어도 작업 유지 가능
            - 제약 조건(Constraints) 설정 가능 (예: 네트워크 필요, 충전 중 실행 등)
            - JobScheduler, AlarmManager, Firebase JobDispatcher 등을 내부적으로 활용
            - 단기 및 장기 작업 모두 가능 (최소 10분 이상의 딜레이 가능)
        - 사용 사례
            - 주기적인 데이터 동기화 (예: 백업, 클라우드 업로드)
            - 네트워크가 가능할 때 파일 업로드
            - 일정한 조건에서 실행해야 하는 작업 (예: 배터리가 충분할 때)
            - 사용자와 직접적인 상호작용이 필요하지 않은 작업
        - 예제
            ```java
            class MyWorker(context: Context, params: WorkerParameters) : Worker(context, params) {
                override fun doWork(): Result {
                    Log.d("WorkManager", "작업 실행 중...")
                    return Result.success()
                }
            }
            // Work 요청
            val workRequest = OneTimeWorkRequestBuilder<MyWorker>().build()
            WorkManager.getInstance(context).enqueue(workRequest)
            ```

    - Foreground Service
        - 개념
            - 사용자가 인식할 수 있는(즉, Notification과 함께 실행되는) 백그라운드 작업
            - 장시간 실행되는 작업을 유지하기 위해 사용됨
            - 사용자가 작업 진행 상태를 확인할 수 있어야 하므로 알림(Notification) 필수
        - 주요 특징
            - 작업이 실행되는 동안 시스템에 의해 종료되지 않음
            - 백그라운드에서 실행되지만, Notification을 통해 사용자에게 표시됨
            - 사용자가 즉시 인식할 수 있는 작업에 적합
            - Android 8.0 (Oreo) 이상에서는 Foreground Service 실행 시 알림(Notification)이 필수
        - 사용 사례
            - 음악 재생 서비스 (Spotify, YouTube Music)
            - 실시간 위치 추적 (Google Maps Navigation)
            - 다운로드 진행 상태 표시
            - 네트워크 스트리밍 (영상, 오디오)
            - 사용자가 직접 실행 중인 작업을 인식해야 하는 경우
        - 예제
            ```java
            class MyForegroundService : Service() {
                override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
                    val notification = NotificationCompat.Builder(this, "channel_id")
                        .setContentTitle("Foreground Service 실행 중")
                        .setContentText("작업을 수행하고 있습니다.")
                        .setSmallIcon(R.drawable.ic_notification)
                        .build()

                    startForeground(1, notification) // Foreground Service 시작
                    return START_STICKY
                }

                override fun onBind(intent: Intent?): IBinder? = null
            }
            ```
    - 결론
        - 사용자가 직접 작업을 인식해야 함: Foreground Service
        - 네트워크 동기화, 백업, 클라우드 업로드 등: WorkManager
        - 앱이 종료되거나 기기가 재부팅되어도 작업을 유지해야 함: WorkManager
        - 사용자가 UI에서 직접 실행하는 작업 (음악, 다운로드 등): Foreground Service
        - OS가 백그라운드 작업을 자동 관리하도록 하고 싶음: WorkManager
        - 정리
            - 사용자가 직접 확인해야 하는 장기 실행 작업 → Foreground Service 사용
            - 앱 종료 후에도 실행되어야 하는 백그라운드 작업 → WorkManager 사용
            - Android 8.0(Oreo) 이상에서는 Foreground Service에 반드시 Notification 필요


- Android에서 Jetpack Paging을 사용하는 이유
    - Jetpack Paging
        - 대량의 데이터를 효율적으로 로드하고 표시하기 위한 라이브러리
        - RecyclerView + Room + Network API에서 페이징 처리를 쉽게 구현할 수 있도록 지원함

    - Jetpack Paging을 사용하는 이유
        - (1) 성능 최적화 (메모리 사용 감소)
            - 대량의 데이터를 한꺼번에 로드하면 메모리 사용량이 증가하고, 앱 성능이 저하됨
            - Jetpack Paging은 필요한 데이터만 로드하여 메모리 사용을 최적화

        - (2) 자동 페이징 처리
            - 사용자가 스크롤할 때 자동으로 다음 페이지를 로드
            - 네트워크 및 데이터베이스 페이징 처리 간소화
            - Room, Retrofit 등과 쉽게 통합 가능

        - (3) 네트워크 및 데이터베이스 연동 가능
            - 네트워크 API에서 데이터를 페이징 처리 가능 (예: Retrofit)
            - 로컬 데이터베이스(Room)와 결합 가능
            - 오프라인 캐싱 및 네트워크 동기화 지원

        - (4) Lifecycle-Aware 지원
            - LiveData, Flow, RxJava와 통합 가능
            - ViewModel과 함께 사용하여 메모리 누수 방지
            - UI가 변경될 때 자동으로 데이터 로드 유지

        - (5) DiffUtil 내장 지원
            - 리스트가 변경될 때 DiffUtil 자동 적용 → 성능 최적화
            - RecyclerView가 불필요한 View 재사용을 최소화하여 렌더링 성능 향상

    - Jetpack Paging 구성 요소
        - PagingSource: 데이터를 로드하는 기본 클래스 (Room/Retrofit 연동)
        - PagingData: 페이징된 데이터 컨테이너 (RecyclerView 연동)
        - Pager: PagingData를 생성 및 관리
        - PagingDataAdapter: RecyclerView에서 DiffUtil 자동 적용

    - 결론
        - Jetpack Paging을 사용 시
            - 대량의 데이터를 효율적으로 로드 가능
            - 자동 페이징 처리 및 성능 최적화
            - 네트워크 API + 로컬 DB(Room)과 쉽게 통합
            - ViewModel + LiveData / Flow와 함께 사용 가능
        - RecyclerView에서 데이터를 페이징하여 로드해야 하는 경우, Jetpack Paging이 가장 효과적인 솔루션

- Android에서 App Bundle과 APK의 차이점
    - APK(Android Package)
        - 특징
            - 완전한 하나의 앱 설치 파일
            - 하나에 모든 리소스, 언어, ABI(프로세서 아키텍처)가 다 들어있음
            - 크기가 큼 (예: 영어, 한글, 중국어, arm64, x86 등 전부 포함)
        - 사용 예시
            - 사내 배포 / 테스트
            - 외부 테스트 (QA, 베타 테스트)
            - adb 설치 가능
    - App Bundle(AAB)
        - 특징
            - 개발자가 만드는 것은 .aab, 이걸 Google Play가 분석해서 기기에 맞는 APK를 자동 생성
            - 기기에 맞는 언어, 해상도, ABI만 포함된 Split APK 를 제공
            - 최대 20~50% 용량 감소 가능
        - 구조
            - Play Store는 여기서 사용자 기기에 필요한 부분만 조합해서 APK 생성
            ```bash
            base/
                - AndroidManifest.xml
                - classes.dex
                - res/
                - lib/arm64-v8a/
                - lib/x86/
                - values-ko/
                - values-en/
            ```
    - 설치 흐름
        - APK: 개발자 빌드 > .apk 생성 > 그대로 배포 및 설치
        - AAB: 개발자 빌드 > .aab 생성 > Play Store 업로드 > 사용자 기기에 맞는 APK 조합 > 설치

    - AAB 사용 이유
        - 앱 사이즈 축소 가능
        - 빠른 설치 가능
        - 다국어, 다양한 ABI 지원 앱에 대해 Split APK 최적화
        - Play Feature Delivery / Dynamic Module 같은 기능 지원

    - AAB > APK 변환 방법
        - 구글 플레이 없이 테스트 희망 시 bundletool 사용
            ```bash
            bundletool build-apks \
                --bundle=app.aab \
                --output=output.apks \
                --ks=my-release-key.jks \
                --ks-key-alias=keyAlias \
                --ks-pass=pass:password \
                --key-pass=pass:password

            bundletool install-apks --apks=output.apks
            ```

- Android에서 Jetpack Compose와 기존 XML 기반 UI의 차이점
    - 개요
        - 기존 명령형 > 선언형 스타일로 변경
        - 상태 선언의 개념 > UI 자동 업데이트
        - 대표 개념의 전환: findViewById, ViewGroup > @Composable, State
    - 컴포즈 장점
        - 코틀린 코드로 UI 작성 (생산성 향상)
        - 상태 변화만 주면 UI 자동 업데이트
        - 함수처럼 @Composable 재사용 가능
            - 함수 기반이라 모듈화 편리함
        - 특히 리스트 구성에 있어서 간편해짐
            - XML + Adapter + ViewHolder -> 하나의 함수로 대체
        - 컴파일러 최적화 + 재구성 효율적 (Recomposition)
        - Material3 지원, 코드 내에서 테마 적용 가능
        - 실시간 미리보기 지원
        - remember, mutableStateOf, State 이용한 상태 업데이트
        - animateAsState, updateTransition 등으로 애니매이션 처리 간결

- StateIn()
    - 개요
        - Flow를 StateFlow로 변환해서 항상 최신 값을 보관하고, 구독자가 없어도 유지되게 만드는 연산자
        - 즉, Flow가 기본적으로 가지고 있지 않은 현재 상태값을 항상 보관하는 능력을 추가해주는 것

    - 사용 시점
        - UI 상태를 Flow로 관리하고 싶은데, StateFlow처럼 현재 값을 바로 가져오고 싶을 때
        - 예: 컴포즈에서 collectAsState() 사용하려면 StateFlow여야 함

    - 컴포즈 예시
        ```java
        @Composable
        fun UserScreen(viewModel: UserViewModel) {
            val users by viewModel.userList.collectAsState() // StateFlow여야 함
            LazyColumn {
                items(users) { user -> Text(user.name) }
            }
        }
        ```

    - 기본 문법
        - scope: 값을 유지할 코루틴 범위 (viewModelScope, lifecycleScope 등)
        - started: Flow 공유 조건 (WhileSubscribed, Eagerly, Lazily)
        - initialValue: 초기 상태값 (StateFlow의 value)
        ```java
        val stateFlow = myFlow
            .stateIn(
                scope = viewModelScope, // CoroutineScope
                started = SharingStarted.WhileSubscribed(5000), // 공유 시작 조건
                initialValue = emptyList() // 초기 값
            )
        ```
    - SharingStarted 종류
        - WhileSubscibed(timeout): 구독자가 있으면 시작 / 없으면 timeout 후 정지
        - Eagerly: scope 진입과 동시에 실행
        - Lazily: 첫 구독자가 있을 때 실행

    - 정리
        - Flow + 상태 보존 = StateFlow
        - UI와 상태 동기화 시 필수
        - collectAsState() 사용 시 핵심 연산자
        - 구독 여부에 따라 실행 제어 가능 (SharingStarted)

- Android에서 ViewModel과 SavedStateHandle의 차이점
    - 개요
        - 둘 다 안드로이드에서 UI 상태를 유지하기 위해 사용되는 도구지만, 목적과 역할, 생명주기, 저장 범위에 차이가 존재
    - 정의
        - 뷰모델
            - 화면 상태(리스트, 로딩여부 등)을 메모리 내에서 오래 유지하도록 설계된 클래스
            - 화면 회전해도 살아 있고, 비즈니스 로직/비동기 처리에 최적
        - SavedStateHandle
            - Bundle 처럼 값을 저장했다가 프로세스가 죽고 재생성될 때 자동 복원되는 상태 저장소
            - 뷰모델 생성자에 주입되어 사용
            - 예제
                ```java
                // 앱이 강제 종료돼도 값 유지됨 (onSaveInstanceState 와 유사)
                class MyViewModel(
                    private val state: SavedStateHandle
                ) : ViewModel() {

                    companion object {
                        private const val KEY_COUNTER = "counter"
                    }

                    var counter: Int
                        get() = state.get<Int>(KEY_COUNTER) ?: 0
                        set(value) {
                            state.set(KEY_COUNTER, value)
                        }

                    fun increase() {
                        counter += 1
                    }
                }
                ```
    - 뷰모델 + SavedStateHandle 함께 쓰는 패턴
        - Navigation Component에서 전달된 파라미터를 자동으로 SavedStateHandle로 받아서 복구 가능하게 함
        - 보통 둘을 같이 사용하는 경우가 많음
        ```java
        class DetailViewModel(
            savedStateHandle: SavedStateHandle
        ) : ViewModel() {
            val userId = savedStateHandle.get<String>("userId")
        }
        ```
    - 사용 시점에 따른 선택 기준
        - 일반적인 UI 상태 유지(회전, 탭 전환 등): 뷰모델
        - 시스템이 앱을 죽였다가 복원할 수 있는 상황: SavedStateHandle
        - 인텐트로 전달된 값 기억해야 할 때: SavedStateHandle
        - API 호출, 비즈니스 로직 상태 관리: 뷰모델

- Android에서 Kotlin Coroutines 실제 내부 동작 원리
    - 개요
        - 경량 스레드처럼 작동하는 코틀린의 비동기 프로그래밍 도구
        - 쓰레드보다 가볍고 효율적
        - suspend, launch, async, withContext 같은 키워드로 사용
        - ViewModel, LiveData, Flow, Room, Retrofit 등과 쉽게 결합 가능
        - 실제로는 스레드를 생성하지 않고, 상태(State machine)와 컨티뉴에이션(continuation)으로 구성된 구조   

    - suspend 키워드 의미
        - 일시 중단 가능하고, 중단된 시점부터 다시 이어서 실행할 수 있는 함수 의미
        - 컴파일 시점에 이 함수는 상태 머신으로 변환됨

    - 코루틴 핵심 (Continuation, 컨티뉴에이션)
        - 코루틴이 중단된 이후에 어떤 동작을 해야 하는지 담고 있는 객체
        - 즉, 코루틴의 실행 상태와 다음 단계를 기억하고 있음
        - 컴파일러는 suspend 내 코드를 상태 머신으로 변경
        - 코루틴은 resume 가능한 함수 호출 객체가 됨

    - CoroutineContext
        - 모든 코루틴은 CoroutineContext를 가지고 실행됨
        - 주요 구성 요소
            - Job: 코루틴의 생명주기 관리 (취소, 완료 등)
            - CoroutineDispatcher: 코루틴이 실행될 쓰레드 결정 (Main, IO)
            - CoroutineName: 디버깅용 이름 설정
            - CoroutineExceptionHandler: 에러 핸들링

    - Dispatcher
        - Dispatchers.IO
            - 내부적으로는 코틀린이 관리하는 공유 스레드 풀에서 실행됨
            - Default는 CPU 코어 수 * 64개의 스레드를 사용
        - 코루틴은 스레드를 직접 만들지 않고, 디스패쳐의 큐에 잡을 넣고 스케쥴링이 가능해질 때 마다 실행되는 구조

    - 코루틴의 시작과 중단
        - 시작
            ```java
            viewModelScope.launch {
                val result = fetch()
            }
            // launch는 CoroutineStart.DEFAULT 상태로 생성
            // fetch()는 suspend라서 내부적으로 Continuation을 생성하고,
            // 실제 실행은 Dispatcher에 의해 스케줄링됨
            ```

        - 중단 (suspend)
            - suspend 함수 내에서 중단 지점이 있으면 현재까지의 상태와 다음 동작을 Continuation에 저장.
            - 스레드를 점유하지 않고 반환
            - 나중에 resume() 되면 저장된 지점부터 재개

    - 가벼움의 비밀: 스레드 점유 안 함이 핵심
        ```java
        suspend fun download() {
            val result = apiCall()   // 중단 지점
            show(result)
        }
        // apiCall() 중에는 스레드를 점유하지 않음
        // 응답이 오면 → Continuation.resume(result) 호출 → 다음 단계 실행
        // → 이런 방식으로 수천 개의 코루틴이 동시에 살아 있을 수 있음
        ```

    - 최종 정리: 코루틴 작동 플로우
        ```
        [launch]
        ↓
        [CoroutineContext + Dispatcher → 스레드 결정]
        ↓
        [suspend 함수 → 컴파일러가 상태머신 생성]
        ↓
        [중단되면 → Continuation 저장 + 스레드 반환]
        ↓
        [재개되면 → 저장된 상태에서 resume()]
        ↓
        [최종 완료 또는 예외 처리]
        ```

    - (참고) suspendCoroutine {} 내부 구조
        - 직접 suspend 함수 구현하는 방법
            ```java
            suspend fun suspendExample(): String = suspendCoroutine { continuation ->
                Thread {
                    Thread.sleep(1000)
                    continuation.resume("완료")
                }.start()
            }
            // suspendCoroutine은 Continuation을 개발자가 직접 다룰 수 있게 해주는 도구
            ```

- Android에서 Room Database와 SQLite의 차이점
    - 개요
        - SQLite는 로우레벨 API, Room은 SQLite를 추상화한 고급 Wrapper이자 ORM(Object-Relational Mapping)
        - 모두 안드로이드에서 로컬 데이터 저장을 위한 도구이지만, 개발 생산성, 안정성, 유지보수성 측면에서 큰 차이 존재
    
    - 핵심 차이 비교
        - 사용방식: rawQuery, execSQL / @Dao, @Entity, @Query 등 애노테이션 기반
        - 타입 안정성: 없음 (런타임 에러 가능) / 컴파일 시 쿼리 검증
        - ORM 기능: 수동으로 Cursor -> Object 매핑 필요 / 자동으로 객체 매핑 지원
        - LiveData / Flow: Room은 지원

    - Room 장점
        - 컴파일 타임에 SQL 검증 (쿼리 오류를 빌드 시 감지 가능)
        - 객체 매핑 자동화 (Cursor 핸들링 불필요)
        - 코루틴, LiveData, Flow 지원 (비동기 작업 구조화 가능)
        - 마이그레이션 유틸 제공 (DB 스키마 변경 처리 가능)
        - Jetpack과 연계 용이 (ViewModel, Repository 패턴에 최적화)

    - 결론 요약
        - SQLite는 강력하나 로우레벨, 귀찮고 오류 발생 가능성 높음
        - Room은 SQLite 위에 만든 Jetpack ORM으로, 생산성/안정성/테스트/확장성 모두 좋음
        - 현 시점은 대부분 Room 사용

- Android에서 Data Binding을 사용하는 이유
    - 개요
        - UI와 데이터(또는 뷰모델)를 더 깔끔하고 효율적으로 연결하기 위해서임
        - XML 레이아웃에서 직접 뷰모델 및 데이터에 접근해 UI를 자동으로 갱신하게 해주는 기능

    - 사용의 이유
        - UI와 데이터 간 연결 코드 감소
            - findViewById 없이도 XML에서 직접 데이터를 바인딩
            - 클릭 리스너도 XML에서 바로 연결 가능
        - 자동 UI 업데이트 (양방향 바인딩도 가능)
            - 뷰모델의 라이브데이터 값이 바뀌면 UI도 자동 반영
            - 데이터가 바뀌면 UI가 자동 업데이트되므로 notifyDataSetChanged() 불필요
        - XML 에서 로직 표현 가능 (삼항 연산자 / 조건문 / 포맷팅 등)
        - MVVM 구조와 어울림
            - 뷰는 XML에서 관찰만 하면 됨
            - 액티비티 / 프래그먼트가 로직에서 자유로워짐 (UI만 담당)
        - Click 리스너, 아답터 설정도 XML 에서 처리 가능

    - 뷰 바인딩과의 차이
        - 뷰 바인딩
            - 단순 findViewById() 대체
            - XML 직접 바인딩 불가
            - 성능 가벼움
            - MVVM 연계 제한적
        - 데이터 바인딩
            - 데이터 바인딩 + 표현식 지원
            - XML 직접 바인딩 가능
            - MVVM 연계 매우 적합
            - 성능 약간 무거움 (컴파일 시 코드 생성됨)

    - 결론
        - 데이터 바인딩은 UI와 데이터를 선언적으로 연결시켜주는 도구
        - 코드량 줄이고, MVVM 구조에서 UI-로직 분리에 최적
        - 라이브데이터, 뷰모델과 결합 시 자동 UI 업데이트 가능
        - 실무 시 중/대형 앱, MVVM 구조, 재사용성 고려 시 매우 유용

- Android에서 Shared Preferences보다 Encrypted Shared Preferences가 필요한 이유
    - 개요
        - EncryptedSharedPreferences는 내부 데이터를 자동으로 암호화하여 저장하는 보안 강화된 버전
        - 로그인 정보, 토큰, 설정 등 민감 데이터 저장 시에는 반드시 사용 필수

    - 주요 차이점
        - AES 암호화된 상태로 저장
        - 보안 수준 높음 (키 스토어 기반 키 암호화)
        - 데이터 유출 위험 낮음
        - 비밀번호, 토큰, 사용자 정보 등 민감 데이터에 사용
        - API 23+ (마시멜로 이상) 부터 사용 가능

    - 필요 이유
        - SharedPreferences의 경우 /data/data/../shared_prefs/*.xml 파일에 평문 그대로 저장되어 있음
        - 루팅 기기 등 도구로 쉽게 열람 가능
        - 자동 암호화 + 복호화 시스템
        - 내부적으로 AES + GCM 방식으로 암호화 (안드로이드 키스토어 기반 키 관리)
        - 키는 키스토어에서 관리되어 앱 외부에서 접근 불가
        - 저장 파일 자체도 암호화되어 있어 디바이스 외부에서 노출돼도 안전
        - MasterKey + Keystore로 키 관리까지 안전

- Android에서 Jetpack Paging 라이브러리
    - 개념
        - Jetpack Paging은 대량의 데이터를 페이징 처리하면서 메모리와 네트워크 자원을 효율적으로 관리해주는 라이브러리
        - RecyclerView 등과 결합해 스크롤할 때 필요한 만큼만 데이터를 로드하도록 도와줌
        - PagingDataAdapter, PagingSource, RemoteMediator 등의 컴포넌트로 구성

    - 사용하는 이유
        - 메모리 최적화: 수천 건의 데이터를 한 번에 메모리에 올리지 않고 필요한 만큼만 로드
        - UI 성능 유지:	RecyclerView 스크롤 중 성능 저하 방지
        - 자동 리프레시 지원: 데이터 소스 변경 시 자동 갱신
        - Room, Retrofit 연동: 로컬 + 네트워크 데이터 흐름을 통합해서 관리 가능
        - 생명주기 대응: LiveData/Flow와 연동해 안전하게 동작함

    - 예제
        ```java
        // 페이저 생성
        val pager = Pager(
            config = PagingConfig(pageSize = 20),
            pagingSourceFactory = { MyPagingSource() }
        ).flow
        
        // PagingDataAdapter와 연결하여 RecyclerView에 연결
        lifecycleScope.launch {
            viewModel.pagingFlow.collectLatest {
                adapter.submitData(it)
            }
        }
        ```

- Android에서 Dependency Injection을 구현하는 방법
    - 개념
        - 객체가 의존하는 개첵를 외부에서 주입하는 설계 패턴
        - 클래스 간 결합도를 줄이고 테스트/유지보수를 쉽게 하는 효과

    - 구현 방식
        - 수동 주입: 생성자 또는 Setter 통해 직접 주입
        - Service Locator: 컨테이너에서 의존 객체를 찾아 사용
        - Dagger / Hilt: 컴파일 타임 의존성 주입 (정적 DI)
        - Koin / Kodein: 런타임 의존성 주입 (동적 DI)

    - DI를 사용하는 이유
        - 유연성 향상: 클래스 내부에서 객체를 생성하지 않음
        - 테스트 용이: Mock 객체 주입이 쉬움
        - 유지보수 쉬움: 컴포넌트 간 결합도 낮아짐
        - 구조적 설계 유도: 계층화된 아키텍쳐 구현에 필수

- Android에서 Hilt와 Dagger의 차이점
    - 개요
        - Hilt는 Dagger를 쉽게 쓰게 도와주는 안드로이드 특화 자동화 DI 프레임워크

    - 설치 복잡도
        - Hilt: 간단(애노테이션 기반)
        - Dagger2: 복잡 (Component, Module 수동 생성 필요)
    - 기본 DI 구조
        - Hilt: 자동 구성 (기본 AppComponent 제공)
        - Dagger2: 수동 구성 (Component 직접 정의)
    - Android 지원 (생명주기)
        - Hilt: Android 의존성 생명주기 자동 대응
        - Dagger2: 수동으로 @Component.Builder 등 관리
    - ViewModel DI
        - Hilt: @HiltViewModel로 자동 지원
        - Dagger2: 별도 ViewModelFactory 작성 필요
    - 테스트 지원
        - Hilt: 테스트 환경 자동 분리 가능
        - Dagger2: 직접 testComponent 만들어야 함
    - 커스터마이징
        - Hilt: 제약 (자동 구성 제한 있음)
        - Dagger2: 자유도 높음 (고급 사용자 용)

- Android에서 WorkManager와 JobScheduler의 차이점
    - 개요
        - 둘 다 백그라운드에서 일정 조건이 충족될 때 작업을 수행하기 위한 프레임워크
        - 사용 목적, 지원 범위, 신뢰성 영역에서의 차이점

    - WorkManager
        - API 14이상 지원 (내부적으로 fallback)
        - Jetpack 라이브러리, AndroidX 라이브러리, 최신 앱 적합
        - Doze Mode, App Standby, 백그라운드 제한에서도 동작 보장
        - 자동 fallback: API 23이상은 JobScheduler, 이하에서는 AlarmManager + BroadcastReceiver 자동 사용
        - 반복 작업 지원은 PeriodicWorkRequest
        - 체이닝 기능 존재: 작업을 순서대로 연결 가능 (WorkManager.beginWith(...))
        - Data 객체로 입출력 데이터 교환 / 전달
        - 앱 재부팅후에도 유지: setPersisted(true) 가능 (단, 기본은 false)
        - 테스트 쉬움 (Worker 클래스 단위 테스트 가능)
        - 재부팅 이후에도 가능 (작업 보존)

    - JobScheduler
        - 안드로이드 기본 내장 스케쥴러 (Android 5.0 (API 21) 이상에서 사용 가능)
        - 네트워크, 충전 중, 유휴 시간 등 조건 설정 (조건 기반 실행)
        - 시스템 제어 기반 (시스템 리소스 최적화를 위한 작업 스케쥴링)
        - 반복 작업: setPeriodic()
        - API 21 이상만 지원, 체이닝 안됨, 기능 제한적
            - 체이닝 / 병렬처리는 지원하지 않고 직접 구현 필요
        - 백그라운드 제약 회피는 불가능
        - 시스템 통합돼 있어 안정성 높음
        - 작업 보존 가능
        - Legacy Code 유지 시에나 커널 레벨 제어가 필요한 경우에만 고려

- Android에서 CameraX와 기존 Camera API의 차이점
    - 개요
        - 모두 안드로이드 기기의 카메라 기능 활용하는 API
    
    - 코드 예시
        - CameraX
            ```java
            val cameraProvider = context.getCameraProvider()
            val preview = Preview.Builder().build().also {
                it.setSurfaceProvider(previewView.surfaceProvider)
            }
            val imageCapture = ImageCapture.Builder().build()

            cameraProvider.bindToLifecycle(this, CameraSelector.DEFAULT_BACK_CAMERA, preview, imageCapture)
            ```
        - Camera2
            ```java
            val cameraManager = getSystemService(Context.CAMERA_SERVICE) as CameraManager
            cameraManager.openCamera(cameraId, cameraCallback, handler)
            // 이후 세션 구성, request 설정, surface 연결 등 복잡한 처리 필요
            ```

    - 전체 요약
        - 라이프사이클 자동 관리, UseCase 방식, 최신 프로젝트 > CameraX
        - 고급 설정이나 특정 기능 필요할 때 > Camera2 API

- Android에서 ViewBinding과 DataBinding의 차이점
    - 개요
        - 두 바인딩 타입 모두 XML 레이아웃과 코틀린/자바 코드 간의 연결 즉, 바인딩을 쉽게 해주는 기능
        - Null safe한 뷰 참조 (findViewById()없이 타입 안전하게 뷰 접근)
        - 뷰 아이디 자동 생성 (XML의 아이디가 자동으로 클래스에 생성됨)
        - XML > 코드 연결 (레이아웃과 액티비티/프래그먼트 연결 가능)

    - 뷰바인딩 (ViewBinding)
        - 뷰 참조 특화 (데이터 표현 목적 아님)
        - 타입 안전, 널 세이프
        - 양방향 바인딩 불가 (@={}문법 불가능), 즉 XML에서 데이터 참조 불가능
        - Observable/LiveData 연동 안됨, 직접 observe() 필요
        - 데이터바인딩보다 가볍고 빠름 (빌드 속도 빠름)
        - 코드 생성 위해서는 binding = ActivityMainBinding.inflate(layoutInflater) 등 방식으로 명시적 호출 필요 
            ```java
            val binding = ActivityMainBinding.inflate(layoutInflater)
            binding.textView.text = "Hello ViewBinding"
            ```

    - 데이터바인딩 (DataBinding)
        - LiveData, Observable 등과 자동 바인딩 가능 즉, XML 에서 데이터 참조 가능
        - 양방향 바인딩 지원, @={user.name} 표현 가능 즉, XML 에서 데이터 참조 가능
        - 뷰모델 연계 (MVVM)
        - annotation 프로세싱으로 무거움, 빌드 속도 상대적으로 느림
        - 잘못된 바인딩 식은 빌드 시 체크 어려움 (실수 발생 시 런타임 에러 가능성 존재)
            ```java
            <data>
                <variable name="viewModel" type="com.example.MyViewModel" />
            </data>
            <TextView android:text="@{viewModel.userName}" />

            binding.viewModel = myViewModel
            binding.lifecycleOwner = this
            ```

    - 단순 정리
        - 코드에서 단순 UI 구성 및 참조 > 뷰바인딩
            - Code <- XML
        - MVVM + LiveData + 양방향 바인딩 필요 > 데이터바인딩
            - Code <-> XML

- Android에서 Parcelable과 Serializable의 차이점
    - 개요
        - 둘 다 객체를 직렬화해서 다른 컴포넌트(액티비티, 서비스 등) 간 전달할 수 있게 함

    - Serializable (Java 표준)
        - 자바 표준 인터페이스
        - 구현 쉬움, 코드 작성 거의 없음
        - 성능 낮음, 내부 적으로 리플렉션 기반으로 느림, 객체 크기도 큼
        - 안드로이드 최적화 X (GC 부하 크며, 안드로이드에서는 비추천)
        - 버전간 충돌 가능성 존재

    - Parcelable (Android 특화)
        - 안드로이드 전용 인터페이스 (안드로이드에 최적화)
        - Parcel 객체를 통해 바이너리로 직접 기록하므로 빠름 (직접 바이트 변환)
        - 구현 코드 많음 (writeToParcel, CREATOR 구현 필요)
        - 코틀린에서는 @Parcelize로 간단하게 처리 가능
            ```java
            @Parcelize
            data class User(val name: String) : Parcelable
            ```
        - 안정성 높음 (명시적 구조)

- Media Player 자체 내부
    - 구조 개요
        - MediaPlayer는 안드로이드 OS에서 제공하는 Native 기반의 기본 미디어 플레이어
        - 내부적으로는 C/C++로 구현된 Stagefright 또는 NuPlayer (MediaCodec 기반) 를 사용해 미디어 디코딩과 렌더링을 처리

    - 내부 처리 흐름
        - (1) Java Layer (android.media.MediaPlayer)
            - 앱 개발자가 사용하는 API (e.g., setDataSource(), prepare(), start() 등)
            - JNI를 통해 Native Layer와 통신

        - (2) JNI Layer (android_media_MediaPlayer.cpp)
            - Java ↔ C++ 통신을 위한 인터페이스
            - MediaPlayerService에 명령을 전달

        - (3) Native Layer (MediaPlayerService, AudioFlinger, SurfaceFlinger)
            - MediaPlayerService: 전체 플레이어 로직을 담당
            - NuPlayer 또는 Stagefright로 미디어 디코딩 수행
            - AudioFlinger: 오디오 출력 처리
            - SurfaceFlinger: 비디오 렌더링 처리

        - (4) Codec Layer (MediaCodec / HW codec)
            - 하드웨어 디코더를 사용하거나, 필요 시 소프트웨어 디코더를 사용
            - MP4, H.264, AAC 등의 기본 포맷 지원

    - 특징
        - 단순한 로직과 사용법
        - 버퍼링, DASH, DRM 등 확장성 부족
        - 스트리밍 최적화는 부족

- ExoPlayer 내부 구조
    - 구조 개요
        - ExoPlayer는 구글이 직접 개발한 모듈형 플레이어
        - MediaPlayer보다 유연하고 확장 가능
        - 앱 프로세스 내에서 실행되며, 모든 구성 요소가 Java/Kotlin으로 구성되어 있음.

    - 주요 컴포넌트
        - (1) ExoPlayer
            - 플레이어 컨트롤러 역할 (prepare, play, seek 등)
            - 각 MediaComponent들을 제어

        - (2) Renderers
            - VideoRenderer, AudioRenderer, TextRenderer
            - MediaCodec 또는 FFmpeg 등을 사용해 디코딩한 데이터를 실제 출력

        - (3) SampleStream / SampleQueue
            - 디코딩 전 압축 스트림을 제공 (MediaSource → Renderer로 전달)

        - (4) MediaSource
            - MP4, HLS, DASH, SmoothStreaming 등 다양한 형식 지원
            - Timeline, TrackGroup 등 관리

        - (5) Extractor
            - MP4, TS, WebM 등의 컨테이너를 파싱하여 Raw Sample 추출

        - (6) Loaders & LoadControl
            - 버퍼링, 데이터 로딩, 네트워크 제어

    - 특징
        - 스트리밍(DASH, HLS, SS 등) 완벽 지원
        - DRM, 오디오 트랙 선택, 자막 등 유연한 지원
        - 라이브 스트리밍이나 광고 삽입에 최적화

- FFMpegPlayer 내부 구조
    - 구조 개요
        - FFmpegPlayer는 FFmpeg 라이브러리를 기반으로 직접 미디어 디코딩과 처리를 수행하는 플레이어
        - FFmpeg는 강력한 디코딩/인코딩/포맷 변환 엔진이며, 거의 모든 미디어 포맷을 지원함.
        - 주의: FFmpeg는 공식적으로 안드로이드에서 지원되지 않기 때문에 JNI로 직접 빌드하고 바인딩해야 함.

    - 처리 흐름
        - (1) Java Layer
            - 플레이어 API 정의 (e.g., play, pause, seek, release)
            - JNI를 통해 C/C++의 FFmpeg 함수 호출

        - (2) JNI Layer
            - FFmpeg 초기화 및 함수 호출 브릿지 역할
            - Java ↔ Native 데이터 변환 처리

        - (3) FFmpeg Core
            - avformat_open_input(): 포맷 열기
            - avformat_find_stream_info(): 스트림 정보 파싱
            - avcodec_find_decoder(): 코덱 찾기
            - av_read_frame(): 패킷 읽기
            - avcodec_send_packet() / avcodec_receive_frame(): 디코딩
            - sws_scale() / swr_convert(): 영상/음성 변환

        - (4) Renderer
            - 디코딩된 프레임을 OpenGL 또는 Android Surface로 렌더링
            - 오디오는 OpenSL ES 또는 AudioTrack API를 통해 출력

    - 특징
        - 거의 모든 포맷, 코덱 지원 (MKV, FLAC, RMVB, HEVC 등)
        - 자체 디코딩으로 MediaCodec 의존 없음
        - 스트리밍, 변환, 필터 등 고급 기능 지원 가능
        - 단점: 무겁고 복잡, HW 가속 부재, 배터리 소모 높음

    - 안드로이드 플레이어 항목별 요약
        - 디코딩 방식	
            - MediaPlayer: HW 중심 (MediaCodec)
            - ExoPlayer: HW + SW 지원	
            - FFmpegPlayer: 완전 SW 디코딩 (FFmpeg 기반)
        - 스트리밍 지원			
            - MediaPlayer: 제한적 (HLS만 간단 지원)
            - ExoPlayer: HLS, DASH, SmoothStreaming 완벽
            - FFmpegPlayer: 가능하지만 구현 난이도 높음
        - 포맷 지원 범위			
            - MediaPlayer: 제한적 (기본 포맷만)
            - ExoPlayer: 다양한 컨테이너 + 코덱 지원
            - FFmpegPlayer: 거의 모든 포맷/코덱 지원
        - 커스터마이징			
            - MediaPlayer: 불가능에 가까움
            - ExoPlayer: 매우 유연함 (모듈화 구조)
            - FFmpegPlayer: 자유롭지만 직접 구현 필요
        - 성능/배터리			
            - MediaPlayer: 우수 (HW 가속)
            - ExoPlayer: 우수 (선택적 HW 가속)
            - FFmpegPlayer: 낮음 (CPU 사용량 높음)

- Android에서 Kotlin을 기본 언어로 채택한 이유
    - 간결한 문법과 높은 생산성
    - Null 안정성 내장
    - 완벽한 자바 호환성
    - 구글의 공식 지원과 안드로이드 스튜디오 통합
    - 코루틴을 통한 비동기 처리의 간결화
    - 모던 언어 (함수형, DSL)
    - Jetpack Compose 중심의 개발 패러다임 변화
        - Declarative UI 구조와 Kotlin DSL 문법의 조화

- Android의 Application Class 정의와 활용 방법
    - 정의
        - 안드로이드 앱의 전체 라이프사이클에서 가장 먼저 실행되고 가장 오래 살아있는 객체
        - 앱 프로세스가 시작될 때 단 한번 생성되며, 앱이 종료될 때까지 유지
        - 기본적으로 android.app.Application 클래스를 상속하여 커스터마이징 가능

    - 사용 목적 및 활용 방법
        - (1) 글로벌 컨텍스트 제공
            - Context가 필요한 객체 (Repository, DB 등)에 안전하게 전달할 수 있는 앱 전역 Context
            ```kotlin
            val appContext = applicationContext // 어디서든 접근 가능
            ```
        - (2) 전역 변수 저장
            - 앱 전체에서 공유해야 하는 값(예: 로그인 유저 정보, 설정값 등)을 저장
        - (3) 초기화 작업 수행
            - 앱이 시작될 때 한번만 수행해야 하는 초기화 작업 (Firebase, DI 설정, Logger 등)
        - (4) DI(Container) or Singleton 관리
            - Hilt, Dagger, Koin 같은 DI 프레임워크 설정 시 활용됨
        - (5) Custom Crash Handling
            - 전역 에러 핸들링용 UncaughtExceptionHandler 설정 가능
            ```kotlin
            Thread.setDefaultUncaughtExceptionHandler { thread, throwable ->
                // 로그 저장 및 재시작 로직 등
            }
            ```
    - 적용 방법
        - Application 클래스를 상속한 클래스를 정의
        - AndroidManifest.xml에 등록
    
    - 코드 주의
        - 메모리 누수 주의: Context를 정적 Static 변수로 저장하면 메모리 누수 위험 존재
        - 많은 초기화 작업은 App Start를 느리게 만들 수 있으니 비동기 처리 또는 최소화 필요
        - Application에 너무 많은 책임을 주면 유지보수가 어려워짐. 역할 분리 중요

- Android에서 Context의 역할과 종류 (ApplicationContext, ActivityContext 등)의 차이점
    - Context 정의와 역할
        - 안드로이드에서 애플리케이션의 전반적인 정보와 리소스, 시스템 서비스에 접근하기 위한 인터페이스이자 핵심 객체
        - 컴포넌트 간 연결고리 역할
        - 앱의 환경/상태/자원에 접근하는 핵심 도구

    - 주요 기능
        - 리소스 접근
        - 시스템 서비스 접근
        - 앱 컴포넌트 제어
        - 파일 / DB 접근
        - View 생성

    - Context 주요 종류 및 차이점
        - (1) ApplicationContext
            - Application 클래스에서 반환되는 전역 컨텍스트
            - 앱의 전체 생명주기와 함께 존재 (앱 실행 ~ 종료까지 살아있음)
            - 메모리 누수 위험 ↓ (Activity 종료와 무관)
            - 주로 오래 살아야 하는 객체, 싱글톤, 서비스 등에서 사용
            - 장기적인 리소스 접근에 적합하며 메모리 누수 위험 적음
            - 예: context.getApplicationContext()
            - 사용 예시:
                ```java
                val prefs = context.applicationContext.getSharedPreferences("settings", MODE_PRIVATE)
                ```
        - (2) ActivityContext
            - Activity 인스턴스 그 자체 (this 또는 MainActivity.this)
            - 해당 Activity의 생명주기와 동일 (Activity가 종료되면 함께 소멸)
            - UI 관련 작업에 최적화되어 있음, 생명주기 관리에 주의 필요
            - View를 inflate하거나 Dialog, Toast를 띄울 때 등 UI와 밀접한 작업에 적합
            - 메모리 누수 유의 (장기 보관 금지)
            - 사용 예시:
                ```java
                val inflater = LayoutInflater.from(this) // Activity context
                val view = inflater.inflate(R.layout.dialog_layout, null)
                ```

        - (3) ServiceContext
            - Service 내부에서 사용되는 Context
            - ApplicationContext와 유사하게 오래 지속됨
            - UI 관련 작업은 불가

        - (4) BroadcastReceiverContext (일회성)
            - BroadcastReceiver 내에서 사용되는 Context는 일시적
            - onReceive() 메서드 내에서만 유효 (함수 종료 시 사라짐)
            - 장기 실행 작업에는 Context 보관 금지

    - Context 사용 시 주의할 점 (메모리 누수 방지)
        - View 또는 Activity Context를 싱글톤에 보관
            - Singleton.context = activity.applicationContext
        - Handler 또는 콜백에서 Activity 참조 보관
            - WeakReference(activity)
        - Glide, Picasso 등의 이미지 라이브러리
            - Glide.with(activity).load()

- Android에서 ContentProvider의 역할과 사용 사례
    - 개요
        - 안드로이드의 4대 컴포넌트 중 하나이자 앱 간 데이터 공유를 담당하는 중요한 구조
    - 정의
        - 앱 간에 데이터를 안전하게 공유할 수 있도록 도와주는 컴포넌트
        - 데이터베이스, 파일, 네트워크 등 다양한 저장소를 추상화해 URI 기반으로 접근할 수 있게 해줌
        - 앱 외부에서도 데이터를 읽거나 쓸 수 있도록 표준화된 API 인터페이스 제공
            - query(), insert(), update(), delete() 등

    - ContentProvider의 주요 역할
        - 앱 간 데이터 공유: 앱 A의 데이터를 앱 B에서 안전하게 접근할 수 있도록 해줌
        - URI 기반 접근: content://authority/path/id 형태의 URI로 데이터를 식별하고 접근 가능
        - 권한 제어: android:exported, permission 속성 등으로 외부 접근 제어 가능
        - ContentResolver 연동: 클라이언트 측에서는 ContentResolver를 통해 데이터에 접근

    - 대표적인 시스템 ContentProvider
        - ContactsContract → 연락처
        - MediaStore → 사진, 동영상, 음악
        - CalendarContract → 일정
        - Settings.System → 시스템 설정 값
        ```kotlin
        val cursor = contentResolver.query(
            ContactsContract.Contacts.CONTENT_URI,
            null, null, null, null
        )
        ```
    - 커스텀 ContentProvider 사용 예
        - 회사 내 여러 앱이 공용 DB를 쓰는 경우
        - 한 앱에서 다른 앱의 데이터를 읽거나 업데이트해야 하는 경우
        - 플러그인 구조 앱에서 각 모듈 간 데이터를 표준 인터페이스로 주고받는 경우

    - 구현방법
        - (1) ContentProvider 상속 클래스 구현
        - (2) AndroidManifest.xml 에 등록
        - (3) 클라이언트 앱에서 ContentResolver 사용

    - 주의점
        - 보안 이슈: 민감한 데이터는 permission 설정 및 android:exported="false" 고려
        - 성능 이슈: 너무 큰 데이터는 파일이나 DB를 직접 공유하는 방식이 나을 수 있음
        - 앱 간 계약(Contract): URI path, 컬럼 명 등 명확한 설계 문서 필요

    - 결론
        - ContentProvider는 안드로이드에서 앱 간 데이터 공유를 표준화하고,URI + ContentResolver를 통해 데이터 접근을 안전하고 구조적으로 관리할 수 있게 도와주는 컴포넌트

- RecyclerView의 ViewHolder 패턴을 사용하는 이유와 성능 최적화 방법
    - ViewHolder 패턴
        - RecyclerView 에서 각 아이템 뷰의 참조를 저장해두는 객체
        - 뷰를 매번 findViewById()로 찾지 않고, 재활용 가능한 구조로 캐싱
        - 아답터 내에서 onCreateViewHolder()로 뷰 홀더를 생성하고, onBindViewHolder()로 데이터를 바인딩
            ```kotlin
            class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
                val titleText: TextView = itemView.findViewById(R.id.titleText)
            }
            ```

    - 뷰 홀더 패턴을 사용하는 이유
        - 뷰 재활용
            - RecyclerView는 스크롤 시 기존 뷰를 재사용하므로 메모리 절약 및 렌더링 효율 ↑
        - findViewById 반복 방지
            - ViewHolder에 뷰 참조를 캐싱해 매번 탐색하는 오버헤드를 제거
        - 성능 향상
            - 스크롤 성능, FPS 향상, GC 부담 감소 등 앱 전반의 UI 반응 속도 개선
        - 명확한 구조
            - 아이템 뷰 구성과 바인딩 로직을 분리해 코드 유지보수성 ↑

    - 성능 최적화 방법
        - (1) 뷰홀더 패턴 철저히 적용
            - findViewById()는 무조건 ViewHolder 내에서 한 번만 호출
            - ViewBinding 또는 DataBinding 사용 시 더 깔끔하게 처리 가능
            ```kotlin
            class MyViewHolder(private val binding: ItemMyBinding) :
                RecyclerView.ViewHolder(binding.root) {
                fun bind(item: MyItem) {
                    binding.title.text = item.title
                }
            }
            ```

        - (2) DiffUtil 사용
            - notifyDataSetChanged() 대신 DiffUtil로 변경된 항목만 업데이트
            - 성능과 배터리 효율 모두 크게 개선됨
            ```kotlin
            val diffCallback = object : DiffUtil.ItemCallback<MyItem>() {
                override fun areItemsTheSame(old: MyItem, new: MyItem): Boolean = old.id == new.id
                override fun areContentsTheSame(old: MyItem, new: MyItem): Boolean = old == new
            }
            ```

        - (3) Payload 활용 (부분 바인딩)
            - onBindViewHolder(holder, position, payloads) 활용 시 전체 바인딩이 아니라 변경된 부분만 바인딩 가능
            ```kotlin
            override fun onBindViewHolder(holder: MyViewHolder, position: Int, payloads: MutableList<Any>) {
                if (payloads.isEmpty()) {
                    super.onBindViewHolder(holder, position, payloads)
                } else {
                    // 부분 업데이트
                }
            }
            ```

        - (4) ViewType 분리
            - 여러 종류의 아이템 뷰가 있는 경우 getItemViewType()을 적절히 활용해서 재활용 혼선 방지

        - (5) Stable ID 사용
            - setHasStableIds(true) 및 getItemId() 재정의 -> View 상태(스크롤, 선택 등) 안정성 ↑

    - 부가적인 성능 팁
        - RecyclerView.setItemViewCacheSize() 조절로 캐시 최적화
        - View 안에 중첩된 복잡한 레이아웃은 ConstraintLayout 등으로 단순화
        - NestedScrolling 필요 시 NestedScrollView → RecyclerView 구조는 신중히 고려

    - 핵심 사항
        - ViewHolder 패턴은 RecyclerView의 핵심 성능 최적화 기법으로, 뷰 재활용 + 참조 캐싱 + 부분 업데이트를 통해 스크롤 성능과 메모리 효율을 극대화한다.

- Android에서 Handler, Looper, MessageQueue의 동작 원리
    - 등장 배경
        - Android는 기본적으로 UI 작업을 Main Thread (UI Thread)에서만 처리해야 함
        - 하지만 앱이 여러 스레드를 사용하면서도 안정적으로 메시지를 전달하거나 딜레이 실행할 수 있어야 하므로 이때 등장하는 구조가 Handler, Looper 그리고 MessageQueue
            - MessageQueue: 메시지를 저장하는 큐
            - Looper: 큐를 순회하며 메시지를 꺼내 처리하는 반복문
            - Handler: 메시지를 생성하거나 보내는 인터페이스

    - 구성 요소별 동작 원리
        - Looper
            - Thread마다 단 1개만 존재 가능 (prepare()로 생성)
            - 내부에 MessageQueue를 포함하고 있음
            - loop() 메서드를 통해 무한 루프를 돌며 메시지를 계속 꺼냄
            - (참고) 메인 스레드에서는 Android가 자동으로 Looper.prepareMainLooper()를 호출해줌.
                ```java
                val looper = Looper.myLooper() // 현재 스레드의 Looper
                Looper.prepare()  // 스레드에서 Looper 준비 (보통 MainThread는 자동 준비됨)
                Looper.loop()     // 무한 루프 돌면서 메시지 처리
                ```

        - MessageQueue
            - 메시지를 시간 순으로 저장하는 큐 구조
            - enqueueMessage()로 삽입되고, next()로 하나씩 꺼냄
            - 메시지가 없을 땐 Looper가 블로킹 상태로 대기함
            - 메시지에는 Handler, Runnable, what, arg1, arg2, obj 등이 포함됨

        - Handler
            - 특정 Looper를 기반으로 작동
            - sendMessage(), post() 등을 통해 메시지를 MessageQueue에 넣음
            - Looper가 메시지를 꺼내면 Handler.dispatchMessage()가 호출되고, → 직접 오버라이드하거나 handleMessage()를 구현해서 메시지 처리
            - (참고) post(Runnable)은 내부적으로 Runnable을 메시지로 감싸서 큐에 넣는 것과 같음.
                ```java
                val handler = object : Handler(Looper.getMainLooper()) {
                    override fun handleMessage(msg: Message) {
                        // 메시지 처리
                    }
                }

                // 메시지 보내기
                handler.sendMessage(Message.obtain().apply { what = 0 })
                ```

    - 전체 동작 흐름 요약
        ```scss
        - sendMessage/post > MessageQueue에 삽입 > Looper가 하나씩 추출 >  Handler.dispatchMessage() 호출 > handleMessage 호출됨
        Thread (MainThread or BackgroundThread)
            │
            ├─ Looper.prepare() → 현재 스레드에 MessageQueue 생성
            ├─ Looper.loop() → 메시지 대기 및 처리 시작
            │
            └─ Handler 생성 → 해당 Looper에 메시지 전송 (sendMessage/post)
                            ↓
                        MessageQueue에 메시지 저장
                            ↓
                    Looper가 하나씩 꺼내서 Handler로 전달
                            ↓
                    Handler.handleMessage()에서 처리됨
        ```

    - 실제 예: 딜레이 처리
        - 내부적으로는 MessageQueue에 미래시간(timestamp)을 가진 메시지를 넣고 Looper가 도달할 때까지 대기했다가 실행
    
    - 주의사항 & 메모리 누수 방지
        - Handler가 Activity의 내부 클래스일 경우, Activity의 참조를 암시적으로 잡고 있어 메모리 누수 가능성 있음 → WeakReference 또는 static + WeakReference 구조 추천

        - Looper.loop()는 무한 루프이므로 반드시 종료 조건이 있는 백그라운드 스레드에서는 사용 후 Looper.quit() 호출 필요

    - 요약 정리 문장
        - Handler, Looper, MessageQueue는 안드로이드에서 스레드 간 메시지 전달과 비동기 처리를 위한 핵심 구조입니다.
        - Handler는 메시지를 생성하고 큐에 넣는 역할
        - Looper는 큐를 돌며 메시지를 처리하는 루프
        - MessageQueue는 시간 순으로 메시지를 보관하며, 이 세 가지는 함께 동작하여 안정적인 UI/비동기 처리를 지원합니다.

- HandlerThread 개념 설명
    - HandlerThread 개념
        - HandlerThread는 Thread를 상속한 클래스로 내부에 Looper를 자동으로 생성해줘서, 해당 스레드에서 메시지 기반 비동기 작업을 처리할 수 있도록 해줘.
        - 즉, Thread + Looper + Handler의 복잡한 설정을 한 번에 해주는 스레드 전용 도우미 역할

    - 기본 개념
        - Thread: 별도의 백그라운드 스레드 생성
        - Looper: 메시지 루프를 돌면서 작업 대기
        - Handler: 메시지를 전달하여 해당 스레드에서 실행되도록 함

    - 사용 구조
        ```java
        // 1. HandlerThread 생성 및 시작
        val handlerThread = HandlerThread("MyBackgroundThread")
        handlerThread.start()

        // 2. Handler 생성 (Looper는 handlerThread의 것 사용)
        val backgroundHandler = Handler(handlerThread.looper)

        // 3. 작업 전송
        backgroundHandler.post {
            // 이 블록은 handlerThread 스레드에서 실행됨
            Log.d("MyApp", "Background task running on: ${Thread.currentThread().name}")
        }

        // 4. 종료 시
        handlerThread.quitSafely()
        ```

    - 내부 동작 흐름
        ```scss
        1. HandlerThread.start()
            └ Thread 실행 → Looper.prepare()
                                ↓
                            Looper.loop() 시작

            2. Handler(handlerThread.looper) 생성
            └ 해당 스레드의 MessageQueue에 작업 등록 가능

            3. handler.post { ... }
            └ 메시지가 MessageQueue에 들어감
                ↓
            Looper가 메시지를 꺼내서 해당 Runnable 실행
        ```

    - 실전 예제
        - 이미지 디코딩, 파일 I/O, 네트워크 요청 등
        ```java
        val decodeThread = HandlerThread("ImageDecodeThread")
        decodeThread.start()
        val decodeHandler = Handler(decodeThread.looper)

        // Coroutine withContext(Dispatchers.IO/Main)과 유사
        decodeHandler.post {
            val image = decodeHeavyBitmap("image_path.jpg")
            mainHandler.post {
                imageView.setImageBitmap(image)
            }
        }
        ```

    - 종료 함수
        - 무한 루프(Looper.loop())를 돌기 때문에 반드시 종료 필요
        - handlerThread.quitSafely() → 큐에 남은 메시지 처리 후 종료
        - handlerThread.quit() → 즉시 종료 (남은 메시지는 처리 안 함)

    - 정리
        - HandlerThread는 별도 스레드에서 Handler를 통한 메시지 기반 비동기 처리를 가능하게 하는 Android의 구조화된 백그라운드 스레드 클래스입니다.

- HandlerThread, Coroutine 비교
    - 개요
        - 핸들러 스레드, 코루틴 둘 다 모두 백그라운드에서 작업을 처리하는 도구

    - 사용 시점에 따른 성택
        - UI/프레임워크 레거시 연동 필요: HandlerThread
        - 간단한 백그라운드 작업: Coroutine
        - 복잡한 동기/비동기 혼합 흐름: Coroutine + suspend, 제어 흐름이 깔끔
        - 오래 지속되는 백그라운드 서비스 (예: 알람, 블루투스 처리)
            - 둘다 가능하나 Coroutine 선호, CoroutineScope + Lifecycle 연동이 유리
    
    - 실무 전략 정리
        - 새로운 프로젝트 or Kotlin 중심 앱이라면 → Coroutine 우선 사용
        - 레거시 시스템과 연동되거나 Android 프레임워크 API가 필요할 때 → HandlerThread
        - UI 바깥의 복잡한 순차/병렬 처리를 선언적으로 관리하고 싶다면 → Coroutine + withContext, async

- Jetpack Compose의 UI, 기존 View 시스템의 렌더링 방식 차이
    - 기존 View 시스템
        - 구조 및 렌더링 방식
            - UI는 XML 레이아웃 파일 또는 코드로 구성된 View 트리(View hierarchy) 기반
            - 트리 구조: ViewGroup > View들로 구성
                - 즉, UI 트리는 ViewGroup 기반 View 트리
            - 렌더링 과정
                - (1) inflate()로 XML을 파싱해 뷰 객체 생성
                - (2) measure() > layout() > draw() 3단계 렌더링 수행
                - (3) UI 갱신 시, 해당 뷰나 부모 뷰에서 invalidate() > requestLayout() 트리거
            - 상태 변경 시
                - 뷰 자체 또는 자식 뷰까지 갱신 (부분적으로 비효율적일 수 있음)
                - 구조가 복잡해질수록 리플로우 비용 증가
            - 요약
                - 명령형 방식 (Imperative UI)
                - 트리 구조가 무겁고 중첩될수록 성능 저하 가능
                - 렌더링 최적화는 개발자가 직접 관리해야 함

    - Jetpack Compose
        - 구조 및 렌더링 방식
            - UI는 @Composable 함수로 선언되는 컴포지션 트리(Composition Tree) 기반
                - UI 트리는 Composition Tree
            - 트리 구조는 RecompositionScope 단위로 관리
            - 렌더링 과정
                - (1) @Composable 함수 호출로 구성요소 트리(Composition Tree) 생성
                - (2) Compose Runtime이 상태를 관찰(State, MutableState), Compose Runtime이 성능 최적화 자동 관리
                - (3) 상태 변경 시 해당 범위만 Recomposition 발생
                - (4) 변경된 UI 요소만 Layout, Draw 재수행
            - 특징
                - 선언형 방식 (Declarative UI)
                - 상태 기반으로 UI 트리 자동 재구성
                - Diffing 및 Skipping 최적화 > 실제 변경된 UI만 업데이트
                - View 트리 없이 Android Canvas를 직접 활용하여 그려짐
            - 렌더링 최적화 요소
                - remember, derivedStateOf, key, LaunchedEffect 등으로 스코프 조절
                - Recomposer와 Snapshot 시스템이 UI 변경 추적 및 최소 렌더링을 보장

    - 결론
        - Jetpack Compose
            - 명령형 View 트리가 아닌 선언형 Composition Tree 기반으로 작동하며, 상태 변화에 따른 최소 범위의 Recomposition을 통해 성능을 자동 최적화
        - 기존 View System
            - ViewGroup 기반 트리 구조와 명령형 접근 방식으로 인해 복잡한 구조에서는 비효율적인 리렌더링이 발생할 수 있음, 종종 부모까지 리렌더링 영향 존재

- Jetpack Compose에서 Recomposition이 발생하는 원인
    - 개요
        - Compose는 선언형 UI 시스템이기 때문에, 상태(state)가 바뀌면 UI 트리를 다시 그리는 Recomposition이 자동으로 발생

    - Recomposition 개념
        - Recomposition은 @Composable 함수의 UI 트리를 다시 실행하여 변경된 상태를 반영하는 과정
            - Compose는 UI를 "상태에 따라 정의되는 함수"로 보고,
            - 상태가 바뀌면 해당 상태를 참조하고 있는 @Composable 함수만 부분적으로 다시 실행

    - Recomposition 발생 주요 원인
        - (1) State, MutableState, remember 등의 상태 값 변경
            - count++ > mutableState 변경됨
            - 이를 참조하는 Text()는 Recomposition 대상이 됨
            ```kotlin
            var count by remember { mutableStateOf(0) }

            Button(onClick = { count++ }) {
                Text("Clicked $count times")
            }
            ```
        
        - (2) remember 되지 않은 값이 계속 새로 생성되는 경우
            - remember 되지 않은 값 자체는 Recomposition을 유발하지는 않음
                - 그 자체가 UI를 바꾸는 데 사용되지 않으면 괜찮음
            - 그 값이 Composable 함수 호출 시 파라미터로 전달되거나 상태 추적의 대상이 될 때 발생
            - 아래 예에서 list는 매번 새로운 객체가 되기 때문에 Compose는 이전 list와 새 list가 다르다고 판단하고, LazyColumn 내부를 다시 리컴포지션하게 됨
            ```kotlin
            // (1) 리컴포지션이 계속 발생하는 예
            val list = List(100) { it } // 매 recomposition 시 새로 생성됨

            LazyColumn {
                items(list) { item -> Text("Item $item") }
            }

            // (2) remember로 캐싱 처리하여 해결한 예
            // remember 또는 rememberUpdatedState 사용으로 극복 가능
            @Composable
            fun Sample() {
                val list = remember { List(1000) { it } } // 한 번만 생성됨
                LazyColumn {
                    items(list) { item ->
                        Text("Item $item")
                    }
                }
            }
            ```

        - (3) 파라미터 값이 변경된 경우
            - 만약 아래 예에서 name이 변경되면, Greeting(name) 전체가 다시 리컴포지션 발생
            ```kotlin
            @Composable
            fun Greeting(name: String) {
                Text("Hello, $name")
            }
            ```

        - (4) derivedStateOf로 감싸지 않은 계산식의 불필요한 참조
            ```kotlin
            // 리컴포지션 발생 예
            val filtered = items.filter { it.isActive } // 매번 계산되면 무조건 recomposition

            // 해결 코드
            val filtered by remember(items) {
                derivedStateOf { items.filter { it.isActive } }
            }
            ```

        - (5) LaunchedEffect, SideEffect 등에서 key 값 변경
            ```kotlin
            LaunchedEffect(userId) {
                // userId가 바뀌면 내부 블록 다시 실행됨 (recomposition과는 다르지만 관련)
            }
            ```

    - Recomposition 최적화 방법 정리
        - remember: 불필요 객체 재생성 방지
        - derivedStateOf: 계산 비용 높은 상태값 캐싱
        - key(): 리스트 내 Composable의 고유성 유지
        - stable 객체 사용: 데이터 클래스나 람다 등은 가능하다면 > @Stable, @Immutable 애노테이션 작성 고려
        - Slot API: 필요에 따라 Composable 영역을 나누고 최소 범위만 갱신하도록 리팩토링 전개

- Android의 ProGuard와 R8의 차이점
    - 개요
        - ProGuard는 코드 축소/난독화 도구
        - R8은 이를 대체하는 차세대 통합 컴파일러 + 최적화 도구

    - 공통 기능
        - 코드 난독화: 클래스/메서드/변수명을 의미 없는 이름으로 치환
        - 코드 제거: 사용되지 않는 코드, 리소스를 빌드 시 제거 (Dead Code Elimination)
        - APK 최적화: 최종 빌드 크기 감소

    - ProGuard, R8(Android Studio 3.4+ 기본)
        - 개발주체
            - ProGuard: 외부(Guardsquare)
            - R8: Google (Android Gradle Plugin 내장)
        - 작동 시점
            - ProGuard: 컴파일 이후 별도 최적화 단계
            - R8: 컴파일과 동시에 최적화 (D8과 통합)
        - 성능
            - ProGuard: 상대적으로 느림
            - R8: 더 빠르고 강력한 최적화 수행
        - 리소스 제거
            - ProGuard: 별도 도구 필요
            - R8: 내장 (이미지, 문자열 등 사용 안하는 리소스 제거)
        - 규칙 파일
            - ProGuard: proguard-rules.pro
            - R8: 동일 파일 사용 (호환성 유지)
        - 난독화 수준
            - ProGuard: 기본 수준
            - R8: 더 정교하고 aggressive

    - 결론 및 정리
        - ProGuard는 예전 방식, 지금은 R8이 기본
        - R8은 D8(Dex Compiler)과 통합되어 성능 + 빌드 속도 + 최적화 모두 개선
        - proguard-rules.pro는 R8에서도 그대로 사용 가능

- Android의 ANR(Application Not Responding) 원인과 해결 방법
    - 정의
        - 앱이 UI 스레드(MainThread)에서 일정 시간 이상 응답하지 않으면 시스템이 강제로 표시하는 경고 다이얼로그

    - ANR 발생 기준 (조건 / 시간제한)
        - Input 이벤트 처리 지연: 5초 이상
        - BroadcastReceiver 실행 지연: 10초 이상
        - Service 실행 지연: 20초 이상(포그라운드) / 200초 이상(백그라운드, 3분 20초)

    - 발생 원인
        - MainThread에서 과도한 연산 수행
            - 예: 파일 다운로드, JSON 파싱, DB 쿼리 등
        - 무한 루프 또는 블로킹 함수 호출
            - while(true) {} or Thread.sleep()
        - 리소스 대기 중 블로킹	
            - synchronized 락 대기, deadlock
        - 느린 네트워크 요청
            - Retrofit, HttpURLConnection 등 동기 방식 호출
        - 브로드캐스트 처리 지연
            - BroadcastReceiver에서 무거운 작업 수행

    - 해결 방법
        - 메인 스레드에서 무거운 작업 제거	
            - Dispatchers.IO, AsyncTask(구), Coroutine, Executor 등 사용
        - 네트워크, DB, I/O 작업은 백그라운드로 변경
            - 비동기 처리 구조로 전환
        - StrictMode 활용
            - UI 스레드에서 잘못된 동기 호출 감지
        - Coroutine, LiveData, Flow, RxJava로 구조화
            - 반응형/비동기 구조 권장
        - 로그 분석	
            - logcat, traces.txt, bugreport 등으로 정확한 원인 파악

- Android의 Jetpack Navigation Component 사용 경험
    - 개요
        - Android Jetpack의 하나로, Fragment 간 이동, BackStack 관리, DeepLink 처리를 간단하고 안정적으로 구현할 수 있는 라이브러리

    - 사용 목적 및 장점
        - Navigation Graph 사용
            - 화면 흐름을 XML로 시각화 (디자인툴 + 코드 일관화)
        - Safe Args 지원
            - Fragment 간 인자 전달을 타입 안정성 있게 처리
        - BackStack 자동 관리
            - popBackStack() 등을 직접 쓰지 않아도 자동 처리
        - DeepLink 쉽게 처리
            - navArgs, <deepLink>로 URI 매핑
        - BottomNavigation, Drawer 통합
            - 탭 기반 화면 전환도 쉽게 구성 가능

    - 실무 활용
        - 다중 그래프 분리
            - 로그인, 메인, 설정 등 분리하면 유지보수에 유리
        - navigation() vs navigateUp()
            - 백버튼 커스터마이징 시 구분 필요
        - SafeArgs plugin 필수	
            - 타입 안정성 높은 인자 전달
        - 복잡한 인자 전달 → ViewModel 공유로 대체
            - 너무 큰 데이터는 navArgs 대신 ViewModel/DI 사용

- AIDL 개념
    - 개요
        - Android Interface Definition Language, AIDL
        - Android에서 다른 앱(또는 다른 프로세스)의 서비스와 통신하기 위한 인터페이스를 정의하는 언어

    - AIDL 필요성
        - 안드로이드는 앱마다 별도의 샌드박스안에서 동작함 > 서로 프로세스가 다름
        - 이 상황에서 메서드 호출 또는 데이터 교환을 하려면 IPC(Inter-Process Communication)가 필요

    - AIDL 구조
        - .aidl 파일 - 인터페이스 정의(func1, func2() 등)
        - AIDL 컴파일러가 자동 생성한 Stub 클래스
            ```java
            class MyService : Service() {
                // 서버 서비스에서 Stub을 구현하고
                private val binder = object : IMyService.Stub() {
                    override fun add(x: Int, y: Int): Int = x + y
                }

                override fun onBind(intent: Intent?): IBinder = binder
            }
            ```
        - Service에서 Stub을 구현하여 onBind()에서 반환
        - Client 앱에서 bindService() > 서비스 연결
            ```java
            bindService(
                Intent("com.example.aidl.MY_SERVICE").setPackage("com.example.server"),
                connection,
                Context.BIND_AUTO_CREATE
            )

            private var myService: IMyService? = null

            val connection = object : ServiceConnection {
                override fun onServiceConnected(name: ComponentName, service: IBinder) {
                    // 클라이언트에서 asInterface()로 바인딩
                    myService = IMyService.Stub.asInterface(service)
                    val result = myService?.add(3, 4)
                    Log.d("AIDL", "결과: $result")
                }

                override fun onServiceDisconnected(name: ComponentName) {
                    myService = null
                }
            }
            ```
    - 데이터 전달을 위한 규칙
        - 기본타입 가능
        - String, CharSequence 가능
        - 커스텀 객체 (MyObject): Parcelable로 정의, .aidl 생성 필요
        - List/Map 가능

    - AIDL 사용 시 정보
        - AIDL은 비동기식 아님: 메서드 호출 블로킹 가능성 > 별도 스레드에서 호출 권장
        - 앱 간 통신은 보안 중요: 권한 확인 필수 (checkPermission 등)
        - 버전 관리 어려움: AIDL 인터페이스 변경 시 호환성 관리 필요
            - 따라서 API 개발 완료 시점에 범용 API를 하나 더 두는 것도 방법
            - 추가 요구사항 발생 시 Bundle 타입으로 서버, 클라이언트 간 약속된 Key, Value만 설정해주면 통신 가능
        - Parcelable 구현 필수: 커스텀 객체는 반드시 Parcelable로 처리 필수

    - 사용 시점
        - 다른 앱 또는 다른 프로세스와의 통신
        - 하드웨어 제어, 시스템 API 구현 등

- HIDL 개념
    - 개요
        - Hardware Interface Definition Language, HIDL
        - Android에서 HAL(Hardware Abstraction Layer)과 Android 프레임워크 사이의 통신을 정의하는 AIDL의 하드웨어 버전
        - HW <> HAL <> HIDL <> Framework

    - 필요성
        - 안드로이드는 하드웨어와 OS 사이에 HAL이라는 추상 계층을 둠
        - 카메라, 오디오, 센서등 디바이스 의존적인 기능은 HAL을 통해 접근
        - 과거, C/C++로 HAL을 구현하면서 프레임워크와 직접 연결했지만, 버전관리, 안정성, 모듈화 문제 증가
            - 안드로이드 8.0(Oreo)부터 도입된 것이 HIDL

    - HIDL 역할
        - 안정적인 인터페이스 정의
            - HAL과 Android 시스템 간 통신을 정해진 방식으로 제한
        - HAL 모듈의 독립성 확보
            - HAL과 시스템 프레임워크가 별도 프로세스로 나뉘어 통신
        - VINTF(버전 독립 프레임워크) 지원
            - 버전 간 호환성 보장, 제조사가 시스템 업데이트와 독립적으로 HAL 제공 가능
        - AIDL 기반 고수준 프레임워크와 분리
            - 시스템 안정성 증가

    - HIDL 구조와 구성 요소
        - HIDL 인터페이스는 .hal 파일로 정의됨
            ```java
            package android.hardware.camera.provider@2.4;

            interface ICameraProvider {
                getCameraIdList() generates (vec<string> cameraDeviceNames);
            }
            ```
        
    - HIDL 기반 HAL 통신 흐름
        - Stub는 HAL 구현체와 통신
        - System은 HIDL 인터페이스만 바라보고 호출
        ```scss
        [ App Framework ]
            ↓
        [ Camera Service (Java/C++) ]
            ↓ (Binder IPC)
        [ HIDL Stub (C++) ]
            ↓
        [ HAL 구현체 (Vendor) ]
            ↓
        [ 하드웨어 드라이버 ]
        ```
        
    - HIDL 도입 효과 (Treble 기반)
        - 안드로이드 8 이후부터 시스템(OS)과 벤더(HAL) 영역을 분리
        - 하드웨어 추상화의 표준으로 도입 (Treble 아키텍쳐)
            - 시스템 업데이트는 구글이 책임
            - 벤더는 HAL만 업데이트 (HAL 구현은 C++로)
            - 제조사는 더 빠르게 업데이트 대응 가능 (프로젝트 트레블 목적)

    - 안드로이드 11+ 이후: HIDL > AIDL 전환 중
        - 안드로이드 11부터는 AIDL도 native 지원을 강화하면서,
        - 일부 HIDL 인터페이스를 AIDL로 대체하는 방향으로 전환되고 있음
        - 예: android.hardware.health

- Android Treble
    - 개요
        - 안드로이드의 프로젝트 Treble은 안드로이드 플랫폼 아키텍쳐를 완전히 바꿔버린 대형 프로젝트
        - OS 업데이트를 빠르게 만들기 위해, 구글이 안드로이드 8.0(Oreo)부터 도입한 핵심 기술
        - 안드로이드 시스템(OS)과 하드웨어 제조사(Vendor) 구현(HAL 등)을 명확히 분리해서, OS 업데이트 속도를 빠르게 만들기 위한 아키텍쳐 재설계 프로젝트

    - 도입 배경
        - 기존 안드로이드는 하드웨어와 OS가 강하게 결합
        - 시스템 업데이트 시 HAL도 같이 수정해야 하는 문제 발생
            - 이로 인해 제조사가 업데이트에 느리게 대응 또는 아예 안하는 경우 발생
            ```scss
            [ Android Framework ]
                ↕ tightly coupled
            [ HAL + Vendor Driver ]
            ```

    - Treble 구조
        - 안드로이드 프레임워크와 Vendor 구현사이에 명확한 인터페이스(VINTF) 삽입
        - 시스템 파티션과 벤더 파티션 완전 분리
        - 구글이 시스템을 업데이트해도 Vendor 구현은 그대로 유지 가능
            ```scss
            [ Android Framework (System partition) ]
                    ↓   ↑
                VINTF Interface (AIDL/HIDL)
                    ↓   ↑
            [ HAL / Vendor Implementation (Vendor partition) ]
            ```

    - 핵심 개념 재정리
        - VINTF (Vendor Interface)
            - Framework과 Vendor 간 호환을 위한 계약(Interface)
        - HIDL / AIDL
            - Framework ↔ HAL 간 IPC를 위한 인터페이스 정의 언어
        - System Partition
            - 구글/OS 업데이트 대상
        - Vendor Partition
            - 제조사 드라이버 및 HAL 구현 담당

    - Treble 도입의 효과
        - 시스템 업데이트 시 HAL도 수정 필요
            - -> 시스템 업데이트만 해도 HAL 그대로 사용 가능
        - 제조사별 맞춤 커널/드라이버로 인해 업데이트 지연
            - -> 커널과 드라이버는 고정, 시스템은 빠르게 교체 가능
        - AOSP 업데이트 후 실제 단말 적용까지 수개월~년 소요
            - -> 이론상 수주 내에 업데이트 가능

    - Treble 이후 변화
        - OS 모듈화
            - 시스템이 여러 개의 모듈로 나뉘어 OTA로 개별 업데이트 가능
        - 시스템 이미지 재사용
            - 하나의 시스템 이미지로 다양한 하드웨어에 이식 가능
        - 벤더 테스트 요구사항 도입 (VTS)
            - HAL이 시스템과 호환되는지 검증 자동화
        - GSI (Generic System Image)
            - 어떤 디바이스에도 올라가는 표준 시스템 이미지 제공
        - (GSI, VINTF, VTS 등 관련 도구/표준과 함께 동작)

    - 실제 시스템 업데이트 플로우 (Treble 적용)
        - (1) 구글이 AOSP 최신 버전 릴리즈
        - (2) 디바이스 제조사는 Vendor HAL은 그대로 유지
        - (3) 새 AOSP를 디바이스에 적용 > VINTF 체크 > 호환되면 바로 업데이트

- AOSP의 HAL(Hardware Abstraction Layer)
    - 개요
        - 안드로이드 프레임워크와 하드웨어 드라이버 사이를 연결해주는 중간 계층
        - 안드로이드 시스템이 하드웨어와 직접 맞닿지 않고도, 하드웨어 기능을 사용할 수 있게 해주는 중간 계층
        - 안드로이드 시스템이 하드웨어를 추상화하여 일관되게 접근할 수 있도록 해줌

    - HAL의 위치
        - 안드로이드 아키텍쳐 계층에서 HAL 구조
            - App → Framework → HAL → Driver 순으로 하드웨어 접근
            - HAL은 프레임워크가 하드웨어를 직접 몰라도 동작할 수 있게 함
            ```css
            [ Android App (Java/Kotlin) ]
                    ↓
            [ Android Framework (Java) ]
                    ↓
            [ JNI / Native C++ ]
                    ↓
            [ HAL (C/C++) ]
                    ↓
            [ 하드웨어 드라이버 / 커널 ]
            ```
    
    - HAL 사용 예시
        - 예: 카메라 기능
            - 앱에서 CameraManager 호출
            - 프레임워크에서 CameraService 동작
            - HAL 레이어의 camera_device 인터페이스 호출
            - 드라이버가 실제 카메라 하드웨어 제어

    - HAL 구성 방식 (Pre-Treble vs Treble+)
        - Android 7 이하 (Pre-Treble)
            - HAL은 .so 형태의 Shared Library
            - 프레임워크와 동일 프로세스에서 호출 → 강결합

        - Android 8 (Treble 도입 이후)
            - HAL은 Binder 기반 IPC 구조
            - 프레임워크와 다른 프로세스에서 동작
            - HIDL (→ Android 11 이후 AIDL로 점진 전환 중)

    - HAL 구현 프로세스 요약
        - .hal 또는 .aidl 인터페이스 정의
        - hidl-gen 또는 aidl-cpp로 Stub 코드 생성
        - 제조사가 실제 하드웨어 동작을 구현 (C/C++)
        - Android Framework는 이 인터페이스만 호출

- AOSP의 시스템 서비스(SystemService)
    - 개요
        - System Service는 AndroidOS의 중추 역할을 하는 핵심 시스템 컴포넌트
        - 안드로이드의 자바 프레임워크 레이어에서 OS기능을 제공하는 핵심 서비스로, 앱과 시스템이 하드웨어/리소스를 안전하고 일관되게 사용할 수 있도록 도와주는 역할

    - 안드로이드 아키텍쳐에서 SystemService 위치
        - 앱은 Context.getSystemService() 또는 Manager API를 통해 시스템 서비스를 호출
        - SystemService는 Java 기반의 OS 기능을 제공하며, 필요시 JNI로 Native 또는 HAL에 접근
            ```scss
            [ 앱 (Java/Kotlin) ]
                ↓ Binder
            [ SystemService (Java) ] ← Android Framework
                ↓ JNI
            [ Native Services (C++) ]
                ↓ HAL → 커널
            [ 하드웨어 ]
            ```

    - 서비스 생성 시점
        - SystemService들은 Android 부팅 시 Zygote → SystemServer 프로세스가 실행되면서 생성
        - 경로
            - frameworks/base/services/java/com/android/server/SystemServer.java
        - 주요 서비스 등록 부분
            - 즉, SystemServer에서 SystemServiceManager.startService()로 시작
            ```java
            private void startOtherServices() {
                traceBeginAndSlog("StartActivityManager");
                ActivityManagerService am = mSystemServiceManager.startService(
                    ActivityManagerService.Lifecycle.class).getService();
                
                traceBeginAndSlog("StartPowerManager");
                mSystemServiceManager.startService(PowerManagerService.class);
                
                // ...
            }
            ```

    - 앱에서 접근하는 방식
        - 앱은 보통 Context.getSystemService()나 Manager 클래스를 통해 접근
        - 아래에서 실제로는 WifiManager → IWIFIService(AIDL) → WifiServiceImpl 로 IPC 호출
            ```java
            val wifiManager = context.getSystemService(Context.WIFI_SERVICE) as WifiManager
            val enabled = wifiManager.isWifiEnabled
            ```

    - Binder 기반 IPC 구조
        - SystemService는 대부분 Binder 기반 IPC 서버로 동작
            - (1) 앱에서 Manager 클래스를 통해 Binder 호출
            - (2) Binder Stub > Service Impl로 연결
            - (3) Native 또는 HAL 레벨로 작업 요청
            ```java
            // 구조 흐름 예시
            LocationManager.kt
                ↓
            ILocationManager.aidl
                ↓
            LocationManagerService.java
                ↓
            GnssHal.cpp or native lib
            ```

- Android의 RenderThread와 UI Thread의 상호작용
    - 개요
        - RenderThread와 UI Thread는 Android의 화면 렌더링 파이프라인에서 중요한 역할을 담당하는 두 축
        - 이 둘의 상호작용을 이해하면 앱의 퍼포먼스 최적화, 특히 jank(버벅임)이나 프레임 드랍 문제를 분석하는 데 도움이 될 것으로 생각

    - UI Thread
        - Android 앱의 메인 스레드(Main Thread).
        - 모든 UI 작업(뷰 그리기, 터치 이벤트 처리, 레이아웃 측정, 애니메이션 제어 등)이 UI 스레드에서 이루어짐
        - 예: Activity, View, Handler, setText(), invalidate() 등.

    - RenderThread
        - Android 5.0 (API 21) Lollipop부터 도입됨.
        - UI Thread의 작업과 별개로, 실제 OpenGL ES 기반의 렌더링 작업을 수행하는 백그라운드 스레드.
        - Choreographer와 연결되어 VSync 타이밍에 맞춰 동작.

    - 상호작용 흐름 요약 (프레임 단위로)
        - (1) UI Thread
            - View hierarchy의 측정(measure), 배치(layout), 그리기(draw) 를 실행함.
            - 그 결과 DisplayList라는 렌더링 명령 리스트를 생성함.
            - 이 DisplayList를 RenderThread로 넘김.

        - (2) RenderThread
            - UI Thread가 만든 DisplayList를 기반으로 실제 GPU에 렌더링 명령을 전송(OpenGL ES).
            - 이때 SurfaceFlinger와 협업하여 디스플레이에 출력.

        - (3) VSync 신호 발생
            - 약 16.6ms마다 발생 (60fps 기준).
            - Choreographer가 이 신호를 받아서 UI Thread와 RenderThread에 프레임 준비를 지시함.

    - 상호작용 시 주의사항
        - UI Thread가 오래 걸리면 → RenderThread가 DisplayList를 제때 못 받아 → 프레임 드랍 발생 (jank).
        - RenderThread는 비동기로 작동하므로 → UI Thread에서 블로킹 작업하면 → 다음 프레임이 늦어짐.
        - UI Thread에서 너무 많은 작업을 하면 → 애니메이션 끊김 발생.


- Android의 WindowManager와 SurfaceFlinger의 역할
    - WindowManager
        - 역할: 앱의 화면(Window)을 관리하는 시스템 서비스
        - API: WindowManager 클래스 > 앱에서 View를 추가하거나 제거할 때 사용
        - 담당 기능
            - 화면 레이아웃 배치 및 Z-Order 조정
            - 창의 크기, 위치, 애니매이션 처리
            - 입력 이벤트 전달 조정
        - 시스템 내부 구성
            - 실제로는 WindowManagerService(WMS)가 백엔드에서 작동하며 시스템 서버에서 앱 창들을 관리
    - SurfaceFlinger
        - 역할: 최종적으로 화면에 그려지는 이미지들을 조합(composite)해서 디스플레이에 출력
        - 동작 방식
            - 앱 또는 시스템 컴포넌트가 Surface 에 그리기 > SurfaceFlinger가 GPU로 모든 Surface들을 합성 > 화면에 렌더링
        - 특징
            - Surface는 BufferQueue를 통해 생산자(앱) <-> 소비자(SurfaceFlinger) 구조로 동작
            - 하드웨어 컴포지터(HWC) 와 협력하여 전력 효율적인 출력 구현
    
    - 역할 정리
        - WindowManager: 화면의 논리적 위치와 상태를 관리
        - SurfaceFlinger: 실제 그려진 내용을 화면에 출력

- Android의 ART(Android Runtime)와 Dalvik의 차이점
    - 개요
        - 안드로이드 앱 실행 방식의 핵심, 성능과 메모리 효율성, 개발 환경에 큰 영향

    - 기본 구조 및 개념의 차이
        - Dalvik은 Android 초기 버전에서 사용된 앱 실행 엔진
            - 자바 바이트코드(.class)를 안드로이드의 .dex(Dalvik Executable)파일로 변환하여 실행
        - ART(Android Runtime)는 안드로이드 5.0(롤리팝) 이후 기본 런타임으로 채택된 시스템
            - Dalvik의 한계 극복하고자 만들어졌으며, .dex 파일을 기계어로 미리 컴파일하는 방식(AOT, Ahead Of Time)을 기반으로 함.

    - 컴파일 방식의 차이
        - 사전 지식 (영어)
            - Just in time: 가까스로, 겨우, 적시에
            - Ahead of time: 미리
        - 방식 차이 설명
            - Dalvik
                - JIT(Just-In-Time)컴파일을 사용하여, 앱이 실행될 때마다 바이트코드를 해석하면서 실행함 -> 이로 인해 첫 실행 속도가 느리고, 실행 중 추가적인 CPU 자원을 소모
            - ART
                - 기본적으로 AOT(Ahead-Of-Time) 컴파일을 채택하여, 앱을 설치할 때 모든 코드를 한번에 네이티브 머신 코드로 변환
                - 실행 시점에서는 이미 변환된 기계어를 실행하기 때문에 앱 실행 속도가 매우 빠름

    - 성능 및 실행 효율성
        - Dalvik은 앱을 실행할 때마다 해석 또는 일부 컴파일을 하므로, 런타임 오버헤드가 크고 배터리 소모도 많음
        - ART는 앱이 기계어로 변환되어 있어, 실행 속도가 빠르고 CPU 자원 사용이 적어, 전반적인 성능과 전력 효율성이 개선됨

    - 설치 시간과 저장 공간
        - Dalvik은 설치가 빠르지만 실행 시 추가 컴파일이 필요
        - ART는 설치 과정에서 AOT 컴파일을 수행하므로 설치시간이 길어지고, 기계어코드가 저장되기 때문에 앱이 차지하는 용량도 커짐

    - Garbage Collection(GC) 성능
        - Dalvik의 GC는 일시 정지 시간이 길고, 앱의 반응성을 저하시킬 수 있음
        - ART는 더 정교하고 빠른 GC 알고리즘을 도입하여 앱 사용중 끊김 현상이 줄고, 더 부드러운 사용자 경험을 제공

    - 디버깅 및 프로파일링 기능
        - Dalvik은 기본적인 로그와 디버깅 기능만 제공
        - ART는 더 강력한 디버깅, 프로파일링, 성능측정 도구를 제공하여 개발자가 성능 병목이나 메모리 누수를 더 잘 분석할 수 있도록 함

    - 호환성 및 이행 과정
        - Android 4.4(킷캣)에서는 ART가 실험적으로 선택 가능했었음, 안드로이드 5.0부터는 ART가 기본 런타임이 되었음
        - ART는 Dalvik용 .dex 파일과도 호환되도록 설계되어, 개발자는 추가 변경 없이도 기존 앱을 사용할 수 있었음

    - 결론 요약
        - ART는 달빅의 런타임 컴파일 부담, 성능 저하, 낮은 디버깅 능력을 해결하고자 도입된 구조로, 안드로이드 시스템의 속도, 효율 개발 편의성을 전반적으로 향상시킨 런타임
        - 현재
            - ART에 JIT + AOT + Profile-Guided Optimization이 혼합되어, 설치속도와 실행 성능 모두를 균형 있게 잡고 있음

- 최신 ART 동작방식 및 개발 영향도
    - 최신 ART(Android Runtime) 동작방식
        - 개요
            - 최근 안드로이드의 ART는 단순한 AOT(선컴파일) 방식에서 진화해서 하이브리드 컴파일 모델 사용

        - 최신 ART의 동작 방식 (Android 7.0 ~ 이후)
            - 현대의 ART는 즉, 안드로이드 런타임은 다음 세가지 기법을 혼합해서 성능과 설치 속도를 균형있게 처리
            - 3가지 기법
                - AOT (Ahead-Of-Time) 컴파일
                    - 앱 설치 시 .dex 파일을 기계어로 변환(OAT, ELF) 해서 저장
                    - 앱 실행 시, 이미 변환된 네이티브 코드가 빠르게 실행됨
                    - 장점: 런타임 성능 뛰어남
                    - 단점: 설치 시간 증가, 저장 공간 많이 차지

                - JIT (Just-In-Time) 컴파일
                    - 앱 실행 중에 자주 사용되는 코드만 선택적으로 네이티브 코드로 변환
                    - Android 7.0부터 도입됨
                    - ART는 런타임 중 핫스팟 코드(자주 실행되는 경로) 를 감지하고 JIT 컴파일함
                    - 장점: 초기 설치 빠름, 저장공간 절약
                    - 단점: 첫 실행 속도가 AOT만큼 빠르진 않음

                - PGO (Profile-Guided Optimization, 프로파일 기반 최적화)
                    - 앱이 실제로 사용되는 패턴을 학습한 "실행 프로파일"을 저장
                    - 이후 앱 업데이트나 재설치 시, 이 프로파일을 기반으로 다시 AOT 컴파일 수행
                    - Android는 이 프로파일을 백그라운드로 수집하고, 사용자가 앱을 자주 사용할수록 성능이 좋아짐

            - 요약
                - 최신 ART는 JIT으로 빠르게 실행을 시작하고, 실행 데이터를 바탕으로 나중에 AOT로 성능을 점진적으로 끌어올리는 구조

    - 개발자에게 미치는 영향
        - (1) 앱 설치 속도 개선
            - 기존 ART (Lollipop): 설치 시간이 길어서 앱 배포 시 사용자 불만 가능
            - 최신 ART: 초기에는 JIT으로 빠르게 실행 → 사용하면서 자동 최적화됨
                - → 설치 속도와 초기 실행 성능의 균형

        - (2) 실행 성능 변화
            - 사용자의 앱 사용 패턴에 따라 성능이 달라짐
            - 즉, 자주 쓰는 기능은 더 빠르게 동작함
            - 따라서 비즈니스 로직이나 중요한 화면 진입 경로는 빠르게 튜닝됨

        - (3) 앱 용량 관리
            - 최신 ART는 디바이스 상황에 따라 코드 캐시를 유동적으로 관리함
            - 개발자가 앱 내에서 불필요한 코드를 줄이면, 최적화 대상이 줄어 공간도 절약됨

        - (4) 개발 중 디버깅/테스트 고려사항
            - 릴리즈 빌드 시 최적화 결과가 달라질 수 있음
            - debug 빌드에서는 JIT만 사용되지만, release 빌드에서는 AOT와 프로파일 최적화가 함께 작동 → 성능 차이 발생 가능
                - → 성능 테스트는 항상 릴리즈 모드에서 수행하는 것이 중요

        - (5) 멀티Dex 최적화
            - 최신 ART는 멀티 Dex를 더 잘 지원하고, Secondary Dex 파일도 AOT/JIT 적용이 가능함
            - 즉, 앱 크기가 커져도 런타임 성능 저하가 최소화됨

        - 결론
            - 최신 ART는 (최신 안드로이드 런타임은)
                - AOT의 빠른 실행 성능
                - JIT의 빠른 설치와 적은 용량 부담
                - PGO 기반의 지능형 최적화
            - 이 세 가지를 하이브리드로 결합해 최적의 성능을 끌어냄.
            - 개발자는 이러한 아키텍처를 이해함으로써 배포 전략, 성능 테스트, 릴리즈 플래닝에 있어 보다 효과적인 판단을 할 수 있음

- Java에서 HashMap과 ConcurrentHashMap의 차이점
    - 개요
        - Java 에서 키-값 쌍을 저장하는 Map 구조
        - 스레드 환경에서의 사용과 성능 최적화 방식에서 큰 차이 존재

    - 스레드 안정성 (Thread-Safety)
        - HashMap
            - 스레드에 안전하지 않음
            - 여러 스레드에서 동시에 접근하면 데이터가 손상되거나 무한 루프 발생 가능
            - 멀티스레드 환경에서는 외부에서 동기화 처리 필요
                ```java
                Map<K, V> syncMap = Collections.synchronizedMap(new HashMap<>());
                ```
        - ConcurrentHashMap
            - 스레드에 안전함
            - 내부적으로 동시 접근을 허용하면서도 안정적으로 동작하도록 설계됨
            - JDK 8 이후에는 Bucket 기반 분할 잠금(Striped Locking) 대신 Segment-Free 구조와 CAS 기반의 동시성 처리로 향상됨

    - 성능 (Performance)
        - HashMap
            - 단일 스레드 환경에서는 빠르고 효율적
            - 그러나 멀티스레드 환경에서는 synchronized를 사용하면 성능 저하
        - ConcurrentHashMap
            - 멀티스레드 환경에서도 높은 성능 제공
            - 전체 맵을 동기화하지 않고, 키에 따라 부분적으로만 잠금(Lock)하므로 경쟁이 줄어듬
            - 읽기(Read) 작업은 대부분 잠금 없이 (non-blocking) 동작
    - null 허용 여부
        - HashMap
            - null 키 1개 허용
            - null 값은 여러 개 허용
        - ConcurrentHashMap
            - null 키나 null 값 모두 허용하지 않음
            - 이유: null 값을 반환하면 key 부재인지 value가 null 인지 판단이 어려워 동기화 오류 유발 가능

    - 락 처리 방식 (Locking Mechanism)
        - HashMap
            - 동기화 없으므로 락 자체가 없음
            - Collections.synchronizedMap을 쓰면 맵 전체에 synchronized 적용
        - ConcurrentHashMap
            - JDK 7: Segment 단위로 락 (16개 Segment 기본)
            - JDK 8+: Bin Level Locking (각 버킷의 노드 단위 잠금) 또는 CAS(Compare And Swap) 연산 활용
            - 동시 수정이 가능한 고성능 구조

    - 결론
        - HashMap: 단일 스레드용, 가볍고 빠르나 멀티스레드에서는 반드시 외부 동기화 필요
        - ConcurrentHashMap: 멀티스레드 환경에서 안전하고 성능 좋은 맵, 실시간 시스템이나 캐시 구현에 적합

- Java에서 Reflection을 사용할 때 주의해야 할 점 및 개념
    - 개요
        - 자바 리플렉션은 매우 강력한 기능, 잘못 사용 시 보안/성능/안정성에 문제 유발
    - 리플렉션 개념
        - 정의 
            - 런타임에 클래스, 필드, 메서드, 생성자 등의 정보를 조사하고 조작할 수 있는 자바 메커니
            - java.lang.reflect 패키지에 포함됨
        - 주요 클래스
            - Class<?>: 클래스 자체 의미
            - Field: 멤버 변수
            - Method: 메서드
            - Constructor: 생성자
        - 예시
            ```java
            Class<?> clazz = Class.forName("com.example.MyClass");
            Method method = clazz.getMethod("doSomething");
            method.invoke(clazz.newInstance());
            ```

    - 주요 기능
        - 클래스 정보 탐색: Class.forName(), getDeclaredFields(), getMethods() 등
        - 메서드 실행: Method.invoke()
        - 필드 접근: Field.set(), Field.get()
        - 생성자 호출: Constructor.newInstance()
        - Private 접근: setAccessible(true) 통해 private / protected 접근 가능

    - 리플렉션 사용시 주의사항
        - (1) 성능 저하
            - 리플렉션은 런타임에 동적으로 검사하고 실행되기 때문에, 일반적인 메서드 호출보다 훨씬 느림
            - 반복 호출 시 성능 저하가 심각할 수 있음 (캐싱 or 제한된 영역에서만 사용 권장)

        - (2) 캡슐화 위반
            - private, protected 접근 제한자를 우회할 수 있음 (setAccessible(true))
            - 이는 객체지향 원칙(정보 은닉) 을 위배하며, 코드 유지보수성을 떨어뜨릴 수 있음

        - (3) 보안 위험
            - 악의적인 코드가 리플렉션을 통해 시스템 내부 구조를 들여다보거나 조작 가능
            - Java에서는 SecurityManager 를 통해 리플렉션 사용을 제한할 수 있었지만, 이는 이후 버전에서 폐지 예정임

        - (4) 런타임 오류 가능성
            - 리플렉션은 컴파일 타임 타입 검사(type checking)가 불가능
            - 잘못된 메서드 이름, 매개변수 타입, 필드명 등을 사용해도 컴파일 시 오류가 발생하지 않음
                - → 런타임 오류가 발생하기 쉬움

        - (5) 코드 난독화 및 유지보수 어려움
            - 코드가 정적 분석 도구나 IDE 자동완성에 잡히지 않음
            - 리팩토링 시에도 영향이 누락될 수 있음 (예: 메서드 이름 바뀌면 invoke는 깨짐)

    - 리플렉션 사용이 유용한 경우
        - 프레임워크 개발: 스프링, 하이버네이트 등에서 의존성 주입, AOP, ORM 등에 활용
        - 라이브러리 코드의 유연성: 외부 라이브러리나 모듈을 동적으로 호출해야 할 때
        - 테스트 도구: Mockito, JUnit 등에서 private 필드나 메서드에 접근할 때
        - 역직렬화: JSON/XML -> 객체 변환 시 클래스 구조 파악 필요

    - 리플렉션 실무 권장 사항
        - 가능하면 리플렉션 대신 정적 코드 구조 사용
        - 필요 시
            - 캐싱해서 재사용 (Method, Field 등)
            - 잘 문서화하고 명확한 fallback 전략을 둬야 함
            - 라이브러리 / 프레임워크 내부에서만 국한시키고, 앱 전역에 남용하지 않도록 설계

    - 결론 정리
        - 리플렉션은 강력한 도구이나 느리고, 위험하고(보안, 캡슐화 침해) 그리고 불안정함(런타임 오류)

- Java에서 equals()와 ==의 차이점
    - 개요
        - 두 값을 비교할 때 사용하는 연산자/메서드
        - 비교하는 대상과 의미가 완전히 다름
    - == 연산자
        - ==는 참조 타입일 경우 메모리 주소(참조값)을 비교
        - 기본 타입일 경우 값 자체를 비교하는 연산자(Operator)
    - equals()
        - 객체가 논리적으로 같은지를 판단하는 메서드
        - 기본적으로 Object.equals()는 ==와 동일하게 참조값을 비교하지만,
        - 필요에 따라 오버라이드하여 값 기반 비교가 가능
        ```java
        String a = new String("hello");
        String b = new String("hello");
        System.out.println(a.equals(b)); // true → 내용이 같음
        ```
    - 결론
        - ==는 참조(주소) 또는 기본값 자체를 비교하는 연산자
        - equals()는 객체의 논리적 동등성을 비교하는 메서드
        - 객체 비교 시에는 반드시 equals()를 사용해야 하며, ==는 동일 인스턴스 여부 확인에만 사용해야 한다.

- Java에서 hashCode()와 equals()의 관계
    - 개요
        - 객체의 동등성 비교와 해시 기반 컬렉션(Set, Map 등)의 동작을 결정하는 핵심 메서드
        - 서로 긴밀하게 연결된 규약(contract)이 있기 때문에, 올바르게 이해하고 함께 오버라이드 해야 문제없이 작동

    - equals()
        - 두 객체가 논리적으로 같은지 비교하는 메서드
        - 기본적으로 Object.equals()는 참조(주소) 비교를 하지만,
        - 직접 오버라이드하여 값 기반 비교가 가능
        ```java
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Person other = (Person) obj;
            return name.equals(other.name) && age == other.age;
        }
        ```

    - hashCode()
        - 객체를 해시 기반 컬렉션(Map, Set 등)의 키로 사용할 때 필요한 정수값을 반환하는 메서드
        - 기본적으로 객체의 메모리 주소 기반으로 계산되지만,
        - equals()를 오버라이드하면 hashCode()도 반드시 같이 오버라이드해야 함
        ```java
        @Override
        public int hashCode() {
            return Objects.hash(name, age);
        }
        ```

    - equals()와 hashCode()의 필수 규약 (Contract)
        - 핵심 규칙
            - 같다고 판단되는 객체는 항상 같은 hashCode 값을 가져야 함
        - 상세 내용
            - a.equals(b) == true 이면 -> a.hashCode() == b.hashCode() 여야 함
            - a.hashCode() == b.hashCode() 라고 해서 반드시 a.equals(b) == true 일 필요는 없음 (충돌 가능)
        - 규약 미 준수 시
            - HashMap, HashSet, HashTable 등의 컬렉션에서 검색/중복 제거/저장 등의 동작이 비정상적으로 작동

    - HashSet에서 문제되는 경우
        ```java
        Set<Person> people = new HashSet<>();
        people.add(new Person("Aiden", 30));
        people.contains(new Person("Aiden", 30)); // hashCode와 equals 둘 다 오버라이드 안 하면 false!
        ```
        - equals()만 오버라이드하고 hashCode()는 그대로 두면
            - -> 논리적으로 같지만 서로 다른 해시 버킷에 들어가서 탐색 실패

    - 올바른 오버라이드 방법 (Java 7+)
        ```java
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Person other = (Person) obj;
            return name.equals(other.name) && age == other.age;
        }

        @Override
        public int hashCode() {
            return Objects.hash(name, age); // java.util.Objects
        }
        ```

    - 총 정리
        - Java에서 equals()는 객체의 논리적 동등성,
        - hashCode()는 해시 기반 자료구조에서 객체 위치 지정을 위해 사용되며,
        - 같다고 판단되는 객체는 반드시 같은 hashCode를 가져야 한다는 규약을 지켜야 한다.
        - 그렇지 않으면 HashMap, HashSet 등에서 검색 오류, 중복 허용 등의 버그가 발생할 수 있다.

- Java StringPool
    - 개요
        - 문자열의 메모리 사용을 최적화하기 위한 JVM의 내부 메커니즘
    
    - String Pool 정의
        - JVM이 관리하는 문자열 상수 전용 메모리 영역
        - 이 영역에 저장된 문자열은 중복 없이 공유되며, 같은 문자열 리터럴을 여러 번 사용할 경우 하나의 인스턴스만 사용
    
    - 필요 이유
        - 문자열은 불변하고 코드 곳곳에서 자주 사용되기 때문
        - 매번 객체를 생성하면 메모리 낭비가 크고 성능 저하 발생
        - JVM은 동일한 문자열 리터럴을 String Pool에 저장하고 재사용

    - 동작 내용
        - 리터럴 사용 시 (컴파일 타임)
            ```java
            String s1 = "Hello";
            String s2 = "Hello";
            System.out.println(s1 == s2); // true
            ```
            - "Hello"는 String Pool에 한번만 생성되고, s1, s2는 같은 메모리 주소를 참조

        - new 연산자 사용 시 (런타임)
            ```java
            String s3 = new String("Hello");
            System.out.println(s1 == s3); // false
            ```
            - new String("Hello")는 Heap 영역에 별도의 객체를 만듦
            - Pool에 있는 "Hello"와는 다른 주소 참조

        - intern() 메서드 사용
            ```java
            String s4 = new String("Hello").intern();
            System.out.println(s1 == s4); // true
            ```
            - 해당 문자열이 String Pool에 있으면 그 객체를 반환하고, 없으면 Pool에 추가하고 반환함
    
    - 특징
        - String Pool은 JVM의 Metaspace (구 JVM PermGen) 영역에 존재
        - JVM이 자동 관리하지만, intern()으로 수동 제어도 가능
        - 문자열 리터럴은 기본적으로 Pool에 들어감
        - 불변성이 기반이라 가능한 기능 (String이 mutable이면 불가능)

    - 추가 설명
        - 문자열 비교 시 == 대신 .equals() 사용이 안전
        - intern()을 무분별하게 사용하면 Metaspace 메모리 부족 가능성
        - JSON이나 대용량 텍스트 처리 시 문자열 객체가 쌓이지 않도록 주의

    - 재 정리
        - Java의 String Pool은 동일한 문자열 리터럴이 메모리상에서 하나의 객체로 공유되도록 하는 JVM 메커니즘
        - 메모리 절약과 성능 향상을 위해 설계된 기능
        - "Hello"와 같이 직접 작성한 문자열 리터럴은 자동으로 Pool에 저장되며, intern() 메서드를 통해 수동으로도 Pool에 등록 가능

- Java에서 String과 StringBuilder, StringBuffer의 차이점
    - String
        - 불변(immutable) 클래스, 문자열 수정 시 항상 새로운 객체가 생성됨
        - 문자열 값이 절대 변경되지 않음
        - 문자열 연산이 생기면 항상 새로운 객체를 생성
        - 가장 많이 사용되며, 문자열 리터럴("abc")로도 선언 가능

    - StringBuilder
        - 가변(mutable) 클래스, 내부 배열을 직접 수정
        - 문자열 조작(append, insert, delete 등)이 자주 발생하는 경우에 적합
        - 싱글 스레드 환경에서 성능이 가장 좋음

    - StringBuffer
        - StringBuilder와 거의 동일하나, 모든 메서드가 synchronized 처리
        - 즉, 스레드 안전(thread-safe) 하지만 성능은 느림
        - 멀티 스레드 환경에서 문자열 조작이 필요할 때 사용
        - 가변이지만 동기화 처리됨

    - 속도
        - StringBuilder > StringBuffer > String

    - StringBuilder, StringBuffer 메소드
        - append
        - insert
        - delete
        - reverse
        - toString

    - 사용 사례별 추천
        - 문자열이 자주 변경되지 않음, String 추천, 코드 간결함, 불변으로 안전
        - 반복적으로 빠른 문자열 조작 필요, StringBuilder. 빠르고 효율적
        - 멀티스레드 환경에서 문자열 조작, StringBuffer, 동기화로 스레드 안전 보장

    - 기타 참고 사항
        - StringBuilder와 StringBuffer는 내부적으로 char[] 배열을 사용
        - 버퍼 크기가 부족하면 자동으로 배열 크기를 2배 이상으로 확장
        - StringBuilder는 JDK 1.5부터 도입 → 기존 StringBuffer보다 빠른 대안으로 자리잡음


- Java의 클래스 로딩 과정(Class Loading Process)
    - 개요
        - Java 프로그램이 실행될 때, .class 파일(바이트 코드)을 JVM이 읽고 메모리에 적재하고 실행하는 과정을 클래스 로딩 과정이라고 함
        - 이 과정은 크게 5단계로 구성됨
            - Loading -> Linking -> Initialization -> Using -> Unloading
            - 클래스 로딩 -> 링킹 -> 초기화 -> 사용 -> 언로드

    - (1) Loading (클래스 로딩) -> .class 파일을 JVM 메모리에 로딩
        - 역할: .class 파일을 JVM 메모리로 읽어들이는 작업
        - 작동 방식
            - 클래스 이름을 기반으로 해당 .class 파일을 찾음
            - 파일 내용을 읽어 메서드 영역에 클래스의 구조를 저장
        - 클래스 로더 종류
            - Bootstrap ClassLoader: java.* 클래스 로딩
            - Extension ClassLoader: ext 디렉토리 클래스 로딩
            - Application ClassLoader: 클래스패스에 있는 사용자 정의 클래스 로딩
        - 클래스 로딩은 Lazy Loading 방식: 실제로 필요한 시점에 로딩됨

    - (2) Linking (링킹) -> 바이트코드 검증, static 필드 메모리 할당, 심볼 참조 해석
        - 로딩된 클래스 파일을 JVM이 실행 가능한 형태로 연결하는 작업, 3단계로 구성
        - (A) Verification (검증)
            - 바이트코드가 JVM 규칙에 맞는지 검사
            - 악의적인 코드로부터 JVM을 보호
            - 스택 사용 규칙, 접근 제어, 포맷 검증 등 수행
        - (B) Preparation (준비)
            - 클래스의 static 변수들을 메모리에 할당
            - 단, 초기값(디폴트 값)만 설정됨 (예: int는 0, boolean은 false)
            - 아직 실제 값으로 초기화되지 않음
        - (C) Resolution (해결)
            - 클래스 내부에서 참조하는 다른 클래스/인터페이스/메서드/필드 등을 연결
            - 심볼릭 참조 -> 직접 참조로 변환 (Symbolic Reference -> Direct Reference)

    - (3) Initialization (초기화) -> static 블록 및 필드 초기화
        - static 초기화 블록 또는 Static 필드의 명시적 초기값을 실행함
        - Preparation 단계에서 할당된 static 필드들이 실제 값으로 초기화되는 단계
        - 이 단계는 클래스가 실제로 사용될 때 한 번만 수행됨
        - 순서는 상속 계층에 따라 상위 클래스부터 하위 클래스 순으로 실행됨

    - (4) Using (사용) -> 클래스 사용 (인스턴스 생성, 메서드 호출 등)
        - 이제 클래스는 정상적으로 메서드를 호출하거나 인스턴스를 생성하는 데 사용할 수 있음
        - JVM은 메서드 호출, 필드 접근 등을 처리하면서 바이트코드를 실행함

    - (5) Unloading (언로드) -> 사용이 끝난 클래스 메모리 해제(GC에 의해)
        - 클래스가 더 이상 사용되지 않으면 GC(가비지 컬렉터)가 해당 클래스를 메모리에서 제거
        - 단, 대부분의 클래스는 앱 종료 전까지 유지됨
        - 동적 클래스 로딩 시 (ClassLoader를 직접 정의할 때) 메모리 해제를 명확히 관리해야 함

    - 참고: 클래스 로더 체인 (Delegation Model)
        - 자바는 위임 모델을 사용해 클래스 로더가 상위 클래스 로더에 먼저 위임하고, 상위에서 찾지 못할 때만 자신이 로딩함
        - 이 구조는 보안과 일관성을 보장하며, 중복 로딩을 방지함.

- Java에서 super 키워드와 this 키워드의 차이점
    - 개요
        - this: 현재 클래스의 인스턴스를 가리킴
        - super: 부모 클래스의 인스턴스를 가리킴

    - this 키워드
        - 필드와 파라미터 이름이 충돌할 때 (this.name = name)
        - 현재 객체를 다른 메서드에 전달할 때
        - 생성자 간 호출 (this(...), 오버로딩된 생성자 재사용)

    - super 키워드
        - 부모 클래스 생성자 호출
        - 부모 클래스 메서드 호출
        - 부모 클래스 필드 참조 (super.field)
            ```java
            class Animal {
                String type = "동물";
                void speak() {
                    System.out.println("소리 낸다");
                }
            }

            class Dog extends Animal {
                void printType() {
                    System.out.println(super.type);  // Animal의 필드
                }
                void speak() {
                    super.speak(); // Animal의 메서드 호출
                    System.out.println("멍멍!");
                }
            }
            ```

- Java에서 메모리 관리(Memory Management)와 가비지 컬렉션(Garbage Collection)
    - 개요
        - 자바는 자동 메모리 관리 언어
        - 개발자가 직접 free()를 호출하지 않아도 JVM이 자동으로 객체를 할당하고 제거(가비지 컬렉션)

    - 자바 메모리 구조(JVM 기준)
        - Heap
            - 객체(instance), 배열 등이 저장되는 영역 → GC 대상
        - Stack	
            - 메서드 호출 시의 지역변수, 매개변수 저장 → 스코프 종료 시 자동 제거
        - Method Area
            - 클래스 정보, static 변수, 메서드 등 → PermGen → MetaSpace
        - PC Register
            - 각 스레드가 어떤 명령어를 실행 중인지 기록
        - Native Method Stack
            - JNI 등 네이티브 호출용

    - 객체 생성과 소멸
        - new 키워드로 객체 생성 → Heap에 메모리 할당
        - 객체를 참조하는 변수가 사라지면 → 더 이상 사용되지 않는 객체
        - JVM이 GC(Garbage Collector) 를 통해 해당 객체를 제거

    - Garbage Collection의 특징
        - 자동 메모리 회수: 더 이상 참조되지 않는 객체는 자동으로 제거
        - 참조 카운트 방식 사용 안함:  Java는 참조 카운트보다 reachability 탐색 기반
        - GC Root 기준: static 변수, 스레드 stack, 메서드 호출 체인에서 도달할 수 없으면 GC 대상

    - GC 동작 방식
        - Mark: GC Root에서 참조 가능한 객체들 "표시"
        - Sweep: 참조되지 않은 객체 제거
        - Compact: 메모리 단편화 해소를 위해 객체를 한 곳으로 정렬
            - → 이 과정은 Full GC 또는 Young GC, Old GC에 따라 달라짐

    - GC 유형(JVM 구현 기준)
        - Serial GC: 단일 스레드, 작은 애플리케이션에 적합
        - Parallel GC: 멀티 스레드, Throughput 중시
        - CMS GC: 응답 속도 중시 (Low latency)
        - G1 GC: 최신 GC, Heap을 Region으로 나눠 관리
        - ZGC / Shenandoah: 매우 낮은 지연을 위한 최신 GC

    - 메모리 누수 방지를 위한 방법
        - 리스너, 콜백, 컨텍스트 참조 해제 필요
        - WeakReference, SoftReference로 GC 대상 객체 구분 가능
        - System.gc() > 직접 GC 요청 가능하지만 보장은 안됨

- 메모리 누수 발생 예시
    - 개요
        - 메모리 누수(Memory Leak)는 Android에서 흔히 발생하는 문제 중 하나고, 특히 Context, Adapter, Static 변수를 잘못 사용하면 앱이 점점 느려지거나 OOM(Out of Memory)을 일으키는 원인이 됨

    - 발생 예시
        - (1) Static 변수에 Context를 저장한 경우
            - 잘못된 코드 예시
                - object / static 필드는 애플리케이션 생명주기보다 오래 살아있음
                - Activity Context는 화면 종료 후에도 메모리에 남게 됨 > GC 되지 않는 이슈 발생
                ```java
                object AppConfig {
                    var context: Context? = null
                }

                class MyActivity : AppCompatActivity() {
                    override fun onCreate(savedInstanceState: Bundle?) {
                        super.onCreate(savedInstanceState)
                        AppConfig.context = this  // 메모리 누수 발생 포인트
                    }
                }
                ```
            - 해결 방법
                - ApplicationContext만 Static으로 저장 (가능한 경우)
                - WeakReference 사용 (GC에 의해 강제로 수집될 수 있는 참조를 나타내는 객체)
                    - 일반적으로 자바에서는 객체에 대한 참조가 있는 경우 해당 객체는 메모리에서 수집안됨
                    - WeakReference는 약한 참조를 제공하여 객체가 메모리에서 수집되도록 허용
                    - WeakReference 사용 시 객체가 더 이상 사용되지 않는 경우 자동으로 메모리에서 제거됨 > 객체의 수명 주기를 추적하고 메모리 누수 방지에 유용
                    - 예: 캐시나 캐시 라인에 저장된 객체 등은 더 이상 필요하지 않을 때 메모리 상에서 제거되어야 함
                    ```java
                    object AppConfig {
                        var contextRef: WeakReference<Context>? = null
                    }
                    ```

        - (2) Adapter 에서 Context 또는 View 참조 유지
            - 잘못된 코드 예시
                - 액티비티가 종료되어도 Adapter가 ViewPager, RecyclerView 등에 의해 계속 참조될 수 있음
                - 내부 클랙스 또는 context 고정 참조가 액티비티를 계속 메모리에 유지
                ```java
                class MyAdapter(context: Context) : RecyclerView.Adapter<...>() {
                    val context = context  // 액티비티 context를 내부에 고정 참조
                }

                inner class MyViewHolder(val view: View) : RecyclerView.ViewHolder(view)  // context를 계속 들고 있음
                ```
            - 해결 방법
                - ApplicationContext 사용 (가능한 경우)
                    ```java
                    val context = context.applicationContext
                    ```
                - ViewHolder를 static(inner class X)으로 구현
                - Context 참조 자체를 없애고 필요 시 itemView.context 활용

        - (3) Handler가 액티비티를 참조하는 경우
            - 잘못된 코드 예시
                - 핸들러는 내부적으로 액티비티를 참조 > 메시지큐에 오래 남으면 GC되지 않음
            - 해결 방법
                - 핸들러를 static / object 클래스로 분리 + WeakReference 사용
                ```java
                class MyHandler(activity: Activity) : Handler(Looper.getMainLooper()) {
                    private val activityRef = WeakReference(activity)

                    override fun handleMessage(msg: Message) {
                        activityRef.get()?.let {
                            Toast.makeText(it, "Hello", Toast.LENGTH_SHORT).show()
                        }
                    }
                }
                ```

        - (4) Listener, Callback 등록 후 해제하지 않은 경우
            - 잘못된 코드 예시
                - 리스너를 등록하고 remove를 호출하지 않으면 시스템이 액티비티를 계속 참조 > GC 불가
            - 해결 방법
                - onDestroy / onPause에서 반드시 해제 (remove/Listener, callback)

        - (5) WebView 사용 시 누수
            - 잘못된 코드 예시
                - 웹뷰는 액티비티보다 오래 살아남는 경우가 많음
                ```java
                val webView = WebView(this)  // 직접 생성 후 addView, 그리고 해제 안 하면 누수
                ```
            - 해결 방법
                ```java
                override fun onDestroy() {
                    webView.apply {
                        clearHistory()
                        clearCache(true)
                        loadUrl("about:blank")
                        removeAllViews()
                        destroy()
                    }
                    super.onDestroy()
                }
                ```
    - LeakCanary 의존성 사용한 누수 탐지
        - debugImplementation "com.squareup.leakcanary:leakcanary-android:2.12"
        - 설치 후 앱 실행 > 누수 발생 시 알림 > 어떤 객체가 해제되지 않았는지 추적 가능

- Listener, Callback 의 개념적 차이
    - 개요
        - 비슷한 개념이고 사용법 유사하나 관점 또는 사용 방식에서 차이 존재
        - 콜백은 함수의 참조(콜백 함수)를 넘겨서 나중에 호출하는 방식
        - 리스너는 인터페이스 기반의 이벤트 수신자를 등록하는 구조

    - 공통점
        - 둘 다 비동기 처리를 위한 메커니즘
        - 어떤 이벤트가 발생했을 때 특정 작업을 수행하게 함
        - 호출 시점은 개발자가 아닌, 시스템 또는 다른 클래스가 제어

    - 개념적 차이
        - 콜백
            - 함수(람다 / 참조)
            - 본질은 함수(코드 블록) 참조 전달
            - 주로 단일 이벤트 처리, 단일 응답/일회성 작업
            - 함수를 인자로 전달하는 구조
            - 람다로 표현 가능하고 짧고 간결한 코드
            - 대표 예: Retrofit의 onResponse, runOnUiThread {}
        - 리스너
            - 인터페이스 구현체
            - 본질은 인터페이스 구현체 전달
            - 주로 복수 이벤트 처리 및 대응
            - 인터페이스 구현 후 등록하는 구조
            - 클래스 구조 많고 장황할 가능성 있음
            - 대표 예: Button의 OnClickListener, RecyclerView의 OnScrollListener

    - 예시
        - 콜백
            - 람다 또는 함수 참조를 인자로 전달
            - 함수 하나만 넘기면 되는 단순한 이벤트에 적합
            ```java
            fun loadData(onFinished: (String) -> Unit) {
                // ...데이터 로드 중
                onFinished("성공!")
            }

            loadData { result ->
                println("결과: $result") // 콜백 함수가 나중에 호출됨
            }
            ```

        - 리스너
            - 인터페이스 구현 > 등록 구조
            - 여러 메서드가 필요한 복잡한 상호작용 이벤트 처리에 적합
            ```java
            interface OnItemClickListener {
                fun onItemClick(position: Int)
            }

            class MyAdapter {
                var listener: OnItemClickListener? = null
            }

            adapter.listener = object : OnItemClickListener {
                override fun onItemClick(position: Int) {
                    println("클릭됨: $position")
                }
            }
            ```
    - Android SDK 예시
        - Button: Listener
        - Retrofit / Volley: Callback
        - Dialog: Listener
        - Coroutines: Callback
        - RecyclerView: Listener

- Java에서 default 메서드를 인터페이스에서 지원하는 이유
    - 배경 및 필요성:
	    - Java 8 이전까지 인터페이스는 추상 메서드만 가질 수 있었고, 이를 구현하는 클래스는 모든 메서드를 구현해야 했음
	    - 하지만 인터페이스에 새로운 기능(메서드)을 추가하면, 그 인터페이스를 구현한 모든 클래스에 컴파일 에러가 발생했음
        - → 이는 기존 코드를 깨뜨리는 문제를 발생시킴.

    - 지원 이유 요약:
	    - 기존 인터페이스에 기능 추가 시, 하위 호환성을 유지하기 위해.
        - 다이아몬드 상속 문제를 피하면서도 다형성과 유연성을 제공하기 위해.
    
    - 예제
        - 기존 구현 클래스가 아무 변경 없이도 sayHello()를 사용할 수 있게 됨
        ```java
        interface MyInterface {
            default void sayHello() {
                System.out.println("Hello from interface!");
            }
        }
        ```

- Java에서 record 키워드를 사용하면 얻을 수 있는 장점
    - 배경:
	    - Java 14부터 도입되었고, Java 16부터 정식 기능으로 포함됨.
	    - record는 불변(immutable) 데이터 객체를 간단하게 선언할 수 있게 해주는 문법.
        - 구조 상 코틀린의 데이터 클래스와 유사

    - 장점 요약:
        - 불변 데이터 객체 생성 간소화
	        - getter, equals(), hashCode(), toString() 자동 생성.
	        - 생성자도 자동 생성됨.
        - 코드 간결화
	        - 수동으로 작성해야 할 보일러플레이트 코드 제거.
        - 가독성과 유지보수성 향상
	        - 데이터 중심 클래스를 명확하게 표현.

    - 예시 비교:
        ```java
        public record User(String name, int age) {}

        public class User {
            private final String name;
            private final int age;
        
            // 생성자, getter, equals, hashCode, toString 등 다 작성해야 함
        }
        ```

- Java에서 switch 문을 개선한 switch expressions의 특징
    - 개요
        - switch expressions는 값 반환 가능하며 안전하고 간결한 문법으로 개선된 switch (when과 유사)
        - Java 14 이후부터 도입
    - 특징
        - yield 키워드 지원: 여러줄 블록에서 값 반환 시 사용
        - 컴파일러가 누락된 case 감지 가능: enum 타입 사용 시 모든 케이스 미 처리시 경고 발생 가능
        - 화살표 문법
        - 반환 가능 (값 반환)
    - 예제
        ```java
        String result = switch (day) {
            case MONDAY, FRIDAY, SUNDAY -> "Weekend";
            case TUESDAY -> "Work hard!";
            default -> "Midweek";
        };

        int result = switch (value) {
            case 1 -> 100;
            case 2 -> {
                int calc = 10 * 2;
                yield calc;
            }
            default -> 0;
        };
        ```
    - 전체 요약
        - 코드 간결 (break 줄이기 가능)
        - 값 반환 가능
        - 타입 안정성 증가 (모든 케이스 커버 > 컴파일러가 체크)
        - 가독성 향상 (블록 없이 화살표 문법)

- Java에서 synchronized 키워드 사용 시 주의점
    - 개요
        - 멀티스레드 환경에서 공유 자원의 동시 접근을 제어하기 위해 사용하는 가장 기본적인 동기화 수단
        - 잘못 사용 시 성능저하, 데드락, 기대하지 않은 동작 등 문제 발생 가능성 있음
    - 주의 사항
        - (1) 락의 범위
            - 객체 또는 클래스 단위로 락 설정
            - 같은 락을 여러 스레드가 요청하면 순차적으로 실행됨
            - 매번 new Object()로 락을 만들면 의미 없음
        - (2) 과도한 락은 성능 저하 (synchronized 블록이 너무 크면)
            - 블록이 너무 크면 해당 영역에 접근하려는 다른 스레드들이 장시간 대기함
            - 최소한의 범위로 락을 걸어야 성능 유지
        - (3) 데드락 (Deadlock) 주의
            - 여러 스레드가 서로의 락을 기다리며 영원히 멈추는 상태
                ```java
                Thread 1: synchronized(objA) → synchronized(objB)
                Thread 2: synchronized(objB) → synchronized(objA)
                ```
            - 락 순서를 일관되게 유지하거나 tryLock() (ReentrantLock 사용 시)을 고려해야 예방 가능
        - (4) synchronized는 가시성 보장도 함
            - 락을 획득하고 해제하는 과정에서 메모리 가시성 보장
            - 즉, 하나의 스레드가 업데이트한 값이 다른 스레드에서도 보이는 상태로 유지
            - volatile과 다르게, 원자성 + 가시성을 모두 제공
        - (5) 메서드 전체 락 가능
            - 인스턴스 메서드: this를 락 객체로 사용
            - static 메서드: Class.class를 락 객체로 사용
                ```java
                public synchronized void doSomething() {
                    // this에 대해 락이 걸림
                }
                public static synchronized void doGlobalThing() {
                    // MyClass.class에 대해 락
                }
                ```
        - (6) 성능에 민감하면 ReentrantLock 고려
            - synchronized는 간단하지만 정밀 제어가 불가능
            - java.util.concurrent.locks.ReentrantLock을 사용하면:
                - 타임아웃 설정 (tryLock)
                - 공정성 설정
                - 명시적인 락 해제 (unlock) 가능
        `   - 단, unlock()을 반드시 finally 블록에서 호출해야 안전

- Java에서 volatile 과 synchronized 차이
    - 개요
        - 둘다 멀티스레드 환경에서 변수의 안전한 접근을 위해 사용되는 키워드
        - 역할과 보장하는 범위가 다르다.
    - 요약
        - volatile: 가시성만 보장
        - synchronized: 가시성 + 원자성 모두 보장
    - volatile 기준 차이 비교
        - 변수 수중에서 메모리 동기화
        - 락 사용하지 않음
        - 성능 빠름 (락이 없으므로)
        - 복잡한 연산 처리 불가 (count++)
        - 데드락 위험 없음 (락 없으므로)
        - 단일 변수의 상태 플래그 사용 용도
    - volatile 이 보장하는 가시성
        - 한 스레드에서 변경한 값을 다른 스레드에서 즉시 볼 수 있도록 보장
        - volatile 없으면 플래그 값이 CPU 캐시에 남아 변경을 감지하지 못할 가능성 존재
    - volatile 이 보장하지 않는 원자성
        - count++ 류의 연산은 내부적으로 복잡한 3단계 연산 (read, add, write)
        - volatile은 가시성만 보장하므로 동시 접근 시 경쟁 조건 발생
    - 결론
        - volatile은 값을 즉시 반영하도록 보장, 연산은 보호하지 않음
        - synchronized는 원자성 + 가시성 모두 보장, 락 기반으로 더 안전하나 느릴 수 있음
        - 플래그처럼 단일 필드 감시는 volatile 사용
        - 데이터 동기화 필요하거나 연산 포함 시에는 synchronized / Lock

- Java에서 AtomicInteger와 synchronized의 차이점
    - 개요
        - AtomicInteger는 단일 변수의 원자적 연산을 빠르게 처리하는 클래스
        - synchronized는 임계 영역 전체의 동시 접근을 제어하는 키워드

    - 차이 비교
        - Atomic은 원자성만 보장, 락 없으며 Lock-Free 방식
        - 성능은 빠르며, CAS 기반, 경합 적을수록 효율은 높아짐
        - 가시성 보장: JMM 기반 volatile 보장

    - Atomic 예제
        - incrementAndGet(), getAndAdd(), compareAndSet() 등 원자 연산 제공
        - 내부적으로 CAS(Compare-And-Swap) 알고리즘 사용
        ```java
        AtomicInteger counter = new AtomicInteger();
        public void increase() {
            counter.incrementAndGet(); // 원자적 증가
        }
        ```

    - Atomic 변수 내부적 동작 원리
        - JVM 수준에서 CAS (Compare And Set) 연산을 사용
        - 경쟁이 있을 경우 재시도(스핀 락) 방식으로 처리
        - 락은 없지만 경쟁이 심할 경우 성능 저하 발생 가능성도 존재

- Java에서 ThreadLocal
    - 개요
        - 각 스레드가 자기만의 값을 가지도록 해주는 변수 저장소
        - 스레드 간에 데이터 충돌 없이 독립적인 값 유지가 필요할 때 사용

    - 예제
        - set, get, remove() 메소드 존재
        ```java
        ThreadLocal<Integer> threadLocal = new ThreadLocal<>();
        threadLocal.set(100); // 현재 스레드만 이 값을 가짐
        Integer value = threadLocal.get(); // 다른 스레드와는 무관한 값
        ```

    - 사용 시점
        - 각 스레드가 자신만의 데이터 / 컨텍스트를 가져야 할 때 (스레드 간 충돌없이 처리)
        - 스레드 풀에서 같은 객체를 재사용해야 할 때 (객체 공유 없이 안전하게 처리)
        - 웹 요청 처리 시 사용자 정보 등 컨텐스트 보관 (스레드로컬로 로그인 정보 등 유지)
        - 로그 트레이싱 정보 저장 (스레드로컬로 트레이스 아이디 유지)

    - 주의 사항
        - 메모리 누수 (스레드 풀에서는 스레드 로컬을 명시적으로 remove 필요)
        - 스레드 로컬 값은 절대 공유되지 않음
        - InheritableThreadLocal (자식 스레드에도 값 전달 희망 시 사용)

- Kotlin에서 inline 함수의 장점과 단점
    - 개요
        - 코틀린의 인라인 함수는 성능 최적화와 람다 사용의 유연성을 위해 자주 사용하는 기능
        - 인라인 함수는 함수 호출을 줄이고, 람다 인자를 컴파일 타임에 코드로 치환하여 성능을 높이는 기능

    - 인라인 함수(inline function)
        - 일반적으로 람다를 인자로 넘기면 익명 클래스가 생성되고 호출됨
        - inline 키워드 사용 시, 함수와 람다 본문이 호출 지점에 직접 삽입됨
        ```java
        // 인라인 함수 정의 
        inline fun runTwice(action: () -> Unit) {
            action()
            action()
        }
        // 인라인 함수 호출 (람다를 인자로 넘김)
        runTwice { println("Hello") }

        // 컴파일 시 실제 코드
        println("Hello")
        println("Hello")
        ```

    - 인라인 함수 장점
        - 성능 향상(콜 제거)
            - 함수 호출 자체가 사라져 호출 비용이 줄어듦 (특히 람다 함수에서 효과 큼)
        - 익명 클래스 생성 안함
            - 람다 인자를 넘겨도 object: FunctionN {}가 생성되지 않음 -> GC 부담 감소
        - non local return 가능
            - 람다 안에서 return을 쓰면 바깥 함수에서 바로 반환 가능
            - 일반 람다에선 불가능한 동작이 인라인 함수 안에서는 허용
            ```java
            inline fun doSomething(action: () -> Unit) {
                action()
            }

            fun test() {
                doSomething {
                    return // 가능: test()에서 바로 빠져나감
                }
            }
            ```
        - reified 타입 사용 가능
            - 제네릭 타입을 런타임에도 사용할 수 있음 -> T::class.java 등 사용 가능
            ```java
            inline fun <reified T> isType(value: Any): Boolean {
                return value is T
            }

            isType<String>("hello") // true
            ```

    - 인라인 함수의 단점
        - 코드 크기 증가 (Code Bloat)
            - 호출 위치마다 본문이 복붙됨 → 큰 함수일수록 빌드 크기 커짐
        - 디버깅 어려움	
            - 중간에 함수가 사라져서 브레이크포인트 설정이 어렵거나 혼란스러움
        - reified는 inline에서만 가능
            - 반대로 말하면, reified 제네릭은 inline 함수에서만 사용 가능 (제약)
        - 재귀 호출 불가
            - inline fun factorial(...) 같이 자기 자신을 호출하는 함수는 inline 불가
        - 람다 캡처 시 주의 필요
            - 람다 안에서 캡처한 외부 변수의 처리 방식이 달라질 수 있음
    
    - 인라인 사용 시점 정리
        - 람다를 자주 사용하는 함수 (map, filter, withContext 등)
            - inline 권장
        - 고차 함수가 빈번하게 호출되는 Utility 함수
            - inline 고려
        - 큰 본문, 재귀 구조, 중복 호출이 많은 함수
            - inline 지양
        - 제네릭 타입의 reified가 필요한 경우
            - 반드시 inline 필요
        - 디버깅 중인 복잡한 로직
            - 디버깅 불편 → 일반 함수 추천

    - 참고
        - 고차 함수(Higher order function): 함수를 인자로 전달받거나 함수를 결과로 반환하는 함수

- Kotlin에서 reified 키워드를 사용하는 이유
    - 개요
        - 코틀린의 인라인 함수와 제네릭을 함께 사용할 때, 타입 정보를 런타임까지 유지하기 위해 사용하는 키워드
        - 제네릭 타입의 정보를 런타임에도 사용할 수 있도록 해주는 키워드, inline함수와 함께 사용될 때에만 가능

    - 필요 이유
        - 코틀린이나 자바에서는 제네릭 타입은 컴파일 시점에만 존재하고, 런타임에는 사라짐 (타입 소거(Type Erasure))
        - 아래 코드에서 T::class 접근시도 시 컴파일 오류 발생
        - inline + reified 사용하면 제네릭 타입 T의 정보를 런타임까지 유지 가능
        - T::class, is T, T::class.java 등 사용 가능
        ```java
        fun <T> printType(value: T) {
            println(T::class) // 컴파일 오류!
        }
        ```
    - 예제 자료
        ```java
        inline fun <reified T> isOfType(value: Any): Boolean {
            return value is T
        }
        val result = isOfType<String>("hello")  // true

        inline fun <reified T> Gson.fromJson(json: String): T {
            return this.fromJson(json, T::class.java)
        }

        // reified 없는 경우 대안책
        // Class<T>를 직접 넘겨줘야 함
        fun <T> fromJson(json: String, clazz: Class<T>): T {
            return Gson().fromJson(json, clazz)
        }
        ```

- Kotlin에서 extension function을 활용하는 방법
    - 개요
        - 확장 함수는 기존 클래스의 소스를 수정하지 않고, 외부에서 마치 클래스의 멤버 함수처럼 새 기능을 추가하는 방법

    - 기본 문법 예제
        - String 클래스에 capitalizeFirst()를 마치 내장된 함수처럼 호출 가능
        - 실제로는 정적 메서드로 컴파일되지만 문법적으로는 확장처럼 보임
        ```java
        fun String.capitalizeFirst(): String {
            if (this.isEmpty()) return this
            return this[0].uppercaseChar() + this.substring(1)
        }

        val name = "aiden"
        val capitalized = name.capitalizeFirst()  // "Aiden"
        ```

    - 활용 예시
        - 컬렉션 확장
            ```java
            fun List<Int>.sumOfSquares(): Int = this.sumOf { it * it }

            val result = listOf(1, 2, 3).sumOfSquares() // 14
            ```
        - Context 관련 확장
            ```java
            fun Context.toast(msg: String) {
                Toast.makeText(this, msg, Toast.LENGTH_SHORT).show()
            }

            // 사용
            context.toast("Hello!")
            ```
        - View 관련 확장
            ```java
            fun View.visible() { this.visibility = View.VISIBLE }
            fun View.gone() { this.visibility = View.GONE }

            // 사용
            button.visible()
            ```
    - 확장 함수, 멤버 함수 충돌 발생의 경우
        - 멤버 함수 우선순위 높음
        - 확장 함수는 정적 바인딩, 멤버 함수는 동적 디스패치

- Kotlin에서 operator overloading을 구현하는 방법
    - 개요
        - Kotlin은 특정 키워드 operator 사용하여 연산자(+,-,[],+=,==등)를 사용자 정의 타입에서 오버로딩할 수 있게 해줌

    - 기본 문법
        ```java
        data class Point(val x: Int, val y: Int) {
            // + 연산자는 내부적으로 plus() 메서드를 호출
            operator fun plus(other: Point): Point {
                return Point(this.x + other.x, this.y + other.y)
            }
        }

        val p1 = Point(1, 2)
        val p2 = Point(3, 4)
        val p3 = p1 + p2  // Point(4, 6)
        ```

    - 주요 operators
        - plus, minus, times, div, rem(%), get, set(a[i] = x), plusAssign (+=), equals (==), rangeTo (1..5), contains(x in list), invoke(foo())

    - 안드로이드 실무 예시
        - Dp + Dp 또는 Offset + Offset 연산 등 UI 컴포넌트 연산 지원
        - Compose에서 Modifier.then() / += 스타일로 사용
        - DSL 구조 만들 때 invoke 오버로드

- Kotlin에서 delegation을 활용하는 방법
    - 정의
        - 클래스의 일부 기능을 다른 객체에 맡기는 설계 패턴
        - 코틀린에서는 언어 차원에서 지원 (by 키워드)

    - 대표적 두가지 위임 방식
        - Interface Delegation(구현 위임)
            - 다른 클래스에 인터페이스 구현을 위임 (by)
        - Property Delegation(속성 위임)
            - get() / set() 동작을 커스텀 위임자로 맡김 (by lazy, by Delegates.observable 등)

    - Interface Delegation
        ```java
        // 인터페이스 정의 코드
        interface Printer {
            fun print()
        }

        class RealPrinter : Printer {
            override fun print() = println("진짜 프린터 출력")
        }

        // Delegation
        // PrinterProxy는 Printer 인터페이스를 직접 구현하지 않고도 위임으로 기능 제공
        class PrinterProxy(private val delegate: Printer) : Printer by delegate

        // 사용하는 부분 코드
        val proxy = PrinterProxy(RealPrinter())
        proxy.print()  // RealPrinter의 print() 호출
        ```

    - Property Delegation
        - by lazy
            - 처음 접근 시에만 계산 중... 출력 (지연 초기화)
            - 이후부터는 캐싱됨
            ```java
            val heavyValue: String by lazy {
                println("계산 중...")
                "무거운 값"
            }
            ```

        - Delegates.observable
            - 값이 변경될 때마다 자동 콜백 발생 (LiveData 와 유사)
            ```java
            import kotlin.properties.Delegates

            var name: String by Delegates.observable("초기값") { prop, old, newv ->
                println("[$prop.name] $old → $newv")
            }
            ```

        - Custom Delegate 직접 구현
            ```java
            class MyDelegate {
                private var value: String = ""
                
                operator fun getValue(thisRef: Any?, property: KProperty<*>) = value
                operator fun setValue(thisRef: Any?, property: KProperty<*>, newValue: String) {
                    println("setValue 호출됨: ${property.name} = $newValue")
                    value = newValue
                }
            }

            var customProp: String by MyDelegate()
            ```

- Kotlin에서 typealias를 사용하는 이유
    - 정의
        - 기존 타입(클래스, 함수, 제네릭 등)에 새로운 이름(별칭)을 부여하는 기능
        ```java
        typealias ClickHandler = (View) -> Unit
        ```

    - 사용 이유
        - 가독성 향상: 복잡한 타입 선언을 읽기 쉽게 만듦
        - 재사용성 향상: 동일한 함수 타입을 여러 곳에서 반복 사용 가능
        - 간접 참조로 유연성: 나중에 내부 타입을 바꾸더라도 외부 코드 수정 필요 없음
        - 플랫폼 타입 추상화: Android, iOS에서 공통 타입처럼 사용 가능 (멀티플랫폼 대응)

    - 실무 사용 예
        - Retrofit API Response	
            - typealias ApiResult<T> = Result<Response<T>>
        - RecyclerView Click	
            - typealias OnItemClickListener = (Int) -> Unit
        - ViewModel StateFlow	
            - typealias UiState = StateFlow<SomeUiModel>

- Kotlin에서 Any, Unit, Nothing 타입
    - Any
        - 모든 타입의 부모, 모든 클래스의 슈퍼 타입
        - equals(), hashCode(), toString() 존재
        - 여러 타입을 다루는 공통 파라미터 필요시 사용
    - Unit
        - 함수가 의미있는 값을 반환하지 않을 때 사용
        - Java void와 비슷하나 Kotlin에서는 Unit도 하나의 객체
        - 생략 가능
        - 명시적으로 콜백, 고차함수 등에서 반환 타입을 지정하고 싶을 때 사용
    - Nothing
        - 절대 반환되지 않는 함수의 반환 타입
        - 주로 예외 전파, 무한 루프, 비정상 종료 등의 상황에서 사용
        - 하위 타입이므로 모든 타입에 대입 가능 (예: val x: String = Nothing)
    - 3가지 타입 비교 예제
        ```java
        fun anything(): Any = "Hello"        // 어떤 값이든 가능
        fun doSomething(): Unit = println("Done") // 반환은 없지만 실제 객체로 존재
        fun neverReturns(): Nothing = throw Exception("죽었음")
        ```

- Kotlin에서 when 표현식과 Java의 switch 문법
    - 표현 형태
        - 코틀린: 표현식 (값 반환 가능)
        - 자바: 문장 (값 반환하지 않음)
    - 리턴 사용 가능
        - 코틀린: 리턴값 사용 가능
        - 자바: 기본적으로 리턴 불가능
    - 타입 유연성
        - 코틀린: 숫자, 문자열, 객체 등 자유롭게 가능
        - 자바: 자바7까지는 정수, 자바 14부터는 향상
    - 범위 비교 가능
        - 코틀린: in/!in 가능 (in 1..10)
        - 자바: 범위 비교 불가
    - 조건식 사용 가능
        - 코틀린: 부울 표현식 가능 (x > 5)
        - 자바: 불가능
    - break 필요 여부
        - 코틀린: 불필요 (자동 break)
        - 자바: 명시적 break 필요
    - default 처리
        - 코틀린: else
        - 자바: default
    - 타입 체크 가능 여부
        - 코틀린: is 로 타입 체크 가능
        - 자바: 타입 체크 안됨 (instanceof로 따로 비교 필요)

- Kotlin에서 vararg를 활용한 가변 인자 함수
    - 개요
        - 가변 인자(Variable number of arguments)를 받기 위해 사용하는 키워드
        - 자바의 String... args와 같은 개념
        - 예제
            ```java
            fun printAll(vararg messages: String) {
                for (msg in messages) {
                    println(msg)
                }
            }
            ```
    - 핵심 동작 방식
        - vararg는 여러 개의 인자를 배열로 포장해서 함수에 넘겨줌
        - 함수 안에서는 예를 들어 messages: Array<out String>형태로 다뤄짐
    - 다른 파라미터와 함께 혼용 사용도 가능
        - 예: log(priority: int, vararg messages: String) {...}
    - 배열을 넘길 때 * 스프레드 연산자 필요
        ```java
        val logs = arrayOf("하나", "둘", "셋")
        log(2, *logs) // <- * 연산자를 붙여야 vararg로 인식됨
        ```
    - 주의 사항
        - vararg는 단 하나의 파라미터에만 사용 가능
        - 위치는 마지막 파라미터 쪽에 두는 것이 일반적 (중간에 두는 것도 가능하긴 하나 사용이 제한됨)
    - 고급 사용법
        - Int형인 경우 sum() 함수 호출 가능
        - 제네릭 타입 사용 가능
            ```java
            fun <T> printList(vararg items: T) {
                items.forEach { println(it) }
            }
            ```
    - 실제 활용 케이스
        - 로깅 시스템
        - 다수의 뷰 업데이트/삭제 처리
        - DSL 작성 시 동적 컴포넌트 리스트 처리
        - Test Helper 함수에서 다수 인자 처리

- Kotlin에서 generic을 사용할 때 out과 in 키워드의 차이점
    - 개요
        - 제네릭(Generic) 선언 방식은 코틀린에서 재사용 가능한 타입 유연성을 부여할 때 사용
    - out T: 공변성(variance) 의미
        - T는 반환(출력) 전용 타입이라는 의미
        - 하위 타입을 상위 타입으로 안전하게 치환 가능 (예: String > Any)
        - 반환만 하고, 받아서 set하지는 않을 때 out 사용
        - 예제
            ```java
            fun getResult(): Result<String> = Result.Success("OK")
            val result: Result<Any> = getResult() // 허용됨, 공변성(out T)
            ```
    - in P, R
        - in P: 입력 전용 타입, 즉 P는 이 클래스 안에서 매개변수로만 사용
        - R: 제약없이 입력/출력 가능
        - in은 반공변성, 입력 타입만 허용하므로.
        - 예를 들어 SafeUseCase<in P, R> 일 때 SafeUseCase<Any, R>에 SafeUseCase<String, R>를 대입 가능 
        - 예제
            ```java
            val useCase: SafeUseCase<Any, String> = MyStringUseCase()
            // 내부에서는 P를 읽기만 가능 (set X, consume only)
            ```
    - 정리
        - out T: 출력 전용(공변성), 반환 타입으로만 사용
        - in T: 입력 전용(반공변성), 파라미터 타입으로만 사용
        - T (생략): 입력 + 출력 가능 (무공변), 유연성은 낮지만 자유롭게 사용 가능
        - 사용 이유: 재사용성, 타입 안정성 보장, 코틀린에서 PECS 원칙(Producer -> out, Consumer -> in)을 기반으로 타입을 안전하게 설계하기 위해 사용

- DSL
    - 개요
        - DSL (Domain Specific Language): 특정 목적/도메인에 특화된 작고 간결한 언어를 의미
        - 코틀린에서는 내장 언어처럼 보이게 만드는 문법적 트릭와 람다 with receiver, 확장 함수 등을 활용해서 만들 수 있다.
    - 예제
        - 설명을 위한 예제
            ```java
            // 일반 스타일
            val person = Person()
                person.name = "Aiden"
                person.age = 32

            // DSL 스타일 -> DSL -> person {... }
            val person = person {
                name = "Aiden"
                age = 32
            }
            ```
    - 코틀린의 대표적인 DSL 예시
        - build.gradle.kts
        - dependencies { ... } 내부는 람다 with receiver 구조로 되어 있음

    - DSL 핵심 기술 요소
        - Lambda with receiver: this 생략 가능한 람다(apply, with, run 등 내부 구조)
        - 확장함수: 기존 클래스에 새로운 함수 추가 가능
        - invoke 연산자: object() 형태로 유스케이스 처럼 함수처럼 호출 가능

    - DSL이 유용한 이유
        - 코드 가독성 증가
        - 선언형 스타일 UI 구성(Jetpack Compose, Anko)
        - 설정 파일, 테스트 시나리오 구성에 탁월
        - 빌더 패턴 개선 가능 

    - DSL 잘쓰는 프레임워크들
        - Gradle Kotlin DSL
        - Jetpack Compose (UI DSL)
        - Ktor(서버 DSL)
        - kotlinx.html
        - MockK, Kotest(테스트 DSL)

- Kotlin에서 SAM(Single Abstract Method) Conversion
    - SAM Conversion (Single Abstract Method Conversion)
        - 단 하나의 추상 메서드만 갖는 인터페이스(SAM)를 람다로 자동 변환해주는 코틀린 기능
        - 자바와의 상호운용성(interoperability)을 돕기 위해 자바의 함수형 인터페이스를 더 코틀린스럽게 쓰게 해주는 것

    - SAM 예
        - Runnable, Comparator<T>, ActionListener 등

    - SAM Conversion 예시 (코틀린)
        - 자바 스타일
            ```java
            val thread = Thread(object : Runnable {
                override fun run() { // 단 하나의 추상 메서드 존재
                    println("작동 중!")
                }
            })
            ```
        - 코틀린 SAM Conversion 사용
            ```java
            val thread = Thread {
                println("작동 중!")
            }
            ```

    - 동작 시점
        - 코틀린은 자바 인터페이스에 대해서만! SAM 변환을 기본 지원
        - 코틀린에서 만든 인터페이스는 기본적으로 SAM 변환 지원 X
            - Kotlin 1.4 이후부터는 fun interface 사용 시 가능
            - fun interface로 정의 시 코틀린 자체에서도 SAM Conversion 가능
            - 반환 타입과 파라미터 타입이 명확해야 가능
        ```java
        fun interface ClickListener {
            fun onClick()
        }

        fun handleClick(listener: ClickListener) {
            listener.onClick()
        }

        handleClick {
            println("클릭됨!")
        }
        ```

- Kotlin에서 try-catch와 runCatching
    - 개요
        - 예외 처리 방식
        - try-catch: 전통적인 명령형 방식
        - runCatching: 함수형 스타일로 예외를 다루기 위한 코틀린의 표준 함수
    - runCatching (함수형 스타일)
        - 결과가 Result<T> 객체로 래핑됨
        - 예외가 발생하든 말든, 결과를 함수형 체이닝 방식으로 처리
        - map, recover, getOrElse, getOrNull 등의 함수 사용 가능
        - 코드 흐름 깔끔, 선언적 스타일
        ```java
        val result = runCatching {
            riskyFunction()
        }

        result
            .onSuccess { println("성공: $it") }
            .onFailure { println("실패: ${it.message}") }
        ```
    - 추가 가공 시 예제
        - result.map {}.onSuccess {}.onFailure {} 이런식의 체이닝 처리 가능

- GlobalScope를 사용하면 안 되는 이유
    - 생명주기와 구조화된 동시성 위반
        - 애플리케이션이 종료되기 전까지 살아 있는 전역 스코프에서 실행됨
        - Lifecycle이나 ViewModel 등 UI 컴포넌트의 생명주기와 연결되지 않음
            - 액티비티가 종료되어도 코루틴이 계속 실행
            - 메모리 누수 또는 예기치 않은 동작의 원인
        - 구조화된 동시성 원칙을 위반하게 되며, 이로 인해 코루틴 취소, 예외 처리, 자원 정리가 어려워짐

    - 예외 처리의 어려움
        - GlobalScope에서 실행된 코루틴은 상위 스코프가 없기 때문에 예외 처리를 포착하기 어려움
        - 예외는 앱 전역에서 처리되지 않으면 앱이 비정상 종료될 수 있음
        - 일반적인 coroutinScope 또는 viewModelScope에서는 예외가 상위 스코프로 전달되어 안전하게 처리 가능

    - 취소(cancel)의 어려움
        - GlobalScope에서 시작한 코루틴은 참조를 별도로 저장하지 않으면 취소 불가능
        - 구조화된 스코프를 사용 시 scope.cancel() 또는 viewModel이 destroy 될 때 자동으로 취소
        - GlobalScope는 명시적인 자원 정리를 하지 않으면 무한정 백그라운드 작업이 남아 있을 수 있음

    - 테스트 어려움
        - GlobalScope는 앱 전체에 영향을 주는 전역 컨텐스트이므로
            - 단위테스트나 UI테스트에서 스코프 조절 불가능
            - 코루틴이 백그라운드에서 살아있기 때문에 테스트가 예측 불가능
        - CoroutineScope를 주입하거나 TestCoroutineScope를 사용하면 의도적으로 컨트롤 가능한 테스트 환경을 만들 수 있음

    - 스코프 선택
        - 액티비티, 프래그먼트, 뷰모델 등 -> lifecycleScope, viewModelScope
        - 명확한 범위 지닌 비동기 작업 -> CoroutineScope + Job() 조합
        - UI와 무관한 앱 전역 백그라운드 작업 -> ApplicationScope 등으로 의도적으로 별도 정의

    - GlobalScope 정리
        - 앱 전역에서 실행
        - 생명주기와 무관하게 계속 실행
        - 예외처리 및 취소의 어려움
        - 구조화된 동시성 유지에 문제 발생, 관리 어려움
        - 명확한 범위를 가진 CoroutineScope 사용 권장
        - 사용 피해야 하는 상황
            - UI와 관련된 모든 작업
            - ViewModel, Activity, Fragment에서 실행되는 로직
            - 예외 처리와 취소가 중요한 작업
            - 앱 상태에 따라 취소되어야 하는 작업

    - 예외
        - 의도적으로 전역 작업이 필요할 때 사용 가능
        - 사용 케이스
            - (1) 앱 생명주기와 무관한 전역 백그라운드 작업이 필요한 경우
                - 앱 전체에서 한 번만 실행되는 초기화 작업
                    - 앱 시작 시 네트워크 구성 초기화, 암호화 키 생성, 라이브러리 초기화 등
                    - Application 클래스에서 실행, 앱 전체 스코프에 속함
                    - CoroutineScope(ApplicationScope) 따로 생성 후 사용하는 것이 더 안전
                    ```kotlin
                    class MyApplication : Application() {
                        override fun onCreate() {
                            super.onCreate()
                            GlobalScope.launch {
                                initCryptoKeys()
                            }
                        }
                    }
                    ```

            - (2) 데모, 테스트 코드, 예제 코드에서 빠르게 결과만 보고 싶을 때
            - (3) 독립적으로 살아야 할 백그라운드 서비스 작업
                - 백그라운드에서 실행되는 JobService, AlarmManager 등에서 앱 종료 후에도 살아야 하는 독립성 있는 백그라운드 작업
                - OS에서 서비스가 종료되거나 GC 될 경우 작업 중단 가능성 존재 -> WorkManager 권장
                ```kotlin
                class MyJobService : JobService() {
                    override fun onStartJob(params: JobParameters?): Boolean {
                        GlobalScope.launch {
                            doLongRunningWork()
                            jobFinished(params, false)
                        }
                        return true
                    }
                }
                ```
            - (4) 실험적 코드, 단발성 Fire and Forget 작업
                - 로그 전송, 임시 캐시 정리처럼 결과가 UI나 사용자와 관계없는 일회성 작업
                - CoroutineScope(loggingDispatcher).launch{} 처럼 명시적 범위 사용이 더 권장
                ```kotlin
                fun logEvent(message: String) {
                    GlobalScope.launch {
                        sendLogToServer(message)
                    }
                }
                ```

- GlobalScope 없이 전역 Scope 만드는 방법
    - ApplicationScope 정의 (Application 클래스)
        - SupervisorJob을 사용하면 하나의 작업이 실패해도 다른 작업이 취소되지 않음
        - Dispatchers.Default는 CPU 바운드 작업에 적합 (계산, 로직 등)
        ```kotlin
        @HiltAndroidApp // ← Hilt 사용하는 경우, 아니면 그냥 Application 상속
        class MyApplication : Application() {

            // 전역 CoroutineScope: SupervisorJob + Dispatchers.Default
            val applicationScope = CoroutineScope(SupervisorJob() + Dispatchers.Default)

            override fun onCreate() {
                super.onCreate()

                // 예: 앱 전역 초기화 비동기 작업
                applicationScope.launch {
                    initAnalytics()
                    preloadCache()
                }
            }
        }
        ```
    
    - 의도적으로 주입해서 사용 (의존성 주입 없이도 가능)
        - 액티비티, Repository 등에서 필요할 때 applicationScope 주입해서 사용 가능
            ```kotlin
            // Application에서 가져오기
            val appScope = (applicationContext as MyApplication).applicationScope

            appScope.launch {
                // 앱 생명주기와 무관한 백그라운드 작업
                syncWithServer()
            }
            ```

    - SupervisorJob 사용 이유
        - Job()은 부모-자식 관계에서 자식이 실패하면 전체 취소
        - SupervisorJob()은 자식이 하나 실패해도 다른 자식에게 영향 없음
            ```kotlin
            val scope = CoroutineScope(SupervisorJob() + Dispatchers.Default)

            scope.launch {
                throw RuntimeException("실패!") // 여기서 실패해도
            }

            scope.launch {
                doSomethingElse() // 여기는 그대로 실행됨
            }
            ```

    - 필요 디스패쳐 정의
        - 상황에 따라 스코프를 나눠서 사용
        ```kotlin
        val ioScope = CoroutineScope(SupervisorJob() + Dispatchers.IO)
        val cpuScope = CoroutineScope(SupervisorJob() + Dispatchers.Default)
        val mainScope = CoroutineScope(SupervisorJob() + Dispatchers.Main.immediate)
        ```

- coroutineScope와 supervisorScope의 차이점
    - 목적과 기본 개념
        - coroutineScope
            - 자식 코루틴들이 모두 정상적으로 완료될 때까지 기다리는 구조
            - 코루틴 블록 안에서 구조화된 동시성(Structured Concurrency)을 구현할 때 기본적으로 사용하는 스코프
        - supervisorScope
            - 자식 코루틴 간의 실패 전파를 분리하고 싶을 때 사용
            - 즉 하나의 자식이 실패해도 다른 자식들에게 영향을 주지 않도록 격리된 실행을 허용하는 스코프

    - 예외 처리 방식의 차이
        - coroutineScope의 경우
            - 자식 코루틴 중 하나라도 예외가 발생하면, 다른 자식 코루틴도 모두 취소되고 스코프 전체가 실패로 간주 > 즉, 실패가 전파되는 구조
            ```kotlin
            coroutineScope {
                launch { /* 성공 */ }
                launch { throw Exception() } // → 모든 자식이 취소됨
            }
            ```
        - supervisorScope의 경우
            - 자식 코루틴 중 하나가 예외로 실패해도, 해당 자식만 취소되고 나머지는 계속 실행됨
            - 스코프 자체는 실패로 간주되지 않으며, 실패를 전파하지 않음
            ```kotlin
            supervisorScope {
                launch { /* 성공 */ }
                launch { throw Exception() } // → 다른 자식은 영향을 받지 않음
            }
            ```

    - 사용 시점
        - coroutineScope
            - 자식 작업들이 서로 강하게 연결되어 있을 때
            - 하나라도 실패하면 전체를 중단해야 하는 경우
                - 예: 여러 API를 병렬로 호출하는데, 하나라도 실패하면 전체화면 로딩을 실패시켜야 하는 경우

        - supervisorScope
            - 자식 작업들이 독립적인 성격인 경우
            - 하나의 실패가 다른 작업을 멈추게 해선 안되는 경우
                - 예: 여러 파일을 업로드할 때 하나는 실패해도 다른 파일은 계속 업로드해야 하는 경우

    - 정리
        - 둘 다 코루틴 빌더가 아닌 스코프 생성 함수 > 구조화된 동시성을 구성
        - 큰 차이점은 예외 전파 방식

- Job과 SupervisorJob
    - 개요
        - 둘다 부모-자식 관계를 가진 코루틴에서 중요하고 오류 전파 방식에 차이 존재
    - 중간 요약
        - Job: 부모-자식 간 오류가 전파 가능
        - SupervisorJob: 자식 코루틴의 오류가 부모나 다른 자식에게 전파되지 않음
    - Job의 특징
        - 자식 코루틴이 예외를 던지면 부모와 다른 자식들도 모두 취소
    - SupervisorJob의 특징
        - 자식 중 하나가 실패해도 다른 자식 코루틴에는 영향을 주지 않음
        - 독립적 실행 보장, 독립적 작업에 적합
    - 사용 사례
        - 네트워크 호출, 파일 쓰기 등 모두 실패 시 중단: Job
        - UI 컴포넌트 여러개 동작 중 하나 실패해도 유지: SupervisorJob
        - ViewModel 내 동시 작업, 한 작업 오류: SupervisorJob (많이 사용)

- Flow와 Channel의 차이점
    - 개요
        - 둘 다 비동기 스트림을 처리하기 위한 도구이나 설계 목적, 동작 방식 그리고 사용 패턴이 다름
    - Flow: 선언형, 콜드 스트림
        - collect()를 호출해야 실행되는 구조
        - collect()를 호출하는 시점부터 emit()이 시작됨
        - 1:N 구조에서 N명 모두 동일한 데이터 스트림을 별도로 실행
        - 리액티브 스타일 map, filter, debounce 등 체이닝 가능
    - Channel: 명령형, 핫 스트림
        - 누가 소비하든 말든 보내면 실행됨
        - 1:1 구조에 적합 (생산자 <-> 소비자)
        - send(), receive()를 명시적으로 호출해야 함
        - send()가 먼저 실행되어도 receive()가 기다리고 있어야 소비됨
    - Channel 예제
        ```java
        val channel = Channel<Int>()
        launch {
            channel.send(1)
            channel.send(2)
        }
        launch {
            println("받음: ${channel.receive()}")
            println("받음: ${channel.receive()}")
        }
        ```

- StateFlow와 SharedFlow의 차이점
    - 개요
        - Kotlin Flow의 일종, UI 상태 처리나 이벤트 처리에 자주 사용
        - 플로우의 확장 버전
        - 둘 다 Hot Flow(앱 실행 중 계속 살아 있음)
        - 둘 다 구조 동일 (emit() > collect() 구조)
        - UI와 뷰모델간 단방향 데이터 흐름(Uni-directional flow) 구현할 때 자주 사용됨
    - StateFlow
        - 항상 현재 상태를 가지고 있는 상태값 전용 플로우
        - 주요 특징
            - State(상태) 개념을 가짐 → 항상 마지막 값 1개를 유지
            - 초기값이 필요함 (MutableStateFlow("초기값"))
            - 새로운 수집자(collector)가 생기면 가장 최근 값 1개를 즉시 받음
            - UI 상태 처리에 최적 (예: 현재 화면 상태, 데이터 상태 등)
    - SharedFlow
        - 이벤트를 여러 구독자에게 브로드캐스팅하는 목적의 Flow
        - 주요 특징
            - 상태 없이 이벤트자체를 발행 (값 유지하지 않음)
            - 초기값 불필요
            - 최근 값을 기억할 수도 있음 (replay 설정)
            - 새로운 수집자는 이전 값 없이 현재부터 수신
                - 단, replay > 0이면 버퍼된 값도 받음
            - UI 단 단발성 이벤트 처리에 적합 (예: 토스트, 네비게이션, 알림 등)
    - 정리
        - StateFlow: 화면 상태를 지속적으로 표현할 때 (예: 로딩/성공/실패 상태)
        - SharedFlow: 클릭 이벤트, 메시지, 네비게이션 등 1회성 이벤트 처리에 적합

- Flow에서 buffer()와 conflate()의 차이점
    - 개요
        - 백프레셔 처리를 위한 대표적인 방식들
        - 어디에서 데이터를 얼마나 저장하고, 어느 시점의 값을 전달할 것인가에서 차이가 있음
    - 백프레셔(Backpressure)
        - 데이터를 생성하는 속도가 데이터를 소비하는 속도보다 빠를 때 생기는 과부하 현상.
    - buffer(): 버펴 큐에 값을 순차적으로 저장
        - 동작 방식
            - 생산자가 데이터를 빠르게 방출해도 소비자가 처리할 때까지 내부 큐에 보관
            - 모든 값이 순서대로 소비
            - 버퍼 크기를 지정하지 않으면 기본은 64
        - 특징
            - 데이터 손실 없음
            - collect가 느려도 데이터는 전부 수집됨
            - 메모리 증가 가능성 존재
    - conflate(): 최신값만 유지, 이전 값은 덮어쓰기
        - 동작 방식
            - 소비자가 처리 중일 때 새 값이 오면 기존 값은 버리고 최신값으로 덮어씀
            - 즉, 가장 최신 상태만 유지
        - 특징
            - 중간값 손실 가능성 있음
            - UI 상태 업데이트 처럼 과거 상태가 중요하지 않은 경우 유리
            - 메모리 사용이 낮고 효율적
    - 실제 사용 예
        - UI 상태 업데이트: conflate()
            - StateFlow, LiveData, collectLatest와 같이 동작
        - 모든 이벤트 로깅은 buffer()
            - 서버 전송, 로그 저장 등에서는 중간값도 중요
    - 추가 정보
        - collectLatest와 conflate 동작 차이
            - conflate() 중간 값 스킵 (이전 작업은 끝냄)
            - collectLatest {}는 새 값이 오면 이전 작업 취소하고 새로 시작
            - 결론은 conflate()는 이전 작업을 끝내고 중간은 스킵, collectLatest{}는 이전 작업 취소하고 신규 값 올 시 새로 시작하는 원리임

- flowOn()을 사용할 때 발생할 수 있는 문제
    - 개요
        - flowOn(dispatcher)은 Flow의 upstream 즉 데이터 생성 쪽의 실행 context(Dispatcher)를 바꿔주는 연산자
        - 코드 예제
            ```java
            flow {
                emit(loadFromDisk()) // 이 부분만 Dispatchers.IO에서 실행됨
            }.flowOn(Dispatchers.IO)
            ```
    - 안전하게 사용하는 방법
        - 데이터 emit + 처리 가공까지 모두 IO > flow{...}.map{...}.flowOn(Dispatchers.IO)
        - collect 쪽에서 무거운 작업 시 > withContext(Dispatchers.IO) { collect (...) }
        - 예외를 처리하고 싶을 때 > catch{}는 flowOn()보다 위에 위치
            - 추가 설명
                - flowOn()은 코루틴 컨텐스트를 변경하는 것이기 때문에 이전까지의 코루틴 스코프와 Context가 달라져서 취소, 예외 핸들링 문제가 발생할 수 있음
                - flowOn() 위에서 발생한 예외가 catch까지 전파되지 않는 경우가 있음
        - context 전환 과다 회피 > flowOn은 최소 사용 지향

- Cold Stream과 Hot Stream
    - Cold Stream
        - 개념
            - 데이터를 소비자가 구독할 때까지만 기다리고 있다가, 구독이 시작되면 그때부터 데이터를 생산(emit)하는 흐름
            - 시작 시점: collect() 호출 시 시작
            - 데이터 소비: 구독자마다 독립된 스트림
            - 재사용: 구독할 때마다 새롭게 실행됨
        - 대표적인 Cold Stream
            - flow{}, asFlow{}, sequence{}
        - 장점
            - 필요할 때만 실행 > 불필요한 리소스 사용 없음
            - 매번 다른 조건, 다른 환경으로 다이나믹하게 실행 가능
            - 구독자마다 독립된 결과가 필요한 로직에 적합
        - 비유: 주문하면 그때 만들어주는 커피
        - 예시
            ```java
            // collect 하기 전까지는 "Flow 시작됨" 도 실행되지 않음
            val myFlow = flow {
                println("Flow 시작됨")
                emit(1)
                emit(2)
                emit(3)
            }
            myFlow.collect { println("값: $it") }
            ```
    - Hot Stream
        - 개념
            - 시작 시점: 생성되자마자 동작 시작 (항상 뜨거움)
            - 데이터 소비: 구독자는 중간부터 수신 가능
            - 재사용: 같은 데이터를 여러 구독자가 공유
        - 추가 설명
            - 이미 돌고 있음
            - 구독자들은 그 흐름에 끼어드는 구조
            - 대표적 예: SharedFlow, StateFlow, RxJava의 Subject, LiveData
        - 비유: 커피포트에 계속 끓고 있는 커피

- Cold Flow와 Hot Flow의 차이점
    - 핵심 차이 요약
        - 데이터 생성 시점
            - Cold Flow: collect 호출 시마다 새로 시작
            - Hot Flow: 이미 시작됨, 구독자 없이도 계속 동작 가능
        - 구독자 처리 방식
            - Cold Flow: 각 구독자마다 독립적인 데이터 흐름
            - Hot Flow: 모든 구독자가 같은 데이터 흐름 공유
        - 예시
            - Cold Flow: flow{}. asFlow{}, sequence{}
            - Hot Flow: StateFlow, SharedFlow, LiveData
        - 기본 동작
            - Cold Flow: 늦게 collect 해도 처음부터 다시 emit
            - Hot Flow: 늦게 collect 하면 최근 상태나 최신 emit만 받음
        - 메모리/리소스 흐름
            - Cold Flow: 필요할 때만 동작 > 효율적
            - Hot Flow: 항상 동작 중이므로 제어 필요
    - 사용 시점에 따른 선택
        - 매 요청마다 새로운 작업 필요(API 호출 등): Cold Flow (flow{})
        - UI 상태 유지, 최신값만 필요할 때: Hot Flow (StateFlow)
        - 다수 구독자에게 이벤트 전파할 때: Hot Flow (SharedFlow)
        - 테스트, 순차 작업용 임시 흐름: Cold Flow

- sequence {}와 Flow {}
    - 개요
        - 둘 다 지연 계산(lazy evaluation)을 제공하는 스트림형 컬렉션
        - 동작 환경, 비동기 처리, 쓰임새에 있어서 차이 존재
        - sequence{}는 동기 지연 계산, flow{}는 비동기 지연 계산을 위한 스트림
    - sequence {}: 동기식 Lazy 스트림
        - 단일 스레드, 동기 방식
        - yield() 통해 값을 순차적으로 반환
        - 컬렉션처럼 사용 가능 (for, map, filter 등 사용 가능)
        - iterator()로 내부 동작
        - yield는 일시 중단하면서 다음 값 반환 > 다음 호출 때 이어서 진행
        ```java
        val seq = sequence {
            yield(1)
            yield(2)
            yield(3)
        }
        // for 문 사용 가능 (내부 iterator 동작)
        for (value in seq) {
            println(value)
        }
        ```
    - flow {}: 비동기식 스트림 (Cold Stream)
        - 비동기방식으로 값 emit
        - emit() 사용 > suspend 함수
        - 코루틴 기반이므로 delay(), 네트워크, DB 등 비동기 작업과 궁합 좋음
        - collect() 호출해야 실행(emit)됨 (Cold Stream)

    - 차이점
        - sequence 에서는 서스펜드 함수 사용 불가능
        - sequence 는 현재 스레드, flow는 코루틴 디스패처에서 실행
        - sequence 는 호출 후 바로 사용 가능, flow는 collect 호출 시 동작
        - sequence 는 계산, 반복, 간단한 지연처리에 적합, flow는 비동기 데이터 스트림, UI, 네트워크 등 처리에 적합

- debounce()와 throttleFirst()의 차이점
    - 개요
        - 둘 다 이벤트 발생 빈도를 제어하기 위한 연산자이나 동작 방식이 정반대
    - debounce: 마지막 이벤트만 처리
        - 짧은 시간 간격으로 들어온 이벤트들을 무시하고, 마지막 이벤트만 처리
        - 입력 완료 후 일정 시간 지났을 때만 발동됨
        - 사용 예: 검색창 자동완성, 입력 필터, 네트워크 요청 최소화 등
        ```java
        flowOf("H", "He", "Hel", "Hell", "Hello")
            .debounce(500)
            .collect { println(it) }  // 마지막 "Hello"만 출력
        ```
    - throttleFirst: 첫 번째 이벤트만 처리
        - 특정 시간 동안의 이벤트 중 첫 번째만 처리하고 나머지는 무시
        - 이후 다시 시간 창이 열리면, 다시 첫번째 이벤트만 처리
        - 사용 예: 버튼 연타 방지, 과도한 네트워크 요청 방지, 게임 조작 등 빠른 반응 1회만 필요 시
        ```java
        button.clicks()
            .throttleFirst(1, TimeUnit.SECONDS)
            .subscribe { println("클릭 처리됨!") }
        ```
    - Kotlin Flow 에서 throttleFirst() 사용 시
        - 직접 구현 및 확장함수 구현 필요
        ```java
        fun <T> Flow<T>.throttleFirst(windowDuration: Long): Flow<T> = channelFlow {
            var lastEmissionTime = 0L
            collect { value ->
                val currentTime = System.currentTimeMillis()
                if (currentTime - lastEmissionTime >= windowDuration) {
                    lastEmissionTime = currentTime
                    send(value)
                }
            }
        }
        ```

- Kotlin의 바이트코드 최적화 과정
    - 개요
        - 코틀린이 컴파일되어 자바 바이트코드로 변환된 뒤 어떻게 최적화되는가에 대한 내용
        - 코틀린의 바이트코드 최적화 과정은 코틀린 > 자바 바이트코드 변환 시의 컴파일러 최적화와 JVM 런타임(JIT) 최적화, 그리고 인라인, 람다, null 처리 최적화로 구성

    - 최적화 흐름
        - (1) 코틀린 컴파일러가 kt > class(자바 바이트코드) 변환
        - (2) 이 과정에서 코틀린 컴파일러가 자체적으로 스마트 캐스트, 인라인 함수, 람다 최적화를 수행
        - (3) 생성된 class는 JVM이 JIT 컴파일을 통해 실행 시점에서 추가로 최적화
        - (4) 경우에 따라 ProGuard / R8 같은 도구로 dead code 제거, 인라이닝, obfuscation(난독화) 수행

    - 코틀린 컴파일러의 바이트코드 최적화 기능
        - (1) 스마트 캐스트 최적화
        ```java
        val x: Any = "Hello"
        if (x is String) {  // 타입 체크 후 중복 캐스팅 생략 최적화
            println(x.length) // 자동 캐스트 → 바이트코드에서 중복 검사 제거
        }
        ```

        - (2) 인라인 함수 최적화
            - inline 키워드를 사용하면 함수 호출 자체를 바이트코드에서 제거하고
            - 함수 본문을 호출 위치에 그대로 삽입해서 성능 최적화
            - 호출 오버헤드 감소 효과, 람다 캡쳐 비용 축소 (남용 시 코드 부풀림 이슈 존재)
            ```java
            inline fun runWithLog(block: () -> Unit) {
                ...
                block()
                println("끝")
            }
            ```

        - (3) 람다 최적화 (Lambda Lifting & SAM conversion)
            - 코틀린은 람다를 클래스 인스턴스로 캡슐화 하지만
            - 가능할 경우 정적 메서드로 변환하거나 캡쳐 없이 최적화된 객체로 생성함

        - (4) Null 안전 코드 최적화
            - 코틀린은 바이트코드에서 IFNULL, IFNONNULL, ATHROW 등을 효율적으로 사용하여 자바보다 더 안전한 널 체크 로직 생성

    - JVM 런타임(JIT)의 바이트코드 최적화
        - 코틀린 컴파일러는 JVM과의 최적화를 위해 표준 자바 바이트코드 구조를 따름
        - JVM의 JIT(Just-In-Time) 컴파일러는 실행 중 아래 런타임 최적화 수행
            - (1) 인라이닝: 자주 호출되는 메서드 > 호출 없이 직접 삽입
            - (2) 루프 언롤링: 반복문 구조 최적화
            - (3) escape analysis: 객체를 힙이 아닌 스택에 할당할 수 있는지 분석
            - (4) dead code elimination: 실행되지 않는 코드 제거
            - (5) GC 최적화: 객체 생명주기 분석을 통한 메모리 정리 효율화

- Kotlin의 delegate 패턴을 사용하는 이유와 성능적 이점
    - 개요
        - delegate 패턴은 코드의 재사용성, 가독성, 캡슐화, 동작 위임을 향상시키기 위한 강력한 기능

    - delegate 패턴 사용 이유
        - 코드 재사용성
            - 여러 클래스에서 공통되는 로직(속성 위임, 상태 저장, 로깅 등)을 중복없이 재사용 가능
            - by lazy, by Delegates.observable 등은 대표적인 표준 델리게이트 구현체

        - 책임 분리와 캡슐화
            - 복잡한 기능을 별도 클래스로 위임하여, 메인 클래스는 비즈니스 로직에 집중할 수 있음
            - 관심사 분리 용이 -> 유지보수, 테스트 용이
            ```kotlin
            class LoggingDelegate<T> : ReadWriteProperty<Any?, T> {
                private var value: T? = null
                override fun getValue(thisRef: Any?, property: KProperty<*>): T {
                    println("값 조회됨: ${property.name}")
                    return value!!
                }
                override fun setValue(thisRef: Any?, property: KProperty<*>, value: T) {
                    println("값 변경됨: ${property.name} = $value")
                    this.value = value
                }
            }

            // Delegate 호출 부분
            var message: String by LoggingDelegate()
            ```

        - 기능 확장 유연
            - 상속보다 조합(Composition) 방식으로 객체 동작을 정의할 수 있음
            - Kotlin의 interface delegation (by interface) 문법은 Java에는 없는 기능
            ```kotlin
            interface Printer {
                fun print()
            }

            class DefaultPrinter : Printer {
                override fun print() = println("프린트!")
            }

            class Report(printer: Printer) : Printer by printer
            ```
    - delegate 패턴의 성능적 이점
        - lazy 연산 최적화 (by lazy)
            - 값이 실제로 사용될 때만 계산되므로 메모리와 연산 비용 절약
            - 특히 앱 초기화 시점에 무거운 객체 생성을 미루는 데 유리
            ```kotlin
            val data by lazy { loadDataFromDisk() } // 호출 시점까지 연기
            ```
        - observable & vetoable로 이벤트 최소화
            - 상태 변경에 따른 부수효과를 정교하게 감지 가능
            - 불필요한 연산/렌더링/UI 업데이트 감소 가능
            ```kotlin
            var count by Delegates.observable(0) { _, old, new ->
                if (old != new) {
                    println("값 변경: $old → $new")
                }
            }
            ```
        - 캐시/메모이제이션 구현 최적화
            - lazy, custom delegate를 활용 -> 결과 캐싱이 자동화되어 연산 중복 방지
        - 프로퍼티 접근을 캡슐화하여 추적/측정 용이
            - getter/setter 직접 오버라이드 대신, delegate를 통해 접근 흐름을 추적하거나 로깅 가능
            - 성능 분석이나 디버깅 시 유용

    - 결론
        - Delegate 패턴은 기능 위임 + 코드 재사용성 구현 목적의 패턴
        - by lazy, observable, interface delegation 등 -> 성능 최적화, 관심사 분리, 유지보수성 향상, 값 지연 계산, 캐싱, 이벤트 감지 최적화


- Kotlin의 스마트 캐스팅(Smart Casting)의 내부적 처리 방법
    - 스마트 캐스팅 (Smart Casting)
        - 코틀린이 변수 타입 검사 결과를 기억하고, 이후 코드에서 자동으로 해당 타입으로 캐스팅 해주는 컴파일러 기능
            ```kotlin
            fun printLength(obj: Any) {
                if (obj is String) {
                    // 여기서 obj는 스마트 캐스트되어 String으로 간주됨
                    println(obj.length)
                }
            }
            ```
    - 스마트 캐스팅의 내부 처리 방식
        - 컴파일 타임 캐스팅 최적화
            - 런타임 캐스팅이 아니라 컴파일러가 분석한 결과로 결정됨
            - 컴파일러는 다음을 통해 스마트 캐스트 판단
                - 변수의 불변성(immutability)(val)
                - 분기문(is/!is/null check) 조건
                - 분기 이후 절대로 타입이 바뀌지 않음을 보장할 수 있는 경우
        - 실제 컴파일 결과
            ```kotlin
            if (obj is String) {
                println(obj.length)
            }
            ```
            - 컴파일 시 내부적으로는 아래와 같이 처리됨 (Java 바이트코드 수준)
            - 개발자에게는 암묵적으로 표현되나, 컴파일러는 명시적인 타입 체크 + 캐스팅 코드로 변환하여 처리
            ```java
            if (obj instanceof String) {
                String str = (String) obj;
                System.out.println(str.length());
            }
            ```

    - 스마트 캐스팅이 불가능한 상황
        - 항상 가능한 것은 아니며, 컴파일러가 타입 안정성을 보장할 수 없다면 거부 처리
            - 예시 1: var로 선언된 변수
                - 다른 스레드나 블록에서 값이 바뀔 가능성이 있으므로 불가능
                - 해결은 var -> val로 변경

            - 예시 2: 커스텀 getter 사용
                - val 이긴 하지만 get() 호출할 때마다 값이 바뀔 수 있기 때문에 불가능
                ```kotlin
                val obj: Any
                    get() = ...

                if (obj is String) {
                    println(obj.length) // 스마트 캐스트 불가
                }
                ```

    - 스마트 캐스트 활용 정리
        - is / !is 검사 후 분기: 스마트캐스트 발생 (val인 경우, 커스텀 get 없는 경우)
        - null체크 후 안전 사용: null 제외 후 스마트캐스트 가능
        - when 조건식 내부: 각 분기에서 자동 캐스트
        - 커스텀 클래스의 필드 검사: val 이면 캐스트 가능, var은 변동성으로 인해 불가능

- Kotlin에서 객체 풀(Object Pool)을 활용하여 성능을 개선하는 방법
    - 개요
        - 빈번하게 생성, 소멸되는 객체의 재사용을 통해 성능과 메모리 효율을 높이는 전략
        - 자주 생성되는 객체를 미리 만들어두고 재사용함으로써 GC 비용을 줄이고 메모리 할당을 최적화

    - 필요성
        - 객체가 반복적으로 빠르게 생성되고 버려질 때 (GC 횟수 증가하고 메모리 부하도 커짐)
        - 게임, 애니매이션, 실시간 네트워크, UI 렌더링 (같은 타입의 객체가 반복적으로 사용됨)
        - Object Pool을 사용하면 필요한 만큼만 만들어서 재사용 가능

    - 기본 구조 구현
        - ArrayDeque, Stack, Queue 등 활용해 직접 구현 가능
        - 반환 처리 필수 (메모리 누수 가능성)
        - 쓰레드 동기화 필요 (멀티스레드 환경에서는 synchronized or ConcurrentLinkedQueue 등 사용)
        - 이전 상태 제거를 위해 reset 초기화 필수
        ```java
        class ObjectPool<T>(private val factory: () -> T, private val reset: (T) -> Unit) {
            private val pool = ArrayDeque<T>()

            fun get(): T {
                return if (pool.isEmpty()) factory() else pool.removeLast()
            }

            fun release(obj: T) {
                reset(obj)
                pool.addLast(obj)
            }
        }

        // 사용 예제
        data class Bullet(var x: Int = 0, var y: Int = 0)

        val bulletPool = ObjectPool(
            factory = { Bullet() },
            reset = { it.x = 0; it.y = 0 }
        )

        val bullet = bulletPool.get()
        bullet.x = 100
        bullet.y = 200

        // 사용 후 반환
        bulletPool.release(bullet)
        ```
    - Android SDK 자체도 객체 풀 전략 적용하고 있음
        - 예: 리싸이클러뷰, RecyclerView.RecycledViewPool, BitmapPool
        - 스크롤 시 뷰 홀더가 사라질 때 GC하지 않고 재활용함
        - 뷰홀더 객체를 계속 재사용하여 성능 극대화

    - Coroutine 관련 객체 재사용 예시
        - Kotlin Coroutines에서는 내부적으로 Continuation이나 DispatchQueue도 풀링되는 구조
        - 사용자가 직접 풀링을 할 경우에도 유사한 방식으로 관리할 수 있음

    - Apache Commons Pool 등 외부 라이브러리 활용도 방법
        - GenericObjectPool<T> 등을 사용하여 연결, 버퍼, 파서 등 풀링 가능

- launch와 async, withContext의 차이점
    - 개요
        - 모두 코루틴을 전환하거나 실행하는데 사용됨
    - 개념
        - launch
            - 새로운 코루틴을 시작하고, 병렬적으로 비동기 작업을 수행
                - 결과 반환하지 않음
                - 작업을 실행만 하면 되는 경우에 사용
                - 비동기 실행 (fire and forget)스타일
                ```kotlin
                launch(Dispatchers.IO) {
                    doSomeWork()
                }
                ```
        - withContext
            - 지정된 컨텍스트(예: Dispatchers.IO)에서 코드 블록을 실행하고 결과를 반환함.
                - 일시적으로 context를 전환
                - 결과를 반환하는 함수
                - 일반적으로 함수 내에서 특정 작업을 일시적으로 IO 쓰레드 등에서 처리할 때 사용

    - 주요 차이
        - launch
            - 새 코루틴 시작
            - 반환값 없음, Job객체 반환
            - 사용 목적은 병렬 실행
            - 예외 전파됨
            - suspend 아님
        - withContext
            - 현재 코루틴 안에서 context만 전환
            - 결과 반환
            - 사용 목적은 컨텍스트 전환 후 결과 사용
            - 예외 전파됨
            - suspend 함수임

    - 예시 비교
        - launch (백그라운드에서 로그만 남기는 경우)
            ```kotlin
            fun logUserEvent(event: String) {
                CoroutineScope(Dispatchers.IO).launch {
                    logToServer(event)
                }
            }
            ```
        - withContext (백그라운드에서 데이터 불러오고 UI에 반영)
            ```kotlin
            suspend fun fetchUser(): User {
                return withContext(Dispatchers.IO) {
                    api.getUserInfo()
                }
            }
            ```

    - launch, async+await 차이
        - launch: 결과없이 코루틴 실행
        - async: 결과를 반환하는 코루틴 실행
        - withContext: 컨텍스트를 바꾸며 결과 반환
        ```kotlin
        val deferred = async { computeValue() }
        val result = deferred.await()   // async는 await와 함께 사용
        ```

- runBlocking을 사용할 때의 문제점
    - 개요
        - 강력한 기능이나 남용, 오용시 심각한 성능 문제를 유발
    - 개념
        - 코루틴을 블로킹 방식으로 실행하는 특수한 함수
        - 코루틴을 실행하고 해당 블록이 끝날 때까지 현재 스레드를 차단
        ```kotlin
        fun main() {
            runBlocking {
                val result = fetchData()
                println("결과: $result")
            }
        }
        ```
        - 주로 사용 위치
            - 테스트 코드
            - main()함수 (entry point)
            - UI 및 뷰모델에서는 비권장
    - 동작 방식
        - 내부적으로는 스레드를 "정지(block)" 시켜서 동작을 기다림
        - 일반 launch, async는 비동기적이지만, runBlocking은 동기적 기다림

    - 사용 시 문제점 리스트
        - UI 쓰레드 블로킹
            - Android에서 runBlocking을 UI 스레드에서 사용하면 앱이 멈추고, ANR 발생 가능
        - 비동기 성능 저하	
            - 코루틴의 장점인 비동기 처리/경량 스레드 특성을 상쇄
        - 데드락 가능성	
            - 내부에서 다른 suspend 함수나 withContext 등이 동작 못하고 데드락 발생할 수 있음
        - 구조적 동시성 위반
            - runBlocking은 스코프 컨트롤 없이 독립적으로 실행되므로 부모 코루틴과 관계 없음
        - 실무 코드에 부적절
            - 테스트나 CLI 앱이 아닌 Android UI 환경에서는 사용 비추천

    - 사용 시기
        - 단위 테스트: 사용 OK (JUnit 등에서 runBlockingTest 권장)
            - runTest { ... } 또는 runBlockingTest (코루틴 테스트 라이브러리 사용)
        - main() 진입점: main 함수에서 suspend 함수 실행할 때

- CoroutineContext의 주요 요소(Job, Dispatcher, ExceptionHandler 등)
    - 개요
        - CoroutineContext는 코루틴의 실행 환경을 구성하는 키-값 형태의 컨테이너
        - 각각의 키는 코루틴의 생명주기, 실행 스레드, 에러 처리 등에 직접적으로 관여

    - CoroutineContext 개념
        - 코루틴의 실행 정보(스레드, 상태, 예외처리자 등)를 담고 있는 컨텍스트 객체
        - 각 코루틴은 자신만의 CoroutineContext를 갖고, 필요 시 상속하거나 조합 가능
        ```kotlin
        CoroutineScope(Dispatchers.IO + Job() + CoroutineName("MyCoroutine"))
        ```

    - CoroutineContext의 주요 요소
        - Job: 코루틴의 생명주기 관리, 취소 처리, kotlinx.coroutines.Job
        - Dispatcher: 코루틴이 실행될 스레드 지정, CoroutineDispatcher
        - CoroutineName: 디버깅용 이름 태그 지정, CoroutineName
        - CoroutineExceptionHandler: 예외 처리 담당자, CoroutineExceptionHandler
        - ThreadContextElement: 스레드 로컬 데이터 연결, ThreadContextElement<T>

    - 각 요소별 상세 설명
        - (1) Job
            - 코루틴의 생명주기, 취소 제어, 구조적 동시성의 핵심
                - launch {} 나 async {} 사용 시 내부적으로 Job 생성
                - cancel(), join(), isActive 등을 통해 상태 관리 가능
                - 부모-자식 관계 자동 구성됨
                ```kotlin
                val job = Job()
                CoroutineScope(Dispatchers.IO + job).launch {
                    // 코루틴 실행
                }
                job.cancel()
                ```
        - (2) Dispatcher
            - 코루틴이 어느 스레드에서 실행될지를 지정
            - 대표적인 Dispatcher:
                - Dispatchers.Main → UI 스레드
                - Dispatchers.IO → I/O 작업 최적화
                - Dispatchers.Default → CPU 연산 최적화
                - Dispatchers.Unconfined → 상위 컨텍스트를 그대로 사용

        - (3) CoroutineExceptionHandler
            - 코루틴 예외를 처리하는 전용 핸들러 (특히 launch 계열)
                - launch 내에서 발생한 예외는 기본적으로 CoroutineExceptionHandler에 위임됨
                - async는 await() 시점에 예외 발생
                ```kotlin
                val handler = CoroutineExceptionHandler { _, throwable ->
                    println("예외 발생: ${throwable.message}")
                }

                CoroutineScope(Dispatchers.Default + handler).launch {
                    throw RuntimeException("예외!")
                }
                ```
        - (4) CoroutineName
            - 디버깅 시 유용한 이름 설정 (Logcat, debugger에서 표시됨)
            ```kotlin
            launch(CoroutineName("MyWorker")) {
                println("현재 코루틴 이름: ${coroutineContext[CoroutineName]}")
            }
            ```
        - (5) ThreadContextElement
            - 스레드 로컬(ThreadLocal) 값 전파에 사용됨
            - 예: MDC(Logback의 로그 태그), 사용자 ID 같은 정보 공유
            ```kotlin
            val threadLocal = ThreadLocal<String?>()
            threadLocal.set("main")

            val context = threadLocal.asContextElement()

            launch(context) {
                println("스레드 로컬 값: ${threadLocal.get()}")
            }
            ```
    - CoroutineContext는 어떻게 동작할까?
        - 각 코루틴은 CoroutineContext를 상속 + 덮어쓰기 가능
        - 내부적으로는 Map-like 구조로 작동 (get(), plus() 연산 지원)
        - coroutineContext 라는 키워드로 현재 컨텍스트 접근 가능 (suspend 함수 내에서만 사용 가능)

    - 전체 예제
        ```kotlin
        val handler = CoroutineExceptionHandler { _, e ->
            println("에러: ${e.message}")
        }

        val context = Dispatchers.IO + Job() + CoroutineName("MyJob") + handler

        CoroutineScope(context).launch {
            println("CoroutineContext 예시 실행")
            throw Exception("테스트 예외")
        }
        ```

- Flow와 LiveData의 차이점
    - 차이 요약
        - 플랫폼
            - LiveData: 안드로이드 전용(LifecycleOwner 필요)
            - Flow: Kotlin Core Library
        - 생명주기 연동
            - LiveData: 생명주기 자동 감지 (onStart, onStop)
            - Flow: 기본은 생명주기 미연동 (직접 처리 필요)
        - 비동기 처리
            - LiveData: 내장 안됨(별도로 MediatorLiveData, CoroutineScope 등 필요)
            - Flow: 코루틴 기반 비동기 처리 내장
        - 데이터 흐름 방식
            - LiveData: Hot Stream (항상 활성 상태)
            - Flow: Cold Stream (collect()로 시작)
        - 멀티 구독자
            - LiveData: 가능 (UI 컴포넌트에 적합)
            - Flow: 가능 (SharedFlow, StateFlow 활용 시)
        - 에러 처리
            - LiveData: 기본 에러 처리 없음 (try-catch 필요)
            - Flow: .catch{} 등 내장 에러 처리 지원
        - 반환/조합 유연성
            - LiveData: 제한적 (Transformations.map, switchMap)
            - Flow: 매우 유연 (map, flatMapConcat 등)
        - 취소 제어
            - LiveData: 수동 해제 필요
            - Flow: collect() 범위에서 자동 취소됨
    - 시점에 따른 선택
        - UI 상태를 뷰모델 > 프래그먼트 연결: LiveData / StateFlow
        - 복잡한 데이터 처리 / 조합 / 변환: Flow
        - Android 외 플랫폼 (멀티플랫폼): Flow
        - 실시간 이벤트 스트림 처리(토스트, 네비게이션 등): SharedFlow
        - 생명주기 안전한 단순 데이터 UI 표시: LiveData
    - LiveData > Flow 전환 시 고려사항
        - viewModelScope.launch 사용 필요
            - collect()는 suspend이기 때문에 코루틴 안에서 사용 필수
        - 생명주기 연동
            - repeatOnLifecycle, lifecycleScope.launchWhenX 같이 사용해야 안전
        - 상태 저장 필요 시
            - StateFlow 또는 LiveData 유지
        - 이벤트 전파
            - SharedFlow가 SingleLiveEvent 대체 가능

- SharedFlow와 StateFlow의 차이점
    - StateFlow
        - 초기값 필요: 반드시 초기값 필수
        - 최신값 저장: 항상 최신값 유지(value) 접근 가능
        - 기본 용도: UI 상태 유지용
    - SharedFlow
        - 초기값 필요: 없음 가능
        - 최신값 저장: 필요 시 replay 설정해야 함
        - 기본 용도: 일회성 이벤트 전달용 (예: 토스트)

- suspend function 내부에서 try-catch를 올바르게 사용하는 방법
    - 개요
        - 코루틴은 예외가 throw될 수 있는 구조이기 때문에 try-catch의 사용 위치와 타이밍이 중요
    - suspend 함수와 예외처리 기본 개념
        - suspend 함수는 일반 함수처럼 예외를 throw할 수 있음
            - 코루틴 내에서 실행되더라도 try-catch로 잡을 수 있음
            - 외부에서 호출할 때 try-catch로 감싸야 에러를 다룰 수 있음
    - 기본 사용 예
        ```kotlin
        suspend fun fetchData(): String {
            try {
                val result = networkCall()  // 이 suspend 함수에서 예외 발생 가능
                return result
            } catch (e: IOException) {
                // 네트워크 오류 처리
                return "Error"
            }
        }
        ```
        - 핵심 포인트
            - suspend 함수 내의 try-catch는 해당 블록 내에서 발생한 예외만 처리
            - 반드시 catch 블록에서 적절히 처리하거나 throw 다시 해야 함
    - 실전 실수
        - launch 내 예외 무시됨
        ```kotlin
        viewModelScope.launch {
            val result = fetchData() // 예외 발생 시 앱이 크래시될 수 있음
        }
        ```
            - launch 블록 내부의 예외는 전파되지 않고, 크래시 발생
            - → 별도의 try-catch로 감싸야 함

    - 올바른 예외 처리 위치
        - (1) suspend 함수 내부에서 처리
        - (2) 호출부에서 처리 (코루틴 블록 내)

    - withContext 내에서의 try-catch
        - withContext 내부도 suspend 블록이기 때문에 try-catch 사용 가능
        - 컨텍스트 전환 후에도 예외 안전하게 처리 가능

    - 코루틴 빌더별 예외 처리 차이
        - launch: 내부에서 크래시 발생,	전파안됨, 크래시 발생, 반드시 try-catch 또는 CoroutineExceptionHandler 사용
        - async: Deferred.await() 호출 시 예외 전파, await() 를 try-catch로 감싸야 함
        - withContext: 예외 발생 시 바로 전파됨, 일반 함수처럼 try-catch 가능

    - 실전 통상적인 팁
        - API 호출: suspend 함수 안에서 try-catch로 감싸고, 실패 시 null 또는 Result 반환
        - ViewModel → UI: suspend 호출부에서 try-catch로 UI 에러 상태 갱신
        - 로깅 필요: catch 블록에 Log.e(...) 또는 서버에 에러 전송
        - 복수 API 병렬 호출: async + await 시 각각의 await()를 try-catch로 감싸기

- Coroutine의 Dispatchers.Default, IO, Main의 차이점
    - 개요
        - 코루틴이 어떤 스레드에서 실행될지를 결정하는 디스패처
    - 디스패처 개념
        - 코루틴이 실행될 스레드(또는 스레드 풀)을 결정하는 컴포넌트
        - launch {}안의 코드가 어디서 실행될 지를 정하는 역할
    - 디스패처 종류
        - Main: UI 작업, TextView 업데이트, LiveData 관찰 등
        - IO: 입출력 작업, DB, 네트워크, 파일 읽기/쓰기 등
        - Default: CPU 연산 작업, JSON 파싱, 정렬, 필터링 등 무거운 계산
    - 각 디스패처의 상세 설명
        - Dispatchers.Main
            - 안드로이드의 UI 스레드(MainThread) 에서 실행됨
                - UI 컴포넌트에 접근 가능 (예: textView.text = "Hello")
                - 너무 무거운 연산을 실행하면 ANR(앱 멈춤) 발생 가능성 있음
                - 내부적으로 Looper/Handler 기반으로 작동
                - 스레드 수: 1 메인 스레드
        
        - Dispatchers.IO: Default 보다 많은 스레드 생성 허용/사용
            - 네트워크, 디스크, DB I/O 등 빠르게 블록될 수 있는 작업을 위한 스레드 풀
                - 내부적으로 최대 64개까지 동시 실행 가능한 스레드 풀 사용
                - Default보다 많은 스레드 생성 허용 → 대기 시간이 짧은 I/O에 적합
                - Room, Retrofit, File.readBytes() 등에 적합
                - 스레드 수: 많음 (최대 64)

        - Dispatchers.Default
            - CPU 집중형 작업을 위한 스레드 풀
                - 코어 수에 맞는 적정 수준의 스레드를 유지 (기본: CPU 수)
                - 무거운 계산, 정렬, 압축, JSON 파싱 등 CPU 부하 작업에 적합
                - I/O 작업보다 스레드 수 제한이 크므로 대기 작업에는 부적절
                - 스레드 수: CPU코어수

    - 디스패처 선택 가이드
        - UI 업데이트, 버튼 클릭 후 처리: Dispatchers.Main
        - Retrofit, Room, 파일 작업: Dispatchers.IO
        - JSON 파싱, 대량 데이터 연산: Dispatchers.Default
        - 테스트용 블로킹 처리: runBlocking, Unconfined (주의해서 사용)

    - 주의 사항
        - Dispatchers.IO에서 CPU 작업을 하면 스레드 낭비
        - Dispatchers.Default에서 네트워크 호출하면 스레드 부족 위험
        - Dispatchers.Main에서 무거운 작업하면 앱 멈춤(ANR) 발생

- Kotlin Coroutine에서 cancel()을 호출했을 때 실행 흐름
    - 개요
        - cancel() 호출 시 코루틴이 즉시 종료되지 않는 이유나 취소가 어떻게 전파되고 중단되는 지에 대해 숙지 필요
    - cancel() 호출 시 개념
        - cancel()은 코루틴의 Job에 취소 요청을 보내는 것이지, 즉시 강제 종료되는 것이 아님
            - 코루틴 내부 코드가 취소 상태를 점검하거나 협조적 중단을 수행해야 종료됨
            - 즉, 취소는 "요청"일 뿐, "즉시 중단"이 아님

    - 실행 흐름 단계별 정리
        - 1단계: cancel() 호출
        - 2단계: Job의 상태 -> isActive == false, isCancelled == true
        - 3단계: suspend 함수 or cancellation point에 도달하면 중단됨
            - 예: delay(), withContext, yield() 등에서 취소를 감지하고 CancellationException 발생

    - 코드 예시
        - cancel() 호출 흐름
        ```kotlin
        val job = CoroutineScope(Dispatchers.Default).launch {
            repeat(5) { i ->
                println("작업 $i 실행 중")
                delay(500) // <---- 취소 포인트
            }
            println("이건 출력되지 않음")
        }

        delay(1000)
        println("cancel 호출")
        job.cancel()
        job.join()
        println("코루틴 취소 완료")

        // 출력 결과
        // 작업 0 실행 중
        // 작업 1 실행 중
        // cancel 호출
        // 코루틴 취소 완료
        ```
    - 취소가 즉시 되지 않는 이유
        - 코루틴은 협조적으로 중단되는 구조
        - 내부 코드가 취소를 감지하려면 다음 중 하나를 해야 함:
            - 취소 가능한 suspend 함수 사용 (delay, withContext, etc.)
            - isActive 직접 확인
            - ensureActive() 호출
        - 취소가 안되는 코드
            - 취소되지 않고 끝까지 다 실행됨
            ```kotlin
            val job = launch {
                repeat(5) {
                    println("계산 중... $it") // delay가 없기 때문에 취소 포인트 없음
                }
            }
            delay(100)
            job.cancel()
            ```

    - 취소 감지 방법들
        - delay(): 내부적으로 취소 체크 포함
        - yield(): 현재 중단 + 취소 여부 확인
        - withContext: 내부에서 컨텍스트 전환 시 자동 확인
        - isActive: 현재 Job이 활성 상태인지 확인
        - ensureActive(): 비활성 상태면 CancellationException 즉시 throw

    - 취소 시 예외처리
        - cancel() 호출 후 내부에서 CancellationException 발생
        - 이 예외는 일반적으로 자동 처리되지만, try-catch로 명시적으로 다룰 수도 있음
        ```kotlin
        try {
            withContext(Dispatchers.IO) {
                delay(5000) // 여기에 취소 발생 시 중단
            }
        } catch (e: CancellationException) {
            println("코루틴이 취소되었습니다: ${e.message}")
        }
        ```

    - 부모 자식 관계와 취소 전파
        - 부모 코루틴이 취소되면 자식 코루틴도 자동으로 모두 취소됨
        - 구조적 동시성(structured concurrency)의 핵심
        ```kotlin
        val parentJob = CoroutineScope(Dispatchers.Default).launch {
            launch { delay(1000); println("자식1") }
            launch { delay(2000); println("자식2") }
        }
        delay(500)
        parentJob.cancel() // 자식들도 모두 취소됨
        ```

    - 전체 요약
        - cancel() 역할: 코루틴을 중단하라고 요청하는 것 (강제 종료 아님)
        - 실행 중단 시점: suspend 함수, isActive, ensureActive() 등에서 협조적으로 중단됨
        - 예외 처리: CancellationException 발생 (기본적으로 무시되지만 처리 가능)
        - 부모-자식 관계: 부모가 취소되면 자식도 모두 취소됨

- Flow에서 buffer()와 conflate()의 차이점
    - 개요
        - 백프레셔 처리를 위한 대표적인 방식들
        - 어디에서 데이터를 얼마나 저장하고, 어느 시점의 값을 전달할 것인가에서 차이가 있음
    - 백프레셔(Backpressure)
        - 데이터를 생성하는 속도가 데이터를 소비하는 속도보다 빠를 때 생기는 과부하 현상.
    - buffer(): 버펴 큐에 값을 순차적으로 저장
        - 동작 방식
            - 생산자가 데이터를 빠르게 방출해도 소비자가 처리할 때까지 내부 큐에 보관
            - 모든 값이 순서대로 소비
            - 버퍼 크기를 지정하지 않으면 기본은 64
        - 특징
            - 데이터 손실 없음
            - collect가 느려도 데이터는 전부 수집됨
            - 메모리 증가 가능성 존재
    - conflate(): 최신값만 유지, 이전 값은 덮어쓰기
        - 동작 방식
            - 소비자가 처리 중일 때 새 값이 오면 기존 값은 버리고 최신값으로 덮어씀
            - 즉, 가장 최신 상태만 유지
        - 특징
            - 중간값 손실 가능성 있음
            - UI 상태 업데이트 처럼 과거 상태가 중요하지 않은 경우 유리
            - 메모리 사용이 낮고 효율적
    - 실제 사용 예
        - UI 상태 업데이트: conflate()
            - StateFlow, LiveData, collectLatest와 같이 동작
        - 모든 이벤트 로깅은 buffer()
            - 서버 전송, 로그 저장 등에서는 중간값도 중요
    - 추가 정보
        - collectLatest와 conflate 동작 차이
            - conflate() 중간 값 스킵 (이전 작업은 끝냄)
            - collectLatest {}는 새 값이 오면 이전 작업 취소하고 새로 시작
            - 결론은 conflate()는 이전 작업을 끝내고 중간은 스킵, collectLatest{}는 이전 작업 취소하고 신규 값 올 시 새로 시작하는 원리임

- with, run 의 차이점
    - 공통
        - 수신 객체(this)를 기준으로 블록 실행
        - 블록의 마지막 표현식이 반환값
    - 차이점
        - with
            - 수신객체를 파라미터로 받음
            - 객체를 인자로 넘겨 블록 실행
            - 확장 함수 아님
            - 수신 객체를 명시적으로 지정하고 블록을 실행할 때 사용 (사용 이유)
            ```kotlin
            val result = with(user) {
                println(name)
                age + 1 // 반환값
            }
            ```
        - run
            - 확장 함수
            - 객체에서 직접 run 실행
            - 수신 객체에서 바로 .run{} 형태로 호출
            - 블록 내부에서 this는 수신 객체
            ```kotlin
            val result = user.run {
                println(name)
                age + 1 // 반환값
            }
            ```
        
        - 요약
            - 둘 다 this 기반, 리턴값을 받고 싶을 때 유용

- run, let 의 차이점
    - 공통
        - 확장함수
        - 블록 실행하고 마지막 표현식을 반환
    - 차이점
        - run
            - 블록 안에서 this로 수신 객체에 접근
            - 객체 초기화나 리턴값 계산 등에서 자주 사용
        - let
            - 블록 안에서 it으로 수신 객체에 접근
            - 주로 null-safe 호출, 체이닝, 일시적 컨텍스트에서 많이 사용
            ```kotlin
            val result = user?.let {
                println(it.name)
                it.age + 1
            }
            ```
        - 요약
            - run -> this 기반, 초기화나 계산
            - let -> it 기반, null-safe 처리에 특화

- let, also 의 차이점
    - 공통
        - 둘 다 it 기반 확장 함수
        - 수신 객체를 블록에 넘기고 사용함
    - 차이점
        - let
            - 블록의 마지막 결과를 반환
            - 객체의 속성을 변형하거나 가공한 값을 리턴하고 싶을 때 사용
        - also
            - 블록 실행 후 원래 객체 자체(this)를 반환
            - 객체는 그대로 유지하면서 로깅, 디버깅, 부수효과(side-effect)등 수행 시 사용
            ```kotlin
            val user = User("Lee").also {
                println("User created: $it")
            }
            // user는 그대로 반환됨
            ```

    - 전체 키워드 요약
        - with: 객체를 파라미터로 넘겨 블록 실행. this로 접근. 일반 함수.
        - run: 객체에서 바로 호출. this로 접근. 계산 결과 반환.
        - let: it으로 객체 접근. 결과를 다른 값으로 변환하거나 null-safe 처리할 때.
        - also: it으로 접근하지만 객체 그대로 반환. 로깅이나 디버깅, 체이닝에 유용.

    - 상황에 따른 사용
        - apply → "객체 초기화" (Intent, RecyclerView.Adapter, Paint 등)
        - let → "null-safe 처리" 또는 "변환이 필요한 경우"
        - also → "디버깅, 로그, 부수효과" 삽입 (원본 유지)
        - run → "값을 계산해서 리턴하고 싶을 때" (스트링 연결, 값 계산)
        - with → "여러 속성/메서드를 한 객체에 집중적으로 적용"
        ```kotlin
        val userName = intent.getStringExtra("userName")?.let {
            it.uppercase()
        } ?: "Guest"

        val user = User().apply {
            name = userName
            age = 30
        }

        user.also {
            Log.d("UserDebug", "생성된 사용자: $it")
        }
        ```

- Kotlin의 sealed class 사용 시점
    - 개요
        - 계층적으로 제한적인 타입 분기를 명확하게 하고 싶을 때 사용하는 강력한 기능
        - 특히, when 과 같이 사용하면 컴파일 타임에서 안전한 조건 분기를 만들 수 있음 (when 분기 시 모든 하위 타입을 처리하지 않으면 컴파일 오류 발생 > 안전성 보장)
    - 요약
        - sealed class 는 상속 가능한 클래스 계층을 제한하고, 모든 하위 클래스가 정해진 경우에만 사용되는 클래스
    - 사용 목적
        - 결과 타입을 명확히 나누고 싶을 때 (성공 / 실패 / 로딩 상태)
        - 분기 처리를 안전하게 하고 싶을 때 (when에서 모든 케이스를 컴파일 시 검사)
        - 계층 구조가 닫힌 상태에서만 유효할 때 (다른 파일/모듈에서 확장 못하게 막음)
        - UI 상태 표현 (Compose나 MVVM에서 UI State 분기에 적합)
        - 이벤트/명령 정의 (EventBus, Command 패턴처럼 사용 가능)
    - sealed
        - 봉인된 클래스 > 하위 타입을 이 파일 내에서만 허용
        - 파일 외부에서 상속 금지 > 타입 안정성 확보
        - 컴파일러가 모든 가능성을 알 수 있음
    - sealed interface
        - Kotlin 1.5+부터 지원
        - 클래스보다 더 유연한 타입 계층 구성 가능

- Kotlin의 companion object
    - 개요
        - 자바에서의 static 키워드 개념을 더 안전하고 유연하게 대체하기 위한 기능
        - 클래스 수준에서 공유되는 정적 멤버를 정의할 때 사용

    - 정의
        - 클래스에 소속된 정적 멤버(필드, 함수 등)를 선언하기 위한 구조
        - static 키워드 대신 companion object를 통해 클래스 레벨에서 공유되는 개체를 만들 수 있음
        

    - 주요 역할
        - 클래스의 정적(static) 멤버를 정의
            - 인스턴스를 생성하지 않아도 접근 가능
            ```kotlin
            class Utils {
                companion object {
                    const val DEFAULT_TIMEOUT = 3000
                    fun log(msg: String) = println("LOG: $msg")
                }
            }

            // 사용
            Utils.log("Hello")
            println(Utils.DEFAULT_TIMEOUT)
            ```
        - 팩토리 메서드 (Factory Method) 제공
            - 객체 생성을 내부적으로 관리하고자 할 때 자주 사용
            ```kotlin
            class User private constructor(val name: String) {
                companion object {
                    // 팩토리 메서드
                    fun create(name: String): User {
                        return User(name.uppercase())
                    }
                }
            }

            // 사용
            val user = User.create("aiden")
            ```

        - 인터페이스 구현도 가능 (객체이므로)
            ```kotlin
            interface Clickable {
                fun click()
            }

            class Button {
                companion object : Clickable {
                    override fun click() {
                        println("Clicked")
                    }
                }
            }
            ```
    - 특징
        - 클래스당 companion object는 하나만 존재 가능
        - 실제로는 클래스 내부의 singleton object로 존재
            - 런타임에는 singleton 객체로 동작
        - 클래스 이름을 통해 정적 접근 가능 (ClassName.member)
        - 정적 필드처럼 보이나 사실은 런타임 객체에 속한 멤버

    - 실제 사용 예시
        - Intent 생성 도우미
        - Fragment.newInstance() 팩토리 패턴
        - 공통 상수 정의
        - @JvmStatic과 함께 사용하여 Java에서 static처럼 호출 가능
        ```kotlin
        class MyFragment : Fragment() {
            companion object {
                fun newInstance(id: Int): MyFragment {
                    return MyFragment().apply {
                        arguments = bundleOf("id" to id)
                    }
                }
            }
        }
        ```

    - 추가 설명
        - @JvmStatic
            - Kotlin에서는 companion object 멤버를 Java에서 호출하려면 ClassName.Companion.method() 형태여야 하지만, @JvmStatic을 해당 멤버에 붙이면 자바에서도 ClassName.log("...")처럼 static처럼 호출 가능

- inline 함수와 일반 함수의 차이
    - 기본 개념
        - 일반 함수
            - 일반적인 함수 호출 방식으로, 함수를 호출하면 스택에 올라가고, 반환되며 종료됨
            - 람다를 인자로 넘기면 실행 시점에 Function 객체로 생성됨
            ```kotlin
            fun greet(name: String, block: () -> Unit) {
                println("Hello, $name")
                block() // Function 객체 실행
            }
            ```

        - inline 함수
            - 함수 호출 시 컴파일 타임에 해당 함수의 코드 자체를 호출 지점에 복붙(inline) 해주는 방식
            - 고차 함수(함수를 인자로 받는 함수)에서 불필요한 객체 생성을 줄이고 성능을 최적화할 수 있음
            - 람다가 인라인되면 Function 객체를 생성하지 않음 -> 성능 향상
            ```kotlin
            inline fun greet(name: String, block: () -> Unit) {
                println("Hello, $name")
                block()
            }
            ```

    - 차이점
        - 함수 호출 방식
            - 일반 함수: 실행 시점에 호출 스택에 올라감
            - inline 함수: 컴파일 타임에 호출 지점에 코드가 삽입됨 (함수 호출 자체가 사라짐)
    
        - 람다 처리
            - 일반 함수: 람다 = Function 객체 생성 -> 힙 메모리 사용
            - inline 함수: 람다 = 객체 생성 없이 코드가 직접 삽입됨 -> GC 부담 없음

        - 성능
            - 일반 함수: 함수 호출 오버헤드 + 람다 객체 할당
            - inline 함수: 오버헤드 없음 + 람다 객체 생성 생략 -> 더 빠름

        - 디버깅 및 코드 크기
            - 일반 함수: 호출 추적이 쉬움 (스택 프레임 존재)
            - inline 함수: 디버깅 시 코드가 여러 위치에 삽입되므로 추적이 어려울 수 있음, 또한 남용시 바이트코드 크기가 증가할 수 있음

    - inline 사용 시점
        - 사용 권장 상황
            - 람다를 자주 넘기는 고차함수
            - 성능 민감한 반복 호출 함수
            - crossinline, noinline 제어가 필요한 컨텍스트
            - 안드로이드에서 with, let, run, apply, use 등 스코프 함수처럼 많이 쓰는 유틸 함수들
        - 사용 주의 상황
            - 함수 내용이 너무 길면 -> 코드 복제 증가 -> 바이트코드 커짐
            - 람다를 저장하거나 나중에 실행해야 하는 경우 -> inline 사용 X
            - 일반적인 단순 함수 -> inline 필요 없음

    - 추가 설명
        - noinline: inline 함수 내에서 특정 람다는 인라인 되지 않게 함
        - crossinline: 람다 내에서 return 이 불가능하도록 막음

- inline class (value class)
    - 개요
        - 런타임에 불필요한 객체 생성을 줄이고 성능을 높이기 위해 도입된 경량 래퍼 클래스
    - inline class (value class) 정의
        - 하나의 프로퍼티만을 가지는 클래스
        - 컴파일 시점에는 일반 클래스처럼 보이지만, 런타임에는 해당 프로퍼티로 인라인(대체) 처리되는 구조
        - 즉, 추가적인 객체 생성 없이 클래스처럼 다루되, 성능은 기본 타입처럼 경량화된 것

    - 기본 사용법
        ```kotlin
        @JvmInline
        value class UserId(val value: String)
        ```
        - 이제 UserId는 String을 감싸는 클래스로 사용되지만, 런타임에는 실제 UserId 객체없이 String 값으로 처리

        ```kotlin
        val id = UserId("aiden123")
        println(id.value)
        ```
        - 컴파일 후 JVM 바이트코드에서는 UserId 객체 없이 "aiden123"만 남게 됨 -> 성능 향상

    - 사용 이유
        - (1) 타입 안정성 확보
            - 단순 String, Int를 직접 넘기는 대신 의미 있는 타입으로 감쌀 수 있음 (UserId)
            ```kotlin
            fun getUser(id: UserId) { ... } // String과 구분되는 안전한 타입
            ```
                - 실수로 productId: String을 넘기는 버그를 방지

        - (2) 성능 최적화
            - 일반 래퍼 클래스는 객체를 생성해야 하지만,
            - value class는 JVM에서 객체를 생성하지 않고 값만 사용함 -> 메모리 효율 + 속도 향상

    - 특징 요약
        - 단 하나의 프로퍼티만 가질 수 있음
        - 기본 타입처럼 처리되지만, 타입의 구분은 유지됨
        - @JvmInline 애노테이션이 필요 (JVM에서 inline 최적화가 적용되도록)

    - 제한 사항 (주의점)
        - 프로퍼티는 val만 가능 (불변)
        - init 블록 사용 불가
        - 상속 불가, abstract/open/interface 구현 불가
        - null 허용 시 타입은 Boxed됨 -> 인라인 최적화가 사라짐
        - 여러 프로퍼티를 가질 수 없음

    - 실제 예시
        - ID, Email, Token 같은 도메인 값의 타입 안정성 확보
            ```kotlin
            @JvmInline
            value class Email(val value: String)

            fun send(email: Email) { ... }

            send(Email("test@a.com")) // 안전
            send("test@a.com")        // 컴파일 에러
            ```

    - 전체 요약
        - inline class 즉, value class는 하나의 값을 감싸는 경량 래퍼 클래스
        - 타입 안전성은 유지하면서 런타임 객체 생성을 제거하여 성능을 향상시키는 코틀린 기능
        - ID, Email, Token 등 의미있는 값 표현에 자주 사용되며, 안드로이드에서도 Parcelable 등과 함께 활용 가능

- Kotlin의 extension function
    - 개요
        - 기존 클래스의 소스코드를 수정하지 않고도 새로운 함수(기능)를 추가할 수 있는 기능

    - 개념
        - 코틀린에서 기존 클래스에 대해 상속없이 새로운 함수를 확장 형태로 추가할 수 있도록 해주는 기능
        - 마치 그 클래스의 멤버 함수처럼 호출 가능

    - 문법과 기본 사용법
        ```kotlin
        fun String.addPrefix(prefix: String): String {
            return "$prefix$this"
        }

        val name = "Aiden"
        val newName = name.addPrefix("Mr. ")  // 출력: "Mr. Aiden"
        ```
        - String 클래스에 addPrefix라는 새로운 함수가 생긴 것처럼 사용

    - 사용 이유
        - 기존 클래스의 기능을 확장하고 싶을 때
            - 외부 라이브러리 클래스, 자바 클래스 등 수정할 수 없는 클래스에 새로운 기능을 붙이고 싶을 때 유용
        - 유틸 함수 또는 DSL 스타일의 가독성 향상
            - apply, with, run, also 등의 스코프 함수들도 내부적으로는 확장 함수
        - 코드 간결성 + 재사용성 향상
            - 중복되는 코드를 확장 함수로 빼면 프로젝트 전체에 깔끔하게 적용 가능

    - 실제 예시
        - 뷰에 간단한 확장 함수 추가
        - 예시
            ```kotlin
            // 뷰 가시성 설정
            fun View.visible() {
                this.visibility = View.VISIBLE
            }

            fun View.gone() {
                this.visibility = View.GONE
            }

            // 사용하는 부분
            button.visible()
            textView.gone()

            // 프래그먼트에 확장함수로 Toast
            fun Fragment.toast(message: String) {
                Toast.makeText(requireContext(), message, Toast.LENGTH_SHORT).show()
            }

            // 사용하는 부분
            toast("토스트!")
            ```

    - 확장 함수의 제약 사항
        - 멤버 함수처럼 보이지만 진짜 멤버 함수는 아님
            - 컴파일 시에는 정적(static) 함수로 처리됨
            - 같은 이름의 멤버 함수가 있다면 멤버 함수가 우선 (원래 것이 우선)
        - private/protected 멤버에는 접근할 수 없음
            - 내부 구현에 접근하는 멤버 함수와 달리,
            - 확장 함수는 클래스 내부 구조에 접근 불가 (공개된 API만 사용 가능)

    - 다른 확장 기능과의 관계
        - 확장 프로퍼티(Extension Property)도 유사하게 존재
        ```kotlin
        val String.lastChar: Char
        get() = this[length - 1]
        ```
            - Operator overloading, DSL, Coroutine builder 등에서 매우 자주 활용됨

    - 결론
        - 기존 클래스에 대해 새로운 기능을 외부에서 추가 가능한 기능
        - 코드 재사용, 유틸리티 함수 작성, 가독성 향상에 유용
        - 안드로이드 실무에서도 뷰, 프래그먼트, 컨텍스트 등의 기능 확장에 자주 사용됨

- Coroutine의 Structured Concurrency(구조적 동시성) 개념
    - 개요
        - 코루틴을 예측가능하게 관리하고, 메모리 누수와 비정상 종료를 방지하는 원칙
    - Structured Concurrency 개념
        - 정의
            - 코루틴은 그 코루틴을 시작한 범위(Scope) 내에서만 존재하며, 부모가 사라지면 자식 코루틴도 함께 취소되는 구조적인 실행 흐름을 보장하는 개념
            - 코루틴을 만든 스코프가 사라지면
            - 그 안에서 실행된 모든 코루틴도 같이 종료
            - 즉, 부모-자식 관계를 통해 동시성 작업을 구조적으로 관리

    - 필요성
        - 기존 문제점 (전통적인 비동기 처리 문제, 예: GlobalScope)
            - 전역에서 실행되는 코루틴은 수명이 관리되지 않음
            - 액티비티나 프래그먼트가 사라져도 코루틴은 계속 실행 > 메모리 누수, 충돌, 데이터 처리 오류 발생
        - 구조적 동시성 장점
            - 코루틴의 생명주기를 안전하게 관리
            - 에러 전파, 취소, 자원 해제가 구조적으로 이루어짐
            - 작업 범위가 명확해지고 예측 가능함

    - 구조적 동시성의 핵심 원칙
        - 부모 - 자식 관계: 코루틴은 자신을 실행한 부모 CoroutineScope에 속함
        - 부모 취소 -> 자식 취소: 부모가 취소되면 자식 루틴도 자동 취소
        - 예외 전파: 자식 코루틴에서 예외가 발생하면 부모로 전달됨
        - coroutineScope {} 사용: 구조적 컨텍스트에서 안전한 자식 코루틴 실행 보장

    - 예제
        - GlobalScope는 액티비티, 프래그먼트가 사라져도 계속 실행됨
            - 구조적 동시성 위반
        - viewModelScope, lifecycleScope는 구조적 동시성을 기본 제공
            - → ViewModel이나 Fragment가 종료되면 내부 코루틴도 자동 취소됨

    - coroutineScope & supervisorScope
        - coroutineScope {}: 자식 중 하나라도 실패하면 모든 자식이 취소됨
        - supervisorScope {}: 자식 중 하나가 실패해도 다른 자식에는 영향 없음
        ```kotlin
        coroutineScope {
            launch { taskA() }     // A 실패 → B도 취소
            launch { taskB() }
        }

        supervisorScope {
            launch { taskA() }     // A 실패 → B는 계속
            launch { taskB() }
        }
        ```

    - 최종 결론
        - Structured Concurrency 는 Kotlin Coroutine의 가장 중요한 설계 철학 중 하나로, 비동기 작업을 명확하고 안전하게 관리하며, 코드 유지보수성과 안정성을 크게 향상

- 안드로이드 APK 파일의 크기를 줄일 수 있는 방법들
    - 개요
        - 다운로드 속도, 설치율, 저장공간 부담과 직결되기 때문에 중요한 사항
    - 크기 축소 방법
        - (1) 리소스 최적화
            - 사용하지 않는 리소스 제거
                - res/ 폴더에 있는 사용되지 않는 drawable, layout, values 등 리소스 삭제
                - Android Studio → Lint 또는 Build → Analyze APK 도구 활용 가능
                - shrinkResources true 옵션 사용
                ```gradle
                buildTypes {
                    release {
                        shrinkResources true
                        minifyEnabled true
                        proguardFiles getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro"
                    }
                }
                ```

            - 리소스 압축 및 포맷 변경
                - PNG -> WebP로 변환 (용량 최소 20~30% 감소 가능)
                - 벡터(VectorDrawable) 사용 (아이콘, 단색 이미지에 효과적)
                - 이미지 압축 도구 사용 (TinyPNG, ImageOptim 등)

            - 다국어 리소스 제거
                - 사용하지 않는 values-xx/strings.xml 제거
                - resConfigs를 통해 필요한 언어만 포함
                ```gradle
                defaultConfig {
                    resConfigs "en", "ko" // 한국어, 영어만 포함
                }
                ```
        - (2) 코드 최적화
            - ProGuard / R8 사용 (난독화 + 코드 축소)
                - 사용하지 않는 클래스, 메서드, 필드 제거 (Dead Code Removal)
                - R8은 ProGuard를 대체하며 최신 빌드 시스템에 통합됨
                ```gradle
                minifyEnabled true
                ```
                    - 주의: ProGuard 설정 시 꼭 필요한 클래스가 제거되지 않도록 Keep 옵션 명시 필요

            - Kotlin Reflection 최소화
                - kotlin-reflect 라이브러리는 매우 무거움 -> 가능하면 사용하지 않도록 리팩토링
                - 대신 KClass.simpleName, sealed class 등을 활용

            - 불필요 써드파티 라이브러리 제거
                - 전체 기능을 사용하지 않는데도 무거운 라이브러리를 참조하는 경우 제거
                - 예: 전체 Glide 대신 Glide-no-op, Picasso-lite 등 경량 버전 사용 고려

        - (3) ABI 및 아키텍쳐 분할
            - 여러 CPU 아키텍쳐에 대해 분할 빌드
                - arm64-v8a, armeabi-v7a, x86 등 모두 포함하면 용량 증가
                - → 각 ABI별 APK 분리 (Split APKs) 또는 App Bundle 사용
                ```gradle
                splits {
                    abi {
                        enable true
                        reset()
                        include "armeabi-v7a", "arm64-v8a" // 필요한 것만 포함
                        universalApk false
                    }
                }
                ```

        - (4) App Bundle 사용 (AAB)
            - .aab (Android App Bundle) 형식으로 배포하면, Google Play가 사용자 디바이스에 맞는 APK만 생성하여 전달
                - 필요 없는 리소스, 코드, ABI 자동 제외
                - APK 크기 평균 20~50% 감소
                - Google Play에서 공식 권장 방식

        - (5) 기타 전략
            - Native 코드 최적화
                - .so 라이브러리 → 사용하지 않는 ABI 제거
                - JNI 호출 줄이기 / NDK 옵션 최적화
            - Dynamic Feature Module
                - 일부 기능을 동적으로 다운로드 하도록 분리 가능 (예: 로그인, 고해상도 이미지 편집 등)
                - 앱 설치 초기 용량 줄이기에 매우 효과적

    - 전략 요약
        - 리소스 최적화
        - 코드 최적화
        - 아키텍처 분리
        - 번들 사용
        - 고급 전략 (Dynamic Feature, Native Code 최적화, Resource Shrinker)

- Gradle은 맨 뒤에 ‘+’를 추가하면 자동으로 최신 버전으로 업데이트, 자동 업데이트하게 하는 방법
    - 사용 방법: 버전 끝에 + 삽입
        ```groovy
        dependencies {
            implementation 'com.squareup.retrofit2:retrofit:2.+'   // 2.x 버전 중 가장 최신
            implementation 'com.google.code.gson:gson:+'            // 전체 중 가장 최신
        }
        ```
        - 의미
            - 1.2.+: 1.2.0, 1.2.1, 1.2.99 등 1.2 버전 내에서 최신
            - 2.+: 2.0.0 ~ 2.99.99 등 2.x 버전 중 최신
            - +: 가장 최신 버전 전체 중 하나 선택

    - 장점
        - 항상 최신 버전으로 자동 반영
        - 보안 패치, 기능 개선 등을 자동 반영
        - 개발 초기에는 빠른 테스트 가능

    - 주의 사항
        - 빌드 결과가 매번 달라짐: 동일 프로젝트라도 날짜/위치에 따라 버전이 바뀜 → 재현 불가 문제
        - 예기치 않은 호환성 이슈: 종속 라이브러리 업데이트로 앱이 갑자기 깨질 수 있음
        - 빌드 속도 저하: 매번 리모트 저장소에서 버전 확인 요청 발생
        - 보안 리스크: 검증되지 않은 버전이 자동 반영될 수 있음
            - 그래서 실무에선 "정확한 버전 명시"가 강력히 권장됨

    - 대안: 최신 버전 자동 확인 후 수동 적용
        - Gradle Version Plugin 사용 (./gradlew dependencyUpdates)
        - GitHub Dependabot 또는 Renovate
        - com.github.ben-manes.versions 플러그인으로 확인 후 수동 업데이트

- 채팅 기능 구현
    - 개요
        - 전체 시스템 구조 개요
            ```text
            [Client: Android App] ←→ [Backend Server] ←→ [Database]
                                        ↑
                                    (WebSocket or Firebase)
            ```
            - Android 클라이언트: UI + 메시지 송수신 처리
            - 서버: 실시간 처리 (WebSocket 등), 메시지 저장
            - 데이터베이스: 메시지, 유저, 채팅방 기록 저장
    - 핵심 기능 목록
        - 메시지 송/수신: 서버와 연결하여 텍스트 / 이미지 / 파일 주고받기
        - 실시간 업데이트: 메시지를 수신 즉시 UI 반영
        - 메시지 저장: DB에 대화 로그 저장 및 불러오기
        - 읽음 처리: 읽음 여부 동기화
        - 사용자 인증: 유저별 메시지 분리 및 식별 필요
    - 기술 선택
        - 실시간 통신
            - 선택 옵션: Firebase Realtime DB / Firestore, WebSocket (Socket.IO, Stomp, OkHttp), MQTT
            - 설명: 서버가 없으면 Firebase가 쉬움 / 서버 있으면 WebSocket 권장
        - 백엔드: Node.js, Spring, FastAPI, Firebase Functions 등 (메시지 중계 및 저장)
        - 데이터 저장: Firebase, MongoDB, MySQL, PostgreSQL	(스케일링 고려)
        - Push 알림: FCM (Firebase Cloud Messaging)	(앱이 꺼져 있을 때 알림)
        - 보안: JWT 인증, Firebase Auth, OAuth (사용자 구분 필수)
    - Android 클라이언트 개발 구조
        - UI 구성
            - RecyclerView + Adapter 사용
            - 메세지 방향에 따라 ViewHolder 분리 (보낸 메세지 / 받은 메시지)
                - 보낸 메세지: 오른쪽 정렬
                - 받은 메세지: 왼쪽 정렬
        - 실시간 메시지 수신 처리
            - Firebase 사용 시 (초보자/빠른 구현용)
                ```kotlin
                val db = FirebaseDatabase.getInstance()
                val messagesRef = db.getReference("chat_rooms/room_id/messages")

                messagesRef.addChildEventListener(object : ChildEventListener {
                    override fun onChildAdded(snapshot: DataSnapshot, previousChildName: String?) {
                        val msg = snapshot.getValue(ChatMessage::class.java)
                        adapter.addMessage(msg)
                    }
                    // ...
                })
                ```
            - WebSocket 사용 시 (고급/사용 서비스)
                ```kotlin
                val client = OkHttpClient()
                val request = Request.Builder().url("wss://yourserver.com/chat").build()
                val listener = object : WebSocketListener() {
                    override fun onMessage(webSocket: WebSocket, text: String) {
                        val msg = gson.fromJson(text, ChatMessage::class.java)
                        adapter.addMessage(msg)
                    }
                }
                client.newWebSocket(request, listener)
                ```
        - 메시지 전송 처리
            ```kotlin
            val message = ChatMessage(senderId, messageText, System.currentTimeMillis())
            messagesRef.push().setValue(message) // Firebase 예시
            ```
    - 서버 구성 예 (웹소켓 기반)
        - /join
        - /send
        - /receive
        - 구현 예제 (Node.js + Socket.IO)
            ```js
            io.on('connection', socket => {
                socket.on('join', roomId => socket.join(roomId));
                socket.on('send', (roomId, msg) => {
                    io.to(roomId).emit('receive', msg);
                });
            });
            ```
    - 고급 기능 확장 예시
        - 채팅방 목록: 사용자별 참여중인 채팅방 목록 표시
        - 이미지/파일 전송: Firebase Storage or Multipart Upload
        - 메시지 읽음 여부: 메시지에 readBy 리스트 저장
        - 메시지 삭제: soft delete or 필드 플래그
        - 타이yping 표시: WebSocket으로 typing 이벤트 전달
    - 실제 적용 기술 스택 예
        - 클라이언트: Android (Kotlin, Jetpack Compose, RecyclerView, ViewModel)
        - 실시간: Firebase RTDB / Firestore or WebSocket (OkHttp, Stomp)
        - 백엔드: Spring Boot, Node.js, FastAPI + Redis pub/sub
        - 데이터 저장: Firebase / MongoDB / MySQL
        - 인증: Firebase Auth or JWT
        - 알림: Firebase Cloud Messaging (FCM)

    - 결론
        - 안드로이드 채팅 기능 구현의 핵심은 실시간 메시지 송수신, 안정적인 데이터 저장, 그리고 반응성 있는 UI 구성
        - Firebase는 서버 없이 빠르게 시작할 수 있고, WebSocket은 고급 커스터마이징에 적합

- 프래그먼트 기본 생성자 사용 이유
    - 개요
        - 반드시 기본 생성자(인자가 없는 생성자) 제공해야 하는 이유는 시스템이 프래그먼트를 복원하고 재생성하는 방식과 관련있음
    - 핵심 이유: 시스템이 프래그먼트를 자동으로 재생성하기 때문
        - 안드로이드 시스템은 다음 상황에서 프래그먼트를 자동 복원
            - 화면 회전(configuration change)
            - 프로세스가 강제 종료된 후 백 스택 복원
            - 앱이 메모리 부족으로 KILL됐다가 다시 시작될 때
            ```java
            Fragment fragment = fragmentClass.newInstance(); // 리플렉션 기반 생성
            ```
            - 리플렉션 통해 기본 생성자로 프래그먼트를 생성하기 때문에 기본 생성자가 반드시 존재해야 오류없이 복원 가능
    - 잘못된 예: 인자 있는 생성자 사용
        ```kotlin
        class MyFragment(private val userId: String) : Fragment() {
            // 위험한 패턴: 복원 시 userId가 전달되지 않음 → crash 가능성 있음
        }
        ```
        - 문제점
            - 시스템이 이 프래그먼트를 복원할 때 userId 값을 전달할 수 없음
            - 결과적으로 IllegalStateException, NullPointerException,  Fragment$InstantiationException 발생 가능

    - 올바른 패턴: 기본 생성자 + Bundle 사용
        ```kotlin
        class MyFragment : Fragment() {
            companion object {
                fun newInstance(userId: String): MyFragment {
                    val fragment = MyFragment()
                    val args = Bundle().apply {
                        putString("userId", userId)
                    }
                    // fragment.arguments 방식으로 데이터 전달하는 것이 가장 안전
                    fragment.arguments = args
                    return fragment
                }
            }

            override fun onCreate(savedInstanceState: Bundle?) {
                super.onCreate(savedInstanceState)
                val userId = arguments?.getString("userId")
                // 이 값을 사용
            }
        }
        ```
        - 장점
            - 기본 생성자 유지
            - 시스템이 프래그먼트를 자동 복원해도 Bundle이 함께 복원됨
            - 생명주기/복원 안전

    - 안드로이드 공식 권장 방식
        - 공식문서 상 프래그먼트는 항상 public 기본 생성자를 제공해야 하며, 파라미터 전달은 arguments를 사용할 것 이라고 명시하고 있음

    - 결론
        - Fragment는 반드시 기본 생성자가 있어야 한다.
        - 이유는 시스템이 리플렉션으로 프래그먼트를 자동 재생성하기 때문에, 인자 있는 생성자를 사용할 경우 복원이 불가능하거나 앱이 크래시될 수 있다.
        - 데이터 전달은 반드시 Bundle(arguments)을 통해 수행해야 한다.

- Gradle / Ant / Maven
    - 개요
        - 빌드 도구(Build Tool)
    - 개념 요약
        - Ant: 가장 오래된 Java 빌드 도구. 절차지향적
        - Maven: Ant 이후 등장. 규약 중심(Convention over Configuration)
        - Gradle: 최신 빌드 도구. 스크립트 기반 + 유연한 설정, Android 공식 빌드 도구
    - 각 도구별 개념 및 특징
        - (1) Ant (Apache Ant)
            - 자바 생태계에서 가장 먼저 널리 쓰인 빌드 도구
                - XML로 작성된 build.xml 파일 사용
                - 작업(task) 중심 → 순서대로 실행
                - 사용자가 모든 작업을 직접 정의 (컴파일, 패키징, 복사 등)
                - 유연하지만 유지보수 어려움
                ```xml
                <project name="HelloApp" default="compile">
                    <target name="compile">
                        <javac srcdir="src" destdir="build/classes"/>
                    </target>
                </project>
                ```
        - (2) Maven (Apache Maven)
            - Ant의 단점을 보완해 나온 규약 기반 빌드 도구
                - XML 기반의 pom.xml로 설정
                - 표준적인 프로젝트 구조와 라이프사이클 존재
                    - 예: src/main/java, src/test/java
                - 의존성 관리 시스템 내장 (중앙 저장소 mvnrepository)
                - 설정은 많지 않지만, 구조 변경은 어렵고 유연성이 떨어짐
                ```xml
                <dependencies>
                <dependency>
                    <groupId>org.springframework</groupId>
                    <artifactId>spring-core</artifactId>
                    <version>5.2.0.RELEASE</version>
                </dependency>
                </dependencies>
                ```
        - (3) Gradle
            - Maven의 규약 + Ant의 유연성 → 현대적인 빌드 도구, 현재 Android 공식 빌드 도구
                - build.gradle 파일에 Groovy/Kotlin DSL로 작성
                - 의존성, 빌드, 릴리즈, 코드 생성 등 매우 유연하게 처리 가능
                - 강력한 캐싱, 병렬 빌드, Incremental Build 등 성능 최적화 우수
                - Plugin 기반으로 확장성 매우 뛰어남
                - Android Studio 기본 통합
                ```groovy
                dependencies {
                    implementation 'androidx.core:core-ktx:1.10.1'
                    implementation 'com.squareup.retrofit2:retrofit:2.9.0'
                }
                ```
    - Android에서 Gradle 사용 이유
        - Google이 공식적으로 Android 빌드 도구로 채택
        - 플러그인 시스템 (e.g. com.android.application)
        - 다양한 빌드 타입, productFlavor, variant 지원
        - 코드 생성, 리소스 관리, AAR/JAR 처리 등 Android 생태계에 최적화
        - Kotlin DSL로도 작성 가능 (build.gradle.kts)

- JAR, AAR, DEX, APK 개념
    - 개요
        - 빌드 결과물 또는 라이브러리 구성 형식
    - JAR (Java ARchive)
        - 개념
            - Java 클래스(.class)파일과 메타데이터(MANIFEST.MF)등을 압축한 Java용 배포 패키지
        - 용도
            - 일반 자바 라이브러리 배포에 사용
            - 안드로이드에서도 사용 가능하지만 자바 코드만 포함 가능
        - 특징
            - 내부에 .class 파일만 있음
            - 리소스(res, AndroidManifest.xml, native 라이브러리 등) 없음
            - 안드로이드에서 사용하려면 .dex 변환이 필요
        - 포함요소
            - .class, META-INF

    - AAR (Android ARchive)
        - 개념
            - 안드로이드 전용 라이브러리 패키지로, JAR보다 확장된 구조를 가지고 있음
        - 용도
            - Android 모듈 또는 라이브러리를 다른 프로젝트에서 재사용할 때 사용
            - resources, Manifest, ProGuard, assets 등 포함 가능
        - 특징
            - 내부 구성
            ```bash
            /classes.jar            ← Java 클래스
            /AndroidManifest.xml    ← 라이브러리용 매니페스트
            /res/                   ← 리소스
            /assets/                ← 에셋
            /proguard.txt           ← 난독화 설정
            /jni/                   ← .so 파일 (native lib)
            ```
            - 일반적으로 maven, jitpack, local repo 등으로 공유
        - 포함요소
            - classes.jar, res, manifest, .so

    - DEX (Dalvik Executable)
        - 개념
            - 안드로이드 런타임(달빅/ART)에서 실행 가능한 바이트코드 파일
        - 용도
            - .class 파일들을 안드로이드에서 실행 가능하게 변환한 결과물
            - 안드로이드에서 실행되는 모든 코드는 .dex 형태여야 함
        - 특징
            - .class -> .dex 변환은 D8 또는 R8 컴파일러가 수행
            - 내부 명령어는 JVM이 아닌 달빅/ART 명령어셋 (레지스터 기반) 사용
            - .apk 안에 포함됨
        - 포함요소
            - 컴파일된 .class 변환 결과

    - APK (Android Package)
        - 개념
            - 안드로이드 앱의 최종 패키지 파일(=실행 가능 배포 파일)
        - 용도
            - GooglePlay에 업로드하거나, 사용자에게 앱 설치 파일로 제공
            - 내부적으로 .dex, .xml, .so, .png 등 다양한 자원을 압축하여 포함
        - 특징
            - .apk는 사실상 zip 압축 파일
            - 내부 구성 예:
            ```bash
            /classes.dex         ← 앱 실행 코드 (DEX)
            /AndroidManifest.xml
            /res/                ← 리소스 (버튼, 배경 등)
            /assets/             ← 에셋 (읽기 전용 리소스)
            /lib/                ← .so 파일 (native library)
            /META-INF/           ← 서명 정보
            ```
            - .apk는 안드로이드 OS에서 설치/실행 가능한 단일 앱 파일
        - 포함요소
            - .dex, 리소스, manifest, lib

    - 간단 결론 요약
        - JAR → 순수 Java 코드 라이브러리
        - AAR → Android 앱에 필요한 리소스 + 코드 포함된 라이브러리
        - DEX → Android에서 실행 가능한 바이트코드
        - APK → Android 앱 최종 설치 패키지

- Annotation 개념
    - 정의
        - Annotation은 코드에 메타데이터(데이터에 대한 데이터)를 추가하는 Java 문법의 한 종류
        - 컴파일러나 툴, 프레임워크에 추가 정보를 제공하는 방식
        - 코드에 부가적인 의미를 부여하지만, 실제 프로그램의 실행 로직에는 직접 영향을 주지 않음
    - 목적
        - 컴파일러 지시: @Override, @SuppressWarnings 등 컴파일러에게 검사 또는 무시 요청
        - 런타임 정보 제공:	@Retention(RUNTIME) 설정 시, 리플렉션으로 런타임에 조회 가능
        - 코드 자동 생성: @Parcelize, @GlideModule, @HiltViewModel 등에서 코드 생성 처리
        - 의존성 주입 처리: @Inject, @Provides, @Module, @Singleton 등에서 DI 구현
    - 애노테이션의 주요 메타 애노테이션
        - 애노테이션 자체도 애노테이션으로 정의 가능
        - 대표적 예
            - @Target: 애노테이션이 적용될 수 있는 위치 (class, field, method 등)
            - @Retention: 유지 범위 (컴파일 시, 클래스 파일에, 런타임까지 등)
            - @Inherited: 상속 가능 여부
            - @Documented: Javadoc에 포함 여부
            ```Kotlin
            @Target(AnnotationTarget.CLASS)
            @Retention(AnnotationRetention.RUNTIME)
            annotation class MyAnnotation
            ```
    - 자주 사용되는 애노테이션
        - @Override: 부모 클래스의 메서드를 오버라이드함을 명시
        - @NonNull, @Nullable: null 허용 여부를 명시, Lint 및 코드 툴이 활용
        - @Inject: Dagger/Hilt 등 의존성 주입 대상 지정
        - @HiltViewModel: ViewModel에 Hilt 자동 주입 설정
        - @Parcelize: Parcelable 인터페이스를 컴파일 타임에 자동 구현
        - @BindingAdapter: DataBinding에서 커스텀 속성 연결 처리
    - 애노테이션 처리기
        - 애노테이션은 해석되고 처리되어야 기능을 발휘
            - Java: Annotation Processing Tool (APT)를 통해 컴파일 타임 처리
            - Kotlin: kapt (Kotlin Annotation Processing)
            - 대표적인 예: Dagger, Hilt, Room, Glide → 모두 APT 기반 코드 자동 생성 사용
            ```kotlin
            // Room 예시
            @Entity
            data class User(
                @PrimaryKey val id: Int,
                val name: String
            )
            ```
                - → @Entity와 @PrimaryKey는 Room이 처리해서 DAO 및 DB 구조 자동 생성
    - 애노테이션 중요한 이유
        - 코드 간결화: 보일러 플레이트 코드 감소
        - 컴파일 시점 오류 감지: @NotNull 등은 앱 실행 전에 오류 가능성 사전 확인 가능
        - 프레임워크 간 통합 포인트: 프레임워크 내부 훅 연결 수단
        - 성능 향상: 컴파일 타임에 코드를 생성하여 리플렉션 비용 감소(Room, Hilt 등)
    - 결론
        - Annotation은 코드에 메타데이터를 부여하여, 컴파일러, 프레임워크, 툴에게 의미 있는 정보를 전달하는 수단이다.
        - Android 개발에서는 DI, 데이터바인딩, 코드 생성 등 광범위하게 사용됨

- Custom Annotation 정의 및 커스텀 기능 구현 방법
    - 개요
        - 안드로이드 또는 코틀린/자바 개발에서 프레임워크처럼 동작하는 기능을 직접 만들고 싶을 때 핵심 개념
    - 전체 구현 흐름
        - Annotation 정의
        - Annotation을 붙인 대상 작성
        - Annotation Processor 작성 (컴파일 타임 or 런타임)
        - (선택) 코드 생성 or 특정 로직 실행
    
    - (1) Custom Annotation 정의
        ```kotlin
        @Target(AnnotationTarget.CLASS, AnnotationTarget.FUNCTION)
        @Retention(AnnotationRetention.RUNTIME)
        annotation class MyLogger(
            val tag: String = "MyLogger"
        )
        ```
        - 주요 요소 설명
            - @Target: 어디에 붙일 수 있는지 지정 (CLASS, FIELD, FUNCTION 등)
            - @Retention: 언제까지 유지할지 지정 (SOURCE, BINARY, RUNTIME)
            - @Repeatable, @MustBeDocumented, @Inherited 등도 있음	
            - RUNTIME 으로 설정하면 리플렉션으로 사용할 수 있음
    - (2) Annotation 사용
        ```kotlin
        @MyLogger(tag = "CustomLogger")
        fun doSomething() {
            println("Doing something...")
        }
        ```
    - (3) 리플렉션을 사용한 런타임 처리
        - 간단한 실행 예시(함수에 @MyLogger 붙은 경우 로그 출력)
        ```kotlin
        fun invokeWithLogging(target: Any) {
            val kClass = target::class

            for (func in kClass.members) {
                val annotation = func.annotations.find { it is MyLogger } as? MyLogger
                if (annotation != null) {
                    println("${annotation.tag} → ${func.name} 실행 전 로그 출력")
                    func.call(target) // 파라미터 없는 함수만 호출 가능
                    println("${func.name} 실행 완료")
                }
            }
        }
        ```
        - 호출
        ```kotlin
        class TestClass {
            @MyLogger(tag = "TEST")
            fun hello() {
                println("Hello, world!")
            }
        }

        fun main() {
            val obj = TestClass()
            invokeWithLogging(obj)
        }
        ```
    - (4) Annotation Processor (컴파일 타임 처리)
        - 런타일이 아닌 컴파일 타임에 코드 생성 및 유효성 검사를 하려면 아래 도구 사용
            - Java:	APT (Annotation Processing Tool)
            - Kotlin: kapt (kotlin-kapt 플러그인)
            - 대표 라이브러리: AutoService, KotlinPoet, JavaPoet
        - Processor 예제
            ```java
            @AutoService(Processor.class)
            public class MyLoggerProcessor extends AbstractProcessor {
                @Override
                public Set<String> getSupportedAnnotationTypes() {
                    return Collections.singleton(MyLogger.class.getCanonicalName());
                }

                @Override
                public boolean process(Set<? extends TypeElement> annotations, RoundEnvironment roundEnv) {
                    for (Element element : roundEnv.getElementsAnnotatedWith(MyLogger.class)) {
                        // 대상 클래스나 메서드 정보 추출
                        System.out.println("Found @MyLogger on: " + element.getSimpleName());
                        // 코드 생성 또는 로깅 등 수행
                    }
                    return true;
                }
            }
            ```
    - 결론
        - 정의: @interface 또는 annotation class로 Annotation 정의
        - 사용: 클래스/함수/필드에 애노테이션 부착
        - 처리 방식: 리플렉션 기반(RUNTIME) 또는 APT/kapt 기반(COMPILE TIME)
        - 도구: kapt, AutoService, KotlinPoet, JavaPoet 등 사용 가능


- AsyncTask Deprecated된 이유
    - 개요
        - 백그라운드 작업을 쉽게 처리하기 위한 기본 API 였으나, 현재는 Deprecated
    - Deprecated된 시점
        - 안드로이드 API 30(Android 11)부터 AsyncTask는 Deprecated 처리됨
        - Jetpack 라이브러리 / Kotlin Coroutine, WorkManager 등 권장
    - Deprecated 된 핵심 이유
        - 생명주기와의 불안정한 연동
            - AsyncTask는 액티비티 / 프래그먼트의 생명주기를 인식하지 못함
            - 액티비티가 종료되어도 doInBackground() 는 계속 실행되므로
                - -> 메모리 누수, 크래시, UI 갱신 오류 발생 가능
        - 스레드 처리 방식의 제한성
            - AsyncTask는 내부적으로 ThreadPoolExecutor를 공유하며, 기본적으로 직렬(serial) 실행
                - → 다중 작업 병렬 처리 시 의도치 않은 대기 현상, 동기화 오류 발생 가능

        - 예외 처리 및 취소 처리의 어려움
            - 예외 발생 시 try-catch 외엔 대응이 어렵고
            - cancel() 호출 이후에도 doInBackground() 내부에서 명시적으로 체크하지 않으면 취소가 제대로 되지 않음

        - 기능 확장과 관리 어려움
            - 작업 취소, 리트라이, 실패 시 대체 로직 등 구조적으로 확장하기 어려움
            - 테스트도 어렵고 구조화된 비동기 처리(구조적 동시성) 개념 부재

    - 권장 대체 방법
        - Kotlin Coroutine
        - WorkManager
        - RxJava

    - 결론
        - AsyncTask는 생명주기 관리 부재, 스레드 처리의 제한, 예외/취소 처리의 불편함, 구조 확장의 어려움 등으로 인해 Android 11(API 30)부터 공식적으로 deprecated 되었으며, Kotlin Coroutine, WorkManager 등 보다 현대적이고 안전한 대체 수단으로 전환하는 것이 권장

- Zygote 개념
    - 개요
        - Zygote(자이곳)는 앱 프로세스의 성능과 메모리 효율에 큰 영향을 주는 중요한 시스템 컴포넌트

    - 정의
        - 안드로이드 시스템에서 애플리케이션 프로세스를 생성하기 위한 기본 프로세스(부모 프로세스)
        - 수정란(Zygote)처럼 다른 앱 프로세서들이 여기서부터 fork(분기)되어 생성

    - 역할
        - 시스템 초기화된 공통 리소스를 미리 로딩
            - Android Framework API, 리소스, 라이브러리, 클래스 로딩 등을 미리 메모리에 올려둠
        - 앱 프로세스 생성의 부모 역할
            - 새로운 앱이 실행될 때, Zygote가 자신을 복제(fork)해서 새로운 앱 프로세스를 생성
        - 빠른 앱 실행 및 메모리 절약
            - 공통 리소스들이 이미 로딩된 상태로 프로세스가 복제되기 때문에
                - -> 앱 실행 속도 향상
                - -> 메모리 절약 (공유 메모리로 처리됨)

    - 동작 흐름 요약
        - (1) 부팅 시 init 프로세스가 Zygote를 실행
        - (2) Zygote는 app_process를 통해 Java VM(Dalvik / ART)환경을 초기화함
        - (3) 시스템 클래스, 리소스, Framework 등이 선로드(preload) 됨
        - (4) 이후 앱을 실행할 때마다 Zygote가 fork() 호출하여 자식 프로세스(앱 프로세스)를 생성
            - 이 구조는 유닉스 계열의 프로세스 생성 모델과 유사하게 설계되어 있음

    - Zygote 사용 이유 (이점)
        - 빠른 프로세스 생성
            - fork()는 기존 메모리를 그대로 복제하므로, cold start 시에도 앱 실행 속도가 매우 빠름

        - 메모리 공유로 절약
            - 프레임워크 및 공통 클래스들이 Copy-On-Write 방식으로 공유됨
                - → 여러 앱에서 동일한 메모리 사용 가능

        - 안정성과 보안성 향상
            - 시스템 리소스는 Zygote에서 미리 안전하게 초기화되어
                - → 앱마다 반복할 필요 없음
                - → 자원 충돌 방지

    - Android 앱 생명주기에서의 위치
        - 앱 실행 시 ActivityManagerService가 앱 실행 요청
        - Zygote에 socket을 통해 실행 명령 전송
        - Zygote가 fork() → 새 앱 프로세스 생성
        - 새로 생성된 앱 프로세스는 자신의 ActivityThread를 시작함
        - 그 후 Application, Activity, Service 등이 실행됨

    - 실무 시 알아야 할 포인트
        - Zygote는 앱 프로세스가 느리게 시작되는 이유가 아님 → 오히려 속도를 빠르게 해주는 주체
        - Zygote fork 이후 초기화가 느린 앱은 대부분 자체 초기화 코드(Application.onCreate 등) 때문
        - Android 8.0 이후에는 Zygote64, Zygote32 등으로 분리되어 64비트/32비트 앱을 각각 지원함

    - 전체 요약
        - Zygote는 안드로이드 핵심 프로세스
        - 모든 앱 프로세스의 부모 역할
        - 앱 실행에 필요한 공통 리소스를 미리 로딩한 뒤, 새로운 앱 실행 요청 시 fork()를 통해 빠르고 효율적으로 프로세스를 생성
        - 앱 실행 속도와 메모리 사용 효율을 극대화하는 안드로이드 아키텍쳐의 핵심 구성 요소

- Zygote 다른 설명
    - 개요
        - 안드로이드 앱이 빠르게 실행될 수 있도록 지원하는 핵심 프로세스

    - 정의
        - 안드로이드에서 모든 앱 프로세스의 부모 역할을 하는 초기 런타임 프로세스
            - 리눅스의 fork() 시스템 호출을 이용하여 새로운 앱 프로세스를 생성
            - 안드로이드 부팅 시 시스템이 가장 먼저 실행하는 앱 런타임 환경의 템플릿
            - app_process 바이너리를 통해 Zygote 프로세스가 런타임 환경을 미리 초기화

    - Zygote 동작 방식
        - 부팅 시 초기화
            - 안드로이드 기기가 부팅되면, Init 프로세스가 Zygote를 실행
            - 아래 작업을 미리 로딩
                - ART 런타임
                - 필수 클래스 (java.lang, android.app 등)
                - 공통 리소스 (Drawable, Layout 등)
        - 앱 실행 시 fork
            - 앱 실행하면 Zygote가 fork()를 호출해 새 프로세스를 복사
            - 이로 인해 새 앱 프로세스는 초기화 시간을 절약
            - 이 방식은 리눅스의 Copy-on-Write(COW) 특성 덕분에 메모리 효율성도 높음

    - 사용 이유
        - 앱 실행 속도 향상: 미리 로드, 앱 프로세스 생성 시 바로 사용
        - 메모리 절약: COW 기법, 부모(Zygote)와 자식(앱)이 공통 메모리 공유
        - 안정성: 초기환경 표준화, 앱 간 실행 일관성 유지

    - 중요 특징
        - ART 초기화 포함: Zygote는 ART를 미리 초기화하여 앱 프로세스는 바로 코드 실행 가능
        - app_process 실행: Zygote는 /system/bin/app_process 실행을 통해 Java런타임 환경을 실행
        - zygote64, zygote32: 64, 32비트 기기 아키텍쳐에 따라 두 종류가 존재, 앱도 ro.zygote 설정에 따라 적절한 버전으로 fork

    - 안드로이드 앱 실행 흐름 내 Zygote 위치
        - SystemServer: 시스템 서비스들을 실행하는 프로세스 (AMS, WMS 등)
        - 앱 프로세스: Zygote로부터 fork 된 독립 실행 환경
        ```scss
        [init] → [Zygote] → fork() → [SystemServer]
                               → fork() → [앱 프로세스]
        ```

    - 총 정리
        - Zygote는 안드로이드에서 모든 앱의 런타임 기반이 되는 템플릿 프로세스
        - 앱 실행 시 Zygote가 fork()로 새 프로세스를 빠르게 복사
        - 앱 실행 속도 향상 + 메모리 효율성 증가
        - 안드로이드 시스템의 핵심 부팅 시퀀스와 런타임 구조의 출발점

    - 참고
        - ZygoteInit.java
        - ActivityManagerService

- .class, .dex 파일 내부 구조
    - .class 파일 (Java Bytecode)
        - 개요
            - JVM에서 실행하기 위한 Java 바이트코드
            - 각 .class 파일은 하나의 클래스 또는 인터페이스를 나타냄
            - 표준 JVM 포맷이고, 바이너리 형식

        - 주요 구성 요소
            - Magic Number
                - 항상 0xCAFEBABE로 시작 → JVM 파일임을 식별
            - 버전 정보
                - Java 버전 명시 (예: major version 52 = Java 8)
            - Constant Pool
                - 문자열, 클래스, 메서드 참조 등 리터럴 상수 저장
                - 바이트코드가 이 인덱스를 참조함
            - Access Flags
                - public, abstract, final 등의 클래스 접근 정보
            - This Class / Super Class
                - 현재 클래스와 부모 클래스 정보
            - Interfaces
                - 구현한 인터페이스 목록
            - Fields / Methods
                - 변수 및 메서드 정의 (이름, 시그니처, 접근자 포함)
            - Attributes
                - Code, LineNumberTable, SourceFile 등의 메타정보

    - .dex 파일 (Dalvik Executable)
        - 개요
            - Android의 Dalvik 또는 ART에서 실행 가능한 특수 포맷
            - 모든 클래스가 하나의 .dex 파일 안에 포함됨
            - 공간 효율성을 고려한 설계 (모바일 환경에 최적화)

        - 주요 구성 요소
            - Header
                - dex\n035\0 → dex 파일 식별자 (magic number)
                - 파일 크기, 체크섬, 버전 정보 포함
            - String IDs
                - 모든 문자열의 목록 (중복 제거)
            - Type IDs
                - 클래스, 인터페이스, 배열 등 타입 목록
            - Proto IDs
                - 메서드 시그니처 정보 (return type, parameters)
            - Field IDs / Method IDs
                - 필드와 메서드의 이름, 소속 클래스, 시그니처 인덱스
            - Class Defs
                - 각 클래스의 정의 (상속 정보, 인터페이스, 메서드 오프셋 등)
            - Code Items
                - 실제 바이트코드 (register 기반 명령어 집합)
            - Data Section
                - 상수, 어노테이션, 디버깅 정보 등 추가 데이터

    - 내부 구조
        - .class
            ```pgsql
            | Magic | Version | Constant Pool | Access Flags |
            | This Class | Super Class | Interfaces |
            | Fields | Methods | Attributes |
            ```
        - .dex
            ```pgsql
            | Header | String IDs | Type IDs | Proto IDs |
            | Field IDs | Method IDs | Class Defs |
            | Code Items | Data Section |
            ```

- JVM과 Dalvik 가상 머신
    - 기본 개념
        - JVM (Java Virtual Machine): Java 프로그램을 실행하는 표준 가상 머신
            - 자바로 작성된 프로그램을 바이트코드(.class) 로 컴파일 후 JVM에서 실행
            - 모든 자바 플랫폼의 기반
            - OS와 하드웨어 독립적인 실행 환경 제공
            - 명령어 기반: 스택 기반
            - 실행 방식: .class를 직접 실행

        - DVM (Dalvik Virtual Machine): 안드로이드 전용으로 설계된 가상 머신 (안드로이드 4.4 이하)
            - 자바 코드를 안드로이드에서 실행할 수 있게 하기 위한 맞춤형 가상 머신
            - .class -> .dex(Dalvik Executable)로 변환 후 실행
            - 모바일 기기 특화 설계: 메모리 적게 사용, 다중 인스턴스 지원
            - 명령어 기반: 레지스터 기반
            - 실행 방식: .dex를 실행 (.class -> .dex 변환 필요 (dx, D8 사용))

    - 구조적 차이
        - JVM
            - 스택 기반 아키텍쳐
            - 명령어 실행 시 스택을 활용 (push, pop 중심)
            - 예: 두 값을 더하려면 스택에 값을 넣고 iadd 수행
        - DVM
            - 레지스터 기반 아키텍쳐
            - 명령어가 가상의 레지스터에 직접 접근
            - 더 빠르고 효율적인 연산 가능 (스택 사용 줄임)
            - 모바일 기기의 메모리 최적화와 속도 향상에 유리

    - 멀티스레드 및 멀티앱 처리
        - JVM: 일반적으로 하나의 인스턴스에서 여러 스레드가 실행
        - DVM: 각 안드로이드 앱마다 하나의 DVM 인스턴스를 가짐
            - 앱 간 충돌방지
            - 앱마다 독립적인 실행 환경 보장

    - Dalvik -> ART (Android Runtime)
        - Android 5.0 롤리팝부터는 ART가 기본 런타임
            - 인터프리터 실행 방식에서 AOT (설치 시 네이티브 코드 변환)
            - 속도는 빨라짐 (기계어로 실행)
            - 메모리 사용은 증가 (기계어 저장 필요)

    - 참고
        - 코드 설계: 안드로이드 앱 개발 시 JVM 특화된 기능 (예: SecurityManager, ClassLoader 구조 등)을 사용할 수 없음

- 바이트 코드를 안드로이드에서 바로 실행 가능한지에 대한 설명
    - 개요
        - 안드로이드는 JVM 바이트코드(.class)를 직접 실행하지 않음

    - 안드로이드는 JVM 사용하지 않음
        - 자바는 기본적으로 JVM위에서 실행되는 언어
            - .java -> .class -> JVM이 실행 (바이트코드 실행)
        - 반면, 안드로이드는 JVM이 아닌 Dalvik/ART(Android Runtime)을 사용
            - JVM 바이트코드를 그대로 실행 불가능

    - 안드로이드 앱 빌드 흐름
        - .java -> .class -> .dex
            ```markdown
            1. Java 소스코드 (.java)
                    ↓
            2. Java 바이트코드 (.class) ← 이건 JVM 용
                    ↓
            3. D8 or DX 툴로 변환
                    ↓
            4. Dalvik/ART 실행용 바이트코드 (.dex = Dalvik Executable)
            ```
            - D8 or R8: .class -> .dex 변환기 (안드로이드용 실행 포맷 생성)
            - .dex 파일은 Android Runtime에서 실행 가능한 포맷
            - 바이트 코드는 중간 산물이며, 직접 실행되지 않음, 반드시 .dex로 변환된 뒤 실행돼야 함 
                - 안드로이드는 .class 바이트코드를 직접 실행할 수 없으며, 반드시 .dex 포맷으로 변환된 후 ART에서 실행됨
                - 바이트코드는 안드로이드에서 직접 실행하는 최종 산물이 아니며, 앱 실행을 위한 중간 단계

    - 실행 환경 비교
        - 실행 대상
            - Java (JVM): .class (바이트코드)
            - Android (ART/Dalvik): .dex
        - 런타임
            - Java (JVM): JVM (Java Virtual Machine)
            - Android (ART/Dalvik): ART(Android Runtime), 이전에는 Dalvik
        - 변환 도구
            - Java (JVM): 없음
            - Android (ART/Dalvik): D8, R8, dx 등을 통해 변환 필요

    - 예외 / 테스트 상황
        - 안드로이드 기기에서 자바 프로그램 직접 실행 시
            - JVM 설치 필요 (Termux 등)
            - .class 또는 .jar 파일을 JVM으로 실행하는 방식

- 직렬화 vs 역직렬화 개념
    - 개요
        - 데이터를 저장하거나 네트워크로 전송할 때 자주 등장하는 개념
        - JSON, Parcelable, Bundle, Room 등 다양한 곳에서 활용

    - 직렬화 (Serialization): 변환
        - 개념
            - 객체의 상태를 바이트나 문자열 형태로 변환하여 파일로 저장하거나 네트워크로 전송 가능한 형태로 만드는 과정
        - 필요 이유
            - 객체는 메모리에서만 유효
            - 데이터를 디스크 저장 또는 다른 장치 전송, DB 저장하려면 문자열 또는 바이트 배열처럼 변환 가능한 형태가 필요
        - 예시
            ```kotlin
            data class User(val name: String, val age: Int)

            val user = User("Aiden", 30)
            val json = gson.toJson(user) // 직렬화: 객체 → JSON 문자열
            ```

    - 역직렬화 (Deserialization): 복원
        - 개념
            - 직렬화된 데이터를 다시 원래의 객체 형태로 복원하는 과정
        - 필요 이유
            - 저장된 데이터나 수신한 데이터는 사람이 이해할 수 있어도 코드에서 객체처럼 다루려면 다시 객체로 되돌려야 함
        - 예시
            ```Kotlin
            val json = """{ "name": "Aiden", "age": 30 }"""
            val user = gson.fromJson(json, User::class.java) // 역직렬화: JSON 문자열 → 객체
            ```

    - 자주 사용되는 직렬화 방식
        - JSON (일반적)
            - Gson, Moshi, Kotlinx,serialization 등 사용
            - 예: REST API 응답을 JSOB -> 객체로 역직렬화
        - Parcelable (안드로이드 전용)
            - Intent, Bundle 간 객체 전달 시 사용
            - 속도 빠르고 경량화
            - 예: Intent.putExtra() -> 객체를 Parcelable로 직렬화
        - Serializable (Java 표준)
            - Java의 Serializable 인터페이스 구현 시 사용
            - 속도 느리고 무겁지만 간단한 구현
- var, val차이
    - val (value)
        - 읽기 전용(Read-only) 변수
        - 한 번 초기화하면 값을 변경할 수 없음
        - 내부적으로는 final 변수처럼 동작함

    - var (variable)
        - 가변(mutable)변수
        - 값을 언제든지 재할당 가능

    - 사용목적
        - val 사용 경우
            - 변하지 않는 값 (상수, 참조만 고정)
            - 불변성을 유지
            - 더 안전한 코드와 의도를 명확히 하기 위해 사용
            - 참조는 고정되나 객체가 불변이냐 가변이냐는 따로 판단
                - 리스트 참조는 고정이나 리스트 아이템들은 변경 가능

        - var 사용 경우
            - 이후에 값을 바꿔야 하는 경우
            - 상태가 바뀌는 모델(뷰모델, UI상태 등)에 사용

    - 성능/안정성 측면
        - val을 우선 사용하는 것이 불변성 유지 + 코드 안정성에 더 유리
        - Kotlin 공식 스타일 가이드도 기본적으로 val 을 선호함
        - 필요할 때는 var 사용 -> 예상치 못한 변경을 방지 가능

- val, const val, var, lateinit var
    - val, const val
        - val
            - 런타임에 값을 할당함 (실행 중에 결정될 수 있음)
                ```kotlin
                val versionName = BuildConfig.VERSION_NAME
                ```
            - 클래스 내부나 함수 내부 어디서나 사용 가능
            - 객체 생성 시 초기화 가능 (동적 값도 가능)
        - const val
            - 컴파일 타임 상수 (값이 컴파일 시점에 고정되어야 함)
            - 오직 top-level, object 또는 companion object 내에서만 선언 가능
            - String, Int, Boolean 등 기본 타입만 사용 가능
            - Android에서는 주로 상수 정의할 때 사용 (Intent키, 설정값 등)
                ```kotlin
                const val EXTRA_USER_ID = "extra_user_id"
                ```
    - var, lateinit var
        - var
            - 가변 변수
            - 선언 즉시 초기화 필요
        - lateinit var
            - var 처럼 가변 변수이나 선언만 하고 나중에 초기화 가능
            - 반드시 Non-null 타입이어야 하며, primitive 타입(Int, Boolean)에는 사용 불가
            - 보통 DI, ViewModel, 의존성 주입, 초기화 지연이 필요한 변수에 사용
            - 초기화 전에 접근하면 UninitializedPropertyAccessException 발생

    - 요약
        - val → 변하지 않는 일반 값
        - const val → 컴파일 시점 고정 상수 (기본 타입 상수 정의에 사용)
        - var → 즉시 초기화 가능한 가변 값
        - lateinit var → 나중에 초기화될 참조 타입 값 (nullable 아님)

- 코틀린에서 두드러지는 특징
    - 개요
        - 간결성 + 안정성 + 실용성 핵심 철학
        - 안드로이드 + 백엔드 + 웹 + 데스크탑 등에서도 널리 사용
        - 자바보다 더 표현력 높고 오류 감소되는 구조 제공

    - 널 안정성 (Null Safety)
        - NullPointerException (NPE)을 언어 차원에서 원천 차단
        - Nullable(String?)과 Non-nullable 타입을 명확히 구분
        - 컴파일 타임에 null 관련 오류를 미리 감지 가능
            ```kotlin
            val name: String = "Aiden"
            val nullableName: String? = null
            println(nullableName?.length) // Safe Call
            ```

    - 간결한 문법 (Concise Syntax)
        - getter/setter, new, 세미콜론, 명시적 타입 선언 등이 불필요
        - 람다 표현식, 확장함수, 스마트 캐스팅 등을 활용해 간결한 코드 작성 가능
            ```kotlin
            val list = listOf(1, 2, 3).filter { it > 1 }.map { it * 2 }
            ```

    - 스마트 캐스팅 (Smart Casting)
        - is 체크 이후, 별도의 형 변환없이 자동으로 해당 타입으로 캐스팅
            ```kotlin
            fun printLength(obj: Any) {
                if (obj is String) {
                    println(obj.length) // obj는 String으로 자동 캐스팅됨
                }
            }
            ```

    - 확장 함수와 확장 프로퍼티
        - 기존 클래스에 기능 추가 가능 (라이브러리나 안드로이드 API 확장에 유용)
            ```kotlin
            fun String.addPrefix(prefix: String): String = "$prefix$this"
            ```

    - 함수형 프로그래밍 지원
        - 고차 함수, 람다, map/filter/reduce 등 함수형 프로그래밍 스타일을 자연스럽게 지원
        - 일급 함수, 비동기 처리를 간결하게 작성 가능
            ```kotlin
            val sum = listOf(1, 2, 3).fold(0) { acc, i -> acc + i }
            ```

    - 코루틴(Coroutines) 기반 비동기 프로그래밍
        - 쓰레드가 아닌 경량 스레드 방식으로 비동기 작업을 효율적으로 처리
        - suspend, launch, async, flow 등을 통해 복잡한 비동기 로직도 간단하게 구현 가능
            ```kotlin
            suspend fun fetchData() {
                withContext(Dispatchers.IO) {
                    // 백그라운드 작업
                }
            }
            ```

    - 데이터 클래스 (data class)
        - equals, hashCode, toString, copy() 등 기본 메서드 자동 생성
        - DTO/모델 클래스 정의 시 매우 유용
            ```kotlin
            data class User(val name: String, val age: Int)
            ```

    - Sealed Class / Enum Class
        - ADT(Algebraic Data Type) 표현 가능 -> 타입에 따라 안전하게 분기 처리 가능
        - when과 함께 사용할 때 컴파일러가 분기 누락을 체크
         ```kotlin
         sealed class UiState
         object Loading : UiState()
         data class Success(val data: String) : UiState()
         object Error : UiState()
         ```

    - 안드로이드 친화성
        - Jetpack Compose, Coroutine, KTX 등과 궁합이 좋음
        - 구글 공식 안드로이드 언어로 채택

- fold, reduce 차이
    - 개요
        - Kotlin 컬렉션에는 컬렉션 내의 데이터를 모두 모으는(Accumulate) 함수인 reduce()와 fold()가 있음

    - reduce()
        - 초기값 없이 첫번째 요소로 시작
            ```kotlin
            val numbers = listOf(7, 4, 8, 1, 9)

            val sum = numbers.reduce { total, num -> total + num }
            println("reduced: $sum") // reduced: 29
            ```
    - fold(): Java Stream 에서는 둘 다 reduce()
        - 지정해준 초기값으로 시작
            ```kotlin
            val numbers = listOf(7, 4, 8, 1, 9)
            
            // 초기 시작값 10
            val sumFromTen = numbers.fold(10) { total, num -> total + num }
            println("folded: $sumFromTen") // folded: 39
            ```
- 엘비스 연산자 (Elvis Operator)
    - 개념
        - 피연산자가 null일 경우 대체 값을 반환하는 연산자
    - 예제 추가 설명
        ```kotlin
        val result = a ?: b

        // 위 아래 두 코드는 동일한 코드
        val result = if (a != null) a else b

        // 아래는 다른 예제들
        val length = user?.name?.length ?: 0

        // null check + 예외처리를 한 줄로 표현 가능
        val user = findUserById(id) ?: throw IllegalArgumentException("User not found")
        ```

- 용어 정리
    - 일급 함수 (First Class Function)
        - 개념
            - 함수를 값처럼 취급할 수 있다 라는 의미
            - 함수가 변수에 저장, 파라미터로 전달, 리턴값으로 반환될 수 있으면 그 언어는 일급 함수를 지원한다라고 할 수 있음
                - 변수저장, 파라미터 전달, 리턴값 반환
        - 특징
            - 함수를 변수에 저장할 수 있음
            - 함수를 다른 함수에 전달할 수 있음
            - 함수에서 다른 함수를 반환할 수 있음
            - 함수 자체를 생성할 수 있음 (람다, 클로저 등)
        - 예시
            ```Kotlin
            val add: (Int, Int) -> Int = { a, b -> a + b }  // 변수에 함수 저장
            println(add(3, 5)) // 8
            ```

    - 고차 함수 (Higher Order Function)
        - 개념
            - 함수를 매개변수로 받거나 또는 함수를 리턴하는 함수
            - 즉, 함수를 인자로 받거나, 함수를 반환하는 함수
            - 고차 함수는 일급 함수가 지원되는 언어에서만 가능
        - 특징
            - 콜백 함수 전달 가능
            - 람다나 익명 함수로 간결한 표현 가능
            - 코드 재사용 및 추상화 수준 증가
        - 예시
            ```Kotlin
            fun operate(a: Int, b: Int, op: (Int, Int) -> Int): Int {
                return op(a, b)
            }

            val result = operate(10, 20) { x, y -> x + y }  // 고차 함수 사용
            println(result) // 30
            ```

    - 활용 예시
        - Java/Kotlin에서 콜백 전달: 버튼 클릭, 네트워크 응답 처리
        - JavaScript에서 map, filter, reduce: 배열 함수 대부분이 고차 함수
        - Swift의 closure, Python의 lambda:	람다 전달로 코드 간결화
        - RxJava / Flow / Coroutine: 대부분 고차 함수 기반의 연산 (map, flatMap, collect)

    - 결론 요약
        - 일급 함수는 "함수를 값처럼 다룰 수 있다"는 능력
        - 고차 함수는 "함수를 인자로 받거나, 반환하는 함수"라는 사용 형태
        - 고차 함수는 일급 함수가 가능한 언어에서만 구현 가능
        - 이 개념은 람다, 콜백, 클로저, 함수형 API 설계에 핵심

- 익명 함수, 람다, 클로저
    - 익명함수 (Anonymous Function)
        - 개념
            - 이름이 없는 함수
            - 함수 정의와 동시에 사용되며, 주로 일회성 목적으로 사용
        - 특징
            - 일반적인 함수와 동일한 구문을 갖지만 이름이 없음
            - 파라미터와 반환 타입 명시 가능
            - Java 8, Kotlin, Swift 등에서 지원
        - 예시
            ```kotlin
            val sum = fun(a: Int, b: Int): Int {
                return a + b
            }
            println(sum(3, 4)) // 7
            ```
    - 람다 표현식 (Lambda Expression)
        - 개념
            - 익명함수의 간단한 표현 방법
            - 함수를 간결하게 전달하고자 할 때 주로 사용
        - 특징
            - fun 키워드 생략 가능
            - 파라미터 타입 생략 가능 (타입 추론됨)
            - return 키워드도 생략 가능 (단일 표현식의 경우)
        - 예시
            - 람다는 본질적으로 익명함수이지만, 더 간결하고 함수형 스타일에 적합
            ```kotlin
            val sum = { a: Int, b: Int -> a + b }
            println(sum(5, 6)) // 11
            ```
    - 클로저 (Closure)
        - 개념
            - 자신이 생성된 환경(스코프)의 변수들을 함께 기억하는 함수 (외부 변수 참조를 기억하는 함수)
            - 즉, 외부 변수에 대한 참조(캡쳐)를 유지하는 함수 객체
            - Java 8+ 에서는 제한적 클로저 지원 (final or effectively final만, ()->{})
        - 특징
            - 지역변수를 캡쳐해서 함수 외부에서도 사용 가능
            - 함수 실행 후에도 그 지역변수가 GC되지 않고 살아 있음
            - 상태를 기억할 수 있어 상태 기반 콜백이나 은닉된 상태 관리에 유리
        - 예시
            - count는 makeCounter() 스코프 안의 지역변수지만, counter() 함수가 외부에서도 기억하고 접근 가능 -> 클로저 개념

    - 최종 정리 요약
        - 익명 함수: 이름 없는 함수, 함수도 값이다가 컨셉, 기본 표현
        - 람다: 익명 함수의 간결 버전, 고차 함수에서 자주 사용
        - 클로저: 외부 변수 캡처(상태 기억)를 통해 진정한 함수형 프로그래밍 가능

- 함수형 프로그래밍 (Function Programming)
    - 개요
        - 함수를 수학적 개념으로 다루고, 부작용 없이 상태를 예측 가능하게 만드는 프로그래밍 패러다임

    - 정의
        - 함수를 일급 시민(First Class Citizen)으로 다루며, 상태 변화나 부작용(Side Effect)을 피하고 순수 함수(Pure Function)를 조합하여 프로그램을 구성하는 방식
        - 즉, 코드가 예측 가능하고 디버깅이 쉽고 테스트가 용이하도록 만드는 방식

    - 주요 특징
        - (1) 순수 함수 (Pure Function)
            - 입력 -> 출력이 항상 같음
            - 외부 상태를 변경하지 않음 (부작용 없음)
                ```kotlin
                fun add(a: Int, b: Int): Int = a + b // 같은 입력이면 항상 같은 결과
                ```
        - (2) 부작용 없음 (Side Effect Free)
            - 함수 내부에서 파일 쓰기, 로그 출력, DB 저장 등 외부 상태 변경 금지
            - -> 코드를 테스트하기 쉽고 예측 가능
        - (3) 불변성 (Immutable State)
            - 변수는 가능한 val 선언
            - 상태 변경 대신 새 객체를 만들어 반환
                ```kotlin
                val list = listOf(1, 2, 3)
                val newList = list + 4 // 원본은 변하지 않음
                ```
        - (4) 고차 함수 (Higher Order Function)
            - 함수를 인자로 전달 또는 반환
        - (5) 일급 함수 (First Class Function)
            - 함수를 값처럼 저장, 전달, 반환 가능
        - (6) 함수 조합 (Composition)
            - 작은 순수 함수들을 조합해서 복잡한 로직을 구성
            - compose(), andThen() 같은 조합 메서드 사용

    - 함수형 프로그래밍 예시
        ```kotlin
        // 불변 컬렉션
        val numbers = listOf(1, 2, 3, 4, 5)

        // 함수형 스타일 (순수 함수, 고차 함수)
        val evenSquares = numbers
            .filter { it % 2 == 0 }      // 짝수 필터링
            .map { it * it }             // 제곱 계산
            .toList()

        println(evenSquares) // [4, 16]
        ```

    - 장점
        - 코드 예측 가능 (동일 입력 -> 동일 출력)
        - 테스트 용이 (상태가 없으므로 모킹 쉬움)
        - 병렬 처리에 강함 (공유 상태 없음)
        - 디버깅 및 추론 쉬움 (로직이 명확)
        - 코드 재사용성 높음

    - 단점
        - 진입 장벽
        - 과도한 불변성 관리 -> 새로운 객체 생성 등의 성능 오버헤드 가능성
        - 중간 상태 추적 어려움
        - 함수형이 과도하면 추상화 심화 가능성

- Java의 다형성(Polymorphism)이란 무엇이며, 구현 방법
    - 개요
        - 객체지향 프로그래밍(OOP)의 핵심 개념 중 하나로, Java에서도 매우 중요하게 사용되는 원리
    - 다형성 개념
        - 하나의 객체가 여러 가지 형태를 가질 수 있는 성질
            - 즉, 부모 타입의 참조 변수로 여러 자식 객체를 가리킬 수 있는 것
            - 동일한 메서드 호출이 객체에 따라 다르게 동작하게 됨
    - 다형성 종류
        - 컴파일타임 다형성: 메서드 오버로딩 (Overloading), 같은 이름의 메서드를 파라미터로 구분
        - 런타임 다형성: 메서드 오버라이딩 (Overriding), 자식 클래스에서 부모 메서드를 재정의
    - 다형성의 핵심 구성요소
        - 상속:	부모 클래스에서 자식 클래스가 상속받아야 함
        - 업캐스팅: 자식 객체를 부모 타입 변수로 참조
        - 메서드 오버라이딩: 부모 메서드를 자식이 재정의
        - 동적 바인딩: 실행 시점에 실제 객체의 메서드를 호출함
    - 구현 예제
        ```kotlin
        class Animal {
            void sound() {
                System.out.println("Some sound");
            }
        }

        class Dog extends Animal {
            void sound() {
                System.out.println("Bark");
            }
        }

        class Cat extends Animal {
            void sound() {
                System.out.println("Meow");
            }
        }

        public class Main {
            public static void main(String[] args) {
                Animal myAnimal = new Dog();  // 업캐스팅
                myAnimal.sound();  // → "Bark"

                myAnimal = new Cat();
                myAnimal.sound();  // → "Meow"
            }
        }
        ```
        - 핵심 설명
            - myAnimal은 Animal 타입이지만 실제 객체는 Dog 또는 Cat
            - sound() 메서드는 실행 시점에 실제 객체 타입에 따라 동작
            - 이것이 바로 런타임 다형성 + 동적 바인딩

    - 업캐스팅과 다운캐스팅
        - 업캐스팅:	자식 → 부모 타입으로 자동 변환	Animal a = new Dog();
        - 다운캐스팅: 부모 → 자식 타입으로 수동 캐스팅	Dog d = (Dog) a; (명시적 필요)
            - 다운캐스팅은 잘못하면 ClassCastException 발생 주의

    - 다형성의 장점
        - 코드 재사용성 ↑: 동일한 메서드명으로 다양한 동작 처리
        - 유지보수성 ↑: 새로운 클래스를 추가해도 기존 코드 수정 최소화
        - 유연성 ↑: 부모 타입을 기준으로 동작을 추상화 가능
        - 설계 확장성 ↑: 인터페이스/추상 클래스 기반 설계에 적합

    - 다형성과 인터페이스
        - interface도 다형성의 한 형태로 사용됨 → 다양한 구현체 처리 가능
        ```java
        interface Drawable {
            void draw();
        }

        class Circle implements Drawable {
            public void draw() {
                System.out.println("Drawing Circle");
            }
        }

        class Square implements Drawable {
            public void draw() {
                System.out.println("Drawing Square");
            }
        }

        public class Main {
            public static void main(String[] args) {
                Drawable shape = new Circle();
                shape.draw(); // "Drawing Circle"
            }
        }
        ```

    - 결론
        - 개념: 하나의 객체가 여러 형태를 가질 수 있는 특성
        - 필수 조건: 상속, 오버라이딩, 업캐스팅
        - 구현 방식: 컴파일타임: 오버로딩, 런타임: 오버라이딩
        - 핵심 효과: 동적 바인딩, 유연한 코드 설계, 유지보수성 향상

- Java에서 오버로딩(Overloading)과 오버라이딩(Overriding)의 차이점
    - 개념 차이
        - 정의	
            - 오버로딩: 같은 이름의 메서드를 다른 파라미터로 여러 개 정의	
            - 오버라이딩: 상속 관계에서 부모 메서드를 자식이 재정의
        - 위치	
            - 오버로딩: 같은 클래스 내에서 정의	
            - 오버라이딩: 부모-자식 클래스 간에서 정의
        - 매개변수	
            - 오버로딩: 개수, 타입, 순서가 달라야 함
            - 오버라이딩: 부모와 매개변수, 반환타입이 동일해야 함
        - 반환 타입	
            - 오버로딩: 다를 수 있음	
            - 오버라이딩: 같아야 함 (또는 공변 반환 타입)
        - 접근자	
            - 오버로딩: 자유롭게 가능
            - 오버라이딩: 부모보다 더 좁은 접근 제한자는 불가
        - 키워드	
            - 오버로딩: X	
            - 오버라이딩: @Override 사용 권장

    - 목적 차이
        - 유연성
            - 오버로딩: 다양한 파라미터에 대해 같은 의미의 동작 수행
            - 오버라이딩: 자식 객체별 고유 동작을 정의
        - 코드 가독성
            - 오버로딩: 함수명을 일관되게 유지
            - 오버라이딩: 다형성(Polymorphism)을 실현

- Java에서 인터페이스(Interface)와 추상 클래스(Abstract Class)의 차이점
    - 개념 차이
        - 정의	
            - 인터페이스: 완전히 추상적인 타입(100% 추상화)	
            - 추상클래스: 부분적으로 구현된 클래스
        - 상속 방식	
            - 인터페이스: 다중 구현 가능 (implements)
            - 추상클래스: 단일 상속만 가능 (extends)
        - 필드	
            - 인터페이스: public static final 상수만 허용	
            - 추상클래스: 일반 필드 사용 가능
        - 메서드	
            - 인터페이스: 기본적으로 추상 메서드 (Java 8부터 default/static 가능)	
            - 추상클래스: 추상 메서드 + 일반 메서드 모두 허용
        - 생성자	
            - 인터페이스: 없음	
            - 추상클래스: 생성자 있음
        - 목적	
            - 인터페이스: 기능 정의 (기능 명세서 역할)	
            - 추상클래스: 공통 기능 구현 + 재사용

- Immutable 변수와 Mutable 변수를 쓰면 좋은점
    - 개념
        - Immutable
            - 한 번 값을 할당하면 변경 불가
        - Mutable
            - 값 변경 가능

    - Immutable 변수를 사용하면 좋은 점
        - (1) 안정성(Safety) 증가
            - 값이 절대 바뀌지 않기 때문에 버그 발생 가능성 감소
            - 특히 멀티스레드 환경에서 매우 중요함 → 동기화 처리 필요 없음

        - (2) 코드 가독성 향상
            - "이 값은 바뀌지 않는다"는 의도를 코드 수준에서 표현
            - 함수형 프로그래밍 스타일과 궁합이 좋음

        - (3) 디버깅이 쉬움
            - 상태 변경이 없으므로 로직 추적이 단순함

        - (4) 부작용(Side Effect) 제거
            - 함수 내부에서 값을 바꾸지 않으니 외부에 영향을 주지 않음 → 순수 함수화 가능

    - Mutable 변수를 사용하면 좋은 점
        - (1) 유연한 상태 관리
            - UI 요소 상태, 누적 계산, 반복 루프에서 값 변경 등 필요 시 간단하게 처리

        - (2) 성능 측면에서 효율적일 수 있음
            - 불변 변수는 값 변경 시 새 객체를 생성 → 메모리 사용량 증가
            - 예: String → StringBuilder 사용으로 최적화 가능

        - (3) 로직 간단화
            - 상태가 변하는 경우 로직을 단순하게 구현 가능 (ex. count++)

    - 선택 기준
        - 초기 값이 이후 절대 바뀌지 않음: Immutable (val, final)
        - 함수 내부에서만 사용하고, 외부 노출 X: Mutable 사용해도 무방
        - 함수형 스타일, 순수 함수 작성 시: 무조건 Immutable
        - UI 상태 관리, 애니메이션 등: Mutable
        - 멀티스레드 환경에서 안전하게 동작해야 함: Immutable 권장

- 안드로이드에서 RxJava2 메모리 관리 하는 법
    - 개요
        - RxJava는 비동기 이벤트를 다루기 쉬운 구조를 제공하지만, 구독(Subscription)을 적절히 해제하지 않으면 리소스가 계속 유지되어 Activity나 Fragment가 GC되지 않고 누수가 발생

    - 메모리 누수 주요 원인
        - 구독(Subscribe) 해제하지 않음	
            - Observable, Flowable, Single 등을 구독한 후 dispose()를 호출하지 않으면 리스너가 살아있음
        - Activity/Fragment를 내부에서 참조	
            - 람다, 클로저, 리스너에서 this, context를 직접 참조하면 해당 객체가 해제되지 않음
        - 무한 스트림 or Timer/Interval	
            - 자동 종료되지 않는 스트림을 무한히 유지

    - 메모리 누수 방지를 위한 핵심 방법
        - (1) CompositeDisposable 사용 (가장 일반적)
            ```kotlin
            class MyViewModel : ViewModel() {
                private val disposables = CompositeDisposable()

                fun loadData() {
                    val disposable = api.getData()
                        .subscribeOn(Schedulers.io())
                        .observeOn(AndroidSchedulers.mainThread())
                        .subscribe({ result ->
                            // handle success
                        }, { error ->
                            // handle error
                        })

                    disposables.add(disposable)
                }

                override fun onCleared() {
                    super.onCleared()
                    disposables.clear() // 모든 구독 해제
                }
            }
            ```
            - Activity나 Fragment
                - onDestroy() 또는 onStop() 등 생명주기에 따라 dispose() 또는 clear() 호출 필요
        
        - (2) 자동 해제를 위한 라이프사이클 연동 (RxLifecycle, AutoDispose 등 활용)
            - RxLifecycle 예시
                ```kotlin
                observable
                    .compose(bindUntilEvent(ActivityEvent.DESTROY))
                    .subscribe()
                ```
            - AutoDispose 예시 (Google 권장)
                ```kotlin
                observable
                    .to(autoDisposable(AndroidLifecycleScopeProvider.from(this)))
                    .subscribe()
                ```
                - 라이프사이클 연동으로 자동 dispose 처리, 누수 방지

        - (3) 구독에서 context, this 직접 참조 금지
            ```kotlin
            // 위험한 코드
            someObservable.subscribe {
                textView.text = "Hello"  // 내부에서 Activity를 참조함
            }
            ```
            - 해결 방법
                - WeakReference 사용
                - Activity나 View를 ViewModel에서 직접 참조하지 않도록 설계

        - (4) 무한 Observable 처리 시 주의
            ```kotlin
            Observable.interval(1, TimeUnit.SECONDS)
                .subscribe { println("Tick") } // 무한 실행
            ```
            - takeUntil, takeWhile, dispose() 등으로 수명 관리

    - 추가 정보
        - CompositeDisposable.clear(): 모든 구독을 해제 (다시 추가 가능)
        - CompositeDisposable.dispose(): 모든 구독을 해제하고 객체도 종료
        - Flowable 사용 시: Backpressure 문제 주의, 구독자 없으면 데이터 누수 가능
        - Schedulers.trampoline(): 테스트 환경에서 블로킹 없이 순차 처리 가능

    - RxJava2 메모리 관리 체크리스트
        - CompositeDisposable 사용: 다수 구독을 묶어서 한 번에 관리
        - 생명주기에 따라 clear/dispose: onDestroy, onCleared, onStop 등에서 처리
        - RxLifecycle / AutoDispose 사용: 생명주기 연동으로 자동 관리
        - context 직접 참조 금지: 람다에서 Activity나 View 참조하지 말 것
        - 무한 Observable 관리: takeUntil, dispose() 등으로 수명 제어

- AOSP의 SELinux 정책과 보안 메커니즘
    - 개요
        - AOSP(Android Open Source Project) 의 SELinux(시큐리티 인핸스드 리눅스) 정책과 보안 메커니즘은 Android 플랫폼의 핵심 보안 방어선

    - SELinux 정의
        - SELinux(Security-Enhanced Linux) 는 리눅스 커널에 내장된 강제적 접근 제어(MAC: Mandatory Access Control) 시스템
            - 기존 리눅스의 권한 기반 모델(UID/GID)만으로는 부족한 보안을 강화
            - 권한을 갖고 있어도, 추가적으로 정책에 명시된 작업만 허용
            - Android 4.3(Jelly Bean)에서 처음 적용 → Android 5.0(Lollipop)부터 Enforcing Mode로 기본 활성화됨

    - Android AOSP 에서 SELinux의 역할
        - 프로세스 간 격리: 앱, 서비스, 시스템 프로세스를 강력하게 분리
        - 최소 권한 원칙 적용: 필요한 작업만 허용 (권한을 갖더라도 정책이 허용하지 않으면 차단)
        - 시스템 무결성 보호: 루트킹/커널 해킹/버그 악용 방지
        - 공격 표면 감소: 시스템 콤포넌트별 최소한의 접근 허용

    - SELinux의 기본 동작 방식
        - 기본 구조
            - 모든 객체(파일, 소켓, 프로세스 등) 에 Security Label(보안 컨텍스트) 부여
            - 모든 주체(프로세스) 도 Security Label을 가짐
            - 정책 파일(policy) 에 따라 "A가 B에 대해 X를 수행할 수 있는가?" 를 검사
        - 예시
            - System Server	u:r:system_server:s0
            - Wifi Service	u:r:wifi:s0
            - Data 파일	u:object_r:app_data_file:s0:c512,c768
        - 접근 제어 예시
            - 정책에서 명시적으로 허용되어야만 동작 허용됨
            ```less
            system_server (u:r:system_server:s0) 
                 → /data/misc/wifi (u:object_r:wifi_data_file:s0)
                 : read 권한 요청
            ```

    - Android SELinux 주요 정책 영역
        - file_contexts: 파일/디렉토리별 기본 Security Label 지정
        - sepolicy: 프로세스, 리소스 별 권한 허용/거부 규칙
        - property_contexts: system property에 대한 label 관리
        - service_contexts: 서비스(component) 별 보안 레이블 지정
        - mac_permissions.xml: 앱 설치 시 MAC(SELinux) 권한 매핑 처리

    - SELinux 상태 모드
        - Permissive: 위반을 허용하고 로그만 기록 (audit)
        - Enforcing: 위반 시 해당 액션 차단 (denied)
            - Android는 Enforcing 모드가 기본값
            - 개발/디버깅 중에는 Permissive로 임시 전환 가능 (adb shell 명령)
            - 명령
                - adb shell setenforce 0   # Permissive 모드
                - adb shell setenforce 1   # Enforcing 모드

    - SELinux 보안 메커니즘 요약
        - Context-Based Access: Label 기반 접근 제어
        - Type Enforcement: 주체-객체 간의 "type" 매칭 제어
        - Role-Based Access Control (RBAC): 사용자의 역할 기반 제어
        - Multi-Category Security (MCS): 프로세스나 파일에 대해 세밀한 분리
        - Least Privilege Principle: "꼭 필요한 권한만 부여" 전략

    - 실무에서 SELinux 정책 적용 예시
        - System 앱이 /data 디렉터리 접근 요청 → 정책에서 명시적으로 허용 필요
        - Vendor-specific Service(ex: Qualcomm, Samsung Service) 추가 시
            - → 새로 추가한 서비스에 대한 Label 설정 및 접근 권한 검토 필수
        - OEM Customization 시 → device-specific sepolicy 분리 필요

    - SELinux 정책 디버깅 툴
        - audit2allow
        - SELinux 보안 위반 로그 분석 흐름(dmesg, logcat 분석)
            - 예: avc: denied { read } for pid=123 comm="myapp" name="file"

    - 결론 요약
        - Android AOSP의 SELinux는 시스템 전체에 강제적 접근 통제를 부여해,
        - 앱 간, 시스템 컴포넌트 간, 커널 자원 간의 보안을 강화하는 핵심 방어선
            - 핵심 개념: MAC 기반 강제 접근 제어
            - 동작 방식: Label + Policy 검사
            - 적용 목적: 앱 격리, 시스템 무결성 보장
            - 실무 시 주의: 서비스 추가, Vendor 커스텀 시 sepolicy 검토 필수

- 안드로이드에서 Unit Test가 필요 한 이유
    - 개요
        - 품질 높은 앱을 만들기 위해 반드시 필요한 핵심 개발 관행
    - 필요한 이유
        - 코드의 정확성 검증
            - 유닛 테스트는 개별 함수나 클래스 단위에서 로직이 정확히 작동하는지 자동으로 검증해준다.
            - 실수로 조건문을 잘못 쓰거나 계산 로직에 오류가 생겨도, 테스트를 통해 빠르게 감지할 수 있다.
            - 버그가 배포 전에 걸러지므로, 전체 앱의 신뢰성이 높아진다.

        - 리팩토링의 안전망 제공
            - 앱의 구조를 개선하거나 기존 코드를 수정할 때, 기존 로직이 깨졌는지 여부를 확인하기 어렵다.
            - 유닛 테스트가 잘 갖춰져 있으면, 리팩토링 이후에도 이전과 동일한 동작을 하는지 자동으로 검증할 수 있다.
            - 테스트가 없는 코드는 수정하기가 무서워진다. 테스트는 개발자의 자신감을 보장해준다.

        - 개발 속도 향상
            - 처음에는 느려 보일 수 있지만, 유닛 테스트를 도입하면 반복적인 수동 테스트 시간이 줄어들고,
            - 버그 발생 시 원인을 빠르게 좁힐 수 있기 때문에 전체 개발 속도가 훨씬 빨라진다.
            - 특히 복잡한 앱 로직에서는 테스트 없이는 검증 시간이 오래 걸리고 디버깅도 어렵다.

        - 회귀 버그 방지
            - 이전 버전에서 잘 작동하던 기능이, 새로운 수정으로 인해 갑자기 오류가 나는 경우가 많다.
            - 이를 회귀 버그(Regression Bug) 라고 부르는데, 유닛 테스트는 이를 미리 차단해준다.
            - 테스트가 실패하면 어디서 문제가 발생했는지 바로 알 수 있어, 배포 전 문제를 미연에 방지할 수 있다.

        - 문서화 효과
            - 테스트 코드는 단순히 검증을 넘어서, 해당 함수가 어떻게 동작해야 하는지 보여주는 훌륭한 예제이자 문서가 된다.
            - 협업 시에도 다른 개발자가 테스트 코드를 보면, 함수의 사용법이나 입력/출력의 기대 결과를 쉽게 이해할 수 있다.

        - 품질 중심의 개발 문화 확립
            - 유닛 테스트를 꾸준히 작성하면 팀 전체가 테스트 가능하고 유지보수하기 쉬운 코드 구조를 설계하게 된다.
            - 이는 장기적으로 코드베이스의 복잡도를 낮추고, 유지보수 비용을 줄이는 효과를 낳는다.
            - 테스트 가능성이 높은 코드 = 설계가 잘 된 코드라는 것을 의미하기도 한다.

    - 결론
        - 유닛 테스트는 단순한 자동화 도구가 아니라, 안정적인 코드 작성, 빠른 개발, 리팩토링의 자신감, 협업 효율, 제품 품질 보장이라는 다양한 이점을 가진 개발의 필수 요소다.
        - Android에서도 ViewModel, UseCase, Repository 단위로 유닛 테스트를 설계하는 것은 대규모 프로젝트일수록 필수적인 습관이다.


- “개발 서버를 바라보는 어플” 과 “프로덕션 서버를 바라보는 어플”을 나눠서 관리해야 할 때 계획에 대한 설명
    - 목적: 나누는 이유
        - 개발 중에는 미완성 기능, 테스트 API, 디버깅 코드 등이 포함되며 불안정할 수 있다.
        - 프로덕션은 사용자에게 실제 제공되는 서비스이므로 안정성, 보안, 성능 보장이 필수다.
        - 하나의 빌드에서 실수로 개발용 설정으로 배포하면 심각한 장애 또는 보안 사고로 이어질 수 있다.
        - 따라서 개발용(Dev) 빌드와 운영용(Prod) 빌드를 명확히 분리하여 관리해야 한다.

    - 환경 분리
        -  Build Variant 활용 (Android 기준)
            - build.gradle에 productFlavors 또는 buildTypes 설정
            - 예: debug → 개발 서버, release → 프로덕션 서버
            ```gradle
            buildTypes {
                debug {
                    buildConfigField "String", "BASE_URL", "\"https://dev.api.example.com\""
                }
                release {
                    buildConfigField "String", "BASE_URL", "\"https://api.example.com\""
                }
            }
            ```
            - 코드에서는 BuildConfig.BASE_URL로 접근

    - 실제 관리 계획
        - 개발용 앱
            - 서버: 개발 서버 (Dev API, QA DB 등)
            - 앱 특징:
                - 디버그 로그 활성화
                - 비정상 상태 허용 (강제 에러 테스트 등)
                - 테스트 계정 하드코딩 가능
                - 기능 플래그 테스트 가능

        - 프로덕션 앱
            - 서버: 실제 운영 서버 (Live API, Production DB)
            - 앱 특징:
                - 로그 최소화 or 제거
                - 보안 적용 (난독화, 무결성 체크 등)
                - 사용 가능한 기능만 노출
                - 철저한 QA 및 서명된 APK

    - 네이밍/패키지 전략
        - 앱 이름: [앱명]-Dev, [앱명]-Live 구분
        - 패키지명: com.example.myapp.dev, com.example.myapp.prod 구분
        - 아이콘 색상, 라벨: 개발용은 구분되는 색상, 아이콘을 지정해 헷갈리지 않도록
        ```gradle
        productFlavors {
            dev {
                applicationIdSuffix ".dev"
                versionNameSuffix "-dev"
                resValue "string", "app_name", "MyApp (Dev)"
            }
            prod {
                resValue "string", "app_name", "MyApp"
            }
        }
        ```

    - 배포 및 QA 전략
        - CI/CD 파이프라인에서 자동으로 구분된 빌드 배포 (예: Firebase App Distribution)
        - 개발용은 QA팀, 테스터, 개발자용 내부 배포
        - 운영용은 정식 서명과 함께 Google Play 스토어 배포
        - Firebase, Sentry 등 로그 툴도 구분된 프로젝트 사용 권장

    - 실무 적용 팁
        - Flavor + BuildType 조합으로 devDebug, devRelease, prodRelease 등 세분화 가능
        - API 키, URL, Firebase 옵션 등을 gradle.properties 또는 local.properties로 외부 관리
        - Git 분기 전략도 develop vs main으로 구분하여 빌드 분리와 연동

    - 결론
        - 개발 서버용 앱과 운영 서버용 앱은 반드시 빌드 단계, 설정, 배포 방식, 보안 수준에서 분리되어야 하며, 이를 통해 테스트 안정성 확보, 실수 방지, 프로덕션 신뢰성 강화가 가능하다.

- DIP (Dependency Inversion Principle)
    - 개념
        - 상위 모듈은 하위 모듈에 의존하면 안 되고, 둘 다 추상화(인터페이스)에 의존해야 한다
        - 추상화는 구체화에 의존하면 안 되고, 구체화가 추상화에 의존해야 한다
        - 즉, 구체적인 구현(implementation) 에 의존하지 말고, 추상적인 인터페이스 에 의존해야 한다

    - 필요성
        - 코드가 유연하고 확장성 있게 만들어짐
        - 하위 모듈이 바뀌어도 상위 모듈은 영향 없이 동작 가능하게 하기 위함
        - 테스트 코드 작성 쉬워지며, 의존성 주입(DI)도 가능

    - 적용 방법
        - 뷰모델이 직접 레파지토리 구현체에 의존하는 것이 아닌 인터페이스에 의존해야 함
        - 실제 레파지토리 구현체는 나중에 주입해서 사용
        ```kotlin
        // 1. 추상화된 인터페이스
        interface UserRepository {
            fun getUser(id: String): User
        }

        // 2. 실제 구현체
        class UserRepositoryImpl(private val remoteDataSource: RemoteDataSource) : UserRepository {
            override fun getUser(id: String): User {
                return remoteDataSource.fetchUser(id)
            }
        }

        // 3. ViewModel은 인터페이스(UserRepository)만 의존
        class UserViewModel(private val userRepository: UserRepository) : ViewModel() {
            fun loadUser(id: String) {
                val user = userRepository.getUser(id)
                // ...
            }
        }
        ```
        - UserRepositoryImpl 을 변경해도 UserViewModel은 수정할 필요 없는 장점
        - 테스트 시에도 FakeUserRepository를 만들어서 UserViewModel에 삽입 가능

    - 결론
        - 구현체에 직접 의존하지 말고, 추상적인 인터페이스에 의존해야 한다.
        - DI Framework 인 Hilt, Dagger, Koin 등도 DIP를 기반으로 만들어짐

- ConstraintLayout의 장점
    - 복잡한 레이아웃을 한 번에 표현 가능
        - 기존에는 LinearLayout, RelativeLayout, FrameLayout 등을 여러 번 중첩해서 복잡한 화면 제작
        - ConstraintLayout은 한 번에 복잡한 레이아웃을 만들 수 있어서 View 계층(View hierarchy) 을 얕게 만들 수 있음
        - 결과적으로 성능(특히 렌더링 속도)이 개선

    - 성능 최적화 (Hierarchy Depth 감소)
        - View 트리의 깊이가 얕아지면 안드로이드 시스템이 레이아웃을 계산하고 그리는 시간 감소
        - ConstraintLayout은 내부적으로 측정(Measure)과 배치(Layout) 과정을 최적화해서 성능을 높임

    - 유연하고 강력한 제약 조건 설정
        - 각각의 View를 부모나 다른 View에 상대적으로 제약(Constraint) 을 걸 수 있음
        - 예를 들면:
            - 좌우 중앙 정렬
            - 다른 View의 바로 아래에 위치
            - 특정 비율(Aspect Ratio) 유지
            - 양쪽에 딱 맞게 늘어나기
        - 기존 레이아웃보다 훨씬 세밀한 위치 조정이 가능해.

    - 레이아웃 에디터(Design Editor)와 호환성
        - Android Studio에서 드래그 앤 드롭으로 제약을 설정 가능
        - 뷰 간 제약선을 시각적으로 확인하고 수정할 수 있어서, 특히 초보자나 복잡한 레이아웃 수정에 용이

    - 가로/세로 화면 대응, 다양한 해상도 대응 용이
        - Constraint를 상대적으로 잡기 때문에, 화면 크기가 달라져도 레이아웃이 자연스럽게 적응
        - 따로 dp를 일일이 계산하거나 별도로 land 레이아웃 파일을 만들 필요가 없는 경우도 있음

    - Chain, Group, Barrier, Guideline 같은 고급 기능 제공
        - Chain: 여러 View를 연결해서 자동 정렬이나 균등 분배 가능
        - Group: 여러 View를 하나로 묶어서 한 번에 제어 가능
        - Barrier: 여러 View의 가장자리 기준으로 제약 걸 수 있음
        - Guideline: 화면 안에 보이지 않는 선을 추가해서 위치 기준 설정 가능

    - 전체 요약
        - ConstraintLayout은 복잡한 화면을 중첩 없이 하나의 레이아웃으로 만들 수 있게 해주고, 성능까지 최적화해주는 강력한 레이아웃

- Activity Lifecycle (액티비티 라이프사이클) 재정리
    - (1) 생성 및 시작 단계
        - onCreate()
            - 액티비티가 처음 생성될 때 호출
            - UI 초기화, 데이터 바인딩, 뷰모델 연결, 리소스 로딩 수행
            - setContentView()로 레이아웃 설정하는 것도 수행
        - onStart()
            - 액티비티가 사용자에게 보이기 시작할 때 호출
            - 아직 포커스 갖지 못함, 화면에는 표시
            - 주로 UI 갱신 또는 화면에 필요한 리소스 준비하는 작업 수행
        - onResume()
            - 액티비티가 사용자와 상호작용 가능한 상태가 될 때 호출
            - 포커스 획득, 완전히 활성화
            - 애니매이션 시작, 센서 리스너 등록, 카메라 접근 등 실제 동작 시작하는 부분

    - (2) 일시 중지 및 정지 단계
        - onPause()
            - 다른 액티비티가 포커스를 가져올 때 호출
            - 화면은 여전히 보일 수 있지만, 포커스를 잃음
            - 센서 해제, 애니매이션 중단, 일시적 데이터 저장 등 수행
            - 시스템이 메모리가 부족하면 이 시점 이후에 액티비티를 종료시킬 수도 있음
        - onStop()
            - 액티비티가 완전히 화면에서 사라질 때 호출
            - UI가 더이상 사용자에게 보이지 않음
            - 무거운 리소스 해제 (네트워크 연결 해제, 브로드캐스트 리시버 해제)
    - (3) 다시 시작과 종료 단계
        - onRestart()
            - 액티비티가 onStop() 이후에 다시 사용자 앞에 나타날 때 호출
            - 일시정지된 액티비티를 재시작할 때 호출되고 이어서 onStart()로 넘어감
            - 화면을 갱신하거나 리소스를 다시 연결하는 작업을 여기서 준비
        - onDestroy()
            - 액티비티가 완전히 종료되기 직전에 호출
            - 시스템이 직접 종료하거나, finish() 호출했을 때 실행
            - 모든 리소스 해제, 쓰레드 종료, 메모리 정리 등 반드시 여기에서 수행
    - 생명주기 전체 흐름 요약
        - 생성: onCreate() → onStart() → onResume()
        - 일시 정지: onPause()
        - 정지: onStop()
        - 재시작: onRestart() → onStart() → onResume()
        - 종료: onPause() → onStop() → onDestroy()
    - 추가 설명
        - onPause()와 onStop() 차이
            - onPause()는 아직 화면에 보이지만 포커스를 잃은 상태
            - onStop()은 화면에서도 완전히 사라진 상태
        - onSaveInstanceState() 호출 시점
            - onSaveInstanceState() → onPause() → onStop()
            - 주로 onPause() 또는 onStop() 직전에 호출돼서, 임시 데이터를 저장할 기회를 준다.
            - (화면 회전 같은 구성 변경에 대비)
        - finish() 호출 시 흐름
            - onPause() → onStop() → onDestroy() 순서로 호출
    - 화면 회전 시
        - (1) 기본 동작
            - 화면 회전 시 액티비티는 완전히 재생성
            - 기존 화면 회전 전 액티비티: onPause() → onStop() → onDestroy() 종료
            - 새로운 액티비티 인스턴스: onCreate() → onStart() → onResume()
        - (2) 화면 회전 시 주의할 점
            - 화면 회전 시 액티비티가 다시 만들어지므로, 초기화한 데이터가 모두 사라질 가능성 존재
            - 회전에도 유지해야 할 데이터는 저장하거나 복구하는 처리가 필요
        - (3) 데이터 유지 방법
            - onSaveInstanceState(Bundle outState)
                - 화면이 회전되기 전에 시스템이 호출해서,
                - 현재 상태를 Bundle 객체에 저장할 수 있게 해준다.
                    ```kotlin
                    override fun onSaveInstanceState(outState: Bundle) {
                        super.onSaveInstanceState(outState)
                        outState.putString("KEY_NAME", name)
                    }
                    ```
            - onRestoreInstanceState(Bundle savedInstanceState)
                - onStart() 이후 호출돼서,
                - onSaveInstanceState()에 저장했던 데이터를 복구할 수 있다.
                - 또는 onCreate(savedInstanceState: Bundle?)안에서도 복구할 수 있음
                    ```kotlin
                    override fun onCreate(savedInstanceState: Bundle?) {
                        super.onCreate(savedInstanceState)
                        setContentView(R.layout.activity_main)
                        val name = savedInstanceState?.getString("KEY_NAME")
                    }
                    ```
        - (4) 화면 회전 시 생명주기 재생성 방지 방법
            - AndroidManifest.xml에 설정 추가
                - android:configChanges="orientation|screenSize"
                - → 이렇게 하면, 회전 시 직접 처리하고, 액티비티를 재생성하지 않는다.
                - 이렇게 설정하면, 회전 시 onConfigurationChanged() 메서드가 호출된다.
                - (주의: 이 방법은 일부 경우에만 추천, 복잡한 화면에서는 리스크가 커질 수 있다.)
        - 최종 정리
            - 화면 회전이 발생하면 액티비티는 기본적으로 완전히 재생성되며, 
            - 데이터를 유지하려면 onSaveInstanceState를 활용하거나, 
            - 특별히 필요한 경우 configChanges로 직접 제어할 수 있다.

- WeakReference 재정리
    - 개념 정의
        - WeakReference는 객체를 참조하지만, 
        - 해당 객체를 가비지 컬렉터(GC)가 수거할 수 있도록 허용하는 참조(Reference)를 의미
            - 일반적으로 객체를 Strong Reference(강한 참조)로 연결하면, GC는 그 객체를 절대 수거하지 못한다.
            - 하지만 WeakReference로 객체를 참조하면, GC가 객체를 "더 이상 강한 참조가 없을 경우" 수거할 수 있다.
        - 요약:
            - "필요하면 쓰고, 필요 없으면 GC가 알아서 치워줄 수 있게 하는 느슨한 참조"

    - 사용 이유/목적
        - 메모리 누수(Memory Leak)를 방지하려고 사용한다.
        - 특히 안드로이드에서는 Context(Activity, Fragment) 를 강한 참조로 오래 잡으면 메모리 릭이 발생할 수 있는데, 이를 예방할 때 쓴다.
        - 캐시(Cache) 를 만들 때도 쓴다.
            - → 메모리에 여유가 있을 땐 데이터를 유지하고, 메모리가 부족하면 알아서 버린다.

    - 주요 특징
        - WeakReference 객체가 참조하는 실제 객체는 GC가 수거해도 WeakReference 자체는 남아있을 수 있다.
        - get() 메서드를 호출하면, 아직 살아있는 객체를 가져올 수 있다. 만약 객체가 수거됐다면 get()은 null을 반환한다.
            ```kotlin
            val weakRef = WeakReference(Activity())
            val activity = weakRef.get()  // 아직 살아있으면 객체 반환, 아니면 null
            ```

    - 안드로이드에서 자주 쓰이는 사례
        - Handler + Activity 조합
            - 오래 실행되는 Handler가 Activity를 직접 참조하면 Activity가 GC되지 못하는 문제가 생긴다.
            - 이때 WeakReference로 Activity를 감싸서 참조해 해결한다.
            ```kotlin
            class MyHandler(activity: Activity) : Handler(Looper.getMainLooper()) {
                private val activityRef = WeakReference(activity)

                override fun handleMessage(msg: Message) {
                    val activity = activityRef.get() ?: return
                    // activity가 살아있을 때만 처리
                }
            }
            ```
            - Custom Cache 시스템 구현
                - LruCache처럼 사용자가 직접 캐시를 만들 때, 메모리 부족 시 자동 삭제를 허용하기 위해 WeakReference로 객체를 저장하기도 한다.

    - 주의할 점
        - WeakReference라고 무조건 메모리 릭을 막아주는 것은 아니다.
            - 강한 참조가 남아있으면 의미가 없다.
        - WeakReference로 감싸더라도, 무분별하게 사용하면 코드 가독성과 안정성을 해칠 수 있다.
        - 자주 접근하는 객체를 WeakReference로 감싸면 null 체크를 매번 해야 해서 코드가 복잡해질 수 있다.

    - 요약
        - WeakReference는 객체를 부드럽게 참조하여, 필요하면 쓰고 메모리 부족 시 자동으로 GC가 수거할 수 있도록 돕는 참조 방식이다. 
        - 메모리 릭을 방지하거나 캐시를 구현할 때 유용하다.

- WeakReference, SoftReference, PhantomReference 차이
    - WeakReference
        - 개념
            - 객체를 참조하지만, GC가 강한 참조(Strong Reference)가 없으면 바로 수거할 수 있도록 허용하는 참조.
        - 특징
            - 메모리가 충분하든 부족하든, Strong Reference가 없으면 바로 수거된다.
            - get() 메서드를 호출하면 살아 있는 객체를 가져올 수 있다. (GC 후에는 null)
        - 주요 사용처
            - 메모리 누수 방지
            - 오래 잡고 있을 필요 없는 객체 참조
            - Handler나 Context 참조 시 메모리 릭 방지

    - SoftReference
        - 개념
            - 객체를 참조하지만, 메모리가 부족할 때에만 수거하는 참조.
        - 특징
            - 강한 참조는 아니지만, WeakReference보다 오래 살아남는다.
            - 메모리가 충분하면 계속 유지된다.
            - 메모리가 부족해지면 GC가 SoftReference 객체를 수거하여 메모리를 확보한다.
        - 주요 사용처
            - 이미지 캐시, 대용량 데이터 캐시
            - 메모리가 허용하는 한 유지하고, 부족할 때만 제거하고 싶은 데이터

    - PhantomReference
        - 개념
            - 객체가 GC에 의해 수거된 이후를 감지할 수 있도록 하는 참조.
            - get() 메서드로 객체를 가져올 수 없다. (항상 null)
        - 특징
            - 수거된 시점을 세밀하게 감시할 수 있다.
            - ReferenceQueue와 함께 사용하여 객체가 사라진 직후 별도 처리를 할 수 있다.
            - 직접 메모리를 해제해야 하는 경우 등에 유용하다 (ex: Direct ByteBuffer 정리)
        - 주요 사용처
            - 리소스 정리(메모리 직접 해제 필요 시)
            - 객체가 죽은 뒤 정밀한 후처리 작업

    - 요약
        - WeakReference는 "강한 참조가 없으면 바로 수거"
        - SoftReference는 "메모리가 부족할 때만 수거"
        - PhantomReference는 "객체가 수거된 이후를 감지해서 후처리"

    - 추가 설명
        - WeakReference는 가벼운 메모리 누수 방지용. (Activity, Context 참조 등에 사용)
        - SoftReference는 캐시용. (메모리 여유가 있으면 남겨두고, 없으면 버림)
        - PhantomReference는 리소스 직접 정리용. (특수한 경우에만 사용)

- Parcelable 개념
    - 개념 정의
        - Parcelable은 안드로이드에서 객체를 직렬화(Serialize)하여 다른 컴포넌트(Activity, Service 등) 간에 빠르게 전달할 수 있도록 하는 인터페이스이다.
        - 즉, 메모리 상의 객체를 바이트 단위로 변환해서, Intent, Bundle, IPC(프로세스 간 통신) 등에 효율적으로 담아서 전송할 수 있게 해준다.

    - 필요 이유
        - 안드로이드는 기본적으로 컴포넌트 간 데이터를 주고받을 때 Bundle이나 Intent에 객체를 담아 전달해야 한다.
        - 그런데 일반 객체는 직접 담을 수 없기 때문에, 직렬화(Serialization) 과정이 필요하다.
            - Java의 Serializable 인터페이스도 사용할 수 있지만,
            - Parcelable은 성능(속도, 메모리 효율성) 면에서 훨씬 최적화되어 있어 안드로이드에서는 Parcelable 사용이 권장된다.
    - 기본 사용 방법
        - 클래스에 Parcelable 인터페이스를 구현한다.
        - 객체의 필드를 Parcel에 쓰고 읽는 코드를 직접 작성해야 한다.
        - CREATOR라는 static 필드를 반드시 정의해야 한다.
        ```kotlin
        import android.os.Parcel
        import android.os.Parcelable

        data class User(val name: String, val age: Int) : Parcelable {
            constructor(parcel: Parcel) : this(
                parcel.readString() ?: "",
                parcel.readInt()
            )

            override fun writeToParcel(parcel: Parcel, flags: Int) {
                parcel.writeString(name)
                parcel.writeInt(age)
            }

            override fun describeContents(): Int = 0

            companion object CREATOR : Parcelable.Creator<User> {
                override fun createFromParcel(parcel: Parcel): User {
                    return User(parcel)
                }

                override fun newArray(size: Int): Array<User?> {
                    return arrayOfNulls(size)
                }
            }
        }
        ```
    - 특징과 주의사항
        - 직접 데이터 읽기/쓰기 구현이 필요하다. (Serializable은 자동)
        - 빠르지만 코드가 많아질 수 있다.
        - 데이터 손상 방지를 위해 읽고 쓰는 순서를 정확히 맞춰야 한다.
        - Kotlin에서는 @Parcelize 어노테이션을 활용해 자동으로 Parcelable 구현을 쉽게 만들 수 있다.
        ```kotlin
        @Parcelize
        data class User(val name: String, val age: Int) : Parcelable
        ```
        - @Parcelize를 사용하면 읽고 쓰는 코드를 직접 작성하지 않아도 된다.
        - 단, kotlin-parcelize 플러그인 적용이 필요하다.

    - 요약
        - Parcelable은 안드로이드에서 객체를 빠르고 효율적으로 직렬화하여 컴포넌트 간 데이터 전달을 가능하게 하는 인터페이스

    - 추가 설명
        - Parcelable은 프로세스 간 통신(IPC) 에서도 많이 사용된다. (ex: AIDL)
        - Intent, Bundle 등에 객체를 담아서 Activity/Service 간 주고받을 때 기본처럼 사용된다.
        - Serializable은 속도가 느리고 GC 부하가 커서, 안드로이드에서는 성능 이유로 Parcelable을 주로 사용한다.

- 인플레이션(inflation)
    - 정의
        - XML로 정의된 레이아웃 리소스 파일을 실제 뷰(View) 객체로 메모리에 생성하는 과정
        - XML 파일(정적인 설계도)을 메모리 상에 동적으로 View 객체 트리로 변환하는 과정
        - XML 레이아웃을 실제 뷰 객체로 메모리에 로드하는 과정
    - 필요 이유
        - 안드로이드에서는 레이아웃을 res/layout 폴더에 XML 파일로 미리 작성한다.
        - 하지만 앱이 실행될 때는 XML 파일을 직접 사용할 수 없고, 반드시 Java/Kotlin 코드에서 동작하는 View 객체로 변환되어야 한다.
        - 이 변환 과정을 수행하는 것이 바로 LayoutInflater이고, 이 과정을 Inflation이라고 부른다
    - 주요 사용 예시
        - 액티비티
            - setContentView(R.layout.activity_main)
        - 프래그먼트
            - onCreateView -> return inflater.inflate(R.layout.fragment_example, container, false)
            - 프래그먼트에서는 LayoutInflater 객체를 직접 받아서 필요한 XML 레이아웃을 뷰 객체로 인플레이트해서 반환
        - 리싸이클러뷰 뷰홀더
            - val view = LayoutInflater.from(parent.context).inflate(R.layout.item_view, parent, false)
            - return ItemViewHolder(view)
            - 리싸이클러뷰에서는 리스트 아이템의 뷰를 재사용하기 때문에 onCreateViewHolder 단계에서 아이템 레이아웃을 인플레이트한다

- Java에서 Lombok 라이브러리를 사용할 때 장점과 단점
    - Lombok 개념
        - Lombok은 Java 코드에서 반복적인 보일러플레이트 코드(예: getter, setter, constructor 등)를 자동으로 생성해주는 라이브러리
            - Getter/Setter, 생성자 등 자동 생성 라이브러리
        - 컴파일 시점에 애노테이션 프로세서(annotation processor)를 통해 소스 코드에 필요한 메서드를 삽입한다.

    - 장점
        - ① 코드 간결화
            - @Getter, @Setter, @ToString, @EqualsAndHashCode, @NoArgsConstructor, @AllArgsConstructor 등 애노테이션만 붙이면
            - 반복적이고 지루한 코드 작성 없이 필요한 메서드를 자동 생성할 수 있다.
            - 클래스가 짧고 명확해지고, 핵심 비즈니스 로직에 집중할 수 있다.

        - ② 생산성 향상
            - 보일러플레이트 코드를 직접 작성하거나 수정할 필요가 없으므로, 개발 속도가 빨라진다.
            - 특히, DTO, VO, Entity 클래스 작성 시 매우 큰 효율을 볼 수 있다.

        - ③ 유지보수성 개선
            - 코드 변경 시, 불필요한 getter/setter 수정으로 인한 오류 가능성을 줄인다.
            - 메서드 수정이 필요하면 필드 선언만 수정해도 자동 반영되므로 관리가 쉽다.

        - ④ 가독성 향상
            - 클래스가 본질적인 필드와 주요 로직 중심으로 간결하게 유지되기 때문에
            - 전체 구조 파악이 더 쉽다.

    - 단점
        - ① 디버깅 어려움
            - 실제 코드에는 존재하지 않지만, 컴파일 후 생성된 메서드가 동작하기 때문에
            - IDE 디버깅 시 소스 코드와 실제 실행되는 메서드가 불일치할 수 있다.
            - 디버깅 과정이 불편해질 수 있다.

        - ② IDE 의존성
            - Lombok을 제대로 사용하려면 IDE 플러그인 설치가 필요하다.
            - (예: IntelliJ IDEA, Eclipse 등에서 Lombok 지원 설정)
            - IDE가 Lombok을 지원하지 않거나 플러그인 버전이 맞지 않으면, 컴파일은 되는데 IDE에서는 에러처럼 보이는 문제가 생길 수 있다.

        - ③ 코드 명시성 감소
            - 생성된 메서드가 소스 코드에 명시적으로 드러나지 않기 때문에,
            - 다른 개발자가 코드를 처음 볼 때 동작을 바로 이해하기 어려울 수 있다.

        - ④ 빌드 도구/환경 호환 이슈
            - Lombok은 annotation processor를 사용하는 특성상,
            - 특정 빌드 툴(Gradle, Maven) 설정이나 특정 버전에서 호환성 문제가 발생할 수 있다.
            - 빌드 자동화/CI 환경에서도 추가 설정이 필요한 경우가 있다.

    - 요약
        - Lombok은 코드 간결성과 생산성을 크게 높여주지만, 디버깅 어려움과 IDE 의존성, 명시성 감소라는 리스크를 함께 수반한다.

- Java에서 CompletableFuture를 활용하는 방법
    - CompletableFuture 개념
        - 비동기(Asynchronous) 프로그래밍을 쉽게 할 수 있도록 제공하는 Java의 표준 API.
        - Java 8에서 java.util.concurrent 패키지에 추가되었다.
        - 기존 Future의 한계(완료 확인을 블로킹해야 함)를 극복하여, 논블로킹(Non-Blocking) 방식으로 비동기 작업을 조합할 수 있다.
        - 여러 비동기 작업을 직렬(then...) 또는 병렬(combine...) 로 쉽게 연결할 수 있다.
        - CompletableFuture는 비동기 작업을 논블로킹 방식으로 연결하고 조합할 수 있게 해주는 Java의 강력한 Future API

    - 기본 사용 방법
        - (1) 비동기 작업 실행
            - supplyAsync()는 리턴값이 있는 비동기 작업을 실행한다.
            ```java
            CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
                // 비동기로 수행할 작업
                return "Hello";
            });
            ```
        - (2) 결과 처리 (thenApply)
            - 앞선 결과를 받아 변환하는 동작을 비동기로 연결
            ```java
            CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> "Hello")
                .thenApply(result -> result + " World");
            System.out.println(future.join());  // 출력: Hello World
            ```
        - (3) 결과 소비 (thenAccept)
            - 결과를 받아 소비만 하고, 리턴값은 없다
            ```java
            CompletableFuture.supplyAsync(() -> "Hello")
                .thenAccept(result -> System.out.println(result));
            ```
        - (4) 두 작업 조합 (thenCombine)
            - 두 개의 CompletableFuture 결과를 받아 조합한다.
            ```java
            CompletableFuture<String> future1 = CompletableFuture.supplyAsync(() -> "Hello");
            CompletableFuture<String> future2 = CompletableFuture.supplyAsync(() -> "World");

            CompletableFuture<String> combined = future1.thenCombine(future2, (f1, f2) -> f1 + " " + f2);

            System.out.println(combined.join());  // 출력: Hello World
            ```
        - (5) 작업 완료 후 추가 행동 (whenComplete)
            - 작업 성공/실패 여부에 관계없이 후처리 가능
            ```java
            CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
                if (true) throw new RuntimeException("Error");
                return "Hello";
            }).whenComplete((result, exception) -> {
                if (exception != null) {
                    System.out.println("Exception: " + exception.getMessage());
                } else {
                    System.out.println("Result: " + result);
                }
            });
            ```

- Java에서 메모리 누수를 방지하는 방법
    - 메모리 누수
        - 프로그램이 더 이상 필요로 하지 않는 객체를 참조하고 있어 GC가 메모리를 회수하지 못하는 상황
        - Java는 GC가 자동으로 메모리를 관리하지만 참조를 잘못 관리하면 여전히 메모리 누수가 발생할 수 있음

    - 메모리 누수 방지하는 주요 방법
        - (1) 객체 참조 해제
            - 사용이 끝난 객체에 대해 null을 명시적으로 할당하여 참조 끊는다.
            - list = null;
        - (2) WeakReference 사용
            - 객체가 더 이상 필요 없을 때 GC가 회수할 수 있다.
            - 주로 캐시 또는 리스너 관리 시 사용
        - (3) 리스너(Listener) 및 콜백 (Callback) 해제
            - 등록한 리스너나 콜백을 제때 제거하지 않으면, 참조가 남아 메모리 누수를 유발
            - 특히 안드로이드에서 액티비티/프래그먼트가 끝났을 때 리스너 해제가 중요
            - button.setOnClickListener(null);
        - (4) 내부 클래스(inner class) static 변경
            - 비정적(Non-static) 내부 클래스는 외부 클래스(예: 액티비티, 프래그먼트)를 암묵적으로 참조한다.
            - 필요 없는 참조 방지를 위해 내부 클래스를 static으로 선언 또는 WeakReference 사용
        - (5) 대용량 컬렉션 관리
            - List, Map, Set 등 컬렉션 사용 시 불필요 시 clear() 호출 > 내부 객체 참조 제거 > 메모리 확보한다.
            - list.clear();, list = null;
        - (6) 스레드 관리
            - 작업 완료 후 중지시키고 참조를 끊는다.
            - thread.interrupt();, thread = null;
        - (7) 적절한 툴 사용 (메모리 분석)
            - Android Studio Profiler, VisualVM, Eclipse MAT(Memory Analyzer Tool) 등을 사용해 메모리 사용량과 누수 지점을 주기적으로 분석한다.
            - 누수 가능성이 있는 패턴(Object Retain, Heap Dump 등)을 조기에 발견할 수 있다.

- Java에서 Java Flight Recorder(JFR)를 사용 이유가
    - Java Flight Recorder(JFR) 개념
        - JVM 내부 동작을 매우 낮은 오버헤드로 기록하는 프로파일링 및 모니터링 도구다.
        - Oracle JDK 7u40 이상, OpenJDK 11 이상부터 기본 내장되어 있다.
        - CPU 사용량, 메모리 할당, GC 활동, 스레드 상태 등 다양한 실행 데이터를 런타임 중 실시간으로 수집하고 분석할 수 있다.

    - Java Flight Recorder를 사용하는 주요 이유
        - ① 매우 낮은 오버헤드로 실시간 데이터 수집
            - 기존 프로파일러는 성능에 큰 부하를 주는 경우가 많지만,
            - JFR은 JVM 자체에 최적화되어 있어 오버헤드가 매우 낮다.
            - 실서비스(Production) 환경에서도 성능에 큰 영향을 주지 않고 데이터를 수집할 수 있다.

        - ② 성능 문제 분석(Performance Tuning)
            - GC 지연, 메모리 할당 문제, 스레드 병목, 클래스 로딩 지연 등
            - 실제 애플리케이션 성능 저하 원인을 정밀하게 분석할 수 있다.
            - 프로파일링 없이 막연히 추측하지 않고, 구체적인 수치를 기반으로 튜닝이 가능하다.

        - ③ 오류 및 장애 분석
            - 서비스 장애나 성능 이슈가 발생했을 때,
            - JFR 데이터만으로 당시 JVM 내부 상태를 정확히 재현하고 분석할 수 있다.
            - 힙 메모리, 스레드 상태, 잠금(Lock) 충돌, 메서드 호출 트레이스 등을 확인하여
            - 근본 원인(Root Cause Analysis) 을 빠르게 찾을 수 있다.

        - ④ 이벤트 기반 데이터 기록
            - JFR은 JVM 및 애플리케이션 레벨의 다양한 이벤트(Event) 들을 수집한다.
            - 예를 들어, GC 이벤트, 스레드 스케줄링, 메소드 호출, 예외 발생, 파일 I/O 활동 등.
            - 개발자가 직접 커스텀 이벤트(Custom Event) 를 만들어 필요한 데이터를 추가 기록할 수도 있다.

        - ⑤ 장기 모니터링 및 운영 데이터 축적
            - 장기간에 걸친 JVM 상태 변화를 기록하여, 성능 트렌드 분석이나 장기적인 리스크 탐지에도 활용할 수 있다.
            - 예를 들어, 점진적 메모리 증가(메모리 누수) 패턴 탐지에도 유용하다.

        - ⑥ 다양한 분석 툴과 연동
            - 수집한 .jfr 파일은 Java Mission Control(JMC) 또는 다른 시각화 도구를 통해 그래픽 기반으로 쉽게 분석할 수 있다.
            - VisualVM, JMC, 혹은 일부 APM 솔루션들과 연계할 수도 있다.

    - 정리
        - Java Flight Recorder는 실시간으로 JVM 내부 동작을 낮은 오버헤드로 기록하여, 성능 분석, 장애 분석, 운영 모니터링에 필수적인 도구다.

- Java의 Optional 클래스를 사용하는 이유
    - Optional 개념
        - Optional<T>는 널이 될 수 있는 값을 명시적으로 표현하디 위한 컨테이너 클래스
        - 자바 8부터 도입, 객체가 존재할 수도 있고(널이 아닐 수도 있고), 널일 수도 있는 상황을 명확하게 표현 가능

    - Optional 사용 주요 이유
        - (1) 널 포인터 예외 방지
            - NPE 예방이 가장 큰 목적
            - 메서드 리턴 타입을 Optional로 명시하면, 호출하는 쪽에서 null여부를 의식적으로 체크하도록 강제 가능
            ```java
            Optional<String> findName() {
                return Optional.ofNullable(null);
            }
            ```
            - 무심코 널 반환 또는 널 값 다루는 실수 감소 효과

        - (2) 코드 가독성 향상
            - if (x != null) 같은 널 체크 코드 중복 문제 감소 효과
            - Optional의 메서드 체이닝 > 가독성 증대
            ```java
            Optional.ofNullable(user)
                .map(User::getName)
                .ifPresent(System.out::println)
            ```

        - (3) 반환값의 의미를 명확하게 표현
            - 메서드의 반환 타입을 Optional로 선언하면,
            - 이 메서드는 값이 없을 수도 있다를 명시적 표현 가능
            - 메서드 문서 따로 읽지 않아도 API 자체가 명확한 계약(Contract)를 보여줌
            ```java
            Optional<User> findUserById(String id);
            ```

        - (4) 함수형 프로그래밍 스타일 지원
            - map, flatMap, filter, orElse, orElseGet, ifPresent 같은 메서드를 통해
            - 함수형 스타일로 null safe한 데이터 흐름을 만들 수 있음
            - 복잡한 if-else 블록 대신 선언적(declarative) 코드 작성이 가능
            ```java
            String name = Optional.ofNullable(user)
                .map(User::getName)
                .orElse("Unknown");
            ```
    - Optional 사용 시 주의점
        - 필드에 Optional 사용 지양
            - 객체 필드에는 사용 안하는것이 권장, 메서드 리턴 타입에 주로 사용
        - Optional.get() 직접 호출 지양
            - 무조건 값을 꺼내는 get()은 NPE 유발 가능성
            - orElse, orElseGet, ifPresent 등 사용 권장
        - 성능 민감 영역에서 남용 주의
            - Optional은 기본 타입까지 감싸므로 성능에 민감한 부분에서는 지양 또는 주의

    - 최종 정리
        - Optional은 널 안정성을 높이고, 코드 가독성과 API 명확성을 개선하기 위해 사용하는 자바의 널 대체 솔루션


- Java에서 Thread와 Executor의 차이점
    - 기본 개념
        - 스레드
            - 스레드는 하나의 독립된 실행 흐름을 생성하는 가장 기본적인 단위
            - 자바에서는 스레드 클래스를 직접 생성하여 스레드 시작 가능
            - 개발자가 직접 start(), join() 관리
            - 스레드풀은 개발자가 직접 구현 필요
            - 자원 최적화 어려움
            - 실패 처리 등의 예외처리는 try-catch로 개발자가 직접 관리 필요
            ```java
            Thread thread = new Thread(() -> {
                System.out.println("Hello");
            });
            thread.start();
            ```
            - 각각의 스레드를 생성하고 직접 관리 필수, 쓰레드 생명주기, 동기화, 예외 처리 등을 개발자가 직접 신경써야 함
            - 1~2개의 스레드 작업에 사용
            - 다수의 동시 작업, 서버 애플리케이션, 백그라운드 작업 시에는 적합하지 않음
            - 대규모 비동기 처리, 스케쥴링, 안정성 필요한 경우에도 적합하지 않음

        - Executor
            - 스레드의 실행을 관리(Submit)하는 고수준의 추상화 API
            - 개발자가 직접 스레드 생성/관리하지 않고, Executor가 쓰레드 풀을 사용해 쓰레드 생성/스케쥴링/종료를 자동으로 관리
            - 스레드 실행 관리 및 스케쥴링 추상화
            - ExecutorService가 내부적으로 스레드 관리, 기본적으로 스레드 풀 지원
            - 스레드 풀로 자원 최적화 가능
            - 얘외 처리 구조 지원
            ```java
            ExecutorService executor = Executors.newFixedThreadPool(2);
            executor.submit(() -> {
                System.out.println("Hello");
            });
            executor.shutdown();
            ```
            - 스레드를 효율적으로 재사용하고 시스템 리소스를 최적화할 수 있다.
            - 효율적으로 확장 가능 (풀 크기 조절 가능)
            - 다수의 동시 작업, 서버 애플리케이션, 백그라운드 작업 시 적합 -> Executor (특히 ExecutorService) 사용
            - 대규모 비동기 처리, 스케쥴링, 안정성 필요한 경우에도 적합하지 않음 -> Executor 사용

    - 추가 내용 키워드
        - ExecutorService 종류 (FixedThreadPool, CachedThreadPool, SingleThreadExecutor, ScheduledThreadPool)
        - Future, Callable과 ExecutorService의 관계
        - Executors 대신 ThreadPoolExecutor 직접 사용하는 방법
        - Java 8 이후 CompletableFuture + Executor 연계 사용

    - 전체 요약
        - 스레드는 스레드를 직접 만들고 관리하는 방법
        - Executor는 스레드 실행과 관리를 효율적으로 추상화한 구조

- Handler, Thread 차이점
    - Thread
        - 스레드는 독립적인 실행 흐름(Flow)을 생성하는 가장 기본 단위
        - 무거운 작업(네트워크, 파일 I/O, 계산 등)을 메인 스레드와 분리해서 처리할 때 사용
        - 스레드는 자체적으로 실행 로직을 가지고 비동기 작업을 수행됨

    - Handler
        - Handler는 특정 쓰레드 즉, 루퍼가 있는 스레드의 메세지 큐에 작업(Runnable)이나 메시지를 보내는 도구
        - 주로 UI스레드(메인 스레드)와 통신하거나, 다른 쓰레드에서 작업 결과를 메인 쓰레드로 전달할 때 사용
        - 핸들러 자체는 별도로 작업 수행하지 않음, 작업을 특정 스레드에 전달(post)하는 역할 수행
        - 새로운 스레드 생성하지 않음 (기존 스레드에 작업 전달)
        - 핸들러는 내부적으로 루퍼와 메세지 큐를 사용
        ```java
        Handler handler = new Handler(Looper.getMainLooper());
        handler.post(() -> {
            // 메인 스레드에서 실행할 코드
        })
        ```
    - Handler와 Thread 함께 사용하는 대표 패턴
        - 보통은 스레드로 백그라운드 작업 처리하고 완료 시 핸들러로 메인쓰레드에 결과 전달하는 패턴
        - 스레드 -> 핸들러 -> UI 업데이트 패턴
            ```java
            new Thread(() -> {
                String result = downloadData();

                // Main Thread로 결과 전달
                new Handler(Looper.getMainLooper()).post(() -> {
                    updateUI(result);
                });
            }).start();
            ```

    - 정리
        - 스레드는 별도 작업을 실행하는 실행 흐름을 만듬
        - 핸들러는 특정 스레드에 작업을 예약하고 전달하는 역할

- Java에서 메모리 정리(Garbage Collection) 최적화 방법
    - Garbage Collection(GC) 개념
        - 프로그램이 더 이상 사용하지 않는 객체를 자동으로 찾아서 메모리에서 해제하는 메커니즘
        - 명시적으로 메모리를 해제하지 않고, JVM이 알아서 필요 없는 객체를 감지하고 회수
        - GC가 비효율적이거나 과도하게 발생 시 앱 성능 저하, 지연(latency), OutOfMemoryError 등이 발생할 수 있음
    - 메모리 정리(GC) 최적화 주요 방법
        - ① 객체 생명주기 관리 철저히 하기
            - 객체를 오래 참조하지 말고, 필요 없으면 참조를 끊어라 (null 할당).
            - 특히 대용량 객체(List, Map, Set)는 작업 완료 후 clear() 해주는 습관.
                - clear() -> null 초기화까지 진행
        - ② 불필요한 객체 생성 줄이기
            - 필요할 때만 객체를 생성하고, 가능한 재사용한다.
            - 예: String은 new String("...") 대신 리터럴 "..." 사용.
        - ③ 가비지 컬렉션 친화적인 자료구조 사용
            - 큰 사이즈의 HashMap, ArrayList 등은 사용 후 반드시 clear.
            - 필요한 경우 WeakReference, SoftReference 등 사용하여 GC가 회수할 수 있도록 설계.
        - ④ 메모리 누수 패턴 제거
            - 리스너(Listener), 콜백(Callback)을 등록했으면 반드시 해제(remove).
            - 내부 클래스는 static으로 선언하여 외부 클래스 암시적 참조 방지.
            - 쓰레드(Thread)나 타이머 작업 완료 후 참조 해제.
        - ⑤ String, Collection 최적화
            - 문자열 연결 시 + 대신 StringBuilder 또는 StringBuffer 사용.
            ```java
            StringBuilder sb = new StringBuilder();
            sb.append("a").append("b").append("c");
            ```
            - 큰 컬렉션 초기 용량(capacity)을 예측 가능하면 미리 지정해서 리사이징 비용 절감
                - List<String> list = new ArrayList<>(1000);
        - ⑥ 객체 풀링(Object Pooling) (주의해서)
            - 자주 생성되고 폐기되는 객체(Thread, Connection)를 풀(pool) 로 관리.
            - 단, 오히려 관리 비용이 커질 수도 있으므로 정말 필요한 경우에만 적용 (ex: DB Connection Pool).
        - ⑦ GC 튜닝 및 JVM 옵션 설정
            - JVM GC 정책을 상황에 맞게 조정할 수 있다.
            - 주요 GC 종류:
                - Serial GC (단일 쓰레드, 작은 메모리용)
                - Parallel GC (다중 쓰레드, Throughput 중시)
                - G1 GC (Balanced, 대규모 메모리용)
                - ZGC, Shenandoah (Low-latency, 초대형 시스템)
        - ⑧ 메모리/GC 모니터링 도구 활용
            - VisualVM, Java Flight Recorder(JFR), JConsole, Eclipse MAT 등을 통해
            - Heap Dump 분석, GC 로그 분석, 메모리 사용량 모니터링을 주기적으로 수행한다.

- Java에서 Functional Interface를 활용하는 방법
    - Functional Interface 개념
        - Functional Interface(함수형 인터페이스) 는
        - 오직 하나의 추상 메서드(abstract method) 만을 가지는 인터페이스를 말한다.
        - Java 8부터 도입된 람다 표현식(lambda expression) 을 사용할 수 있게 해주는 핵심 기반이다.
        - @FunctionalInterface 애노테이션을 붙이면 컴파일러가 이를 강제하고 체크해준다.
        ```java
        @FunctionalInterface
        public interface MyFunction {
            int apply(int x, int y);
        }
        ```
    - Functional Interface를 활용하는 방법
        - ① 람다 표현식과 함께 사용하기
            - 함수형 인터페이스를 구현할 때 익명 클래스 대신 간결한 람다 표현식으로 대체할 수 있다.
            ```java
            MyFunction add = (x, y) -> x + y;
            System.out.println(add.apply(2, 3));  // 출력: 5
            ```

        - ② 메서드 참조(Method Reference)로 사용하기
            - 람다 표현식 대신 메서드 참조(::) 를 활용할 수 있다.
            - 메서드 참조는 람다를 더 짧고 직관적으로 표현 가능하게 해줌
            ```java
            Function<String, Integer> parseInt = Integer::parseInt;
            System.out.println(parseInt.apply("123"));  // 출력: 123
            ```

        - ③ 표준 함수형 인터페이스 사용하기 (java.util.function 패키지)
            - Java는 다양한 표준 함수형 인터페이스를 제공한다
                - Function<T, R>: 입력을 받아 출력을 반환, 값 변환
                - Consumer<T>: 입력을 소비하고 반환 없음, 값 소비
                - Supplier<T>: 입력 없이 출력을 제공, 값 공급
                - Predicate<T>: 입력을 받아 true/false 반환, 조건 판단
                - BiFunction<T, U, R>: 두 입력을 받아 하나의 출력 반환, 두 값 변환
                ```java
                Function<String, Integer> lengthFunction = s -> s.length();
                Consumer<String> printConsumer = s -> System.out.println(s);
                Supplier<String> helloSupplier = () -> "Hello";
                Predicate<Integer> isPositive = x -> x > 0;
                ```
        
        ④ 스트림 API와 함께 사용하기
            - Java 8의 Stream API에서는 함수형 인터페이스가 필수적으로 활용된다.
            - 스트림 내에서 Predicate, Function, Consumer 등을 자연스럽게 연결해 데이터를 변환하고 처리
            ```java
            List<String> names = Arrays.asList("Tom", "Jerry", "Spike");
            names.stream()
                .filter(name -> name.startsWith("T"))   // Predicate
                .map(String::toUpperCase)               // Function
                .forEach(System.out::println);          // Consumer
            ```
    - 정리
        - Functional Interface는 자바에서 람다 표현식을 활용하고 코드 간결성, 가독성, 함수형 프로그래밍 스타일을 지원하는 핵심 도구

- Java의 JVM, JRE, JDK의 차이점
    - 개념
        - JVM(Java Virtual Machine)
            - Java 바이트코드(.class 파일)를 실행하는 가상 머신
            - Java 프로그램이 어떤 OS에서도 동작할 수 있게 해주는 핵심 역할을 담당한다.
            - 주요 기능:
                - 바이트코드 해석 및 실행
                - 메모리 관리 (Heap, Stack, Method Area 등)
                - 가비지 컬렉션 (Garbage Collection)
                - 런타임 오류 감지
                - 보안 및 플랫폼 독립성 제공
            - 요약: Java 프로그램을 실행하는 "엔진"

        - JRE(Java Runtime Environment)
            - JVM + Java 라이브러리(API) + 실행 환경 파일 세트
            - 즉, Java 애플리케이션을 실행할 수 있는 "준비된 환경"이다.
            - JRE에는 Java 개발에 필요한 도구(컴파일러)는 포함되지 않고, 오직 실행에 필요한 것만 포함된다.
            - 요약: Java 프로그램을 "실행만" 할 수 있게 해주는 환경

        - JDK(Java Development Kit)
            - JRE + 개발 도구(Compiler, Debugger, Javadoc, Keytool 등) 를 포함한 패키지
            - Java 프로그램을 작성(개발)하고, 컴파일하고, 디버깅할 수 있는 전체 도구 세트다.
            - 개발자는 JDK를 설치해서 소스코드를 작성하고 .class 파일을 만든다.
            - 요약: Java 프로그램을 "개발하고 실행할 수 있게" 해주는 도구 모음

    - 구조
        - JDK > JRE > JVM 포함 관계
        - 즉, JDK 설치 시 JRE와 JVM도 같이 포함되어 있음
        ```markdown
        JDK
        └── JRE
            └── JVM
        ```

    - 결론
        - JVM은 실행 엔진
        - JRE는 실행 환경
        - JDK는 개발과 실행을 모두 가능하게 하는 종합 개발 Kit

- Compose에서 remember와 rememberSaveable의 차이점
    - 개념
        - remember
            - 컴포저블 함수가 Recomposition될 때 데이터를 유지하도록 해주는 함수
            - 즉, 화면이 다시 그려져도 이전에 저장된 값을 그대로 유지 가능
            - 예: val count = remember { mutableStateOf(0) }
            - 액티비티가 종료되거나 프로세스가 죽거나 하면 기억한 값은 사라짐
            - 이전 값은 메모리에 저장
        - rememberSaveable
            - remember의 기능 + 추가로 프로세스 종료/액티비티 재생성 시에도 데이터 유지를 지원하는 함수
            - 내부적으로 SavedInstanceState를 이용해 데이터를 저장하고 복원
            - val count = rememberSaveable { mutableStateOf(0) }
            - 화면 전환이 발생해도 값 유지됨
            - 이전 값은 SavedInstanceState에 저장

    - 추가 주의사항
        - rememberSaveable은 Serializable 하거나, 번들에 저장 가능한 타입(Int, String, Boolean 등)만 기본으로 저장 가능
        - 복잡한 객체를 저장하려면 Saver를 커스터마이징 필수
        ```kotlin
        // MyCustomSaver -> Saver의 커스터마이징
        val customObject = rememberSaveable(stateSaver = MyCustomSaver) { mutableStateOf(MyData()) }
        ```
    - 결론
        - remember는 재구성 시 값을 유지하고, rememberSaveable은 재구성 + 화면 회전이나 프로세스 복구 시까지 값을 유지

- Jetpack Compose의 Snapshot 시스템과 상태 관리 방식
    - Snapshot 시스템
        - SnapShot은 컴포즈가 상태를 안전하고 효율적으로 관리하기 위해 사용하는 내부 메커니즘
        - 일종의 메모리상의 상태 복사본이며, 여러 상태 변경을 일관성있게 적용하고,
        - 동시에 여러 스레드가 상태를 안전하게 읽고 쓸 수 있게 만듬

    - Snapshot 필요 이유
        - Compose는 선언형 UI 패턴을 따르기 때문에, UI = 상태(State)의 함수로 간주
        - 상태가 변하면 자동으로 UI가 다시 그려져야 (리컴포지션) 한다
        - 이때,
            - 여러 상태 변경이 동시에 일어나더라도,
            - 비정합이나 충돌없이 정확하고 예측 가능한 방식으로 화면을 업데이트 해야 한다.
        - 이를 위해 Compose는 Snapshot 시스템을 도입

    - Snapshot 상태 관리 흐름
        - ① 상태 읽기 (State Read)
            - Compose 컴포저블이 remember { mutableStateOf(...) } 같은 상태를 읽으면,
            - 현재 Snapshot의 상태를 읽는다.
            - 읽은 상태에 의존하는 컴포저블은 자동으로 구독(Subscribe) 된다.

        - ② 상태 변경 (State Write)
            - 상태를 변경하면, 변경은 즉시 적용되는 게 아니라, 새로운 Snapshot에 기록(pending write) 된다.
            - 변경은 "스냅샷 버전" 이 따로 관리되어, 나중에 일괄적으로 반영된다.
            ```kotlin
            var text by remember { mutableStateOf("Hello") }
            text = "World"  // 실제로는 Snapshot이 pending write로 기록
            ```

        - ③ Snapshot Commit & Recomposition
            - 한 번의 상태 변경이 끝나면, Compose는 Snapshot을 Commit(확정) 하고,
            - 변경된 상태를 참조하는 컴포저블만 선택적으로 Recompose 한다.
                - (참고) Commit: 변경사항 확정
            - 필요한 부분만 다시 그리기(Fine-grained Recomposition)가 가능해진다.
            - 전체 화면을 다시 그리지 않고, 변경된 UI만 똑똑하게 갱신하는 것이다.

    - 추가 특성
        - Atomicity (원자성): 여러 상태 변경이 한 번에 일괄 Commit 되어 일관성 유지.
        - Isolation (격리성): 서로 다른 Snapshot끼리 독립적으로 상태를 읽고 변경 가능.
        - Concurrency Support (동시성 지원): 멀티스레드 환경에서도 Snapshot Isolation 덕분에 안전하게 상태 관리 가능.

- Compose에서 LazyColumn과 RecyclerView의 내부 동작 차이점
    - 기본 개념
        - RecyclerView (Android View System)
            - 기존 뷰 시스템에서 리스트를 효율적으로 표시하는 컨포넌트
            - 뷰 객체를 재사용하여, 수천 개의 아이템을 메모리 낭비 없이 렌더링할 수 있음
            - 직접 Adapter, ViewHolder, LayoutManager 등을 구현해서 리스트 구성
            ```kotlin
            recyclerView.adapter = MyAdapter()
            recyclerView.layoutManager = LinearLayoutManager(context)
            ```

        - LazyColumn (Jetpack Compose)
            - Jetpack Compose의 선언형 UI 방식에서 리스트를 효율적으로 렌더링하는 컴포저블
            - 이름처럼 필요할 때만 아이템을 컴포즈
            - 별도의 아답터, 뷰홀더 구현 없이 컴포저블 함수를 통해 직접 UI 구성
            ```kotlin
            LazyColumn {
                items(list) { item ->
                    Text(text = item.name)
                }
            }
            ```
    - 내부 구조
        - 렌더링 방식
            - 미리 뷰객체를 생성하고 재사용 (뷰홀더 패턴) -> RecyclerView
            - 필요한 순간에만 컴포저블을 호출하여 렌더링 -> LazyColumn
        - 메모리 관리
            - 뷰 풀을 유지하고 뷰 객체를 계속 재사용 -> RecyclerView
            - 메모리에 불필요한 컴포저블을 남기지 않고 필요할 때만 다시 컴포즈 -> LazyColumnn


- Jetpack Compose의 상태 관리에서 State Hoisting 패턴을 활용하는 방법
    - State Hoisting 개념
        - Composable 내부에서 직접 상태를 가지지 않고, 상태를 외부로 끌어올려 관리하는 패턴
        - 상태를 컴포저블이 직접 들고 있지 않고, 상위 컴포저블이 소유하고,
        - 하위 컴포저블은 상태를 받아서(display) + 수정 요청(callback)만 함

    - 사용 이유
        - 단방향 데이터 흐름: 데이터가 한 방향으로만 흐르게 해서 코드가 명확해짐 (상위 -> 하위)
        - 재사용성 증가: 컴포저블을 다양한 상태에 대해 재사용할 수 있음
        - 테스트 용이성: 하위 컴포저블이 순수하게 입력만 받아 렌더링하므로 테스트하기 쉬움
        - 코드 구조 명확화: 상태 소유와 UI 역할을 분리

    - 상태 호이스팅 기본 패턴
        - 직접 상태를 가지는 나쁜 예
            ```kotlin
            @Composable
            fun Counter() {
                var count by remember { mutableStateOf(0) }

                Button(onClick = { count++ }) {
                    Text(text = "Clicked $count times")
                }
            }
            ```
            - Counter() 컴포저블이 상태를 직접 들고 있음 -> 재사용성, 확장성 감소

        - 상태 호이스팅 적용한 예
            - 외부(CounterScreen)에서 상태를 전달받고 수정 요청만 한다.
            - 상위가 상태를 소유하고, 하위는 UI와 액션만 담당
            ```kotlin
            // 하위 컴포저블
            @Composable
            fun Counter(
                count: Int,
                onIncrement: () -> Unit
            ) {
                Button(onClick = onIncrement) {
                    Text(text = "Clicked $count times")
                }
            }

            // 상위 컴포저블
            @Composable
            fun CounterScreen() {
                var count by rememberSaveable { mutableStateOf(0) }

                Counter(
                    count = count,
                    onIncrement = { count++ }
                )
            }
            ```
    - 상태 호이스팅 구조가
        - State Owner(상위): 상태를 소유하고 관리 (remember, rememberSaveable)
        - Stateless Composable(하위): 상태를 전달받아 화면에 그리기만 함
        - Event Callback: 하위 컴포저블에서 사용자 액션 발생 시 상위에 통지

    - 정리
        - 항상 상위에서 상태를 가지고, 하위로 전달
        - 하위 컴포저블은 입력만 받고 출력만 발생
        - 이 패턴 규칙 유지 시 컴포즈의 선언형 UI 구조와 완벽하게 일치하게 됨
        - 상태 호이스팅은 상태를 컴포저블 외부로 끌어올려 단방향 데이터 흐름을 만들고, 재사용성과 테스트성을 높이는 컴포즈 상태 관리 패턴

- Compose에서 derivedStateOf와 remember를 활용한 성능 최적화 방법
    - 개념
        - remember
            - 컴포저블이 재구성될 때마다 값을 다시 계산하지 않고, 이전 값을 기억(캐시)해주는 역할
            - 주로 무거운 계산이나 객체 생성 비용이 큰 경우, 불필요한 연산을 방지하지 위해 사용

        - derivedStateOf
            - 다른 상태에 의존해 계산된 값을 관리할 때 사용
            - 의존하는 상태가 변경될 때만 다시 계산하고 그렇지 않으면 이전 결과를 재사용
            - 비용이 큰 계산을 의존성 변화가 있을 때만 수행하도록 최적화 가능
            ```kotlin
            val isButtonEnabled = derivedStateOf { text.isNotBlank() }
            ```
            - text가 변할 때만 isButtonEnabled를 다시 계산

    - 성능 최적화 중요 이유
        - 무조건 재계산 문제 (상태 변경될 때마다 복잡한 계산이 다시 수행되면 성능 저하 발생)
        - 불필요한 리컴포지션 (의존 상태 변하지 않아도 컴포저블이 재구성 시 매번 다시 계산되는 문제)
        - derivedStateOf + remember (필요할 때만 계산하고, 캐싱을 통해 비용을 절약)

    - 최적화 방법
        - 기본 패턴
            ```kotlin
            val expensiveValue by remember(input) {
                derivedStateOf {
                    // input에 따라 비싼 계산
                    heavyComputation(input)
                }
            }
            ```
            - input이 변경될 때만 heavyComputation이 실행
            - 컴포저블 재구성만으로는 다시 계산되지 않음

        - 검색 필터 최적화
            ```kotlin
            @Composable
            fun SearchScreen(query: String, allItems: List<String>) {
                val filteredItems by remember(query, allItems) {
                    derivedStateOf {
                        allItems.filter { it.contains(query, ignoreCase = true) }
                    }
                }

                LazyColumn {
                    items(filteredItems) { item ->
                        Text(item)
                    }
                }
            }
            ```
            - query나 allItems가 변경될 때만 필터링 작업을 수행
            - 스크롤이나 화면 리컴포지션과 무관하게, 필터 연산은 최소한만 수행됨

    - 결론
        - remember 는 값 자체를 캐시하고, derivedStateOf는 의존 상태 변화가 있을 때만 계산을 다시 해서 컴포즈 성능을 최적화함


- Jetpack Compose에서 State와 Event를 분리하는 이유
    - State와 Event의 개념 명확화
        - State(상태):
            - UI를 그리는 데 필요한 데이터.
            - 화면이 어떤 모습이어야 하는지를 결정한다.
            - (예) 텍스트 필드의 입력 값, 버튼의 활성화 여부 등

        - Event(이벤트):
            - 사용자의 액션이나 시스템에 의해 발생하는 동작.
            - 화면을 변경하거나 특정 처리를 트리거(trigger)한다.
            - (예) 버튼 클릭, 스크롤 이벤트, 입력 완료 이벤트 등
        - 정리
            - → State는 "현재 상태를 나타내는 값",
            - → Event는 "변화를 유발하는 행동" 으로 역할이 다르다.

    - 책임 분리 (Separation of Concerns)
        - 각각의 책임을 명확히 구분하면, 코드가 더 이해하기 쉬워진다.
        - State는 "어떤 데이터가 있는지"만 신경 쓰고,
        - Event는 "어떤 일이 일어나는지"에만 집중한다.
        - 서로 다른 변화의 주체(State 업데이트 vs Event 처리)를 혼동하지 않게 된다.
        - 이를 통해 코드의 가독성(Readability) 과 유지보수성(Maintainability) 이 크게 향상된다.

    - 단방향 데이터 흐름 (Unidirectional Data Flow, UDF) 보장
        - Compose는 단방향 데이터 흐름을 핵심으로 한다.
        - State → UI → Event → State 업데이트 로 흐름이 돌아가야 한다.
        - State와 Event를 명확히 나누지 않으면, 흐름이 꼬이고, 사이드 이펙트(side-effect)가 발생할 위험이 높아진다.
        - State를 변경하는 건 항상 Event를 통해 이루어져야 하며, UI는 오직 State만 보고 그려져야 한다.
        - → 이 흐름이 깨지면 버그를 추적하기 어렵고, 동시성 문제(concurrency issues)도 생길 수 있다.

    - 테스트 용이성(Testability) 향상
        - Event 핸들링을 별도로 분리하면, UI를 직접 띄우지 않고도 이벤트 처리를 단위 테스트할 수 있다.
        - State 변화도 독립적으로 검증할 수 있다.
        - ViewModel 레벨에서는 "이벤트를 받으면 어떤 상태 변화를 일으키는가?"를 명확히 테스트할 수 있게 된다.
        - 테스트 가능한 구조는 장기적으로 프로젝트 품질에 매우 중요한 영향을 준다.

    - UI 재사용성과 유연성 향상
        - 동일한 State를 가진 다양한 화면을 만들 수 있다.
        - 동일한 Event를 다른 방식으로 처리할 수 있다 (예: 다른 화면에서는 같은 버튼 클릭을 다르게 처리).
        - State와 Event를 분리하지 않으면, UI가 로직과 강하게 결합되어 재사용이 어려워진다.
        - ViewModel과 Composable이 느슨하게 연결(loose coupling)되어, 하나를 변경해도 다른 부분에 영향을 최소화할 수 있다.

    - 코드 복잡도 관리
        - 기능이 커질수록 State와 Event를 섞어놓으면 코드가 복잡해지고 유지보수가 어려워진다.
        - 특히 비즈니스 로직이 많은 앱에서는 이벤트별 처리 로직(Event Handler)이 늘어나는데, 이를 깔끔히 관리하려면 분리가 필수적이다.
        - 각각을 모듈화하거나 다른 클래스로 옮기는 것도 쉬워진다.

    - 예제
        - State와 Event 미 분리 케이스
            ```kotlin
            @Composable
            fun CounterScreen() {
                var count by remember { mutableStateOf(0) }

                Column(
                    horizontalAlignment = Alignment.CenterHorizontally,
                    verticalArrangement = Arrangement.Center
                ) {
                    Text(text = "Count: $count", fontSize = 24.sp)

                    Button(
                        onClick = {
                            // Event 로직과 State 업데이트가 뷰 안에 다 섞여있음
                            count++
                        }
                    ) {
                        Text("Increment")
                    }

                    Button(
                        onClick = {
                            count = 0 // Reset 이벤트도 뷰 안에 섞여있음
                        }
                    ) {
                        Text("Reset")
                    }
                }
            }
            ```
            - 문제점
                - 상태와 이벤트 처리 모두 하나의 Composable 안에 존재
                - 화면 복잡할 시 관리 어려움
                - 테스트 어려우며 다른 화면에서 동일 로직 재사용 어려움
                - UI에 로직이 섞여 있어서 가독성과 유지보수성이 나빠짐
        - 분리 케이스
            ```kotlin
            // 뷰모델
            class CounterViewModel : ViewModel() {
                private val _count = mutableStateOf(0)
                val count: State<Int> = _count

                fun onIncrement() {
                    _count.value++
                }

                fun onReset() {
                    _count.value = 0
                }
            }
            // 컴포저블 함수
            @Composable
            fun CounterScreen(viewModel: CounterViewModel = viewModel()) {
                val count by viewModel.count

                Column(
                    horizontalAlignment = Alignment.CenterHorizontally,
                    verticalArrangement = Arrangement.Center
                ) {
                    Text(text = "Count: $count", fontSize = 24.sp)

                    Button(
                        onClick = {
                            viewModel.onIncrement() // Event 발생만 위임
                        }
                    ) {
                        Text("Increment")
                    }

                    Button(
                        onClick = {
                            viewModel.onReset() // Event 발생만 위임
                        }
                    ) {
                        Text("Reset")
                    }
                }
            }
            ```
            - 장점
                - CounterScreen은 State(count) 구독하고 표시만 함
                - 이벤트 처리는 뷰모델이 담당
                - State 변경은 항상 이벤트를 통해서만 이루어짐
                - 테스트 용이 (뷰모델만 단위테스트 실시하면 됨)
                - 유지보수성이 높고, 확장하기 쉽다
    - 요약
        - Jetpack Compose에서 State와 Event를 분리하는 이유는
            - 책임 분리로 코드 가독성과 유지보수성을 높이고,
            - 단방향 데이터 흐름을 확실히 지키며,
            - 테스트 용이성을 확보하고,
            - UI 재사용성과 유연성을 높이고,
            - 코드 복잡도를 체계적으로 관리하기 위함이다.
        - State는 '어떻게 보일까'를 담당하고, Event는 '무슨 일이 일어날까'를 담당한다.
        - 이 둘을 명확히 나누는 것이 Compose 아키텍처의 핵심 원칙이다.


- Jetpack Compose에서 key()를 사용하여 Recomposition을 최적화하는 방법
    - key() 함수 개념
        - Compose에서 특정 Composable 블록에 고유 식별자(Identity)를 부여하는 함수
        - 이 식별자를 기반으로, Compose가 Recomposition(재구성) 시 "어떤 Composable을 유지할지, 다시 만들어야 할지" 를 판단하는 기준을 제공한다.
        - 기본적으로 Compose는 컴포저블의 위치(Position)를 기준으로 구분하지만, 복잡한 리스트나 조건부 UI에서는 위치만으로는 정확히 판단할 수 없다.
        - key()를 사용하면 개발자가 "이 블록은 이 ID를 가진다" 고 명시해주기 때문에, Compose가 더 똑똑하게 재구성을 최적화할 수 있다.
            - 즉 원래 기본은 위치로 구분하나 복잡한 UI의 경우 정확한 판단 어려우므로 개발자가 명시적으로 ID 즉, key를 지정해줘야 성능에 좋다
    
    - key()를 사용해야 하는 상황
        - 리스트(List)나 반복문 안에서 항목별로 고유한 구분이 필요할 때
        - 조건부 분기(If/Else) 로 뷰가 동적으로 바뀌는 경우
        - 항목 추가/삭제/순서 변경이 있을 때
        - 복잡한 Composable에서 위치 기반 추론만으로 식별이 모호해질 때
            - → 즉, "항상 같은 자리에 같은 내용이 있다는 보장이 없을 때" key()를 써야 한다.

    - key() 사용법
        - 기본 사용 예
            ```kotlin
            LazyColumn {
                // items 함수 내 key 필드 셋팅
                items(userList, key = { it.id }) { user ->
                    UserItem(user)
                }
            }
            ```
            - key = {it.id}를 명시하면, 각 UserItem은 id를 기준으로 식별
            - 사용자가 스크롤하거나, 리스트가 추가/삭제될 때 불필요한 Recomposition을 방지하고, 필요한 부분만 깔끔하게 업데이트
        
        - 명시적으로 key() 감싸기
            ```kotlin
            Column {
                userList.forEach { user ->
                    key(user.id) { // 직접 감싸기
                        UserItem(user)
                    }
                }
            }
            ```
            - forEach 같은 단순 반복문에서는 key()로 직접 감싸야 함
            - 감싼 이후 user.id가 같은 항목은 컴포즈 노드를 재활용하고, id가 바뀐 항목만 다시 그린다.

    - key()를 사용하지 않으면 생기는 문제
        - 항목의 위치가 바뀌거나 추가/삭제될 때, Compose가 잘못된 항목을 재활용할 수 있다.
        - 의도치 않은 UI 깜빡임, 리셋, 잘못된 State 매칭 문제가 발생할 수 있다.
        - 리스트의 한 항목만 수정했는데도 전체가 불필요하게 Recomposition될 수 있다.
        - 퍼포먼스 저하 및 사용자 경험 악화로 이어진다.

    - key()를 제대로 사용했을 때 얻는 효과
        - Recomposition 범위 최소화: 변경된 항목만 다시 그린다.
        - State 보존: 항목 간 이동이 발생해도 내부 상태(예: 입력값)가 유지된다.
        - 퍼포먼스 최적화: 리스트나 복잡한 UI 구조에서도 빠르고 부드러운 동작을 보장한다.
        - 코드 안정성 향상: 예측 가능한 동작과 디버깅 용이성 증가.

    - 결론
        - key()는 Compose가 Composable을 정확하게 추적하고 최소한으로 Recomposition할 수 있도록 명확한 식별자를 제공하는 도구
        - 리스트나 동적 UI에서 key()를 적절히 사용하면 성능과 안정성이 크게 향상
        - 항상 같은 자리에 같은 내용을 보장할 수 없을 때는 key()로 식별자를 명확히 제공해야 함

- Compose에서 UI 요소가 계속해서 Recomposition되는 문제를 해결하는 방법
    - 문제의 원인
        - 상태 값이 변경되거나 컴포저블 함수가 입력 파라미터(인자)를 통해 변경되었을 때
        - 불필요한 상태 변경
        - 불안정한 파라미터를 컴포저블 함수에 전달 (매번 새로운 객체 전달)
        - remember 등을 사용하지 않고 매번 연산
        - 외부 객체가 무분별하게 변할 때
        - 핵심: 컴포즈는 입력값이 변했다고 인식하면 무조건 다시 그린다.

    - 대표적 해결 방법
        - remember 사용한 메모이제이션
            - 컴포저블 내부에서 고정된 계산 결과나 객체를 매번 새로 만들지 않고, remember를 이용해 값을 저장하고 필요할 때만 재생성
            ```kotlin
            @Composable
            fun Example() {
                val user = remember { User("Aiden") }
                // 매 리컴포지션 때마다 새로운 User 객체를 만들지 않는다
                // remember로 고정 가능한 값이나 객체는 항상 캐싱해서 리컴포지션 방지
            }
            ```
        - rememberSaveable로 상태 저장하고 복구
            - 사용자가 화면을 회전하거나 프로세스가 죽었다 살아나도,
            - State를 잃지 않고 복구할 수 있게 rememberSaveable 사용
            ```kotlin
            @Composable
            fun Example() {
                // 사용자의 입력 등을 화면 변화에도 안정적으로 유지
                var name by rememberSaveable { mutableStateOf("") }
            }
            ```
        - 상태 객체를 세밀하게 분리하고 필요한 부분만 관찰
            - 하나의 큰 State 객체를 여러 컴포저블이 참조하면, 작은 변경에도 전체가 다시 그려진다.
            - 필요한 부분만 따로 분리하거나 derivedStateOf를 이용해 최소한만 감시한다.
            ```kotlin
            // 관찰 범위를 좁혀서 불필요한 리컴포지션 방지
            val isButtonEnabled by remember {
                derivedStateOf { name.isNotEmpty() }
            }
            ```
        - Stable한 객체 전달
            - 컴포저블에 매번 새로운 객체나 람다를 넘기면 컴포즈는 변경됐다고 인식
            - 항상 안정적인 값을 넘겨야 함
            - 리스트나 데이터 클래스는 변경되지 않는 한 그대로 전달해야 함
            - @Immutable / @Stable을 활용해 컴파일러에게 이 객체는 바뀌지 않음을 명시
            ```kotlin
            @Immutable
            data class User(val name: String)

            @Composable
            fun UserProfile(user: User) { ... }
            ```
        - key()를 적절히 사용해 리컴포지션 범위 제어
            - 리스트나 반복문 내에서는 key()를 설정하여 개별 항목을 정확히 식별하게 한다.
            - 데이터 변경에도 필요한 항목만 다시 그리도록 최적화
            ```kotlin
            LazyColumn {
                items(userList, key = { it.id }) { user ->
                    UserItem(user)
                }
            }
            ```
        - Modifier 순서, 중복 호출 주의
            - Modifier를 매번 새로 생성하거나, Modifier 체이닝 순서가 엉키면 Recomposition이 많아질 수 있음
            - Modifier는 불변성을 유지하고, 불필요한 호출을 최소화

        - SideEffect, LaunchedEffect 활용
            - Compose는 LaunchedEffect, SideEffect, DisposableEffect 등을 제공해서 컴포즈 생명주기에 따라 부수효과(side-effect)를 관리하게 한다.
            - 이걸 사용하지 않고 그냥 Composable 안에 로직을 적어버리면 Recomposition 때마다 다시 실행된다.
            ```kotlin
            // 필요할 때 한번만 동작하도록 제어
            LaunchedEffect(key1 = userId) {
                viewModel.loadUser(userId)
            }
            ```

    - 문제 해결 재정리
        - 불필요한 State 변경 제거
        - remember / rememberSaveable을 적극 활용
        - derivedStateOf로 필요한 부분만 감시
        - 항상 Stable 객체를 전달
        - key()로 리스트 항목 식별을 정확히 설정
        - Modifier 호출과 체이닝을 순서
        - SideEffect 계열 API로 부수효과를 관리

    - 의견
        - Compose에서 UI 요소가 불필요하게 Recomposition된다면, 원인은 거의 항상 State 관리 문제 또는 입력 안정성 문제
        - 이를 구조적으로 해결 필요

- Jetpack Compose의 CompositionLocal 개념과 사용 시점
    - CompositionLocal 개념
        - CompositionLocal은 컴포지션 트리(Composable 계층 구조) 안에서 데이터를 암묵적으로 공유할 수 있게 하는 메커니즘
        - 일반적인 파라미터 전달(Composable 함수 → Composable 함수) 방식 대신, 중간 계층을 거치지 않고 필요한 곳에서 직접 값을 가져올 수 있다.
        - 대표적으로 테마(Theme), 폰트 크기, 언어, 다크 모드 설정 등 "전역적이지만 상황에 따라 바뀔 수 있는 값" 을 공유할 때 사용한다.
            - → 즉, "전역(Global)처럼 보이지만, 컴포지션 트리(Local)에 따라 변할 수 있는 데이터" 를 다룬다.

    - CompositionLocal 동작 방식
        - CompositionLocalProvider를 통해 특정 Local 값을 컴포지션 트리의 하위로 주입(Inject)한다.
        - 하위 Composable은 CompositionLocal.current를 통해 주입된 값을 참조한다.
        - 트리 상위에 다른 Provider가 있으면 그 값을 따르고, 없으면 기본(Default) 값을 사용한다.
        - 흐름:
            - Provider에 값 설정 → 하위 컴포저블이 current로 읽기

    - CompositionLocal 사용 방법
        - (1) CompositionLocal 정의
            ```kotlin
            val LocalUserName = compositionLocalOf<String> { error("No username provided") }
            ```
            - 기본값 설정 (혹은 예외 던지기)

        - (2) 값 제공하기 (Provider)
            ```kotlin
            CompositionLocalProvider(LocalUserName provides "Aiden") {
                MyScreen()
            }
            ```
            - MyScreen()과 그 하위는 LocalUserName을 사용할 수 있다.

        - (3) 값 읽기
            ```kotlin
            @Composable
            fun MyScreen() {
                val userName = LocalUserName.current
                Text(text = "Hello, $userName")
            }
            ```
            - LocalUserName.current를 통해 현재 컨텍스트(Context)의 값을 읽는다.

    - CompositionLocal의 특징
        - 상위 Provider가 바뀌면 하위 모든 관련 Composable이 Recomposition된다.
        - Scope(Local)이기 때문에, 다른 트리에서는 다른 값을 가질 수 있다.
        - Nullable 값 관리를 조심해야 한다 (초기값을 적절히 설정하거나 null 처리 필요).

    - CompositionLocal 사용 시점
        - (1) 테마(Theme) 관리
            - 색상, 폰트 스타일, 크기 등 테마 관련 데이터를 전역으로 주입할 때.
            - 예: MaterialTheme은 내부적으로 CompositionLocal을 이용해 색상 팔레트, 타입 세트 등을 제공한다.
            ```kotlin
            val colors = lightColors()
            MaterialTheme(colors = colors) {
                // 여기서 colors를 암묵적으로 사용할 수 있다.
            }
            ```

        - (2) 앱 설정(App Settings) 공유
            - 다크 모드 여부, 언어(Locale) 설정, 접근성 설정 등을 전역으로 공유할 때.

        - (3) 컨텍스트성 데이터(Context-like Data) 전달
            - 로그인한 사용자 정보
            - 지역화된 리소스
            - 공통적으로 필요한 네트워크 상태, 기기 정보 등
                - → 공통적으로 필요한 값이지만, 모든 Composable에 직접 파라미터로 넘기기 싫을 때

        - (4) 뷰모델 또는 스코프 객체 전달
            - 화면 단위로 Scope를 분리할 때
            - 특정 컴포저블 하위 트리에서만 사용해야 하는 컨텍스트 데이터를 넘길 때

        - (5) 커스텀 디자인 시스템 구축
            - 프로젝트에서 자체 Theme 시스템이나 UI 컴포넌트 스타일링을 관리할 때
            - 버튼, 카드, 다이얼로그 등의 스타일을 글로벌하게 주입하고 싶을 때

    - 결론 요약
        - CompositionLocal은 Compose 트리 내부에서 값을 전역처럼 암묵적으로 공유하는 방법
        - 주로 테마, 앱 설정, 공통 데이터 관리에 사용되며, 컴포저블 간 데이터 전달을 단순화하고 유지보수를 쉽게 만듬
        - 명시적 전달이 번거롭고, 글로벌하되 트리별로 다를 수 있는 값은 CompositionLocal로 관리 권장

- Jetpack Compose에서 custom Modifier를 활용한 성능 최적화 방법
    - Custom Modifier 개념
        - Modifier는 Compose에서 UI 요소(Composable)에 레이아웃, 그리기, 동작(Interaction) 을 추가하는 일종의 "데코레이터" 역할
        - 기본 제공 Modifier(예: padding, background, clickable) 외에도, 필요에 따라 Custom Modifier를 직접 만들어서 복잡한 기능을 하나의 Modifier로 캡슐화할 수 있다.
        - 특히, 자주 사용되는 조합이나 반복되는 패턴을 커스텀 Modifier로 묶으면, 코드 재사용성 뿐만 아니라 성능 최적화도 가능

    - Custom Modifier를 통한 성능 최적화 핵심 전략
        - (1) Modifier 조합 최소화
            - 여러 Modifier를 체이닝(.으로 연결)하면 각각 별도의 노드를 추가하고 연산한다.
            - Custom Modifier로 여러 기능을 하나로 묶으면, Compose 트리의 노드(Node) 수를 줄여 렌더링과 측정(Measure) 단계를 최적화할 수 있다.
            - 별도 체이닝 없이 modifer.shadowAndBackground() 한 번에 적용
            ```kotlin
            fun Modifier.shadowAndBackground(): Modifier = 
                this
                    .shadow(8.dp, RoundedCornerShape(4.dp))
                    .background(Color.White, RoundedCornerShape(4.dp))
            ```

        - (2) layout Modifier 직접 구현
            - 단순히 padding, offset 같은 조작만 필요한 경우, Compose가 제공하는 기본 layout modifier를 조합하지 않고 직접 layout 함수를 구현하면, Measure, Layout, Draw 과정을 줄여 성능을 최적화 가능
            - 직접 필요한 연산만 수행해서 오버헤드를 줄임
            ```kotlin
            fun Modifier.customOffset(x: Dp, y: Dp): Modifier = layout { measurable, constraints ->
                val placeable = measurable.measure(constraints)
                layout(placeable.width, placeable.height) {
                    placeable.placeRelative(x.roundToPx(), y.roundToPx())
                }
            }
            ```

        - (3) drawBehind / drawWithContent 최적 활용
            - 배경을 그리기 위해 불필요한 Box 래핑을 만들지 않고, Modifier에서 바로 drawBehind, drawWithContent를 사용하면 Compose 트리 깊이를 줄이고 성능을 높일 수 있다.
            - 추가 레이아웃을 만들지 않고 바로 그리기(렌더링)
            ```kotlin
            fun Modifier.customUnderline(color: Color, thickness: Dp): Modifier =
            this.drawBehind {
                val y = size.height - thickness.toPx() / 2
                drawLine(
                    color = color,
                    start = Offset(0f, y),
                    end = Offset(size.width, y),
                    strokeWidth = thickness.toPx()
                )
            }
            ```

        - (4) Modifier에 Stable 타입 사용
            - Custom Modifier 내부에서 인자로 받는 값들은 @Stable, @Immutable 등을 붙여 불필요한 Recomposition을 막는다.
            - Modifier 파라미터가 변경되지 않는 한 다시 그리지 않도록 한다

        - (5) Modifier 순서 신경쓰기
            - Modifier의 적용 순서에 따라 Layout → Draw → Interaction이 결정된다.
            - 성능 최적화를 위해서는 layout 관련 Modifier를 먼저, draw 관련 Modifier를 나중에 붙여야 한다.
            - 잘못된 순서로 Modifier를 적용하면 불필요한 layout pass나 draw pass가 추가될 수 있다.
            - layout -> draw -> interaction 순서 권장
            ```kotlin
            modifier
                .padding(8.dp)          // Layout
                .background(Color.Red)  // Draw
                .clickable { }          // Interaction
            ```

    - Custom Modifier 사용 시 주의사항
        - 너무 많은 기능을 하나의 Custom Modifier에 넣지 않는다.
            - → 관리가 어려워지고 디버깅이 힘들어진다.
        - 진짜 성능 병목이 있는 부분에만 직접 layout이나 drawBehind를 구현한다.
            - → 과도한 최적화는 오히려 복잡성만 높인다.
        - Modifier를 만들어 쓸 때는 Stable, Immutable 데이터를 우선적으로 고려한다.

- 액티비티가 다른 액티비티에 의해 가려질 때 호출되는 메서드
    - 호출되는 메서드
        - onPause()
            - 현재 액티비티는 화면에 보이지 않거나 일부만 보이는 상태로 전환된다.
            - "다른 액티비티가 앞으로 나타날 때" 가장 먼저 호출된다.
            - CPU 리소스를 덜 소모하도록 처리하거나, 애니메이션/센서 업데이트를 멈추는 등의 작업을 수행하는 곳이다.

        - 주의할 점
            - 이때는 아직 완전히 소멸(onStop())한 것이 아니다.
            - 반투명 액티비티(예: 다이얼로그 테마 Activity)가 뜨는 경우에도 onPause()만 호출되고 onStop()은 호출되지 않을 수 있다.

- 앱이 완전히 종료될 때 호출되는 생명주기 메서드
    - 호출되는 생명주기 메서드
        - onDestroy()
            - 액티비티가 완전히 종료될 때 호출된다.
            - 사용자가 "뒤로 가기"를 눌러 종료하거나, 시스템이 메모리 회수 등을 위해 액티비티를 제거할 때 호출된다.
    - 앱 전체 종료 관점에서는
        - 안드로이드 시스템에는 "앱 종료"라는 개념이 명확하지 않다. 
        - 모든 액티비티가 소멸되어야 사실상 앱이 종료된 것으로 간주한다.
        - 각각의 액티비티들은 소멸될 때 개별적으로 onDestroy()가 호출된다.
    - 주의할 점
        - 강제 종료(killProcess 등)나 비정상 종료(OOM 등) 상황에서는 onDestroy()가 호출되지 않을 수 있다.
        - 따라서 onDestroy에 중요한 저장작업만 의존하는 것은 위험하다. 필요한 경우 onPause()나 onStop() 단계에서도 데이터를 저장하는 것이 안전하다.

- onSaveInstanceState()와 onRestoreInstanceState()의 차이
    - onSaveInstanceState()
        - 호출 시점
            - 액티비티나 프래그먼트가 일시적으로 소멸될 가능성이 있을 때 (ex: 화면 회전, 백그라운드 이동 후 시스템에 의해 종료될 때) 호출된다.
            - onSaveInstanceState() -> onPause() -> onStop()
        - 작업 내용
            - 현재 UI 상태나 임시 데이터를 Bundle 객체에 저장한다.
            - 사용자가 보고 있던 상태를 보존하기 위한 목적.
        - 특징
            - 반드시 호출되지는 않는다. 시스템이 결정한다.
            - 매우 빠르게 실행되어야 한다. 무거운 작업 금지.

    - onRestoreInstanceState()
        - 호출 시점
            - 액티비티가 onStart() 직후,
            - 프래그먼트가 onViewStateRestored()나 onActivityCreated() 직후에 호출된다.
            - onCreate()에서도 Bundle이 전달되지만, onRestoreInstanceState()는 onStart 이후 UI가 모두 준비된 상태에서 추가로 복원할 수 있게 도와준다.
        - 작업 내용
            - onSaveInstanceState()에 저장했던 데이터로 UI 상태를 복원한다.
            - 주로 View나 입력값 등 사용자 인터랙션 관련 데이터를 복원.
        - 특징
            - onCreate() 때 복원할 수도 있지만, UI가 다 만들어진 이후 복원할 작업이 있다면 여기서 처리하는 게 좋다.

- 프래그먼트에서 onAttach()와 onCreateView() 호출 시점
    - onAttach()
        - 호출 시점
            - 프래그먼트가 호스트 액티비티에 처음 연결될 때 호출된다.
            - Fragment 객체가 Context (Activity) 와 연결되는 최초 시점.
        - 작업 내용
            - Context를 활용해야 하는 초기 설정을 수행할 수 있다.
            - 예를 들어, 액티비티에 대한 참조를 저장하거나 콜백 인터페이스를 연결할 수 있다.
        - 특징
            - 아직 View는 존재하지 않는다. (UI 생성 전 단계)

    - onCreateView()
        - 호출 시점
            - 프래그먼트의 UI를 처음 생성할 때 호출된다.
            - onAttach()와 onCreate()가 끝난 후 호출된다.
        - 작업 내용
            - XML 레이아웃을 inflate 해서 화면에 보여질 View를 반환한다.
            - 프래그먼트의 실질적인 UI 구성을 담당하는 메서드.
        - 특징
            - 이 메서드에서 직접 findViewById() 등을 통해 View를 다룰 수 있다.

    - 간단 요약 흐름
        - onAttach() — "호스트 액티비티에 연결됨 (Context 연결)"
        - onCreate() — "초기 데이터 준비"
        - onCreateView() — "UI(View) 생성"

- RecyclerView와 ListView의 핵심 차이
    - RecyclerView
        - 유연성과 확장성이 뛰어남.
        - ViewHolder 패턴을 강제하여 스크롤 성능을 최적화.
        - 다양한 레이아웃 지원 (LinearLayoutManager, GridLayoutManager,StaggeredGridLayoutManager 등).
        - 아이템 추가/삭제/갱신을 효율적으로 처리 (notifyItemInserted, notifyItemRemoved 등 세밀한 제어 가능).
        - ItemAnimator, ItemDecoration 등 커스터마이징이 용이.
        - RecyclerView.Adapter를 반드시 직접 구현해야 함.

    - ListView
        - 사용이 간단하지만 확장성과 유연성이 떨어짐.
        - ViewHolder 패턴을 권장사항으로만 제공 (강제 아님 → 퍼포먼스 저하 가능성).
        - 기본적으로 수직 스크롤만 지원.
        - 아이템 변경 시 전체 갱신 (notifyDataSetChanged만 있음 → 성능 저하 우려).
        - 꾸미기나 애니메이션 추가가 번거롭고 제한적.

    - 결론
        - 새로운 앱 개발에서는 RecyclerView가 사실상 표준이다.
        - ListView는 과거의 단순 리스트 표시 용도로 사용되었으나, 현재는 권장되지 않는다.

- Jetpack Compose에서 rememberSaveable과 remember의 차이
    - remember
        - 컴포저블이 재구성(recomposition)될 때만 유지되는 상태를 저장한다.
        - 앱이 프로세스 종료(예: 백그라운드 이동 중 강제 종료)되거나, 화면 회전(구성 변경, Configuration Change)이 발생하면 값이 사라진다.
        - 매우 빠르지만, 수명(lifecycle)이 짧다.

    - rememberSaveable
        - remember + 저장(Bundle 기반) 기능을 함께 가진다.
        - 프로세스 종료나 화면 회전(구성 변경) 시에도 값을 자동으로 복구한다.
        - 내부적으로 SavedStateHandle처럼 동작하며, 저장 가능한 타입(Primitive, Serializable, Parcelable 등)만 가능하다.
        - 추가로 custom Saver를 구현하면 복잡한 객체도 저장할 수 있다.

    - 간단 요약
        - remember: 단순 재구성 유지용, 일시적 상태 저장.
        - rememberSaveable: 구성 변경(회전 등)과 프로세스 종료에도 복구 가능한 영구적 상태 저장.

- ConstraintLayout을 사용하는 주요 이점
    - 유연한 UI 구성
        - 복잡한 레이아웃을 한 번에 하나의 레이아웃 트리로 작성할 수 있다.
        - 중첩된 LinearLayout, RelativeLayout 없이도 다양한 위치 배치가 가능하다.

    - 퍼포먼스 최적화
        - 레이아웃 트리가 얕아져서 계층 구조가 단순화된다.
        - 중첩 레이아웃을 줄이면 Measure → Layout → Draw 과정이 빨라진다.

    - 직관적이고 강력한 제약 시스템
        - View들 간에 관계(Constraint) 로 배치하므로 복잡한 정렬과 비율 조정이 쉬워진다.
        - Guideline, Barrier, Group 등을 활용하여 유동적인 레이아웃 구성이 가능하다.

    - 디자이너 친화적
        - Android Studio의 ConstraintLayout Editor(시각적 에디터)를 통해 드래그 앤 드랍으로 직관적으로 UI를 설계할 수 있다.

    - 기타 장점
        - 체인(Chain), 가중치(Weight), 비율 설정 등을 이용해 복잡한 반응형 디자인도 쉽게 구현 가능하다.

- ViewBinding과 DataBinding의 차이점
    - ViewBinding
        - 자동으로 View에 대한 타입 안전한 참조를 생성해준다.
        - findViewById() 호출 없이 XML에 선언된 모든 View에 접근할 수 있다.
        - UI와 데이터의 연결은 직접 수동으로 해야 한다.
        - 단순하고 빠르며, 성능 오버헤드가 거의 없다.
        - 런타임 시 오류를 줄이고 컴파일 타임에서 오류를 잡을 수 있다.

    - DataBinding
        - UI와 데이터를 직접 연결(bind) 할 수 있다.
        - XML 파일 안에서 변수, 식(Expression), LiveData 관찰 등을 선언할 수 있다.
        - @BindingAdapter 등을 통해 커스텀 바인딩 로직도 정의 가능하다.
        - 복잡한 양방향 바인딩(@={}) 지원으로 MVVM 아키텍처에 적합하다.
        - 다만 컴파일 시간이 길어지고, 초기 설정이 ViewBinding보다 복잡할 수 있다.

    - 간단 요약
        - ViewBinding: View 참조만 쉽게 하자. (빠르고 가벼움)
        - DataBinding: UI와 데이터까지 직접 연결하자. (MVVM에 적합, 더 무겁고 복잡)

- 안드로이드에서 긴 작업을 수행할 때 UI 스레드가 차단되지 않게 하기 위한 방법
    - 원칙
        - UI 스레드(Main Thread) 는 반드시 가볍고 빠르게 유지해야 한다.
        - 긴 작업(네트워크 통신, 파일 I/O, 디코딩 등)은 반드시 백그라운드 스레드에서 처리해야 한다.

    - 주요 방법
        - (1) Kotlin Coroutines
            - Dispatchers.IO, Dispatchers.Default 등을 사용하여 비동기 작업 수행.
            - 가볍고 코드를 직관적으로 작성할 수 있어 현대 안드로이드 개발의 표준.
        - (2) Thread + Handler
            - 전통적인 방법.
            - 별도의 Thread를 생성하고, 결과를 Handler로 메인스레드에 전달.
            - 직접 스레드를 관리해야 하므로 비교적 번거롭다.
        - (3) AsyncTask (Deprecated)
            - 과거에 UI-Thread와 백그라운드 스레드 작업을 쉽게 연결하려고 만든 클래스.
            - 현재는 권장되지 않고 Coroutine이나 WorkManager를 사용하는 것이 좋다.
        - (4) WorkManager
            - 장시간 실행이 필요한 작업(특히 앱이 종료돼도 보장되어야 하는 작업)을 백그라운드로 예약.
            - 주로 서버 동기화, 파일 업로드 같은 작업에 적합.

- WorkManager와 AlarmManager의 차이점
    - WorkManager
        - 장시간 작업을 안정적으로 예약하고 실행한다.
        - 앱이 꺼져도, 기기가 재부팅돼도 작업이 유지된다.
        - 네트워크 연결 여부, 충전 상태 같은 조건부 실행 제어가 가능하다.
        - 내부적으로 상황에 따라 JobScheduler, FirebaseJobDispatcher, AlarmManager 등을 적절히 조합해서 사용한다.
        - 주로 신뢰성이 중요한 백그라운드 작업(예: 서버 업로드, 데이터 동기화)에 사용.

    - AlarmManager
        - 특정 시간에 알람을 발생시킨다.
        - 시간이 되면 앱이 실행 중이든 아니든 PendingIntent를 통해 알람을 발생시킨다.
        - 단순히 알람만 울릴 뿐, 작업 완료 보장이나 상태 체크는 스스로 관리해야 한다.
        - 주로 시간 기반 트리거(예: 특정 시간에 알림 표시, 예약 동작 실행 등)에 사용.

    - 간단 요약
        - WorkManager: 조건 기반, 작업 성공 보장, 백그라운드 장시간 신뢰성 작업.
        - AlarmManager: 시간 트리거 기반 알람 발생, 이후 작업은 개발자가 알아서 관리.

- 코루틴에서 Dispatchers.Main, Dispatchers.IO, Dispatchers.Default의 차이
    - Dispatchers.Main
        - UI 스레드(Main Thread) 에서 코루틴을 실행한다.
        - UI 갱신, 사용자 입력 처리와 같은 작업을 수행할 때 사용.
        - 무거운 연산이나 블로킹 작업을 하면 절대 안 된다.

    - Dispatchers.IO
        - I/O 작업(네트워크 요청, 파일 읽기/쓰기, 데이터베이스 쿼리 등)을 위한 최적화된 스레드 풀을 사용한다.
        - 다수의 I/O 요청을 효율적으로 처리할 수 있게 설계되어 있다.
        - I/O 작업은 CPU를 많이 소모하지 않기 때문에 스레드를 많이 만들어도 부담이 적다.

    - Dispatchers.Default
        - CPU 집약적 작업(복잡한 계산, 데이터 처리, 대규모 리스트 정렬 등)을 위한 스레드 풀을 사용한다.
        - 내부적으로 기기 CPU 코어 수에 맞춰 스레드 수를 최적화한다.
        - 무거운 연산을 병렬로 처리할 때 적합하다.

    - Dispatchers.Unconfined
        - 개념
            - 특정 스레드에 묶이지 않고 코루틴을 실행하는 디스패처다.
            - 처음 실행할 때는 현재 호출한 스레드에서 실행하고, suspension(일시 중단) 이후에는 재개되는 스레드가 달라질 수 있다.
        - 동작 방식
            - 코루틴이 처음 시작될 때:
                - 현재 코루틴을 호출한 스레드(보통 Main, IO 등) 에서 즉시 실행된다.
            - suspend 지점 이후 재개될 때: (예: delay(1000) 이후)
                - 어떤 스레드에서든 재개될 수 있다. (보장되지 않음)

        - 특징
            - 스레드를 고정하지 않는다. (비고정 디스패처)
            - 매우 가볍고 빠르지만, UI 작업처럼 특정 스레드에서 안전하게 실행해야 하는 작업에는 위험하다.
            - 주로 테스트 용도나 간단한 작업에서 사용한다.
            - 무거운 작업이나 멀티스레드 충돌이 발생할 수 있는 작업에는 적합하지 않다.

        - 사용 시기
            - 특정 스레드에 구애받지 않고 작업 순서만 중요할 때.
            - 테스트 코드 작성 시 디스패처를 가볍게 처리할 때.
            - UI 업데이트가 필요 없는, 단순 로직을 빠르게 처리하고 싶을 때.

        - 주의사항
            - 스레드 안정성(Thread Safety)이 필요한 작업에는 절대 사용하면 안 된다.
            - 특히 UI 컴포넌트 접근은 반드시 Dispatchers.Main을 사용해야 한다.
            - 예상치 못한 스레드에서 재개되면, 디버깅이 매우 까다로워질 수 있다.

        - 간단 요약
            - Unconfined = "처음은 호출 스레드, suspend 후는 어디서든 재개"
            - 빠르고 가볍지만, 안정성 보장 X
            - 테스트나 간단한 작업에서만 신중하게 사용

- Explicit Intent와 Implicit Intent의 차이
    - Explicit Intent (명시적 인텐트)
        - 명확하게 대상 컴포넌트(Activity, Service 등)를 지정해서 호출하는 인텐트.
        - 앱 내부의 특정 화면이나 기능을 직접 실행할 때 사용.
        ```kotlin
        val intent = Intent(this, DetailActivity::class.java)
        startActivity(intent)
        ```
        - 사용 예시
            - 다른 액티비티 열기
            - 서비스 시작하기
            - BroadcastReceiver 직접 호출

    - Implicit Intent (암시적 인텐트)
        - 수행하고 싶은 액션(Action)만 지정하고, 시스템이 적합한 컴포넌트를 찾아 실행하는 인텐트.
        - 주로 다른 앱의 기능을 호출할 때 사용.
        ```kotlin
        val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://example.com"))
        startActivity(intent)
        ```
        - 사용 예시
            - 웹 브라우저 열기
            - 카메라 앱 실행
            - 연락처에서 전화번호 선택

    - 간단 요약
        - Explicit Intent: "어디로 갈지 정해져 있다" → 내부 컴포넌트 호출
        - Implicit Intent: "무엇을 할지만 정해져 있다" → 시스템이 적합한 앱이나 기능을 찾아 실행

- Activity 간 데이터를 전달하는 가장 일반적인 방법
    - Intent를 사용한 데이터 전달
        - 가장 표준적이고 많이 쓰이는 방법.
        - Intent의 extras(Bundle) 를 이용해서 데이터를 넘긴다.

    - 방법
        - 보내는 쪽 (Activity A → Activity B)
            ```kotlin
            val intent = Intent(this, BActivity::class.java)
            intent.putExtra("key_name", "value_data")
            startActivity(intent)
            ```
        - 받는 쪽 (Activity B)
            ```kotlin
            val data = intent.getStringExtra("key_name")
            ```
    - 특징
        - 간단한 타입(Primitive, String, Serializable, Parcelable 등)을 쉽게 전달할 수 있다.
        - 복잡한 객체를 전달할 때는 Parcelable 구현을 권장한다. (Serializable은 느리다)
        - startActivityForResult → registerForActivityResult로 대체되면서 ActivityResult API를 함께 쓰는 경우도 많아졌다.

- BroadcastReceiver를 사용하는 상황
    - 개념
        - 앱 내부 또는 외부에서 발생한 시스템/앱 이벤트를 감지하고 대응하는 컴포넌트.
        - 브로드캐스트(전파)되는 이벤트를 수신하여 처리한다.

    - 사용하는 대표 상황
        - (1) 시스템 이벤트 감지
            - 예시:
                - 기기 부팅 완료 (BOOT_COMPLETED)
                - 네트워크 연결 상태 변경 (CONNECTIVITY_CHANGE)
                - 배터리 부족 경고 (BATTERY_LOW)
        - (2) 앱 내부 이벤트 전달
            - 앱 컴포넌트 간 느슨하게 통신할 때 사용.
            - 예시: 특정 작업 완료 시 다른 컴포넌트에 알리기.

    - 주의할 점
        - Android 8.0(API 26)부터 정적 등록(Manifest 등록) BroadcastReceiver 제한이 생겼다.
            - (일부 시스템 브로드캐스트만 수신 가능 → 나머지는 동적 등록해야 함)
        - 꼭 필요한 경우에만 사용해야 한다. 과도한 브로드캐스트 수신은 배터리 소모를 초래할 수 있다.

- Android 8.0(API 26)부터 정적 등록(Manifest 등록) BroadcastReceiver 제한
    - 기본 개념
        - 이전까지는 Manifest에 등록만 하면 앱이 꺼져 있어도 대부분의 브로드캐스트를 수신할 수 있었다.
        - 하지만 Android 8.0부터는 앱이 실행 중이 아닐 때 Manifest에 등록된 BroadcastReceiver가 일부 시스템 이벤트에 대해서만 호출된다.

    - 제한된 이유
        - 백그라운드 앱들의 무분별한 브로드캐스트 수신으로 인해 배터리 소모 증가
        - 시스템 리소스 낭비 
        - 백그라운드 앱 활동을 최소화하여 배터리 수명 향상과 성능 최적화를 목적으로 도입됨.

    - 제한 되는 경우
        - 앱이 완전히 종료되어 있고 (Background 상태)
        - Manifest에 등록된 BroadcastReceiver만 의존하는 경우.
        - 허용된 특정 시스템 이벤트만 수신 가능.
        - 대부분의 일반 브로드캐스트(CONNECTIVITY_CHANGE, NEW_PICTURE 등)는 수신 불가.

    - 수신 가능한 대표적 예외 (허용된 이벤트)
        - BOOT_COMPLETED (기기 부팅 완료)
        - SMS_RECEIVED (SMS 수신)
        - PACKAGE_ADDED, PACKAGE_REMOVED (앱 설치/삭제)
        - ACTION_MY_PACKAGE_REPLACED (자기 앱이 업데이트됨)
        - 일부 알람 관련 이벤트(TIMEZONE_CHANGED, TIME_SET 등)
        - ※ 허용 리스트는 한정적이며, 대부분의 일반 이벤트는 수신 불가.

    - 대응 방법
        - (1) 동적 등록 사용
            - 앱이 실행 중일 때 코드에서 registerReceiver()로 수신 등록해야 한다.
            - 앱이 꺼지면 수신되지 않지만, 필요할 때만 정확하게 리스닝 가능.
                - 자바/코틀린 코드 상에서 작성 (onStart / onStop)
        - (2) Foreground Service 이용
            - 지속적으로 브로드캐스트를 수신해야 할 경우
                - → 앱을 Foreground Service로 전환하여 백그라운드 제한을 우회할 수 있다.
                - 단, 사용자에게 알림(Notification) 을 항상 표시해야 한다.

        - (3) WorkManager 사용
            - 예약된 작업이나 조건부 작업이 필요할 경우
                - → WorkManager를 활용해서 시스템 이벤트 감지 후 필요한 작업을 수행.

    - 간단 요약
        - Android 8.0부터는 Manifest 등록만으로 대부분의 브로드캐스트 수신 불가
        - 반드시 필요한 경우만 일부 시스템 이벤트 허용
        - 일반적인 경우는 동적 등록 또는 Foreground Service, WorkManager를 사용해서 대응 필수

- Room 데이터베이스에서 DAO 역할
    - DAO (Data Access Object): 데이터 접근 객체
        - Room 데이터베이스와 앱의 비즈니스 로직 간의 연결 통로 역할을 한다.
        - SQL 쿼리를 추상화하여 메서드로 표현하는 인터페이스 또는 추상 클래스다.

    - 주요 기능
        - 데이터베이스 접근 메서드 정의
            - (조회, 삽입, 수정, 삭제 작업 → SQL 없이 메서드로 표현)
            ```kotlin
            @Dao
            interface UserDao {
                @Query("SELECT * FROM user")
                fun getAll(): List<User>

                @Insert
                fun insert(user: User)

                @Delete
                fun delete(user: User)
            }
            ```
            - 컴파일 타임에 SQL 문법 검사가 가능하다.
            - Room이 DAO 코드를 기반으로 자동으로 구현체를 생성한다.

    - 특징
        - 코드의 가독성과 유지보수성이 높아진다.
        - Room은 DAO 없이 직접 접근하는 것을 허용하지 않는다. → 강제적으로 안전한 구조 유지

- SQLiteOpenHelper를 사용할 때 onUpgrade() 호출 시점
    - onUpgrade() 개념
        - 데이터베이스 버전이 변경될 때 호출되는 메서드.
        - 기존 데이터베이스 구조를 새 버전에 맞게 마이그레이션하는 역할을 한다.

    - 호출되는 정확한 조건
        - SQLiteOpenHelper를 생성할 때 지정한 버전 번호가 기존 데이터베이스의 버전보다 클 때 호출된다.
        ```kotlin
        SQLiteOpenHelper(context, "database_name", null, NEW_VERSION)
        ```
        - 예를 들어:
            - 기존 DB 버전이 1
            - 새로 코드에 설정한 버전이 2
            - 앱 실행 시 → onUpgrade() 호출됨

    - onUpgrade()에서 주로 하는 일
        - 테이블 추가/삭제
        - 컬럼 추가
        - 데이터 이전(Migration)
        - 구조 변경에 필요한 모든 작업
        ```kotlin
        override fun onUpgrade(db: SQLiteDatabase, oldVersion: Int, newVersion: Int) {
            if (oldVersion < 2) {
                db.execSQL("ALTER TABLE user ADD COLUMN last_login INTEGER")
            }
        }
        ```

    - 주의할 점
        - onUpgrade()를 잘못 설계하면 데이터 손실이 발생할 수 있다.
        - 반드시 데이터 백업 → 구조 변경 → 데이터 복구를 고려한 설계를 해야 한다.

    - 간단 요약
        - Room의 DAO:
            - DB 접근 메서드를 정의하는 추상화된 인터페이스/클래스.
            - Room이 자동 구현, SQL 안전성 보장.
        
        - SQLiteOpenHelper의 onUpgrade():
            - DB 버전이 상승할 때 호출된다.
            - 테이블 구조 변경 및 데이터 마이그레이션 수행.

- Android 6.0 (Marshmallow) 이후 퍼미션을 처리하는 방법
    - 배경
        - Android 6.0(API 23)부터 "런타임 퍼미션" 제도가 도입되었다.
        - 설치할 때가 아니라, 앱이 실제로 기능을 사용할 시점에 사용자에게 퍼미션을 요청해야 한다.

    - 퍼미션 처리 흐름
        - (1) AndroidManifest.xml에 퍼미션 선언
            - 선언만 하면 끝이 아니라, 실제 앱 실행 중 요청을 별도로 해야 한다.

        - (2) 퍼미션 상태 체크
            - 앱이 퍼미션을 이미 갖고 있는지 먼저 확인한다.
            ```kotlin
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED) {
                // 이미 권한 있음
            } else {
                // 권한 요청 필요
            }
            ```

        - (3) 퍼미션 요청
            - 권한이 없으면 사유자에게 요청
            ```kotlin
            ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.CAMERA), REQUEST_CODE)
            ```

        - (4) 결과 처리
            - 사용자가 수락/거절했는지 콜백을 통해 처리한다.
            ```kotlin
            override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray) {
                if (requestCode == REQUEST_CODE) {
                    if ((grantResults.isNotEmpty() && grantResults[0] == PackageManager.PERMISSION_GRANTED)) {
                        // 권한 허용됨
                    } else {
                        // 권한 거부됨
                    }
                }
            }
            ```

    - 추가 포인트
        - "다시 묻지 않기"를 선택하면, 앱 설정 화면으로 유도해야 한다.
        - 여러 퍼미션을 묶어서 동시에 요청할 수도 있다.
        - 최신 API에서는 ActivityResultLauncher 기반의 권한 요청 방식 (registerForActivityResult)을 권장한다.

- ContentProvider의 주요 목적
    - 개념 (표준화된 인터페이스, 앱 간 / 앱 내부 데이터 공유)
        - 앱 간 또는 앱 내부에서 데이터를 안전하게 공유할 수 있도록 하는 컴포넌트.
        - 데이터베이스, 파일, 네트워크 등 다양한 소스의 데이터를 표준화된 인터페이스로 제공한다.

    - 주요 목적
        - (1) 앱 간 데이터 공유
            - 다른 앱에서 ContentProvider를 통해 데이터에 접근할 수 있다.
            - 예시: 연락처 앱이 자신의 데이터를 다른 앱에 제공.
            ```kotlin
            val cursor = contentResolver.query(ContactsContract.Contacts.CONTENT_URI, null, null, null, null)
            ```

        - (2) 보안 제어
            - 권한을 이용해 데이터 접근 권한을 정밀하게 관리 가능
            - 읽기/쓰기 권한을 별도로 설정 가능

        - (3) 통합된 데이터 접근 방식 제공
            - ContentResolver를 통해 앱 내외부의 다양한 데이터 소스에 일관된 방식으로 접근할 수 있다.
            - 데이터베이스를 직접 노출하지 않고, 추상화된 API로 제어할 수 있다.

    - 사용 시점
        - 앱 간 데이터 공유가 필요한 경우
        - (ex: 연락처, 사진 갤러리, 메시지 앱 등)
        - 앱 내부에서도 여러 컴포넌트(Activity, Service 등)가 데이터를 통합적으로 사용할 때.

    - 간단 요약
        - Android 6.0 이후 퍼미션 처리:
            - 설치 시점 아님 → 기능 사용 시점에 런타임 요청 필요

        - ContentProvider 주요 목적:
            - 앱 간 안전한 데이터 공유
            - 데이터 접근 보안 관리
            - 표준화된 데이터 인터페이스 제공

- 앱의 민감한 데이터를 저장할 때 권장되는 방법
    - 기본 원칙
        - 민감한 데이터(토큰, 로그인 정보, 개인 식별 정보 등)는 암호화하여 저장해야 한다.
        - 저장 위치는 반드시 보안이 강화된 영역이어야 한다.

    - 권장 저장 방법
        - (1) EncryptedSharedPreferences
            - SharedPreferences를 AES-256 암호화하여 저장하는 공식 방법.
            - Android Jetpack Security 라이브러리 지원.
            ```kotlin
            val sharedPreferences = EncryptedSharedPreferences.create(
                "secure_prefs",
                MasterKeys.getOrCreate(MasterKeys.AES256_GCM_SPEC),
                context,
                EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
                EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
            )
            ```
            - 안전하게 키-값 쌍으로 저장 가능

    - (2) EncryptedFile
        - 파일 형태로 저장해야 할 경우, 파일 자체를 암호화해서 저장.
        - 대용량 데이터(예: 문서, 로그) 저장 시 사용.

    - (3) Android Keystore System
        - 암호화 키를 안전하게 저장하는 시스템.
        - 민감한 키(예: RSA 키, AES 키)를 직접 노출하지 않고, Keystore 내부에 보관.
        - 키를 직접 다루지 않고 사용만 할 수 있게 되어 있어 매우 안전함.

    - 기타 주의사항
        - 민감 데이터는 외부 저장소(SD 카드 등)에 저장하면 안 된다.
        - 네트워크 통신 시에도 HTTPS를 반드시 사용해야 한다.

- Android에서 메모리 누수(Memory Leak)가 발생하는 가장 흔한 예를 하나 들고, 이를 방지하는 방법
    - 가장 흔한 예: Context 참조로 인한 메모리 누수
    - 예시 상황
        - Activity나 Fragment의 Context를 오래 참조하는 경우
        - 예를 들어, Activity가 이미 종료되었는데도
        - 백그라운드에서 실행 중인 객체(예: Handler, Thread, Singleton 등)가 Activity를 참조하고 있으면 GC(가비지 컬렉터)가 Activity를 수거하지 못해 메모리 누수가 발생
        ```kotlin
        object MyManager {
            var context: Context? = null
        }
        ```
        - 이 경우, MyManager가 Application Context가 아니라 Activity Context를 참조하면, 액티비티 메모리가 해제되지 않음
    
    - 방지 방법
        - (1) Application Context 사용
            - Activity나 View의 Context 대신 applicationContext를 사용하면 메모리 누수를 막을 수 있다.

        - (2) WeakReference 사용
            - 메모리 해제가 가능하도록 WeakReference로 감싸서 참조한다.
            - Callback, Listener 등에서 자주 활용됨
            - 예: val weakContext = WeakReference(context)

        - (3) 생명주기와 함께 관리
            - Handler, Runnable, Observer 같은 비동기 객체들은 onDestroy()나 onCleared() 시점에 반드시 해제해야 한다.
            ```kotlin
            override fun onDestroy() {
                handler.removeCallbacksAndMessages(null)
                super.onDestroy()
            }
            ```
    - 간단 요약
        - 민감 데이터 저장:
            - EncryptedSharedPreferences, EncryptedFile, Keystore 사용.

        - 메모리 누수 흔한 예:
            - Context를 잘못 참조 → GC가 수거 못함.
            - Application Context 사용, WeakReference 사용, 수명 주기와 함께 해제로 예방.

- ViewHolder 패턴을 사용하는 이유
    - 배경
        - ListView, RecyclerView 같은 스크롤 가능한 뷰들은
        - 스크롤할 때마다 계속해서 View를 생성하고 findViewById() 호출을 반복한다.
        - 이 작업은 매우 비용이 크고 느리다.

    - ViewHolder 패턴의 핵심
        - 뷰를 재활용하고, findViewById 호출을 최소화하여 성능을 최적화하는 패턴이다.

    - 방법
        - 각 아이템 View에 대해 뷰 참조를 저장하는 객체(ViewHolder)를 만든다.
        - 뷰를 재활용할 때 기존 ViewHolder를 재사용하고, 다시 findViewById()를 호출하지 않는다
        ```kotlin
        class ViewHolder(view: View) {
            val titleTextView: TextView = view.findViewById(R.id.title)
        }

        // Adapter의 getView나 onBindViewHolder에서 사용
        ```

    - 주요 이점 (스크롤, 메모리, 반응성)
        - 스크롤 성능 향상 (findViewById()는 호출할 때마다 View 트리를 탐색하므로, 제거하면 훨씬 빨라진다.)
        - 메모리 사용량 감소 (불필요한 View 객체 생성 방지)
        - UI 반응성 개선 (스크롤이 부드러워진다)

- Bitmap을 효율적으로 로드할 때 주의해야 할 점
    - 문제
        - 고해상도 이미지를 한 번에 메모리에 로드하면 OutOfMemoryError(OOM) 가 쉽게 발생할 수 있다.
        - 특히 안드로이드에서는 메모리 관리가 제한적이기 때문에 주의해야 한다.

    - 주의사항 및 해결 방법
        - (1) 이미지 크기 조절 (샘플링)
            - 화면에 표시할 크기에 맞게 Bitmap을 축소해서 로드해야 한다.
            - 원본 사이즈를 그대로 메모리에 로드하지 않는다.
            ```kotlin
            val options = BitmapFactory.Options().apply {
                inSampleSize = 4 // 1/4 크기로 로드
            }
            val bitmap = BitmapFactory.decodeResource(resources, R.drawable.large_image, options)
            ```
        - (2) 캐싱 전략 사용
            - 이미 로드한 Bitmap은 메모리 캐시나 디스크 캐시에 저장하여 다시 로딩할 때 빠르게 가져온다.
            - 대표적인 라이브러리: Glide, Picasso, Coil

        - (3) Bitmap Config 최적화
            - 필요 없는 경우에는 ARGB_8888 대신 RGB_565 같은 저용량 포맷을 사용해 메모리 절약 가능.
            - options.inPreferredConfig = Bitmap.Config.RGB_565

        - (4) 리소스 해제 (recycle)
            - 사용이 끝난 Bitmap은 필요에 따라 recycle() 호출해서 명시적으로 메모리 해제할 수 있다.
            - 단, Glide 같은 라이브러리를 사용하면 직접 recycle할 필요는 없다.

    - 총 정리
        - ViewHolder 패턴:
            - findViewById 최소화, 뷰 재활용, 스크롤 성능 향상.
        - Bitmap 효율적 로드:
            - 샘플링(축소), 캐시 사용, Bitmap Config 조정, 리소스 해제로 OOM 방지.

- AndroidManifest.xml에서 필수적으로 정의해야 하는 두 가지 (컴포넌트 + 권한)
    - (1) 앱의 컴포넌트(Component)
        - 앱을 구성하는 주요 컴포넌트는 반드시 Manifest에 등록해야 한다.
        - 컴포넌트 종류
            - Activity
            - Service
            - BroadcastReceiver
            - ContentProvider
        - 등록하지 않으면 시스템이 해당 컴포넌트를 인식하지 못해 동작할 수 없다.

    - (2) 앱의 권한(Permissions)
        - 앱이 민감한 기능(네트워크, 카메라, 파일 읽기 등)을 사용할 경우
        - 사용 권한을 명시적으로 선언해야 한다.
        - 선언하지 않으면 해당 기능을 사용할 수 없고, 요청해도 자동으로 거부된다.

    - 추가적으로 자주 정의하는 항목
        - 최소/타겟 SDK 버전 (minSdkVersion, targetSdkVersion)
        - 앱 이름, 아이콘 (application 태그 내부 설정)
        - 인텐트 필터 (intent-filter) 등록 (예: 런처 설정, 딥링크 설정)

- Jetpack Navigation Component를 사용하는 주요 이점
    - (1) 복잡한 네비게이션을 단순화
        - 여러 Fragment나 Activity 간의 이동을 선언적(Declarative) 으로 설계할 수 있다.
        - XML 파일(nav_graph.xml)로 전체 화면 흐름을 한눈에 볼 수 있다.

    - (2) 안전한 인자 전달(Safe Args)
        - 화면 전환 시 데이터 전달을 타입 안전(type-safe) 하게 할 수 있다.
        - 컴파일 타임에 오류를 잡아주기 때문에, Intent나 Bundle 실수(키 오타 등)를 막을 수 있다.

    - (3) 백 스택 자동 관리
        - 화면 이동 시 Back Stack을 자동으로 관리해준다.
        - 개발자가 직접 FragmentTransaction을 일일이 다루지 않아도 된다.

    - (4) 딥링크(Deep Link) 지원
        - 외부에서 앱의 특정 화면으로 바로 진입할 수 있도록 딥링크를 쉽게 설정할 수 있다.
        - 인텐트 필터 설정 없이도 XML에서 쉽게 매핑 가능.

    - (5) UI 상태와 네비게이션 상태 통합 가능
        - NavigationUI를 활용하면 BottomNavigationView, NavigationDrawer 등과 NavController를 자동으로 연결할 수 있다.
        ```kotlin
        NavigationUI.setupWithNavController(bottomNavigationView, navController)
        ```

    - (6) 싱글 액티비티 체제 아키텍쳐와의 궁합

- 프로가드(ProGuard) 설정은 주로 어떤 목적으로 사용
    - 주요 목적
        - (1) 코드 난독화(Obfuscation)
            - 클래스, 메서드, 변수 이름을 의미 없는 이름(a, b, c 등)으로 변경하여 코드를 리버스 엔지니어링하기 어렵게 만든다.
            - APK를 디컴파일해도 원래 의미를 파악하기 힘들어진다.

        - (2) 코드 최적화(Optimization)
            - 사용되지 않는 코드(dead code)를 제거하고, 중복 코드를 통합하여 APK 파일 크기를 줄이고 성능을 개선한다.

        - (3) 코드 축소(Shrinking)
            - 사용되지 않는 클래스, 메서드, 리소스를 자동으로 제거하여 앱의 최종 크기를 최소화한다.

        - (4) 보안 강화(Security)
            - 핵심 로직이나 알고리즘을 쉽게 파악하지 못하게 하여 어느 정도 보안성을 높일 수 있다.

    - 간단 요약
        - ProGuard = 코드 난독화 + 최적화 + 축소 + 보안 강화
        - 디컴파일/해킹을 100% 막지는 못하지만, 리버스 엔지니어링 난이도를 높인다.

- 액티비티가 onStop() 상태에 있다가 다시 사용자에게 표시되면 호출되는 메서드
    - 호출되는 메서드
        - onRestart() → onStart()

    - 동작 순서
        - 액티비티가 onStop() 상태에 있음 (사용자에게 화면이 안 보이는 상태)
        - 사용자가 다시 액티비티로 돌아오면:
            - onRestart() 먼저 호출
                - "멈췄던 액티비티를 다시 시작하려고 준비하는 단계"
            - 이어서 onStart() 호출
                - 화면이 사용자에게 다시 보이기 시작하는 단계
            - 그리고 onResume() 호출되어 완전 활성화됨.

    - 간단 흐름 요약
        - onStop() → onRestart() → onStart() → onResume()

    - 간단 요약
        - ProGuard 설정:
            - 난독화 + 최적화 + 축소 + 보안 강화 목적으로 사용.
        - onStop() 후 다시 표시될 때 호출되는 메서드:
            - onRestart() 호출 후 onStart() → onResume() 순서로 이어진다.

- 프래그먼트가 재사용될 때 onCreateView()는 항상 호출되는지와 호출된다면 그 이유
    - 항상 호출 여부
        - 프래그먼트가 재사용될 때 onCreateView()는 항상 호출됨

    - 호출 이유
        - onCreateView()는 프래그먼트듸 UI(View)를 새로 생성하는 메서드
        - 프래그먼트가 화면에서 사라질 때(onDestroyView() 호출)
            - -> 뷰 객체는 메모리에서 해제
        - 프래그먼트 객체 자체는 살아있어도, 뷰는 재사용되지 않음
        - 다시 화면에 표시될 때는 반드시 새로운 뷰를 생성하기 위해 onCreateView()가 호출

    - 정리
        - 프래그먼트 인스턴스는 살아있을 수 있지만,
        - View는 항상 새로 만들어야 하므로 onCreateView()는 호출된다.

- ViewModel은 어떤 생명주기를 기준으로 메모리에서 제거되는 지 설명
    - 어떤 생명주기를 기준으로 메모리에서 제거되는지에 대한 내용
        - ViewModel은 연결된 LifecycleOwner(Activity나 Fragment)가 종료될 때 메모리에서 제거된다

    - 상세 설명
        - 액티비티에 연결된 뷰델
            - 액티비티가 Finish()되거나 시스템에 의해 파괴될 때 onCleared() 호출됨
        - 프래그먼트에 연결된 뷰모델
            - 프래그먼트가 소멸될 때, 그리고 관련된 ViewModelStoreOwner도 더 이상 존재하지 않을 때 onCleared() 호출됨
        - 뷰모델은 화면 회전 같은 구성 변경 (Configuration Change)시에는 자동으로 재사용됨
        - 액티비티나 프래그먼트가 재생성되어도 뷰모델은 살아남음

    - 주의사항
        - ViewModel은 View의 수명과 다르다.
        - 프래그먼트의 View가 onDestroyView()로 파괴되어도,
        - 프래그먼트가 살아 있다면 ViewModel도 그대로 살아있다.

    - 총정리
        - 프래그먼트 재사용 시 onCreateView() 호출 여부:
            - 항상 호출된다. (View는 새로 생성되어야 하기 때문)
        - ViewModel 메모리 제거 기준:
            - 연결된 Activity나 Fragment의 Lifecycle이 완전히 종료될 때 (onCleared() 호출)

- SavedStateHandle은 어떤 상황에서 유용하게 사용되는지 설명
    - 개념
        - SavedStateHandle은 ViewModel에 데이터를 안전하게 저장하고 복구할 수 있도록 도와주는 도구다.
        - 화면 회전, 프로세스 종료(시스템 강제 종료) 같은 구성 변경(Configuration Change) 상황에서도 상태(state)를 유지하고 복구할 수 있게 해준다.

    - 유용한 상황
        - (1) 화면 회전 등 구성 변경 시 데이터 복구
            - 예시: 사용자가 입력 중이던 데이터를 화면 회전 후에도 유지하고 싶을 때.
            ```kotlin
            class MyViewModel(private val savedStateHandle: SavedStateHandle) : ViewModel() {
                fun saveUserInput(input: String) {
                    savedStateHandle["user_input"] = input
                }

                fun getUserInput(): String? {
                    return savedStateHandle["user_input"]
                }
            }
            ```

        - (2) 프로세스가 강제 종료되었다가 복원될 때 데이터 유지
            - 예시: 백그라운드에서 메모리 부족으로 앱 프로세스가 죽었다가 다시 살아날 때, 사용자가 보고 있던 상태를 복구해야 할 때 유용하다.

        - (3) Navigation Component와 함께 인자 관리    
            - SafeArgs 없이도 SavedStateHandle을 이용해 프래그먼트 간 전달된 인자를 저장하고 복구할 수 있다.
            ```kotlin
            val userId = savedStateHandle.get<String>("userId")
            ```

    - 간단 요약
        - SavedStateHandle은
            - 구성 변경, 프로세스 종료 시에도 ViewModel에 안전하게 데이터 저장/복구를 도와준다.
        - 주로 입력값 저장, 상태 유지, 네비게이션 인자 관리 등에 유용하다.

- CoroutineScope를 액티비티에서 사용할 때 취소(Cancel)를 반드시 해줘야 하는 이유
    - 이유
        - 액티비티가 종료되었는데도 Coroutine이 계속 살아있으면 메모리 누수(Memory Leak)가 발생할 수 있다.
        - 살아있는 Coroutine이 Activity나 Fragment의 Context, View 등을 참조하면 GC(가비지 컬렉터)가 메모리를 해제하지 못해 누수가 생긴다.

    - 주요 문제점
        - 메모리 낭비 (필요 없는 리소스가 계속 살아있음)
        - 비정상적인 작업 수행 (이미 닫힌 화면에 데이터를 업데이트하려고 하거나, 충돌 발생)
        - 배터리 소모 증가 (불필요한 작업이 계속 백그라운드에서 돌 수 있음)

    - 올바른 사용법
        - lifecycleScope나 viewModelScope를 사용하면 Lifecycle에 따라 자동으로 Coroutine이 취소된다.
        - 만약 별도로 CoroutineScope를 만들었다면, 반드시 onDestroy()나 적절한 시점에 직접 cancel() 호출해줘야 한다.
        ```kotlin
        private val myScope = CoroutineScope(Dispatchers.Main)

        override fun onDestroy() {
            super.onDestroy()
            myScope.cancel()
        }
        ```

- viewModelScope와 lifecycleScope의 주요 차이
    - viewModelScope
        - 개념
            - ViewModel 전용 CoroutineScope다.        
            - ViewModel이 onCleared() 될 때 자동으로 Coroutine이 취소(canceled) 된다.
            - ViewModel 안에서 비동기 작업(네트워크, DB 등)을 수행할 때 사용.
        - 특징
            - ViewModel과 수명(lifecycle) 을 같이 함.
            - 화면 회전(Configuration Change)이 일어나도 ViewModel은 살아남기 때문에, 비동기 작업도 계속 유지된다.
            - 주로 UI 상태 관리, 데이터 로드, 비즈니스 로직을 처리할 때 사용.

    - lifecycleScope
        - 개념
            - LifecycleOwner(Activity, Fragment) 전용 CoroutineScope다.
            - 해당 컴포넌트가 DESTROYED 상태가 되면 Coroutine이 자동으로 취소된다.
        - 특징
            - Activity나 Fragment의 Lifecycle에 직접 연결된다.
            - 화면이 종료되면 즉시 Coroutine이 취소된다.
            - 주로 UI와 밀접한 작업, 짧은 생명주기 작업(애니메이션, 간단한 비동기 요청 등)에 사용한다.

    - 총정리
        - viewModelScope: ViewModel 수명에 맞춰 살아있음.
            - → UI 데이터 관리, 비즈니스 로직 처리에 적합.
        - lifecycleScope: Activity/Fragment 수명에 맞춰 살아있음.
            - → UI 처리, 화면 기반 짧은 작업에 적합.

- suspend 키워드를 함수에 붙였을 때 함수 동작 원리
    - suspend 개념
        - suspend 키워드를 붙이면, 이 함수는 코루틴 안에서만 호출할 수 있는 일시 중단(suspendable) 함수가 된다.
        - 일시 중단이란: 함수를 실행하는 도중에도 다른 작업을 할 수 있도록 "잠시 멈췄다가 다시 이어서 실행" 할 수 있게 만든다는 의미.

    - 동작 원리
        - suspend 함수는 내부적으로 Continuation이라는 콜백 객체를 사용한다.
        - 함수 실행 중 suspend 지점에 도달하면, 현재 상태를 저장하고 Coroutine Dispatcher에게 제어권을 넘긴다.
        - 나중에 작업이 완료되면 저장된 상태에서 다시 이어서 실행된다.
        - 이 과정은 개발자가 신경 쓰지 않아도, Kotlin 컴파일러가 자동으로 변환(Continuation-passing style)해준다.

    - 예시
        - 첫번째 예제
            ```kotlin
            suspend fun fetchData(): String {
                delay(1000) // 1초 동안 일시 중단
                return "Result"
            }
            ```
            - delay()는 중단 지점(suspension point)이다.
            - 코루틴은 1초 동안 멈추고, 그 사이에 다른 코드를 실행할 수 있다.
            - 1초 후 다시 이어서 return "Result"를 실행한다.

        - 두번째 예제
            - suspending 되었을 때 다른 코드를 실행하는 예제
            ```kotlin
            import kotlinx.coroutines.*
            fun main() = runBlocking {
                launch {
                    println("Fetch start at ${System.currentTimeMillis()}")
                    val result = fetchData()
                    println("Fetch result: $result at ${System.currentTimeMillis()}")
                }

                launch {
                    repeat(5) { i ->
                        delay(200)
                        println("Other work $i at ${System.currentTimeMillis()}")
                    }
                }
            }

            suspend fun fetchData(): String {
                delay(1000) // 1초 동안 멈춤
                return "Result"
            }
            ```
            - 실행 흐름 설명
                - 첫 번째 launch 블록이 fetchData() 를 호출한다.
                - fetchData() 안에서 delay(1000) 을 만나면서
                    - 이 코루틴은 일시 중단(suspend) 되고,
                    - 다른 코루틴(여기선 두 번째 launch)이 CPU를 사용하게 된다.
                - 두 번째 launch는 0.2초마다 반복하면서 "Other work 0", "Other work 1", ..., "Other work 4" 를 출력한다.
                - 1초가 지나고 나면 중단된 fetchData()가 다시 이어져서 "Result" 반환 후 결과를 출력한다

            - 예상 출력 예시
            ```pgsql
            Fetch start at 1714567890000
            Other work 0 at 1714567890200
            Other work 1 at 1714567890400
            Other work 2 at 1714567890600
            Other work 3 at 1714567890800
            Other work 4 at 1714567891000
            Fetch result: Result at 1714567891000
            ```

    - 주의할 점
        - suspend 함수는 직접 호출할 수 없다.
        - 반드시 launch, async, 또는 다른 suspend 함수 안에서 호출해야 한다.

    - 총 정리
        - 스레드를 차단(block)하지 않으면서, 동시에 여러 작업을 자연스럽게 병렬로 처리할 수 있다는 점이 코루틴의 장점
        - delay 중단 동안 다른 코루틴이 CPU를 사용해서 작업 수행 가능
        - suspend는 스레드를 블로킹하지 않음
        - 작업을 미뤄놓고 그 사이 다른 코루틴이 자연스럽게 실행되는 구조

- SupervisorJob을 사용하는 주요 이유
    - 개념
        - SupervisorJob은 자식 코루틴 중 하나가 실패해도 다른 자식 코루틴에 영향을 주지 않게 하는 특별한 Job이다.
        - 일반 Job과는 달리, 한 자식의 실패가 부모나 다른 자식에게 전파되지 않는다.
        
    - 주요 사용 이유
        - (1) 독립적인 작업 관리
            - 여러 코루틴을 병렬로 실행할 때, 하나의 작업이 실패하더라도 다른 작업이 계속 수행되길 원할 때 사용한다.
            ```kotlin
            val supervisor = SupervisorJob()
            val scope = CoroutineScope(Dispatchers.Main + supervisor)

            scope.launch {
                // 실패해도 다른 작업 영향 없음
            }
            scope.launch {
                // 독립적으로 실행
            }
            ```
        - (2) 병렬 작업 중 하나만 실패해도 전체 취소를 막고 싶을 때
            - 일반 Job은 하나의 실패로 전체가 취소된다.
            - 하지만 SupervisorJob은 실패를 "개별적으로" 다룬다.

        - (3) 안정성 강화
            - 사용자 경험상, 하나의 작은 실패(예: 네트워크 요청 하나 실패) 때문에
            - 앱 전체가 비정상적으로 멈추는 것을 막을 수 있다.

    - 결론
        - SupervisorJob:
            - → 자식 코루틴 실패를 독립적으로 처리하여
            - → 다른 작업에 영향 없이 안정적인 병렬 처리를 가능하게 만든다.

- Retrofit에서 suspend 함수를 사용하는 것과 콜백 기반 함수를 사용하는 것의 차이
    - suspend 기반 사용 (코루틴)
        - Retrofit 서비스 인터페이스를 suspend 함수로 정의하면, 코루틴 안에서 네트워크 요청을 자연스럽게 일시 중단하고 재개할 수 있다.
        ```kotlin
        interface ApiService {
            @GET("users")
            suspend fun getUsers(): List<User>
        }

        viewModelScope.launch {
            val users = apiService.getUsers()
        }
        ```
        - 특징
            - 코드가 동기식처럼 깔끔하게 작성된다.
            - 예외 처리도 일반 try-catch로 간단하게 처리 가능.
            - 콜백 지옥(callback hell) 없음 → 가독성 및 유지보수성 향상.

    - 콜백 기반 사용
        - 과거 방식: Retrofit의 enqueue()를 이용해 콜백(callback) 으로 결과를 받는다.
            ```kotlin
            apiService.getUsers().enqueue(object : Callback<List<User>> {
                override fun onResponse(call: Call<List<User>>, response: Response<List<User>>) {
                    // 성공 처리
                }

                override fun onFailure(call: Call<List<User>>, t: Throwable) {
                    // 실패 처리
                }
            })
            ```
            - 특징
                - 네트워크 요청 결과를 비동기 콜백으로 처리.
                - 콜백 중첩 문제(callback hell)가 발생하기 쉽다.
                - 코드가 복잡해지고 에러 핸들링이 번거롭다.

- OkHttp Interceptor를 사용하는 주요 목적
    - 개념
        - Interceptor는 HTTP 요청/응답을 가로채서 수정하거나 기록하거나 추가 작업을 할 수 있는 OkHttp의 강력한 기능
        - 일종의 중간 단계 필터 역할

    - 주요 사용 목적
        - (1) 공통 요청 헤더 추가
            - 모든 요청에 공통적으로 Authorization 토큰, User-Agent 등을 자동으로 추가할 수 있다.
            ```kotlin
            class AuthInterceptor : Interceptor {
                override fun intercept(chain: Interceptor.Chain): Response {
                    val request = chain.request().newBuilder()
                        .addHeader("Authorization", "Bearer token")
                        .build()
                    return chain.proceed(request)
                }
            }
            ```
        - (2) 요청/응답 로깅
            - API 통신 내용을 로깅하여 디버깅할 수 있다.
            - 개발 중에는 HttpLoggingInterceptor를 많이 사용한다.

        - (3) 요청/응답 가로채서 수정
            - 요청에 파라미터 추가하거나,
            - 응답을 가로채서 필요한 데이터만 추출하거나 변형할 수 있다.

        - (4) 통합 에러 처리
            - 서버에서 공통 에러 응답이 올 때, Interceptor에서 일괄적으로 처리 가능하다.
            - (예: 401 Unauthorized 응답 시, 토큰 재발급 로직 처리)
    - 정리
        - OkHttp Interceptor는 요청/응답을 가로채고 수정/기록/추가 작업할 수 있는 강력한 중간 처리 장치

- 서버 통신 중 발생할 수 있는 TimeoutException을 안전하게 처리하는 코루틴 패턴
    - 문제
        - 서버가 느리거나 네트워크가 불안정할 때 TimeoutException (ex: SocketTimeoutException)이 발생할 수 있다.
        - 이를 제대로 처리하지 않으면 앱이 강제 종료되거나 불안정한 상태에 빠질 수 있다.

    - 안전하게 처리하는 코루틴 패턴
        - (1) withTimeout() 사용
            - 일정 시간 내에 작업이 끝나지 않으면 TimeoutCancellationException을 발생시키고, 코루틴을 자동 취소한다.
            - 5초 넘으면 코루틴이 취소되고 예외가 발생한다
            ```kotlin
            suspend fun fetchDataSafely(): String {
                return withTimeout(5000L) { // 5초 이내 완료
                    apiService.getData()
                }
            }
            ```

        - (2) try-catch로 안전하게 예외 처리
            - TimeoutCancellationException은 CancellationException의 하위 타입이라 일반 Exception으로 잡아도 되고, 명시적으로 TimeoutCancellationException만 잡을 수도 있다.
            ```kotlin
            viewModelScope.launch {
                try {
                    val result = fetchDataSafely()
                    // 성공 처리
                } catch (e: TimeoutCancellationException) {
                    // 타임아웃 처리
                    showToast("서버 응답이 지연되고 있습니다.")
                } catch (e: Exception) {
                    // 기타 에러 처리
                    showToast("알 수 없는 에러 발생")
                }
            }
            ```
        - 추가
            - withTimeoutOrNull() 을 사용하면 예외 대신 null을 반환시킬 수도 있다.
            ```kotlin
            val result = withTimeoutOrNull(5000L) {
                apiService.getData()
            }
            if (result == null) {
                showToast("서버 응답 시간 초과")
            }
            ```

- Jetpack Compose에서 recomposition을 피하기 위한 최적화 기법
    - Recomposition 개념
        - 컴포저블이 입력값이나 상태가 변경되었을 때 다시 그리는 과정.
        - 필요한 경우에만 다시 그리는 것은 좋지만, 불필요한 Recomposition이 과도하면 성능 저하를 일으킬 수 있다.

    - 주요 최적화 기법
        - (1) remember 사용
            - 계산 결과나 객체를 메모리에 저장해서, 재구성(Recomposition)될 때 다시 계산하지 않고 재사용한다.
        - (2) key 사용
            - 리스트 같은 동적 컴포저블에서 각 아이템을 명확하게 구분해 불필요한 리빌드를 막는다.
            ```kotlin
            LazyColumn {
                items(items, key = { it.id }) { item ->
                    ItemRow(item)
                }
            }
            ```
        - (3) derivedStateOf 사용
            - 상태가 복잡한 계산 결과를 기반으로 변할 때, 의미 있는 변경이 일어날 때만 recomposition 하도록 한다.
            - derivedStateOf는 변경이 필요할 때만 값을 다시 계산한다.
            ```kotlin
            val isButtonEnabled by remember {
                derivedStateOf { text.isNotEmpty() }
            }
            ```
        - (4) 부하가 큰 컴포저블 분리
            - 무거운 UI나 상태 변화가 많은 부분은 별도의 컴포저블로 분리한다.
            - 변화가 없는 부모 컴포저블까지 재구성되는 걸 막을 수 있다.
        - (5) stable한 데이터 구조 사용
            - Compose는 Stable 데이터(변경 추적이 가능한 데이터) 를 다루는 데 최적화되어 있다.
            - 데이터 클래스를 불필요하게 새로 생성하거나 변형하지 않고, 필요한 경우만 갱신한다.

- derivedStateOf의 사용 시점
    - 개념
        - derivedStateOf는 다른 State를 기반으로 계산된 값을 가질 때 사용하는 API다.
        - 내부적으로 값이 실제로 변경될 때만 recomposition을 유발한다.

    - 사용 시점
        - (1) 복잡한 계산 결과를 캐시하고 싶을 때
            - 예를 들어, 입력된 텍스트가 비어 있는지 여부를 매번 직접 계산하는 대신, 필요한 경우에만 다시 계산하게 한다.
            ```kotlin
            val isFormValid by remember {
                derivedStateOf { name.isNotEmpty() && email.contains("@") }
            }
            ```
        - (2) 관찰하는 State의 변화가 자주 일어나지만, 결과는 자주 변하지 않을 때
            - 상태가 자주 바뀌더라도 계산 결과가 자주 변하지 않으면 불필요한 recomposition을 줄일 수 있다.

        - (3) Lazy 컴포넌트 최적화 (ex: LazyColumn)
            - 리스트 필터링, 정렬처럼 리스트 원본이 자주 변경되지만, 실제로 보여줄 리스트가 크게 변하지 않는 경우에 derivedStateOf로 계산해서 효율적으로 갱신할 수 있다
            ```kotlin
            val visibleItems by remember {
                derivedStateOf { allItems.filter { it.isVisible } }
            }
            ```
    - 개념 재정리
        - derivedStateOf: 다른 State에 의존하는 계산된 값을 캐싱할 때 사용한다.
        - 변화가 있을 때만 recomposition을 유발하여 성능 최적화에 효과적이다.

- LaunchedEffect와 rememberCoroutineScope의 차이
    - LaunchedEffect
        - 컴포저블의 생명주기(Lifecycle)에 종속된 Coroutine을 실행한다.
        - 키(key)가 바뀌면, 기존 Coroutine을 취소하고 새로운 Coroutine을 재실행한다.
            ```kotlin
            LaunchedEffect(key1) {
                // key1이 바뀔 때마다 이 블록이 재실행됨
                doSomething()
            }
            ```
        - 특징
            - 컴포저블이 Composition에 들어갈 때 실행된다.
            - 컴포저블이 Composition에서 제거될 때 Coroutine도 자동 취소된다.
            - 키가 변경되면 기존 Coroutine을 취소하고 새로운 작업을 시작한다.
            - 주로 Side Effect (예: 네트워크 요청, 애니메이션 트리거 등)에 사용한다.

    - rememberCoroutineScope
        - 컴포저블에 수명(Lifecycle)을 묶은 CoroutineScope를 생성해준다.
        - 코드를 직접 명령형으로 실행하고 싶을 때 사용한다.
        - Scope는 컴포저블이 Composition에서 사라질 때 자동으로 cancel된다.
            ```kotlin
            val coroutineScope = rememberCoroutineScope()
            Button(onClick = {
                coroutineScope.launch {
                    doSomething()
                }
            }) {
                Text("Click Me")
            }
            ```
        - 특징
            - Coroutine이 명시적으로 launch될 때만 실행된다.
            - 컴포저블이 살아있는 한 Scope는 유지된다.
            - 주로 버튼 클릭, 사용자 인터랙션 등 명령형 이벤트 처리에 사용한다.


- onTrimMemory()는 어떤 상황에서 호출되고 주요 레벨 중 몇가지를 예로 들어 설명
    - onTrimMemory()
        - 시스템 메모리가 부족할 때 앱에 메모리를 줄이라고 신호를 보내는 콜백 메서드다.
        - Activity, Service, ContentProvider 등이 이 메서드를 구현할 수 있다.
        ```kotlin
        override fun onTrimMemory(level: Int) {
            when (level) {
                ComponentCallbacks2.TRIM_MEMORY_RUNNING_LOW -> {
                    // 메모리가 부족하니 캐시 줄이기
                }
                ComponentCallbacks2.TRIM_MEMORY_UI_HIDDEN -> {
                    // 앱 UI가 완전히 숨겨졌으니 리소스 정리
                }
            }
        }
        ```

    - 주요 호출 상황
        - 백그라운드 앱이 많거나,
        - 포그라운드 앱이 메모리를 많이 사용할 때,
        - OS가 프로세스를 정리해야 할 때 호출된다.

    - 주요 레벨 예시
        - (1) TRIM_MEMORY_RUNNING_MODERATE
            - 시스템이 메모리 부족을 감지했지만, 심각한 수준은 아님.
            - 앱은 필요 없는 리소스를 조금 줄이면 된다.

        - (2) TRIM_MEMORY_RUNNING_LOW
            - 시스템 메모리가 심각하게 부족한 상태.
            - 앱은 가능한 많은 리소스를 해제해야 한다.

        - (3) TRIM_MEMORY_UI_HIDDEN
            - 앱의 UI가 완전히 사용자 눈에 보이지 않는 상태가 됨. (ex: 앱이 백그라운드로 전환)
            - 이때는 UI 관련 리소스(이미지, 뷰 캐시 등)를 해제해 메모리를 절약할 수 있다.

        - (4) TRIM_MEMORY_COMPLETE
            - 시스템이 메모리 확보를 위해 앱 프로세스를 강제 종료할 수도 있는 심각한 수준.
            - 앱은 최대한 빨리 메모리를 해제해야 한다.

    - 정리
        - LaunchedEffect: 
            - 자동 실행, 키 변화에 따라 재시작 → Side Effect 작업에 적합.
        - rememberCoroutineScope: 
            - 수동 실행, 명령형 이벤트 대응 → 클릭/입력 등 트리거 작업에 적합.
        - onTrimMemory():
            - 시스템 메모리 부족 시 호출,
            - 레벨에 따라 리소스 정리 정도를 조절해야 한다. (예: UI 숨김, 메모리 심각 부족 등)

- Foreground Service를 정상적으로 실행하기 위해 Android 8.0 이상에서 추가로 필요한 작업
    - 배경
        - Android 8.0 (API 26)부터 Background Execution Limits가 도입되면서,
        - 백그라운드 상태에서 바로 일반 Service를 시작하는 것이 금지되었다.
        - 대신, 백그라운드에서 Service를 시작하려면 Foreground Service를 사용해야 하고, 즉시 Notification을 띄워야 한다.

    - 추가로 필요한 작업
        - (1) startForegroundService() 사용
            - 일반 startService() 대신, 반드시 Context.startForegroundService(Intent) 로 Service를 시작해야 한다.
            ```kotlin
            val intent = Intent(this, MyForegroundService::class.java)
            ContextCompat.startForegroundService(this, intent)
            ```

        - (2) Service 내에서 빠르게 startForeground() 호출
            - Service가 시작된 후 5초 이내에 반드시 startForeground() 호출로 Notification을 띄워야 한다.
            - 지연되면 시스템이 ANR (App Not Responding)로 서비스를 강제 종료시킬 수 있음
            ```kotlin
            override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
                val notification = createNotification()
                startForeground(NOTIFICATION_ID, notification)
                return START_STICKY
            }
            ```

- JobScheduler와 WorkManager를 비교할 때, API 23 이상에서 WorkManager를 선호하는 이유
    - JobScheduler
        - Android 5.0 (API 21)부터 도입.
        - OS가 관리하는 백그라운드 작업 예약 시스템.
        - 네트워크 연결 여부, 충전 중 여부 등 조건을 붙여 작업을 예약할 수 있다.

    - WorkManager
        - Android Jetpack 라이브러리 중 하나.
        - 내부적으로 JobScheduler, AlarmManager, Firebase JobDispatcher 등을 상황에 따라 적절히 사용한다.
        - API 14 이상 지원.
        - 앱이 꺼지거나 디바이스가 재부팅되어도 작업을 보장한다.

    - 왜 API 23 이상에서도 WorkManager를 선호하는가? JobScheduler보다 훨씬 신뢰성과 편의성이 높다
        - (1) 더 높은 신뢰성과 일관성
            - WorkManager는 JobScheduler에 비해 백그라운드 작업의 성공 보장이 강력하다.
            - 앱 프로세스가 죽어도, 디바이스가 재부팅돼도 작업이 살아남는다.

        - (2) 다양한 상황 대응
            - WorkManager는 내부적으로 상황에 따라 JobScheduler, AlarmManager, 직접적인 Alarm + Broadcast 등을 적절히 조합해 사용한다.
            - 즉, JobScheduler 단독 사용보다 훨씬 유연하고 견고하다.

        - (3) Chaining, Constraints 지원
            - 여러 작업을 순차적으로 연결(Chaining) 하거나,
            - 네트워크 연결, 충전 여부 등 다양한 제약 조건(Constraints) 을 세밀하게 지정할 수 있다.
            - 복잡한 작업 플로우를 쉽게 관리할 수 있다.

        - (4) API 통합
            - 여러 기기, 다양한 안드로이드 버전에서도 한 가지 API(WorkManager)만 사용하면 되기 때문에 개발과 유지보수가 훨씬 쉬워진다.


- Memory Leak을 방지하기 위해 Fragment에서 ViewBinding을 사용할 때 주의해야 할 점
    - 문제
        - Fragment는 onCreateView() 에서 View를 생성하고, onDestroyView() 에서 View를 파괴한다.
        - 그런데 ViewBinding 객체를 Fragment의 멤버 변수로 계속 참조하고 있으면, View가 파괴된 후에도 메모리에 남아 Memory Leak이 발생할 수 있다.

    - 올바른 ViewBinding 패턴
        - (1) _binding 변수를 nullable로 선언
            - 외부에서는 항상 binding을 통해 접근
            - 내부에서는 _binding을 관리
            ```kotlin
            private var _binding: FragmentHomeBinding? = null
            private val binding get() = _binding!!
            ```

        - (2) onDestroyView()에서 _binding을 null로 해제
            - View가 파괴될 때 반드시 _binding = null 해줘야 뷰에 대한 참조가 끊어지고 GC가 메모리를 회수 가능
            ```kotlin
            override fun onDestroyView() {
                super.onDestroyView()
                _binding = null
            }
            ```

- Android Profiler를 사용할 때 앱의 스레드 덤프(Thread Dump)를 분석하는 상황
    - 스레드 덤프 개념
        - 앱의 모든 스레드 상태(Sleeping, Running, Waiting 등)를 한 번에 스냅샷처럼 저장한 것
        - 각각의 스레드가 어떤 코드에서 무엇을 하고 있는지 기록된다.

    - Thread Dump를 분석해야 하는 상황
        - (1) 앱이 응답하지 않거나 멈췄을 때 (ANR, Hang)
            - UI가 멈췄다면 메인 스레드(Main Thread) 가 무엇을 하고 있는지 확인해야 한다.
            - 긴 작업이 메인 스레드에서 돌고 있으면 ANR(앱 응답 없음)이 발생할 수 있다.

        - (2) Deadlock이나 무한 대기가 의심될 때
            - 여러 스레드가 서로 자원을 기다리면서 멈춰 있는 상태(Deadlock)를 파악할 수 있다.
            - 특정 스레드가 Lock을 잡고 계속 대기하거나 Release하지 않는지 확인한다.

        - (3) 비정상적으로 많은 스레드 생성이 의심될 때
            - 스레드가 비정상적으로 많이 생성되어 메모리를 잡아먹고 있다면,
            - 어떤 스레드가 과도하게 생성되었는지 Thread Dump로 추적할 수 있다.

    - 분석하는 방법
        - Android Studio → Profiler → Threads 탭으로 이동
        - 특정 순간(Freeze, ANR 등) 포착해서 Thread Dump 생성
        - 각 스레드 이름과 스택 트레이스를 분석해서 문제 원인을 찾는다.


- Bitmap 이미지를 메모리 효율적으로 로드하기 위해 사용하는 Android API 또는 라이브러리
    - Android 기본 API
        - BitmapFactory.Options
            - inSampleSize 설정을 통해 원본 이미지 크기를 축소하여 로드.
            - inJustDecodeBounds = true를 먼저 사용해 메모리 할당 없이 이미지 크기만 파악하고, 적절한 축소 비율을 계산 후 로드.
            - inPreferredConfig = Bitmap.Config.RGB_565를 사용하면 기본 ARGB_8888보다 메모리 사용량을 줄일 수 있음 (16bit vs 32bit).

        - ImageDecoder (Android 9, API 28 이상)
            - 고해상도 이미지를 다양한 크기로 효율적으로 디코딩할 수 있음.
            - setTargetSampleSize, setTargetSize 등을 통해 다운샘플링하여 로드 가능.

        - Bitmap.recycle()
            - 사용이 끝난 Bitmap 객체는 명시적으로 recycle() 호출하여 메모리 해제 (단, 주의해서 사용해야 함).

    - 대표 라이브러리
        - Glide
            - 강력한 이미지 로딩 및 캐싱 라이브러리.
            - 디스크 캐시, 메모리 캐시 자동 지원.
            - placeholder, thumbnail, override 등을 통해 리사이즈 및 지연 로딩 최적화 가능.
            - 대용량 이미지도 스크롤 시 부드럽게 처리 가능.

        - Picasso
            - 간단한 코드로 이미지 로딩 가능.
            - 메모리 및 디스크 캐시 기본 제공.
            - 자동으로 이미지 크기를 조정하여 View에 맞춰서 로드.

        - Coil
            - Kotlin 코루틴 기반 경량 이미지 로딩 라이브러리.
            - AndroidX 라이프사이클과 친화적.
            - Glide/Picasso 대비 더욱 가벼운 메모리 사용량을 지향.

    - 요약
        - Android API로는 BitmapFactory.Options + ImageDecoder를 활용
        - 라이브러리로는 Glide가 가장 널리 쓰이며, Coil은 최신 프로젝트에서 경량화를 목표로 많이 채택되고 있다.

- Android Keystore를 사용하는 주요 목적
    - 키(Key) 보안 저장
        - 암호화 키(대칭/비대칭)를 단말 내부의 별도 보호된 영역(Keystore)에 저장.
        - 앱이 직접 키를 가져오지 않고, Keystore를 통해 키를 간접적으로 사용 (키가 메모리에 노출되지 않음).

    - 암호화 및 복호화
        - Keystore에 저장된 키를 사용하여 안전하게 데이터 암호화/복호화 가능.
        - 키를 외부로 노출시키지 않고, 내부적으로만 연산 처리.

    - 인증(Authentication) 연계
        - 지문, 얼굴 인식 등 생체 인증을 통해 키 접근을 제한할 수 있음 (StrongBox 지원 기기에서는 더욱 강화됨).
        - 예를 들어 "사용자가 지문 인증을 해야만 복호화 가능" 같은 보안 시나리오 구현 가능.

    - 키 관리 자동화
        - 키 생성, 저장, 삭제 등을 Android Keystore System이 관리해 줌.
        - 개발자가 직접 파일 시스템이나 SharedPreferences에 민감한 키를 저장하지 않아도 됨.

    - 요약
        - Android Keystore는 "키를 안전하게 보호하고, 앱 외부나 메모리에 노출 없이 암호화/복호화 기능을 제공"하는 것을 주 목적으로 사용한다. 
        - 특히 금융, 인증, 민감 정보 처리가 필요한 앱에서 필수적으로 활용된다.

- Proguard / R8 설정에서 -keepclassmembers 옵션
    - 기본 개념
        - -keepclassmembers는 클래스 전체를 유지하는 것이 아니라, 특정 멤버(필드나 메서드)만 난독화/제거하지 않고 보존하는 옵션이다.
        - 클래스 자체는 최적화나 난독화 대상이 될 수 있지만, 지정된 멤버는 반드시 유지된다.

    - 주요 사용 목적
        - 리플렉션(Reflection) 사용하는 경우 필드나 메서드 이름이 필요할 때 보존.
        - 직렬화/역직렬화(Serialization/Deserialization) 프레임워크 (예: Gson, Moshi)에서 필드 이름이 런타임에 참조될 때 필수.
        - 라이브러리 API에서 명시적으로 노출해야 하는 필드나 메서드만 선택적으로 유지할 때 유용

    - 기본 사용 예시
        ```proguard
        -keepclassmembers class com.example.model.** {
            <fields>;
        }
        ```
        - com.example.model 패키지 하위의 모든 클래스에서 필드만 보존하고 나머지는 최적화 가능.

        ```proguard
        -keepclassmembers class * {
            @com.google.gson.annotations.SerializedName <fields>;
        }
        ```
        - @SerializedName 애노테이션이 붙은 필드만 유지.

    - 주의사항
        - -keepclassmembers는 클래스를 유지하지 않는다는 점 주의해야 함.
        - 만약 클래스가 삭제될 위험이 있다면 -keep이나 -keepclasseswithmembers와 조합 사용해야 함.

    - 요약
        - -keepclassmembers는 클래스는 최적화 대상이 되더라도 특정 필드/메서드만 안전하게 보존하고 싶을 때 사용
        - 리플렉션 기반 라이브러리나 직렬화 처리 시 필수 설정이 된다.

- Dynamic Feature Module을 사용할 시 앱 배포 및 설치 시 장점
    - 기본 개념
        - Dynamic Feature Module(DFM)은 앱을 여러 모듈로 분리하여, 필요한 기능만 "다운로드" 해서 사용할 수 있게 하는 기능
        - Android App Bundle(.aab) 기반 배포 구조에서만 사용할 수 있다.

    - 주요 장점
        - (1) 설치 파일 크기 감소
            - 사용자에게 처음 다운로드되는 APK 크기를 대폭 줄일 수 있음.
            - 초기 설치 시 불필요한 기능(예: 무거운 기능, 특정 국가 전용 기능 등)을 제외하고 최소 구성만 제공.

        - (2) 필요한 시점에 기능 제공
            - 앱 실행 중에도 특정 Dynamic Feature를 필요할 때만 다운로드하고 설치 가능 (On-demand delivery).
            - 예를 들어, "AR 뷰어 기능"을 실제로 필요할 때만 다운로드하는 구조 구현 가능.

        - (3) 맞춤형 기능 제공
            - 사용자별, 디바이스별, 지역별로 맞춤형 기능 다운로드 가능.
            - 예: 특정 국가 사용자에게만 특정 모듈 제공.

        - (4) 업데이트 유연성
            - 개별 Dynamic Module만 업데이트 가능.
            - 전체 앱을 다시 설치하거나 업데이트할 필요 없이 일부 기능만 빠르게 배포 가능.

        - (5) 스토어 최적화
            - Google Play에서는 앱 설치 크기, 업데이트 크기가 작을수록 사용자 경험이 좋아지고 설치 전환율이 증가.
            - Dynamic Delivery는 스토어 최적화(ASO) 측면에서도 긍정적인 효과가 있음.

    - 대표 활용 예
        - 게임 앱: 새로운 스테이지를 클리어할 때마다 새로운 레벨 모듈을 다운로드.
        - 전자상거래 앱: 고화질 3D 뷰어나 대용량 AR 뷰어 기능을 별도 모듈로 분리.
        - 여행 앱: 특정 지역 관련 콘텐츠를 별도 모듈로 제공.

    - 요약
        - Dynamic Feature Module을 사용하면 "앱 설치 용량을 줄이고, 필요한 기능만 동적으로 다운로드하여 사용자 맞춤 경험을 제공" 가능
        - 앱의 경량화, 설치 전환율 향상, 업데이트 유연성을 동시에 얻을 수 있다.


- LazyColumn을 최적화할 때 주의해야 할 점
    - 아이템 키(key) 지정
        - key를 명시하지 않으면, Compose는 position 기준으로 아이템을 구분함.
        - 데이터 변경 시 스크롤 위치나 상태가 깨질 수 있음.
        - 해결: items나 item에서 key를 명시해서 데이터 아이덴티티를 기준으로 관리.
            ```kotlin
            LazyColumn {
                items(items = list, key = { it.id }) { item ->
                    Text(item.name)
                }
            }
            ```
    - 불필요한 recomposition 방지
        - 리스트 내 아이템이 자주 업데이트되면 전체 리스트가 재구성될 수 있음.
        - 개별 아이템이 변경되지 않는다면 Stable 데이터를 사용하거나, remember 등을 활용해 변화 감지 최소화.
        - 데이터 클래스에는 @Immutable 어노테이션을 붙여 immutability를 보장하는 것도 방법.

    - Layout 측정 최적화
        - Modifier.fillMaxWidth() 같은 명시적 크기 설정을 사용하여, Compose가 측정 비용을 줄일 수 있게 돕는다.
        - 크기를 명확히 주지 않으면 매번 측정이 재수행될 가능성이 높아짐.

    - 간결한 Item UI 구성
        - LazyColumn 아이템 안에서는 복잡한 로직이나, 무거운 연산(예: bitmap decode, heavy composable)을 직접 넣지 않는다.
        - 가능한 별도의 Composable 함수로 분리하고, 최적화된 상태로 호출한다.

    - Nested Scrolling 문제 주의
        - LazyColumn 안에 또 다른 Scrollable 컴포넌트가 있으면 성능 저하나 충돌이 발생할 수 있음.
        - 이 경우 nestedScroll 처리나 스크롤 상호작용 조정이 필요하다.

    - 요약
        - LazyColumn 최적화 핵심은 "key를 명시하고, 데이터 변경 범위를 최소화하며, 측정/계산을 가볍게 유지하는 것"

- recomposition을 방지하기 위해 derivedStateOf의 동작 원리
    - 기본 개념
        - derivedStateOf는 State를 기반으로 계산된 새로운 State를 만들되, 실제로 값이 변할 때만 recomposition을 발생시키는 고급 기능이다.
        - 관찰하고 있는 입력 State 값이 변할 때만 재평가된다.

    - 동작 흐름
        - (1) 초기 계산
            - derivedStateOf { } 블록 안에서 값을 한 번 계산함.
        - (2) 입력 State 추적
            - 블록 안에서 참조하는 State를 자동으로 추적한다.
        - (3) 입력 State 변화 감지
            - 참조 중인 State 값이 변하지 않으면, derivedStateOf는 다시 계산하거나 recomposition을 트리거하지 않음.
            - 참조된 State가 변하면, 블록을 다시 실행하여 새로운 값을 계산함.
        - (4) Recomposition 최소화
            - derivedStateOf로 래핑된 값만 바뀌어야 recomposition이 발생한다.
            - 값이 같으면 Compose는 UI를 다시 그리지 않음.
    - 사용 예시
        ```kotlin
        val searchText by remember { mutableStateOf("") }
        val filteredList by remember(searchText) {
            derivedStateOf {
                fullList.filter { it.contains(searchText, ignoreCase = true) }
            }
        }
        ```
        - searchText가 바뀔 때만 filteredList가 재계산된다.
        - fullList는 고정되어 있다면 recomposition을 유발하지 않는다.

    - 주의사항
        - derivedStateOf는 메모리상 캐시처럼 작동하지만, 너무 복잡한 계산을 넣으면 오히려 관리 부담이 생길 수 있다.
        - 불필요하게 많이 중첩해서 사용하지 말고, 진짜 "비용이 크거나, 변화 감지를 최적화할 필요가 있는" 계산에만 사용하는 것이 좋다.

    - 요약
        - derivedStateOf는 "State 기반 연산을 최적화해서, 필요할 때만 recomposition을 발생시키는 스마트한 캐시" 개념이다.
        - 주로 필터링, 정렬, 값 계산 최적화 같은 곳에 사용된다.

- LaunchedEffect와 rememberUpdatedState를 조합해야 하는 상황
    - 핵심 개념
        - LaunchedEffect는 컴포지션 시점에 Coroutine을 시작하는 데 사용
        - LaunchedEffect 안에서 참조하는 값이 변경될 경우,
            - → LaunchedEffect는 재시작돼야 하지만
            - → 기존 코루틴은 취소되고 새로 시작됨
        - 이를 막고 싶을 때 rememberUpdatedState를 사용해 "최신 값을 참조만" 하게 만들 수 있음

    - 조합해야 되는 시기
        - LaunchedEffect는 키 변경 없이 그대로 유지하고 싶고, 내부에서 참조하는 값만 항상 최신으로 유지하고 싶을 때.
        - 대표적인 상황:
            - 콜백 함수나 외부 상태가 바뀌더라도
            - LaunchedEffect 자체는 재시작하지 않고,
            - 최신 상태를 반영만 하고 싶을 때.

    - 예시
        ```kotlin
        @Composable
        fun MyComposable(onEvent: () -> Unit) {
            val latestOnEvent = rememberUpdatedState(newValue = onEvent)

            LaunchedEffect(Unit) { // 키를 Unit으로 고정 = 재시작 방지
                while (true) {
                    delay(1000)
                    latestOnEvent.value() // 항상 최신 onEvent 호출
                }
            }
        }
        ```
        - 포인트:
            - LaunchedEffect(Unit) → 재시작 안 함
            - rememberUpdatedState(onEvent) → onEvent가 변경돼도 항상 최신 값을 사용

    - 정리
        - LaunchedEffect: 컴포지션 시점에 코루틴 시작, 키 변경 시 재시작
        - rememberUpdatedState: 키는 고정하고, 참조하는 값만 최신으로 유지

- Modifier.recomposeHighlighter()를 사용할 시 장점
    - 핵심 개념
        - Modifier.recomposeHighlighter()는 컴포저블이 Recomposition(다시 그리기)될 때 화면에 깜빡이는 하이라이트 효과를 보여준다
        - 즉, 어떤 컴포저블이 자주 다시 그려지는지 시각적으로 확인할 수 있는 디버깅 툴

    - 장점
        - 불필요한 Recomposition을 바로 눈으로 파악할 수 있다.
        - 최적화 포인트를 빠르게 찾을 수 있다.
        - 코드만 봐서는 알기 힘든 부분을 시각적으로 분석할 수 있다.

    - 예시
        ```kotlin
        Box(
            modifier = Modifier
                .size(100.dp)
                .background(Color.Blue)
                .recomposeHighlighter() // Recomposition 발생 시 깜빡임
        )
        ```
        - 이 Box가 리컴포즈될 때마다 화면이 잠깐 깜빡인다.
        - 깜빡임이 자주 발생한다면 → 불필요한 상태 변화나 recomposition 의심 가능.

- Compose Navigation에서 ViewModel을 안전하게 공유하기 위한 방법
    - [공유 ViewModel의 목적]
        - 여러 Composable(Screen) 간에 상태를 유지하고 공유하고 싶을 때 필요
        - 예: A → B → C 로 이동하면서 하나의 ViewModel로 데이터 공유

    - [문제점]
        - viewModel()을 각 Composable에서 개별 호출하면 ViewModel이 재생성되거나 스코프가 달라져 공유되지 않음
        - 특히 NavGraphBuilder.composable() 내부에서 viewModel() 호출 시 기본은 그 Composable에 종속된 ViewModelStoreOwner를 따름

    - [해결 방법]
        - (1) hiltViewModel() + Navigation Graph ViewModel 사용
            ```kotlin
            val sharedViewModel: SharedViewModel = hiltViewModel(navController.getBackStackEntry("routeA"))
            ```
            - getBackStackEntry("routeA")를 통해 "routeA를 기준으로 생성된 ViewModel"을 하위 화면에서 안전하게 재사용 가능
            - routeA는 해당 ViewModel을 처음 생성한 screen의 route명

        - (2) activityViewModel() 혹은 sharedViewModel() (비권장 또는 제한적)
            - 전체 액티비티 스코프에서 공유하는 방식이지만,
            - 복잡한 구조에서는 데이터 오염 위험이 있어, 보통은 BackStackEntry 기반 접근이 더 권장됨

    - [주의사항]
        - 반드시 NavController의 route가 back stack에 존재해야 함
        - Dialog, BottomSheet처럼 backstack에 올라가지 않는 경우에는 공유 불가


- remember 대신 rememberSaveable을 써야 하는 대표적인 상황
    - [차이점 요약]
        - remember: 상태를 메모리에만 저장 → 프로세스가 유지될 때만 복원됨
        - rememberSaveable: 상태를 Bundle에 저장 → Activity 재생성(예: 회전, 백그라운드 후 복귀) 시에도 복원됨

    - [rememberSaveable이 필요한 대표적 상황]
        - (1) 화면 회전 시 상태 유지
            - 예: TextField 입력값, 선택된 탭 인덱스 등
            - 화면 회전하면 remember는 초기화되지만, rememberSaveable은 값 유지됨

        - (2) 시스템에 의한 프로세스 kill 후 재생성
            - 예: 사용자가 앱을 백그라운드로 뒀다가 오래 지나 다시 열었을 때
            - remember는 데이터가 사라지고, rememberSaveable은 복원됨

        - (3) Form 입력 단계
            - 여러 화면을 이동하며 입력할 때, 임시 상태를 유지해야 하는 상황 (예: 회원가입, 주문 정보 작성)

    - [주의사항]
        - 저장 가능한 타입이어야 함 (Bundle에 저장 가능한 기본 타입 or Saver 제공)
        - 커스텀 객체는 Saver를 별도로 정의해야 함

    - 요약
        - ViewModel 공유는 NavBackStackEntry 기준으로 hiltViewModel(backStackEntry) 사용이 가장 안전

        - 사용자가 화면을 회전하거나 백그라운드에서 앱이 재생성되더라도 상태를 복원하고 싶다면 반드시 rememberSaveable 사용

- LaunchedEffect(Unit) 취소 시점
    - [핵심 개념]
        - LaunchedEffect(Unit)은 Composable이 Composition에 진입할 때 실행되고 Composable이 Composition에서 벗어날 때(cancel) 자동으로 취소된다.

    - [취소되는 시점]
        - 해당 Composable이 사라지거나 recomposition에서 제외될 때
        - Unit을 key로 썼기 때문에, 다시 실행되는 일은 없고, 해당 Composable이 제거될 때 한 번만 취소됨

    - [예시 상황]
        - if (isVisible) 조건 안에서 Composable을 보여주고 있는데
        - isVisible이 false로 바뀌면 해당 LaunchedEffect(Unit)도 종료됨

    - [주의]
        - LaunchedEffect(someKey)로 key를 바꾸면, key가 변경될 때마다 기존 코루틴이 취소되고 재시작된다.
        - (이건 재시작, 위의 Unit은 종료)

- derivedStateOf의 핵심 역할
    - [핵심 기능]
        - Compose에서 계산된 상태(derived state)를 메모이징해서 불필요한 recomposition을 방지하는 데 사용된다.

    - [사용 시점]
        - 어떤 State를 기반으로 파생된 값을 계산할 때, 그 파생 값이 의미 있는 변경이 있을 때만 recomposition되게 하고 싶을 때

    - [예시]
        ```kotlin
        val list by remember { mutableStateOf(listOf(1, 2, 3)) }
        val evenCount by remember {
            derivedStateOf { list.count { it % 2 == 0 } }
        }
        ```
        - list가 변경되지 않으면 evenCount는 다시 계산되지 않는다
        - 즉, 불필요한 recomposition 방지 + 성능 최적화

    - [비교]
        - 그냥 val derived = list.count { ... }면 recomposition마다 재계산됨
        - derivedStateOf는 값이 실제로 변경될 때만 recomposition을 유발

- key를 설정하지 않고 LazyColumn을 사용할 경우 발생할 수 있는 문제
    - [문제 원인]
        - LazyColumn은 내부적으로 item content를 재사용(reuse) 하기 때문에 고유한 key 없이 index로만 item을 추적하면 순서가 바뀌거나 삭제/추가 시 잘못된 recomposition이 발생할 수 있음

    - [대표적인 문제들]
        - 스크롤 위치가 튐
        - 아이템 애니메이션이 잘못됨 (예: 삭제인데 다른 아이템이 사라짐)
        - 상태가 섞임 (예: 체크박스 상태가 엉뚱한 곳에 적용)

    - [해결 방법]
        - 반드시 stable하고 unique한 key를 제공해야 함
        ```kotlin
        items(list, key = { it.id }) { item ->
            Text(item.name)
        }
        ```
    
    - 전체 정리
        - LaunchedEffect(Unit)은 해당 Composable이 Composition에서 제거될 때 취소된다.
        - derivedStateOf는 파생 상태 계산을 메모이징해 불필요한 recomposition을 줄이는 최적화 도구다.
        - LazyColumn에서 key 없이 사용하면 스크롤 위치 튐, 상태 섞임, 잘못된 애니메이션 등의 문제가 생긴다.

- rememberCoroutineScope()로 launch한 코루틴 자동 취소 시점
    - [핵심 개념]
        - rememberCoroutineScope()는 Composable의 Composition 범위에 종속되지 않음
        - 즉, LaunchedEffect와 달리 Composable이 제거돼도 자동 취소되지 않음

    - [취소 시점]
        - 자동으로는 취소되지 않는다
        - 직접 관리해야 한다 (Job.cancel() 등)

    - [사용 시점]
        - 버튼 클릭 같은 UI 이벤트에서 코루틴을 일시적으로 실행하고 싶을 때
        ```kotlin
        val scope = rememberCoroutineScope()
        Button(onClick = {
            scope.launch {
                doSomething()
            }
        }) { ... }
        ```

    - [주의사항]
        - 오래 지속되거나 ViewModel 단위로 관리해야 할 경우에는 ViewModelScope 사용이 적절함
        - rememberCoroutineScope()는 메모리 누수 주의가 필요함

- Compose에서 recomposition 발생을 디버깅하기 위한 방법
    - [디버깅 방법]
        - (1) Modifier.recomposeHighlighter()
            - 리컴포지션 시 깜빡이며 시각적으로 확인 가능 (디버깅 전용)
            ```kotlin
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .recomposeHighlighter()
            )
            ```

        - (2) Log.d() 사용
            - Composable 내부에 Log.d()로 컴포지션 확인

        - (3) @Stable, @Immutable 확인
            - 리컴포지션 과다 발생 시 data class나 parameter에 불필요한 변화가 있는지 확인
            - 안정을 위한 주석과 data 구조 리팩토링 고려

- rememberUpdatedState()는 사용 시점
    - [기본 개념]
        - LaunchedEffect, DisposableEffect 등과 같이 Compose scope 내에서 오래 지속되는 작업에서 "최신 값을 참조" 해야 할 때 사용

    - [필요 이유]
        - Compose에서는 Effect 블록이 초기 Composition 시점의 값을 캡처하기 때문에 이후 변경된 값을 알 수 없음

    - [사용 시점 예시]
        ```kotlin
        @Composable
        fun MyScreen(onEvent: () -> Unit) {
            val currentOnEvent = rememberUpdatedState(onEvent)

            LaunchedEffect(Unit) {
                delay(2000)
                currentOnEvent.value() // 항상 최신 콜백을 참조
            }
        }
        ```

    - [정리]
        - 외부 값이 바뀌더라도 Effect 블록 자체는 재시작되지 않고, 내부에서 참조하는 값만 항상 최신으로 유지하고 싶을 때 사용

- Modifier.graphicsLayer를 사용할 때 주의할 점
    - [문제 원인]
        - graphicsLayer는 Modifier.drawLayer의 저수준 API
        - 성능과 시각 효과 측면에서 강력하지만 하드웨어 레이어를 생성하므로 렌더링 비용이 증가할 수 있음.

    - [대표적인 문제들]
        - 불필요한 레이어 생성으로 UI 렌더링 성능 저하
        - 자식 Composable이 과도하게 overdraw되는 현상
        - alpha, scale, translation 등의 속성 적용 시 의도치 않은 clipping 또는 시각적 오류 발생

    - [해결 방법]
        - 시각적 효과(예: fade, transform)가 정말 필요한 경우에만 사용
        - 애니메이션이나 변형 효과를 넣을 때는 Modifier.graphicsLayer 대신 
        - Modifier.alpha, Modifier.scale, Modifier.offset 등 Compose 기본 Modifier 우선 고려

- CompositionLocalProvider를 남발할 경우 문제가 되는 이유
    - [문제 원인]
        - CompositionLocal은 전역 상태를 계층적으로 전달하는 강력한 도구
        - 남발하면 상태 관리가 불투명해지고 성능 문제도 발생할 수 있음.

    - [대표적인 문제들]
        - 구조가 복잡해짐: 어떤 값이 어디서 바뀌는지 추적 어려움
        - 성능 저하: CompositionLocal 값이 변경되면 하위 전체 recomposition 발생
        - 테스트/유지보수 어려움: 명시적 파라미터가 아닌 암묵적 상태 전달이 많아지면 컴포저블 재사용성 저하

    - [해결 방법]
        - 꼭 계층적 상태 전달이 필요한 경우에만 사용
        - 일반적인 데이터 전달은 state hoisting으로 처리
        - CompositionLocal은 테마, 다크모드, 로케일, 디바이스 정보처럼 컨텍스트성 전역 상태 전달에 국한

- Composable 함수에 key1, key2를 걸고 LaunchedEffect(key1, key2)를 걸었을 때, 둘 중 하나라도 바뀔 시 발생하는 것
    - [동작 원리]
        - LaunchedEffect(key1, key2)는 key1 또는 key2 중 하나라도 변경되면 
        - 기존 코루틴을 취소하고 새 코루틴을 실행함.

    - [대표적인 동작]
        - 이전 LaunchedEffect 블록 내 코루틴은 CancellationException으로 중단됨
        - 새로운 LaunchedEffect 블록이 재실행됨
        - 상태 관찰, 이벤트 수신 등에서 재구독이 일어날 수 있음

    - [주의사항]
        - key를 잘못 설정하면 불필요한 코루틴 재시작
        - side effect 동작은 key 변화에 따라 정확하게 한 번만 실행되도록 보장해야 함

    - [해결 방법]
        - key1, key2는 정말로 side effect 실행 조건에 해당하는 값만 넣을 것
        - 불필요한 재실행 방지를 위해 derivedStateOf + snapshotFlow 사용 고려

- Compose에서 상태 호이스팅(State Hoisting)
    - [정의]
        - 상태(state)를 Composable 내부가 아닌 외부에서 소유하고, 
        - Composable은 그 상태를 입력값(파라미터)으로 받고, 변경은 콜백을 통해 요청하는 구조를 의미함.

    - [도입 배경]
        - 재사용성 향상: 내부 상태를 갖지 않기 때문에 다양한 상황에서 재사용 가능
        - 테스트 용이: 외부에서 상태를 주입받으므로 단위 테스트가 쉬움
        - 단방향 데이터 흐름(One-way data flow)을 유지해 버그 감소, 예측 가능한 UI 동작 유도

    - [대표적인 문제들] (상태 호이스팅이 없을 경우)
        - Composable 내부에 remember로 상태를 관리하면,
            - 외부에서 값을 제어하기 어려움
            - 동기화 안 된 상태로 인해 UI 버그 발생 가능
            - 다른 Composable과 상태 공유 어려움

    - [상태 호이스팅 기본 구조 예시]
        ```kotlin
        // 상태는 외부에서 주입받고, 변경은 콜백을 통해 요청
        @Composable
        fun MySwitch(
            isChecked: Boolean,
            onCheckedChange: (Boolean) -> Unit
        ) {
            Switch(
                checked = isChecked,
                onCheckedChange = onCheckedChange
            )
        }

        // 외부에서 아래와 같이 호출하여 사용
        var checked by remember { mutableStateOf(false) }

        MySwitch(
            isChecked = checked,
            onCheckedChange = { checked = it }
        )
        ```
    - [요약]: Compose의 권장 패턴, 복잡한 UI에서의 유지보수성과 테스트성 향상의 핵심
        - Composable은 상태를 소유하지 말고 받아라
        - 변경은 콜백으로 위임하라
        - 단방향 흐름을 지켜라

- Compose에서 animation API를 활용할 때 발생할 수 있는 성능 문제와 해결책
    - [문제 원인]
        - animate*AsState, updateTransition, AnimatedVisibility 등의 애니메이션 API는
        - 내부적으로 Frame-by-Frame recomposition이나 Layout Pass 재요청을 발생시킬 수 있음.

    - [대표적인 문제들]
        - 불필요한 recomposition으로 인한 UI 렌더링 부담
        - 오브젝트 재생성 비용 증가 (예: 애니메이션 대상 값이 복잡한 객체일 경우)
        - 중첩된 애니메이션 또는 LazyColumn 내 사용 시 jank 발생 가능성

    - [해결 방법]
        - animate*AsState 대상은 가급적 Primitive 타입 또는 immutable 객체 사용
        - AnimatedVisibility는 간단한 UI에만 사용, 복잡한 경우 Transition 기반 커스텀 애니메이션 고려
        - 애니메이션 대상 Composable은 key 또는 derivedStateOf 등으로 불필요한 recomposition 차단

- Jetpack Compose에서 rememberCoroutineScope를 사용할 때 주의해야 할 점
    - [문제 원인]
        - rememberCoroutineScope()는 Composition과 함께 생명주기를 가지며, 
        - 수동으로 관리하지 않으면 코루틴이 뷰가 사라진 후에도 살아남을 수 있음.

    - [대표적인 문제들]
        - 메모리 누수(leak): Composable이 사라졌는데 코루틴은 계속 실행 중
        - 중첩 Composable에서 여러 Scope 생성 시 의도치 않은 동시성 문제

    - [해결 방법]
        - 실제로 Composable의 수명과 정확히 일치하는 작업은 LaunchedEffect 사용 우선
        - rememberCoroutineScope는 사용자 상호작용 기반(one-shot 이벤트 처리) 등에만 제한적으로 사용
        - DisposableEffect 등을 활용해 scope 사용 후 정리 필요 시 정리 로직 명시

- Compose에서 LazyColumn의 성능을 최적화하는 방법
    - [문제 원인]
        - LazyColumn은 화면에 보여지는 아이템만 Compose하지만, 
        - 내부 상태 관리, recomposition, 측정 등에서 성능 병목 발생 가능

    - [대표적인 문제들]
        - key 없이 사용 시 아이템 변경 시 잘못된 recomposition 또는 스크롤 위치 튐
        - 무거운 Composable을 리스트 안에서 직접 호출
        - 애니메이션 중첩, Modifier 조합 과다

    - [해결 방법]
        - items(items, key = { it.id }) 형태로 stable하고 unique한 key 제공
        - 아이템 Composable은 @Composable fun ItemRow(...)처럼 분리하고 재사용 가능하게 구성
        - LazyColumn 내부의 상태나 애니메이션은 반드시 성능을 고려해 최소화
        - 이미지 등은 AsyncImage, rememberImagePainter + contentScale.Crop 등 최적화 적용

- Compose에서 MutableState와 ImmutableState의 차이점
    - [개념 차이]
        - MutableState<T>: 값이 바뀌면 Compose가 자동으로 recomposition
        - ImmutableState (예: val state = remember { derivedStateOf { ... } }): 읽기 전용 뷰, 외부에서는 값을 변경할 수 없음

    - [용도 차이]
        - MutableState는 UI 변경을 트리거하는 값
        - derivedStateOf 기반 State<T>는 계산된 상태로 성능 최적화 목적

    - [주의사항]
        - MutableState는 지나치게 많이 생성하면 불필요한 recomposition 초래
        - 직접 노출하지 말고 viewModel -> UI로는 Immutable 형태로 전달하는 구조 권장

    - [패턴]
        ```kotlin
        // ViewModel
        private val _isVisible = mutableStateOf(false)
        val isVisible: State<Boolean> get() = _isVisible
        ```

- LaunchedEffect, DisposableEffect 설명 및 LaunchedEffect 대신 DisposableEffect로 다 대체해도 문제없는지에 대한 설명
    - LaunchedEffect
        - [정의]
            - Composable이 composition될 때 코루틴을 실행할 수 있도록 하는 API.
            - 지정된 key가 변경되면 기존 코루틴을 자동으로 취소하고 새로 시작함.

        - [주 사용 사례]
            - 화면 진입 시 초기 로직 실행
            - 상태 변경 시 네트워크 요청, 애니메이션 시작 등 비동기 작업 수행
            - collect, delay, launch 기반의 작업 처리

        - [예시]
            ```kotlin
            LaunchedEffect(Unit) {
                delay(1000)
                viewModel.fetchData()
            }
            ```

    - DisposableEffect
        - [정의]
            - Composable이 composition될 때 리소스를 생성하고, 
            - composition이 종료될 때 해당 리소스를 정리하는 용도의 API

        - [주 사용 사례]
            - 리스너 등록/해제
            - 콜백, 브로드캐스트 수신 등록
            - 리소스나 참조 해제 로직 (onDispose { ... })

        - [예시]
            ```kotlin
            DisposableEffect(key1 = context) {
                val listener = SomeListener()
                registerListener(listener)
                onDispose {
                    unregisterListener(listener)
                }
            }
            ```

    - LaunchedEffect를 DisposableEffect로 전부 대체 가능한지?
        - [결론]
            - 불가능하며 적절한 용도 구분이 필요
        - [이유]
            - LaunchedEffect는 코루틴 실행을 위한 API, DisposableEffect는 리소스 정리를 위한 API
            - DisposableEffect에서는 suspend 함수를 호출할 수 없음 → 비동기 로직 실행 불가
            - LaunchedEffect는 rememberCoroutineScope() 없이도 키 변경에 따라 자동 관리되는 scope를 제공

    - [정리 요약]
        - LaunchedEffect: 비동기 처리 / 코루틴 실행용
        - DisposableEffect: 등록/해제 / 정리용 (side-effect 해제)
        - 서로 용도가 완전히 다르므로 대체 불가이며, 각 목적에 맞게 사용해야 Compose 생명주기에 맞는 안정적인 동작이 보장됨

- LaunchedEffect와 DisposableEffect를 하나의 Composable 함수 내에서 같이 사용할 때의 현상
    - [동작 구조]
        - LaunchedEffect와 DisposableEffect는 각각 별도의 Composition 트리 lifecycle에 따라 작동
        - 둘 다 같은 Composable 내에 존재하더라도 독립적으로 관리되며, 서로 간섭하지 않음
        - key가 같다면 각자 해당 key의 변경 여부에 따라 작동함

    - [공존할 때의 실제 현상]
        - Composable이 처음 composition될 때:
            - DisposableEffect → effect 실행 후 onDispose 등록됨
            - LaunchedEffect → 코루틴 시작

        - key가 변경될 때:
            - 두 effect의 key가 동일하면:
                - DisposableEffect → onDispose 먼저 실행 → 새로운 effect 재실행
                - LaunchedEffect → 기존 코루틴 자동 취소 → 새 코루틴 시작

        - Composable이 composition에서 제거될 때:
            - DisposableEffect.onDispose → 호출됨
            - LaunchedEffect의 코루틴 → CancellationException으로 종료됨

    - [주의사항]
        - DisposableEffect는 즉시(onDispose) 실행
        - LaunchedEffect는 코루틴 내부에서 순차적으로 실행되므로
        - 둘 다 동일한 자원을 다룰 경우 작업 순서 및 동기화 문제 주의
        - 예: DisposableEffect에서 리소스 해제 후, 
        - LaunchedEffect에서 접근하면 NullPointerException 발생 가능

    - [실제 사용 예시]
        ```kotlin
        @Composable
        fun ExampleComposable(id: String) {
            DisposableEffect(id) {
                val listener = registerSomeCallback()
                onDispose {
                    unregisterSomeCallback(listener)
                }
            }

            LaunchedEffect(id) {
                // suspend 함수 실행 가능
                delay(500)
                fetchData(id)
            }
        }
        ```
    - [요약 정리]
        - LaunchedEffect와 DisposableEffect는 같은 Composable에서 공존 가능하며, 독립적으로 동작
        - 동일한 key를 공유하더라도 각자의 역할(코루틴 vs 리소스 해제)은 분리되어 관리됨
        - 단, 동일 자원 접근 시 순서 주의 필요

- LaunchedEffect와 DisposableEffect 중 먼저 실행되는 것
    - [정확한 실행 순서]
        - DisposableEffect가 먼저 실행된다.
        - Compose의 내부 동작 순서상 DisposableEffect는 composition 단계에서 즉시 실행되며,
        - LaunchedEffect는 composition이 끝난 후 Frame 시점에 코루틴으로 예약되어 실행됨.

    - [이유 및 배경]
        - DisposableEffect는 SideEffect 계열 중에서도 composition 시점의 리소스 등록 및 정리 용도
        - LaunchedEffect는 composition이 완료된 후에 실제로 CoroutineScope.launch로 코루틴을 시작

    - [실제 예시 흐름]
        ```kotlin
        @Composable
        fun Example(id: String) {
            DisposableEffect(id) {
                println("DisposableEffect 실행")
                onDispose {
                    println("DisposableEffect onDispose 실행")
                }
            }

            LaunchedEffect(id) {
                println("LaunchedEffect 실행")
            }
        }
        // 출력 결과
        // DisposableEffect 실행
        // LaunchedEffect 실행

        // 만약 id가 바뀌어서 recomposition이 발생하면:
        // DisposableEffect onDispose 실행 (기존 리소스 정리)
        // DisposableEffect 실행 (새 리소스 등록)
        // LaunchedEffect 실행 (새 코루틴 실행)
        ```
    - [요약 정리]
        - DisposableEffect는 항상 먼저 실행됨
        - LaunchedEffect는 composition 이후 다음 Frame에 코루틴으로 실행
        - 리소스 해제 → 재설정 → 코루틴 시작 순서를 의도한 대로 설계해야 안정성 확보

- Jetpack Compose의 Layout 코드를 최적화하는 방법
    - [문제 원인]
        - 중첩된 Layout (Column > Row > Box > ...) 구조가 깊어지면 측정, 배치, 그리기 비용 증가
        - 불필요한 recomposition이 빈번히 발생하면 프레임 드롭 가능

    - [대표적인 비효율 사례]
        - 너무 많은 Box, Row, Column 중첩
        - Modifier.padding().background().padding() 등 중복 Modifier 사용
        - 재사용 불가능한 Layout 구성
        - remember 없이 매 recomposition 시 객체 생성

    - [최적화 방법]
        - Modifier.layoutId, Modifier.zIndex, Modifier.graphicsLayer 등은 꼭 필요할 때만
        - Layout, SubcomposeLayout을 통한 커스텀 배치로 중첩 최소화
        - Modifier.combinedClickable 등 결합 가능한 Modifier 사용
        - remember, derivedStateOf로 계산 최소화
        - 무거운 연산은 LaunchedEffect, produceState 등 비동기 처리로 분리

- Jetpack Compose에서 동적 리스트 아이템을 효율적으로 렌더링하는 방법
    - [문제 원인]
        - 리스트 아이템이 자주 바뀌거나 삭제/추가되면 key가 없을 경우 재조합 오류
        - 무거운 Composable이 리스트 내에 직접 들어가면 불필요한 리소스 소모

    - [비효율 사례]
        - LazyColumn { items(list) { ... } } 에서 key 없이 사용
        - 리스트 내부에서 직접 Image(bitmapFromUrl(url)) 등 무거운 작업 수행
        - 리스트 아이템마다 새로운 remember {} 호출

    - [효율적 렌더링 방법]
        - items(items = list, key = { it.id }) 형태로 stable key 사용
        - 복잡한 아이템은 @Composable fun ListItem(...)처럼 재사용 가능한 함수로 분리
        - LazyColumn 내 상태는 remember 대신 상위에서 전달받아 stateless하게 구성
        - 비동기 이미지 로딩은 AsyncImage, rememberImagePainter 사용
        - Paging3 + LazyPagingItems로 페이지 단위 렌더링 적용도 고려

- Jetpack Compose에서 SnapshotStateList와 일반 List의 차이점
    - [개념 차이]
        - List<T>: 불변형 또는 변경 감지되지 않는 일반 리스트, Compose는 이 변경을 감지하지 못함
        - SnapshotStateList<T>: Compose의 State 시스템과 연결된 리스트, 변경 시 recomposition 자동 유도

    - [주요 동작 차이]
        - List.add(), List.remove()는 Compose에서 UI 갱신되지 않음
        - SnapshotStateList.add()는 자동으로 recomposition 트리거

    - [사용 시점]
        - UI 리스트가 동적으로 변하고, UI가 해당 변화를 즉시 반영해야 할 때 mutableStateListOf() 사용
        - 외부에서 immutable하게 리스트를 전달할 때는 List<T> suffices

    - [주의사항]
        - SnapshotStateList는 mutable 상태이므로 직접 노출 금지
        - → ViewModel 등에서 val list: List<T> get() = _stateList 식으로 읽기 전용 노출 권장

- Jetpack Compose에서 ConstraintLayout을 활용하는 이유
    - [기본 개념]
        - ConstraintLayout은 Compose에서도 복잡한 상대적 위치 지정이 필요한 경우 사용하는 고급 레이아웃 도구

    - [활용 이유]
        - Column, Row, Box로는 구현하기 어려운 상대적 제약 관계를 설정할 수 있음
        - 다중 요소의 정렬, 비율 기반 배치, 바깥 여백 유지 등의 복잡 레이아웃 구현에 적합

    - [대표적인 사용 시점]
        - 정확한 위치와 정렬 제어가 필요한 UI
        - 가로/세로 중앙 정렬, 비율 유지, 고정 마진/간격 등이 조합된 복잡한 디자인
        - 기존 XML ConstraintLayout을 마이그레이션할 때

    - [주의사항]
        - ConstraintLayout은 성능은 뛰어나지만 오버킬일 수 있으므로 간단한 UI는 기본 레이아웃으로 충분
        - ConstraintSet을 사용하면 동적 제약 조건 구성 가능

- Compose의 Recomposer 내부 구조와 실행 방식
    - [Recomposer 개념]
        - Compose의 렌더링 엔진 핵심 컴포넌트
        - 변경된 상태를 감지하고 해당 Composable을 재구성(Recomposition)하는 역할을 함

    - [내부 구조]
        - Recomposer는 Snapshot 시스템과 연결되어 있음
        - State가 변경되면 Snapshot이 이를 감지하고 → Recomposer가 해당 Composable scope에 재구성 요청

    - [실행 방식]
        - State 변경 → Compose runtime이 Snapshot을 통해 변경 감지
        - Recomposer는 변경된 Composable scope를 재실행 대상으로 큐에 추가
        - Main thread에서 순차적으로 recomposition 실행
        - 필요 시 layout → draw 단계로 UI 업데이트

    - [중요 개념]
        - 재조합은 필요한 부분만 수행 (Composable 단위로 granularity(세분성) 있음)
        - 무한 recomposition 방지를 위해 정상 종료 또는 안정된 상태 보장 필요

- Jetpack Compose의 produceState는 어떤 경우에 유용한가
    - [기본 개념]
        - produceState는 비동기 데이터를 State로 변환할 때 사용하는 Composable Scope API
        - 내부에서 CoroutineScope를 제공하며, 데이터를 State<T>로 자동 제공함

    - [사용 시점]
        - 비동기 API 호출 결과를 Compose UI 상태로 바인딩할 때
        - ViewModel 없이 단일 Composable에서 간단히 사용할 때
        - 상태 캐싱이 필요 없는 경우

    - [예시]
        ```kotlin
        @Composable
        fun WeatherWidget(city: String) {
            val weather by produceState(initialValue = "Loading...", city) {
                value = fetchWeather(city) // suspend fun
                // 뷰모델 없이 단일 컴포저블에서 간단히 사용 시 유용
            }

            Text(text = weather)
        }
        ```
    
    - [장점]
        - LaunchedEffect보다 직관적으로 상태 + 로직을 통합할 수 있음
        - remember 없이도 자동 State 제공 + recomposition 유도

    - [주의사항]
        - 상태 저장이 필요한 경우엔 ViewModel + mutableStateOf() 패턴이 더 적합
        - produceState는 내부적으로 launch되므로 정리 코드 필요 시 DisposableEffect 병행 고려


- Compose에서 Slot API를 활용하여 UI를 구성하는 방법
    - [Slot API]
        - 부모 Composable이 자식 UI를 파라미터(Composable lambda)로 전달받아 
        - 원하는 위치에 삽입하는 구성 방식
        - UI 재사용성과 확장성을 높이는 Compose의 핵심 디자인 패턴

    - [사용 예시]
        ```kotlin
        @Composable
        fun CustomCard(
            title: String,
            content: @Composable () -> Unit
        ) {
            Column {
                Text(text = title)
                content() // Slot 영역
            }
        }

        CustomCard(title = "공지") {
            Text("이곳은 사용자 정의 영역입니다")
        }
        ```

    - [활용 이유 및 장점]
        - UI 컴포넌트 재사용: 고정 레이아웃 + 유동 콘텐츠 혼합 가능
        - 컴포저블 조합 가능성 증가: Scaffold, AlertDialog, BottomSheetScaffold 등 내부도 Slot API 사용

    - [Best Practice]
        - Slot은 @Composable () -> Unit 또는 @Composable () -> T 형태로 명시
        - 여러 Slot이 필요한 경우, 명확하게 이름 구분: topBar, content, actions 등

- Jetpack Compose에서 UI Test를 수행하는 방법과 Best Practice
    - [기본 도구]
        - androidx.compose.ui.test.junit4.createComposeRule 사용
        - composeTestRule.setContent { ... }로 테스트 대상 UI 정의
        - onNodeWithText(), onNodeWithTag() 등으로 UI 요소 선택 및 검증

    - [기본 예시]
        ```kotlin
        @get:Rule
        val composeTestRule = createComposeRule()

        @Test
        fun myButton_click_changesText() {
            composeTestRule.setContent {
                MyComposable()
            }

            composeTestRule.onNodeWithText("Click me").performClick()
            composeTestRule.onNodeWithText("Clicked!").assertIsDisplayed()
        }
        ```

    - [Best Practice]
        - Modifier.testTag("myTag")를 사용해 테스트 대상 명확하게 식별
        - 사용자 플로우 테스트는 SemanticsMatcher 조합으로 시나리오 구성
        - 비동기 작업이 포함된 경우 waitUntil, idle, runOnIdle 등 사용해 안정화
        - 테스트 명은 행동 기반으로 구체적으로 작성 (예: loginButton_showsError_whenFieldsEmpty())

- Jetpack Compose에서 Theme와 Material 3를 활용하는 방법
    - [기본 개념]
        - MaterialTheme은 앱 전반의 색상(ColorScheme), 타이포그래피(Typography), 쉐이프(Shape)를 관리하는 테마 시스템
        - Material 3는 Dynamic Color, adaptive theming, 새로운 component 스타일 등을 지원

    - [설정 예시]
        ```kotlin
        @Composable
        fun MyAppTheme(content: @Composable () -> Unit) {
            val colorScheme = dynamicLightColorScheme(LocalContext.current) // or custom
            MaterialTheme(
                colorScheme = colorScheme,
                typography = Typography,
                shapes = Shapes,
                content = content
            )
        }

        @Composable
        fun MyScreen() {
            MyAppTheme {
                Surface { Text("Hello") }
            }
        }
        ```

    - [활용 포인트]
        - MaterialTheme.colorScheme.primary 등으로 색상 참조
        - 다크모드 대응: isSystemInDarkTheme()로 조건 분기
        - Dynamic Color는 Android 12 이상에서 dynamicLightColorScheme() 등으로 적용

    - [Best Practice]
        - 앱 전역에 공통 Theme 적용하고, 하위 컴포넌트는 Theme 기반 속성 사용
        - 직접 색상/스타일을 하드코딩하지 말고 MaterialTheme 참조 사용
        - Preview에서도 MyAppTheme {}로 감싸 테스트

- Compose에서 Preview 기능을 활용할 때 발생할 수 있는 문제
    - [문제 원인]
        - @Preview는 Android Studio 내에서 UI 렌더링을 위한 디자인 시뮬레이션 도구로, 일반적인 Compose 환경과 다소 차이가 있음

    - [대표적인 문제들]
        - Context, ViewModel, NavController 등 실행 시점 의존성 주입 불가
        - LocalContext.current 사용 시 NPE 또는 "Preview not supported" 오류 발생 가능
        - 동적 데이터(Firebase, Room, Network 등) 접근 시 미동작 또는 실패
        - 커스텀 Theme 적용 누락 시 실제와 다른 UI 미리보기

    - [해결 방법]
        - Preview 용 mock 데이터 또는 fake ViewModel 생성
        - @Preview(showBackground = true)로 기본 배경 확인
        - 의존성이 필요한 컴포넌트는 분리하고, slot-based 구조로 Preview 가능한 형태로 설계
        - PreviewParameterProvider로 리스트/객체 인젝션 가능

- Jetpack Compose에서 SideEffect, DisposableEffect, LaunchedEffect의 차이점
    - [공통점]
        - 모두 Composable의 생명주기와 연결된 Side Effect 처리 도구

    - SideEffect
        - 매 recomposition마다 실행됨
        - 비 suspend 작업 수행 시 사용 (예: 로그 기록, 외부 객체에 상태 전달)
        ```kotlin
        SideEffect {
            Log.d("TAG", "This runs every recomposition")
        }
        ```
    
    - LaunchedEffect
        - key가 변경될 때마다 suspend 함수 실행
        - 코루틴 기반으로 delay, collect, API 호출 등 수행 가능
        ```kotlin
        LaunchedEffect(key1) {
            delay(1000)
            viewModel.loadData()
        }
        ```

    - DisposableEffect
        - Composable 진입 시 실행, 사라질 때 onDispose 블록 실행
        - 리소스 정리 또는 등록/해제 목적
        ```kotlin
        DisposableEffect(key1) {
            registerCallback()
            onDispose { unregisterCallback() }
        }
        ```

- Jetpack Compose에서 LocalContext와 LocalLifecycleOwner의 활용 방법
    - LocalContext
        - 현재 Composable이 소속된 Context 제공
        - Activity, Application, Toast, startActivity 등 Android API 접근에 필수
        ```kotlin
        val context = LocalContext.current
        Toast.makeText(context, "Hello", Toast.LENGTH_SHORT).show()
        ```

    - LocalLifecycleOwner
        - 현재 Composable이 위치한 LifecycleOwner 제공
        - LifecycleObserver 등록, Flow.observeWithLifecycle() 등에 활용
        ```kotlin
        val lifecycleOwner = LocalLifecycleOwner.current
        DisposableEffect(Unit) {
            val observer = LifecycleEventObserver { _, event -> ... }
            lifecycleOwner.lifecycle.addObserver(observer)
            onDispose {
                lifecycleOwner.lifecycle.removeObserver(observer)
            }
        }
        ```

    - [활용 팁]
        - ViewModel 연동 시 viewModel() 함수는 내부적으로 LocalViewModelStoreOwner.current 사용
        - LocalContext는 비동기 Context 기반 작업 (WorkManager, CameraX, Permission)에 유용
        - LifecycleOwner 활용 시에는 Composable이 화면에 보이는 동안만 observer가 살아 있도록 설계해야 메모리 누수 방지 가능

- Compose에서 Layout Inspector를 활용하여 UI Debugging을 수행하는 방법
    - [기본 개념]
        - Android Studio의 Layout Inspector는 현재 앱에서 표시 중인 Compose UI를 실시간으로 계층 구조 및 상태까지 시각화할 수 있는 도구

    - [주요 기능]
        - 재조합 경로 확인: 어떤 Composable이 리컴포지션 되었는지 추적
        - Modifier 확인: 패딩, 마진, 클릭 등 실제 적용된 Modifier 정보 확인
        - Composition tree 시각화: 뷰 계층 없이도 Compose만의 트리 확인
        - State 추적: MutableState 값 및 해당 Composable 위치 직접 확인 가능`

    - [활용 방법]
        - 앱 실행 → Android Studio → Layout Inspector 실행
        - Live updates 활성화 → 현재 UI 상태 실시간 반영
        - 특정 Composable 클릭 시 속성, Modifier, 상태 값 확인 가능

    - [주의사항]
        - Preview 상태에선 사용 불가, 실제 기기 또는 에뮬레이터에서만 가능
        - release 빌드나 minify된 경우 정보가 제한될 수 있음

- Jetpack Compose에서 Accessibility를 개선하는 방법
    - [문제 원인]
        - Compose는 XML의 contentDescription 같은 속성이 명시적으로 존재하지 않기 때문에, Accessibility 지원을 명시적으로 구현해야 함

    - [개선 방법]
        - 텍스트 설명 제공
            ```kotlin
            Icon(
                imageVector = Icons.Default.Favorite,
                contentDescription = "즐겨찾기 아이콘"
            )
            ```

        - TalkBack 인식 명확히 하기 위한 Semantics 설정
            ```kotlin
            Modifier.semantics {
                contentDescription = "로그인 버튼"
            }
            ```

        - 비시각 요소는 accessibilityMerged: false로 제어
            ```kotlin
            Modifier.clearAndSetSemantics { }
            ```

        - custom component는 role, state, action을 명시적으로 정의
            ```kotlin
            Modifier.semantics {
                role = Role.Button
                stateDescription = "켜짐"
            }
            ```

        - Focusable 처리 및 접근성 포커스 이동 고려
            - Modifier.focusable(), Modifier.clickable() 사용 시 접근성 포커스 지원됨

    - [Best Practice]
        - 이미지/아이콘엔 항상 contentDescription 설정
        - 복잡한 UI는 semantics {}로 명시적 의미 추가
        - TalkBack, VoiceOver 등으로 직접 테스트 필수

- Jetpack Compose로 마이그레이션할 때 고려해야 할 사항
    - [1. 점진적 전환 전략 필요]
        - 기존 View + Compose 혼합 운영: ComposeView, AndroidView 활용
        - XML을 완전히 버리지 않고 중요 UI부터 Compose 전환

    - [2. 아키텍처 고려]
        - ViewModel, State 관리 구조 먼저 정비
        - 단방향 데이터 흐름(One-way data flow), 상태 호이스팅 도입

    - [3. 테마 및 스타일 정리]
        - MaterialTheme, ColorScheme, Typography 통일
        - 다크 모드, 접근성 대비 포함

    - [4. 테스트 전략]
        - UI 테스트 코드 재작성 필요 (Espresso → Compose UI Test)
        - 화면마다 @Preview 추가하여 시각적 품질 확인

    - [5. 팀원 학습 곡선 고려]
        - Compose 문법/상태 관리에 익숙하지 않다면 내부 교육 및 코드리뷰 기준 수립

    - [6. 퍼포먼스 주의]
        - LazyColumn, Recomposition, SideEffect 등 Compose 특성 이해 후 마이그레이션
        - 잘못된 사용 시 초기 앱 성능 저하 가능

- Compose에서 XML 기반 View와 혼합하여 사용할 때 성능 문제를 해결하는 방법
    - [문제 원인]
        - ComposeView 또는 AndroidView로 XML과 Compose를 혼합할 경우, 렌더링 트리 간 경계 비용이 발생
        - View 계층과 Compose 계층이 서로 이벤트/상태를 오갈 때 중복 측정(measure), 배치(layout), draw 작업이 추가됨

    - [대표적인 문제]
        - 스크롤/애니메이션 시 끊김
        - View ↔ Compose 간 데이터/포커스 전달 지연
        - ComposeView를 RecyclerView 안에 넣는 등 잘못된 중첩 사용 시 성능 급락

    - [해결 방법]
        - 필요한 구간만 최소한으로 ComposeView/AndroidView 사용
        - ComposeView.setViewCompositionStrategy(DisposeOnViewTreeLifecycleDestroyed)로 메모리 누수 방지
        - 상태 공유는 ViewModel, LiveData, StateFlow 등 공통 아키텍처 계층에서 처리
        - Scroll/Touch 이벤트 충돌 시 NestedScrollInteropConnection 또는 pointerInteropFilter 사용

- Jetpack Compose에서 ViewModel과 StateFlow를 결합하여 상태를 관리하는 방법
    - [기본 구조]
        - StateFlow는 ViewModel에서 상태를 스트림 형태로 관리할 수 있는 선언적 방식
        - Compose에서는 이를 collectAsState()로 UI에 바인딩하여 자동 recomposition 유도

    - [ViewModel 예시]
        ```kotlin
        class MyViewModel : ViewModel() {
            private val _uiState = MutableStateFlow("Hello")
            val uiState: StateFlow<String> = _uiState

            fun update() { _uiState.value = "Updated" }
        }
        ```

    - [Composable 예시]
        ```kotlin
        @Composable
        fun MyScreen(viewModel: MyViewModel = viewModel()) {
            val state by viewModel.uiState.collectAsState()
            Text(text = state)
        }
        ```

    - [Best Practice]
        - collectAsState()는 Composable 내부에서 호출, UI recomposition 보장
        - StateFlow는 ViewModel에서 private mutable / public immutable 패턴 유지
        - 단순 이벤트는 SharedFlow 또는 Channel로 분리

- Compose에서 Flow를 collect하여 UI를 업데이트하는 최적의 방법
    - [문제점: 일반적인 Flow 사용 시]
        - Flow는 cold stream이기 때문에 직접 collect하면 
        - recomposition 타이밍과 lifecycle mismatch 발생 가능
        - 수동 collect 시 메모리 누수, 중복 실행, 죽은 lifecycle에서의 collect 문제 발생

    - [최적의 방법]
        - collectAsState() 사용 (StateFlow or Hot Flow)
            ```kotlin
            val state by flow.collectAsState(initial = "Loading")
            ```

        - collectAsStateWithLifecycle() 사용 (lifecycle-aware)
            - Jetpack Lifecycle Compose 라이브러리 필요
            ```kotlin
            val state by viewModel.flow.collectAsStateWithLifecycle()
            ```

        - LaunchedEffect + collect 사용 (이벤트 흐름 처리)
            - Flow<T>가 UI 상태가 아닌 이벤트 스트림일 경우
            ```kotlin
            LaunchedEffect(Unit) {
                viewModel.eventFlow.collect { event -> 
                    handleEvent(event)
                }
            }
            ```

    - [Best Practice]
        - UI 상태는 StateFlow + collectAsState()
        - 일회성 이벤트는 SharedFlow + LaunchedEffect
        - Lifecycle에 민감한 경우 collectAsStateWithLifecycle() 활용 (crash 방지)

- Android 14에서 Jetpack Compose와 관련된 주요 변경 사항
    - [핵심 변경 사항]
        - (1) Runtime Permission 변경
            - SCHEDULE_EXACT_ALARM, POST_NOTIFICATIONS 등 새로운 퍼미션이 등장 → Compose 앱도 명시적 요청 필요
        - (2) Predictive Back 지원 강화
            - Compose Navigation에 Predictive Back Transition API 도입됨
            - BackHandler 사용 시 predictive back 흐름 방해 주의 필요
        - (3) IME(키보드) 애니메이션 개선
            - Compose에서 WindowInsets.ime 사용 시 애니메이션이 더 자연스럽고 동기화된 애니메이션 동작 가능
        - (4) Compose Compiler 및 Kotlin 1.9.x 대응
            - 최신 Android Studio에서는 Kotlin 1.9 + Compose Compiler 1.5+ 조합 사용 권장
            - @Composable target 변경 등 내부 최적화 적용됨

    - [대응 방법]
        - AndroidManifest에 새로운 퍼미션 반영
        - androidx.activity:activity-compose 최신 버전 사용
        - compose.navigation 업데이트 시 Predictive Back 관련 옵션 설정
        - Jetpack BOM을 최신으로 유지 (compose-bom:2023.10.01 이상)

- Jetpack Compose의 새로운 Material 3 디자인 적용 시 고려해야 할 사항
    - [변경된 핵심 요소]
        - (1) ColorScheme 기반 색상 시스템
            - MaterialTheme.colorScheme.primary 등 → 더 세분화된 색상 체계 제공
            - Android 12 이상에서는 Dynamic Color까지 자동 적용 가능
        - (2) 기본 컴포넌트 스타일 변화
            - Button, TextField, Card, AppBar 등 Material 2 대비 여백, 모서리, 간격, 상태 변화 다름
            - FilledTonalButton, ElevatedCard, CenterAlignedTopAppBar 등 신규 컴포넌트 추가
        - (3) Motion 및 Shape 시스템 업데이트
            - Elevation과 Motion이 시각적으로 더 표현되도록 변경됨
    - [적용 시 고려사항]
        - Material3로 테마 마이그레이션할 때 기존 Material2 스타일과 혼용 주의
        - 기본 MaterialTheme → MaterialTheme3로 변경 후, colorScheme, typography, shapes를 전면 적용
        - 다크모드 + Dynamic Color 대응은 dynamicLightColorScheme()로 분기

- Jetpack Compose에서 터치 이벤트를 처리하는 방법
    - [기본 처리 방식]
        - (1) Modifier.clickable()
            - 단일 탭 제스처 처리
            - ripple 효과 및 accessibility 자동 지원

        - (2) Modifier.pointerInput()
            - 저수준 터치 제어 (탭, 드래그, 멀티터치 등)
            - detectTapGestures, awaitPointerEventScope 등 활용 가능

        - (3) Modifier.pointerInteropFilter()
            - Android View 방식의 MotionEvent 직접 처리 가능 (Interop 용)

    - [예시]
        ```kotlin
        Modifier.pointerInput(Unit) {
            detectTapGestures(
                onTap = { offset -> /* 좌표 기반 동작 */ },
                onDoubleTap = { /* 더블탭 처리 */ }
            )
        }

        // pointerInteropFilter
        Modifier.pointerInteropFilter {
            when (it.action) {
                MotionEvent.ACTION_DOWN -> { /* 뷰 방식 이벤트 */ true }
                else -> false
            }
        }
        ```

    - [Best Practice]
        - 간단한 동작: clickable()
        - 제스처 복합 조합: pointerInput()
        - 기존 View 연동 필요 시: pointerInteropFilter()
        - 터치 충돌 방지 시 indication = null, interactionSource = remember { MutableInteractionSource() } 활용 가능

- Jetpack Compose에서 다크 모드를 지원하는 방법
    - [기본 개념]
        - Compose는 시스템 다크 모드에 따라 자동으로 테마를 변경할 수 있는 구조를 갖고 있음
        - isSystemInDarkTheme()을 사용해 현재 테마 상태를 판단 가능

    - [구현 방법]
        - (1) 테마 설정
            ```kotlin
            @Composable
            fun MyAppTheme(
                darkTheme: Boolean = isSystemInDarkTheme(),
                content: @Composable () -> Unit
            ) {
                val colorScheme = if (darkTheme) DarkColorScheme else LightColorScheme

                MaterialTheme(
                    colorScheme = colorScheme,
                    typography = Typography,
                    shapes = Shapes,
                    content = content
                )
            }

            // 사용 시
            MyAppTheme {
                // Your UI
            }
            ```
    - [Best Practice]
        - 시스템 설정에 따라 테마 자동 전환 (isSystemInDarkTheme)
        - 색상은 MaterialTheme.colorScheme.primary 등으로 추상화해 하드코딩 방지
        - 다크 모드 기준 테스트 필요 (Preview 또는 실제 기기)

- Compose에서 WebView를 사용할 때 발생하는 문제와 해결책
    - [문제 원인]
        - Compose는 Viewless 환경이지만 WebView는 기존 View 시스템 기반 → AndroidView를 통해 사용해야 함
        - WebView 내에서 상태 저장, 포커스, 크래시 등 문제가 발생할 수 있음

    - [대표적인 문제들]
        - WebView 리로드 시 상태 초기화
        - BackPress 충돌 (WebView 내부에서 뒤로가기 처리 필요)
        - Compose recomposition 시 WebView가 의도치 않게 재생성됨

    - [해결 방법]
        - (1) AndroidView로 WebView 삽입
            ```kotlin
            AndroidView(factory = {
                WebView(it).apply {
                    loadUrl("https://example.com")
                }
            })
            ```
        - (2) WebView 재생성 방지
            - remember { WebView(context) } 사용해 인스턴스 유지
        - (3) BackPress 지원
            ```kotlin
            val webView = remember { WebView(context) }

            BackHandler(enabled = webView.canGoBack()) {
                webView.goBack()
            }
            ```
    - [추가 설명]
        - WebView 설정은 반드시 .apply { ... } 블록에서 초기화
        - 쿠키, 자바스크립트, 클라이언트 설정은 명시적으로 처리

- Jetpack Compose에서 Edge-to-Edge UI를 구현하는 방법
    - [기본 개념]
        - Edge-to-Edge UI는 시스템 상태바/내비게이션바 영역까지 UI를 확장하는 방식
        - Compose는 WindowInsets를 통해 상태바, 내비바, IME 높이 등을 제어함

    - [구현 절차]
        - (1) System UI Controller 설정 (Accompanist 사용)
            ```kotlin
            val systemUiController = rememberSystemUiController()
            SideEffect {
                systemUiController.setSystemBarsColor(Color.Transparent, darkIcons = true)
            }
            ```

        - (2) 전체화면 설정 (Activity)
            ```kotlin
            WindowCompat.setDecorFitsSystemWindows(window, false)
            ```

        - (3) Insets Padding 처리
            ```kotlin
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(WindowInsets.systemBars.asPaddingValues())
            ) {
                // Content
            }
            ```

    - [주의사항]
        - 상태바 영역과 겹치는 UI 요소에는 반드시 padding 처리
        - WindowInsets.navigationBars 및 ime 도구로 입력창/내비게이션 대응 가능
        - 시스템 배경색/아이콘 명도 조절 필요 (darkIcons = true/false)

- Android의 Binder IPC 메커니즘
    - [정의]
        - Binder는 안드로이드에서 프로세스 간 통신(IPC, Inter-Process Communication)을
        - 지원하는 고성능 커널 기반 메커니즘
        - 클라이언트와 서비스 간 메서드 호출 형태로 데이터 전달 가능

    - [동작 방식]
        - (1) 클라이언트가 서비스에 AIDL 인터페이스를 통해 요청
        - (2) 요청은 Binder Driver를 통해 커널 영역을 거쳐 서비스로 전달 (바인더 구조 조사 필요)
        - (3) 서비스는 요청을 처리하고 응답을 다시 클라이언트에 전달

    - [특징]
        - 직접 메모리 공유 없이 안전하게 통신 가능
        - 안드로이드의 Service, ContentProvider, Messenger, AIDL 등이 Binder 위에서 동작

    - [장점]
        - 빠른 IPC 성능 (shared memory 기반보다 안정적)
        - 보안성 높음: UID/PID 기반 인증 가능
        - 시스템 서비스와 앱 간 통신에서도 주요 기반 기술

- Binder 구조
    - [Binder 개념]
        - Android의 IPC (Inter-Process Communication) 메커니즘의 핵심
        - 앱 프로세스와 시스템 서비스 또는 다른 앱 간에 직접 메서드 호출처럼 통신할 수 있도록 해주는 커널 기반 드라이버와 프레임워크의 조합

    - [Binder의 전체 구조]
        - (1) Application Layer (Java/Kotlin)
            - Service, Messenger, AIDL 등을 통해 Binder 통신을 추상화하여 사용
            - 예: MyAidlInterface.Stub.asInterface(binder)

        - (2) Binder Framework (Native Layer, C++)
            - IBinder, Binder, Parcel 객체를 통해 실제 데이터 직렬화 및 메서드 호출 처리
            - BpBinder / BnBinder 구조
                - BpBinder: 클라이언트 측 프록시 (proxy), 서버에 요청 전달
                - BnBinder: 서버 측 수신자 (native binder), 요청 처리

        - (3) Binder Driver (커널 레벨)
            - /dev/binder에 위치한 실제 Linux 커널 모듈
            - 클라이언트와 서버 간의 데이터 및 메시지 전달을 중재
            - 프로세스 간 메모리를 공유하지 않고 버퍼 복사 방식으로 안전하게 데이터 전달

    - [Binder 통신 흐름 요약]
        - 클라이언트가 AIDL을 통해 요청을 생성 (BpBinder)
        - 요청이 Parcel 형태로 직렬화되어 Binder Driver에 전달
        - 커널의 Binder Driver가 메시지를 서버 프로세스에 전달
        - 서버의 BnBinder가 요청을 역직렬화하고 처리
        - 응답이 다시 Binder Driver를 통해 클라이언트로 전달됨

    - [Binder 구조의 장점]
        - 고속 IPC 성능 (Unix Socket이나 메시지 큐보다 효율적)
        - 안전성: 각 프로세스는 메모리를 공유하지 않으며 UID/PID 인증이 가능
        - 프레임워크 통합도 우수: ServiceManager, ActivityManager, MediaService 등 모두 Binder 기반

    - [Binder 관련 주요 구성요소]
        - IBinder: Binder 인터페이스의 최상위 추상화
        - Binder: 서버 측 구현체 (Stub)
        - BpBinder: 클라이언트 측 프록시
        - Parcel: 데이터 직렬화/역직렬화 클래스
        - Binder Driver: 커널 공간의 메모리 메시지 전달 드라이버
        - ServiceManager: 시스템 서비스 레지스트리

    - [실무 관점 활용 예시]
        - AIDL 기반 서비스 통신
        - System Service (예: LocationManager, NotificationManager)는 모두 Binder 기반
        - 앱 ↔ 서비스 프로세스 간 통신 시 Binder가 핵심

- ListView와 RecylerView 설명
    - [ListView]
        - 오래된 리스트 컴포넌트 (API 1부터 존재)
        - 스크롤 시 convertView를 통해 일부 재활용은 가능하지만 재사용 범위와 유연성이 제한적
        - 레이아웃이 고정적이고 ViewHolder 패턴을 직접 구현해야 함
        - 레이아웃 관리 -> 고정 (세로 리스트만)
        - 애니매이션 -> 기본 또는 없음

    - [RecyclerView]
        - ListView의 단점을 개선한 최신 리스트 컴포넌트
        - ViewHolder 패턴 내장, 다양한 LayoutManager (Linear, Grid, Staggered) 지원
        - ItemAnimator, ItemDecoration, DiffUtil 등으로 확장성과 효율성 탁월
        - 레이아웃 관리 -> 다양한 LayoutManager 지원
        - 애니매이션 -> ItemAnimator로 쉽게 구현 가능

- ListView 재활용 가능 여부를
    - [가능 여부]
        - 불가능하지는 않고 제한적으로 가능함

    - [재활용 방식]
        - getView() 메서드에서 convertView가 null이 아니면 기존 뷰를 재사용
        - 하지만 RecyclerView처럼 ViewHolder가 내장되지 않았기 때문에, 개발자가 직접 재활용 로직(ViewHolder 패턴)을 구현해야 함

    - [한계]
        - 재활용 범위가 제한적 (스크롤 시 일정 수의 뷰만 재사용)
        - 복잡한 레이아웃이나 다양한 뷰 타입이 필요한 경우 재사용 관리가 까다로움

    - [정리]
        - 재활용은 가능하지만 비효율적이며 관리가 복잡
        - 유지보수성과 성능을 고려하면 RecyclerView 사용이 권장됨

- Java에서 Stream API를 활용하는 방법
    - [기본 개념]
        - Stream API는 Java 8부터 추가된 컬렉션 처리의 선언형 방식
        - map, filter, collect 등 체이닝 메서드로 데이터 흐름 중심 처리 가능
    - [대표적인 사용 예시]
        ```java
        List<String> names = Arrays.asList("Tom", "John", "Alice");
        List<String> filtered = names.stream()
            .filter(name -> name.startsWith("A"))
            .map(String::toUpperCase)
            .collect(Collectors.toList());
        ```
    - [핵심 연산 유형]
        - 중간 연산: filter(), map(), sorted() → lazy evaluation
        - 종단 연산: collect(), forEach(), count() → 실행 발생

    - [장점]
        - 코드 간결성: 복잡한 for-loop 없이 선언형 코드 가능
        - 병렬 처리: .parallelStream()으로 멀티스레드 실행
        - 불변성 유지: 기존 컬렉션 변경 없이 새로운 결과 생성

    - [주의점]
        - Stream은 1회성 소비 → 재사용 불가
        - 성능 민감한 경우 .parallelStream()은 주의해서 사용

- WorkManager, AlarmManager, Foreground Service의 차이점
    - [공통점]
        - 모두 지속적인 백그라운드 작업을 예약하거나 실행하는 컴포넌트

    - WorkManager
        - 백그라운드에서 신뢰성 있는 작업 예약 가능
        - 앱 종료/재부팅 후에도 보장
        - 네트워크 조건, 충전 중 여부 등 제약 조건 지정 가능
        - 장점: 지연 허용 작업, 조건 기반 실행
        - 단점: 즉시 실행보단 예약 기반
        ```kotlin
        val workRequest = OneTimeWorkRequestBuilder<MyWorker>().build()
        WorkManager.getInstance(context).enqueue(workRequest)
        ```
    
    - AlarmManager
        - 지정한 시간에 정확히 실행되는 작업 예약
        - 앱이 종료되었어도 시스템이 알람을 전달
        - 장점: 정확한 시점에 동작
        - 단점: Android 6+ 이상에서 Doze 모드로 인해 지연 가능

    - Foreground Service
        - 사용자 인식 하에 지속 실행되는 작업
        - 알림(Notification)과 함께 실행됨 → 시스템에서 우선순위 높음
        - 장점: 실시간 처리 필요 시 (위치 추적, 음악 재생)
        - 단점: 배터리 소모 큼, 사용자 알림 필수

- Jetpack Paging3 라이브러리, 동작 방식
    - [핵심 개념]
        - Paging 3는 Jetpack에서 제공하는 대용량 리스트의 효율적인 로딩 라이브러리
        - 데이터를 페이지 단위로 불러오며, RecyclerView와 결합해 사용

    - [동작 방식 요약]
        - (1) PagingSource
            - 서버/DB 등 데이터 로딩 로직 정의 (load())
        - (2) Pager
            - PagingSource를 기반으로 PagingData 스트림 생성
        - (3) ViewModel
            - Flow<PagingData<T>>로 노출 → Compose or RecyclerView로 연결
        - (4) UI (LazyColumn or Adapter)
            - collectAsLazyPagingItems() 또는 PagingDataAdapter.submitData()
        ```kotlin
        val pager = Pager(PagingConfig(pageSize = 20)) {
            MyPagingSource()
        }.flow.cachedIn(viewModelScope)
        ```

    - [장점]
        - 스크롤 이벤트 기반 자동 로딩
        - DiffUtil 내장, loadState로 로딩/에러 상태 추적 가능
        - Room, Retrofit 등과 쉽게 연동 가능

    - [Best Practice]
        - RemoteMediator 사용 시 캐싱 + 페이징 동기화 가능
        - UI에서 LazyPagingItems나 PagingDataAdapter로 처리
        - 에러 처리 및 빈 목록 대응은 LoadState 기반으로 UI 분기

- Java에서 Semaphore, CountDownLatch, CyclicBarrier의 차이점
    - [공통점]
        - 모두 java.util.concurrent 패키지에 속한 스레드 동기화 도구

    - Semaphore
        - 리소스 수 제한을 두고 스레드 접근 제어
        - 내부적으로 허용 가능한 permit 수만큼 acquire/release
        - 여러 스레드 중 제한된 수만 동시 실행, 순차 완료나 그룹 동기화 목적에는 부적합
        ```java
        Semaphore semaphore = new Semaphore(3); // 최대 3개 동시 접근 허용
        semaphore.acquire();  // 접근 요청
        semaphore.release();  // 리소스 반환
        ```

    - CountDownLatch
        - N개의 스레드가 완료될 때까지 기다리는 구조
        - countDown()이 0이 되면 await() 중인 스레드가 모두 진행
        - 단방향/일회성 구조, 재사용 불가
        ```java
        CountDownLatch latch = new CountDownLatch(3);
        latch.countDown(); // 스레드 3개 완료
        latch.await();     // 모든 작업 완료까지 대기
        ```

    - CyclicBarrier
        - 여러 스레드가 모두 도달할 때까지 기다렸다가 동시에 실행
        - barrier.await()로 모두 도착 시 동시 진행
        - 다방향/재사용 가능 (라운드별로 반복 가능), 동기화 실패 시 BrokenBarrierException 주의

- Compose에서 폴더블(Foldable) 디바이스를 대응하는 방법
    - [기본 개념]
        - 폴더블 디바이스는 화면이 접히거나 펴지면서 UI 구성 변경이 필요
        - 화면이 접히는 히지(Hinge) 위치, 상태 등을 반영한 UI 설계 필수

    - [구현 방법]
        - (1) Window Manager Jetpack 라이브러리 사용
            ```kotlin
            implementation("androidx.window:window:1.1.0")
            ```
        - (2) foldingFeature 감지
            ```kotlin
            val windowLayoutInfo = LocalWindowLayoutInfo.current
            val foldingFeature = windowLayoutInfo.displayFeatures
                .filterIsInstance<FoldingFeature>()
                .firstOrNull()
            ```
        - (3) 히지 상태에 따른 UI 대응
            - FoldingFeature.State.HALF_OPENED, FLAT
            - orientation == VERTICAL → 좌우 분할
            - orientation == HORIZONTAL → 위아래 분할
        - (4) Adaptive Layout 구성
            - 두 개의 Column/Row로 나누고 힌지 영역만큼 Spacer 처리

    - [Best Practice]
        - BoxWithConstraints 활용해 폭/높이 기준 레이아웃 분기 처리
        - 힌지 좌표는 FoldingFeature.bounds로 계산해 View 나누기
        - 화면 접힘 전/후의 상태 저장 및 복원 처리 필수

- Jetpack Compose에서 Navigation Component를 활용하는 방법
    - [기본 구성 요소]
        - NavHost: 화면 전환이 일어나는 루트 컨테이너
        - NavController: 화면 이동을 제어하는 객체
        - composable(): 각 화면의 경로(route)를 정의하는 엔트리

    - [예시 코드]
        ```kotlin
        @Composable
        fun MyAppNavHost(navController: NavHostController) {
            NavHost(navController = navController, startDestination = "home") {
                composable("home") { HomeScreen(navController) }
                composable("detail/{id}") { backStackEntry ->
                    DetailScreen(id = backStackEntry.arguments?.getString("id"))
                }
            }
        }

        val navController = rememberNavController()
        MyAppNavHost(navController)
        ```

    - [전달 방식]
        - 파라미터 전달: "detail/123"
        - backStackEntry.arguments?.getString("id")`로 받기

    - [Best Practice]
        - sealed class Screen(val route: String) 으로 route 구조화
        - hiltViewModel() 등으로 ViewModel injection
        - deep link, nested navigation, dialog/BottomSheet 지원 가능
        - AnimatedNavHost 등으로 transition 확장 가능

- Compose에서 비동기 데이터 로딩 중 UI를 최적화하는 방법
    - [문제 상황]
        - API 응답 대기 중 무조건 Blank UI 노출
        - LaunchedEffect 내 suspend 호출 시 UI 상태와 분리되지 않으면 UI 지연 발생
        - 로딩 중에도 사용자 피드백 부족하면 UX 저하

    - [최적화 방법]
        - (1) UI 상태 분리 및 상태 기반 분기
            ```kotlin
            when (uiState) {
                is Loading -> CircularProgressIndicator()
                is Success -> Content(uiState.data)
                is Error -> ErrorView()
            }
            ```

        - (2) produceState 활용한 비동기 초기화
            ```kotlin
            val data by produceState<Result>(initialValue = Loading) {
                value = loadData()
            }
            ```

        - (3) Placeholder/샘플 UI 활용
            - 로딩 중에도 Skeleton UI나 Shimmer 효과로 사용자 관심 유지

        - (4) Recomposition 최소화
            - 로딩 상태와 데이터 상태를 derivedStateOf로 분리해 불필요한 리컴포지션 차단

    - [Best Practice]
        - 상태 → UI 흐름을 명확하게 유지 (Unidirectional Data Flow)
        - 비동기 작업은 ViewModel + StateFlow로 분리
        - Compose의 remember, LaunchedEffect는 UI 전용으로만 사용

- Jetpack Compose에서 ConstraintLayout을 사용할 때 주의할 점
    - [문제 원인]
        - Compose는 선언형 UI 구조인데, ConstraintLayout은 제약 조건 기반 배치 시스템
        - 과도한 ConstraintLayout 사용은 Compose의 간결성과 성능 저하 가능

    - [주의할 점]
        - (1) ConstraintSet 사용 시 id는 Modifier.layoutId로 지정
            ```kotlin
            ConstraintLayout(
                constraintSet = constraints,
                modifier = Modifier.fillMaxSize()
            ) {
                Text("A", Modifier.layoutId("textA"))
            }
            ```
        - (2) 복잡한 제약 조건 → Compose Layout DSL로 대체 가능한지 검토
            - 단순 정렬/간격/중앙 배치 등은 Box, Row, Column으로 충분
        - (3) ConstraintLayout 내부 중첩 최소화
            - 다른 Layout들과 혼용 시 측정/배치 충돌 가능
        - (4) Compose ConstraintLayout 버전 관리
            - androidx.constraintlayout:constraintlayout-compose는 일반 ConstraintLayout과 별도 라이브러리이며 최신 버전 사용 필요

    - [Best Practice]
        - 복잡한 UI에만 사용 (예: 양쪽 고정, 비율 배치, 힌지 대응 UI)
        - ConstraintSet을 사용해 재구성 가능한 UI 설계
        - ConstraintLayout은 UI 정렬 도구이지 상태 관리는 맡기지 않음

- Compose에서 WorkManager와 Coroutines을 함께 활용하는 방법
    - [기본 구조]
        - WorkManager는 백그라운드 작업을 스케줄링
        - CoroutineWorker를 사용하면 suspend fun 형태로 코루틴 기반 비동기 작업 수행 가능

    - [구현 방법]
        - (1) CoroutineWorker 정의
            ```kotlin
            class MyWorker(ctx: Context, params: WorkerParameters) :
                CoroutineWorker(ctx, params) {
                override suspend fun doWork(): Result {
                    val result = repository.syncData()
                    return if (result) Result.success() else Result.retry()
                }
            }
            ```
        - (2) Work 요청
            ```kotlin
            val work = OneTimeWorkRequestBuilder<MyWorker>().build()
            WorkManager.getInstance(context).enqueue(work)
            ```
        - (3) Compose 내 Trigger (예: Button 클릭)
            ```kotlin
            Button(onClick = {
                WorkManager.getInstance(context).enqueue(work)
            }) {
                Text("작업 시작")
            }
            ```
    - [Best Practice]
        - 장시간 작업, 앱 종료 이후에도 유지해야 하는 작업은 반드시 WorkManager 사용
        - 내부에서는 withContext(Dispatchers.IO) 등 코루틴 최적화 가능
        - Compose는 WorkManager 진행 상태를 Observe 하되, 작업 로직은 ViewModel 또는 Worker에 위임

- Jetpack Compose에서 ML Kit을 활용한 AI 기능을 추가하는 방법
    - [기본 개념]
        - ML Kit은 Google이 제공하는 온디바이스 머신러닝 기능 라이브러리
        - 얼굴 인식, 텍스트 인식(OCR), 바코드 스캔, 번역 등 다양한 AI 기능 제공

    - [구현 흐름]
        - (1) ML Kit 의존성 추가
            ```gradle
            implementation "com.google.mlkit:text-recognition:16.0.0"
            ```
        - (2) CameraX 또는 이미지 입력을 받아 InputImage로 변환
            ```kotlin
            val image = InputImage.fromBitmap(bitmap, rotation)
            ```
        - (3) ML Kit 모델 적용 (예: OCR, Optical Character Recognition, 광학 문자 인식 기술)
            ```kotlin
            val recognizer = TextRecognition.getClient()
            recognizer.process(image)
                .addOnSuccessListener { result -> /* 텍스트 사용 */ }
            ```
        - (4) 결과를 Compose 상태에 반영
            ```kotlin
            val recognizedText = remember { mutableStateOf("") }
            ```
    -  [Best Practice]
        - 온디바이스 모델만 사용 시 네트워크 불필요, 빠름
        - 결과 처리 후 remember, State로 UI에 바인딩
        - 권한(Camera 등) 처리와 함께 ViewModel에서 처리 로직 분리 권장

- Compose의 Glance를 활용하여 Widget을 구현하는 방법
    -  [Glance 개념]
        - Jetpack Compose 기반의 앱 위젯(Widget) 구현 라이브러리
        - 기존 RemoteViews 기반 위젯보다 구조적이고 선언형으로 구현 가능

    - [기본 구성 요소]
        - (1) GlanceAppWidget
            - 위젯 정의 클래스. Content() 내부에 UI 선언

        - (2) GlanceAppWidgetReceiver
            - 위젯 업데이트를 OS에 연결해주는 Receiver

    - [예시 구조]
        ```kotlin
        class MyWidget : GlanceAppWidget() {
            @Composable
            override fun Content() {
                Text("Hello from Widget!")
            }
        }

        class MyWidgetReceiver : GlanceAppWidgetReceiver() {
            override val glanceAppWidget: GlanceAppWidget = MyWidget()
        }

        // AndroidManifest.xml
        <receiver android:name=".MyWidgetReceiver" ... />
        ```
    - [주의사항 및 팁]
        - GlanceStateDefinition으로 상태 저장 가능
        - Compose와 비슷하지만 완전히 동일한 Modifier/컴포넌트는 아님
        - 배경 업데이트, 클릭 핸들링은 Glance API를 통해 따로 정의해야 함

- Jetpack Compose에서 Jetpack CameraX를 활용하는 방법
    - [기본 개념]
        - CameraX는 Jetpack에서 제공하는 고수준 카메라 API
        - 다양한 디바이스에서 일관된 사진/영상/분석 기능을 제공
    - [Compose에서 CameraX 연동 방식]
        - (1) CameraX 의존성 추가
            - implementation "androidx.camera:camera-camera2:1.1.0"
            - implementation "androidx.camera:camera-lifecycle:1.1.0"
            - implementation "androidx.camera:camera-view:1.1.0"
        - (2) PreviewView를 AndroidView로 삽입
            ```kotlin
            AndroidView(factory = { context ->
                PreviewView(context).apply {
                    scaleType = PreviewView.ScaleType.FILL_CENTER
                }
            }, modifier = Modifier.fillMaxSize())
            ```
        - (3) CameraProvider 사용
            ```kotlin
            val cameraProviderFuture = ProcessCameraProvider.getInstance(context)
            cameraProviderFuture.addListener({
                val cameraProvider = cameraProviderFuture.get()
                val preview = Preview.Builder().build().also {
                    it.setSurfaceProvider(previewView.surfaceProvider)
                }

                val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA
                cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, preview)
            }, ContextCompat.getMainExecutor(context))
            ```

    - [Best Practice]
        - CameraX + ML Kit 조합 시 ImageAnalysis로 실시간 프레임 처리 가능
        - lifecycleOwner와 함께 안전하게 리소스 관리
        - Compose 전용 Camera 라이브러리는 아직 미완성 → AndroidView 활용이 필수

- Jetpack Compose에서 Biometric API를 활용하는 방법
    - [기본 개념]
        - BiometricPrompt API는 지문, 얼굴 인식 등을 활용한 생체 인증 API
        - Compose에서는 FragmentActivity 기반 Context를 사용해야 하며, Dialog 기반으로 표시

    - [구현 흐름]
        - (1) 의존성 추가
            - implementation "androidx.biometric:biometric:1.1.0"
        - (2) BiometricPrompt 구성
            ```kotlin
            val executor = ContextCompat.getMainExecutor(context)
            val promptInfo = BiometricPrompt.PromptInfo.Builder()
                .setTitle("지문 인증")
                .setNegativeButtonText("취소")
                .build()

            val biometricPrompt = BiometricPrompt(
                context as FragmentActivity,
                executor,
                object : BiometricPrompt.AuthenticationCallback() {
                    override fun onAuthenticationSucceeded(result: BiometricPrompt.AuthenticationResult) {
                        onSuccess()
                    }
                    override fun onAuthenticationError(errorCode: Int, errString: CharSequence) {
                        onError()
                    }
                }
            )

            biometricPrompt.authenticate(promptInfo)
            ```
        - (3) Compose에서 Trigger
            ```kotlin
            Button(onClick = { startBiometricAuth() }) {
                Text("생체 인증")
            }
            ```
    - [주의사항]
        - context는 반드시 FragmentActivity여야 함 (LocalContext.current as FragmentActivity)
        - 테스트 환경 따라 생체 인증이 없을 경우 fallback 처리 필요

- Compose에서 Jetpack Hilt와 함께 DI를 활용하는 방법
    - [기본 개념]
        - Hilt는 Android에서 공식적으로 권장하는 DI 프레임워크
        - Compose에서도 @HiltViewModel과 hiltViewModel()로 ViewModel을 주입 가능

    - [기본 설정]
        - (1) 의존성 추가
            - implementation "androidx.hilt:hilt-navigation-compose:1.0.0"
        - (2) Application 클래스에 Hilt 설정
        - (3) ViewModel 주입 예시
        - (4) Composable에서 주입
            ```kotlin
            @Composable
            fun MyScreen(viewModel: MyViewModel = hiltViewModel()) {
                val state by viewModel.state.collectAsState()
                ...
            }
            ```

    - [Best Practice]
        - DI는 반드시 ViewModel까지로 한정, UI 계층에 직접 주입은 피함
        - Navigation graph가 여러 개일 경우 HiltNavGraphBuilder 등으로 scope 분리
        - 테스트용 Hilt 모듈도 함께 구성 (@TestInstallIn)

- Android의 View 렌더링 과정과 성능 최적화 방법을 설명해주세요.
    - [렌더링 과정 요약]
        - (1) Measure: 각 View의 크기를 결정 (뷰의 크기)
        - (2) Layout: 부모 기준으로 View의 위치 배치 (뷰의 위치 배치)
        - (3) Draw: 실제 픽셀로 화면에 그리기 (그리기)
            - → 이 과정은 매 프레임마다 UI 쓰레드(Main Thread) 에서 처리됨

    - [성능 저하 원인]
        - 레이아웃 계층이 깊거나 중첩 (Nested LinearLayout, RelativeLayout)
        - UI Thread에서 비동기 처리 없이 네트워크, 디코딩 등 수행
        - onDraw() 커스텀 로직 과도하거나 무한 invalidate 호출

    - [최적화 방법]
        - (1) 레이아웃 단순화
            - ConstraintLayout 또는 Compose로 깊이 줄이기
        - (2) ViewHolder 패턴 / LazyColumn 사용
            - RecyclerView, Compose의 Lazy 계열로 필요한 UI만 렌더링
        - (3) 비동기 처리
            - 이미지 로딩은 Glide, Coil 등의 백그라운드 처리 라이브러리 사용
            - 코루틴, RxJava 등으로 UI Thread 분리
        - (4) GPU 오버드로우 최소화
            - 투명도/배경 중첩 줄이기 → Debug GPU overdraw로 분석 가능
        - (5) StrictMode + Profiler 활용
            - 느린 View 측정, UI Thread block 탐지 → Android Studio Profiler로 추적

- Android에서 BroadcastReceiver를 사용할 때 주의해야 할 점
    - [기본 개념]
        - BroadcastReceiver는 앱 간 또는 시스템과 앱 간 메시지 수신을 위한 컴포넌트
        - 예: 부팅 완료, 배터리 변경, 네트워크 상태 변경 등

    - [주의할 점]
        - (1) Android 8.0(API 26)+ 이상에서 제한 강화
            - 대부분의 implicit broadcast는 Manifest 등록 불가
            - 예: CONNECTIVITY_CHANGE, ACTION_NEW_PICTURE 등은 동적 등록만 가능

        - (2) Context 생명주기 짧음
            - onReceive()는 UI 작업이나 장기 작업에 부적합 → 별도 서비스 또는 WorkManager 사용 필요

        - (3) 앱 비정상 종료 리스크
            - 무거운 처리 로직, 네트워크 호출 등은 BroadcastReceiver에서 직접 하지 말 것

        - (4) 보안 고려
            - sendBroadcast()로 공개된 브로드캐스트는 악의적 앱이 수신 가능
            - 민감한 데이터는 LocalBroadcastManager 또는 Context.sendBroadcast(Intent, permission) 사용

    - [Best Practice]
        - Manifest 등록은 시스템 이벤트만 최소한으로
        - 장시간 작업은 JobIntentService / WorkManager로 위임
        - 동적 등록은 반드시 unregisterReceiver()로 해제

- Android에서 권한 시스템(Permission Request)이 동작하는 방식
    - [기본 개념]
        - Android 6.0(API 23)부터 런타임 권한 모델 도입
        - targetSdkVersion >= 23이면 위험 권한은 앱 실행 중 사용자에게 명시적으로 요청해야 함

    - [권한 요청 흐름]
        - (1) AndroidManifest.xml에 선언
            ```xml
            <uses-permission android:name="android.permission.CAMERA" />
            ```
        - (2) 실행 중 권한 체크 및 요청
            ```kotlin
            if (ContextCompat.checkSelfPermission(context, CAMERA) != PERMISSION_GRANTED) {
                ActivityCompat.requestPermissions(activity, arrayOf(CAMERA), REQUEST_CODE)
            }
            ```
        - (3) 결과 콜백 처리
            ```kotlin
            override fun onRequestPermissionsResult(...) {
                if (grantResults[0] == PERMISSION_GRANTED) { ... }
            }
            ```

    - [권한 분류]
        - Normal Permission: 자동 승인 (예: INTERNET)
        - Dangerous Permission: 사용자 승인 필요 (예: CAMERA, LOCATION)
        - Special Permission: 별도 UI 접근 필요 (예: SYSTEM_ALERT_WINDOW, MANAGE_EXTERNAL_STORAGE)

    - [주의사항]
        - 거부 + "다시 묻지 않기" 선택 시, 권한 요청 재시도 불가 → 설정 화면 유도 필요
        - 여러 권한 동시 요청 시 사용자 혼란 주의, 단계적으로 처리 권장

- Android의 Jetpack WorkManager와 JobScheduler의 차이점
    - [공통점]
        - 둘 다 백그라운드 작업 예약 실행을 위한 API
        - 조건 기반 실행, 지연 실행 가능

    - [WorkManager]
        - Jetpack 공식 백그라운드 작업 처리 API
        - 앱 종료/재부팅 후에도 작업 보장
        - CoroutineWorker, ListenableWorker, RxWorker 등 다양한 타입 지원
        - Firebase JobDispatcher, AlarmManager 등 내부적으로 통합하여 관리

    - [JobScheduler]
        - Android 시스템 기본 제공 스케줄러 (API 21+)
        - 시스템 수준의 조건 기반 작업 예약 (네트워크, 충전 중 등)
        - JobService 기반의 구현 필요

- Android에서 Jetpack Navigation Component를 사용할 때의 장점
    - [기본 개념]
        - Jetpack Navigation Component는 Fragment 간 전환, BackStack 관리, SafeArgs 데이터 전달 등을
        - 명시적이고 구조적으로 처리할 수 있도록 지원하는 라이브러리

    - [주요 장점]
        - (1) BackStack 자동 관리
            - Fragment 간 전환 시 뒤로가기 동작을 자동 처리
        - (2) 시각적 NavGraph 설계 가능
            - XML 또는 Kotlin DSL로 전체 앱 내 이동 흐름을 한눈에 파악 가능
        - (3) Safe Args 지원
            - 화면 간 데이터 전달을 타입 안정성 있게 처리 (컴파일 타임 검증)
        - (4) DeepLink, Dialog, BottomSheet 등 대응
            - 네비게이션 목적지로 다양한 유형의 UI 컴포넌트 지원
        - (5) Jetpack Compose 지원
            - Navigation-Compose를 통해 선언형 UI에서도 동일하게 구성 가능

    - [Best Practice]
        - singleActivity 아키텍처와 함께 활용 시 효과 극대화
        - Fragment 외에도 Composable 화면 전환에 활용 가능

- Android에서 Jetpack DataStore와 SharedPreferences의 차이점
    - [기본 개념]
        - 둘 다 키-값 기반의 데이터 저장 방식
        - DataStore는 SharedPreferences의 모던 대체 기술

    - [SharedPreferences 특징]
        - 동기식 API (commit()) 사용 → ANR 발생 위험
        - 내부적으로 XML 파일에 저장
        - 데이터 일관성, 타입 안정성 부족
        - Multi-process 환경에 취약

    - [DataStore 특징]
        - 비동기 처리 기반 (Coroutine/Flow)
        - 두 가지 유형
            - Preferences DataStore: 키-값 구조 (SharedPrefs 대체)
            - Proto DataStore: 구조화된 타입 저장 (Protocol Buffers)
        - 타입 안전성 보장, 트랜잭션 안정성 우수
        - DataStore.updateData()를 통해 원자적 갱신 가능

- Android에서 ViewModel과 Repository 패턴을 함께 사용하는 이유
    - [기본 구조 개념]
        - ViewModel: UI 상태와 생명주기 관리를 담당 (UI 중심)
        - Repository: 데이터 소스 (Local, Remote)와의 추상화 계층을 담당 (도메인 중심)

    - [ViewModel만 사용할 경우 문제점]
        - ViewModel이 API 호출, DB 접근, 비즈니스 로직까지 포함하게 되면 역할이 커지고 테스트/유지보수 어려움
        - 다양한 데이터 소스를 UI와 직접 연결하면 의존성 증가 + 중복 코드 유발

    - [Repository와 함께 쓰는 이유]
        - (1) 관심사 분리 (Separation of Concerns)
            - ViewModel은 UI 상태 관리에 집중, Repository는 데이터 처리 담당
        - (2) 테스트 용이성
            - Repository를 mocking하여 ViewModel 테스트 가능
        - (3) 유지보수성 향상
            - 데이터 변경(예: API → Room 변경) 시 ViewModel 코드 변경 없이 대응 가능
        - (4) 다중 소스 통합 처리
            - 로컬 캐시 + 원격 API 등 여러 소스를 Repository에서 조합 가능

    - [Best Practice]
        - suspend fun, Flow, LiveData 등 비동기 처리를 ViewModel ↔ Repository 계층에서 분리
        - Repository는 interface → implementation 구조로 DI와 테스트 유리하게 설계

- Android에서 ViewModelStoreOwner의 역할
    - [기본 개념]
        - ViewModelStoreOwner는 ViewModel을 보관(ViewModelStore)하고, 
        - 생명주기 범위에 따라 공유 가능하도록 해주는 인터페이스

    - [주요 역할]
        - (1) ViewModel 범위 결정
            - Activity, Fragment, NavBackStackEntry 등이 ViewModelStoreOwner를 구현함
            - ViewModel은 이 Owner의 생명주기 동안 유지됨

        - (2) ViewModelStore 제공
            - viewModelStore: ViewModelStore 반환 → 내부적으로 ViewModel을 키 기반으로 저장

        - (3) 공유 가능성
            - 동일한 ViewModelStoreOwner를 기반으로 하면 여러 Composable 또는 Fragment 간 ViewModel 공유 가능

    - [예시]
        ```kotlin
        val viewModel = ViewModelProvider(owner).get(MyViewModel::class.java)
        ```
        - owner는 보통 activity, fragment, navBackStackEntry 등

    - [Best Practice]
        - Navigation Component 사용 시 NavBackStackEntry를 ViewModelStoreOwner로 활용하여 화면 간 상태 유지/공유 최적화
        - ViewModel 범위를 정확히 설정하지 않으면 불필요한 메모리 유지 또는 상태 초기화 문제 발생

- Android에서 Room Database와 SQLite의 차이점
    - [Room의 장점]
        - @Entity, @Dao, @Database 기반으로 명시적 구조화
        - SQL 쿼리도 @Query로 작성하면서 컴파일 타임 오류 검출 가능
        - LiveData / Flow와 연계하여 UI와 자동 연결 가능
        - 테스트 용이, 멀티 스레드 안전성 ↑

    - [실무 팁]
        - Room은 내부적으로 SQLite를 사용 → 성능은 SQLite와 같음
        - 단, Room은 타입 안전성 + 아키텍처 통합 + 추상화 제공이 강점

- Jetpack Compose와 기존 View 기반 UI의 차이점
    - [Compose의 강점]
        - UI와 상태 간의 단방향 데이터 흐름 (Unidirectional Data Flow)
        - View 계층 없이 간단하고 유연한 UI 구성 가능
        - 코드 → UI 직접 연결로 테스트, 유지보수, 리팩토링 용이

    - [주의할 점]
        - 재컴포지션 원리 이해 필수 (remember, derivedStateOf)
        - 기존 뷰 시스템과의 혼용 시 AndroidView, ComposeView 사용
        - Navigation, Lifecycle, Animation 등 Compose 전용 API 학습 필요


- Compose에서 State Hoisting 개념을 설명과 사용 시점
    - [개념 설명]
        - State Hoisting은 Composable 내부의 상태를 외부로 끌어올려 관리하는 패턴
        - 즉, 상태(State)와 상태 변경 로직(onValueChange 등)을 상위 컴포저블에 위임함
        ```kotlin
        @Composable
        fun MyInput(value: String, onValueChange: (String) -> Unit) {
            TextField(value = value, onValueChange = onValueChange)
        }
        ```

    - [사용 이유]
        - 재사용성 증가
            - → 상태 없이 동작하는 순수 UI 구성 가능
        - 단방향 데이터 흐름(One-way Data Flow)
            - → 버그가 줄고 디버깅이 쉬움
        - 상태 공유 및 ViewModel과 연결 용이
            - → 여러 Composable 간 동일 상태 공유 가능

    - [사용 시점]
        - UI 상태를 여러 컴포넌트에서 제어하거나 ViewModel과 연동할 때
        - 리팩토링 가능한 컴포넌트를 만들고 싶을 때
        - 모든 @Composable은 상태를 가능하면 외부에서 주입받도록 설계

- Jetpack Compose에서 remember와 rememberSaveable의 차이점
    - [공통점]
        - 둘 다 Composable 내부에서 값을 기억(캐싱)해서 recomposition 시 값 유지
        - remember는 메모리에 저장 → 재구성 시 유지, 프로세스 종료 시 손실

    - [remember]
        - 재구성(Recomposition) 동안 값 유지
        - 그러나 프로세스 종료 / 화면 회전 시 값 사라짐

    - [rememberSaveable]
        - 내부적으로 SavedInstanceState를 활용해 → 화면 회전 / 프로세스 재시작 후에도 값 유지

- Jetpack Compose에서 recomposition을 방지하는 방법
    - [recomposition 개념]
        - 상태가 변경되면 해당 Composable 또는 하위가 자동 재실행되는 과정
        - 과도한 recomposition은 성능 저하의 원인

    - [방지 또는 최소화 방법]
        - (1) remember / derivedStateOf로 값 메모이제이션
            - val derived = remember { derivedStateOf { expensiveComputation(data) } }
        - (2) key를 이용한 리컴포지션 범위 분리
        - (3) LaunchedEffect, SideEffect의 의존성 정확히 설정
            - 의존 값이 바뀔 때만 재실행 되도록 관리
        - (4) 함수 분리로 scope 최소화
            - 큰 Composable 안에서 복잡한 UI를 함수 단위로 분리해 불필요한 재실행 줄임
        - (5) Stable 클래스 활용
            - 불변 객체를 넘기면 Compose가 변경 없음을 추적 가능

    - [Best Practice]
        - 상태의 위치와 범위를 의도적으로 설계
        - 상태가 불필요한 UI에 영향을 주지 않도록 분리
        - CompositionLocal 남용 금지 → 전역 리컴포지션 유발 가능

- Jetpack Compose의 SnapshotStateList와 일반 List의 차이점
    - [상태 추적 여부]
        - SnapshotStateList는 Compose의 상태 시스템에 통합되어 있어 아이템 추가, 삭제, 변경 시 자동으로 recomposition이 발생
        - 반면 일반 List나 MutableList는 상태 추적이 불가능해 값이 바뀌어도 UI가 자동으로 갱신되지 않는다.

    - [recomposition 반응성]
        - SnapshotStateList는 내부 변경에도 반응하여 Compose UI가 자동으로 업데이트된다.
        - 일반 리스트는 리스트 자체를 새로운 값으로 할당해야만 Compose가 변화로 인식한다.

    - [사용 목적]
        - UI 상에서 리스트 항목이 동적으로 변경되는 경우(추가, 삭제, 변경 등)에 SnapshotStateList를 사용한다.
        - 반대로 정적인 리스트를 단순히 출력할 때는 일반 리스트로 충분하다.

    - [선언 방식 차이]
        - SnapshotStateList는 mutableStateListOf()로 선언하며, 
        - 일반 리스트는 listOf() 또는 mutableListOf()로 생성된다.

- Jetpack Compose의 Side Effect API (LaunchedEffect, rememberCoroutineScope, SideEffect 등)의 차이점
    - [LaunchedEffect]
        - Composable이 Composition될 때 suspend 함수나 비동기 작업을 수행할 수 있도록 하는 API. 
        - key가 바뀌면 이전 작업이 취소되고 새로운 코루틴이 실행된다. 
        - 주로 초기 API 호출, 애니메이션 시작 등에 사용한다.

    - [rememberCoroutineScope]
        - Composable 외부에서도 코루틴을 실행할 수 있게 해주는 Scope를 기억한다.
        - recomposition과 무관하게 유지되며, 예를 들어 버튼 클릭 등 사용자의 이벤트 발생 시 비동기 작업을 트리거할 때 사용된다.

    - [SideEffect]
        - Composition이 완료된 후 동기적으로 실행되는 블록이다. 
        - UI에는 직접적인 영향을 주지 않지만, 로그 출력, ViewModel 연동, 외부 상태 기록 등 비동기 작업이 아닌 side-effect 로직에 적합하다.

    - [비교 정리]
        - LaunchedEffect는 suspend 기반 side-effect, 
        - rememberCoroutineScope는 수동 트리거, 
        - SideEffect는 composition 이후 동기 처리 용도로 사용하며 각각의 lifecycle 및 실행 시점이 다르므로 목적에 따라 구분해서 사용해야 한다.

- Compose에서 LazyColumn과 RecyclerView의 성능 차이
    - [UI 렌더링 방식]
        - RecyclerView는 ViewHolder 패턴을 통해 뷰를 재활용하면서 View 객체를 직접 다룬다. 
        - 반면 LazyColumn은 선언형 구조로 필요한 항목만 동적으로 Composable을 구성하고 필요 없으면 자동으로 폐기하여 메모리 사용을 최소화한다.

    - [성능 최적화 방식]
        - RecyclerView는 내부적으로 Pool을 활용한 뷰 재사용을 통해 성능을 확보하며, 
        - LazyColumn은 recomposition을 최소화하며 필요한 데이터만 그리도록 설계되어 비슷한 수준의 성능을 보여준다. 
        - 다만 복잡한 뷰 타입이나 고급 스크롤 기능은 RecyclerView가 유리하다.

    - [코드 복잡도]
        - RecyclerView는 Adapter, ViewHolder, DiffUtil 등 별도 클래스를 작성해야 하지만, 
        - LazyColumn은 코드량이 적고 선언형 구조로 UI 설계가 더 직관적이다.

    - [상태 시스템과의 통합성]
        - LazyColumn은 Compose의 상태 시스템과 자연스럽게 연결되어 있어 
        - State, Flow, LiveData 등과 손쉽게 연동된다. 
        - 반면 RecyclerView는 Observe 기반으로 UI 변경을 수동 처리해야 한다.

    - [사용 추천 기준]
        - 새로운 프로젝트에서는 LazyColumn이 기본 선택이며, 
        - 복잡한 커스텀 애니메이션이나 기존 View 기반 시스템과의 호환성이 필요한 경우 RecyclerView를 고려

- Compose에서 Modifier의 역할과 주요 Modifier 예제를 설명
    - [역할]
        - Modifier는 Composable의 레이아웃, 동작, 스타일, 제스처 등 속성을 연속적으로 설정할 수 있는 구성 블록임. 
        - 모든 Modifier는 순차적으로 체이닝되며, 각 단계에서 Composable의 속성을 꾸미거나 제어함.

    - [레이아웃 관련 예시]
        - Modifier.padding(16.dp) → 내부 여백 설정
        - Modifier.fillMaxWidth() → 부모의 가로 폭 전체 사용
        - Modifier.size(100.dp) → 고정된 너비와 높이 지정

    - [스타일 관련 예시]
        - Modifier.background(Color.Red) → 배경 색상 적용
        - Modifier.border(1.dp, Color.Black) → 테두리 추가
        - Modifier.alpha(0.5f) → 투명도 설정

    - [동작/제스처 예시]
        - Modifier.clickable { ... } → 클릭 이벤트
        - Modifier.pointerInput(Unit) { detectTapGestures { ... } } → 사용자 제스처 감지

    - [조합의 특징]
        - Modifier는 순서에 따라 동작이 달라질 수 있으므로, 실행 순서를 고려한 조합 설계가 중요함.

- Jetpack Compose에서 rememberScopedState가 필요한 이유
    - [기본 개념]
        - rememberScopedState는 Navigation Compose 환경에서 route 단위로 remember된 값을 NavBackStackEntry의 생명주기 범위에 따라 관리하기 위해 사용됨.

    - [필요 이유]
        - 일반적인 remember나 rememberSaveable은 Composable이 사라지면 값이 소멸됨. 
        - 하지만 화면 전환으로 인해 Composable이 제거되었다가 다시 돌아오는 경우, 값을 유지해야 하는 경우가 있음.
        - 이때 rememberScopedState를 사용하면 BackStackEntry 단위로 상태를 저장하고 화면 복귀 시 이전 상태를 복원할 수 있음.

    - [주로 사용되는 경우]
        - 탭 전환, 다중 네비게이션 그래프, Dialog/BottomSheet 등 BackStack 유지가 필요한 복합 구조에서 사용됨.

    - [Compose 공식 상태 관리 흐름의 보완용]
        - 아직 Compose Navigation에선 공식 API로 노출된 것은 아니고, rememberSaveable(stateSaver, key = backStackEntry)와 유사한 방식으로 커스텀 구현하는 사례가 많음.

- Compose에서 Slot API를 활용하는 방법
    - [개념]
        - Slot API는 Composable 내부에 특정 UI 자리를 열어두고, 외부에서 Composable을 주입받아 내부에 삽입할 수 있도록 하는 방식임.
        - 즉, "레이아웃 안에 원하는 부분을 외부에서 정의할 수 있게 열어두는 기술"

    - [사용 이유]
        - 재사용 가능한 컴포넌트를 만들 때 UI 일부를 유연하게 커스터마이징하기 위해 사용함.
        - 예: 제목/본문/버튼이 정해진 Card 컴포넌트 안에 버튼만 바꿔 쓰고 싶을 때

    - [기본 구조 예시]
        ```kotlin
        @Composable
        fun CustomCard(
            title: String,
            content: @Composable () -> Unit
        ) {
            Column {
                Text(title, fontWeight = FontWeight.Bold)
                Spacer(modifier = Modifier.height(8.dp))
                content()
            }
        }

        // 사용 예
        CustomCard(title = "안내") {
            Text("이곳에 Slot으로 들어갈 내용입니다.")
        }
        ```

    - [실전 활용]
        - AlertDialog, Scaffold, TopAppBar 등의 Jetpack Compose 공식 컴포넌트들도 
        - 모두 Slot API 구조로 되어 있음.
        - 따라서 Slot 구조에 익숙해지면 확장 가능한 UI 컴포넌트 설계가 가능함.

- Compose에서 UI 성능을 최적화하는 방법
    - [Recomposition 최소화]
        - 상태가 변경될 때 불필요한 리컴포지션이 발생하지 않도록 remember, derivedStateOf, key 등을 적절히 사용해야 함.
        - Composable 내부에서 자주 바뀌지 않는 값은 remember로 캐싱하고, 계산이 많은 파생 상태는 derivedStateOf로 분리함.

    - [함수 분리]
        - 하나의 Composable 함수가 너무 크거나 많은 상태에 의존하면 리컴포지션 범위가 커짐.
        - 따라서 UI를 작은 단위의 함수로 분리하여 변경된 영역만 다시 그리도록 유도해야 함.

    - [Lazy 계열 사용]
        - 리스트나 반복 구조는 Column이 아닌 LazyColumn, LazyRow 등을 사용하여 필요한 항목만 렌더링하도록 해야 메모리와 연산 비용을 아낄 수 있음.

    - [Modifier 최적화]
        - Modifier는 체이닝 순서와 구성에 따라 불필요한 레이아웃 측정이나 그리기가 반복될 수 있으므로, 중복 Modifier 제거와 불필요한 drawBehind, graphicsLayer 회피가 중요함.

    - [SnapshotState 관리]
        - mutableStateListOf, mutableStateMapOf 등을 사용할 때는 변경 범위를 명확히 하고, 불필요한 전체 리스트 갱신 대신 부분 업데이트를 유도해야 함.

- Compose에서 정적인 상태와 동적인 상태를 관리하는 모범 사례
    - [정적인 상태 예시]
        - 앱 내에서 고정된 문자열, 색상, UI 구조 등은 재조합이 필요 없는 정적인 상태로, val, remember 등을 통해 컴포지션 동안 한 번만 선언되도록 해야 함.

    - [동적인 상태 예시]
        - 사용자 입력값, API 결과, 스크롤 위치, 버튼 클릭 상태 등은 자주 바뀌는 값이므로 remember { mutableStateOf(...) }, collectAsState() 등을 사용해 관리함.

    - [모범 분리 방식]
        - ViewModel에서 상태를 StateFlow 또는 LiveData로 선언하고, Composable에서는 collectAsState()로 구독함.
        - 상태는 가능한 외부에서 주입(hoisting)하고, Composable은 순수 UI 함수로 유지하는 것이 이상적임.

    - [불변성과 추적 가능성 유지]
        - 상태 객체는 최대한 불변 구조로 관리하여 예측 가능하게 만들고, 필요하다면 State → UI → Event → ViewModel → State로 이어지는 단방향 흐름(One-way Data Flow) 구조를 유지해야 함.

- Jetpack Compose의 Preview 기능을 활용하는 방법
    - [기본 사용 방법]
        - @Preview 애노테이션을 붙이면 Android Studio에서 XML처럼 Composable UI를 실시간 미리보기 가능함.
        - showBackground = true, name, uiMode, device 등 다양한 옵션으로 테스트 시나리오를 설정할 수 있음.

    - [상태 분리 중요성]
        - Preview에서는 ViewModel이나 실제 데이터가 없기 때문에, UI 로직과 상태 로직을 분리해야 제대로 동작함.
        - 미리보기용 dummy 데이터를 직접 전달하는 방식으로 Preview에 대응해야 함.

    - [예제 구조]
        ```kotlin
        @Preview(showBackground = true)
        @Composable
        fun MyScreenPreview() {
            MyScreen(title = "예시 제목", onClick = {})
        }
        ```

    - [활용 포인트]
        - 다크 모드, 폰트 크기, 화면 방향, 기기 종류에 따른 UI 미리보기 테스트를 통해 다양한 기기 대응력을 확인할 수 있음.
        - 디자이너와 협업 시 빠르게 레이아웃 피드백을 받기에도 매우 유용함.

    - [주의점]
        - Preview에서 remember, LaunchedEffect 등 런타임 컨텍스트 의존 코드가 동작하지 않을 수 있으므로, UI 전용 Preview 전용 함수 구조로 분리하는 것이 좋음.

- Compose에서 BottomSheet와 Dialog를 구현하는 방법
    - [BottomSheet 구현 방법]
        - ModalBottomSheet 또는 ModalBottomSheetLayout을 사용함. 
        - 상태 관리는 rememberModalBottomSheetState와 ModalBottomSheetState로 제어함.
        - 코루틴을 사용하여 show/hide 동작을 수행해야 하며, 외부 클릭/뒤로가기 처리도 자동 지원됨.
        ```kotlin
        val sheetState = rememberModalBottomSheetState(skipPartiallyExpanded = true)
        val scope = rememberCoroutineScope()

        ModalBottomSheet(
            onDismissRequest = { scope.launch { sheetState.hide() } },
            sheetState = sheetState,
            sheetContent = {
                Text("시트 내용")
            }
        ) {
            Button(onClick = { scope.launch { sheetState.show() } }) {
                Text("시트 열기")
            }
        }
        ```

    - [Dialog 구현 방법]
        - AlertDialog 또는 Dialog를 사용하여 간단한 팝업 UI를 구성함.
        - 보여줄지 여부는 Boolean 상태로 제어하고, 닫기 동작은 onDismissRequest에서 수행함
        ```kotlin
        if (showDialog) {
            AlertDialog(
                onDismissRequest = { showDialog = false },
                title = { Text("제목") },
                text = { Text("내용입니다.") },
                confirmButton = { Button(onClick = { showDialog = false }) { Text("확인") } }
            )
        }
        ```

    - [팁]
        - BottomSheet와 Dialog는 모두 UI 상태와 직접 연결되므로 Composable 내부에서 상태 분리를 명확히 하고,
        - rememberSaveable로 복원 가능하게 관리하는 것이 중요함.

- Jetpack Compose에서 Navigation을 적용하는 방법
    - [기본 구조]
        - androidx.navigation:navigation-compose 라이브러리를 사용함.
        - NavHost, NavController, composable(route) 등을 활용하여 화면 간 전환을 구성함.

    - [기본 흐름 예시]
        ```kotlin
        val navController = rememberNavController()
        NavHost(navController, startDestination = "home") {
            composable("home") { HomeScreen(navController) }
            composable("detail") { DetailScreen(navController) }
        }
        ```

    - [인자 전달 방법]
        - 경로에 파라미터를 포함하여 전달할 수 있으며, navBackStackEntry.arguments?.getString(...)으로 수신함.
        ```kotlin
        composable("detail/{itemId}") { backStackEntry ->
            val itemId = backStackEntry.arguments?.getString("itemId")
        }
        ```

    - [복귀 및 스택 제어]
        - navController.popBackStack()을 통해 뒤로가기 가능하며, 특정 화면으로 되돌아가거나 스택 초기화도 가능함.

    - [다중 그래프/BottomNav 구조]
        - NavGraphBuilder를 별도로 분리하거나, Nested Navigation 구조를 활용하여 모듈화 가능함.

- Compose의 LazyColumn에서 성능을 최적화하는 방법
    - [아이템 고유 키 지정]
        - items(items, key = { it.id }) 형식으로 고유 key를 지정해야 삭제/추가/변경 시 위치 추적 오류 및 리컴포지션 오작동을 방지할 수 있음.

    - [최소 상태 관여]
        - 리스트 내부 Composable이 상태를 가지지 않도록 하고, 상태는 ViewModel이나 외부에서 관리하여 각 아이템이 리컴포지션되지 않게 해야 함.

    - [화면 외 아이템 제거]
        - LazyColumn은 스크롤 범위 밖 아이템은 메모리에서 자동 제거되므로, Column 대신 반드시 LazyColumn을 사용해야 함.

    - [고정 높이, Stable class 사용]
        - 아이템이 자주 바뀌는 경우에는 Modifier.height()로 고정 높이를 지정하고, 데이터 모델에 @Stable 또는 @Immutable 어노테이션을 붙여야 Compose가 최적화 가능함.

    - [nested scrolling 주의]
        - 내부에 또 다른 스크롤 가능한 Composable을 포함할 경우, Modifier.nestedScroll() 등으로 충돌 방지 조치 필요함.

- Compose에서 GestureDetector를 활용한 제스처 처리 방법
    - [기본 방식]
        - Jetpack Compose에서는 Modifier.pointerInput과 detectTapGestures, awaitPointerEventScope 등을 통해 다양한 제스처를 처리함. 
        - GestureDetector라는 명시적 클래스는 없지만, gesture detection은 Modifier 수준에서 처리하는 구조임.

    - [단일 탭 예시]
        ```kotlin
        Modifier.pointerInput(Unit) {
            detectTapGestures(onTap = { offset -> /* 클릭 처리 */ })
        }
        ```

    - [복합 제스처 예시]
        - drag, longPress, doubleTap 등 다양한 제스처를 동시에 감지 가능하며, 필요 시 커스텀 제스처도 구현할 수 있음.
    
    - [드래그 제스처 예시]
        ```kotlin
        Modifier.pointerInput(Unit) {
            detectDragGestures { change, dragAmount ->
                // 드래그 거리 활용
            }
        }
        ```

    - [주의점]
        - pointerInput 블록은 suspend 함수이기 때문에 Modifier.combinedClickable 등의 고수준 Modifier를 먼저 고려하고, 
        - 복잡한 제스처가 필요한 경우 pointerInput을 직접 구현하는 것이 좋음.

- Jetpack Compose에서 Recomposition을 피하는 방법
    - [상태 변경 최소화]
        - 상태 변경이 불필요한 Composable에 상태가 전달되면 리컴포지션이 발생함. 
        - 이를 방지하기 위해 상태는 필요한 최소한의 범위로 전달하고, 상태가 자주 변하는 영역과 그렇지 않은 영역을 함수로 분리해야 함.

    - [remember와 derivedStateOf 사용]
        - remember는 값이 변하지 않도록 캐싱하고, derivedStateOf는 상태에서 파생된 값을 메모이제이션하여 재계산을 줄임.

    - [key로 리컴포지션 범위 제어]
        - key(key1, key2) { ... } 형태로 내부 컴포저블의 리컴포지션 기준을 명확하게 설정할 수 있음.

    - [Stable 클래스 활용]
        - 전달하는 파라미터가 불변이면 Compose가 재컴포지션을 생략할 수 있음. 
        - @Stable 또는 @Immutable 어노테이션을 활용하여 데이터 구조의 불변성을 보장해야 함.

    - [LaunchedEffect, SideEffect 등 제한적 사용]
        - 리컴포지션 시 LaunchedEffect가 다시 실행되지 않도록, key 값을 정확히 설정하거나 scope를 줄여야 불필요한 side-effect 실행을 피할 수 있음.

- Compose에서 ConstraintLayout과 Box를 활용하는 방법
    - [Box의 활용]
        - Box는 자식들을 겹쳐서 쌓는 레이아웃임. 
        - 내부 자식은 기본적으로 좌측 상단에 배치되며, Modifier.align()을 통해 정렬 가능함. 
        - 간단한 UI 겹치기, 배경+텍스트 구성, 센터 정렬 등에 적합함.
        ```kotlin
        Box(modifier = Modifier.fillMaxSize()) {
            Text("중앙 텍스트", modifier = Modifier.align(Alignment.Center))
        }
        ```

    - [ConstraintLayout의 활용]
        - ConstraintLayout은 Compose에서도 사용할 수 있으며, 복잡한 배치 조건(예: 뷰 간 거리, 비율, 기준점 정렬 등)이 필요한 경우 적합함. 
        - ConstraintSet, createRefs, constrainAs 등을 통해 유연한 배치 가능.
        ```kotlin
        ConstraintLayout(modifier = Modifier.fillMaxSize()) {
            val (title, button) = createRefs()
            Text("제목", Modifier.constrainAs(title) {
                top.linkTo(parent.top)
                start.linkTo(parent.start)
            })
            Button(onClick = {}, Modifier.constrainAs(button) {
                top.linkTo(title.bottom)
                end.linkTo(parent.end)
            }) {
                Text("버튼")
            }
        }
        ```

    - [선택 기준]
        - 간단한 배치(정렬, 겹침)는 Box, Column, Row로 충분하며, 
        - 복잡한 조건이 필요한 경우에만 ConstraintLayout을 도입하는 것이 성능과 가독성 면에서 유리함.

- Compose의 SnapshotFlow는 무엇이며, 언제 사용해야 하는 가
    - [기본 개념]
        - snapshotFlow는 Compose의 상태 시스템인 Snapshot 내부의 State를 감지하고, 
        - 이를 Coroutine Flow 형태로 변환해주는 API임.
        - 즉, Compose의 상태 변경을 감지해 비Compose 환경에서 반응형으로 처리할 수 있게 해줌.

    - [사용 목적]
        - State가 변경될 때마다 특정 side-effect를 실행하고 싶을 때 사용함. 
        - 예를 들어 스크롤 위치를 관찰하거나, 애니메이션 상태를 감지해서 외부 API 호출 등을 해야 할 때 유용함.

    - [예시]
        ```kotlin
        val scrollState = rememberScrollState()
        LaunchedEffect(Unit) {
            snapshotFlow { scrollState.value }
                .distinctUntilChanged()
                .collect { position ->
                    // 스크롤 위치에 따른 동작 처리
                }
        }
        ```

    - [주의할 점]
        - snapshotFlow는 Compose 내부의 상태를 Coroutine 환경으로 bridge 시켜주는 역할이므로, 
        - 항상 LaunchedEffect 또는 CoroutineScope 안에서 사용해야 하며, State를 기준으로 해야 작동함.

- Jetpack Compose에서 Skia 렌더링 엔진을 활용한 성능 최적화 기법
    - [Skia 렌더링 엔진 개념]
        - Jetpack Compose는 내부적으로 Skia 기반의 그래픽스 엔진(SkiaRenderer) 를 사용함. 
        - 이는 Android 뿐 아니라 데스크탑, 웹 Compose에도 공통적으로 쓰이며 고성능 벡터 기반 2D 그래픽 처리가 가능함.

    - [최적화 기법 1: drawBehind 사용 최소화]
        - Skia는 draw 호출마다 새로운 레이어나 캔버스를 생성할 수 있어 성능 저하를 유발함.
        - Modifier.drawBehind를 남용하면 불필요한 그리기 연산이 반복되므로, 가급적 Box + background 등으로 단순히 처리하는 것이 좋음.

    - [최적화 기법 2: Clip, Shadow, graphicsLayer 남용 주의]
        - clipToBounds, graphicsLayer, shadow는 모두 하드웨어 가속 연산을 유도하므로 오버드로우가 발생할 수 있음.
        - 뷰가 많거나 깊은 계층에선 layer를 최소화해야 GPU 렌더링 효율이 좋아짐.

    - [최적화 기법 3: drawIntoCanvas 최적 활용]
        - Skia의 저수준 API에 접근할 수 있는 drawIntoCanvas를 사용할 경우, 
        - 직접적으로 캔버스를 제어하여 맞춤형 고성능 UI를 구현할 수 있음. 
        - 단, 이 방식은 일반적인 UI 구성보단 커스텀 차트/애니메이션 등에 권장됨.


- Android Thermal API를 활용하여 배터리 및 성능 최적화를 수행하는 방법
    - [기본 개념]
        - Android 10(API 29)부터 제공되는 Thermal API는 디바이스의 열 상태를 감지하고, 
        - 앱이 이에 따라 성능 조절, 애니메이션 간소화, 통신 제어 등을 수행할 수 있게 해줌.

    - [핵심 클래스]
        - android.os.ThermalService 또는 ThermalManager를 통해 시스템의 thermal 상태를 구독할 수 있음.

    - [thermal 상태 종류]
        - ThermalStatus.NORMAL, LIGHT, MODERATE, SEVERE, CRITICAL, EMERGENCY, SHUTDOWN 등 총 7단계가 있으며, 상태가 나빠질수록 CPU throttling이 발생함.

    - [사용 예시]
        ```kotlin
        val thermalManager = getSystemService(Context.THERMAL_SERVICE) as ThermalManager
        thermalManager.registerThermalStatusListener({ status ->
            if (status >= ThermalStatus.MODERATE) {
                // 애니메이션 중단, 통신 제한 등 성능 조정
            }
        }, handler)
        ```

    - [실전 대응 전략]
        - 열 상태가 일정 기준 이상이면 →
            - 고성능 연산 연기 (ex. 영상 처리, 실시간 렌더링)
            - 애니메이션/이펙트 간소화
            - 데이터 전송 빈도 조절
            - 사용자에게 상태 안내 (배터리 과열 경고 등)

    - [주의할 점]
        - Thermal API는 모든 디바이스에서 완벽히 대응하지 않음, 제조사별 차이가 있으며, 
        - 과도한 개입보다는 온도 수준에 따른 사용자 경험 보호 목적으로 사용하는 것이 좋음.

- ExoPlayer에서 DRM(Digital Rights Management) 처리의 고급 기법
    - [기본 구조]
        - ExoPlayer는 MediaDrm, DrmSessionManager, DefaultDrmSessionManagerProvider 등을 통해 Widevine, PlayReady 등의 DRM 기술을 통합 처리함.
        - 콘텐츠 제공자(CDN)는 보통 .mpd(DASH), .m3u8(HLS) 등의 콘텐츠에 KEY_ID를 포함시키고, 클라이언트는 라이선스 서버로부터 키를 받아 복호화함.

    - [고급 기법 1: Custom DRMSessionManager]
        - 기본 제공되는 DefaultDrmSessionManager 대신 직접 DRM 세션 매니저를 구현함으로써,
            - 커스텀 헤더 추가
            - 사용자 인증 토큰 삽입
            - 네트워크 재시도 로직
            - 서드파티 키 서버 연동
                - 같은 고급 요구 사항을 처리할 수 있음.

    - [고급 기법 2: Key Rotation 대응]
        - 일부 콘텐츠는 키가 일정 시간마다 교체됨. 
        - 이를 위해 ExoPlayer에서 OnKeyStatusChangeListener를 등록하고, 재요청 로직을 구현해야 함.
        - 동적 키 갱신 실패 시 재생 중단이 발생하므로, 이중화 및 리트라이 전략이 중요함.

    - [고급 기법 3: Secure Decoder Path 설정]
        - DRM 콘텐츠는 하드웨어 보안 영역(TEE)에서만 재생 가능해야 하는 경우가 있음. 
        - 이때 MediaCodecInfo.isSecure()를 확인하고, setDrmSessionManager()에서 secure decoder를 강제 설정해야 함.

    - [실전 고려사항]
        - 키 만료 시점 체크
        - offline license storage
        - Widevine L1/L3 장치 구분
        - 개발 중에는 DRM debug license server로 테스트 필요

- Android 14에서 추가된 보안 기능과 권한 관리 변화
    - [사진 및 미디어 접근 권한 세분화]
        - 기존의 READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE 권한 대신, Android 14에서는
        - READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, READ_MEDIA_AUDIO로 분리되어 미디어 유형별로 최소 권한 요청이 가능함.

    - [Partial Media Access 기능 추가]
        - 전체 갤러리 접근 대신, 사용자가 선택한 이미지/동영상만 접근하는 옵션이 도입됨.
        - 개발자는 Intent.ACTION_PICK_IMAGES를 활용하여 선택형 권한 흐름을 구현해야 함.

    - [Implicit Intent 보안 강화]
        - PendingIntent나 Intent를 사용할 때 명시적 대상 지정이 강제되며,
        - export 속성이 없는 컴포넌트는 외부 접근이 차단됨. 의도치 않은 컴포넌트 노출이 방지됨.

    - [알림 권한의 지속적 강화]
        - Android 13부터 도입된 POST_NOTIFICATIONS 권한 요구가 Android 14에서도 유지되며,
        - 백그라운드에서 자동 알림 등록 제한이 강화됨. 유저 인터랙션 없이 알림 권한 유도 시 거부 가능성 증가.

    - [보안 로그 및 API 접근 제약 강화]
        - 시스템 로그나 제약된 API 접근 시 RuntimeException 발생. 보안 민감 기능(예: Accessibility, 녹음, 위치)은 점진적으로 더 강한 사용자 승인이 요구됨.

- Android에서 ART(Android Runtime) 최적화를 위한 AOT, JIT, PGO의 차이점
    - [AOT (Ahead-Of-Time)]
        - 앱 설치 시점에 Dalvik bytecode → native machine code로 컴파일하는 방식.
        - 앱 실행 시 로딩 속도가 빠르지만, 설치 시간 증가 및 설치 용량이 커지는 단점이 있음. 
        - Android 5~6 시기까지 기본 사용됨.

    - [JIT (Just-In-Time)]
        - 런타임 중 자주 실행되는 메서드만 즉시 native code로 컴파일함.
        - 설치 속도가 빠르고 메모리 효율적이지만, 초기 실행 성능이 다소 느릴 수 있음. 
        - Android 7 이후부터 기본 적용.

    - [PGO (Profile-Guided Optimization)]
        - JIT와 AOT의 장점을 결합한 방식
        - 앱 사용 중 수집된 실제 실행 profile 정보를 기반으로 AOT 컴파일을 최적화함.
        - 자주 사용되는 경로만 빠르게, 거의 사용되지 않는 코드는 미리 컴파일하지 않음.

    - [최적화 흐름]
        - (1) 초기 앱 실행 → JIT으로 profile 수집
        - (2) 일정 시간 후 → background에서 profile 분석
        - (3) 다음 설치/업데이트 시점에 AOT 최적화 실행 → 부팅/실행 속도 향상

    - [실무 팁]
        - dexopt, profileinstaller API 등을 통해 개발 중에도 PGO 데이터를 수동으로 관리 가능함.
        - ART 최적화를 위해 baseline profile을 직접 설정하는 것도 성능 향상에 도움 됨.

- Android에서 WorkManager의 내부 스케줄링 메커니즘
    - [기본 구조]
        - WorkManager는 백그라운드에서 지속적이고 신뢰성 있는 작업을 처리하는 Jetpack 컴포넌트임.
        - 내부적으로 OS 버전에 따라 실행 엔진이 다르게 적용됨.

    - [스케줄링 전략]
        - Android 6.0 미만 → AlarmManager + BroadcastReceiver
        - Android 6.0 이상 → JobScheduler
        - Android 12 이상에서도 여전히 JobScheduler 기반이지만, 시스템 정책이 더 엄격해짐 (ex. Doze, 배터리 제한)

    - [데이터 저장 방식]
        - 작업 정의, 상태, 입력/출력은 Room 기반 internal DB에 저장됨.
        - 앱이 강제 종료되어도 재부팅 후 작업이 복원 가능함.

    - [재시도 및 백오프 정책]
        - 네트워크 미연결, 배터리 부족 등으로 실패할 경우 지수 증가 방식의 백오프(BackoffPolicy)를 설정할 수 있음.
            - 실패할 때마다 재시도 간격을 점점 더 길게 설정하는 방식 적용
        - 예: BackoffPolicy.LINEAR 또는 EXPONENTIAL + delay 설정

    - [실행 조건 설정]
        - 네트워크 필요 여부, 충전 상태, 저장 공간 등 다양한 조건을 Constraints로 명시 가능.
        - 조건이 만족될 때까지 작업이 보류됨.

    - [최적화 포인트]
        - UniqueWork로 중복 작업 방지
        - Chain 작업으로 순차 실행 보장
        - WorkContinuation을 활용한 병렬 작업 제어

- Android에서 Jetpack CameraX API를 활용한 맞춤형 카메라 솔루션 구축 방법
    - [CameraX 개요]
        - CameraX는 기존 Camera2 API의 복잡함을 줄이고 Lifecycle-aware하며, 
        - 대부분의 기기와 호환되는 카메라 API임.
        - Preview, ImageCapture, ImageAnalysis 등으로 구성되어 있음.

    - [기본 구성 방식]
        ```kotlin
        val cameraProvider = ProcessCameraProvider.getInstance(context).get()
        val preview = Preview.Builder().build().also {
            it.setSurfaceProvider(previewView.surfaceProvider)
        }
        val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA
        cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, preview)
        ```

    - [이미지 캡처 기능 추가]
        - ImageCapture.Builder()를 사용해 JPEG 화질, 회전 방향, 캡처 모드 등을 설정할 수 있음.
        - 캡처 후 저장 또는 Bitmap 처리도 가능.

    - [맞춤형 분석 처리]
        - ImageAnalysis를 활용하면 실시간으로 프레임 데이터를 분석할 수 있음.
        - 얼굴 인식, QR코드 인식, OCR 등 AI 기능과 결합 가능.
        ```kotlin
        val imageAnalysis = ImageAnalysis.Builder().build().also {
            it.setAnalyzer(executor, { imageProxy -> ... })
        }
        ```

    - [최적화 포인트]
        - cameraExecutor는 백그라운드 전용 스레드 사용
        - 해상도는 필요한 수준으로 제한 (ex. 720p로 충분하면 FHD는 비효율적)
        - useCaseGroup으로 Preview, Capture, Analysis 조합 최적화

- Android의 Foreground Service와 Background Service의 차이점 및 최적화 기법
    - [Foreground Service 개념]
        - 사용자 인지 가능 상태로 실행되는 서비스로, 알림(Notification)을 항상 표시해야 함.
        - 백그라운드 제약이 강화된 Android 8 이상에서는 지속적인 작업(예: 위치 추적, 녹음, 파일 업로드) 등에 필수로 사용됨.

    - [Background Service 개념]
        - 사용자에게 표시되지 않는 일반 서비스. Android 8부터는 앱이 백그라운드 상태일 경우 시스템에 의해 자동 종료됨.
        - 현재는 JobIntentService, WorkManager, JobScheduler로 대체하는 것이 권장됨.

    - [주요 차이점]
        - Foreground Service는 즉시 실행되며 종료되지 않음
        - Background Service는 제한적이며, 오랜 실행이 불가함

    - [Foreground 최적화 전략]
        - 서비스 시작 직후 startForeground() 호출 필수
        - 알림 채널을 통해 사용자에게 기능 안내 제공
        - CPU/GPU 리소스를 과도하게 사용하지 않도록 조절 필요

    - [대체 전략]
        - 지속 작업이 아닌 경우 Foreground Service 대신 WorkManager 또는 JobScheduler를 사용하면 배터리 최적화 및 시스템 호환성이 높아짐.

    - [실무 예시]
        - 실시간 위치 추적, 오디오 스트리밍, 운동 기록 앱 등의 기능은 Foreground Service로 구현됨.
        - 반면, 데이터 동기화, 백업 등은 WorkManager를 통해 주기 실행 처리.

- Android에서 TensorFlow Lite를 활용하여 ML 모델을 최적화하는 방법
    - [TensorFlow Lite 개요]
        - TensorFlow Lite(TFLite)는 모바일 및 엣지 디바이스에서 경량화된 머신러닝 모델을 실행하기 위한 솔루션임.
        - .tflite 확장자를 가진 모델 파일을 Android에서 로드해 추론(inference)을 수행할 수 있음.

    - [최적화 기법 1: 모델 양자화(Quantization)]
        - Float32 기반 모델을 int8, float16 등으로 줄여 모델 크기 및 추론 속도 향상 가능.
        - Post-training quantization 기법으로 적용하며 정확도 손실을 최소화하면서 성능 개선 효과가 큼.

    - [최적화 기법 2: 모델 슬라이싱 및 프루닝]
        - 사용하지 않는 노드를 제거하거나 구조를 단순화하여 모델 용량 및 연산량 감소
        - 예: MobileNetV3-small, EfficientNet-lite 모델 사용

    - [최적화 기법 3: NNAPI / GPU Delegate 사용]
        - CPU 외에 NNAPI, GPU, Hexagon delegate를 활용해 추론 속도 향상 가능.
        - 기기 성능에 따라 delegate를 자동 선택하거나 fallback 처리 필요.

    - [실무 적용 팁]
        - Interpreter.Options에 delegate 설정
        - Model metadata를 포함하면 텐서 이름 없이도 쉽게 입출력 가능
        - Android Studio ML Model Binding을 활용하면 boilerplate 코드 생략 가능

- Android에서 Baseline Profiles을 활용한 앱 성능 개선 방법
    - [Baseline Profile 개요]
        - Baseline Profile은 앱 실행 중 자주 호출되는 경로를 미리 컴파일(AOT) 하기 위한 최적화 방식임.
        - Google Play 또는 ART 런타임이 이 정보를 기반으로 특정 메서드들을 사전 컴파일하여 
        - 앱의 cold start, animation lag, JIT delay를 줄일 수 있음.

    - [작성 및 적용 흐름]
        - (1) profileinstaller 라이브러리 설정
        - (2) 특정 시나리오에 대한 프로파일 수집 테스트 실행
        - (3) baseline-prof.txt 생성 후 앱 빌드에 포함
        - (4) Google Play Upload 시 자동 인식 및 적용됨

    - [개발 도구]
        - Macrobenchmark 라이브러리를 활용해 generateBaselineProfile() 실행
            - → cold start, 화면 전환, 리스트 렌더링 등 자주 호출되는 경로 자동 수집

    - [실제 효과]
        - Cold Start 시간 최대 30% 감소
        - 첫 화면 진입 속도 개선
        - RecyclerView / LazyColumn 초기 렌더링 지연 감소

    - [주의 사항]
        - 프로파일은 release 빌드 기준으로 생성해야 효과가 있음
        - 앱 업데이트 시 새로운 profile 유지 필요
        - Gradle Plugin 7.0 이상 필요

- Android에서 Kotlin Coroutines를 사용하는 이유
    - [비동기 처리의 구조적 개선]
        - 기존의 Thread, Handler, AsyncTask 등은 콜백 지옥(callback hell)과 메모리 누수 문제를 유발하기 쉬움.
        - CoroutineScope를 활용하면 lifecycle-aware한 비동기 코드를 간결하고 안전하게 작성 가능함.

    - [가독성 및 유지보수 향상]
        - suspend 키워드를 사용하여 동기 코드처럼 순차적 흐름의 비동기 코드를 작성할 수 있음.
        - 예외 처리, 취소, timeout 등도 한눈에 파악 가능해 유지보수가 쉬움.

    - [경량 스레드 기반]
        - 코루틴은 실제 스레드를 생성하지 않고, 경량 스레드(continuation)로 동작하기 때문에
        - 수천 개의 병렬 작업도 최소한의 자원으로 실행할 수 있음.

    - [구성 요소와의 통합성]
        - Jetpack ViewModel, Room, Retrofit, WorkManager 등과 자연스럽게 통합됨.
        - viewModelScope, lifecycleScope, Dispatchers.IO, Flow와 조합하면 UI, 데이터, 네트워크를 하나의 일관된 흐름으로 처리 가능함.

    - [예시]
        ```kotlin
        viewModelScope.launch {
            try {
                val data = repository.getData()
                _uiState.value = UiState.Success(data)
            } catch (e: Exception) {
                _uiState.value = UiState.Error(e)
            }
        }
        ```

- Android에서 Paging 3 라이브러리를 사용하는 이유
    - [대용량 데이터 처리에 최적화됨]
        - Paging 3는 RecyclerView와 연동되어 스크롤할 때마다 필요한 데이터만 로드함으로써 메모리 효율성과 성능을 모두 향상시킴. 
        - 전체 데이터를 한 번에 불러오지 않아도 되기 때문에 OOM 리스크도 낮아짐.

    - [Flow 기반 비동기 구조]
        - Paging 3는 Flow<PagingData<T>>를 기반으로 동작하므로 Coroutines와 자연스럽게 통합되어, 비동기 처리, 에러 처리, 로딩 상태 관리가 간결해짐.

    - [Jetpack 구성 요소와 통합]
        - ViewModel, Room, Retrofit과 쉽게 연결되며, PagingSource, PagingDataAdapter 등으로 데이터 흐름을 구조화할 수 있음.

    - [Load 상태 관리 지원]
        - 로딩 중, 로딩 실패, 리트라이 등의 상태를 별도로 관리할 수 있어 사용자 경험을 개선할 수 있음.

- Android에서 App Startup Library를 활용하는 방법
    - [기본 개념]
        - App Startup은 Jetpack의 애플리케이션 초기화 라이브러리로, 앱이 시작될 때 각 서브 시스템이 어떤 순서로 초기화되는지 명확히 제어할 수 있음. 
        - ContentProvider를 활용해 자동 실행됨.

    - [Initializer 정의 방법]
        - 각 모듈 또는 라이브러리는 Initializer<T> 인터페이스를 구현하여 필요한 리소스를 초기화함. 
        - 다른 Initializer에 의존성도 명시 가능.
        ```kotlin
        class MyInitializer : Initializer<MyDependency> {
            override fun create(context: Context): MyDependency {
                return MyDependency.init(context)
            }

            override fun dependencies(): List<Class<out Initializer<*>>> = emptyList()
        }
        ```

    - [활용 사례]
        - Firebase, Timber, WorkManager 등 앱 시작 시 필수 설정을 AppStartup에 등록하면 초기화 순서 충돌 방지, 스타트업 비용 측정 등이 가능함.

    - [장점]
        - Application 클래스 비대화 방지
        - 의존성 그래프 기반 순서 관리
        - 조건부 초기화 구현 용이

- Android에서 UI 렌더링 속도를 최적화하는 방법
    - [불필요한 뷰 계층 제거]
        - 중첩된 LinearLayout, Nested ScrollView 등의 복잡한 계층 구조는 Measure/Layout/Draw 단계에서 병목을 유발함.
        - ConstraintLayout이나 Compose로 단순화하는 것이 렌더링 최적화에 효과적임.

    - [View 재사용 및 ViewHolder 최적화]
        - RecyclerView에서 ViewHolder 패턴을 철저히 지키고, DiffUtil을 사용해 변경된 항목만 갱신함으로써 전체 재그리기를 방지할 수 있음.

    - [GPU 과부하 방지]
        - Drop Shadow, Clip, Overdraw 등을 과도하게 사용할 경우 GPU 렌더링이 지연될 수 있음. 
        - Profile GPU Rendering, Layout Inspector를 통해 프레임 렌더링 병목을 시각적으로 분석해야 함.

    - [이미지 최적화]
        - Glide, Coil 등의 이미지 라이브러리에서 썸네일 크기 지정, 메모리 캐싱, 리사이징 등을 활용하여 ImageView 렌더링 병목을 줄여야 함.

- Android에서 OutOfMemory(OOM) 오류를 방지하는 방법
    - [이미지 메모리 관리]
        - 이미지 로딩 시 inSampleSize, inPreferredConfig, Bitmap.recycle() 등의 설정을 통해 메모리 사용량을 줄여야 하며, Glide/Coil을 사용하면 자동 관리 가능함.

    - [Context 누수 방지]
        - Activity나 Fragment의 Context를 static 변수에 보관하면 메모리 해제가 불가능해짐
        - 반드시 applicationContext를 사용하거나, 참조 해제를 명확히 해야 함.

    - [리소스 해제 처리]
        - RecyclerView, ViewPager 등에서 View 재사용 시 이벤트 리스너, animation, coroutine 등 비정상적 참조가 남지 않도록 onViewRecycled, onDestroyView 등에서 해제를 철저히 해야 함.

    - [메모리 Leak 감지]
        - LeakCanary 등을 통해 정적 참조, Coroutine 누수, LiveData 구독 미해제 등을 지속적으로 감시해야 함.

    - [대용량 리스트 대응]
        - Paging 3, Jetpack Compose의 LazyColumn 등 지연 로딩 방식을 사용하여 메모리에서 한 번에 많은 데이터를 다루지 않도록 설계해야 함.

- Android에서 백그라운드 작업을 최적화하는 방법
    - [WorkManager 사용 권장]
        - OS 제약 없이 신뢰성 있게 백그라운드 작업을 실행하려면 WorkManager 사용이 가장 안전함.
        - 네트워크 조건, 충전 상태, 딜레이 설정 등 다양한 조건을 만족할 때 실행되며 앱 종료 후에도 유지됨.

    - [ForegroundService는 필수 작업에만]
        - 지속적인 위치 추적, 오디오 스트리밍 등 사용자 인식이 필요한 작업은 ForegroundService로 처리해야 하며, Notification 표시가 필수임.
        - 단, 과도한 사용은 배터리 소모 및 시스템 제한 가능성 있음.

    - [JobScheduler와 AlarmManager의 제한]
        - JobScheduler는 API 21+에서 사용 가능하지만 정확한 시점을 보장하지 않음.
        - AlarmManager는 정확한 시점 지정이 가능하나 Android 6.0 이상에서는 Doze Mode의 영향을 받음.

    - [Doze & App Standby 대응]
        - Android 6.0 이상에서는 백그라운드 작업이 제한되므로 setAndAllowWhileIdle() 또는 WorkManager의 setExpedited() 옵션을 활용해야 함.

    - [Battery 및 네트워크 고려]
        - 대량 작업은 충전 중이거나 Wi-Fi 상태일 때 실행되도록 제약을 걸어야 시스템 차단을 피할 수 있음.

- Android에서 Jetpack Compose의 Recompositions를 최적화하는 방법
    - [remember와 derivedStateOf 사용]
        - 불필요한 계산이나 상태 변화를 막기 위해 remember { ... }, derivedStateOf { ... }로 메모이제이션을 적용해야 함.

    - [함수 분리 및 Stable 클래스 사용]
        - 리컴포지션 범위를 줄이기 위해 Composable을 작게 분리하고, 데이터 모델에는 @Stable 또는 @Immutable 어노테이션을 붙여 불필요한 리렌더링 방지가 가능함.

    - [key 사용으로 제어]
        - key(id) { ... }를 사용하면 특정 항목의 리컴포지션 기준을 명확하게 제어할 수 있음. 
        - 특히 LazyColumn 등 리스트 항목에서는 필수임.

    - [UI 상태와 데이터 상태 분리]
        - ViewModel에서 상태를 관리하고, Composable은 전달받은 State를 기반으로 UI만 그리도록 하여 단방향 데이터 흐름(One-Way Data Flow) 유지가 중요함.

    - [무의미한 recomposition 탐지]
        - Android Studio의 Recomposition Highlighter 또는 println() 로그로 recompose 시점을 추적하며 최적화 포인트를 식별해야 함.

- Android에서 Bitmap 메모리 관리를 최적화하는 방법
    - [샘플링 및 해상도 제한]
        - 고해상도 이미지를 그대로 메모리에 로드하면 OOM 발생 위험이 크기 때문에,
        - BitmapFactory.Options.inSampleSize를 설정하여 필요한 크기만큼만 로드해야 함.

    - [inPreferredConfig 설정]
        - 기본 ARGB_8888은 고용량이므로, 품질이 중요하지 않은 경우에는 RGB_565로 설정하여 메모리 사용량 절반으로 감소시킬 수 있음.

    - [이미지 캐싱 활용]
        - Glide, Coil 등 이미지 라이브러리는 LruCache 기반 메모리 캐시를 제공하므로 재로드 방지 및 메모리 최적화에 효과적임.
            - LRU Cache: 캐시에 공간이 부족할 때 가장 오랫동안 사용하지 않은 항목을 제거하는 방식

    - [불필요한 Bitmap 해제]
        - 사용이 끝난 Bitmap은 bitmap.recycle() 또는 참조를 null로 해제하여 GC 대상이 되도록 처리해야 함.
        - 특히 ZoomView, CanvasView 등의 커스텀 뷰에서는 수동 해제가 중요함.

    - [Bitmap pooling 고려]
        - 반복적으로 이미지가 생성되는 환경에선 BitmapPool을 이용해 Bitmap을 재사용함으로써 GC 및 메모리 할당 비용을 줄일 수 있음.

- Android에서 Custom View를 만들 때 고려해야 할 사항
    - [onMeasure, onDraw 구현]
        - onMeasure()에서 정확한 크기 계산, onDraw()에서 최소 연산으로 필요한 UI만 그리도록 구현해야 성능 저하를 막을 수 있음.
        - 특히 onDraw 내부에서 객체 생성, 텍스트 측정 등은 캐싱 처리가 필요함.

    - [레이아웃 최소화]
        - 기존 ViewGroup을 확장해서 Custom View를 만드는 경우 중첩된 뷰를 줄이고 하나의 컴포넌트로 통합하는 것이 바람직함.

    - [Touch 이벤트 처리]
        - onTouchEvent()나 GestureDetector를 통해 사용자 인터랙션을 처리할 경우, 이벤트 전파 흐름(dispatchTouchEvent, onInterceptTouchEvent)을 명확히 이해하고 제어해야 함.

    - [Attribute 설정]
        - attrs.xml에 속성을 정의하고, 생성자에서 context.obtainStyledAttributes()로 값을 받아 처리하면 XML에서의 유연한 설정이 가능함.

    - [Custom View 성능 최적화]
        - setWillNotDraw(true)로 draw 생략 가능
        - invalidate() 호출 최소화
        - Hardware acceleration 이슈 확인

- Android에서 CPU 및 메모리 사용량을 최적화하는 방법
    - [불필요한 연산 제거]
        - 반복 호출되는 UI나 루프 내부에서 연산/할당 발생을 줄이고 캐싱을 활용함.
        - ex: TextView.setText() 과도한 호출, JSON 파싱 반복 등

    - [메모리 누수 방지]
        - Context를 static 변수에 보관하지 않기
        - 콜백, Handler, Coroutine scope 등에서 참조 해제 명확히
        - LiveData, BroadcastReceiver, Room Observer 구독 해제 처리

    - [이미지 메모리 절감]
        - Glide, Coil 등 라이브러리에서 .override(), .fitCenter() 적용
        - Bitmap 불필요할 경우 즉시 recycle() 호출

    - [객체 생성 최소화]
        - ViewHolder, Adapter, 커스텀 뷰 내 반복 처리에서 객체 재사용 원칙 준수
        - ex: Paint, Path, RectF 등은 val로 재사용

    - [GC 및 쓰레드 최적화]
        - GC가 자주 발생하지 않도록 메모리 청크를 효율적으로 관리하고, 불필요한 쓰레드 생성을 방지함.
        - 필요 시 HandlerThread, Executors, CoroutineDispatcher 활용

- Android에서 StrictMode를 활용한 성능 분석 방법
    - [StrictMode 개요]
        - 개발 중에 MainThread에서 발생하는 위험한 작업이나 리소스 누수를 탐지할 수 있는 디버깅 도구임. 
        - 앱 퍼포먼스 디버깅 시 매우 유용함.

    - [ThreadPolicy 설정 예시]
        ```kotlin
        StrictMode.setThreadPolicy(
            StrictMode.ThreadPolicy.Builder()
                .detectAll()
                .penaltyLog()
                .build()
        )
        ```

    - [VmPolicy 설정 예시]
        ```kotlin
        StrictMode.setVmPolicy(
            StrictMode.VmPolicy.Builder()
                .detectLeakedSqlLiteObjects()
                .detectLeakedClosableObjects()
                .penaltyLog()
                .build()
        )
        ```

    - [탐지 가능한 항목 예시]
        - MainThread에서의 네트워크/디스크 I/O
        - Cursor/SQLite 미해제
        - 미닫힌 File/Stream
        - 리소스 누수

    - [활용 방법]
        - 개발 단계에서 Application.onCreate()에 설정해두고, 로그를 통해 문제 코드 탐지 → 리팩터링 유도.
        - 단, 릴리즈 빌드에서는 제거해야 함.

- Android에서 TraceView와 Perfetto를 활용한 성능 분석 방법
    - [TraceView 개요]
        - Android Studio에서 제공하는 UI 트레이싱 도구로, 메서드 단위의 호출 시간, 호출 빈도, 병목 구간을 시각적으로 분석할 수 있음.
        - Debug.startMethodTracing("trace")로 수동 기록 가능.

    - [TraceView 단점]
        - 메서드 호출 단위라서 시스템 수준 분석은 불가능
        - Android Q 이후부터는 Perfetto 사용이 권장됨

    - [Perfetto 개요]
        - 시스템 전반(CPU, 메모리, I/O, 프레임 렌더링 등)을 고정밀 추적할 수 있는 Google의 공식 trace 도구
            - Android Studio → Profiler → Record → System Trace 탭
            - systrace, atrace보다 정밀하고 확장 가능

    - [Perfetto 사용 포인트]
        - Choreographer 프레임 드롭 분석
        - Garbage Collection 시간
        - UI 스레드, RenderThread, Binder call 병목 확인
        - 앱 시작 지연 원인 추적

    - [결과 해석 방법]
        - 프레임 당 16ms 이상 걸리면 dropped frame
        - Idle 시간이 많다면 최적화 가능성 있음
        - UI thread blocking 시, 비동기 처리 고려

- Android에서 RecyclerView의 DiffUtil을 활용하는 방법
    - [DiffUtil 개요]
        - DiffUtil은 RecyclerView의 데이터가 변경될 때 최소한의 업데이트만 수행하도록 도와주는 유틸리티 클래스임.
        - 전체 리스트가 아닌, 변경된 항목만 갱신되므로 성능 및 UX가 향상됨.

    - [구현 방식]
        - (1) DiffUtil.ItemCallback<T> 또는 DiffUtil.Callback을 구현
        - (2) areItemsTheSame() → 같은 항목인지 여부(ID 비교 등)
        - (3) areContentsTheSame() → 내용이 변경되었는지 여부
        ```kotlin
        class MyDiffCallback : DiffUtil.ItemCallback<MyItem>() {
            override fun areItemsTheSame(oldItem: MyItem, newItem: MyItem) = oldItem.id == newItem.id
            override fun areContentsTheSame(oldItem: MyItem, newItem: MyItem) = oldItem == newItem
        }
        ```

    - [실무 적용]
        - ListAdapter 또는 AsyncListDiffer에 전달하여 자동으로 diff 계산 적용함.
        - 대용량 리스트 변경, 애니메이션 적용 시 매우 효과적임.

- Android에서 Jetpack Compose의 UI 테스트를 수행하는 방법
    - [테스트 환경 설정]
        - androidx.compose.ui:ui-test-junit4, 
        - androidx.compose.ui:ui-test-manifest 라이브러리를 추가하고 
        - createAndroidComposeRule<Activity> 사용

    - [기본 구조 예시]
        ```kotlin
        @get:Rule
        val composeTestRule = createAndroidComposeRule<MainActivity>()

        @Test
        fun myButton_isVisible_andClickable() {
            composeTestRule.onNodeWithText("확인").assertIsDisplayed().performClick()
        }
        ```

    - [Node 탐색 방법]
        - onNodeWithText, onNodeWithTag, onAllNodesWithContentDescription 등 다양한 selector 제공
        - Modifier.testTag("myTag")로 노드 식별 가능

    - [동기화 및 애니메이션 대기]
        - Compose 테스트는 기본적으로 UI 상태 변화가 안정될 때까지 자동 대기함.
        - waitUntil, hasAnyDescendant, assertExists 등의 조합으로 복잡한 동작도 검증 가능

    - [실전 팁]
        - 복잡한 UI는 Custom Matcher로 재사용성 높임
        - 상태 변경 후 UI 확인까지 고려하여 Test State 관리 필요

- Android에서 Prefetching과 Lazy Loading의 차이점
    - [Prefetching]
        - 사용자가 필요로 하기 전에 미리 데이터를 가져오는 방식
        - 예: RecyclerView의 setItemViewCacheSize() 또는 PagingConfig.prefetchDistance
        - 장점: 사용자 체감 속도 향상, 스크롤 지연 감소
        - 단점: 불필요한 네트워크/메모리 사용 가능

    - [Lazy Loading]
        - 요청이 있을 때 그 시점에 데이터를 로딩하는 방식
        - 예: Glide의 이미지 로딩, Paging 3의 loadState 기반 로딩 등
        - 장점: 리소스 절약, 필요한 만큼만 처리
        - 단점: 로딩 딜레이로 UX 저하 가능

    - [차이 핵심]
        - Prefetching은 선제적 대비, Lazy Loading은 요청 기반 처리
        - 둘은 조합해서 사용 가능 (예: Lazy Loading 기반이지만 미리 prefetch도 설정)

- Android의 ART(Android Runtime) 최적화 방법
    - [ART 개요]
        - Android 5.0 이상에서 사용되는 런타임으로, AOT 컴파일 + JIT + 인터프리터 조합으로 앱을 실행함.
        - Android 7 이후에는 JIT, Android 9 이후에는 Profile Guided Optimization (PGO) 포함됨.

    - [최적화 방식]
        - AOT (Ahead-Of-Time): 앱 설치 시 바이트코드를 native 코드로 컴파일 → 실행 빠름, 설치 느림
        - JIT (Just-In-Time): 실행 중 자주 호출되는 메서드만 native로 변환 → 설치 빠름, 실행 중 최적화
        - PGO (Profile-Guided Optimization): 사용 프로파일을 기반으로 중요한 경로만 AOT → 앱 시작 속도 개선

    - [Baseline Profile 활용]
        - 자주 실행되는 경로를 미리 지정하여 Google Play나 ART가 해당 메서드를 AOT로 최적화하도록 유도할 수 있음.
        - profileinstaller, baseline-prof.txt 활용

    - [기대 효과]
        - Cold start 최대 30% 단축
        - 첫 진입 화면 렌더링 속도 향상
        - GC 횟수 감소

- Android에서 Firebase Performance Monitoring을 활용하는 방법
    - [기본 개념]
        - Firebase Performance Monitoring은 앱의 실행 시간, 네트워크 응답 속도, 앱 시작 지연 등을 자동 수집해주는 성능 분석 도구임.
        - 앱 릴리즈 이후 실 사용자 환경에서의 성능 데이터를 수집할 수 있음.

    - [적용 방법]
        - firebase-perf 라이브러리 추가 (build.gradle)
        - Firebase 콘솔에서 성능 모니터링 활성화
        - PerformanceMonitoring.getInstance().isPerformanceCollectionEnabled = true (선택)

    - [자동 수집 항목]
        - 앱 시작 시간
        - 화면 렌더링 지연 (slow rendering)
        - HTTP/S 네트워크 요청 시간 (URL, 응답 코드 포함)

    - [커스텀 Trace 측정]
        ```kotlin
        val trace = FirebasePerformance.getInstance().newTrace("custom_trace_name")
        trace.start()
        // 측정할 로직
        trace.stop()
        ```

    - [네트워크 요청 커스터마이징]
        - Retrofit이나 OkHttp에서 FirebasePerfOkHttpClient로 감싸거나
        - addApplicationInterceptor를 사용하여 자동 추적 설정 가능

- Android 14에서 추가된 주요 기능과 변경 사항
    - [사진 접근 권한 세분화]
        - Android 13에 이어 Android 14에서도 READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, READ_MEDIA_AUDIO를 세분화하여
        - 앱이 접근 가능한 미디어 범위 제한 및 사용자 선택 권한 강화

    - [선택적 미디어 접근 허용]
        - 사용자가 이미지 전체가 아닌 선택한 파일만 공유 가능하도록 ACTION_PICK_IMAGES 등 새 API 제공됨

    - [보안 및 권한 강화]
        - PendingIntent가 명시적 인텐트만 허용되도록 제한 강화
        - 앱이 백그라운드에서 포그라운드 서비스 실행 시 시스템 승인 필요

    - [앱 호환성 및 백그라운드 제약 강화]
        - 앱이 백그라운드에서 알림을 생성하려면 POST_NOTIFICATIONS 권한 필요
        - 정지된 앱(suspended app)은 Broadcast 수신 차단됨

    - [새 시스템 동작]
        - Non-dismissable 알림 제한
        - 시스템 UI와 상호작용 시 Full-Screen Intent 제한
        - 앱 타겟 SDK 34 이상 시 동작 방식 변경 필요

- Android에서 Jetpack Macrobenchmark를 활용한 성능 측정 방법
    - [기본 개요]
        - Macrobenchmark는 Cold Start, Warm Start, Scroll, Navigation 등의 성능을 측정하는 Jetpack 도구임.
        - 실제 APK에서 실행되므로 릴리즈 빌드 기준 성능 측정이 가능함.

    - [설정 방법]
        - macrobenchmark 모듈 생성
        - androidx.benchmark.macro.junit4.MacrobenchmarkRule 사용
        - 측정 대상 액티비티를 Intent로 실행하고, UIAutomator로 조작
        ```kotlin
        @get:Rule val benchmarkRule = MacrobenchmarkRule()

        @Test
        fun startupBenchmark() = benchmarkRule.measureRepeated(
            packageName = "com.example.app",
            metrics = listOf(StartupTimingMetric()),
            iterations = 5,
            setupBlock = {
                pressHome()
            },
            measureBlock = {
                startActivityAndWait()
            }
        )
        ```

    - [지원 측정 항목]
        - StartupTimingMetric
        - FrameTimingMetric
        - PowerMetric, CpuUsageMetric, CustomTraceMetric

    - [실무 적용 포인트]
        - release 빌드 기준으로 측정해야 실 성능 반영
        - baseline-prof.txt와 연결하여 최적화 효과 확인
        - 실제 사용 시나리오 기반 측정 루틴 구성

- Android에서 Jetpack Compose로 SEO 대응 웹뷰를 구현하는 방법
    - [기본 한계점]
        - Jetpack Compose 앱 자체는 SEO 크롤러가 인식하지 않기 때문에 
        - SEO는 WebView가 로드하는 웹 콘텐츠에서 대응해야 함.
        - 즉, SEO 대응은 앱이 아닌 웹 콘텐츠 측면에서 이뤄져야 함.

    - [Compose에서 WebView 구현]
        ```kotlin
        AndroidView(factory = {
            WebView(it).apply {
                settings.javaScriptEnabled = true
                loadUrl("https://example.com/seo-page")
            }
        })
        ```

    - [SEO 대응 핵심 전략]
        - WebView 내 페이지가 SSR(Server-Side Rendering) 또는 Prerender 기반으로 구성되어야 함
        - React, Vue 같은 SPA는 meta, og, robots.txt, structured data 등을 HTML에 직접 포함시켜야 함
        - WebView의 User-Agent를 크롤러에 맞게 설정하거나 대응

    - [테크니컬 대응 방법]
        - WebView.getSettings().userAgentString으로 커스터마이징
        - shouldOverrideUrlLoading 또는 WebViewClient에서 redirect 흐름 제어
        - SEO를 위한 noindex, canonical, og:image, description 등 메타 태그 포함된 HTML을 로드해야 함

- Android에서 TensorFlow Lite를 활용한 AI/ML 모델 적용 방법
    - [TFLite 개요]
        - TensorFlow Lite는 모바일 및 엣지 디바이스용 경량 머신러닝 프레임워크로, .tflite 확장자의 모델 파일을 Android에서 로드하여 추론 가능.

    - [기본 적용 흐름]
        - 모델을 .tflite 파일로 변환 (TensorFlow → TFLite Converter)
        - tflite-model 파일을 assets에 추가
        - Interpreter 또는 ML Model Binding으로 로드 후 추론 수행

    - [코드 예시]
        ```kotlin
        val interpreter = Interpreter(loadModelFile("model.tflite"))
        val input = floatArrayOf(...)
        val output = Array(1) { FloatArray(RESULT_SIZE) }
        interpreter.run(input, output)
        ```

    - [최적화 전략]
        - Quantization (int8, float16 등)으로 추론 속도 및 메모리 절약
        - GPU / NNAPI Delegate로 하드웨어 가속
        - Model metadata 추가 시 입출력 텐서 이름 생략 가능

- Android의 Low Latency Rendering을 구현하는 방법
    - [Low Latency 목표]
        - UI → GPU → Display까지의 지연을 최소화하여 빠르고 부드러운 사용자 반응성 확보.
        - 특히 실시간 카메라, 게임, 미디어 앱에서 중요.

    - [최적화 전략]
        - Choreographer.postFrameCallback을 활용해 프레임 타이밍을 조절
        - SurfaceView / TextureView / OpenGL ES 사용 시 하드웨어 직접 렌더링 유도
        - setWillNotDraw(true)로 불필요한 draw 생략

    - [Jetpack Compose에서 대응]
        - Modifier.graphicsLayer() 최소 사용
        - 리컴포지션 범위 제한 (derivedStateOf, key, remember)
        - SnapshotFlow로 상태 변경 감지 시점 최적화

    - [도구 활용]
        - Profile GPU Rendering
        - Perfetto / Systrace
        - FrameMetricsAggregator (API 24+) 로 렌더링 타임 측정 가능

- Android에서 Jetpack CameraX를 활용하는 방법
    - [CameraX 개요]
        - Jetpack CameraX는 기존 Camera2 API의 복잡성을 줄이고 Lifecycle-aware, 간단한 카메라 기능 구현을 도와주는 Jetpack 라이브러리.

    - [기본 구성 요소]
        - Preview: 미리보기
        - ImageCapture: 사진 촬영
        - ImageAnalysis: 실시간 프레임 분석
        - CameraSelector: 전/후면 카메라 지정

    - [설정 및 코드 예시]
        ```kotlin
        val cameraProvider = ProcessCameraProvider.getInstance(context).get()
        val preview = Preview.Builder().build().also {
            it.setSurfaceProvider(previewView.surfaceProvider)
        }
        val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA
        cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, preview)
        ```

    - [고급 기능]
        - 실시간 얼굴 인식, QR 분석 시 ImageAnalysis 활용
        - HDR, 줌, 플래시 등은 Camera2Interop으로 확장
        - CameraX Extensions API로 Bokeh, Night, HDR 등의 특수 모드 지원

- Google Play 정책 변경이 앱 개발에 미치는 영향
    - [권한 제한 강화]
        - Android 11 이후로 백그라운드 위치, 전화/문자 접근, 알림 권한 등 민감 권한은 사용 제한 강화
            - ACCESS_BACKGROUND_LOCATION 사용 시 심사 필요
            - Android 13~14: READ_MEDIA_*, POST_NOTIFICATIONS로 세분화됨

    - [타겟 SDK 요구사항 강화]
        - 매년 타겟 SDK 상향 요구됨 (현재 기준: SDK 34 이상)
            - → 미대응 앱은 스토어 노출 제한, 업데이트 불가, 신규 앱 등록 제한 발생

    - [정책 위반 시 영향]
        - 앱 삭제, 계정 정지
        - 결제 정책 위반 시 IAP 차단
        - 민감 권한 위반 시 앱 노출 불가

    - [개발자 대응 전략]
        - 정기적으로 정책 변경 공지 확인
        - Privacy Policy, 권한 사용 사유, 민감 정보 처리 방식을 명확히 명시
        - 앱심사 요청 시 스크린샷, 데모영상, 정책 설명 문서를 함께 제출하여 리젝 방지

- Android에서 WebRTC를 활용한 실시간 영상 통화 구현 방법
    - [WebRTC 개요]
        - WebRTC는 Google이 주도한 브라우저 및 네이티브에서의 실시간 P2P 영상/음성 통신 프로토콜임. 
        - Android에선 Java/Kotlin 기반 SDK로 제공됨.

    - [기본 구성 요소]
        - PeerConnection: P2P 연결 담당
        - MediaStream, MediaTrack: 영상/음성 데이터 스트림
        - SurfaceViewRenderer: 영상 출력 뷰
        - Signaling Server: SDP/ICE candidate 교환 (직접 구현 필요, WebSocket 등 활용)

    - [구현 순서]
        - WebRTC 라이브러리 의존성 추가 (Maven 또는 aar 수동 빌드)
        - 카메라/마이크 권한 요청
        - PeerConnectionFactory 초기화
        - MediaStream 생성 및 addTrack()
        - PeerConnection 구성, signaling 서버를 통해 offer/answer/sdp/candidate 교환
        - SurfaceViewRenderer로 내/외부 영상 렌더링

    - [실전 팁]
        - 네트워크 NAT, TURN/STUN 서버 고려 필수
        - 영상 해상도 및 FPS는 성능 최적화 핵심
        - signaling 서버는 WebSocket 또는 Firebase 활용 가능

- WebRTC 동작 흐름 요약 (기기 A <-> 기기 B)
    - [1. Signaling 시작 (초기 연결 수립 준비)]
        - 역할: 두 클라이언트가 통신을 시작하기 위한 SDP (Session Description Protocol) 와 ICE Candidate 정보를 주고받는 과정
        - 방법: WebRTC 자체에는 signaling이 없으므로 직접 WebSocket, Firebase, MQTT 등으로 구현해야 함
        - 초기 흐름:
            - A가 offer SDP 생성 → signaling 서버를 통해 B에게 전달
            - B가 answer SDP 생성 → A에게 전달

    - [2. PeerConnection 생성 및 구성]
        - 양쪽 모두 PeerConnection 객체를 생성
        - 필요한 ICE 서버 정보(STUN/TURN) 등록
        - 미디어 스트림(Local Camera/Audio 등)을 연결에 추가
        ```kotlin
        val peerConnection = peerConnectionFactory.createPeerConnection(iceServers, observer)
        ```

    - [3. SDP 교환 (Offer/Answer)]
        - A: createOffer() 호출 → setLocalDescription()
        - B: setRemoteDescription() 후 createAnswer() → setLocalDescription() → A에 전송

    - [4. ICE Candidate 교환]
        - ICE(Interactive Connectivity Establishment): 실제 통신 경로(IP, 포트 등)를 찾는 과정
        - 양쪽에서 onIceCandidate 콜백이 발생할 때마다 상대방에게 전달
        - 모든 후보(Candidate)를 교환한 후 가장 효율적인 경로로 연결 수립
        ```kotlin
        peerConnection.onIceCandidate = { candidate ->
            signaling.send(candidate)
        }
        ```

    - [5. 연결 완료 및 미디어 스트림 전달]
        - SDP와 ICE 교환이 완료되면 연결이 수립됨 (→ onAddStream, onTrack 콜백 발생)
        - SurfaceViewRenderer나 TextureView에 미디어 스트림을 연결해 렌더링함

    - [6. 실시간 통신 시작]
        - 영상/음성이 P2P 방식으로 전달됨
        - NAT, 방화벽 회피를 위해 TURN 서버를 통해 릴레이할 수도 있음
        - 통신 도중 ICE candidate가 추가되면 계속 반영 가능 (ICE trickling)

    - WebRTC 전체 흐름 시각 요약
        - Signaling 연결 (WebSocket 등)
        - PeerConnection 생성 + ICE 서버 설정
        - SDP Offer/Answer 교환
        - ICE Candidate 교환
        - Connection 수립 (ICE 연결 완료)
        - 미디어 스트림 교환 및 렌더링

- Android에서 onSaveInstanceState()와 ViewModel의 차이점
    - [공통 목적]
        - 둘 다 Activity/Fragment 상태가 파괴될 때 데이터를 유지하기 위해 사용되지만, 사용 시점과 보존 범위가 다름.

    - [onSaveInstanceState()]
        - 기기 회전, 프로세스 킬 후 재생성 등에서 일시적인 상태 보존에 사용
        - Bundle에 저장 가능한 크기 제한 있음 (약 1MB 이하)
        - UI 관련 데이터(스크롤 위치, 입력값 등) 보존에 적합
        - 생명주기: onSaveInstanceState() → onCreate(savedInstanceState)로 복원

    - [ViewModel]
        - UI 상태, 로직 데이터, 비동기 처리 결과 유지에 사용
        - Configuration 변경(Activity 재생성)에도 소멸되지 않음
        - 프로세스가 완전히 종료되면 유지되지 않음
        - LiveData, StateFlow, repository와 함께 구조화 가능

    - [핵심 차이]
        - ViewModel: 메모리 상 유지, 복잡한 상태와 UI 로직 담당
        - onSaveInstanceState: 저장소 기반 일시 복원, 간단한 UI 상태 처리에 적합

- Android의 Activity와 Fragment의 생명주기에서 주요 차이점
    - [Activity 생명주기]
        - 앱의 한 화면(단독 실행 단위)으로, onCreate → onStart → onResume → onPause → onStop → onDestroy 순서
        - 생성 -> 시작 -> 재개 -> 중지 -> 정지 -> 파괴
        - Activity 종료 시 OS에 의해 완전히 파괴됨

    - [Fragment 생명주기]
        - Activity에 의존적인 화면 구성 단위
        - onAttach → onCreate → onCreateView → onViewCreated → onStart → onResume 등 View 중심 생명주기가 추가됨
        - onDestroyView() 이후에도 Fragment 인스턴스는 메모리에 남아 있을 수 있음

    - [핵심 차이점]
        - Fragment는 UI(View) 생명주기와 자체 생명주기가 분리되어 있음
        - Fragment는 addToBackStack()을 통해 백스택 관리 가능
        - Activity는 앱 내에서 독립적인 context이고, Fragment는 조립형 UI 구조의 일부임

- Jetpack Lifecycle Observer의 역할과 활용 방법
    - [LifecycleObserver 개요]
        - LifecycleObserver는 Activity/Fragment의 생명주기 변화에 비침투적으로 반응하는 컴포넌트 구조를 제공함.
        - → 메모리 누수 방지, 명확한 구조화에 도움

    - [사용 예시]
        ```kotlin
        class MyObserver : DefaultLifecycleObserver {
            override fun onStart(owner: LifecycleOwner) {
                // 생명주기 이벤트 대응
            }
        }
        lifecycleOwner.lifecycle.addObserver(MyObserver())
        ```

    - [주요 활용 사례]
        - Sensor, Location Listener 등록/해제
        - 카메라, 오디오, 타이머 등 리소스 관리
        - Compose, Room, Retrofit 등의 비동기 작업 Lifecycle-aware하게 구성

    - [장점]
        - ViewModel, UseCase, Manager 등 다양한 계층에 안전하게 생명주기 의존 로직 분리 가능
        - 수동으로 onStart() 등 호출할 필요 없이 자동으로 연결됨

- Android에서 Multi-Window를 지원하는 방법
    - [기본 개념]
        - Multi-Window는 하나의 화면에 두 개 이상의 앱을 동시에 표시하는 기능으로, Android 7.0 (API 24)부터 지원됨.
        - 사용자 멀티태스킹 및 대화면 UX 대응에 필수적임.

    - [지원 설정 방법]
        - AndroidManifest.xml에 다음 속성 추가:
        ```xml
        <activity
            android:resizeableActivity="true"
            android:supportsPictureInPicture="true" />
        ```

    - [주의 사항]
        - onMultiWindowModeChanged() 콜백에서 레이아웃 대응 필요
        - 화면 크기가 줄어들 수 있어 ConstraintLayout, Compose, WindowMetrics 등으로 동적 UI 대응
        - 화면 비율, orientation 변경 감안

    - [실전 대응 포인트]
        - 비디오 플레이어: Picture-in-Picture(PiP) 모드 연동
        - 채팅/메신저 앱: Multi-instance 구성 고려
        - Compose에서는 WindowSizeClass 활용해 레이아웃 분기 가능

- Android에서 Foldable(접이식) 디바이스 대응 방법
    - [기기 특성]
        - Foldable 디바이스는 하나의 앱이 여러 화면 크기, 비율, 접힘 상태에서 동작해야 하므로 Window 상태 변화 감지 및 반응형 UI 설계가 중요함.

    - [Jetpack WindowManager 활용]
        - androidx.window:window 라이브러리를 사용하여 fold 상태, hinge 위치, layout bounds를 감지

    - [주의할 점]
        - WindowSizeClass로 화면 크기 대응 (Compact/Medium/Expanded)
        - isSeparating, FoldingFeature로 분할 UI 구성
        - 화면 회전 시 각 레이아웃 크기, 비율 변경 고려

    - [실전 활용 예]
        - Chat 앱 → 좌: 리스트 / 우: 상세
        - 이메일 앱 → 분할 레이아웃 대응
        - 게임 → 접힌 상태 시 미니맵 표시

- Android에서 OpenGL ES를 활용한 그래픽 렌더링 최적화 방법
    - [OpenGL ES 개요]
        - OpenGL ES는 Android에서 저수준 하드웨어 가속 2D/3D 렌더링을 위한 그래픽 API로, 게임, AR/VR, 실시간 시각화에 사용됨.

    - [최적화 전략]
        - Draw Call 최소화: glDrawArrays() 호출 횟수 줄이기, batching 처리
        - VBO(Vertex Buffer Object) 사용으로 정점 데이터 GPU에 캐싱
        - 텍스처 압축 사용: ETC2, ASTC 포맷 활용해 메모리 절약
        - Framebuffer Object (FBO): 오프스크린 렌더링으로 성능 향상
        - Viewport 최적화: 실제 화면 크기에 맞게 조정해 불필요한 픽셀 렌더링 제거

    - [개발 도구 활용]
        - Android GPU Inspector (AGI)
        - Adreno Profiler (퀄컴 디바이스)
        - Mali GPU Tools (ARM 디바이스)

    - [주의 사항]
        - glFinish()는 강제 GPU 동기화 → 성능 저하 유발
        - glGetError() 호출 과다 시 성능 악영향
        - 메모리 누수 방지 위해 glDeleteBuffers, glDeleteTextures 필요

- Android에서 Material 3 디자인 시스템을 적용하는 방법
    - [Material 3 개요]
        - Material 3 (또는 Material You)는 Google의 최신 디자인 시스템으로, 동적 색상, adaptive 컴포넌트, 모던 스타일링을 제공함.

    - [적용 방법 (Compose 기준)]
        - (1) 의존성 추가
            - implementation("androidx.compose.material3:material3:1.1.0")
        - (2) Theme 설정
            ```kotlin
            MaterialTheme(
                colorScheme = dynamicLightColorScheme(context),
                typography = Typography,
                shapes = Shapes
            ) {
                // UI content
            }
            ```
    - [Material 3 특징]
        - 동적 색상: 시스템 배경 기반 자동 테마 적용 (Android 12 이상)
        - 모양, 간격, 애니메이션 개선
        - Composable 기반 컴포넌트 확장 (e.g. CenterAlignedTopAppBar, NavigationDrawer 등)

    - [실전 대응 팁]
        - Legacy MaterialTheme 대신 androidx.compose.material3.MaterialTheme 사용
        - 커스텀 colorScheme 정의 시 lightColorScheme, darkColorScheme 사용
        - M2 → M3 전환 시는 전용 컴포넌트로 교체 필요 (예: TopAppBar → CenterAlignedTopAppBar)

- Jetpack Compose로 Widget을 만드는 방법
    - [Compose 기반 위젯은 직접적으로 불가능]
        - Jetpack Compose 자체는 아직 App Widget(View 기반)에서 직접 사용이 불가능함.
            - → 대신 Jetpack Glance를 통해 Compose 스타일로 위젯을 구성할 수 있음.

    - [기존 Compose에서는 아래 방식 불가]
        - 일반 @Composable은 위젯 RemoteViews로 변환할 수 없음
        - 따라서 AppWidgetProvider 방식 + RemoteViews로만 구성됨

    - [대안]
        - → Jetpack Glance 사용 (Compose-like DSL로 RemoteViews 생성)
        - → Android 12 이상에서는 일부 OS 위젯 영역에 Compose 적용 예정


- Android에서 Jetpack Glance를 활용한 위젯 개발 방법
    - [Glance 개요]
        - Jetpack Glance는 Compose-like 문법을 사용해 앱 위젯(AppWidget)을 선언적으로 구성할 수 있게 해주는 라이브러리임.
        - 내부적으로 RemoteViews를 생성하지만 더 간결하게 UI 정의 가능.

    - [기본 구조 예시]
        ```kotlin
        class MyWidget : GlanceAppWidget() {
            @Composable
            override fun Content() {
                Text("안녕하세요!", style = TextStyle(fontSize = 18.sp))
            }
        }

        class MyWidgetReceiver : GlanceAppWidgetReceiver() {
            override val glanceAppWidget = MyWidget()
        }
        ```

    - [구성 요소]
        - GlanceAppWidget: 위젯 UI 정의
        - GlanceAppWidgetReceiver: Manifest에 등록되는 수신자
        - update(), actionRunCallback() 등으로 동적 처리 가능

    - [제약사항]
        - Compose처럼 복잡한 View 트리는 불가능
        - Image, Text, Button, Column, Row 등 제한된 컴포넌트만 지원
        - 모든 로직은 RemoteViews 제약을 따름

- Android에서 Dynamic Feature Module을 활용하는 방법
    - [기본 개요]
        - Dynamic Feature Module은 앱 설치 시 필수 기능만 설치하고, 선택 기능은 필요 시 다운로드하는 구조를 가능하게 함.
        - → 앱 초기 설치 용량 감소, 기능 단위 업데이트 가능

    - [기본 구성]
        - (1) Base Module (앱 기본 기능)
        - (2) Feature Module (install-time, on-demand, conditional 설치 가능)
        - (3) Play Core API로 런타임 중 다운로드 및 실행

    - [Manifest 설정 예시]
        ```xml
        <dist:module
            dist:onDemand="true"
            dist:title="@string/feature_title" />
        ```

    - [호출 방법 예시]
        - SplitInstallManager.requestInstall(SplitInstallRequest.newBuilder().addModule("feature_name").build())

    - [활용 사례]
        - AR 기능, 고급 설정, 관리자 도구 등 비일상적 기능
        - 국가/디바이스별 기능 분리 배포

    - [주의 사항]
        - Instant App과 호환 불가
        - Base 모듈에서 Feature 모듈 코드를 직접 참조 불가 → Reflection 또는 Navigation 사용 권장

- Android에서 Baseline Profiles을 활용한 성능 최적화 방법
    - [개요]
        - Baseline Profiles는 앱의 핵심 경로(startup, navigation 등)의 메서드 호출 정보를 미리 컴파일하도록 가이드하여 앱 실행 성능을 향상시킴.

    - [적용 흐름]
        - (1) baseline-profile 모듈 생성
        - (2) ProfileInstaller 라이브러리 추가
        - (3) BaselineProfileRule을 사용하여 프로파일 자동 생성
        - (4) 생성된 baseline-prof.txt를 앱 모듈에 포함

    - [테스트 코드 예시]
        ```kotlin
        @get:Rule val baselineProfileRule = BaselineProfileRule()

        @Test
        fun generateStartupProfile() = baselineProfileRule.collectBaselineProfile(
            packageName = "com.example.app"
        ) {
            startActivityAndWait()
            // 주요 네비게이션 동작 수행
        }
        ```

    - [실제 효과]
        - 앱 Cold Start 속도 최대 30~40% 단축
        - 초기 렌더링 프레임 개선
        - Profile 기반으로 ART가 AOT 컴파일 수행 가능

    - [적용 시점]
        - Google Play에 업로드하면 자동으로 활용됨.
        - 로컬 테스트 시에는 adb shell cmd package compile 명령으로 직접 적용 확인 가능

- Android 앱에서 Zero Trust Security를 구현하는 방법
    - [Zero Trust 개요]
        - Zero Trust는 “아무도 신뢰하지 않는다(Trust No One)”는 보안 모델로, 앱 내에서도 사용자, 디바이스, 네트워크 모두 검증 기반으로 접근 제어함.

    - [핵심 구성 요소]
        - 인증 강화: MFA, 생체인증, OAuth2, FIDO2 등
        - 디바이스 상태 검증: 루팅 여부, 악성 앱 탐지, OS 버전 체크
        - 네트워크 검증: VPN 우선 사용, TLS pinning, 비인가 IP 차단
        - 최소 권한 원칙 적용: 민감 API, 로컬 저장소 접근 제한

    - [실전 적용 예시]
        - 로그인 후 토큰 기반 API 접근 (Refresh 포함)
        - SafetyNet, Play Integrity API, Attestation 으로 디바이스 무결성 확인
        - 인증 토큰 만료 시 자동 로그아웃 및 토큰 재검증

    - [추가 전략]
        - 앱 내 SecureStorage 사용 (EncryptedSharedPreferences, Keystore)
        - 사용자별 기능 접근 제한 (RBAC 적용)

- Android에서 AI 기반 추천 시스템을 구현하는 방법
    - [기본 개념]
        - AI 추천 시스템은 사용자의 행동, 선호, 맥락을 기반으로 콘텐츠 또는 기능을 추천하는 구조로, 협업 필터링, 콘텐츠 기반 필터링 등이 대표적임.

    - [구현 방식]
        - 클라이언트 기반 (Lightweight): 사용자 행동 로그 분석 → 모델 적용 (ex: TF Lite)
        - 서버 기반: Firebase, TensorFlow Serving 등 백엔드에서 추천 결과 제공

    - [Android 구현 흐름 예시]
        - 유저 행동 수집: 클릭, 검색어, 체류 시간
        - 로컬 저장 또는 서버 전송
        - 추천 결과를 서버에서 받고 RecyclerView 등 UI에 반영
        - or, 사전 학습된 .tflite 모델로 실시간 유사도 계산

    - [라이브러리 및 도구]
        - Firebase Recommendations
        - TensorFlow Lite + MLModelBinding
        - Scikit-learn 기반 서버 추천 API

    - [실전 활용 예]
        - 쇼핑앱: 비슷한 상품 추천
        - 미디어 앱: 유사 콘텐츠 자동 추천
        - 위치/시간 기반 개인화 추천

- Android에서 Jetpack Compose로 Instant Apps를 만드는 방법
    - [Instant Apps 개요]
        - 사용자가 앱을 설치하지 않고도 일부 기능을 체험할 수 있는 Android 기능.
            - → 특정 기능만 노출하여 다운로드 유도 가능

    - [Compose Instant App 구성 방식]
        - 기본은 View 기반이지만, Compose 앱도 Dynamic Feature + Instant App 규칙을 적용하면 지원 가능
        - Compose 자체는 제한 없지만 Module 분리와 경량화 구조 필수

    - [구현 흐름]
        - base 모듈 + feature 모듈로 앱 구성
        - Instant App 모듈 생성 (.instantapp)
        - URL routing (App Links) 또는 IntentFilter로 진입점 설정
        - Compose UI는 feature 모듈 내 구성

    - [제약 조건]
        - 전체 앱 크기 15MB 이하 권장
        - 로그인, 결제, 저장소 접근 등에 제한 있음
        - Play Store Console에서 별도 테스트 필요

    - [활용 사례]
        - 체험판 게임
        - 공유 가능한 특정 화면
        - 쇼핑앱에서 상품 상세만 미리보기

- Android에서 AI 기반 음성 인식을 활용하는 방법
    - [기본 구현 방식]
        - Android SpeechRecognizer (내장)
        - Google Cloud Speech-to-Text API
        - Custom TFLite 모델 기반 음성 인식

    - [내장 SpeechRecognizer 예시]
        ```kotlin
        val recognizer = SpeechRecognizer.createSpeechRecognizer(context)
        recognizer.setRecognitionListener(...)
        val intent = RecognizerIntent.getVoiceDetailsIntent(context).apply {
            putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
        }
        recognizer.startListening(intent)
        ```
    - [Cloud 기반 고정밀 인식]
        - Google Cloud Speech API를 사용하면 노이즈 억제, 다중 언어, 실시간 스트리밍 지원
        - 단, 인터넷 연결 필수 + 비용 발생

    - [실전 응용 예]
        - 음성 명령 기반 제어 앱 (예: “라이트 꺼줘”)
        - 키오스크, 자동차, IoT 인터페이스
        - 자막 생성, 전화 녹취 분석

    - [주의할 점]
        - 권한: RECORD_AUDIO
        - UI thread blocking 방지 (비동기 처리 필수)
        - 배터리/데이터 소모 고려

- Intent를 통해 데이터 전달하는 과정에서 클래스 객체를 바로 전달하지 못하는 이유와 전달하기 위해 필요한 작업 그리고 액티비티 간 데이터 전달을 위해 Intent를 사용하는 이유
    - [문제 원인]
        - Intent는 내부적으로 Parcel이라는 직렬화 포맷을 사용하여 데이터를 주고받음.
        - → 일반 클래스는 Parcelable 또는 Serializable이 아니면 Parcel로 변환 불가능 → 런타임 예외 발생

    - [해결 방법]
        - Parcelable 인터페이스 구현
            - 더 빠르고 Android에 최적화
            - @Parcelize 애노테이션 사용하면 자동 생성 가능
            ```kotlin
            @Parcelize
            data class User(val name: String, val age: Int) : Parcelable
            ```
        - Serializable 구현
            - 자바 표준 방식이지만 느리고 비효율적
            - 단순 테스트용/임시 용도 외에는 비추천

    - [Activity 간 데이터 전달 시 Intent 사용하는 이유]
        - Activity는 Android OS에서 Intent 기반으로 관리되기 때문에 시스템적으로 안전하게 데이터 전달 가능
        - 명시적/암시적 호출이 모두 가능
        - Bundle과 함께 다양한 타입의 데이터 전달 가능
        - 구조적으로 UI 간 느슨한 결합을 유지

- 복수의 Fragment 간 데이터 전달 방법
    - [1. ViewModel 공유 방식 (권장)]
        - activityViewModels() 또는 sharedViewModel()을 통해 동일한 ViewModel을 공유
        - 상태 보존 + Lifecycle-aware
        ```kotlin
        class SharedViewModel : ViewModel() {
            val selectedItem = MutableLiveData<String>()
        }
        ```

    - [2. FragmentResult API 사용 (Jetpack 제공)]
        - Fragment → Fragment 간 안전한 통신 (Navigation 사용 시에도 유용)
        ```kotlin
        // 보내는 쪽
        parentFragmentManager.setFragmentResult("requestKey", bundleOf("key" to value))

        // 받는 쪽
        setFragmentResultListener("requestKey") { _, bundle ->
            val result = bundle.getString("key")
        }
        ```

    - [3. Navigation Component 이용 시 SafeArgs 활용]
        - XML에서 argument 정의 → 자동으로 타입 안전 클래스 생성
        - Navigation Graph 기반 프로젝트에서 권장

    - [4. Interface 콜백 방식 (구식/비추천)]
        - Fragment → Activity → 다른 Fragment로 직접 전달
        - 강한 결합 발생 → 유지보수 어려움

- Width가 1000px Height가 20000px인 이미지가 있고 해당 이미지를 보여주려고 했을 때 아래와 같은 에러가 떴다.
- 이를 이미지 라이브러리를 사용하지 않고 해결하는 방법에 대한 설명
    - 에러: W/OpenGLRenderer: Bitmap too large to be uploaded into a texture (max=2048x2048)

    - [문제 원인]
        - Android의 GPU/OpenGL은 텍스처로 업로드할 수 있는 최대 사이즈 제한이 있음 (일반적으로 2048x2048 또는 4096x4096)
        - → 1000x20000은 세로 길이가 초과되어 OpenGL에서 처리 불가능

    - [해결 방법]
        - Canvas + ScrollView 사용 (이미지를 분할하여 그리기)
            - BitmapRegionDecoder를 활용해 세로로 분할한 이미지 조각을 순차적으로 그려주면 전체 이미지 표현 가능

        - WebView 사용
            - WebView는 내부적으로 GPU 제한을 받지 않고 HTML <img>로 긴 이미지를 처리 가능

        - SurfaceView 또는 TextureView + 수동 렌더링
            - Canvas.drawBitmap(...)으로 화면에 보이는 부분만 수동으로 그리는 방식
            - 더 복잡하지만 유연한 제어 가능

        - ImageView + Matrix 사용해 가상 스크롤 구현
            - 전체 이미지를 보여주지 않고, 현재 보이는 위치만 Bitmap.createBitmap()으로 잘라서 표시
    
    - [주의 사항]
        - 절대 ImageView.setImageBitmap()에 초대형 이미지 그대로 넣지 말 것 → OOM 발생
        - 가능한 경우 이미지 리사이징 또는 분할이 정석적인 해결책

- BitmapRegionDecoder로 초대형 이미지 표시 예시
    - 준비물: 1000x20000 크기의 초대형 이미지 파일 (예: assets 폴더에 long_image.jpg)
    - 이미지 분할 후 ImageView에 표시 (스크롤 기반)
        - 이 커스텀 뷰는 세로로 1000px 단위로 잘라서 화면에 쌓아 그리는 방식으로 GPU 제한을 피함. 
        - 성능 개선을 위해 현재 View 높이 내에서만 draw 되도록 최적화도 가능.
        ```kotlin
        class LargeImageView(context: Context, attrs: AttributeSet) : View(context, attrs) {

            private lateinit var decoder: BitmapRegionDecoder
            private val paint = Paint()
            private val options = BitmapFactory.Options().apply {
                inPreferredConfig = Bitmap.Config.RGB_565
            }

            private val regionHeight = 1000
            private var imageWidth = 0
            private var imageHeight = 0

            init {
                val inputStream = context.assets.open("long_image.jpg")
                decoder = BitmapRegionDecoder.newInstance(inputStream, false)
                imageWidth = decoder.width
                imageHeight = decoder.height
            }

            override fun onDraw(canvas: Canvas) {
                var yOffset = 0
                while (yOffset < imageHeight) {
                    val bottom = (yOffset + regionHeight).coerceAtMost(imageHeight)
                    val rect = Rect(0, yOffset, imageWidth, bottom)
                    val bitmap = decoder.decodeRegion(rect, options)
                    canvas.drawBitmap(bitmap, 0f, yOffset.toFloat(), paint)
                    yOffset += regionHeight
                }
            }
        }
        ```

- Jetpack Compose를 기존 XML 방식과 비교했을 때의 장점과 단점
    - [장점]
        - 선언형 UI
            - UI 상태(state)에 따라 자동으로 UI가 갱신됨 → 코드가 간결하고 예측 가능
        - 코드 통합
            - XML과 Kotlin이 분리되지 않고 한 파일에서 UI와 로직을 함께 작성 가능
        - 재사용성과 테스트 용이
            - Composable 함수 단위로 구조화 가능 → Preview, 단위 테스트, Slot API 활용 용이
        - Animation, State 관리 간편화
            - 내장된 animate*AsState, remember, derivedStateOf 등으로 자연스러운 애니메이션과 상태 추적 가능
        - 호환성
            - 기존 View 시스템과 혼합 사용 가능 (AndroidView, ViewBinding 등)
    - [단점]
        - 러닝 커브
            - 기존 View 시스템에 익숙한 개발자에겐 새로운 Compose 개념(State Hoisting, recomposition 등)이 낯설 수 있음
        - 성능 디버깅 어려움
            - 초기엔 recomposition 관련 디버깅이 복잡하며, 잘못 사용할 경우 성능 저하 유발
        - Jetpack 라이브러리/서드파티 대응 제한
            - 모든 Jetpack/서드파티 라이브러리가 Compose를 완전히 지원하는 건 아님 (ex. 지도 SDK 등)
        - 툴링 제약
            - Preview나 Layout Inspector 기능이 완전하지 않을 때도 있음 (버전 이슈, IDE 문제 등)

- Android Lifecycle에 대해 설명하고, ViewModel이 어떻게 메모리 관리를 도와주는지 설명
    - [Android Lifecycle 개요]
        - Activity/Fragment는 OS 상태에 따라 onCreate → onStart → onResume → onPause → onStop → onDestroy 생명주기를 순차적으로 가짐
        - → 생명주기마다 UI/리소스 해제 또는 초기화를 적절히 수행해야 메모리 누수 방지

    - [ViewModel의 역할]
        - ViewModel은 Activity/Fragment의 Lifecycle보다 더 오래 살아남는 상태 저장소
            - 화면 회전 등 Configuration 변경에도 살아남음
            - ViewModelStore에 저장되어 onDestroy() 이전까지 유지됨
            - ViewModel 내부의 코루틴은 viewModelScope 사용 시 자동으로 Lifecycle 종료에 따라 취소됨

    - [메모리 관리 기여]
        - UI 상태/비즈니스 로직 분리로 Activity/Fragment에 의존성 감소
        - 비동기 작업이 Lifecycle에 안전하게 연동됨 (LiveData, StateFlow 등)
        - ViewModel이 메모리를 점유하더라도 View가 종료되면 자동 해제됨 → 누수 위험 감소

- Coroutine과 LiveData의 차이
    - [공통점]
        - 둘 다 비동기 처리 및 UI 상태 전달에 활용됨

    - [LiveData]
        - Lifecycle-aware 데이터 전달 도구
        - Activity/Fragment가 STARTED 이상 상태일 때만 자동으로 observe
        - 데이터 변경만 전달하며, 내부적으로 MainThread에서 동작
        - Configuration 변경에도 Observer는 자동 재연결됨

    - [Coroutine]
        - 비동기 흐름 제어 자체에 집중한 Kotlin 언어 레벨 기능
        - launch, async, withContext 등을 활용한 비동기 블록
        - Lifecycle에 연결하려면 viewModelScope, lifecycleScope 등을 명시적으로 사용해야 함
        - Flow와 함께 사용할 경우 LiveData처럼 구독/취소가 가능하며 더 유연하고 강력함

    - [핵심 차이]
        - LiveData는 UI 상태 관리에 적합한 고수준 API
        - Coroutine은 비동기 로직 처리에 더 적합한 저수준 구조
        - LiveData는 무거운 로직 처리에 불리하고, Coroutine은 직접 Lifecycle 관리가 필요함

- Flow와 StateFlow, SharedFlow의 차이점
    - [공통점]
        - 모두 Kotlin Coroutines 기반 비동기 데이터 스트림 API
        - → cold stream vs hot stream, 단일 구독 vs 다중 구독 여부에서 차이 발생

    - Flow
        - [특징]
            - Cold Stream (collect되기 전까지 아무 작업 없음)
            - collect가 시작될 때마다 새롭게 실행됨 (1:1 관계)
            - 기본적으로 한 번의 수신자만 가능

        - [사용 예]
            - Repository에서 네트워크/DB 결과를 1회성으로 방출
            - 비동기 데이터 스트림

    - StateFlow
        - [특징]
            - Hot Stream + 상태 보존 (항상 최신 값을 1개 유지)
            - 기본값이 반드시 있어야 함 (StateFlow("초기값"))
            - collect하면 항상 가장 최근 값부터 수신
            - ViewModel의 UI 상태 저장에 적합

        - [사용 예]
            - val uiState = MutableStateFlow(UiState())
            - ViewModel에서 UI 상태 전파

    - SharedFlow
        - [특징]
            - Hot Stream + 상태 없음 (즉시 소멸)
            - 기본값 필요 없음
            - 여러 수신자에게 이벤트 broadcast 가능 (1:N 구조)
            - 이벤트 보존 버퍼 설정 가능 (replay, extraBufferCapacity)

        - [사용 예]
            - UI 단발성 이벤트 처리 (ex: Toast, Navigation, Dialog 호출)
            - val event = MutableSharedFlow<Event>()

- SharedFlow replay, extraBufferCapacity 속성 설정
    - [replay]
        - 역할:
            - 새로운 수집자(collect)가 붙었을 때, 이전에 방출된 이벤트 중 몇 개를 다시 전달할지 설정

        - 예시:
            ```kotlin
            val sharedFlow = MutableSharedFlow<Int>(replay = 2)
            sharedFlow.emit(1)
            sharedFlow.emit(2)
            sharedFlow.emit(3)

            sharedFlow.collect { println(it) }
            ```
            - -> 출력 결과: 2, 3 (마지막 2개의 이벤트가 replay 된다)
        - 주의 사항:
            - replay 캐시는 수집자가 collect 하기 전에 발생한 이벤트를 재전달
            - replay 버퍼도 메모리를 차지하므로 적절한 크기 관리 필요

    - [extraBufferCapacity]
        - 역할:
            - 수집자가 처리하지 못할 경우를 대비해, replay 외에 추가로 버퍼에 쌓을 수 있는 이벤트 수

        - 예시:
            ```kotlin
            val sharedFlow = MutableSharedFlow<Int>(
                replay = 1,
                extraBufferCapacity = 2
            )
            ```
            - 총 수용 가능 이벤트 수: replay(1) + extraBufferCapacity(2) = 3개
            - emit()이 호출되었는데 수집자가 없거나 느릴 경우에도 최대 3개까지는 버퍼링됨

        - 추가 이벤트가 emit되면?
            - 버퍼 초과 시 오래된 이벤트부터 drop (삭제)
            - 또는 BufferOverflow.DROP_OLDEST / DROP_LATEST / SUSPEND 전략에 따라 동작 조절 가능

    - 예제 코드
        ```kotlin
        val sharedFlow = MutableSharedFlow<String>(
            replay = 1,
            extraBufferCapacity = 2,
            onBufferOverflow = BufferOverflow.DROP_OLDEST
        )

        sharedFlow.emit("A")
        sharedFlow.emit("B")
        sharedFlow.emit("C")
        sharedFlow.emit("D") // "A"는 버퍼에서 사라지고, B, C, D만 남음

        sharedFlow.collect { println(it) }
        // 출력: C, D (replay 1개: D, 수집 이후 emit된 C)
        ```
    - 실전 팁
        - UI 이벤트 (toast, navigation)에는 replay = 0, extraBufferCapacity = 1~2 정도가 적절
        - 상태(state) 저장용에는 StateFlow를 사용하고, 이벤트용은 SharedFlow에 replay + buffer 설정을 적극 활용

- Android 앱의 성능 최적화를 위해 사용한 기법
    - [UI 성능 최적화]
        - ConstraintLayout, LazyColumn, Modifier.recomposeHighlighter() 등으로 뷰 트리 간소화
        - Jetpack Compose에서 derivedStateOf, key, remember로 리컴포지션 최적화
        - Nested Scroll, Overdraw 줄이기, Layout Inspector 활용

    - [메모리 최적화]
        - Glide/Picasso 등 이미지 캐싱 적용
        - ViewModel + StateFlow로 Configuration Change 대응
        - Fragment ViewBinding의 null 해제 처리 (_binding = null)

    - [네트워크 최적화]
        - Retrofit + OkHttp + Gzip 압축
        - 통신 실패 시 재시도 로직 (retry, exponential backoff)
        - Paging3 + RecyclerView로 효율적 목록 처리

    - [스타트업 속도 최적화]
        - Baseline Profiles 적용 → 앱 cold start 30% 이상 향상
        - App Startup Library 도입으로 Lazy init 수행
        - Splash 화면에서 초기화 최소화 (실제 초기화는 MainActivity에서 지연 실행)

    - [툴 활용]
        - Android Profiler, LeakCanary, StrictMode, Perfetto
        - Systrace, TraceView로 렌더링 병목 파악

- ProGuard와 R8의 차이
    - [ProGuard 개요]
        - Java 기반 앱 최적화 도구
            - 클래스, 필드, 메서드 이름 난독화
            - 사용하지 않는 코드 제거 (shrink)
            - Java 코드 기준으로 동작 (Dex 파일 아님)

    - [R8 개요]
        - Google이 만든 최신 최적화 컴파일러
            - ProGuard + D8(Dex Compiler) 통합
            - ProGuard 설정 파일을 그대로 인식
            - 더 빠른 컴파일 + 더 강력한 최적화 수행 (inlining, dead code 제거 등)

    - [주요 차이점]
        - 통합성: R8은 컴파일 시점에 작동 → 빌드 파이프라인 단축
        - 성능: R8이 코드 크기를 더 효과적으로 줄이고 빠름
        - 기본 설정: Android Gradle Plugin 3.4 이상에선 R8이 기본 활성화
        - R8은 ProGuard와 100% 호환되진 않음 → 복잡한 규칙은 테스트 필요

    - [사용 시 주의점]
        - -keep 규칙 누락 시 앱 크래시 발생
        - Retrofit, Gson, Hilt 등 reflection 기반 라이브러리의 경우 별도 -keepclassmembers 필요

- Java의 ArrayList와 LinkedList의 차이점
    - [구조 차이]
        - ArrayList: 배열 기반의 동적 리스트
        - LinkedList: 이중 연결 리스트(Double Linked List) 기반

    - [삽입/삭제 성능]
        - ArrayList는 중간 삽입/삭제 시 모든 요소를 이동해야 하므로 느림
        - LinkedList는 포인터만 변경하면 되므로 중간 삽입/삭제가 빠름

    - [조회 성능]
        - ArrayList는 index 기반 조회가 O(1)
        - LinkedList는 처음부터 순회 → O(n)

    - [메모리 사용]
        - ArrayList는 배열 메모리만 사용 (덜 복잡)
        - LinkedList는 노드마다 추가 포인터가 있어 메모리 오버헤드가 큼

    - [정리]
        - 빈번한 조회/검색 위주면 ArrayList
        - 빈번한 삽입/삭제 위주면 LinkedList

- Java의 HashMap과 TreeMap의 차이점
    - [구조 및 정렬]
        - HashMap: 해시 테이블 기반, 정렬되지 않음
        - TreeMap: Red-Black Tree 기반, Key 기준 오름차순 정렬

    - [Null 허용 여부]
        - HashMap: null 키 1개 허용, null 값 다수 허용
        - TreeMap: null 키 허용 안 함 (NPE 발생), 값은 허용

    - [성능]
        - HashMap: 평균 O(1) (충돌 많으면 O(n))
        - TreeMap: 항상 O(log n) (정렬 유지를 위해)

    - [사용 목적]
        - HashMap: 빠른 검색이 중요할 때
        - TreeMap: 정렬된 순서 유지가 필요할 때

- Java에서 ConcurrentHashMap과 Collections.synchronizedMap()의 차이점
    - [기본 구조]
        - ConcurrentHashMap: Segmented Lock 기반 동시성 맵
        - synchronizedMap(): 전체 Map에 대해 동기화 Wrapper 적용

    - [동시성 처리 방식]
        - ConcurrentHashMap은 버킷 단위로 lock → 동시 쓰기 가능
        - synchronizedMap은 전체 맵을 lock → 병목 발생 가능

    - [성능]
        - ConcurrentHashMap이 다중 스레드 환경에서 훨씬 빠름
        - synchronizedMap은 thread-safe이긴 하지만 효율성 떨어짐

    - [Null 처리]
        - ConcurrentHashMap: null 키/값 모두 허용 안 함
        - synchronizedMap: HashMap 기반이므로 null 키/값 허용 가능

    - [정리]
        - 멀티스레드 환경에서 성능이 중요하다면 → ConcurrentHashMap
        - 단순한 thread-safe 래핑만 필요하다면 → synchronizedMap

- Java에서 WeakHashMap을 사용하는 이유
    - [기본 개념]
        - WeakHashMap은 Key가 WeakReference로 저장됨
        - Key 객체가 GC 대상이 되면 자동으로 Map에서 제거됨

    - [사용 목적]
        - 메모리 누수 방지: 더 이상 참조되지 않는 키에 대한 매핑 자동 삭제
        - 캐시, 리스너 저장소, 이미지 메모리 관리 등에 적합

    - [비교]
        - 일반 HashMap은 Key가 Strong Reference → GC가 수집 못 함
        - WeakHashMap은 Key가 GC 대상이 되면 entry 자체가 제거됨

    - [예시 용도]
        - Activity → Presenter 매핑 시, Activity가 종료되면 자동으로 제거
        - 컴파일러의 심볼 테이블
        - 이미지 캐시에서 미사용 리소스 제거

- Java에서 LinkedHashMap을 활용하여 캐시(Cache)를 구현하는 방법
    - [개요]
        - LinkedHashMap은 삽입 순서 또는 접근 순서 유지가 가능한 Map이며, 
        - removeEldestEntry() 메서드를 오버라이드하면 LRU 캐시처럼 동작 가능함.

    - [LRU 캐시 구현 예시]
        ```kotlin
        class LRUCache<K, V> extends LinkedHashMap<K, V> {
            private final int capacity;

            public LRUCache(int capacity) {
                super(capacity, 0.75f, true); // true → access-order 모드
                this.capacity = capacity;
            }

            @Override
            protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
                return size() > capacity;
            }
        }
        ```

    - [동작 방식]
        - accessOrder = true 로 설정 시, 가장 최근 접근된 항목이 뒤로 이동됨
        - put() 또는 get() 시 마다 순서가 갱신됨
        - size()가 capacity를 초과하면 가장 오래된 항목 자동 제거

    - [활용 예]
        - 이미지 캐시, 네트워크 응답 캐시, View 객체 캐싱 등에 적합

- Java에서 PriorityQueue의 동작 방식
    - [기본 구조]
        - PriorityQueue는 내부적으로 최소 힙(Min-Heap) 구조를 사용함
        - → 가장 작은 값이 우선순위를 가짐 (peek() 시 가장 낮은 값 반환)

    - [정렬 기준]
        - 기본: Comparable 구현에 따라
        - 사용자 정의: PriorityQueue(Comparator<T>) 생성자로 커스터마이징 가능

    - [시간 복잡도]
        - 삽입 (offer): O(log n)
        - 삭제 (poll): O(log n)
        - 조회 (peek): O(1)

    - [특징]
        - 중간 요소는 정렬되어 있지 않음
        - 오직 우선순위가 가장 높은 요소만 빠르게 접근 가능
        - Collections.sort()처럼 전체 정렬이 필요할 땐 부적합

    - [사용 예]
        - Dijkstra, A* 알고리즘
        - 작업 스케줄링 (Job Queue)
        - Top-K 문제

- Java에서 Deque와 Queue의 차이점
    - [Queue (First-In-First-Out)]
        - 단방향 선입선출 자료구조
        - add() / offer() → 요소 추가
        - poll() / remove() → 앞에서 제거
        - 예시 구현체: LinkedList, ArrayDeque, PriorityQueue

    - [Deque (Double-Ended Queue)]
        - 양쪽에서 삽입/삭제 가능한 구조 (스택 + 큐 겸용 구조 가능)
        - addFirst(), addLast()
        - pollFirst(), pollLast()
        - peekFirst(), peekLast()
        - 예시 구현체: ArrayDeque, LinkedList

    - [Deque 활용 예]
        - Stack 대체 (push, pop)
        - 슬라이딩 윈도우 최대값 계산
        - 양방향 탐색

- Java에서 ArrayDeque와 LinkedList의 차이점
    - [구조 차이]
        - ArrayDeque: 배열 기반의 원형 버퍼 구조
        - LinkedList: 이중 연결 리스트 기반 구조

    - [성능]
        - ArrayDeque는 index 기반 접근이 빠르고 캐시 적중률이 높음
        - LinkedList는 노드 포인터 이동이 필요하므로 검색이나 반복 시 느림

    - [삽입/삭제]
        - 양쪽 삽입/삭제는 둘 다 O(1)이지만,
        - ArrayDeque는 크기 초과 시 배열 복사가 발생할 수 있음
        - LinkedList는 노드 연결만 바꾸면 되므로 항상 일정 성능

    - [메모리 사용]
        - ArrayDeque는 배열 오버헤드 + 리사이징 비용
        - LinkedList는 노드마다 포인터 2개(앞/뒤)로 메모리 사용량 증가

    - [정리]
        - 빈번한 양방향 삽입/삭제 → LinkedList
        - 빠른 순차 접근과 낮은 메모리 오버헤드 → ArrayDeque (Stack/Queue 대체로 권장)

- Java의 HashSet과 TreeSet의 차이점
    - [구조 및 정렬]
        - HashSet: 해시 테이블 기반, 순서 없음
        - TreeSet: Red-Black Tree 기반, 정렬된 순서 유지

    - [성능]
        - HashSet: 삽입/삭제/검색 평균 O(1)
        - TreeSet: 삽입/삭제/검색 O(log n)

    - [Null 허용 여부]
        - HashSet: null 허용
        - TreeSet: null 허용 안 함 (NPE 발생 가능)

    - [사용 예]
        - HashSet: 빠른 중복 제거가 필요할 때
        - TreeSet: 정렬된 데이터가 필요하거나 범위 검색 (subSet, headSet 등)

- Java에서 Iterator와 ListIterator의 차이점
    - [기본 구조]
        - Iterator: 단방향 탐색만 가능
        - ListIterator: 양방향 탐색 가능 (단, List 계열에서만 사용 가능)

    - [탐색 기능]
        - Iterator: hasNext(), next(), remove()
        - ListIterator: hasNext(), hasPrevious(), next(), previous(), add(), set()

    - [적용 범위]
        - Iterator: 모든 Collection
        - ListIterator: List 계열 (ArrayList, LinkedList)만 가능

    - [기능적 차이]
        - ListIterator는 현재 위치 기반으로 앞/뒤 탐색, 인덱스 기반 삽입, 변경 가능
        - Iterator는 간단한 순방향 순회 전용

    - [사용 예]
        - Iterator: 필터링하며 순회, 간단한 제거 작업
        - ListIterator: 탐색 중 중간 삽입/수정이 필요한 경우

- Java에서 CopyOnWriteArrayList의 사용 사례
    - [기본 개념]
        - CopyOnWriteArrayList는 쓰기 연산 시마다 전체 배열을 복사하여 새로운 배열로 대체하는 Immutable 방식의 thread-safe List

    - [특징]
        - 읽기 작업이 많고 쓰기 작업이 드문 환경에서 매우 효율적
        - Iterator 도중에 List가 수정되어도 ConcurrentModificationException 발생하지 않음
        - 동기화 비용 없이 Safe iteration 가능

    - [사용 사례]
        - 이벤트 리스너 목록: 리스너 등록/해제는 드물고, 이벤트 브로드캐스트는 자주 발생
        - 캐시 리스트: 빈번한 조회, 간헐적 갱신이 필요한 설정 목록
        - 멀티스레드 환경의 정적 데이터 리스트: 실시간 동기화 없이 안정된 읽기 필요

    - [주의점]
        - 쓰기 연산이 자주 발생하는 경우 성능 급락
        - 객체 수가 많거나 크기가 클수록 메모리 부담 커짐

- Java에서 EnumMap을 사용하는 이유
    - [정의 및 구조]
        - EnumMap<K extends Enum<K>, V>는 Enum 키 전용 Map 구현체
        - 내부적으로 배열 기반으로 매우 빠르게 작동함.

    - [장점]
        - 성능 우수: 해시 연산이 아닌 배열 인덱스를 통해 값에 직접 접근 → 일반 HashMap보다 훨씬 빠름
        - 메모리 절약: Enum 값 개수만큼의 배열만 유지하므로 공간 효율성도 뛰어남
        - null 키 허용 안 함: Enum 값이 아닌 키는 compile-time에 걸러짐 → 타입 안정성 확보

    - [사용 예]
        - 상태머신 구현 (ex. OrderStatus -> Handler)
        - 요일, 방향, 단계 등 명확한 Enum 매핑 구조 필요 시

- Java에서 BlockingQueue의 역할과 사용 예제
    - [정의 및 목적]
        - BlockingQueue는 스레드 간 안전한 데이터 교환을 위한 큐.
            - 큐가 비어있으면 take()가 블록됨
            - 큐가 가득 차면 put()이 블록됨

    - [사용 예]
        - 생산자-소비자 패턴 (Producer-Consumer)
        - 쓰레드 풀에서 작업 큐로 활용
        - 백그라운드 작업 처리용 이벤트 큐

    - [대표 구현체]
        - ArrayBlockingQueue: 고정 크기 버퍼
        - LinkedBlockingQueue: 동적 크기, 무제한 가능
        - PriorityBlockingQueue: 우선순위 기반 처리
        - DelayQueue: 특정 시간 이후 처리용 큐

    - [예제]
        ```kotlin
        BlockingQueue<String> queue = new LinkedBlockingQueue<>();

        // Producer
        new Thread(() -> {
            queue.put("작업 A");
        }).start();

        // Consumer
        new Thread(() -> {
            String task = queue.take();
            // 처리
        }).start();
        ```

- Java에서 Stream API와 for-each 루프의 차이점
    - [Stream API 특징]
        - 선언형(Declarative): 원하는 작업을 명시적으로 기술 (ex. filter, map, collect)
        - 내부 반복(Internal Iteration): 병렬 처리 및 최적화에 유리
        - 중간 연산/최종 연산 분리: filter().map().collect()
        - 병렬 스트림 지원: .parallelStream() 으로 멀티코어 사용

    - [for-each 특징]
        - 명령형(Imperative): 반복 로직을 직접 구현
        - 외부 반복(External Iteration): 제어가 개발자에게 있음
        - 단순 반복에 적합: 성능 예측이 쉽고, 직관적

    - [차이 요약]
        - Stream은 코드 가독성, 불변성, 병렬성에 유리
        - for-each는 간단한 반복이나 수정이 필요한 로직에 유리

- Java에서 Collectors.toMap()을 사용할 때 발생할 수 있는 문제
    - [문제 1: 키 중복 시 예외 발생]
        ```kotlin
        list.stream().collect(Collectors.toMap(
            item -> item.getId(),
            item -> item.getValue()
        ));
        ```
        - → 같은 키가 두 번 나오면 IllegalStateException 발생
    - [해결 방법: 병합 함수 제공]
        ```kotlin
        .collect(Collectors.toMap(
            item -> item.getId(),
            item -> item.getValue(),
            (v1, v2) -> v1  // 충돌 시 v1 유지
        ));
        ```
    - [문제 2: Null 키 또는 Null 값 허용 안 함]
        - toMap()은 기본적으로 null 키나 null 값 허용하지 않음 → NullPointerException 발생 가능
        - 처리 방법: .filter(Objects::nonNull) 등 사전 정제 필요

    - [문제 3: LinkedHashMap 등 커스텀 맵 지정 없이 HashMap 고정]
        - 기본적으로 HashMap으로 수집되므로 순서 보장 불가
        - 해결: 4번째 인자로 LinkedHashMap::new 등 전달
        ```kotlin
        .collect(Collectors.toMap(
            k -> ..., v -> ..., (v1, v2) -> v1, LinkedHashMap::new
        ));
        ```

- Java에서 Spliterator의 역할과 활용 방법
    - [정의]
        - Spliterator는 Stream의 병렬 처리 또는 대용량 데이터 분할 탐색을 위한 Iterator의 확장형
        - → Split + Iterator = Spliterator

    - [주요 역할]
        - 컬렉션을 분할(split) 하여 병렬 처리에 적합하도록 나누는 기능
        - tryAdvance()로 개별 요소 처리, forEachRemaining()으로 일괄 처리
        - trySplit() 호출 시 처리 단위를 절반으로 나누어 새로운 Spliterator 반환

    - [활용 예시]
        ```java
        List<String> list = List.of("A", "B", "C", "D");

        Spliterator<String> spliterator = list.spliterator();

        spliterator.tryAdvance(System.out::println); // A
        spliterator.forEachRemaining(System.out::println); // B, C, D
        ```

    - [Stream 내부에서의 활용]
        - Stream은 내부적으로 Spliterator를 사용하여 병렬 처리를 분기함 (parallelStream())

- Java에서 Unmodifiable Collection을 생성하는 방법
    - [정의]
        - Unmodifiable Collection은 요소 추가/삭제/수정이 불가능한 읽기 전용 컬렉션

    - [생성 방법]
        - Collections.unmodifiableXXX()
            ```java
            List<String> list = new ArrayList<>();
            List<String> readOnly = Collections.unmodifiableList(list);
            ```
        - List.of() / Set.of() / Map.of() (Java 9+)
            ```java
            List<String> list = List.of("A", "B", "C"); // 불변 + 수정 불가
            ```

    - [주의사항]
        - Collections.unmodifiableXXX()는 원본이 변경되면 같이 변경됨 (view 역할)
        - 완전한 불변을 원한다면 Java 9 이후의 of() 메서드 사용 추천

- Java에서 Arrays.asList()를 사용할 때 주의할 점
    - [정의]
        - Arrays.asList()는 고정 크기(List 형태지만 내부는 배열 기반)의 리스트를 반환함

    - [주의사항]
        - add(), remove() 등 요소의 크기를 변경하는 작업은 UnsupportedOperationException 발생
        - set()은 가능하지만 구조 변경은 불가

    - [예시 문제]
        ```java
        List<String> list = Arrays.asList("A", "B");
        list.add("C"); // 예외 발생
        ```

    - [해결 방법]
        - 구조 변경이 필요하다면 new ArrayList<>(Arrays.asList(...))로 감싸서 사용해야 함

- Java에서 Immutable Collections을 생성하는 방법
    - [정의]
        - Immutable Collection은 요소 추가/삭제/수정 모두 불가능하며, 안전하게 공유할 수 있는 컬렉션

    - [생성 방법]
        - Java 9+ List.of() / Set.of() / Map.of()
            ```java
            List<String> list = List.of("A", "B", "C");
            Set<Integer> set = Set.of(1, 2, 3);
            Map<String, String> map = Map.of("k", "v");
            ```
        - Google Guava 라이브러리
            ```java
            ImmutableList<String> list = ImmutableList.of("A", "B", "C");
            ```
        - Java 8 이하
            ```java
            List<String> list = Collections.unmodifiableList(new ArrayList<>(...));
            ```

    - [장점]
        - Thread-safe
        - 불변 보장 → side effect 방지
        - 의도 명확 → 유지보수 용이

    - [차이점 vs Unmodifiable Collection]
        - Unmodifiable: 내부 데이터는 변경 가능 (view 역할)
        - Immutable: 내부도 변경 불가 (완전 불변)

- Java에서 Map.computeIfAbsent()의 활용 사례
    - [기능 설명]
        - computeIfAbsent(key, mappingFunction)은 지정한 key에 값이 없을 경우에만 mappingFunction을 호출하여 값을 계산 후 Map에 저장
            - → lazy initialization 방식으로, 중복 확인 + 초기화 코드를 줄여줌

    - [활용 사례]
        - Map 내부에 List/Set 등의 복합 자료구조 초기화
            ```java
            Map<String, List<String>> map = new HashMap<>();
            map.computeIfAbsent("A", k -> new ArrayList<>()).add("hello");
            ```

        - 캐시 패턴 구현
            ```java
            cache.computeIfAbsent(id, this::loadFromDb);
            ```

        - 데이터 그룹핑 처리
            ```java
            list.forEach(item -> 
                groupedMap.computeIfAbsent(
                    item.category(), k -> new ArrayList<>()).add(item)
            );
            ```
    - [장점]
        - 코드 간결화 (if-contains-key + put의 반복 제거)
        - thread-safe Map과 함께 쓰면 성능 및 안정성 향상 (ConcurrentHashMap 등)

- Java에서 ConcurrentLinkedQueue와 LinkedBlockingQueue의 차이점
    - [ConcurrentLinkedQueue]
        - 비동기(non-blocking) 큐
        - 내부적으로 CAS 기반의 Lock-Free 큐
        - null 허용 안 함
        - offer(), poll() 즉시 반환됨 (대기 없음)

    - [LinkedBlockingQueue]
        - BlockingQueue의 대표 구현체
        - 내부적으로 take()/put()은 대기 상태 가능 (block)
        - 생산자-소비자 패턴에 적합
        - 큐의 크기를 고정 또는 무제한 설정 가능

    - [사용 예]
        - UI 이벤트 비동기 큐 → ConcurrentLinkedQueue
        - 스레드 간 데이터 전달 (Blocking 필요) → LinkedBlockingQueue

- Java의 ForkJoinPool을 활용한 병렬 처리 구현 방법
    - [정의]
        - ForkJoinPool은 Java 7에서 도입된 작업 분할-정복(Fork/Join) 기반 병렬 처리 프레임워크
        - → 큰 작업을 재귀적으로 쪼개서 여러 코어에서 병렬 처리 후 합침

    - [기본 구성]
        - RecursiveTask<T>: 결과 반환
        - RecursiveAction: 반환 없음

    - [예제: 배열 합계 계산]
        ```java
        class SumTask extends RecursiveTask<Long> {
            private final int[] array;
            private final int start, end;
            private static final int THRESHOLD = 1000;

            SumTask(int[] array, int start, int end) {
                this.array = array; this.start = start; this.end = end;
            }

            @Override
            protected Long compute() {
                if (end - start <= THRESHOLD) {
                    long sum = 0;
                    for (int i = start; i < end; i++) sum += array[i];
                    return sum;
                } else {
                    int mid = (start + end) / 2;
                    SumTask left = new SumTask(array, start, mid);
                    SumTask right = new SumTask(array, mid, end);
                    left.fork();
                    return right.compute() + left.join();
                }
            }
        }

        // 사용
        ForkJoinPool pool = new ForkJoinPool();
        long result = pool.invoke(new SumTask(array, 0, array.length));
        ```

    - [장점]
        - 작업을 자동 분할하여 CPU 코어를 최대한 활용
        - fork()는 서브 작업 시작, join()은 해당 작업 완료 대기
        - 내부적으로 work-stealing 알고리즘을 사용해 idle 스레드가 다른 작업을 가져와 수행

    - [사용 예]
        - 대용량 계산 (병렬 정렬, 이미지 처리, 행렬 연산 등)
        - 데이터 분석용 MapReduce-like 연산

- Java에서 NavigableMap과 NavigableSet의 차이점
    - [공통점]
        - 둘 다 Java 1.6부터 추가된 정렬 기반 컬렉션 인터페이스, 하위 구조는 각각 TreeMap, TreeSet
        - → 범위 조회, 순방향/역방향 탐색, 가장 가까운 값 조회 기능 제공

    - [NavigableMap]
        - Map<K, V> 인터페이스 확장
        - Key 기반 정렬 Map
        - 주요 메서드:
            - lowerKey(K key): 보다 작은 key 중 최대
            - ceilingKey(K key): 같거나 큰 key 중 최소
            - subMap(K from, K to, boolean inclusive...)

    - [NavigableSet]
        - Set<E> 인터페이스 확장
        - 정렬된 고유 값 집합
        - 주요 메서드:
            - lower(E e), floor(E e), ceiling(E e), higher(E e)
            - pollFirst(), pollLast()

- Java에서 TreeMap을 활용하여 정렬된 데이터를 관리하는 방법
    - [기본 개념]
        - TreeMap은 NavigableMap 인터페이스 구현체로, 내부적으로 Red-Black Tree(이진 균형 트리) 기반
        - → Key 기준 자동 정렬 Map

    - [기본 정렬 방식]
        - Comparable 구현 시 자동 정렬
        - 또는 생성자에서 Comparator 전달 가능
            ```java
            TreeMap<String, Integer> map = new TreeMap<>(Comparator.reverseOrder());
            ```

    - [활용 예]
        - 시간순 정렬 로그 저장
        - 범위 검색: subMap, headMap, tailMap 등으로 부분 Map 추출
        - 최대/최소 키 조회: firstKey(), lastKey(), higherKey(), lowerKey()

    - [주의사항]
        - Key가 null이면 NullPointerException 발생
        - 성능은 삽입/검색/삭제 모두 O(log n)

- Java에서 PriorityBlockingQueue의 동작 원리
    - [정의]
        - PriorityBlockingQueue는 우선순위 큐 + 동기화 지원(BlockingQueue) 를 결합한 구조

    - [동작 원리]
        - 내부적으로 Heap(Binary Heap) 기반으로 동작 (기본은 Min-Heap)
        - Comparator 또는 Comparable을 통해 우선순위 정의
        - put()/take() 시 내부적으로 ReentrantLock으로 동기화 처리
        - 비어 있으면 take()는 블록 상태, 요소가 들어올 때까지 대기

    - [특징]
        - 우선순위 정렬 + 스레드 간 안전한 큐 처리
        - peek()는 가장 높은 우선순위 요소 반환
        - Iterator로 순회 시 정렬된 상태는 아님 (heap 구조 유지 때문)

    - [사용 예]
        - 작업 스케줄러 큐
        - 우선순위 기반 이벤트 처리
        - Job Queue 시스템

- Java에서 Thread-Safe Collection의 대표적인 구현체
    - [Legacy Thread-Safe] (동기화 래핑된 컬렉션: 느림)
        - Vector, Hashtable
        - Collections.synchronizedList(...), synchronizedMap(...)

    - [Concurrent 패키지 기반: 현대적 방식]
        - ConcurrentHashMap
        - CopyOnWriteArrayList
        - ConcurrentLinkedQueue
        - ConcurrentSkipListMap
        - LinkedBlockingQueue, ArrayBlockingQueue, PriorityBlockingQueue

    - [특징]
        - ConcurrentHashMap: Segment 기반 Lock으로 성능 향상
        - CopyOnWriteArrayList: 읽기 위주에 적합, 쓰기 시 전체 복사
        - ConcurrentLinkedQueue: lock-free 구조, 빠른 비동기 큐
        - BlockingQueue 계열: 생산자-소비자 구조에서 강력함

    - [선택 기준]
        - 읽기 중심 + 안전성 보장 → CopyOnWriteArrayList
        - 다중 스레드 빠른 조회/수정 → ConcurrentHashMap
        - 대기 및 큐 처리 필요 → LinkedBlockingQueue, PriorityBlockingQueue

- Java에서 Stream API의 parallelStream()을 사용할 때 주의해야 할 점
    - [기본 개념]
        - parallelStream()은 내부적으로 ForkJoinPool(commonPool) 을 이용하여 데이터를 병렬 처리
        - → Stream 요소들을 여러 스레드에서 병렬로 분할 처리

    - [주의할 점]
        - 공유 상태 사용 금지: 병렬 환경이므로 List.add() 등 외부 상태를 사용하는 코드는 race condition 발생
            - → 반드시 reduce, collect 등 불변 기반 함수형 연산 사용
        - Stream 연산 순서 불보장: forEach() 사용 시 순서가 뒤섞일 수 있음
            - → 순서가 중요하면 forEachOrdered() 사용
        - 작업 비용이 충분히 커야 효율 있음: 간단한 연산은 오히려 병렬 오버헤드가 더 큼
        - 디폴트 스레드 풀 공유: 다른 라이브러리도 같은 commonPool을 공유하므로 리스크 존재
            - → 병렬 작업이 많을 경우 custom ForkJoinPool 사용 고려

    - [요약]
        - CPU 연산 중심 작업에 적합
        - I/O 중심, 순서 민감, 사이드 이펙트 있는 경우 지양

- Java에서 FlatMap()을 활용하는 방법
    - [기본 개념]
        - flatMap(Function<T, Stream<R>>)은 여러 Stream을 하나의 Stream으로 평탄화(flatten) 할 때 사용
        - → 다차원 구조 → 일차원 스트림으로 변환

    - [활용 예: List<List<String>> → List<String>]
        ```java
        List<List<String>> list = List.of(
            List.of("A", "B"),
            List.of("C", "D")
        );

        List<String> flat = list.stream()
            .flatMap(Collection::stream)
            .collect(Collectors.toList());
        ```

    - [문자열 분해 예시]
        ```java
        List<String> words = List.of("hello world", "java stream");

        List<String> tokens = words.stream()
            .flatMap(s -> Arrays.stream(s.split(" ")))
            .collect(Collectors.toList());
        ```

    - [요약]
        - 중첩 구조 → 단일 Stream 변환
        - map()은 계층 유지, flatMap()은 계층 제거

- Java에서 Collectors.groupingBy()를 활용한 데이터 분류 방법
    - [기본 개념]
        - groupingBy(Function)은 Stream 요소를 특정 기준(key)으로 그룹화하여 Map 형태로 반환
    - [기본 사용 예]
        ```java
        Map<String, List<Person>> byDept = people.stream()
            .collect(Collectors.groupingBy(Person::getDepartment));
        ```
    - [중첩 사용: 분류 + 집계]
        ```java
        Map<String, Long> countByDept = people.stream()
            .collect(Collectors.groupingBy(
                Person::getDepartment,
                Collectors.counting()
            ));
        ```
    - [중첩 사용: 분류 + 최대값]
        ```java
        Map<String, Optional<Person>> topSalaryByDept = people.stream()
            .collect(Collectors.groupingBy(
                Person::getDepartment,
                Collectors.maxBy(Comparator.comparing(Person::getSalary))
            ));
        ```
    - [요약]
        - 데이터 분류, 통계, 분할 등을 선언적으로 처리 가능
        - groupingBy + downstream collector 조합으로 유연한 통계 구현 가능

- Java의 Stream.reduce()를 활용한 데이터 집계 방법
    - [기본 개념]
        - reduce는 Stream 요소들을 하나의 결과값으로 축소(Aggregate) 시키는 연산
        - → 누적값을 만들기 위해 BinaryOperator를 반복 적용

    - [기본 예: 합계 구하기]
        ```java
        int sum = list.stream()
            .reduce(0, Integer::sum);
        ```
    - [문자열 연결 예시]
        ```java
        String combined = List.of("a", "b", "c")
            .stream()
            .reduce("", (a, b) -> a + b);
        ```
    - [고급 예: 객체 누적 처리]
        ```java
        int totalSalary = employees.stream()
            .map(Employee::getSalary)
            .reduce(0, Integer::sum);
        ```
    - [요약]
        - reduce(identity, accumulator) or reduce(accumulator) 형태
        - 기본형 stream (IntStream)에서는 sum(), average() 등을 활용하는 것이 더 간단함
        - 복잡한 누적 로직에는 reduce()가 강력함

- Java에서 ExecutorService를 활용한 스레드 풀(Thread Pool) 구현 방법
    - [정의]
        - ExecutorService는 Java의 스레드 풀(Thread Pool) 을 구현한 인터페이스
        - 스레드 생성/관리/작업 제출을 추상화한 API

    - [기본 생성 방법]
        - ExecutorService executor = Executors.newFixedThreadPool(5);
    - [주요 구현 종류]
        - newFixedThreadPool(int n): 고정 개수 스레드
        - newCachedThreadPool(): 필요할 때 무제한 스레드 생성, 사용 후 재사용
        - newSingleThreadExecutor(): 단일 스레드, FIFO
        - newWorkStealingPool(): ForkJoinPool 기반 (Java 8+)

    - [작업 제출]
        - executor.submit(Runnable) 또는 executor.submit(Callable)
        - 반환값 필요 시 Future 이용

    - [종료]
        ```java
        executor.shutdown();               // graceful shutdown
        executor.awaitTermination(10, TimeUnit.SECONDS); // 대기
        executor.shutdownNow();           // 강제 종료
        ```

- Java에서 Future와 CompletableFuture의 차이점
    - [Future]
        - Java 5 도입
        - 비동기 작업의 결과를 반환받기 위한 객체
        - future.get()으로 결과 가져오며, 완료될 때까지 블로킹됨
        - 콜백 처리 불가 → 동기적 접근 방식
        - 예외 처리 시 try-catch 필요
        - 병렬 연산 조합 불가

    - [CompletableFuture]
        - Java 8 도입
        - Future 확장형으로, 비동기 + 콜백 기반 처리 가능
        - thenApply(), thenAccept(), thenCombine() 등 체이닝 지원
        - supplyAsync() 또는 runAsync() 로 스레드 풀 연계 가능
        - 예외 처리: .exceptionally(), .handle()
        - 병렬 연산 조합 가능 (.thenCombine(), .allOf())

- Java에서 ScheduledExecutorService의 역할
    - [정의]
        - ScheduledExecutorService는 지연 또는 반복 실행 작업을 예약하기 위한 Executor 인터페이스 확장

    - [생성 방법]
        - ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(2);
    - [사용 예]
        ```java
        scheduler.schedule(() -> {
            System.out.println("3초 후 실행");
        }, 3, TimeUnit.SECONDS);

        scheduler.scheduleAtFixedRate(task, 0, 5, TimeUnit.SECONDS); // 고정 주기 반복
        ```

    - [차이점 vs Timer]
        - 예외 발생 시에도 전체 스케줄러 멈추지 않음
        - 멀티스레드 기반으로 Timer보다 안정성, 확장성 우수

    - [주요 메서드]
        - schedule(...): 일정 지연 후 1회 실행
        - scheduleAtFixedRate(...): 고정 간격 반복
        - scheduleWithFixedDelay(...): 이전 작업 종료 후 일정 지연 반복

- Java에서 ReentrantLock과 synchronized의 차이점
    - [공통점]
        - 둘 다 스레드 동기화를 위한 방법으로, 임계 영역에서 동시 접근 방지 기능 제공

    - [synchronized]
        - Java 내장 키워드
        - 블록 단위 혹은 메서드 전체에 적용
        - 자동 잠금/해제 → try-finally 필요 없음
        - 공정성(Fairness) 제어 불가
        - 조건 변수 지원: 불가능

    - [ReentrantLock]
        - java.util.concurrent.locks 패키지 제공
        - 명시적 lock() / unlock() 필요 (try-finally 필수)
        - 공정성 설정 가능 (new ReentrantLock(true))
        - 추가 기능: tryLock(), lockInterruptibly(), Condition await/signal
        - 조건 변수 지원: Condition 객체 지원

- 공정성(Fairness) 설정
    - [개요]
        - Java에서 ReentrantLock 또는 Semaphore 같은 동기화 도구를 사용할 때, 
        - 락을 기다리는 스레드들에게 락을 얼마나 '공평하게' 분배할 것인가를 제어하는 설정

    - [공정성(Fairness) 설정 개념]
        - 락을 얻으려는 여러 스레드가 대기 중일 때, 먼저 기다린 스레드가 먼저 락을 얻도록 보장할지 여부를 설정하는 것을 말함.

    - [공정성 종류]
        - 공정(Fair) 락 (fair = true)
            - 대기 큐에서 가장 오래 기다린 스레드에게 우선 락을 부여
            - 락 요청 순서를 FIFO(선입선출) 방식으로 보장
            - → 예측 가능, 하지만 약간의 성능 저하 가능

        - 비공정(Non-Fair) 락 (fair = false, 기본값)
            - 락을 요청한 스레드가 즉시 획득할 수 있다면, 대기열을 무시하고 바로 락을 획득함
            - → 빠르지만, 일부 스레드가 락을 계속 선점하게 되는 기아(Starvation) 현상이 발생할 수 있음

    - [예시]
        ```java
        ReentrantLock fairLock = new ReentrantLock(true);   // 공정 락
        ReentrantLock unfairLock = new ReentrantLock(false); // 비공정 락
        ```

    - [공정 락 사용 시점]
        - 실시간성 보장이 중요한 경우
        - 기아 현상(Starvation) 을 방지해야 하는 시스템 (예: ATM, 티켓 발매 등 순서 보장 필요)

    - [요약]
        - 공정성 설정은 락의 순서 보장 여부에 대한 설정
        - fair = true: 대기 순서 보장 (안전하지만 성능 낮음)
        - fair = false: 빠르지만 스레드가 굶을 수 있음 (기아 발생 가능성)

- Java에서 ForkJoinTask와 RecursiveTask를 활용한 병렬 처리 구현 방법
    - [기본 개념]
        - ForkJoinTask는 Java 7부터 도입된 Fork/Join 프레임워크의 기본 단위로,
        - 큰 작업을 작게 나누어(fork) 병렬로 처리하고, 최종 결과를 합치는(join) 방식의 병렬 처리에 사용됨.

    - [RecursiveTask vs RecursiveAction]
        - RecursiveTask<V>: 반환값 있는 작업
        - RecursiveAction: 반환값 없는 작업

    - [구현 예제: 배열의 합 계산]
        ```java
        class SumTask extends RecursiveTask<Long> {
            private final int[] arr;
            private final int start, end;
            private static final int THRESHOLD = 1000;

            SumTask(int[] arr, int start, int end) {
                this.arr = arr;
                this.start = start;
                this.end = end;
            }

            @Override
            protected Long compute() {
                if (end - start <= THRESHOLD) {
                    long sum = 0;
                    for (int i = start; i < end; i++) sum += arr[i];
                    return sum;
                } else {
                    int mid = (start + end) / 2;
                    SumTask left = new SumTask(arr, start, mid);
                    SumTask right = new SumTask(arr, mid, end);
                    left.fork(); // 비동기 실행
                    return right.compute() + left.join(); // 결과 병합
                }
            }
        }

        ForkJoinPool pool = new ForkJoinPool();
        long total = pool.invoke(new SumTask(array, 0, array.length));
        ```

- Java에서 Phaser와 CyclicBarrier의 차이점
    - [공통점]
        - 둘 다 지정된 수의 스레드가 특정 지점(barrier)에 도달할 때까지 대기시키는 동기화 도구

    - [CyclicBarrier]
        - 고정된 수의 스레드가 도달할 때까지 대기
        - 도달 후 모든 스레드가 동시에 재개
        - 재사용 가능, 이름 그대로 "사이클형 장벽"

    - [Phaser]
        - 유연한 파티 참가/탈퇴 관리 가능 (동적 등록/도착 지원)
        - 여러 "단계(phase)"를 가질 수 있어 멀티 스텝 동기화에 적합
        - 복잡한 병렬 워크플로우를 지원

- Java에서 Callable과 Runnable의 차이점
    - [Runnable]
        - Java 1.0부터 존재
        - run() 메서드만 있고, 반환값 없음, 예외 던지기 불가
        - Thread 또는 ExecutorService.submit(Runnable)에서 사용 가능

    - [Callable<V>]
        - Java 5부터 도입 (java.util.concurrent)
        - call() 메서드로 동작, 결과 반환 가능, 예외 던질 수 있음
        - ExecutorService.submit(Callable) → Future<V> 반환

    - [예시 비교]
        ```java
        Callable<Integer> task = () -> {
            return 42;
        };

        Future<Integer> result = executor.submit(task);
        ```

- Java에서 AsynchronousFileChannel의 역할
    - [정의]
        - AsynchronousFileChannel은 Java NIO.2에서 제공하는 비동기 파일 I/O 채널
        - → 파일을 읽거나 쓸 때 스레드 블로킹 없이 비동기 방식으로 처리 가능

    - [주요 특징]
        - read() 또는 write() 호출 시 작업이 백그라운드에서 실행
        - 완료되면 CompletionHandler 콜백이 실행됨
        - I/O가 완료될 때까지 현재 스레드는 대기하지 않음
        - 고성능 서버/로깅 시스템에 적합

    - [예시: 비동기 파일 읽기]
        ```java
        Path path = Paths.get("sample.txt");
        AsynchronousFileChannel channel = AsynchronousFileChannel.open(path, StandardOpenOption.READ);

        ByteBuffer buffer = ByteBuffer.allocate(1024);
        channel.read(buffer, 0, buffer, new CompletionHandler<Integer, ByteBuffer>() {
            @Override
            public void completed(Integer result, ByteBuffer attachment) {
                attachment.flip();
                System.out.println("Read: " + new String(attachment.array()));
            }

            @Override
            public void failed(Throwable exc, ByteBuffer attachment) {
                System.err.println("Failed: " + exc.getMessage());
            }
        });
        ```

    - [활용 예]
        - 고성능 로깅 시스템
        - 대용량 파일 비동기 업로드/다운로드
        - GUI 앱에서 파일 처리 중 UI 멈춤 방지

- 블로킹, 논블로킹, 동기, 비동기 재정리
    - 개요
        - 모든 I/O 또는 멀티스레딩 시스템의 기본 동작 모델
    - [블로킹 (Blocking)]
        - [정의]
            - 호출한 스레드가 작업이 끝날 때까지 멈추는 방식
            - → 예: InputStream.read()를 호출하면 데이터가 도착할 때까지 스레드는 대기
        - [특징]
            - 제어권이 호출자에 없다 (스레드가 작업을 기다리며 멈춰 있음)
            - 코드 흐름은 직관적이지만, 리소스를 장시간 점유
        - [예시]
            - int byteRead = inputStream.read(); // 데이터 없으면 블로킹됨

    - [논블로킹 (Non-Blocking)]
        - [정의]
            - 호출한 스레드가 즉시 반환되고, 데이터가 없으면 예외나 기본값을 반환
            - → 예: SocketChannel.read()는 데이터가 준비되지 않으면 0을 반환하고 돌아감
        - [특징]
            - 스레드가 멈추지 않음
            - 계속 폴링하거나 다른 작업과 병행 가능
        - [예시]
            - int bytesRead = socketChannel.read(buffer); // 준비 안 됐으면 0 반환

    - [동기 (Synchronous)]
        - [정의]
            - 호출한 함수가 결과를 직접 기다리며 리턴을 받을 때까지 흐름이 멈추는 방식
        - [특징]
            - 호출 → 완료 → 다음 실행
            - 블로킹일 수도 있고, 논블로킹일 수도 있음
            - (ex. 반복 호출로 직접 확인하면 논블로킹+동기)
        - [예시]
            - String result = syncCall(); // 결과를 받아야 다음 코드 진행

    - [비동기 (Asynchronous)]
        - [정의]
            - 호출자가 요청을 보낸 뒤 즉시 제어권을 넘겨받고, 결과는 콜백, Future, 이벤트 등으로 나중에 받는 방식
        - [특징]
            - 호출 즉시 다음 로직 실행 가능
            - 주로 콜백, 이벤트 리스너, CompletableFuture, Promise 패턴 활용
            - 블로킹일 수도 있고, 논블로킹일 수도 있음 (일반적으로 논블로킹과 함께 쓰임)
        - [예시]
            ```java
            CompletableFuture.supplyAsync(() -> longRunningTask())
                .thenAccept(result -> System.out.println("완료됨: " + result));
            ```

- 블로킹, 논블로킹, 동기, 비동기 조합 상황 설명
    - 개요
        - "비동기면서 블로킹일 수 있다" 또는 "동기지만 논블로킹일 수 있다"는 표현은 언뜻 보면 모순처럼 느껴지지만, 
        - 실제로는 동기/비동기와 블로킹/논블로킹이 서로 다른 차원의 개념이기 때문에 가능한 조합
    - [동기 + 블로킹]
        - [설명]
            - 함수 호출자가 직접 결과를 받을 때까지 기다리며, 그동안 스레드가 멈춤
        - [예시]
            - String data = readFromSocket(); // 내부에서 InputStream.read() 사용
            - // 여기서 스레드는 데이터가 올 때까지 멈춰 있음
        - [사용 상황]
            - 가장 일반적인 I/O 처리 방식. 간단하지만, 다수의 연결 처리에는 부적합.

    - [동기 + 논블로킹]
        - [설명]
            - 함수 호출자가 직접 결과를 요청하지만, 스레드는 멈추지 않음
        - [예시]
            ```java
            int read = socketChannel.read(buffer); // NIO 방식
            if (read == 0) {
                // 아직 데이터 없음. 다음에 다시 시도
            }
            ```
        - [사용 상황]
            - 직접 폴링하거나, 상태를 계속 확인해야 하는 시스템 (예: 게임 루프, 이벤트 루프 등)

    - [비동기 + 블로킹]
        - [설명]
            - 함수는 비동기 처리로 등록되지만, 이후에 결과를 블로킹 방식으로 기다림
        - [예시]
            - Future<String> result = executor.submit(task);
            - String data = result.get(); // 작업은 비동기였지만, get()은 블로킹
        - [사용 상황]
            - 실제 실행은 비동기이지만, 나중에 호출자가 결과를 반드시 기다려야 할 때

    - [비동기 + 논블로킹]
        - [설명]
            - 함수는 비동기로 실행되고, 결과는 콜백/이벤트로 전달되며, 스레드는 절대 멈추지 않음
        - [예시]
            ```java
            CompletableFuture.supplyAsync(() -> loadData())
                .thenAccept(result -> System.out.println("결과 도착: " + result));
            ```
        - [사용 상황]
            - 고성능 웹 서버, Netty, GUI 앱에서 이벤트 처리, RxJava, Coroutine 등

    - [실전 팁]
        - 비동기 = 흐름이 끊기지 않는다 (내가 결과를 기다리지 않아도 된다)
        - 논블로킹 = 스레드가 멈추지 않는다 (즉시 반환)
            - 두 개념은 독립적이므로 조합해서 동작 방식이 다양해질 수 있다.

- Java에서 Non-blocking I/O(NIO)와 Blocking I/O(BIO)의 차이점
    - [Blocking I/O (BIO)]
        - Thread-per-connection 모델
        - I/O 작업(예: read(), write())이 완료될 때까지 스레드가 블록됨
        - 구현이 단순하지만, 동시 연결이 많아지면 스레드 수 급증 → 성능 저하
        - 복잡도는 낮고 확장성도 낮음 (스레드 많아짐)

    - [Non-blocking I/O (NIO)]
        - Single-thread + Selector 기반의 이벤트 처리 모델
        - 채널을 등록하고, Selector를 통해 여러 채널의 I/O 이벤트를 감시
        - I/O 작업이 준비되지 않아도 스레드가 블로킹되지 않음
        - 복잡도는 높음(셀렉터/채널 관리), 확장성 높음(셀렉터로 수천 개 처리)

- Java에서 Netty를 활용한 네트워크 프로그래밍의 장점
    - [Netty]
        - Netty는 Java 기반의 비동기 이벤트 기반 고성능 네트워크 프레임워크
        - TCP/UDP/HTTP/WebSocket 등 다양한 프로토콜 지원

    - [주요 장점]
        - NIO 기반: 블로킹 없이 수천~수만 개 연결 처리 가능
        - ChannelPipeline: 요청 처리 흐름을 핸들러 체인으로 구성 → 높은 유연성
        - ThreadPool 관리 최적화: I/O 작업과 비즈니스 로직을 분리
        - 성능 최적화: Zero-Copy, DirectBuffer, ByteBuf 등 제공
        - WebSocket, TLS, HTTP2 등 다양한 프로토콜 지원

    - [실전 사용 예]
        - 실시간 메시징 서버, 게임 서버, IoT 게이트웨이, 고성능 API Gateway 등

- Java에서 Zero-Copy 기법을 활용하여 성능을 최적화하는 방법
    - [Zero-Copy 개념]
        - 데이터를 커널 공간 → 유저 공간으로 복사하지 않고, 
        - 커널 레벨에서 직접 처리하여 불필요한 데이터 복사를 줄이는 기술

    - [전통적 방식]
        - 디스크 → 커널 버퍼 → 사용자 버퍼 → 소켓 버퍼 → NIC

    - [Zero-Copy 방식]
        - 디스크 → 커널 버퍼 → 소켓 버퍼 → NIC (사용자 영역 복사 생략)

    - [Java에서 적용 방법]
        - FileChannel.transferTo() / transferFrom()
            ```java
            FileChannel source = new FileInputStream("file").getChannel();
            WritableByteChannel dest = Channels.newChannel(socket.getOutputStream());
            source.transferTo(0, source.size(), dest);
            ```

        - Netty 내부의 FileRegion, DirectBuffer 사용
            - Netty는 내부적으로 Zero-Copy를 추상화하여 자동 적용

    - [효과]
        - CPU 사용량 감소
        - GC 부담 줄어듦
        - 대용량 파일 전송 시 효율 극대화

- Java에서 WebSockets을 활용한 실시간 통신 구현 방법
    - 개요
        - 가장 일반적인 방법은 Java EE의 javax.websocket API 또는 Spring Framework의 Spring WebSocket을 사용하는 것

    - Java EE 방식 (javax.websocket API)
        - 주요 라이브러리
            - javax.websocket
            - 서버: Tomcat 8+, Jetty, GlassFish 등

        - 기본 구성
            - ① 의존성 추가 (예: Maven)
                ```xml
                <dependency>
                    <groupId>javax.websocket</groupId>
                    <artifactId>javax.websocket-api</artifactId>
                    <version>1.1</version>
                </dependency>
                ```

            - ② 서버 엔드포인트 정의
                ```java
                import javax.websocket.*;
                import javax.websocket.server.ServerEndpoint;
                import java.io.IOException;

                @ServerEndpoint("/chat")
                public class ChatEndpoint {

                    @OnOpen
                    public void onOpen(Session session) {
                        System.out.println("Connected: " + session.getId());
                    }

                    @OnMessage
                    public void onMessage(String message, Session session) throws IOException {
                        System.out.println("Received: " + message);
                        session.getBasicRemote().sendText("Echo: " + message);
                    }

                    @OnClose
                    public void onClose(Session session) {
                        System.out.println("Disconnected: " + session.getId());
                    }

                    @OnError
                    public void onError(Session session, Throwable throwable) {
                        throwable.printStackTrace();
                    }
                }
                ```

            - ③ 클라이언트 연결 (JS 예시)
                ```js
                const socket = new WebSocket("ws://localhost:8080/your-app/chat");
                socket.onmessage = (e) => console.log(e.data);
                socket.send("Hello");
                ```

    - Spring Framework 방식 (Spring WebSocket + STOMP)
        - 주요 의존성 (Spring Boot 기준)
            ```xml
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-websocket</artifactId>
            </dependency>
            ```

        - 서버 구성 단계
            - ① WebSocket 설정
                ```java
                @Configuration
                @EnableWebSocketMessageBroker
                public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
                    @Override
                    public void configureMessageBroker(MessageBrokerRegistry registry) {
                        registry.enableSimpleBroker("/topic"); // 구독 주소
                        registry.setApplicationDestinationPrefixes("/app"); // 송신 주소
                    }

                    @Override
                    public void registerStompEndpoints(StompEndpointRegistry registry) {
                        registry.addEndpoint("/ws").withSockJS(); // 웹소켓 엔드포인트 등록
                    }
                }
                ```

            - ② 메시지 수신/전송 Controller
                ```java
                @Controller
                public class ChatController {
                    @MessageMapping("/send") // 클라이언트가 보낼 주소 (/app/send)
                    @SendTo("/topic/messages") // 구독자에게 브로드캐스트
                    public String handle(String message) {
                        return "Received: " + message;
                    }
                }
                ```

            - ③ 클라이언트 (JS + SockJS + STOMP)
                ```html
                <script src="https://cdn.jsdelivr.net/npm/sockjs-client"></script>
                <script src="https://cdn.jsdelivr.net/npm/stompjs"></script>
                <script>
                const socket = new SockJS("/ws");
                const stomp = Stomp.over(socket);

                stomp.connect({}, () => {
                    stomp.subscribe("/topic/messages", (msg) => {
                    console.log(msg.body);
                    });

                    stomp.send("/app/send", {}, "Hello from client!");
                });
                </script>
                ```
    - 상황에 따른 선택
        - 단순한 서버-클라이언트 웹소켓 통신 -> javax.websocket (Java EE)
        - 복잡한 메시징 구조, 브로드캐스트, 인증 -> Spring WebSocket + STOMP

- Java에서 gRPC와 REST API의 차이점
    - 프로토콜 및 데이터 포맷
        - REST-API
            - 전송 프로토콜: HTTP 1.1
            - 데이터 포맷: JSON (텍스트 기반)
            - 성능: 상대적으로 느림
            - 인터페이스 정의: OpenAPI (Swagger 등)
        - gRPC
            - 전송 프로토콜: HTTP/2
            - 데이터 포맷: Protocol Buffers (바이너리)
            - 성능: 빠름 (바이너리 + HTTP/2 스트리밍)
            - 인터페이스 정의: .proto 파일 기반 명세

    - 특징 요약
        - REST: 직관적이고 범용적, 브라우저/프론트엔드 친화적
        - gRPC: 고성능, 양방향 스트리밍, 엄격한 타입, 내부 마이크로서비스 간 통신에 유리

- Java에서 HttpClient와 URLConnection의 차이점
    - URLConnection (구버전 API)
        - java.net.URLConnection, JDK 1.1부터 존재
        - 기능 제한적, 비동기 미지원, 설정 불편 (헤더, 타임아웃 등)
        - 예외 처리, 쿠키, 인증 등 수동 처리 필요

    - HttpClient (JDK 11부터)
        - java.net.http.HttpClient
        - 비동기 지원 (CompletableFuture), HTTP/2 지원
        - 사용 간결, 표준화된 API, 리액티브 스타일 가능

    - 비교 예시
        ```java
        // HttpClient (추천)
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://example.com"))
            .build();
        HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
        ```

- Java에서 Thread Dump를 분석하는 방법
    - Thread Dump 개념
        - JVM에서 실행 중인 모든 스레드의 상태(stack trace) 를 출력한 내용
        - Deadlock, 병목, 무한 루프 등 진단에 사용

    - 획득 방법
        - 콘솔: kill -3 <pid> (Unix)
        - jcmd: jcmd <pid> Thread.print
        - jstack: jstack <pid>
        - VisualVM, JMC 등 툴 사용

    - 분석 포인트
        - RUNNABLE: CPU 사용 중
        - BLOCKED: 다른 스레드가 락을 잡고 있어 대기
        - WAITING / TIMED_WAITING: wait() 또는 sleep() 상태
        - java.lang.Thread.State 정보로 스레드 상태 확인

    - Deadlock 확인
        - 스레드 A가 락 X를 잡고, Y를 기다리며
        - 스레드 B가 락 Y를 잡고, X를 기다리는 경우
        ```csharp
        Found one Java-level deadlock:
        "Thread-1":
            waiting to lock monitor 0x000... (object A), held by "Thread-2"
        "Thread-2":
            waiting to lock monitor 0x000... (object B), held by "Thread-1"
        ```

- Java에서 Deadlock이 발생하는 원인과 해결 방법
    - 발생 원인
        - 두 개 이상의 스레드가 서로 상대방의 락을 점유한 상태에서 대기
        - 일반적으로 락 획득 순서 불일치 또는 중첩 락 획득에서 발생

    - 재현 예시
        ```java
        synchronized (lockA) {
            synchronized (lockB) { /* ... */ }
        }

        synchronized (lockB) {
            synchronized (lockA) { /* ... */ }
        }
        ```

    - 해결 방법
        - 락 획득 순서 통일
            - 모든 스레드가 항상 같은 순서로 락을 요청

        - tryLock() 사용 (ReentrantLock)
            - 일정 시간 내 락 획득 실패 시 포기 → 교착 상태 방지

        - Deadlock 감지 도구 사용
            - jstack, VisualVM, DeadlockDetector 사용

        - 동시성 제어 구조 리팩토링
            - 락 사용 최소화, 메시지 큐 기반 구조 도입

- Java에서 Thread.sleep()과 Object.wait()의 차이점
    - 개요
        - Thread.sleep()과 Object.wait()는 Java에서 스레드를 일시 중단(suspend)시키는 데 사용되지만, 동작 방식과 목적이 다름

    - Thread.sleep(ms)
        - 목적
            - 스레드를 지정된 시간(ms) 동안 일시적으로 멈추게 함.

        - 특징
            - 현재 스레드를 멈춤 (CPU 점유 안 함)
            - 잠금(lock)을 해제하지 않음
            - 아무 객체와도 관련이 없음

        - 참고
            - sleep() 중인 스레드는 interrupt()로 깨울 수 있음
            - 예외: InterruptedException 발생 가능

    - Object.wait()
        - 목적
            - 스레드를 지정된 시간 또는 notify() 호출 전까지 대기시킴
            - 스레드 간 동기화(synchronization)를 위해 사용됨

        - 특징
            - wait()은 반드시 synchronized 블록/메서드 안에서 호출해야 함
            - 호출 시, 해당 객체의 모니터 락(lock)을 반납함
            - notify()나 notifyAll()이 호출되면 대기 중인 스레드가 깨어남

        - 예시
            ```java
            synchronized (sharedObject) {
                sharedObject.wait(); // wait 중에는 lock을 반납함
            }
            ```

    - 결론
        - sleep()은 단순한 시간 지연.
        - wait()은 동기화된 환경에서 다른 스레드의 작업을 기다릴 때 사용합니다

- Java에서 ScheduledThreadPoolExecutor의 활용 방법
  - 용도: 주기적/지연된 작업 실행
  - 생성: new ScheduledThreacPoolExecutor(nThreads)
  - 사용 예시
    ```java
    executor.scheduleAtFixedRate(task, initialDelay, period, TimeUnit.SECONDS);
    ``` 
  - 장점
    - 타이머보다 정확하고 예외처리 안전
    - 병렬 실행 가능 (스레드 수 조절 가능)

- Java에서 ThreadLocal의 메모리 누수 문제를 방지하는 방법
    - 문제 원인: ThreadLocal 변수는 Thread에 종속되어 Thread가 종료되지 않으면 GC 대상이 안됨 (특히 ThreadPool 사용 시)

    - 예방 방법:
        - 작업 완료 후 ThreadLocal.remove() 호출
        - 가능하면 스레드 재사용 없는 환경에서만 사용
        - ThreadLocal 사용을 피하고 다른 컨텍스트 전달 방식 고려

- CompletableFuture.supplyAsync()
    - 비동기적으로 Supplier의 결과를 반환하는 작업을 실행.
    - 기본적으로 ForkJoinPool.commonPool() 사용, 특정 Executor 전달 가능.

- Virtual Threads (Project Loom)
    - 경량 스레드. OS 스레드보다 생성·스케줄링 비용이 낮아 수만 개 동시 실행 가능
    - 기존 Thread API와 호환되며 블로킹 코드도 효율적으로 처리.

- GraalVM AOT 컴파일
    - 자바 코드를 네이티브 바이너리로 변환해 JIT 준비 시간 제거, 시작 속도 및 메모리 사용 최적화. 
    - 네이티브 이미지 빌드 시 리플렉션, 동적 로딩 주의 필요.

- Project Panama
    - JNI 없이 자바에서 네이티브 라이브러리와 직접 상호작용 가능. 
    - MemorySegment, Foreign Function API 제공.

- Structured Concurrency
    - 여러 작업을 그룹으로 관리해 전체 성공·실패를 제어. 
    - 스레드 수명과 작업 범위를 명확히 하여 리소스 누수 방지.

- CDS (Class Data Sharing)
    - 클래스 메타데이터를 미리 로드해 공유 메모리 맵에 저장, JVM 시작 속도 개선 및 메모리 절약. 
    - AppCDS로 사용자 클래스도 포함 가능.

- Dispatchers.IO 에서 ANR 발생 원인 / 해결책
    - 과도한 IO 스레드 블로킹, 메인 스레드로의 전환 지연 시 발생
    - 해결책:
        - IO 범위를 최소화, suspend 함수/비차단 IO 사용
        - withContext로 명확히 컨텍스트 전환

- 2025년 안드로이드 / 자바 / 코틀린 트렌드
    - Java: Virtual Threads, Structured Concurrency, GraalVM 네이티브 이미지 확산.
    - Kotlin: K2 Compiler 안정화, Compose Multiplatform 확대, Coroutine 구조적 동시성 강화.
    - Android: Compose 1.x → 2.x 전환, Jetpack 라이브러리 성능 최적화, AI 기반 코드 생성·분석 도구 확산.

- Kotlin vs Java 주요 차이점
    - 널 안정성, 확장 함수, 데이터 클래스, 코루틴 지원, 스마트 캐스팅 등 문법적 간결성과 안정성 강화.

- var vs val
    - var: 변경 가능 변수
    - val: 읽기 전용(한 번 초기화 후 변경 불가).

- lateinit vs lazy
    - lateinit: 나중에 초기화하는 var, nullable 불필요. 
    - lazy: 최초 접근 시 초기화하는 val.

- data class 사용 이유
    - equals(), hashCode(), toString(), copy() 자동 생성
    - 값 기반 객체 표현에 적합.

- sealed class vs enum class
    - sealed: 타입 계층 제한, 상태 표현·패턴 매칭에 적합
    - enum: 고정된 상수 집합 표현.

- companion object vs object
    - companion object: 클래스 내부의 정적 멤버 보관.
    - object: 싱글톤 인스턴스 생성.

- open 키워드 사용 이유
    - Kotlin의 클래스와 메서드는 기본적으로 final
    - open은 상속이나 오버라이드를 허용하기 위해 사용

- Functional Interface와 Lambda Expression 관계
    - Functional Interface(추상 메서드 1개)는 람다식의 대상이 될 수 있음
    - 람다는 이를 구현한 익명 클래스의 축약 표현

- Stream API 활용
    - 컬렉션/배열 데이터를 선언형으로 처리.
    - stream().filter().map().collect() 패턴으로 필터링, 변환, 집계 가능.

- Comparator vs Comparable
    - Comparable: 객체 자체에 정렬 기준 구현(compareTo).
    - Comparator: 외부에서 정렬 기준 정의(compare).

- 앱 디버깅 & 메모리 관리
    - 메모리 릭 찾기/해결
    - LeakCanary, Android Profiler로 탐지. Context 누수, static 참조, 리스너 해제 누락 방지.

- 크래시 발생 시 디버깅
    - Logcat 스택 트레이스 확인 → 원인 코드 추적 → 재현 → 수정 및 예외 처리.

- Android 기본 개념
    - Lifecycle
        - 액티비티: onCreate → onStart → onResume → onPause → onStop → onDestroy.
        - 프래그먼트: onAttach → onCreate → onCreateView → onViewCreated → onStart → …

- Service vs Foreground Service
    - Service: 백그라운드 작업 수행, UI 없음.
    - Foreground Service: 사용자 인지 필요, 알림 필수, 종료 우선순위 낮음.

- ViewBinding vs DataBinding
    - ViewBinding: 타입 안전한 뷰 참조.
    - DataBinding: XML에서 데이터 바인딩, 양방향 바인딩 지원.

- UI/구조
    - Jetpack Compose vs 기존 View 시스템
    - Compose: 선언형 UI, 상태 기반 렌더링, XML 불필요.
    - 기존 View: 명령형, XML + findViewById 기반.

- RecyclerView에서 ViewHolder 패턴 중요성
    - findViewById 반복 호출 방지, 성능 및 스크롤 효율 향상.

- 권한 & 아키텍처
    - 권한 요청 변화 (Android 6.0 이후, 마시멜로우 버전 이후)
    - 설치 시점 권한 부여 → 실행 중(Runtime) 요청으로 변경. 
    - 위험 권한은 사용자 동의 필요.

- 멀티 모듈 장단점
    - 장점: 빌드 속도 개선, 코드 재사용, 팀 병렬 작업 용이.
    - 단점: 설정 복잡, 모듈 간 의존성 관리 필요.

- DI 라이브러리 사용 경험
    - Dagger/Hilt/Koin 등으로 의존성 주입, 모듈화, 테스트 용이성 확보.

- ANR 해결 방법
    - 메인 스레드에서 장시간 작업 금지 → 네트워크·DB·파일 I/O는 별도 스레드/코루틴 사용.
    - UI 렌더링 최적화, BroadcastReceiver 실행 시간 최소화, StrictMode로 블로킹 코드 점검.

- OOP 특징
    - 추상화, 캡슐화, 상속, 다형성.

- JVM / JRE / JDK
    - JVM: 바이트코드 실행 환경.
    - JRE: JVM + 라이브러리.
    - JDK: JRE + 개발 도구(javac 등).

- Retrofit vs Volley
    - Retrofit: 선언형 API, OkHttp 기반, JSON 직렬화 용이.
    - Volley: 요청 큐 기반, 이미지 로딩·캐싱 지원, 소규모 프로젝트 적합.

- Crashlytics 활용
    - 앱 크래시 자동 수집·분석, 로그·사용자 정보 첨부, 특정 빌드·기기별 이슈 추적, 실시간 경고.

- Java 메모리 & 동시성
    - GC 동작
        - 참조되지 않는 객체 식별 → Heap 영역 청소. 
        - Stop-the-world 발생 가능, GC 알고리즘(Serial, Parallel, G1 등) 사용.

- volatile / synchronized / Atomic 차이
    - volatile: 가시성 보장, 원자성 미보장.
    - synchronized: 임계영역 잠금, 가시성·원자성 보장, 성능 저하 가능.
    - Atomic: 락 없이 원자성 연산 제공(CAS 기반).

- Java 8 기능
    - 주요 추가 사항
        - 람다 표현식, Stream API, Optional, 메서드 참조(::), 기본 메서드(default method) in interface, 날짜·시간 API(java.time).

- Checked vs Unchecked Exception
    - Checked: 컴파일 시 처리 강제(IOException, SQLException 등).
    - Unchecked: Runtime 시 발생(NullPointerException 등), 처리 강제 없음.

- HashMap vs ConcurrentHashMap
    - HashMap: 비동기, null key 1개 허용.
    - ConcurrentHashMap: 동기화 지원, 분할 락(Concurrent Level), null key 불허.

- Reflection
    - 주의점
        - 성능 저하, 캡슐화 위반, 보안 이슈. 런타임 오류 가능성 높음.

- Kotlin vs Java
    - 주요 차이점
        - Kotlin: Null-safety, 데이터 클래스, 확장 함수, 코루틴, 간결 문법.
        - Java: 더 광범위한 생태계, 명시적 문법, NullPointerException 발생 가능.

- Kotlin Data Class
    - 차이점
        - data class: equals(), hashCode(), toString(), copy(), componentN() 자동 생성.
        - 일반 클래스: 위 메서드 수동 구현 필요.

- Kotlin & Coroutine
    - suspend 함수와 Coroutine 작동 방식
        - suspend 함수는 일시 중단 가능한 함수로, 코루틴 컨텍스트에서만 호출 가능.
        - 일시 중단 시 스레드를 블록하지 않고, 다른 작업으로 전환 후 재개 시 상태 복원.

- lateinit vs lazy
    - lateinit: 
        - 나중에 초기화되는 var (non-null), primitive 불가, 초기화 전 접근 시 예외.
    - lazy: 
        - 호출 시 최초 1회 초기화되는 val, 쓰레드 안전 모드 선택 가능 (LazyThreadSafetyMode).

- SharedFlow vs StateFlow
    - SharedFlow: replay 가능, 상태 개념 없음, 여러 이벤트 브로드캐스트.
    - StateFlow: 항상 최신 상태 1개 보유, 구독 시 즉시 최신값 전달.

- Delegation 패턴
    - 기능을 다른 객체에 위임해 코드 재사용 및 컴포지션 강화.
    - 예: class MyList(private val list: List<T>) : List<T> by list.

- Slot API
    - 부모 컴포저블이 UI 구조를 정의하고, 자식 콘텐츠를 슬롯 형태로 전달받아 렌더링.
    - 예: Scaffold(topBar = { TopAppBar(...) }, content = { ... }).

- invoke operator 예제
    ```kotlin
    class Greeter(val msg: String) {
        operator fun invoke(name: String) = "$msg, $name"
    }
    val hello = Greeter("Hello")
    println(hello("World")) // Hello, World
    ```
    - 객체를 함수처럼 호출 가능.

- Kotlin Multiplatform
    - 문제점
        - 플랫폼별 API 차이, 네이티브 의존성 충돌, Gradle 빌드 속도 저하.
    - 해결
        - expect/actual 키워드로 플랫폼별 구현 분리, 공통 모듈 최소화, Gradle 캐시 활용.

- SharedPreferences commit vs apply
    - commit(): 동기 저장, 성공 여부 반환, 메인 스레드에서 호출 시 ANR 위험.
    - apply(): 비동기 저장, 반환값 없음, 즉시 메모리에 반영 후 백그라운드 저장.

- 메모리 누수 줄이는 방법
    - Context 참조 관리(Activity 참조 보관 금지), 리스너/콜백 해제, ViewBinding 해제, static 변수 남용 방지, Lifecycle-aware 컴포넌트 사용.

- 비트맵보다 용량이 작고 XML로 작성 가능한 방법
    - Vector Drawable 사용 (해상도 독립, 용량 작음).

- 빌드 시간 단축 방법
    - Gradle Daemon 사용, Gradle 캐시 활성화, 불필요한 리소스/모듈 제거, Instant Run/Apply Changes 활용, Kotlin incremental compilation, 멀티 모듈 병렬 빌드.

- Gradle & 빌드 옵션
    - aaptOptions.cruncherEnabled = false
        - PNG 최적화(crunching) 비활성화.
        - 빌드 속도는 빨라지지만 리소스 크기는 커질 수 있음.
        - 주로 개발 빌드에서 빌드 시간 단축 용도로 사용.

    - ext.alwaysUpdateBuildId = false
        - 빌드 시 마다 새로운 Build ID를 생성하지 않도록 설정.
        - Gradle 캐시 활용도를 높여 빌드 속도 개선.

- Flow vs Channel
    - Flow: cold stream, 구독 시 데이터 흐름 시작, 선언적 비동기 스트림 처리.
    - Channel: hot stream, 실시간 데이터 전송 파이프, producer-consumer 패턴에 적합.

- Jetpack Compose
    - Composition: Composable 함수 트리를 UI에 배치하는 초기 과정.
    - Recomposition: 상태 변경(State 변화)로 인해 UI의 일부 또는 전체를 다시 그리는 과정.
    - 발생 조건: State, MutableState, Flow/LiveData collect, remember 값 변경 등.

- WorkManager vs AlarmManager
    - WorkManager: 지연·조건 기반 백그라운드 작업, 앱 종료/재부팅 후에도 보장, 네트워크 조건 설정 가능.
    - AlarmManager: 특정 시각 또는 주기로 실행, 보장성 낮고 조건 제어 제한적.

- 성능 모니터링
    - StrictMode 활용
    - 개발 중 메인 스레드의 디스크/네트워크 접근, 누수 객체, 리소스 누출 등을 감지.
    - 예: StrictMode.setThreadPolicy 로 UI 스레드에서 I/O 작업 탐지.

- ViewModel 관리
    - Scope별로 ActivityViewModel, FragmentViewModel, Navigation Graph ViewModel로 구분 관리.
    - Activity 공용 데이터 → Activity Scope,
    - 특정 화면만 → Fragment Scope,
    - 네비게이션 흐름 전체 → NavGraph Scope.

- 데이터 영속성
    - DataStore: 비동기, 타입 안전(Preferences vs Proto), 최신 권장 방식, 트랜잭션 안전.
    - Room: SQLite 기반 구조화 데이터 저장, 쿼리 가능, 대량 데이터 적합.
    - SharedPreferences: 간단한 key-value, 동기 방식은 ANR 위험, 경량 데이터에 적합.

- Parcelable vs Serializable
    - Parcelable: Android 전용, 빠른 성능, 메모리 효율 높음, Boilerplate 코드 필요.
    - Serializable: Java 표준, 속도 느림, GC 부하 높음.
        - ⇒ Android에서는 성능 때문에 Parcelable 선호.

- MotionLayout 애니메이션
    - ConstraintLayout 확장으로, XML 기반 Scene/Transition 정의.
    - 시작·종료 상태 제약조건을 지정하고, Transition 속성과 KeyFrame으로 세밀한 애니메이션 구현 가능.
    - 예: MotionScene XML → MotionLayout 위젯에서 실행.

- Jetpack Navigation Component – Deep Link
    - 동작 방식:
        - 딥링크 URI/Intent를 NavController가 수신하여 지정된 목적지(Fragment/Activity)로 이동.
        - 그래프 XML에 <deepLink app:uri="..."/>로 선언하거나 코드로 추가 가능.

    - 활용 사례:
        - 알림 클릭 시 특정 화면 이동, 외부 앱에서 콘텐츠 직접 열기, 웹 URL과 앱 화면 매핑.

- 앱 보안 강화
    - ProGuard/R8: 코드 난독화, 최적화, 사용하지 않는 코드 제거. proguard-rules.pro로 예외 규칙 설정.
    - App Integrity: Google Play의 앱 무결성 API를 활용해 변조된 앱 탐지.
    - 추가: 네트워크 전송 시 HTTPS/TLS 강제, 키/토큰 안전 저장, 디버그 빌드 배포 방지.

- Java – ClassLoader 동작 원리
    - Bootstrap ClassLoader: JVM 코어 라이브러리 로드(java.lang.*).
    - Extension ClassLoader: 확장 라이브러리(jre/lib/ext).
    - System ClassLoader: 애플리케이션 클래스패스 로드.
    - Custom ClassLoader: 네트워크/압축 파일 등 커스텀 로딩 로직 구현 시 사용.

- ThreadLocal
    - 역할: 스레드마다 독립적인 변수를 저장해 동시성 문제 방지.
    - 활용 사례: 스레드 전용 DB 연결, 포맷터(SimpleDateFormat) 인스턴스 공유 방지.

- final 키워드
    - 클래스: 상속 불가.
    - 메서드: 오버라이드 불가.
    - 변수: 재할당 불가(참조형은 참조 변경만 불가, 내부 상태 변경 가능).

- static 키워드
    - 클래스 레벨 멤버, 인스턴스 생성 없이 접근 가능.
    - 모든 인스턴스가 공유하는 값/메서드.
    - static block으로 클래스 로딩 시 초기화 가능.

clone() 문제점
얕은 복사로 인한 참조 공유 문제 발생.

깊은 복사 구현 필요.

Cloneable 인터페이스 구현 필요하며, 생성자 호출 안 되므로 초기화 로직 누락 가능.

Serializable 인터페이스
객체를 바이트 스트림으로 변환/복원 가능하게 하는 마커 인터페이스.

네트워크 전송, 파일 저장 등에 활용.

transient 키워드
직렬화 시 제외할 필드 지정.

민감 정보(비밀번호), 캐시 데이터, 직렬화 불필요 데이터에 사용.

try-with-resources
AutoCloseable 구현 객체의 자원을 자동으로 close().

예외 발생 여부와 상관없이 안전하게 리소스 해제.

코드 간결화 및 누수 방지.


Java – Optional 활용
역할: null 참조를 안전하게 다루기 위한 컨테이너.

사용 예:

java
코드 복사
Optional<String> name = Optional.ofNullable(getName());
name.ifPresent(System.out::println);
String result = name.orElse("default");
장점: NPE 방지, 명시적인 null 처리 흐름 제공.

varargs(가변 인자) 주의점
내부적으로 배열로 처리되므로 성능에 민감한 경우 반복 호출 주의.

오버로딩 시 모호성 발생 가능.

null 전달 시 NullPointerException 가능성.

enum 활용과 장점
활용: 상태/상수 집합 표현, switch-case에서 안전하게 사용.

장점: 타입 안정성, 메서드/필드 추가 가능, 싱글턴 패턴 구현 가능.

CompletableFuture vs ExecutorService
ExecutorService: 작업 제출/스레드 풀 관리 중심, 반환값 Future.

CompletableFuture: 비동기 연산 체이닝, 콜백 처리, 조합 가능.

java
코드 복사
CompletableFuture.supplyAsync(() -> "Data")
                 .thenApply(String::toUpperCase)
                 .thenAccept(System.out::println);
GC 알고리즘 차이
G1 GC: 힙을 리전으로 나누고 병렬/동시 수집, 짧은 STW 목표.

CMS: 동시 마크-스윕, STW 최소화, 단편화 문제 존재.

ZGC: 매우 낮은 지연 시간(<10ms), 대규모 힙(테라바이트) 지원.

최적화: GC 로그 분석, 힙 크기 조정, 적절한 GC 선택.

synchronized / Lock / ReentrantLock
synchronized: JVM 모니터 락, 간단하지만 세밀한 제어 불가.

Lock: 명시적 lock/unlock, 타임아웃, 인터럽트 가능.

ReentrantLock: 동일 스레드 재진입 가능, 조건변수(Condition) 지원.

ForkJoinPool
용도: 큰 작업을 작은 태스크로 분할해 병렬 처리(Work-Stealing).

활용 예: 재귀적 분할-정복 알고리즘, 병렬 스트림 내부 실행기.

AOSP – init 프로세스 & 서비스 관리
init: 부팅 시 최초 실행, init.rc 스크립트 기반 서비스 시작/환경 설정.

서비스 관리: service 선언, property trigger, restart policy 적용.

AOSP – Binder & IPC
Binder 드라이버: 커널 모듈 /dev/binder를 통해 프로세스 간 메서드 호출 가능.

IPC 메커니즘: 프록시-스텁 구조, 직렬화(Parcel) 기반 데이터 전송, 보안 검증 포함.

Android – MVI Orbit
Orbit MVI: 상태(state), 사이드 이펙트 처리, View-ViewModel 단방향 데이터 흐름.

특징: 코루틴 기반, DSL 스타일로 상태 변경 정의.

GC 방식
Serial GC: 단일 스레드, 작은 힙에 적합.

Parallel GC: 멀티스레드, 처리량 위주.

CMS, G1, ZGC, Shenandoah: 저지연·대규모 힙 지원.

Multi-threading 구현
Thread 클래스 상속

Runnable 구현

ExecutorService

ForkJoinPool

CompletableFuture / Parallel Streams

Immutable 객체 설계 & 장점
설계:

모든 필드 final

setter 없음

가변 객체는 복사본 저장

장점: 스레드 안전성, 예측 가능한 동작, 캐싱 최적화 가능.


- Java 17의 최신 기능과 주요 변경 사항을 설명하라.
- Spring Boot의 IoC 컨테이너에서 Bean Lifecycle과 @PostConstruct, @PreDestroy의 역할은?
- Kotlin의 inline, noinline, crossinline 키워드는 언제 사용하는가?
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
- Android에서 Service와 JobIntentService의 차이점은?
- Jetpack Compose에서 recomposition이 발생하는 조건은?
- Jetpack Compose에서 remember와 rememberSaveable의 차이점은?
- Kotlin Coroutines에서 Structured Concurrency가 왜 중요한가?
- Kotlin에서 suspend function이 호출되는 스레드는 어떻게 결정되는가?


- Kotlin에서 inline functions을 사용할 때의 장점과 단점은?
- Kotlin에서 Flow와 LiveData의 차이점은?
- Compound Component 패턴과 Slot API 설명
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
- Kotlin에서 copy() 메서드를 사용하는 이유는?
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
- Kotlin의 reified 키워드가 동작하는 원리를 설명하시오.
- Kotlin의 sealed interface와 sealed class의 차이점 및 내부 구현 차이는?
- Kotlin의 default parameter와 Java의 method overloading 차이점은?
- Kotlin에서 String interpolation이 내부적으로 어떻게 최적화되는가?
- Kotlin의 메모리 관리 방식과 Java의 GC(Garbage Collector) 차이점은?
- Kotlin에서 가변 객체(mutable object)의 성능 최적화 방법은?
- Kotlin에서 immutable 객체를 구현하는 방법과 효과적인 활용 사례는?
- Kotlin의 escape analysis가 어떻게 동작하는지 설명하시오.
- Kotlin의 inline function이 내부적으로 어떻게 동작하는가?
- Kotlin에서 tail recursion이 동작하는 방식을 설명하시오.


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
- Kotlin에서 @OptIn 어노테이션을 사용하는 이유는?


- Kotlin Coroutines의 핵심 개념은?
- suspend 함수란 무엇이며, 일반 함수와의 차이점은?
- Kotlin Coroutines에서 테스트를 수행하는 방법은?
- ViewModelScope를 활용하여 네트워크 요청을 수행하는 방법은?
- Retrofit과 Coroutines을 함께 사용할 때의 장점은?
- Room Database에서 Coroutines을 사용하는 이유는?
- Android에서 LiveData와 StateFlow를 함께 사용할 때의 고려사항은?
- WorkManager와 Coroutines을 함께 사용할 때의 주의점은?
- MutableSharedFlow에서 replay 옵션을 설정하는 이유는?
- StateFlow에서 초기 값을 설정해야 하는 이유는?
- yield() 함수의 역할은?
- cancel()을 호출한 후에도 코루틴이 종료되지 않는 이유는?


- ensureActive() 함수의 역할은?
- select {} 블록을 활용하여 여러 채널을 동시에 처리하는 방법은?
- produce {}와 consumeEach {}의 차이점은?
- Mutex와 Atomic을 활용한 동시성 문제 해결 방법은?
- Android에서 코루틴을 활용한 백그라운드 작업 최적화 방법은?
- CoroutineContext의 구성 요소는?
- withContext()와 async-await의 차이점은?
- Dispatchers.IO, Dispatchers.Main, Dispatchers.Default의 차이점은?
- runBlocking을 사용하는 것이 위험한 이유는?
- Kotlin Coroutines에서 Structured Concurrency란?
- CoroutineExceptionHandler의 역할은?
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
- combine() 연산자를 활용한 데이터 스트림 결합 방법은?
- retry()와 catch() 연산자의 차이점은?
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