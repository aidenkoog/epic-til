# Design Pattern

정리될 내용들은 아래와 같습니다.

- 개념 / 용어 정의, 사용 이유


#### 디자인 패턴 (Design Pattern) 개념

- 배경
  - 소프트웨어를 재사용 가능하고 유연, 확장성있고 유지보수가 용이하게 만드는 것은 어려운 일
  - 패턴 없는 개발 후 유지보수 비용이 더 들게되는 상황 발생
  - 기술, 창의성 등도 중요하나 경험이 가장 중요하다는 관점
- 개념
  - 소프트웨어 공학의 소프트웨어 설계에서 공통으로 발생하는 문제에 대해 자주 쓰이는 설계 방법을 정리한 패턴
  - 개발 효율성, 유지보수성 그리고 운용성이 높아지고 프로그램 최적화에 도움

#### 디자인 패턴 유형 설명

- 목적
  - 생성: 객체 인스턴스 생성하는 패턴
    - 클래스
      - Factory Method
        - 입력되는 인자에 따라 다른 인스턴스 생성
        - 생성한 인스턴스 관리까지 하고자 한다면 팩토리 클래스 내부에 HashMap으로 관리 가능
    - 오브젝트
      - Absract Factory
      - Builder
        - 인스턴스 생성 시 필요한 인자가 많은 경우
        - 설정되는 인자에 따라 다른 스타일의 인스턴스 생성 가능
        - 다이얼로그 팩토리가 그 예
      - Prototype
        - 자바 clone() 메소드가 대표적인 예
          - 참고: 일반적으로 clone()은 얕은 복사, 내부적으로 참조하고 있는 인스턴스는 인스턴스가 복제되는것이 아니라 그 주소가 복제되므로 만약 복제한 인스턴스로 값을 변경할 경우 기본 인스턴스의 값도 변경됨
          - 따라서 깊은 복사를 하려면 clone 메소드를 오버라이딩한 후 따로 복사해주는 루틴 작성 필요
      - Singleton
  - 구조: 클래스와 객체를 더 큰 구조로 만들 수 있게 구성을 사용하는 패턴
    - 클래스
      - Adapter (class)
        - 구성 요소: 타겟 (클라이언트가 직접적으로 호출하는 인터페이스), 어댑티, 어댑터, 클라이언트
        - 정의 재정리
          - 호환되지 않는 인터페이스를 연결하는 패턴
          - 기존클래스(어댑티)를 수정하지 않고도 특정 인터페이스를 필요로 하는 코드에서 사용할 수 있게 해줌
          - 클래스의 인터페이스를 다른 인터페이스로 변환 가능
          - 서로 다른 인터페이스를 가진 클래스들이 상호 작용할 수 있도록 해서 코드의 재사용량을 증가
        - 사용 예
          - Adaptee: run() 존재
          - Adapter: void execute() { adaptee.run() }
          - new Adapter(new Adaptee()).execute()
    - 오브젝트
      - Adapter (object)
      - Bridge
        - 개념과 기능 구현부의 분리
        - 분리하지 않으면 상속구조가 복잡해지므로 필요한 패턴
      - Decorator
        - Java의 IO 관련 클래스들이 대표적 예 (BufferedReader etc)
        - 기능 확장이 필요할 때 서브 클래싱 대신 사용할 수 있는 대안
        - 객체의 결합 을 통해 기능을 동적으로 유연하게 확장 할 수 있게 해주는 패턴
        - 즉, 기본 기능에 추가할 수 있는 기능의 종류가 많은 경우에 각 추가 기능을 Decorator 클래스로 정의 한 후 필요한 Decorator 객체를 조합함으로써 추가 기능의 조합을 설계 하는 방식
          - new Dec1(new Dec2(new Dec3(component)))
      - Facade
      - Flyweight
        - 실행시에 객체 인스턴스의 개수를 줄여서 메모리를 절약할 수 있습니다
        - 여러 "가상" 객체의 상태를 한 곳에 집중시켜놓을 수 있습니다.
        - 즉 어떤 클래스의 인스턴스가 아주 많이 필요하지만 모두 똑같은 방식으로 제어할 수 있는 경우에 유용하게 사용됩니다,
        - 특정 인스턴스만 다른 인스턴스처럼 동작하도록 하는 것이 불가능
        - 객체의 값을 변경하면 공유받은 "가상" 객체를 사용하는 곳에 영향을 줄 수 있습니다.
      - Proxy
      - Composite
        - 클라이언트가 복합 객체(group of object) 나 단일 객체를 동일하게 취급하는 것을 목적
        - 의도는 트리 구조로 작성하여, 전체-부분(whole-part) 관계를 표현하는 것
        - 복합 객체와 단일 객체의 처리 방법이 다르지 않을 경우, 전체-부분 관계로 정의 가능.
        - 전체-부분 관계의 대표적인 예는 Directory-File 이 대표적.
        - 전체-부분 관계 정의
          - 전체-부분 관계를 트리 구조로 표현하고 싶을 경우.
          - 전체-부분 관계를 클라이언트에서 부분, 관계 객체를 균일하게 처리하고 싶을 경우.
  - 행위: 클래스와 객체들이 상호작용하는 방법과 역할을 분담하는 방법을 다루는 패턴
    - 클래스
      - Interpreter
      - Template Method
        - 하위 클래스에 구현부를 위임
        - abstract가 아닌 일반 함수를 즉 바디가 있는 함수를 abstract 에 선언하는 것을 훅 오퍼레이션
    - 오브젝트
      - Chain of Responsibility
      - Command
        - 특정 기능 / 요청들을 캡슐화 시키는 패턴
      - Iterator
      - Mediator
      - Memento
      - Observer
      - State
      - Strategy
        - 정책이나 알고리즘 교체시 주로 사용
        - 부모 클래스에서 Strategy 인스턴스를 가지고 있으며 이를 설정하기 위한 setter 필요
        - 따라서 실제로 나의 클래스에서 사용 시 xxxStrategy.run() 이런 식으로 구현이 되어야 함
          - public void run() { xxxStrategy.run() }
      - Visitor
