#### 리팩토링 개념

- 소프트웨어 공학에서 결과의 변경없이 코드의 구조를 재조정하는 것을 의미
- 가독성 증대, 복잡성 감소, 유지보수를 용이하게 하는 목적
- 버그 수정 / 새로운 기능 추가는 리팩토링이 아님
- 사용자가 보는 외부 화면은 그대로 두면서 내부 논리나 구조를 개선하는 유지보수 행위
- 소프트웨어 설계, 구조 및 구현을 개선하는 동시에 소프트웨어 기능을 보존하는 것
- 소프트웨어를 더 이해하기 쉽고 수정하기 쉽게 만드는 것
- 성능 최적화 X => 코드를 신속하게 개발하게 해주고 코드 품질을 좋게 만들어 주는 것
- 기능 변경 X
- 개발 과정에서 편리한 코드가 되도록 재작성
- 유지 보수의 용이성 요구 => 코드 중복 제거 => 수정 편리 => 코드 품질 상승 => 개발 속도 상승

#### 리팩토링 사용 시기

- 3번 이상의 중복 / 같은 행위
  - 개발 일정 / 계획 감안한 리팩토링 수행
- 기능 추가때마다 리팩토링 수행
  - 현재 코드 유지한 채로 새 기능 추가가 어렵다면 리팩토링 권장
- 버그 수정때마다 리팩토링 수행
- 코드 리뷰때마다 리팩토링 수행
  - 많은 인원 참여는 권장 X

#### 리팩토링 과정 설명

- 단일 모듈 리팩토링 => 테스트 => 정상 동작 여부 => 반복

#### 리팩토링 불필요한 상황 설명

- 현재 코드가 정상동작 하지 않는 상태
  - 리팩토링보다 재작성 필요
- 개발 일정 마감이 다가온 상황

#### 리팩토링 원칙 설명

- Two Hats 원칙
  - 기능 추가 시: 기존 코드 수정 X, 기능 / 테스트만 추가
  - 리팩토링 시: 기존 동작 유지 상태로 내부 구조만 변경

#### 클린 코드, 코드 리팩토링의 관계 설명

- 리팩토링이 조금 더 넓은 의미
- 클린코드: 단순 가독성 증대를 위한 작업
  - 설계부터 잘 이루어져 있는 것이 중요 (기본 코드 작성 과정에서부터 잘 이루어져야 함)
- 리팩토링: 클린 코드 포함한 유지 보수를 위한 코드 개선
  - 결과물 나온 이후 수정 또는 추가 작업때마다 개선해나가는 것이 올바른 방향

#### 클린코드 설명

- 개발자가 보기에 깔끔한 코드
- 이해하기 쉬운 코드
- 클린 코드 작성 팁
  - 유명 코드 컨벤션 설정
  - 핵심 기능 코드는 주석 통한 세부적인 내용 설명
  - 동사 사용
  - 하나의 파일 내 하나의 프로그래밍 언어
  - 참조되거나 수정되는 코드는 기존 코드보다 클린해야 함
  - 매개변수 이름 생략 또는 과도한 축약 금지

#### 자바 코드 리팩토링 방법 및 예제

- 변수 선언과 초기값을 할당하는 부분이 분리되어 있을 이유는 없음
- 간단한 if-else문은 삼항 연산자로 대체 (간결성, 표현력, 유지보수성,성능의 이유)
- if-else 문을 switch로 전환 (가독성, 성능, 유지관리)
- 흐름이 긴 메소드는 분리
- 중복 코드 제거 / 메소드 분리
- 디자인 패턴 적용
- 알고리즘 / 데이터 구조 최적화 (효율적인 알고리즘 선택, 캐싱 및 지연 로드 등 사용 가능)
- 자바 코드 컨벤션 준수
- 들여쓰기 Depth가 3이 넘지 않도록 구현 (2까지만 허용)
  - while문 안에 if 문이 있다면 들여쓰기는 2
  - Depth를 줄이는 가장 좋은 방법은 함수를 분리하는 것
