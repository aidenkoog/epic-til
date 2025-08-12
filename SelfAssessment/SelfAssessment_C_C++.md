# C, C++

- C언어, C++ 관련 내용을 정리합니다

## C언어 프로그램 실행

- 맥북(macOS)에서 C 코드 실행
  - C 컴파일러 설치 확인
  - clang 설치여부 확인
    - clang --version
  - 미설치 시 Xcode Command Line Tools 설치
    - xcode-select --install
  - 컴파일
    - clang hello.c -o hello
  - 실행
    - ./hello

- 리눅스(서버 PC)에서 C 코드 실행
  - 참고: ARM 기반이라면 크로스 컴파일이 필요
  - C 컴파일러 설치
    - gcc가 기본적으로 설치되어 있을 가능성
    - 미설치 시 아래와 같이 설치 진행
      - sudo apt update && sudo apt install gcc (Ubuntu 계열)
      - sudo yum install gcc (CentOS 계열)
    - 설치 여부 확인
      - gcc --version
    - 내 PC에서 서버PC로 파일 복사
      - scp hello.c user@server-pc-ip:/home/user/
    - 컴파일 및 실행
      - gcc hello.c -o hello
      - ./hello

- 맥북에서 컴파일한 실행 파일을 리눅스에서 실행하는 방법
  - 맥북과 리눅스는 운영체제가 다르기 때문에, 맥북에서 빌드한 실행 파일을 그대로 리눅스에서 실행 불가능
    - 방법 1: 서버 PC에서 직접 컴파일
    - 방법 2: 리눅스용 실행 파일을 크로스 컴파일
  - 맥북에서 크로스 컴파일을 위해 설치 필요 항목
    - gcc-arm-linux-gnueabi 또는 gcc-aarch64-linux-gnu 같은 크로스 컴파일러
      - brew install x86_64-elf-gcc (x86_64 리눅스용 실행 파일 빌드)
      - brew install aarch64-linux-gnu-gcc (ARM 리눅스용 실행 파일 빌드)
  - 컴파일
    - aarch64-linux-gnu-gcc hello.c -o hello_arm
  - 서버 PC로 전송
    - 이렇게 생성한 실행 파일(hello_arm)을 scp로 서버PC에 복사하고 실행
  - 참고: PC가 어떤 CPU 아키텍쳐인지 확인하는 방법
    - uname -m 명령어를 실행하면 아키텍처를 알 수 있음