- 범위
  - 클래스
  - 객체

#### 디자인 패턴 적용의 필요성

- 규칙은 아니나 재사용성, 유연성, 확장성, 모듈화 작업을 향상
- 소프트웨어 개발 자체 커뮤니케이션에 도움
- 높은 결합도나 종속적으로 구현된 소프트웨어의 리팩토링을 가능하게 함
  - 잘못 설계된 소프트웨어 개선 작업에 도움
- 좋은 설계를 유도하며 유지보수에 들어가는 비용 절약 가능

#### Observer 패턴 설명

- 어떤 이벤트가 일어나는 것을 감시하여 특정 이벤트 발생 시 어떠한 동작을 즉각 수행하게 해줌
- 다른 객체의 상태 변화를 별도의 함수 호출 없이 즉각적으로 알 수 있어 효율적인 프로그래밍 가능

#### 객체지향 프로그래밍과 객체지향 설계

- 추상화
  - 처리과정 / 데이터 구조, 표현 방법 추상화
  - 속성 또는 기능 추출하는 작업
- 캡슐화
  - information hiding
  - 단순한 접근을 제공하여 오류가 생길 부분을 감소
  - 클라이언트 코드가 세부적인 사항을 알 필요 없음
- 상속성
  - 일반적인 객체와 구체적인 개념의 객체 관계 표현 (General <-> Specific)
  - 상위 클래스의 타입을 내포
  - 단순 코드의 재사용 목적이 아님
  - 상위 클래스의 속성과 기능을 하위 클래스에서 사용 또는 재정의 가능
- 다형성 (polymorphism)
  - 같은 메세지, 구현에 대해 각 객체가 다른 표현과 결과를 나타내는 것
  - 클래스의 상속, 인터페이스의 구현 시 각각의 다른 구현을 가진 클래스들이 상위 타입으로 업캐스팅
  - 오버라이딩한 메소드가 존재할 시 같은 상위 타입으로 선언된다 하더라도 각기 다른 인스턴스의 메소드가 호출되는 것
  - 예. 인터페이스 타입의 변수에 그 인터페이스를 구현한 클래스를 대입하는 것
  - 자바의 경우 모든 메소드가 가상함수 기반으로 구현되므로 하위 클래스에 재정의된 메소드가 있는 경우 그 메소드가 호출됨
    - C++의 경우 virtual function 만이 재정의된 함수가 호출
- 객체 지향 설계
  - Design Heuristics
    - (참고) Heuristic: 경험에 기반하여 어떤 문제를 해결, 학습 또는 발견해내는 방법
    - 추상 클래스, 구체 클래스
    - 클래스 상속 또는 합성
    - 인터페이스 상속, 구현체 상속
- 응집도
  - 하나의 모듈, 객체 내부의 요소들 간의 연관성
  - 하나의 책임을 구현하는 하나의 객체는 높은 응집도
- 결합도
  - 객체 상호 간의 연관 관계
  - 결합도가 높으면 하나의 객체를 수정할 때 다른 객체도 수정 필요

#### OOP의 5가지 설계 원칙 설명 (SOLID)

- SRP(Single Responsibility Principle, 단일 책임 원칙)
  - 클래스는 단 하나의 목적을 가져야 하며, 클래스를 변경하는 이유는 단 하나의 이유여야 함
  - 한 클래스에서 여러 기능을 제공하게 되면 유지보수가 어려움