- 함수는 한 가지 일, 즉 단일 책임만 가지도록 최대한 작게 만들기
- 함수의 길이가 15라인을 넘어가지 않도록 구현
- else 사용 금지 (if 조건절에서 값을 반환하도록 설계하면 else 사용 불필요)

#### 리팩토링

- 마틴 파울러
  - 리팩토링 기술을 분류별로 나열

#### 리팩토링 방법

- 코드 스멜 파악

#### 코드 스멜 종류

- 이해가 어려운 이름
  - 함수, 변수, 필드, 클래스, 모듈 등의 이름
  - 기술
    - 함수 선언 변경
    - 변수 이름 변경
    - 필드 이름 변경
  - 상세 기술 내용
    - 함수 선언 변경
      - 함수 이름, 메소드 이름 변경, 매개변수 추가/제거, 시그니처 변경
      - 좋은 이름 찾는 방법
        - 함수에 주석 작성 후 주석을 함수 이름으로 일단 만들기 (가장 중요한 부분)
      - 함수 매개 변수는 함수 내부의 문맥 결정, 의존성을 결정
      - 매개 변수를 다시 받도록 수정하는 법
        - 시그니쳐 변경 (가시성, 이름, 매개변수)
    - 변수 이름 변경
      - 다이나믹 타입 지원 언어에서는 타입을 이름에 넣기도 함
      - 람다식 변수는 n, r등의 방식도 좋고 메소드 레퍼런스 방식 적용 (ex. n -> n...)
      - 예를 들어 A를 가져오는 함수 안에서 A관련 이름이 없는 것은 문제
    - 필드 이름 변경
      - 사용되는 범위가 넓으므로 이름이 중요
      - Record, Dictionary (dicts) 자료형, 자바 14버전부터
      - Record 는 Immutable 한 특징 (public record)
        - 코틀린의 데이터 클래스와 유사
- 중복되는 코드
  - 비슷한지 아닌지 살펴보기 어려움
  - 코드 변경 시 여러 곳을 변경해야 함
  - 기술
    - 함수 추출
    - 코드 분리 (코드가 비슷하나 완전히 동일하지 않은 경우, Slide Statements)
    - 메소드 올리기 (여러 하위 클래스에 동일 코드)
  - 상세 기술 내용
    - 함수 추출
      - 의도와 구현 분리, 의도를 드러내고 있는지, 구현을 드러내고 있는지
      - 함수를 봤을 때 이해하려는 노력이 필요하다면 그것은 구현
      - 한줄 짜리 메소드도 가능 (의도를 잘 드러낼수만 있다면)
      - 거대한 함수 내 주석은 도움 (주석 기준으로 함수화하면 되니까 편함)
      - 순서 정리: 함수 내 기능 파악 후 주석 작성 
      - -> 주석 기준으로 메소드 추출 
      - -> 변경된 메소드들로 다 변경 
      - -> 기존의 주석 메세지는 삭제 
      - -> 주석 삭제해도 알아보기 쉽다면 리팩토링 작업이 제대로 된 것임
    - 코드 정리 (Slide Statements)
      - 코드 위치 조정하면서 비슷한 동일한 코드 찾기
      - 함수에서 사용할 변수를 상단에 미리 정의하지 말고 해당 변수를 실제 사용하는 코드 바로 위에 선언
        - 코드들을 한 블럭 단위로 보는 것이 가능해짐
      - 관련있는 코드끼리 묶은 다음 함수 추출하기 방법으로 코드 정리 가능
    - 메소드 올리기 (Pull Up Method)
      - 중복 코드는 당장 잘 동작하더라도 미래에 버그를 만들어 낼 가능성이 높음
      - 두 메소드가 비슷한 절차를 따르고 있다면 템플릿 메소드 패턴 적용 고려 가능
      - 함수 매개변수화 작업이 선행된 이후에 적용 가능
