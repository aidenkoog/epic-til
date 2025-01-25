#### OOP 설명

- Object-Oriented Programming
- 객체 지향 프로그래밍
- 객체의 관점에서 프로그래밍 하는 것
- 객체들의 유기적인 관계를 통해서 프로세스가 진행
- 애플리케이션을 구성하는 요소들을 객체로 바라보고 객체들을 유기적으로 연결하여 프로그래밍하는 것
- 사물(개체)를 코드로 모델링하여 프로그램을 작성하는 방식
- 다양한 부품을 조합하여 하나의 완성 프로그램을 조립하는 것으로 비유 가능
- 재사용성 높음
- 절차 지향 방식에 비해 실행 속도가 느림
- 실제 세계의 사물들을 객체로 모델링하여 개발을 진행하는 프로그래밍 기법
- 가장 대표적인 언어로 Java가 있음
- 캡슐화, 상속, 다형성 등과 같은 기법을 이용 가능. 다형성은 동일한 키보드의 키가 다른 역할을 하는 것처럼 하나의 메소드나 클래스가 다양한 방법으로 동작하는 것을 의미

#### OOP 특징 설명

- 캡슐화 (Encapsulation): 각 객체의 독립적 기능
  - Don't ask (ex. obj.getXXStatus() == 2)
  - 디미터(데미테르)의 법칙 (여러 개 도트 사용 금지)
  - 여러 개의 도트를 사용하는 stream API의 경우는 위배가 아님
    - 같은 stream 객체를 반환하므로. 만약 각각의 도트 지점마다 다른 객체를 반환하고 이를 사용한다면 위배하는 것임을 의미 
- 추상화 (Abstraction): 공통적인 속성, 메소드 정의, 복잡한 부분은 감추고 공통된 주요 부분으로 일반화하는 것 => 시스템은 확장 가능한 구조가 됨
- 다형성 (Polymorphism): 다르게 동작하는 함수를 동일한 함수명으로 호출 가능
  - 오버라이딩: 같은 이름 / 매개변수
  - 오버로딩: 같은 이름 / 매개변수 다름
- 상속성, 재사용 (Inheritance): 코드 재사용성, 생산성 높임

#### 절차 지향 프로그래밍 설명

- 위에서 차례대로 순서에 맞게 코드 작성하고 실행하는 것
- 일반적인 컴퓨터 처리 방식, 처리 구조와 유사하므로 통상적으로 객체 지향 방식보다 빠름
- 추상성 낮은 편
- 물이 위에서 아래로 흐르는 것처럼 순차적인 처리를 중요시하는 프로그래밍 기법
- 가장 대표적인 언어로 C언어가 있음
- 코드의 순서가 바뀌면 동일한 결과를 보장하기 어렵다.

#### 클래스 설명

- 객체 지향 프로그래밍에서 특정 객체 생성하기 위해 정의하는 일종의 틀
- 변수와 함수 정의 가능
- 비슷한 성격을 가진 연관있는 변수와 함수들을 한 클래스에 정의