- 다이아몬드 상속 (Diamond Inheritance)
  - 다이아몬드 상속(diamond inheritance)은 한 공통 기저 클래스(Base)를 두 개의 중간 파생 클래스(B, C)가 상속하고, 최종 클래스(D)가 B와 C를 동시에 상속할 때 생기는 구조

  - 형태가 다이아몬드

  - 핵심 이슈는 두 가지
    - 중복 서브오브젝트: Base가 D 안에 두 번 들어올 수 있음
    - 모호성: 어떤 경로의 Base 멤버를 쓰는지 애매해짐

  - 가상 상속 없이 사용 케이스 (문제 발생 예시)
    ```cpp
    #include <iostream>
    struct Base {
        void hello() const { std::cout << "Base::hello\n"; }
        int x = 0;
    };

    struct B : /* 가상 아님 */ Base {
        void setFromB() { x = 1; }
    };

    struct C : /* 가상 아님 */ Base {
        void setFromC() { x = 2; }
    };

    struct D : B, C {
        void f() {
            // hello();        // 모호성 오류: B::Base인지 C::Base인지?
            B::hello();        // 경로를 명시해야 함
            C::hello();

            // x = 3;          // 역시 모호: B::Base::x ? C::Base::x ?
            B::x = 3;          // 서로 다른 Base가 두 개 존재
            C::x = 4;
        }
    };
    ```
    - D 안에 Base가 두 개 생김(B 경로의 Base, C 경로의 Base)
    - 그래서 hello()/x 접근이 모호해짐

  - 가상 상속 (virtual inhetitance)으로 해결
    - B와 C가 virtual public base로 상속하면, D안에 단 한나의 Base만 존재
    - 예시
      ```cpp
      #include <iostream>
      struct Base {
          Base(int v = 0) : x(v) { std::cout << "Base()\n"; }
          void hello() const { std::cout << "Base::hello, x=" << x << "\n"; }
          int x;
      };

      struct B : virtual public Base {
          void setFromB() { x = 1; }
      };

      struct C : virtual public Base {
          void setFromC() { x = 2; }
      };

      struct D : public B, public C {
          D() : Base(42) {             // ★ 가상 기저(Base)는 '가장 바깥(최종)'에서만 초기화
              std::cout << "D()\n";
          }
          void f() {
              hello();                  // 모호성 없음: 단 하나의 Base
              x = 100;                  // 역시 단일 Base에 접근
              setFromB();
              setFromC();
              hello();                  // 값 변화 확인
          }
      };

      int main() {
          D d;
          d.f();
      }
      ```
    - 가상 상속의 특징/주의점
      - 단일 Base 공유: D에는 Base가 하나만 존재 → 모호성 해소.
      - 초기화 규칙: 가상 기저 클래스는 항상 가장 최종 클래스(D) 생성자 이니셜라이저에서 초기화해야 함 (B나 C 생성자에서 Base(...) 해도 무시됨)
      - 오버헤드: 구현상 가상 기저 포인터(vbptr) 등이 추가되어 객체 크기/간접 접근 비용이 늘 수 있음 (대부분 미미하지만 구조가 복잡하면 체감될 수 있음)
      - 언제 쓰나: “진짜로 ‘하나의 베이스 정체성’을 공유해야 할 때”만. 많은 경우 합성(Composition), 인터페이스성 기저(순수 가상) + 합성을 권장.

  - 자바(Java)에서의 대응/차이
    - 자바는 클래스 다중 상속 금지
      - 클래스 다중 상속 자체 불가능 > 다이아몬드 문제 근본 원인 회피
      - 대신 인터페이스 다중 상속 지원

    - 인터페이스 default method의 다이아몬드와 해결 규칙
      - 자바 8부터 인터페이스에 default 메서드가 탄생하였기 때문에 형식상 다이아몬드가 생길 수 있음
      - 이때 충돌 해결 규칙이 명확히 정의되어 있음
        ```java
        interface A {
          default void hello() { System.out.println("A.hello"); }
        }
        interface B extends A {
          default void hello() { System.out.println("B.hello"); }
        }
        interface C extends A {
          default void hello() { System.out.println("C.hello"); }
        }

        class D implements B, C {
          @Override
          public void hello() {
              // 충돌 해결: 어느 경로의 default를 쓸지 명시
              B.super.hello();  // 혹은 C.super.hello();
              // 또는 자체 구현으로 완전히 덮어쓰기
          }
        }
        ```
    - 규칙 요약
      - 클래스의 메서드가 인터페이스 default보다 우선.

      - 다수 인터페이스의 동일 시그니처 default가 충돌하면 구현 클래스에서 반드시 오버라이드해 선택/재정의.

      - 즉, Java는 설계 상 모호성을 ‘컴파일 타임에’ 강제 해결하게 만들었고, C++은 언어 차원에서 가상 상속이라는 메커니즘을 제공해 런타임 표현(단일 Base 서브오브젝트)을 보장하도록 설계

  - 추가 정보 / 팁
    - C++
      - 단순 재사용/확장은 다중 상속보다 합성을 우선 고려
        - 참고: 합성(Composition)은 상속받지 않고 필요한 객체를 멤버 변수로 포함해서 기능을 재사용하는 방식
      - 정말 하나의 Base 정체성을 공유해야 할 때만 virtual 상속.
      - 가상 기저 초기화는 최종 클래스에서만 가능 → 생성자 설계에 주의.
      - 모호성은 정규화된 이름(B::Base::foo)로도 풀 수 있지만, 근본 해결은 가상 상속.

    - Java
      - 다형성 조합은 인터페이스로, 상태/구현 공유는 합성.
      - default 충돌 시 구현 클래스에서 의도를 명시적으로 작성(X.super.m() 혹은 완전 재정의).