- 긴 함수
  - 주석을 남기고 싶다면 주석 대신 함수를 만들어서 의도를 명확히 표현
  - 99%는 함수 추출로 해결 가능
  - 함수 분리 시 전달해야 될 매개변수가 많아지는 경우
    - 임시 변수를 질의 함수로 변경
    - 매개변수 객체 생성
    - 객체 통째로 전달
    - 함수를 명령으로 변경
    - 조건문 분해 (Decompose Conditional)
    - 반복문 쪼개기 (Split Loop)
    - 조건문을 다형성으로 바꾸기
  - 조건문 분해하기
  - 조건문을 다형성으로 바꾸기 (Replace Conditional with Polymorphism)
  - 반복문 안에서 여러 작업이 있어서 하나의 메소드로 추출이 어렵다면 반복문 쪼개기 적용
  - 상세 기술 내용
    - 임시 변수를 질의 함수로 변경
      - 만들어놓은 함수 내에서 쿼리가 가능한 내용이면 변수를 전달하지 않고
      - 그 함수 내에서 바로 쿼리해서 사용하도록 수정 가능 (ex. getXXX())
    - 매개변수 객체 생성
      - 같은 매개 변수들이 여러 메소드에 걸쳐 나타난다면 그 매개변수들을 묶은
      - 자료 구조 생성 가능
      - 테이터간의 관계 명시적으로 표현 가능
    - 객체 통째로 넘기기
      - 객체 통째로 넘기는 방향으로 적용 후 각각의 함수들이 해당 객체에 의존성을
      - 가지는 게 맞는 방향인지 고민해야 함
    - 함수를 명령으로 변경
      - 커맨드 패턴 맥락과 유사
      - ex. new XXX().execute();
    - 조건문 분해 (Decompose Conditional)
      - 조건식 (&&, || 등)이 복잡한 경우, if-else 복잡한 경우
      - 조건과 액션 모두 의도를 표현해야 함
      - 함수 추출하기 기법을 적용하면서 의도를 명확히 하는 방법
      - 딱 조건문들을 봤을 때 한번에 알아볼 수 없는 코드는 분해가 필요
      - 자바로 작성되어 있다면 삼항 연산자 적용도 고려 권장
    - 반복문 쪼개기 (Split Loop)
      - 하나의 반복문에서 여러 다른 작업을 하는 코드 존재할 때
      - 반복문을 여러개로 쪼개면 보다 쉽게 이해 및 수정 가능
      - 성능 문제 야기 가능하나 리팩토링은 성능 최적화와는 별개 작업 (리팩토링 후 성능 최적화 시도 순서)
      - 관련 변수와 for loop를 메소드로 분리
    - 조건문을 다형성으로 바꾸기 (Replace Conditional with Polymorphism)
      - 모든 조건문을 다형성으로 바꿀 필요 없음
      - 복잡한 Switch 문이 있는 클래스 유지한 상태로 새로운 클래스 생성
      - 복잡한 Switch 문이 있는 함수를 오버라이드해서 내용 작성
      - 장황한 조건식 제거 가능
- 긴 매개변수 목록 (Long Parameter List)
  - 문제점
    - 매개변수가 많으면 함수 역할 이해 어려움
  - 적용 가능한 것들
    - 매개 변수 객체 만들기 적용도 가능 / 통째로 넘기기 등
    - 플래그 인수 제거하기 사용 가능
    - 여러 함수가 일부 매개변수를 공통적으로 사용한다면 여러 함수를 클래스로 묶어 뺀 다음 매개변수를 해당 클래스의 멤버 필드로 지정함으로서 매개변수 개수 줄이기가 가능
  - 매개변수를 질의 함수로 바꾸기
    - 짧을수록 이해 수월
    - 어떤 매개변수를 다른 매개변수를 통해 알아낼 수 있다면 중복 매개변수 (오브젝트, 오브젝트 내 Int값)
    - 매개변수 값 전달하는 것은 함수 호출 측의 책임 (가능하면 함수 내부에서 책임지도록 처리)
  - 플래그 인수 제거 (Remove Flag Argument)
    - 플래그 사용한 함수는 차이 파악이 어려움
    - 조건문 분해하기를 활용하여 개선 가능
    - true, false에 해당하는 로직을 떼어내서 각각의 함수로 만들어서 개선
    - 예. excercise(node, true) --> exercise(node) / exerciseWithPerson(node)
  - 여러 함수를 클래스로 묶기
    - 클래스로 묶어서 필요한 자주 사용되는 매개 변수들을 멤버 변수로 설정
