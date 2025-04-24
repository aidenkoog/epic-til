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

- Compound Component 패턴과 Slot API 설명
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

- Android에서 onSaveInstanceState()와 ViewModel의 차이점
- Android의 Activity와 Fragment의 생명주기에서 주요 차이점
- Jetpack Lifecycle Observer의 역할과 활용 방법
- Android에서 ContentProvider의 역할과 사용 사례
- RecyclerView의 ViewHolder 패턴을 사용하는 이유와 성능 최적화 방법
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

- AOSP의 SELinux 정책과 보안 메커니즘에 대해 설명해주세요.
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

- AOSP의 init 프로세스와 서비스 관리 방법을 설명해주세요.
- AOSP의 Binder 드라이버와 IPC 메커니즘에 대해 설명해주세요.
- Android MVI orbit 설명
- Java의 JVM, JRE, JDK의 차이점은?
- Java의 Garbage Collection 방식에는 어떤 것들이 있는가?
- Java에서 Multi-threading을 구현하는 방법은?
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

- Java에서 Stream API를 활용하는 방법은?
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

- Java의 다형성(Polymorphism)이란 무엇이며, 어떻게 구현되는가?
- Java에서 오버로딩(Overloading)과 오버라이딩(Overriding)의 차이점은?
- Java에서 인터페이스(Interface)와 추상 클래스(Abstract Class)의 차이점은?
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

- Java에서 final 키워드를 사용할 수 있는 곳과 그 의미는?
- Java에서 static 키워드가 가지는 의미는?
- Java에서 객체를 clone()할 때 발생할 수 있는 문제는?
- Java에서 Serializable 인터페이스의 역할은?
- Java에서 transient 키워드를 사용하는 이유는?
- Java에서 try-with-resources를 사용하는 이유는?
- Java의 Optional 클래스를 활용하는 방법은?
- Java에서 varargs(가변 인자)를 사용할 때 주의할 점은?
- Java에서 enum을 활용하는 방법과 장점은?
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


- Java의 Functional Interface와 Lambda Expression의 관계는?
- Java의 Stream API를 활용하는 방법은?
- Java의 Comparator와 Comparable 인터페이스의 차이점은?
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


- Kotlin에서 @OptIn 어노테이션을 사용하는 이유는?
- Kotlin Coroutines의 핵심 개념은?
- suspend 함수란 무엇이며, 일반 함수와의 차이점은?
- launch와 async의 차이점은?
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

- CoroutineContext의 구성 요소는?
- withContext()와 async-await의 차이점은?
- Dispatchers.IO, Dispatchers.Main, Dispatchers.Default의 차이점은?
- runBlocking을 사용하는 것이 위험한 이유는?
- Kotlin Coroutines에서 Structured Concurrency란?
- CoroutineExceptionHandler의 역할은?
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

- MutableSharedFlow에서 replay 옵션을 설정하는 이유는?
- StateFlow에서 초기 값을 설정해야 하는 이유는?
- yield() 함수의 역할은?
- cancel()을 호출한 후에도 코루틴이 종료되지 않는 이유는?
- ensureActive() 함수의 역할은?
- select {} 블록을 활용하여 여러 채널을 동시에 처리하는 방법은?
- produce {}와 consumeEach {}의 차이점은?
- Mutex와 Atomic을 활용한 동시성 문제 해결 방법은?
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

- combine() 연산자를 활용한 데이터 스트림 결합 방법은?
- retry()와 catch() 연산자의 차이점은?
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

- Kotlin의 escape analysis가 어떻게 동작하는지 설명하시오.
- Kotlin의 inline function이 내부적으로 어떻게 동작하는가?
- Kotlin에서 tail recursion이 동작하는 방식을 설명하시오.
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

- Kotlin의 reified 키워드가 동작하는 원리를 설명하시오.
- Kotlin의 sealed interface와 sealed class의 차이점 및 내부 구현 차이는?
- Kotlin의 default parameter와 Java의 method overloading 차이점은?
- Kotlin에서 String interpolation이 내부적으로 어떻게 최적화되는가?
- Kotlin의 메모리 관리 방식과 Java의 GC(Garbage Collector) 차이점은?
- Kotlin에서 가변 객체(mutable object)의 성능 최적화 방법은?
- Kotlin에서 immutable 객체를 구현하는 방법과 효과적인 활용 사례는?
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
- launch와 async의 차이점은?
- runBlocking을 사용할 때의 문제점은?
- withContext()와 launch의 차이점은?
- CoroutineContext의 주요 요소(Job, Dispatcher, ExceptionHandler 등)를 설명하시오.
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

- suspend function 내부에서 try-catch를 올바르게 사용하는 방법은?
- Coroutine의 Dispatchers.Default, IO, Main의 차이점은?
- supervisorScope와 coroutineScope의 차이점은?
- Kotlin Coroutine에서 cancel()을 호출했을 때 실행 흐름은?
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
- Android에서 Service와 JobIntentService의 차이점은?
- Jetpack Compose에서 recomposition이 발생하는 조건은?
- Jetpack Compose에서 remember와 rememberSaveable의 차이점은?
- Kotlin Coroutines에서 Structured Concurrency가 왜 중요한가?
- Kotlin에서 suspend function이 호출되는 스레드는 어떻게 결정되는가?
- Kotlin에서 inline functions을 사용할 때의 장점과 단점은?
- Kotlin에서 Flow와 LiveData의 차이점은?
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
- Java에서 volatile, synchronized, Atomic의 차이를 설명하라.
- Java 8에서 추가된 주요 기능(람다, 스트림, Optional 등)에 대해 설명하라.
- Checked Exception과 Unchecked Exception의 차이는?
- HashMap과 ConcurrentHashMap의 차이점은?
- Java에서 Reflection을 사용할 때 주의할 점은?
- Kotlin과 Java의 주요 차이점은?
- Kotlin의 data class와 일반 클래스의 차이는?
- suspend 함수와 Coroutine의 작동 방식은?
- Kotlin에서 lateinit과 lazy의 차이는?
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
- Kotlin의 Flow에서 SharedFlow와 StateFlow의 차이는?
- Kotlin의 Delegation 패턴은 어떤 경우에 유용한가?
- Jetpack Compose의 Slot API 개념과 활용 사례는?
- invoke operator를 활용한 고급 함수형 프로그래밍 예제를 설명하라.
- Kotlin Multiplatform에서 JVM, Native, JS 타겟을 함께 사용할 때의 문제점과 해결 방법은?
- SharedPreferences 에서 commit() 과 apply() 의 다른점에 대해 말해주세요.
- 안드로이드에서 메모리 누수를 줄일 수 있는 방법에 대해 말해주세요.
- 안드로이드 APK 파일의 크기를 줄일 수 있는 방법들을 말해주세요.
- 비트맵보다 용량이 작으면서 XML로 작성 가능한 방법
- 안드로이드 어플리케이션의 빌드 시간을 줄일 수 있는 방법들을 말해주세요.
- aaptOptions.cruncherEnabled=false 설명
- Ext.alwaysUpdateBuildId = false 설명
- Gradle은 맨 뒤에 ‘+’를 추가하면 자동으로 최신 버전으로 업데이트, 자동 업데이트하게 하는 방법
- 채팅 기능 구현
- 프래그먼트는 기본 생성자를 왜 사용해야 할까?
- Gradle / Ant / Maven이 무엇인가?

- JAR, AAR, DEX, APK 개념
- Annotation 개념
- Custom Annotation 정의 및 커스텀 기능 구현 방법
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