- OCP(Open-Closed Principle, 개방 폐쇠 원칙)
  - 클래스는 확장에는 열려 있고, 변경에는 닫혀 있어야 함
  - 객체 자신의 수정에 대해서는 유연하고, 다른 클래스가 수정될 때는 영향을 받지 않음
  - 인터페이스나 추상 클래스를 통해 접근하도록 유도
  - 예) 자바 JDBC, I/O Stream
    - 여러 종류의 DB 가 있다고 가정 => JDBC에는 인터페이스가 정의되어 있음 => 그 인터페이스들에 대한 구현을 각각의 회사의 데이터베이스 로직에서 구현을 함
    - Client DAO 단만 수정하면 됨 (Client DAO ==> JDBC ==> Database)
    - I/O Stream 예: InputStream ==> File / Network / Etc
- LSP(Liskov Substitution Principle, 리스코프 치환 원칙)
  - 상위 타입의 객체를 하위 타입으로 바꾸어도 프로그램은 일관되게 동작해야 함
  - 하위 클래스는 항상 상위 클래스로 교체될 수 있어야 함
    - 하위 클래스는 오버라이드든 오버로딩의 형태든 모든 정보를 가질 수 있어야 함.
  - 즉, 상위 클래스에 제공되는 여러 기능은 하위 클래스가 모두 사용가능 해야 함
  - IS-A 관계 (is a kind of 관계)
- ISP(Interface Segregation Principle, 인터페이스 분리 원칙)
  - 클라이언트는 이용하지 않는 메소드에 의존하지 않도록 인터페이스를 분리해야 함
  - 제공하는 기능에 대한 인터페이스에만 종속적이어야 함
  - 하나의 객체가 여러 기능을 제공할 수 밖에 없다면 (단일 책임 원칙에 위배되는 상황) 클라이언트가 사용할 수 있는 여러 인터페이스로 분리하여 제공하면 클라이언트가 사용하지 않는 기능에 종속적이지 않을 수 있음
  - (예) I-a, I-b, I-c <-- A class 구조일 때 I-a 의 기능을 사용하고 싶으면 I-a obj = new A(); 의 형태로 필요한 인터페이스만 사용 가능
- DIP(Dependency Inversion Principle, 의존 역전 법칙)
  - 클라이언트는 추상화(인터페이스)에 의존해야 하며, 구체화(구현된 클래스)에 의존해선 안됨.
  - 의존 관계는 구체적인 것 보다는 추상적인 것에 의존 (추상클래스 또는 인터페이스로 의존해야 함)
  - 구체적인 것은 이미 구현이 되어 있고 변하기 쉬운 것
  - 추상적인 것은 인터페이스나 추상 클래스 (상위 클래스)

#### UML

- Unified Modeling Language
- 프로그램 설계를 표현하기 위해 사용하는 표기법
- 소프트웨어 시스템, 업무 모델링, 시스템의 산출물을 규정하고 시각화, 문서화하는 언어
- 기호와 도식 이용한 표현
- 모델링 언어
- 객체 지향 시스템을 가시화, 명세화, 문서화하기 위한 목적

#### UML 종류 설명

- UseCase
  - 요구 분석 과정에서 시스템과 외부와의 상호 작용 묘사
- Activity
  - 업무의 흐름을 모델링 / 객체 생명 주기 표현
- Sequence
  - 객체 간 메세지 전달을 시간적 흐름에서 분석
- Collaboration
  - 객체와 객체가 주고받는 메세지 중심으로 작성
- Class
  - 시스템 구조적인 모습
- Component
  - 소프트웨어 구조
- Deployment
  - 기업 환경 구성과 컴포넌트들 간의 관계

#### 클래스 다이어그램 관련 내용

- 이탤릭체 : 추상 / 인터페이스
- 다이아몬드: 변수나 매개변수로 객체를 가지고 있음을 의미
- 연관 관계 Association
  - 양방향 연관관계는 직선, 단방향은 화살표로 표시
  - 연관 개체 수 표현도 가능
- 집합 관계 Composition, Aggregation
  - 집약 관계
    - 멤버 변수로 선언이 되어 있고 초기화가 매개 변수로 전달되어 생성되는 형태
    - 빈 마름모로 표시
  - 합성 관계
    - 주로 멤버 변수로 선언하여 사용
    - 생성자에서 부분 객체를 생성
    - 채워진 마름모로 표시
    - 전체 객체의 라이프 타임에 부분 객체가 종속 (전체 객체가 소멸되면 부분 객체도 소멸)
- 의존 관계 Dependency
  - 연관과 유사하나 짧은 라이프 타임
  - 참조 변수가 매개 변수나 지역 변수로 구현
  - 점선 화살표로 표시
- 일반화 관계 Generalization
  - 상속 표현
  - 빈 화살표와 실선으로 표현
- 실체화 관계 Realization
  - 기능이 선언된 인터페이스를 구현하는 클래스는 선언된 기능을 구현할 책임이 있음
  - 여러 클래스가 하나의 인터페이스를 구현함으로써 다형성을 제공
  - 빈 화살표와 점선으로 표시
- 접근 제어자
  - public: +
  - protected: \*
  - default: ~
  - private: -