- 전역 데이터 (Global Data)
  - 문제점 
    - 전역 데이터는 아무곳에서나 변경 가능하다는 문제
    - 값이 바뀐 이유 추적 어려움
    - 편하게 개발 시 사용 가능하나 많이 자주 사용하면 독이 됨
  - 적용 가능한 것들
    - 변수 캡슐화하기 적용을 통해 접근 제어 가능 (Encapculate Variable)
  - 변수 캡슐화
    - 메소드 활용
    - 매소드로 감싸게 되면 Set 한 뒤 노티피케이션을 주거나 하는 등의 처리가 가능 / 설정 값에 대한 유효성 검사 로직 삽입이 가능 (값을 아무것이나 넣는 것을 방지하기 위한 목적)
    - 불변 데이터의 경우에는 리팩토링 적용 불필요
    - 접근이 쉬워 값 변경이 쉬워지며 오류 발생 가능성이 높음
    - 글로벌 접근을 허용하는 경우는 불변의 public final 인 경우에만 권장
    - Getter / Setter 통해 처리하도록 수정 필요
- 가변 데이터 (Mutable Data)
  - 가변 데이터에 대한 처리 필요한 이유
    - 함수형 프로그래밍 언어는 데이터를 변경하지 않고 복사본을 전달하는데 그밖의 프로그래밍 언어는 데이터 변경을 허용하고 있으므로 이에 대한 리스크 관리가 필요
  - 변수 쪼개기 (Split Variable)
    - 재할당 되는 변수에 대한 고민
      - 재할당 되는 변수들이 있다면 계속 재할당만 하지말고 문맥 상 의미에 따라 변수를 재 선언해서 의미를 명확하게 해줘야 함
    - 변수 하나당 하나의 책임을 가져야 함
    - 상수 활용
  - 질의 함수와 변경 함수 분리 (Separate Query from Modifier)
    - 명령 조회 분리 (Command-Query Separation) 규칙
      - 어떤 값을 리턴하는 함수는 사이드 이펙트가 없어야 함
    - 캐시는 중요한 객체 상태 변화는 아님. 분리할 필요 없음
    - 값 수정하는 로직과 다른 로직 등이 있을 때 각각을 다른 메소드로 분리
      - Get과 Set 기능의 분리
  - 세터 제거 (Remove Setting Method)
    - 해당 필드가 변경될 수 있다는 것을 의미 (세터를 제공한다는 것은)
    - 객체 생성 시 처음 설정된 값이 변경될 필요가 없다면 생성자 생성 후 세터는 제거
  - 파생 변수를 질의 함수로 변경 (Replace Derived Variable with Query)
    - 변경 가능한 데이터를 최대한 축소시키는 데에 집중4
    - 계산해서 알아낼 수 있는 변수는 제거 권장 (계산 자체가 데이터 의미를 잘 표현할 수도 있음)
    - 헤딩 변수의 변경 가능성을 제거 가능
    - assert로 계산식 유효성 확인 후 적용하는 방식으로 보통 진행
    - return this.adjustments.stream().mapToDouble(Double::valueOf().sum())
  - 여러 함수를 변환 함수로 묶기 (Combine Functions into Transform)
    - 관련있는 여러 파생 변수를 만들어내는 함수가 여러곳에서 만들어지고 사용된다면 그러한 파생 변수를 변환 함수 즉, Transform Function 을 통해 한 곳으로 모아두는 것 가능
    - 소스 데이터가 변경될 수 있는 경우 여러 함수를 클래스로 묶기 사용이 적절 (Combine Functions into Class)
    - 소스 데이터가 변경되지 않는 경우에는 두가지 방법 모두 사용 가능 하나 변환 함수를 사용해서 불변 데이터의 필드로 생성해 두고 재사용하는 것도 가능
    - 중복 수식 제거
  - 참조를 값으로 변경 (Change Reference to Value)
- 뒤엉킨 변경 (Divergent Change)
  - 응집도는 높아야 하고 결합도는 낮아야 좋은 코드
  - 서로 다른 문제는 서로 다른 모듈에서 해결해야 함
  - 하나의 클래스를 계속 수정해야 되는 상황
  - 단계 쪼개기 (Split Phase) / 함수 옮기기 (Move Function) / 함수 추출하기 (Extract Function) / 클래스 추출하기 (Extract Class)
  - 단계 쪼개기 (Split Phase)
    - 서로 다른 일을 하는 코드를 각기 다른 모듈로 분리
    - 단계 구분 (전처리 - 주요 작업 - 후처리)
    - 중간 데이터를 만들어 단계를 구분하고 매개변수를 줄이는데 활용 가능
  - 함수 옮기기 (Move Function)
    - 해당 함수가 다른 클래스에 있는 데이터 필드를 더 많이 참조하는 경우 / 해당 함수를 다른 클라이언트(클래스)에서도 필요로 하는 경우 사용
    - 여러 함수를 클래스로 묶기 (Combine Functions into Class) / 클래스 추출하기 (Extract Class) 사용
    - 함수를 옮기게 되면 기존에 사용하던 변수들은 매개변수로 받아야 함.
    - 순환 참조는 피하는 방향 권장
  - 클래스 추출하기 (Extract Class)
    - 클래스가 다루는 책임이 많아질수록 클래스 사이즈가 커짐
    - 쪼개는 기준
      - 데이터나 메소드 중 일부가 매우 밀접한 관련이 있는 경우
      - 일부 데이터가 대부분 같이 바뀌는 경우
      - 데이터 또는 메소드 중 일부를 삭제한다면 어떻게 되는가?
    - 하위 클래스를 만들어 책임을 분산 시키는 것도 가능
    - 사람 정보와 사무실 정보가 같이 있는 경우 사무실 정보에 대한 클래스를 따로 생성하고 사람 정보 클래스에서는 생성자를 통해 사무실 정보 객체를 받아와서 설정
- 산탄총 수술 (Shotgun Surgery)
  - 하나의 일로 여러 곳을 손봐야 하는 문제
  - 함수 옮기기 / 필드 옮기기 / 여러 함수를 클래스로 묶기 / 단계 쪼개기 / 함수 인라인 / 클래스 인라인
  - 필드 옮기기 (Move Field)
    - 어떤 데이터를 항상 어떤 레코드와 함께 전달하는 경우
    - 어떤 레코드 변경 시 다른 레코드에 있는 필드를 변경해야 하는 경우
    - 여러 레코드에 동일한 필드를 수정해야 하는 경우
  - 함수 인라인 (Inline Function)
    - 함수 추출하기와 반대되는 리팩토링
      - 함수로 추출하여 함수 이름으로 의도를 표현하는 방법
    - 함수 본문이 함수 이름 만큼 또는 더 의도를 잘 표현하는 경우 존재
    - 리팩토링 실패 시 여러 함수를 인라인 시킨 다음 다시 함수 추출하기 진행 시도 가능
    - 우회형 (Indirection) 메소드라면 인라인으로 없애는 것 가능
  - 클래스 인라인 (Inline Class)
    - 클래스 추출하기의 반대
    - 두 클래스의 코드를 한곳으로 모으고 그 다음에 클래스 추출하기를 다시 적용해서 새롭게 리팩토링 적용 가능
    - 필드를 옮기고 클래스 내 멤버를 인자로 받는 생성자를 정의하고 나서 메소드를 가져오는 방향으로 리팩토링 진행
- 기능 편애 (Feature Envy, 기능 욕심)
  - 어떤 모듈 내 함수가 다른 모듈에 있는 데이터나 함수를 더 많이 참조하는 경우 발생
    - 다른 객체의 getter를 여러개 사용하는 메소드
  - 함수 옮기기 / 함수 추출하기
  - 데이터와 해당 데이터를 참조하는 행동을 같은 곳에 두도록 함
  - 데이터와 행동을 분리한 전략 / 방문자 패턴 적용을 할 수도 있음
- 데이터 뭉치 (Data Clumps)
  - 여러 클래스에 존재하는 비슷한 필드 목록
  - 여러 함수에 전달하는 매개변수 목록
  - 클래스 추출하기 / 매개변수 객체 만들기 / 객체 통째로 넘기기 (Preserve Whole Object)
  - 