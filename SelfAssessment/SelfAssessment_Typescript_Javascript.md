# Self-Assessment Vue.js

This page summarizes the main concepts, features, pros and cons of Javascript and Typescript.

## Javascript, Typescript

- 브라우저에서 JavaScript 코드가 실행되는 과정 설명
  - 브라우저의 주요 구성 요소
    - JavaScript가 실행되는 환경은 브라우저
    - 주요 구성 요소
	  - HTML 파서: HTML을 읽고 DOM(Document Object Model) 생성
	  - CSS 파서: CSS를 읽고 스타일 규칙을 생성
	  - JavaScript 엔진: JavaScript 코드 실행 (예: Chrome의 V8, Firefox의 SpiderMonkey)
	  - 렌더링 엔진: 화면을 그리는 역할 (예: Blink, WebKit)
	  - 네트워크 모듈: 서버에서 리소스를 다운로드

    - 브라우저의 JavaScript 실행 과정
      - HTML 문서 로드 및 파싱
	    - 브라우저는 먼저 HTML 문서를 다운로드하고, 위에서부터 차례로 분석(파싱)하여 DOM을 생성
	    - HTML 내 <script> 태그를 만나면 JavaScript 코드 실행을 위해 파싱을 멈춤(동기 실행)
        - "<script src="app.js">" 처럼 외부 파일을 불러오면 네트워크 요청이 발생하며, 다운로드가 완료될 때까지 HTML 파싱이 멈출 수 있음.
	      - 해결 방법: <script async> 또는 <script defer> 속성을 사용.
	        - async: HTML 파싱과 병렬로 다운로드, 다운로드 완료 즉시 실행.
	        - defer: HTML 파싱이 끝난 후 실행

      - JavaScript 엔진이 코드 실행
        - 브라우저는 JavaScript 엔진을 사용하여 코드를 실행
        - 대표적인 JavaScript 엔진
	      - Chrome: V8 엔진
	      - Firefox: SpiderMonkey
	      - Edge: Chakra
	      - Safari: JavaScriptCore

        - JavaScript 엔진의 실행 과정
          - 파싱 (Parsing)
	        - JavaScript 코드를 토큰(token) 단위로 분석하여 AST(Abstract Syntax Tree, 추상 구문 트리) 생성
          - 컴파일 (Compilation, JIT Compilation)
	        - JavaScript 엔진은 인터프리터 + JIT(Just-In-Time) 컴파일러를 사용
              - JIT: 실행과정에서 컴파일하기 위해, 실행하는 시점에서 필요한 부분을 컴파일하는 방식
	        - 코드를 한 줄씩 실행하는 것이 아니라, 최적화된 바이트코드로 변환하여 실행 속도 개선
          - 실행 (Execution)
	        - JavaScript 코드는 콜 스택(Call Stack)과 힙(Heap) 메모리에서 실행

      - 실행 컨텍스트 생성 및 콜 스택 관리
        - JavaScript 엔진이 코드를 실행할 때 실행 컨텍스트(Execution Context) 를 생성하고 콜 스택(Call Stack) 에 저장하면서 실행
          - 콜 스택은 LIFO(Last In, First Out) 방식으로 동작
        - 실행 컨텍스트
          - 실행 컨텍스트에는 변수, 함수, this 객체 등이 포함
        - 코드 실행 과정
          - global execution context (전역 실행 컨텍스트) 생성
          - xxx() 함수 실행 → 새로운 실행 컨텍스트 생성 → 콜 스택에 추가
          - 내부 코드 실행 후 xxx() 컨텍스트가 제거

      - 비동기 코드 실행 (이벤트 루프와 콜백 큐)
        - JavaScript는 싱글 스레드(single-threaded) 기반
        - 비동기 처리를 위해 이벤트 루프(Event Loop) 와 콜백 큐(Callback Queue) 를 사용

      - DOM 업데이트 및 렌더링
        - JavaScript 실행이 끝나면 브라우저는 렌더링 엔진을 통해 화면을 다시 그림 (Repaint & Reflow).
	    - 비효율적인 DOM 조작이 많으면 성능 저하 발생
        
- 이벤트 루프(Event Loop)가 렌더링과 관련된 최적화 기법과의 관계
    - 이벤트 루프(Event Loop)
        - JavaScript의 비동기 처리를 담당하는 메커니즘으로, 단일 스레드 환경에서 비동기 작업을 효율적으로 처리하는 방식
        - JavaScript는 싱글 스레드(Single Thread) 기반이므로, 이벤트 루프를 통해 비동기 작업(렌더링, I/O, 타이머 등)을 관리하며 UI를 원활하게 업데이트
        - 주요 역할:
	        - 콜백 큐(Callback Queue)에서 태스크를 하나씩 가져와 실행
	        - 렌더링과 동시성 작업을 최적화하여 성능을 향상

    - 이벤트 루프의 동작 과정
        - (1) Call Stack(콜 스택)
	        - JavaScript 코드가 실행될 때 호출되는 함수가 쌓이는 스택(Stack)
	        - 함수 실행이 끝나면 스택에서 제거(Pop)

        - (2) Web APIs (비동기 작업 처리)
	        - setTimeout, DOM 이벤트, AJAX 요청 등 비동기 작업은 Web API를 통해 처리
	        - 완료된 작업은 콜백 큐(Callback Queue) 또는 마이크로태스크 큐(Microtask Queue)에 추가

        - (3) Task Queue (콜백 큐 & 마이크로태스크 큐)
	        - 마이크로태스크 큐 (Microtask Queue): Promise.then(), MutationObserver 등이 들어감.
	        - 콜백 큐 (Callback Queue): setTimeout(), setInterval(), event listeners 등이 들어감.

        - (4) Rendering (렌더링)
	        - 이벤트 루프는 각 주기(Tick)마다 태스크 실행 후 렌더링을 수행.
	        - 프레임 단위로 UI를 업데이트하며, 성능을 유지하기 위해 16.6ms(60FPS 기준) 이내에 처리.

    - 이벤트 루프와 렌더링 최적화
        - (1) requestAnimationFrame()을 사용한 부드러운 애니메이션
	        - setTimeout()이나 setInterval()은 고정된 시간 간격으로 실행되며, 화면 리프레시 속도와 동기화되지 않음.
	        - 브라우저는 60FPS 기준으로 16.6ms마다 화면을 업데이트하는데, requestAnimationFrame()을 사용하면 브라우저의 렌더링 주기에 맞춰 실행됨.
            - 예제: setTimeout() vs requestAnimationFrame()
            - 렌더링 최적화 효과
	            - FPS(Frame Per Second)와 동기화되어 CPU 부하 최소화
	            - 성능이 저하될 경우 프레임 조절이 가능하여 화면 끊김 방지
            
        - (2) 비동기 작업을 setTimeout(0) 대신 Promise.then()으로 처리
	        - 마이크로태스크 큐(Microtask Queue)가 콜백 큐보다 먼저 실행되므로, UI 업데이트 전에 실행이 보장됨.
            - 예제: setTimeout(0) vs Promise.then()
            - 렌더링 최적화 효과
	            - Promise는 마이크로태스크 큐에서 즉시 실행되므로 UI 업데이트 전에 작업 가능.
	            - setTimeout(0)은 다음 이벤트 루프에서 실행되므로 UI 업데이트 이후에 실행됨.

        - (3) Heavy Task(무거운 연산) 분할 실행
	        - 무거운 연산이 실행되면 Call Stack이 차단(blocking)되어 UI가 멈출 수 있음
	        - Chunking(작은 작업 단위로 나누어 실행) 또는 Web Worker 사용
            - 예제: Chunking 기법 (setTimeout())
            - 렌더링 최적화 효과
	            - 긴 연산을 여러 개의 작은 청크(chunk)로 나누어 UI가 멈추지 않도록 함
	            - setTimeout(0)으로 이벤트 루프의 다음 Tick에서 실행하여 UI 업데이트 보장

        - (4) Debouncing & Throttling 기법 활용
            - Debouncing (연속 호출 방지)
	            - 사용자의 입력이 멈춘 후 일정 시간 후에 실행
	            - ex. 검색 자동완성, 입력값 검증

            - Throttling (지정된 시간 간격으로 실행)
	            - 일정 시간마다 한 번만 실행됨
	            - ex. 스크롤 이벤트, 리사이즈 이벤트 최적화.

            - 렌더링 최적화 효과
	            - 불필요한 UI 업데이트 방지
	            - 성능 저하 없이 부드러운 애니메이션 & 이벤트 처리 가능.

    - 결론
        ➡ 이벤트 루프를 이해하고 활용하면 웹 애플리케이션의 성능을 향상시키고 부드러운 UI 렌더링을 제공 가능

- JavaScript에서 메모리 누수를 방지하는 방법
    - 메모리 누수
        - 메모리 누수(Memory Leak)는 프로그램이 더 이상 필요하지 않은 메모리를 해제하지 않고 계속 점유하는 상태를 의미
        - JavaScript는 가비지 컬렉션(Garbage Collection, GC)을 자동으로 수행하지만, 특정 패턴에서는 메모리 누수가 발생할 수 있음

    - JavaScript에서 발생하는 주요 메모리 누수 유형 및 방지 방법
        - (1) 글로벌 변수 남용 방지 (var 대신 let 또는 const 사용)
            - 문제점:
	            - var로 선언된 전역 변수는 window 객체에 저장되므로, 명시적으로 해제하지 않으면 메모리에 계속 남아 있음.
                - 해결 방법
	                - let 또는 const를 사용하여 블록 범위 변수로 선언
	                - use strict를 적용하여 암묵적 전역 변수 생성 방지 (function 위 정의)

        - (2) 타이머(setInterval, setTimeout) 정리
            - 문제점:
	            - setInterval()을 사용할 때, 참조하는 객체가 삭제되었음에도 타이머가 계속 실행되면 메모리 누수가 발생
                - 해결 방법
	                - clearInterval()을 사용하여 불필요한 타이머를 제거

        - (3) DOM 요소의 이벤트 리스너 정리
            - 문제점:
	            - 이벤트 리스너가 제거되지 않으면, 관련 객체가 메모리에 계속 유지됨.
            - 해결 방법: removeEventListener()를 사용하여 이벤트 리스너를 제거.

        - (4) 클로저(Closure) 사용 시 참조 정리
            - 문제점:
	            - 클로저 내부에서 외부 변수를 참조할 경우, 해당 변수가 GC(가비지 컬렉션)에서 제거되지 않음
            - 해결 방법
	            - 필요하지 않은 데이터는 null로 할당하여 참조를 해제

        - (5) 객체 간의 순환 참조 방지
            - 문제점:
	            - 객체가 서로를 참조하면 가비지 컬렉터가 이를 수집하지 못하고 메모리 누수가 발생
            - 해결 방법
	            - 객체가 서로를 참조할 경우, WeakMap 또는 WeakRef을 사용하여 가비지 컬렉션이 가능하도록 함

        - (6) WeakMap과 WeakSet을 활용한 메모리 자동 해제
	        - WeakMap과 WeakSet은 가비지 컬렉터가 참조를 자동으로 관리하므로 메모리 누수 방지에 효과적
            - 메모리 최적화 효과:
	            - user = null로 설정하면 GC가 자동으로 WeakMap에서 해당 데이터를 제거

        - (7) 개발자 도구를 활용한 메모리 누수 디버깅
            - Chrome DevTools에서 메모리 누수 분석 가능
	            - Performance 패널: 메모리 사용량이 지속적으로 증가하는지 확인
	            - Memory Snapshot: 객체 할당 상태 분석
	            - Heap Snapshot: 참조가 유지되고 있는 객체 추적

    - 결론
        - JavaScript의 메모리 누수를 예방하려면, 불필요한 참조를 제거하고, 이벤트 리스너 및 타이머를 적절히 정리하는 것이 중요

- 클로져의 핵심 개념
    - 개요
        - 함수 안의 함수
        - 외부 함수의 변수를 기억하고 접근할 수 있는 함수

    - 클로저의 핵심 개념 (함수, 내부함수)
        - 함수 안에 정의된 함수(내부 함수)
        - 외부 함수의 변수에 접근 가능
        - 심지어 외부 함수의 실행이 끝난 후에도 변수를 기억하고 사용 가능
        - 변수를 은닉(캡슐화)하는 효과를 가질 수 있음

    - 예제 1: 기본적인 클로저
        - inner_function은 outer_function의 변수 x를 기억하고 있음 → 클로저
        - 예제 코드
            ```python
            def outer_function(x):
                def inner_function(y):
                    return x + y  # 외부 함수의 변수 x를 사용
                return inner_function  # 내부 함수를 반환

            closure = outer_function(10)  # outer_function 실행 후 inner_function 반환
            print(closure(5))  # 10 + 5 = 15
            ```

    - 예제 2: 클로저가 변수를 기억하는 동작
        - increment()는 counter()의 count 변수를 기억하고 있음 → 클로저
        - 예제 코드
            ```python
            def counter():
                count = 0  # 외부 함수의 변수

                def increment():
                    nonlocal count  # 외부 변수 사용 (nonlocal 키워드 필요)
                    count += 1
                    return count

                return increment  # 내부 함수 반환

            counter1 = counter()  # 새로운 카운터 생성
            print(counter1())  # 1
            print(counter1())  # 2

            counter2 = counter()  # 새로운 카운터 생성
            print(counter2())  # 1  (독립적인 상태 유지)
            ```

    - 결론
        - 클로저는 "함수 안의 함수"일 뿐만 아니라, 외부 함수의 변수를 기억하고 사용하는 함수
        - 내부 함수가 외부 함수의 변수를 포획(Closure) 하여, 외부 함수가 종료되어도 변수를 유지 가능
        - 데이터 은닉과 상태 유지가 가능하여 함수형 프로그래밍과 객체 지향 프로그래밍에서 유용하게 활용됨
        - 외부 함수의 변수를 기억하는 함수 안의 함수

- Javascript/Typescript에서 클로저를 사용한 객체 지향 프로그래밍 예를 보여주세요.
    - 정의: 클로저는 함수가 외부 스코프의 변수에 접근할 수 있게 하는 구조임
    - OOP 방식 사용 예:
        ```ts
        function Counter() {
            let count = 0; // private 변수

            return {
                increment: () => ++count,
                getCount: () => count
            };
        }

        const counter = Counter();
        counter.increment(); // 1
        counter.getCount();  // 1
        ```
        - 특징: count는 외부에서 접근 불가, 내부 함수에서만 접근 → 은닉성 구현

- Immutable 데이터 패턴 사용 시 이점
    - 정의: 데이터 변경 없이 복사본을 생성하여 새로운 상태를 만드는 방식
    - 이점:
        - 상태 추적과 디버깅이 쉬움
        - 예측 가능한 상태 관리 (Redux 등에서 유리)
        - 사이드 이펙트 감소 → 안정성 향상
        - React의 shouldComponentUpdate 최적화에 유리

- 프론트엔드 성능 최적화를 위해 JavaScript에서 할 수 있는 것들
    - 주요 방법들:
        - 이벤트 디바운싱/스로틀링 사용
        - 불필요한 DOM 조작 최소화
        - Lazy loading, 코드 스플리팅
        - Web Worker로 연산 분산
        - 메모리 누수 방지 및 클로저 주의
        - requestAnimationFrame 활용 (애니메이션 시)

- TypeScript의 제네릭(Generic)을 사용 시 장점
    - 정의: 제네릭은 타입을 함수나 클래스에 매개변수처럼 넘길 수 있게 해주는 기능
    - 장점:
        - 코드 재사용성 증가: 여러 타입에 대해 하나의 함수/클래스 정의
        - 타입 안정성 유지: 타입이 고정되지 않으면서도 타입 체크 가능
        - 자동 타입 추론 가능: 호출 시 인자에 따라 자동으로 타입 추론
    - 예시
        ```ts
        function identity<T>(value: T): T {
            return value;
        }

        identity<string>('hello');  // 타입 명시
        identity(123);              // 타입 추론
        ```
        - 한줄 요약: 제네릭은 유연하면서도 타입 안정성을 유지할 수 있게 해줌

- TypeScript의 strict 옵션을 활성화 시 이점
    - 정의: strict는 타입스크립트의 모든 엄격한 타입 검사 기능을 켜는 플래그임
    - 이점:
        - null/undefined에 대한 엄격한 검사 (strictNullChecks)
        - 암시적 any 방지 (noImplicitAny)
        - 더 안전한 코드 작성 가능 → 런타임 에러 사전 방지
        - 의도하지 않은 버그를 컴파일 단계에서 발견 가능

    - 예시:
        ```ts
        function greet(name: string | null) {
            // strictNullChecks 없으면 오류 없이 통과됨
            console.log(name.toUpperCase()); // runtime error 가능
        }
        ```
        - 한줄 요약: strict는 버그 가능성을 줄이고 타입 안정성을 높여줌

- TypeScript의 Decorator 패턴은 무엇이며, 실제 사용 방법
    - 정의: 데코레이터는 클래스/속성/메서드/파라미터에 메타 프로그래밍 기능을 부여하는 특수 문법임
    - 특징:
        - 코드에 부가 기능 주입: 로깅, 인증, 바인딩 등
        - AOP(관점 지향 프로그래밍)처럼 동작
        - experimentalDecorators 설정 필요

    - 예시:
        ```ts
        function Log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
            const original = descriptor.value;
            descriptor.value = function (...args: any[]) {
                console.log(`Called ${propertyKey} with`, args);
                return original.apply(this, args);
            };
        }

        class Example {
            @Log
            greet(msg: string) {
                console.log(msg);
            }
        }

        new Example().greet('hello'); // 로그 출력 후 메서드 실행
        ```
        - 한줄 요약: 데코레이터는 클래스나 메서드에 기능을 주입해 코드 재사용성과 관심사 분리를 돕는 메타 프로그래밍 도구임

- JavaScript와 TypeScript를 비교했을 때 TypeScript를 사용하면 유지보수성이 개선되는 이유
    - 정적 타입 검사: 컴파일 시점에 타입 오류를 사전에 확인 가능
    - IDE 자동완성 & 리팩토링 용이: 타입 기반 코드 추적 및 변경이 쉬움
    - 자체 문서화 효과: 타입 정의만 봐도 함수/객체 구조를 쉽게 이해
    - 대규모 프로젝트에 적합: 협업 시 계약 기반 개발(타입 계약) 가능
    - 요약: 코드 안정성 향상, 예측 가능한 동작, 오류 감소로 유지보수 비용 절감

- JavaScript에서 CSR(Client Side Rendering)과 SSR(Server Side Rendering)의 차이점
    - CSR (클라이언트 측 렌더링):
        - 브라우저가 JS 받아서 렌더링
        - 초기 로딩 느림, 이후 빠름
        - SEO 불리, 동적 UI에 유리

    - SSR (서버 측 렌더링):
        - 서버에서 HTML 생성 후 전달
        - 초기 로딩 빠름, SEO에 유리
        - 서버 부하 증가, JS 상호작용 시 추가 로딩 필요

    - 요약: CSR은 UX 최적화에, SSR은 초기 속도·SEO에 유리

- JavaScript의 this 바인딩 원리
    - 기본 바인딩: 함수 단독 호출 → 전역(window, undefined in strict)
    - 암시적 바인딩: obj.method() 형태 → obj가 this
    - 명시적 바인딩: call, apply, bind로 this 직접 지정
    - new 바인딩: 생성자 함수 호출 시 새 객체가 this
    - 화살표 함수: this는 선언 당시 상위 스코프를 따라감 (렉시컬 바인딩)
    - 요약: 호출 방식에 따라 this가 결정되며, 화살표 함수는 예외적으로 고정됨

- JavaScript의 Promise와 async/await의 차이
    - Promise:
        - 비동기 작업을 .then().catch() 체인으로 처리
        - 가독성 떨어질 수 있음 (콜백 중첩 유사)

    - async/await:
        - async 함수 내에서 await으로 동기처럼 작성 가능
        - 에러 핸들링도 try/catch로 일관성
        - 더 간결하고 가독성 좋음

    - 요약: Promise는 체이닝 방식, async/await은 동기형 코드 스타일로 더 읽기 쉬움

- TypeScript의 interface와 type의 차이
    - interface: 객체의 구조 정의에 최적화됨, 선언 병합(extend, merge) 가능
    - type: 모든 타입 정의 가능 (유니언, 튜플, 함수 등), 유연한 조합에 강함
    - 차이 요약:
        - interface는 주로 객체 타입 확장에 적합
        - type은 복잡한 타입 표현에 유리
    - 실무에서는 interface를 기본으로, 복잡한 조합이 필요할 때 type을 사용함

- 렉시컬 스코프에 대한 설명
    - 정의: 함수가 정의된 위치(코드 작성 시점) 기준으로 변수의 유효 범위가 결정되는 스코프 방식
    - 특징: 실행 시점이 아닌 선언 시점의 스코프 체인을 따름
    - 예시:
        ```javascript
        function outer() {
            const x = 10;
            function inner() {
                console.log(x); // 10
            }
            return inner;
        }
        ```
    - 요약: 렉시컬 스코프는 함수가 선언된 위치 기준으로 상위 변수에 접근함

- JavaScript에서 클로저(Closure)는 동작원리
    - 정의: 함수가 외부 스코프의 변수에 접근할 수 있는 상태를 유지하는 구조
    - 동작 원리: 함수가 반환되거나 실행 컨텍스트가 종료되어도, 참조된 외부 변수는 GC되지 않고 살아있음
    - 용도: 정보 은닉, 상태 유지, 콜백 핸들링 등
    - 예시:
        ```js
        function counter() {
            let count = 0;
            return () => ++count;
        }

        const c = counter();
        c(); // 1
        c(); // 2
        ```
    - 요약: 클로저는 함수가 외부 변수에 계속 접근 가능하게 하여 상태를 보존함

- JavaScript의 event loop와 call stack의 동작 원리
    - Call Stack:
        - 현재 실행 중인 함수들의 스택. 
        - 함수가 호출되면 쌓이고, 종료되면 빠짐
    
    - Event Loop: Call Stack이 비어 있을 때 Task Queue의 콜백을 하나씩 처리함
    
    - 비동기 처리 흐름:
        - setTimeout, Promise, DOM 이벤트 → 큐에 등록됨
        - Call Stack이 비면, Event Loop가 큐에서 꺼내 실행
    
    - 요약: Call Stack은 함수 실행 순서를, Event Loop는 비동기 작업의 실행 시점을 관리함

- TypeScript에서 unknown과 any의 차이점
    - any: 어떤 타입도 허용하며, 모든 연산 가능 → 타입 안전성 없음
    - unknown: 모든 타입을 수용하지만, 사용 전에 타입 검사가 필요함
    - 차이점:
        - any는 무제한 자유, unknown은 타입 보호 후 사용 가능
        - unknown은 타입 안정성을 유지할 수 있음
        ```ts
        let val: unknown = "test";
        val.toUpperCase(); // 오류
        if (typeof val === 'string') val.toUpperCase(); // OK
        ```
    - 요약: unknown은 타입 안전한 any로, 더 엄격하고 안전함

- TypeScript에서 never 타입 사용 시점
    - 정의: 절대 발생하지 않는 값의 타입 (예: 함수가 끝나지 않거나 에러만 발생할 때)
    - 주요 사용처:
        - throw만 있는 함수 → 반환값 없음
        - switch문의 모든 case를 처리한 후의 default
        - 타입 좁히기 후 도달 불가능한 경우
    - 예제
        ```ts
        function fail(): never {
            throw new Error("error");
        }

        function check(x: string | number) {
            if (typeof x === 'string') return;
            if (typeof x === 'number') return;
            x; // never
        }
        ```
    - 요약: never는 도달 불가능한 상태나 반환값이 절대 없는 상황을 명시할 때 사용함

- JavaScript의 debounce와 throttle의 차이
    - debounce: 이벤트 발생 후 일정 시간 동안 추가 이벤트 없을 때 실행
        - 마지막 이벤트만 실행됨
        - 예: 검색창 자동완성, resize 끝난 후 작업

    - throttle: 일정 간격마다 이벤트 실행, 중간 이벤트 무시
        - 주기적으로 실행됨
        - 예: 스크롤 위치 추적, 드래그 처리

    - 요약:
        - debounce는 “마지막에 한 번”,
        - throttle은 “간격마다 한 번”

- JavaScript의 Prototype Chain과 Closure를 활용한 메모리 최적화 방법
    - Prototype Chain: 
        - 객체 간 상속 구조. 
        - 공통 메서드는 prototype에 정의하여 메모리 절약
        - 추가 설명
            - 메서드를 인스턴스마다 생성하지 않음
            - Object.create()나 클래스 prototype에 메서드 저장
            ```js
            function Animal() {}
            Animal.prototype.speak = function () { 
                console.log('sound'); 
            };
            ```
    
    - Closure 활용: 필요한 값만 클로저로 캡슐화하여 외부 노출 차단
        - 반복적으로 생성되는 객체의 내부 상태 은닉 → 불필요한 참조 제거
        ```js
        function createCounter() {
            let count = 0;
            return () => ++count;
        }
        ```
        - 요약:
            - Prototype은 공용 메서드 공유로 메모리 절약
            - Closure는 불필요한 전역 노출 방지와 상태 은닉에 도움

- JavaScript의 Event Loop와 Microtask Queue의 차이
    - Event Loop: Call Stack이 비면 큐에서 작업을 꺼내 실행
    - Microtask Queue: Promise .then, MutationObserver 등 고우선 작업이 담김
        - 이벤트 큐(Task Queue)보다 먼저 처리됨
        - 하나의 작업(예: 클릭 이벤트) 처리 후, 다음 이벤트 전에 모든 Microtask 처리
        ```js
        console.log('start');
        Promise.resolve().then(() => console.log('microtask'));
        setTimeout(() => console.log('macrotask'), 0);
        console.log('end');
        // 출력: start → end → microtask → macrotask
        ```
    - 요약:
        - Microtask는 더 빠르게, 우선적으로 실행됨
        - 일반 이벤트보다 먼저 소비되는 고우선 큐

- TypeScript의 Mapped Types와 Conditional Types의 동작원리
    - Mapped Types: 기존 타입의 모든 프로퍼티에 대해 일괄적으로 수정된 타입을 생성
        - 예: readonly, optional, nullable 변환
        ```ts
        type ReadOnly<T> = {
            [P in keyof T]: T[P];
        };
        ```

    - Conditional Types: 타입 간 조건 분기
        - A extends B ? X : Y 형태로 사용
        ```ts
        type IsString<T> = T extends string ? true : false;
        ```

    - 요약
        - Mapped → 속성 반복 변형
        - Conditional → 타입 조건 분기

- JavaScript에서 WeakMap, WeakSet의 사용 사례
    - WeakMap: 키가 객체만 가능, 참조가 사라지면 자동 GC
        - 캐싱, 프라이빗 데이터 저장 등에 사용
        ```js
        const wm = new WeakMap();
        wm.set(obj, "value"); // obj가 null되면 자동 GC
        ```
    - WeakSet: 객체만 저장 가능, 중복 허용 안 함
        - 특정 객체가 등록됐는지 여부 추적할 때 사용

    - 실제 사례:
        - DOM 노드 관련 임시 데이터 저장
        - 라이브러리에서 내부 상태 은닉 (메모리 누수 방지)
    - 요약:
        - GC 친화적 구조로, 일시적 객체의 상태 추적이나 은닉에 유리
    
- JavaScript에서 Proxy와 Reflect API 유용한 시점
    - Proxy: 객체의 접근/설정/삭제 등 모든 동작을 가로채는 래퍼
        - 예: 속성 접근 감시, 유효성 검사, 동적 속성 대응
        ```js
        const user = new Proxy({}, {
            get: (target, prop) => prop in target ? target[prop] : 'default',
        });
        ```

    - Reflect: Proxy 트랩 내부에서 원래 동작을 안전하게 수행할 때 사용
        - 내부 작업을 직접 구현하지 않고 일관된 방식으로 수행 가능
        ```js
        get(target, prop) {
            console.log('get', prop);
            return Reflect.get(target, prop);
        }
        ```

    - 요약:
        - Proxy → 행동을 가로채고 제어
        - Reflect → 가로챈 동작을 안전하게 위임

- TypeScript에서 Utility Types를 활용하여 코드 재사용성을 높이는 방법
    - 정의: 기존 타입을 변형해 새로운 타입을 만들 수 있는 도구 타입들
    - 대표 예시:
        - Partial<T>: 모든 속성을 optional로
        - Pick<T, K>: 특정 속성만 선택
        - Omit<T, K>: 특정 속성 제외
        - Readonly<T>: 모든 속성을 읽기 전용
        - Record<K, T>: K 키들에 대해 T 값을 매핑
        ```ts
        type User = { id: number; name: string; age: number };
        type UserPreview = Pick<User, 'id' | 'name'>;
        ```
    - 요약: 반복 타입 정의 없이 필요한 구조를 간결하게 재구성 가능 → 유지보수성과 재사용성 향상

- JavaScript의 var, let, const의 차이점
    - var: 함수 스코프, 중복 선언 가능, 호이스팅 시 undefined
    - let: 블록 스코프, 재할당 가능, 호이스팅되지만 TDZ(Temporal Dead Zone) 존재
    - const: 블록 스코프, 재할당 불가 (하지만 객체는 내부 변경 가능)
    ```js
    {
        var a = 1; // 바깥에서도 접근됨
        let b = 2; // 블록 내부에서만
        const c = 3;
    }
    ```
    - 요약: let과 const는 블록 스코프, const는 불변 참조 → var는 지양, const 우선 사용 권장

- Hoisting(호이스팅) 정의와 동작 원리
    - 정의: 변수, 함수 선언이 스코프 최상단으로 끌어올려지는 JS의 동작 방식
    - 동작 원리:
        - var, function 선언은 실행 전에 메모리에 등록됨
        - let, const도 호이스팅되지만 TDZ(Temporal Dead Zone) 때문에 초기화 전 접근 시 오류 발생
        ```js
        console.log(a); // undefined
        var a = 5;  // 5로 정의

        console.log(b); // ReferenceError
        let b = 10; // 10으로 정의
        ```
    - 요약:
        - var/function은 선언만 끌어올려짐 → undefined로 접근 가능
        - let/const는 호이스팅되지만 초기화 전 접근 금지 → 런타임 에러 발생

- 호이스팅에 대한 고찰
    - 개요
        - C++에서 함수 선언을 코드 상단에 명시 > 아래에서 해당 함수 호출 가능한 것처럼
        - 자바스크립트에서는 호이스팅 덕분에 아래에서 선언된 함수나 변수를 위에서 사용할 수 있게 됨
        - 그러나 C++의 이 개념과는 차이가 있음

    - C++ 함수 선언 vs JavaScript 호이스팅 차이
        - C++: 함수의 시그니처만 상단에 명시하는 선언(Declaration).
            - 실제 구현(Definition)은 아래에 있어도 됨.
            - 컴파일러가 명시적으로 해석함 (정적 언어)
            ```cpp
            void print(); // 선언

            int main() {
                print(); // 사용 가능
            }

            void print() {
                std::cout << "Hello";
            }
            ```
        - JavaScript: 인터프리터가 실행 전에 암묵적으로 선언을 끌어올림
            - 변수는 undefined로 초기화 (var), let/const는 TDZ 적용
            - 함수 선언문은 전체 함수 본문까지 호이스팅됨
            ```js
            greet(); // 가능
            
            function greet() {
                console.log("Hello");
            }
            ```

        - 요약
            - C++은 명시적 선언,
            - JavaScript는 암묵적 호이스팅
            - 비슷하지만, 정적 vs 동적 해석 방식의 차이로 인해 의도적이냐 자동이냐, 언제 초기화되냐가 다름

- undefined에 대한 설명
    - 정의: 변수는 선언됐지만, 값이 할당되지 않았을 때 자동으로 부여되는 기본값
    - 자동 부여 상황:
        - 변수를 let, var로 선언만 했을 때
        - 함수에서 명시적 return 없이 종료
        - 객체에서 존재하지 않는 속성 접근
        - 배열의 비어 있는 인덱스 접근
        ```js
        let a;
        console.log(a); // undefined

        function test() {}
        console.log(test()); // undefined

        const obj = {};
        console.log(obj.foo); // undefined
        ```
    - typeof 결과: typeof undefined → 'undefined'
    - 주의: undefined는 null과 다름 (둘 다 falsy지만 의미가 다름)
    - 요약
        - undefined는 "값이 없다"가 아니라, "값이 아직 할당되지 않았다"는 상태
        - 명시적 할당 없이 생기는 JavaScript 고유의 기본값
        - 개발자가 직접 할당하기보다는 상태 확인용으로 사용하는 것이 좋음

- null, NaN, falsy, == vs === 비교
    - null
        - 의도적으로 "없음"을 나타내는 값
        - 개발자가 직접 할당
        - typeof null은 'object' (역사적 버그지만 유지됨)
        - 예: let data = null; → "여기에 일부러 비워둠" 의미

    - NaN (Not-a-Number)
        - 숫자 타입인데, 숫자가 아님을 의미
        - 계산이 실패했을 때 발생 (ex: 0 / 0, parseInt('abc'))
        - typeof NaN은 'number'
        - NaN은 자기 자신과도 같지 않음 → NaN === NaN → false
        - 비교할 땐 Number.isNaN(value) 사용

    - falsy
        - Boolean 변환 시 false로 평가되는 값들
        - 대표적인 falsy 값:
            - false, 0, '' (빈 문자열), null, undefined, NaN
        - truthy는 falsy가 아닌 모든 값

    - == vs ===
        - == (느슨한 비교): 타입이 다르면 암묵적 형변환 후 비교
        - === (엄격한 비교): 타입과 값이 모두 같아야 true
            - 실무에서는 예측 가능한 결과를 위해 항상 === 권장

    - 요약
        - null: 일부러 비운 값
        - NaN: 수치 연산 실패 결과
        - falsy: 조건문에서 false로 처리되는 값들
        - ==: 형 변환 후 비교 / ===: 타입까지 비교 (권장)

- typeof null === 'object'가 왜 버그인지, 왜 발생했는지, 그리고 왜 아직까지 유지되는지에 대한 설명
    - typeof null === 'object'는 왜 버그인가?
        - null은 원시 타입(primitive)인데, typeof 연산자 결과가 'object'로 나옴
        - 논리적으로 맞지 않음: null은 객체가 아님
        - JS 입문자들이 가장 많이 혼동하는 부분 중 하나

    - 이 버그는 왜 생겼는가?
        - 역사적 배경:
            - JavaScript의 typeof는 초기 구현 당시 값의 내부 표현을 참조
            - 내부적으로 값들은 태그(tag) 형태로 저장됨
                - 예: 객체는 000으로 시작하는 태그, null도 같은 태그 사용
            - 결과적으로 null도 object처럼 취급된 것
        - ECMAScript 초창기 설계 실수였고, 이미 퍼져버린 생태계로 인해 변경 불가

    - 왜 지금까지 수정되지 않았는가?
        - 하위 호환성 때문
            - typeof null === 'object'를 기반으로 만든 수많은 웹사이트가 존재
            - 수정할 경우 기존 코드에서 오류 발생 위험 → JS는 웹 호환성에 매우 민감
        - 대신 대안 제공
            - 정확히 null 여부 확인 시는 value === null
            - 또는 value == null로 null | undefined 동시에 체크

    - 요약
        - typeof null === 'object'는 초기 JS 설계 실수
        - null은 객체가 아님에도 내부 태그값 때문에 'object'로 표시됨
        - 하위 호환성 때문에 지금도 유지 중
        - 정확한 null 체크는 value === null로 수행해야 함

- ==와 ===의 차이점
    - == (동등 연산자): 타입이 다르면 암묵적 형변환 후 비교
    - === (일치 연산자): 타입과 값 모두 동일해야 true
    - 예시:
        ```js
        0 == '0';           // true (형변환 발생, 암묵적 형변환)
        0 === '0';          // false
        null == undefined;  // true
        null === undefined; // false
        ```
    - 요약: ===은 예측 가능한 정확한 비교, 실무에서는 === 사용이 기본

- typeof, instanceof, Object.prototype.toString 간의 차이
    - typeof
        - 용도: 원시 타입(primitive) 확인
        - 결과값: 
            - 문자열 ('string', 'number', 'undefined', 'boolean', 'symbol', 'bigint', 'function', 'object')
        - 한계:
            - 배열, 객체, null, 함수 → 대부분 'object'로 나옴
            - typeof null === 'object' (역사적 버그)
        ```js
        typeof 123          // 'number'
        typeof 'hi'         // 'string'
        typeof undefined    // 'undefined'
        typeof null         // 'object' ← 주의, 역사적 버그
        typeof [1, 2, 3]    // 'object'
        typeof function(){} // 'function'
        ```

    - instanceof
        - 용도: 객체가 어떤 생성자(constructor)의 인스턴스인지 확인
        - 기준: 프로토타입 체인을 따라 constructor.prototype을 검사
        - 한계:
            - 원시 타입엔 사용 불가
            - 다른 iframe/window에서 생성된 객체는 실패할 수 있음 (다른 realm)
        - 예제
            ```js
            [] instanceof Array      // true
            {} instanceof Object     // true
            'hi' instanceof String   // false (원시값은 false)
            new String('hi') instanceof String // true
            ```

    - Object.prototype.toString.call(value)
        - 용도: 정확한 내부 타입 식별
        - 결과값: "[object Type]" 형태의 문자열
        - 장점: 배열, null, Date 등도 정확히 구분 가능
        - 실무에서 가장 정밀한 타입 확인 방법 중 하나
        ```js
        Object.prototype.toString.call(null)         // '[object Null]'
        Object.prototype.toString.call([])           // '[object Array]'
        Object.prototype.toString.call(() => {})     // '[object Function]'
        Object.prototype.toString.call(new Date())   // '[object Date]'
        ```

- JavaScript에서 null과 undefined의 차이
    - undefined: 변수는 선언되었지만 값이 할당되지 않은 상태
        - 자바스크립트가 자동으로 부여
    - null: 의도적으로 “값이 비어 있음”을 나타내기 위해 개발자가 명시적으로 할당
    - 차이 요약:
        - undefined → "할당되지 않음"
        - null → "비어 있도록 명시함"
    - 예제
        ```js
        let a;
        console.log(a); // undefined

        let b = null;
        console.log(b); // null
        ```


- JavaScript에서 typeof 연산자가 반환하는 값
    - 결과값: 항상 문자열 형태로 타입 이름을 반환
    - 주요 반환값:
        - 'undefined', 'object', 'boolean', 'number', 'string'
        - 'function', 'symbol', 'bigint'
    - 주의할 점:
        - typeof null → 'object' (버그)
        - 배열도 'object'
    - 예제
        ```js
        typeof 123           // 'number'
        typeof 'hi'          // 'string'
        typeof undefined     // 'undefined'
        typeof null          // 'object' ← 주의
        typeof () => {}      // 'function'
        ```

- JavaScript에서 데이터 타입 종류 및 개수
    - 총 개수
        - 총 8가지 (ES6 기준)

    - 원시 타입 (Primitive)
        - undefined
        - null
        - boolean
        - number
        - string
        - symbol (ES6)
        - bigint (ES2020)

    - 참조 타입 (Reference)
        - object
            - 배열, 함수, 객체, 날짜 등 포함

    - 요약:
        - 원시 타입은 값 자체를 저장
        - 참조 타입은 메모리 주소를 통해 값 참조

- IIFE(즉시 실행 함수, Immediately Invoked Function Expression)의 역할
    - 정의
        - 즉시 실행 함수, Immediately Invoked Function Expression
        - 정의하자마자 즉시 실행되는 함수 표현식
    - 형태
        ```js
        (function() {
            console.log('실행됨');
        })();
        ```

    - 주요 역할:
        - 변수 스코프를 지역화해서 전역 오염 방지
        - 모듈화 패턴 구현 (ES6 이전)
        - 클로저 기반 초기화 코드 실행에 활용

    - 요약: IIFE는 즉시 실행 + 스코프 보호용 함수로 많이 사용됨

- JavaScript에서 truthy와 falsy 값 설명
    - falsy 값 (Boolean으로 변환 시 false):
        - false, 0, '' (빈 문자열), null, undefined, NaN

    - truthy 값 (그 외 전부):
        - 빈 배열 [], 빈 객체 {}, '0', 'false', Infinity, -1 등

    - 요약: falsy는 JS에서 조건문 등에서 false로 간주되는 값 → 이외는 모두 truthy

- JavaScript에서 deep copy와 shallow copy의 차이
    - shallow copy (얕은 복사):
        - 최상위 값만 복사, 내부 객체는 참조 유지
        - ex: Object.assign({}, obj), spread { ...obj }

    - deep copy (깊은 복사):
        - 중첩 객체까지 전부 복사, 원본과 완전히 독립
        - ex: structuredClone(obj), JSON.parse(JSON.stringify(obj)) (단점 있음)

    - 예제 (얕은 복사)
        ```js
        const obj = { a: 1, b: { c: 2 } };
        const shallow = { ...obj };
        shallow.b.c = 9; // 원본 obj도 영향 받음
        ```

    - 요약:
        - shallow: 참조 공유됨
        - deep: 완전히 독립된 복사본 생성

- ...obj 에서 ...의 의미
    - 정의: 전개 연산자(Spread Operator, 스프레드 오퍼레이션)
        - 객체나 배열의 요소를 개별적으로 펼쳐서 복사하거나 전달하는 문법

    - 객체에서 사용 예제
        ```js
        const obj1 = { a: 1, b: 2 };
        const obj2 = { ...obj1, c: 3 };  // { a: 1, b: 2, c: 3 }
        ```

    - 배열에서 사용
        ```js
        const arr1 = [1, 2];
        const arr2 = [...arr1, 3]; // [1, 2, 3]
        ```
        - 배열도 마찬가지로 각 요소를 펼쳐서 새로운 배열을 만듦

    - 함수 인자에서 사용 (Rest Parameter 와는 반대)
        ```js
        function sum(a, b, c) {
            return a + b + c;
        }

        const nums = [1, 2, 3];
        sum(...nums); // 6
        ```
        - 배열 요소를 개별 인자처럼 전달할 때 사용

    - 요약
        - ...은 객체/배열/인자의 요소를 펼치거나 복사할 때 사용
        - Spread는 복사, 병합, 전달에 유용한 문법 도구

- Rest parameter, default parameter, 배열과 객체 구조 분해
    - Rest Parameter (...args)
        - 정의: 함수의 가변 인자들을 배열로 수집
        - 문법: function fn(...args) {}
        - 예시:
            ```js
            function sum(...nums) {
                return nums.reduce((a, b) => a + b, 0);
            }
            sum(1, 2, 3); // 6
            ```
        - 요약: Rest는 나머지를 모은다, 항상 마지막 인자에만 위치 가능

    - Default Parameter
        - 정의: 함수 인자에 기본값 설정
        - 예시:
            ```js
            function greet(name = 'Guest') {
                console.log(`Hello, ${name}`);
            }
            greet(); // Hello, Guest
            ```
        - 요약: 전달된 인자가 undefined일 경우 기본값 사용

    - 구조 분해 할당 (Destructuring Assignment)
        - 배열 구조 분해
            ```js
            const arr = [1, 2, 3];
            const [a, b] = arr; // a=1, b=2
            ```
        - 객체 구조 분해
            ```js
            const user = { name: 'Tom', age: 30 };
            const { name, age } = user;
            ```
        - 구조 분해 + 기본값 + 나머지 (Rest)
            ```js
            const [x, y = 5, ...rest] = [1];
            console.log(x); // 1
            console.log(y); // 5
            console.log(rest); // []

            const { a, ...others } = { a: 1, b: 2, c: 3 };
            console.log(others); // { b: 2, c: 3 }
            ```

    - 요약: 
        - 구조 분해는 값을 변수로 쉽게 분리
        - Rest는 나머지를 모음
        - Default는 값이 없을 때 기본 대입

- JavaScript에서 Object.freeze(), Object.seal(), Object.assign()의 차이점
    - Object.freeze(obj)
        - 불변 객체로 만듦
        - 속성 추가/삭제/수정 모두 불가능
        - 깊은 freeze는 아님 (중첩 객체는 여전히 변경 가능)

    - Object.seal(obj)
        - 속성 추가/삭제 불가, 수정은 가능
        - 구조는 고정되지만 값은 바뀔 수 있음

    - Object.assign(target, source)
        - 객체 복사 또는 병합에 사용, 속성 추가/수정 가능
        - 얕은 복사 (shallow copy) 수행
        - 같은 키가 있으면 덮어씀

    - 예제
        ```js
        const a = { x: 1 };
        const b = { y: 2 };
        const merged = Object.assign({}, a, b); // { x: 1, y: 2 }
        ```

- JavaScript에서 Object.create(null)를 사용하면 어떤 차이가 있는지 설명
    - 일반 객체는 Object.prototype을 상속
        - 기본 메서드 (toString, hasOwnProperty, 등)가 있음
    - Object.create(null)은 순수한 딕셔너리 객체 생성
        - 프로토타입 체인이 없음
        - 해시 맵처럼 사용 시 충돌 방지
    - 예제
        ```js
        const obj = Object.create(null);
        obj.toString; // undefined
        ```
    - 실전 활용: 키 충돌 없는 순수 데이터 저장용 객체로 적합

- JavaScript에서 함수 선언과 함수 표현식의 차이
    - 함수 선언 (Function Declaration)
        ```js
        function greet() {
            console.log('hi');
        }
        ```
        - 호이스팅 O: 코드 위에서도 호출 가능, 선언 전 사용 가능
        - 전역이나 블록 내에 선언됨

    - 함수 표현식 (Function Expression)
        ```js
        const greet = function() {
            console.log('hi');
        };
        ```
        - 호이스팅 X: 변수는 호이스팅되지만, 값 할당 전엔 사용 불가, 선언 이후에만 사용 가능
        - 함수가 값처럼 변수에 할당됨

- JavaScript에서 bind, call, apply의 차이점
    - 공통점: 함수의 this를 명시적으로 설정하는 방법
    - 차이점:
        - bind:
            - 실행 여부 X
            - 인자 전달 방식: 나중에 실행, bind(this, a, b)
            - 용도: 함수 복제 (지연 실행용)
        - call:
            - 실행 여부 O
            - 즉시 실행, call(this, a, b)
            - 용도: 즉시 실행 + this 지정
        - apply:
            - 실행 여부 O
            - 즉시 실행, apply(this, [a, b])
            - 용도: 인자를 배열로 전달해야 할 때 유용
    - 예제
        ```js
        function greet(msg) {
            console.log(msg + ', ' + this.name);
        }
        const person = { name: 'Tom' };

        greet.call(person, 'Hello');        // Hello, Tom
        greet.apply(person, ['Hi']);        // Hi, Tom

        const bound = greet.bind(person);   // 지연 실행용
        bound('Hey');                       // Hey, Tom
        ```

- JavaScript에서 setTimeout과 setInterval의 동작 원리
    - setTimeout(fn, delay): 일정 시간 후 한 번 실행
    - setInterval(fn, delay): 일정 시간마다 반복 실행
    - 공통점:
        - 둘 다 비동기 타이머 함수, Web API에 의해 동작
        - 실행 후 콜백은 Task Queue에 등록, Call Stack이 비면 실행됨
    - 예제
        ```js
        setTimeout(() => console.log('once'), 1000);
        setInterval(() => console.log('repeat'), 1000);
        ```
    - 주의: 정확한 시간 보장은 아님 (이벤트 루프 상태에 따라 지연 가능)

- JavaScript에서 Map과 Object의 차이점
    - Map
        - 키 타입: 모든 값 (객체 포함)
        - 순서 보장: 입력 순서 보장
        - 반복 및 크기 측정: map.size, for...of 가능
        - 성능: 많은 키 삽입/삭제 시 더 안정적
    - Object
        - 키 타입: 문자열, 심볼만
        - 순서 보장: 일부 엔진만 보장(명시적 아님)
        - 반복 및 크기 측정: 수동 처리 필요(ex: Object.keys)
        - 성능: 간단한 구조에만 적합
    - 예제
        ```js
        const map = new Map();
        map.set('a', 1);
        map.set({}, 2); // 객체도 키로 가능

        const obj = { a: 1 };
        obj[{}] = 2; // 키가 문자열로 강제 변환됨: "[object Object]"
        ```
    - 요약
        - Map은 고급 키/값 저장, 순서 보장, 객체 키 가능
        - Object는 간단한 구조에 적합하며 프로토타입 이슈 있음

- JavaScript에서 forEach, map, filter, reduce의 차이점
    - forEach
        - 목적: 반복 수행(단순 실행)
        - 반환값: 없음 (undefined)
        - 사용 예: 로그 출력, 외부 변수 조작 등
    - map
        - 목적: 요소 변환
        - 반환값: 새 배열
        - 사용 예: 변환된 배열 만들 때
    - filter
        - 목적: 조건 필터링
        - 반환값: 조건 통과한 새 배열
        - 사용 예: 조건 만족 요소 추출
    - reduce
        - 목적: 누적 계산
        - 반환값: 누적 결과값
        - 사용 예: 합계, 객체로 변환 등
    - 예제
        ```js
        const arr = [1, 2, 3];
        arr.forEach(v => console.log(v));           // 단순 실행
        const doubled = arr.map(v => v * 2);        // [2, 4, 6]
        const evens = arr.filter(v => v % 2 === 0); // [2]
        const sum = arr.reduce((a, b) => a + b, 0); // 6
        ````
    - 요약
        - forEach는 실행만
        - map은 변환
        - filter는 추출
        - reduce는 누적

- JavaScript에서 동기 코드와 비동기 코드의 차이
    - 동기(Synchronous):
        - 위에서 아래로 차례대로 실행
        - 다음 작업은 이전 작업이 끝날 때까지 대기
        - 예: 일반 함수 호출, 수학 계산

    - 비동기(Asynchronous):
        - 바로 다음 줄로 넘어감, 작업 완료는 나중에
        - 대기 중인 작업은 콜백, 프로미스 등으로 처리
        - 예: setTimeout, fetch, 이벤트 리스너

    - 예제
        ```js
        console.log(1);
        setTimeout(() => console.log(2), 0);
        console.log(3);  // 결과: 1 → 3 → 2
        ```

    - 요약:
        - 동기: 순차 실행
        - 비동기: 나중에 실행 (이벤트 루프에 의해 처리)

- JavaScript의 실행 컨텍스트(Execution Context)
    - 정의: 코드가 실행되는 환경/정보의 집합
    - 종류:
        - 전역 실행 컨텍스트 (스크립트 전체 실행 시 생성)
        - 함수 실행 컨텍스트 (함수 호출 시마다 생성)
        - eval 실행 컨텍스트 (사용 지양)

    - 구성요소:
        - Variable Environment: 변수/함수 선언 정보
        - Lexical Environment: 현재 스코프 체인
        - this 바인딩: 현재 컨텍스트의 this 값

    - 실행 흐름:
        - 실행 컨텍스트는 Call Stack에 쌓이고,
        - 가장 위의 컨텍스트가 현재 실행 중인 코드 환경을 의미

    - 예제
        ```js
        function foo() {
            let x = 10;
        }
        foo(); // foo() 실행 시 새로운 컨텍스트 생성됨
        ```
    - 요약: 실행 컨텍스트는 JS 코드가 어디서, 어떻게 실행될지를 정의하는 실행 단위의 기본 구조

- this 바인딩, 클로저, 실행 컨텍스트, 스코프 체인 고찰
    - this 바인딩
        - 정의: 함수가 호출되는 방식에 따라 결정되는 실행 컨텍스트 내의 참조 객체
        - 바인딩 방식:
            - 호출방식 & this 값 정보
                - 일반 함수 호출: 전역 객체 (window, strict에서는 undefined)
                - 메서드 호출: 해당 객체
                - 생성자 호출(new): 새로 생성된 인스턴스
                - call, apply, bind: 명시적으로 지정한 객체
                - 화살표 함수: 외부 스코프의 this를 그대로 사용 (렉시컬 this)
        - 예제
            ```js
            const obj = {
                value: 1,
                get: function () { return this.value; }
            };
            obj.get(); // 1

            const get = obj.get;
            get(); // undefined (전역 또는 strict 모드에 따라 다름)
            ```
        - 요약: this는 정의된 곳이 아니라 호출된 방식에 따라 결정됨

    - 클로저 vs 실행 컨텍스트
        - 클로저
            - 정의: 함수가 외부 스코프의 변수를 기억하는 기능
            - 생성 시점: 함수가 정의될 때
            - 수명: 참조가 유지되는 한 지속됨 (GC 예외 대상)
            - 역할: 상태 유지, 은닉
        - 실행 컨텍스트
            - 정의: 코드 실행 환경에 대한 모든 정보 집합
            - 생성 시점: 코드 실행 시 (전역, 함수 등)
            - 수명: 실행 종료 시 콜 스택에서 제거됨
            - 역할: 변수/스코프/this 관리
        - 예제
            ```js
            function outer() {
                let count = 0;
                return function () {
                    return ++count;
                };
            }

            const counter = outer(); // 클로저 생성
            counter(); // 1
            counter(); // 2
            ```
        - 요약:
            - 실행 컨텍스트는 일시적인 실행 환경
            - 클로저는 그 환경의 일부를 계속 기억하는 함수 객체

    - 스코프 체인 (Scope Chain)
        - 정의: 변수를 찾을 때 현재 렉시컬 환경부터 상위 스코프까지 검색하는 구조
        - 실행 컨텍스트 안의 Lexical Environment가 체인 구조로 연결됨
        - 예제:
            ```js
            function outer() {
                let x = 10;
                function inner() {
                    console.log(x); // outer의 x를 참조
                }
                inner();
            }
            ```
        - 동작 원리:
            - inner → outer → global 순으로 위로 거슬러 올라가며 변수 탐색
        - 관련 키워드:
            - 렉시컬 스코프(정의된 위치 기준)
            - 클로저도 이 스코프 체인을 참조해 외부 변수 기억함
        - 요약: 스코프 체인은 내부 함수에서 외부 변수에 접근할 수 있게 해주는 구조
    
    - 핵심 흐름 요약
        - 실행 컨텍스트가 만들어지면 → 스코프 체인과 this 바인딩 설정
        - 함수가 생성될 때 외부 스코프를 기억하며 → 클로저가 생성됨
        - 클로저는 해당 실행 컨텍스트 일부(렉시컬 환경)를 계속 참조함
        - 변수 탐색 시 스코프 체인을 따라 위로 올라가며 찾음

- 렉시컬 스코프(Lexical Scope)와 렉시컬 this
    - 렉시컬 스코프 (Lexical Scope)
        - 정의: 함수가 정의된 위치(코드 작성 시점) 기준으로 상위 스코프가 결정되는 방식
            - 누가 호출했는지와는 무관, 어디서 선언되었는지가 중요함
            - 쉽게 말해: 함수가 어디서 호출되든, 자기 주변 코드(정의된 위치)만 본다는 것
        - 예제
            ```js
            const x = 1;

            function outer() {
                const x = 2;

                function inner() {
                    console.log(x); // → 2 (정의된 위치 기준)
                }

                return inner;
            }

            const fn = outer();
            fn(); // outer 안에 정의됐으므로 x = 2
            // 즉, fn() 호출은 외부에서 했지만 함수가 정의된 위치,
            // 코드 작성 시점 기준으로 동작하게 됨
            // 그러므로 값은 2 즉, 기존에 선언될 때 정의되었던 const x = 2의 2가 반환
            ```

    - 렉시컬 this (Lexical this)
        - 정의: this 값이 선언된 위치의 상위 스코프를 따라 결정되는 방식
        - 화살표 함수에서만 적용
        - 일반 함수는 this가 호출된 방식에 따라 달라지지만, 화살표 함수는 고정됨
        - 예제
            ```js
            const person = {
                name: 'Alice',
                greet: function () {
                    setTimeout(() => {
                        console.log(this.name); // → 'Alice'
                    }, 100);
                }
            };

            person.greet();
            ```
        - setTimeout 안의 화살표 함수는 this를 자신이 선언된 greet 함수의 this로 고정해서 사용함 → 즉 person

    - 요약
        - 렉시컬 스코프
            - 기준: 함수의 정의 위치
            - 적용대상: 모든 함수
            - 동작방식: 변수 탐색 시 상위 코드 범위 기준
        - 렉시컬 this
            - 기준: 화살표 함수의 정의 위치
            - 화살표 함수만 해당
            - this는 상위 스코프의 this를 따름

- this 바인딩 방식 5가지와 함께, 화살표 함수 vs 일반 함수의 this 차이
    - JavaScript의 this 바인딩 방식 5가지 (기본, 암시, 명시, new, 렉시컬)
        - 기본 바인딩 (Default Binding)
            - 일반 함수 호출 시 → this는 전역(window) 또는 undefined (strict mode)
            ```js
            function show() {
                console.log(this); // window or undefined
            }
            show();
            ```

        - 암시적 바인딩 (Implicit Binding)
            - 객체의 메서드로 호출될 경우 → 해당 객체가 this
            ```js
            const obj = { name: 'Tom', say() { console.log(this.name); } };
            obj.say(); // 'Tom'
            ```

        - 명시적 바인딩 (Explicit Binding)
            - call, apply, bind를 통해 this를 직접 지정
            ```js
            function say() { console.log(this.name); }
            const user = { name: 'Alice' };
            say.call(user); // 'Alice'
            ```

        - new 바인딩 (Constructor Binding)
            - new 키워드로 생성자 함수 호출 시 -> 새로 생성된 인스턴스가 this
            ```js
            function Person(name) { this.name = name; }
            const p = new Person('Bob'); // p.name = 'Bob'
            ```

        - 렉시컬 바인딩 (Arrow Function)
            - this가 정적으로 결정됨 -> 상위 스코프의 this를 그대로 사용
            - 바인딩 불가능 (call, apply, bind로도 변경 안됨)

    - 화살표 함수 vs 일반 함수의 this 차이
        - 일반 함수
            - this 바인딩 방식: 호출 시점에 결정(동적)
            - call/apply/bind 작동: 작동함
            - 주 용도: 동적 객체 메서드, 생성자 함수 등
        - 화살표 함수
            - this 바인딩 방식: 정의된 위치의 외부 this (렉시컬)
            - call/apply/bind 작동: 작동 안 함
            - 주 용도: 콜백 함수, setTimeout 내부, React 등
        - 예제
            ```js
            const obj = {
                name: 'Charlie',
                say: function () {
                    setTimeout(function () {
                        console.log(this.name); // undefined (전역)
                    }, 100);
                },
            };

            const obj2 = {
                name: 'Dana',
                say: function () {
                    setTimeout(() => {
                        console.log(this.name); // 'Dana' (렉시컬 this)
                    }, 100);
                },
            };
            ```
        - 요약
            - this는 어떻게 호출되었는지에 따라 달라지는 동적 개념
            - 화살표 함수는 유일하게 this가 정적으로(렉시컬) 바인딩됨
            - 정확한 제어가 필요하면 call, bind, 또는 화살표 함수 사용 고려

- 렉시컬 스코프 vs 다이나믹 스코프, 가비지 컬렉션 시점, 메모리 누수 원인, Event Loop + 클로저 조합 문제
    - 렉시컬 스코프 vs 다이나믹 스코프
        - 렉시컬 스코프
            - 기준: 코드 작성 시점 (함수 정의 위치)
            - 변수 탐색 위치: 정의된 시점의 외부 스코프 체인
            - 언어 예시: 자바스크립트, 파이썬 등
        - 다이나믹 스코프
            - 기준: 코드 실행 시점 (함수 호출 위치)
            - 변수 탐색 위치: 호출한 곳의 실행 컨텍스트 체인
            - 언어 예시: 일부 Lisp 계열, Bash 등
        - 예제
            ```js
            // 렉시컬 스코프 예시
            const a = 1;
            function outer() {
                const a = 2;
                function inner() {
                    console.log(a); // 2 ← 정의된 외부 스코프 기준
                }
                inner();
            }
            outer();
            ```
        - 요약: 자바스크립트는 정의 위치 기준(정적)인 렉시컬 스코프만 사용

    - 가비지 컬렉션(GC) 시점
        - 정의: 더 이상 접근할 수 없는 메모리를 자동으로 해제
        - GC 시점 조건:
            - 도달 불가능한 객체 (reachability graph에 포함되지 않음)
            - 루트 객체(window/globalThis)에서 참조되지 않으면 GC 대상
        - 예제
            ```js
            let obj = { name: 'data' };
            obj = null; // 이전 객체는 더 이상 참조되지 않음 → GC 대상
            ```
            - GC는 명시적 시점이 없음 → JS 엔진(V8 등)이 알고리즘으로 자동 처리
        - 요약: 참조가 완전히 끊긴 객체는 GC 대상, 직접 해제는 불가능

    - 메모리 누수(Memory Leak) 주요 원인
        - 전역 변수 남용
            - 참조가 계속 유지되어 GC가 못 지움
        - 클로저 내부에서 불필요한 외부 참조 유지
            - 오래 살아남는 클로저가 불필요한 데이터까지 보관
        - DOM 참조 유지
            - 제거된 DOM을 코드에서 계속 참조할 경우
        - 이벤트 리스너 제거 안 함
            - addEventListener만 하고 removeEventListener 안 하면 참조 유지됨
        - 누수 예시
            ```js
            function leak() {
                const large = new Array(1000000).fill('...');
                return () => console.log(large.length); // 클로저가 large를 계속 참조
            }
            const hold = leak(); // large가 GC 안 됨
            ```
        - 요약: GC는 똑똑하지만, 개발자가 참조를 무심코 유지하면 메모리 누수 발생

    - Event Loop + 클로저 조합 문제
        - 상황: 클로저로 묶인 데이터를 Event Queue나 Timer로 넘길 때, 이벤트가 실행되기 전까지 불필요한 메모리 유지

        - 문제 예시:
            ```js
            function createHandler() {
                const hugeData = new Array(1000000).fill('...');
                setTimeout(() => {
                    console.log('event'); // hugeData 클로저로 잡힘 → 3초 동안 GC 안 됨
                }, 3000);
            }
            createHandler();
            ```
            - 해결 방법:
                - 클로저에서 불필요한 외부 변수 참조 제거
                - null 할당 또는 스코프 제한

    - 전체 요약
        - 렉시컬 vs 다이나믹 스코프: 정의 위치 기준 vs 호출 위치 기준(JS는 렉시컬만 사용)
        - 가비지 컬렉션 시점: 참조 끊긴 객체가 GC 대상
        - 메모리 누수 원인: 전역변수, 클로저, DOM 참조, 이벤트 리스너 등
        - 이벤트 루프 + 클로저 문제: 콜백 실행 전까지 클로저가 데이터 유지 -> 메모리 오래 점유할 가능성 존재

- 클로저 최적화 전략, 메모리 관리 베스트 프랙티스
    - 클로저 최적화 전략
        - 불필요한 참조 최소화
            - 클로저 내부에서 외부 변수 사용을 최소화
            - 불필요한 대용량 객체는 참조하지 않기
            ```js
            function create() {
                const big = new Array(1000000).fill('...');
                return () => {
                    // console.log(big); 필요 없으면 제거
                    console.log('hello'); ✅
                };
            }
            ```

        - 클로저 수명 제한
            - 클로저를 전역이나 장기 참조 변수에 저장하지 않기
            - 필요 시 명시적으로 null 할당
            ```js
            let handler = create();
            handler = null; // 참조 해제 → GC 가능
            ```

        - 타이머/이벤트에서 클로저 정리
            - setTimeout, setInterval, addEventListener 안에 클로저가 있을 경우
                - → 실행 후 null 처리 또는 clearTimeout / removeEventListener
                ```js
                const id = setTimeout(() => {
                    // 클로저 내부 참조 정리
                }, 3000);
                clearTimeout(id);
                ```

    - JavaScript 메모리 관리 베스트 프랙티스
        - 전역 변수 최소화
            - 전역에 변수를 선언하면 앱이 종료될 때까지 GC 대상에서 제외
            - let, const, 모듈 범위로 스코프 제한

        - DOM 요소 참조 시 정리 필수
            - 제거된 DOM을 여전히 코드에서 참조하면 메모리 누수 발생
            - 이벤트 핸들러도 함께 해제
            ```js
            const el = document.getElementById('btn');
            function handleClick() { ... }

            el.addEventListener('click', handleClick);

            // 제거 시
            el.removeEventListener('click', handleClick);
            ```

        - 클로저 내부 변수와 타이머 정리
            - setInterval은 특히 주의: 자동 반복되며 클로저 내 변수 계속 참조
            - 컴포넌트 언마운트 시 반드시 clear

        - 객체 캐시 또는 Map은 WeakMap 사용 고려
            - 참조 해제 자동화, GC 친화적
            ```js
            const wm = new WeakMap();
            wm.set(obj, 'value'); // obj가 사라지면 자동 GC
            ```

        - 메모리 릭 감지 툴 사용
            - DevTools → Performance 탭, Heap Snapshot 활용
            - console.profile() → GC 후에도 살아 있는 객체 추적 가능

    - 전체 요약 정리
        - 클로저 참조 최소화: 메모리 점유 줄이기
        - 타이머/리스너 정리: 참조 유지 방지
        - WeakMap 사용: 자동 해제 가능한 키-값 저장
        - 전역 변수 지양: 수명 통제 불가능한 참조 방지
        - DevTool 활용: 누수 진단 및 객체 생명 주기 분석

- JavaScript에서 arguments 객체 동작 원리
    - 정의: 함수 내부에서 사용 가능한 유사 배열 객체로, 모든 인자 목록을 담고 있음
    - 특징:
        - 배열처럼 생겼지만 진짜 배열은 아님 (map, filter 등 사용 불가)
        - ES5 이하에서 주로 사용
        - 화살표 함수에는 존재하지 않음
        - ES6 이후엔 ...rest로 대체하는 것이 일반적
    - 예제
        ```js
        function sum() {
            let total = 0;
            for (let i = 0; i < arguments.length; i++) {
                total += arguments[i];
            }
            return total;
        }
        sum(1, 2, 3); // 6
        ```
    - 요약: arguments는 함수 인자 전체를 담는 옛 방식 유사 배열 객체


- JavaScript에서 use strict의 역할
    - 정의: "use strict"는 ES5에서 도입된 엄격 모드 선언
    - 역할 및 효과:
        - 암묵적 전역 변수 선언 방지
        - 중복된 파라미터 금지
        - 삭제 불가능한 속성 삭제 차단
        - this가 undefined인 경우 오류 발생 (예: 일반 함수에서의 this)
        - 보안성과 오류 예방에 도움
    - 예제
        ```js
        "use strict";

        x = 10; // ReferenceError: x is not defined
        ```
    - 요약: "use strict"는 코드를 더 엄격하고 안전하게 실행하는 개발자 보호 모드

- JavaScript에서 함수형 프로그래밍을 적용하는 방법
    - 정의: 순수 함수 + 불변성 유지 + 고차 함수 사용을 중심으로 동작하는 프로그래밍 스타일
    - 핵심 원칙:
        - 순수 함수: 같은 입력 → 같은 출력, 부작용 없음
        - 불변 데이터: 원본 데이터 변경 없이 새로운 값 생성
        - 고차 함수: 함수를 인자로 받거나 함수를 반환하는 함수
    - 예제
        ```js
        // 순수 함수
        const add = (a, b) => a + b;

        // 불변 데이터
        const arr = [1, 2];
        const newArr = [...arr, 3]; // 원본 수정 안 함

        // 고차 함수
        const twice = fn => x => fn(fn(x));
        ```
    - 실무 적용:
        - map, filter, reduce 활용
        - lodash/fp, Ramda 같은 라이브러리 사용
        - 상태 변경은 복사본으로 처리

    - 요약: 함수형 프로그래밍은 순수성과 예측 가능성을 바탕으로 버그를 줄이고 테스트 용이성을 높임

- 순수 함수 vs 비순수 함수, 고차 함수의 활용, 불변성 유지 방법
    - 순수 함수 vs 비순수 함수
        - 순수 함수 (Pure Function)
            - 특징:
                - 동일한 입력 → 항상 동일한 출력
                - 외부 상태 변경 없음 (부작용 없음)
                - 내부에서 외부 변수에 영향 주지 않음
            - 예제:
                ```js
                const add = (a, b) => a + b;
                ```
        - 비순수 함수 (Impure Function)
            - 특징:
                - 실행 시마다 결과가 달라질 수 있음 (ex. Date.now(), Math.random())
                - 외부 상태를 읽거나 변경함 → 사이드 이펙트 발생
            - 예제:
                ```js
                let count = 0;
                function increase() {
                    return ++count;
                }
                ```
        - 요약:
            - 순수 함수는 예측 가능하고 테스트 용이
            - 비순수 함수는 상태 의존 → 디버깅 어려움

    - 고차 함수(Higher-Order Function)의 활용
        - 정의: 함수를 인자로 받거나 함수를 반환하는 함수
        - 대표 활용 예시
            - 배열 메서드: map, filter, reduce 등
                ```js
                [1, 2, 3].map(x => x * 2); // [2, 4, 6]
                ```
            - 함수 생성기
                ```js
                const multiplyBy = factor => x => x * factor;
                const double = multiplyBy(2);
                double(3); // 6
                ```
            - 로직 캡슐화
                ```js
                function withLogging(fn) {
                    return function (...args) {
                        console.log('call with', args);
                        return fn(...args);
                    };
                }
                ```
        - 요약: 고차 함수는 재사용성 높이고 로직을 추상화하는 데 유용함

    - 불변성 유지 방법
        - 정의: 원본 데이터를 변경하지 않고 복사하여 새로운 값 생성
        - 이유: 예측 가능한 상태 변경, 디버깅 용이, 버그 감소
        - 객체/배열 복사 방법
            - 스프레드 연산자
                ```js
                const obj1 = { a: 1 };
                const obj2 = { ...obj1, b: 2 }; // obj1은 변경되지 않음
                ```

            - Object.assign
                ```js
                const obj2 = Object.assign({}, obj1, { b: 2 });
                ```

            - 배열 조작
                ```js
                const arr = [1, 2];
                const newArr = [...arr, 3]; // [1, 2, 3]
                ```

            - 라이브러리 활용
                - immer, immutable.js 등으로 복잡한 구조도 불변 처리 가능
                - 요약: 불변성은 직접 수정 대신 복사 후 변경이 원칙
                    - → 상태 관리 라이브러리(Redux 등)에서 필수 개념

- JavaScript에서 setTimeout(fn, 0) 동작 원리
    - 정의: 0ms 후에 콜백 함수를 실행하라는 요청
    - 오해 주의: 즉시 실행이 아님 → 최소 지연 시간, 이벤트 루프(Task Queue)에 등록
    - 예제
        ```js
        console.log('start');
        setTimeout(() => console.log('timeout'), 0);
        console.log('end');

        // 출력 순서: start → end → timeout
        ```
    - 이유: setTimeout 콜백은 Call Stack이 비워진 후 실행, 최소 4ms~ 정도 실제 지연 가능
    - 요약: setTimeout(fn, 0)은 “다음 틱에 실행” 요청하는 방식 → 비동기 처리 예약용

- JavaScript에서 Event Delegation(이벤트 위임)
    - 정의: 자식 요소 각각에 이벤트를 등록하지 않고, 부모 요소에 이벤트를 위임해서 처리하는 방식
    - 원리: 이벤트는 버블링(Bubbling)을 통해 상위로 전파됨
    - 활용 이유:
        - 동적 요소에도 이벤트 자동 적용
        - 이벤트 리스너 수 감소 → 성능 향상
    - 예제
        ```js
        document.getElementById('list').addEventListener('click', e => {
            if (e.target.tagName === 'LI') {
                console.log('클릭된 항목:', e.target.textContent);
            }
        });
        ```
    - 요약: 이벤트 위임은 부모 한 곳에서 자식 이벤트를 관리하는 효율적 패턴

- JavaScript에서 this가 동적으로 바뀌는 경우/시점
    - 동적 바인딩 개념: 
        - 함수 호출 방식에 따라 this가 다르게 결정되는 것

    - 주요 동적 바인딩 상황
        - 일반 함수 호출
            - → this는 window (strict 모드에선 undefined)

        - 메서드 호출
            - → 호출한 객체가 this

        - call, apply, bind 사용
            - → 명시적으로 this 지정

        - 이벤트 핸들러에서
            - → DOM 요소가 this
            - (단, 화살표 함수는 예외 → 상위 스코프의 this 유지)

        - setTimeout, setInterval 안에서
            - → 일반 함수면 this는 전역 (화살표 함수 쓰면 외부 this 유지)
    - 예제
        ```js
        const obj = {
            val: 1,
            show: function () {
                setTimeout(function () {
                    console.log(this.val); // undefined
                }, 0);

                setTimeout(() => {
                    console.log(this.val); // 1 (렉시컬 this)
                }, 0);
            }
        };
        obj.show();
        ```
    - 요약: this는 함수가 어떻게 호출됐는지에 따라 바뀌며, 화살표 함수는 예외적으로 정적 바인딩을 사용

- JavaScript에서 비동기 프로그래밍을 다루는 방법
    - 콜백 (Callback)
        - 가장 기초적인 방식
        - 단점: 콜백 지옥(callback hell) → 가독성, 에러 처리 어려움
        - 예제:
            ```js
            fs.readFile('file.txt', (err, data) => {
                if (err) return console.error(err);
                console.log(data);
            });
            ```
    - Promise
        - 비동기 작업을 객체로 표현
        - .then() / .catch()로 결과 처리
        - 상태: pending → fulfilled/rejected
        - 예제:
            ```js
            fetch(url)
                .then(res => res.json())
                .catch(err => console.error(err));
            ```
    - async/await
        - Promise를 동기 코드처럼 작성 가능
        - await은 Promise가 해결될 때까지 기다림
        - 에러는 try/catch로 처리
        - 예제:
            ```js
            async function getData() {
                try {
                    const res = await fetch(url);
                    const json = await res.json();
                    console.log(json);
                } catch (e) {
                    console.error(e);
                }
            }
            ```
    - 요약:
        - 콜백 → 오래된 방식
        - Promise → 체이닝, 에러 처리 분리
        - async/await → 가장 가독성 좋고 표준화된 방식

- JavaScript의 Generator 함수와 일반 함수의 차이점
    - 개요
        - Generator 함수: function*으로 선언, yield로 실행 중단 가능
        - 일반 함수: 한 번 호출되면 끝까지 실행됨

    - Generator 특징:
        - lazy evaluation (지연 실행)
        - 이터러블/이터레이터 프로토콜을 따름
        - yield로 중간 값 반환 + 중단
        - next() 호출로 실행을 제어
        - 예제
            ```js
            function* gen() {
                yield 1;
                yield 2;
                yield 3;
            }
            const it = gen();
            console.log(it.next()); // { value: 1, done: false }
            ```
        - 활용 예시:
            - 반복 제어
            - 중단 가능한 상태 머신
            - 비동기 흐름 제어 (과거엔 co 등에서 사용)

        - 요약: Generator는 실행 흐름을 직접 제어하고, 중단/재개 가능한 함수

- JavaScript에서 Symbol 타입 필요성
    - 정의: ES6에서 도입된 고유하고 변경 불가능한 원시 값
    - 용도:
        - 객체 프로퍼티의 고유 키로 사용
            - → 충돌 없는 키 생성 가능
        - 숨겨진 내부 속성 구현
            - → 외부에서 의도치 않게 접근 못 하게 함
        - 내장 심볼 활용 (ex: Symbol.iterator)
    - 예제:
        ```js
        const id = Symbol('id');
        const user = {
            [id]: 123,
            name: 'Tom'
        };
        console.log(user[id]); // 123
        ```

        - 내장 Symbol 예시:
        ```js
        const obj = {
            *[Symbol.iterator]() {
                yield 1;
                yield 2;
            }
        };
        for (const val of obj) console.log(val); // 1, 2
        ```
    - 요약: Symbol은 고유 키, 은닉 속성, 내부 프로토콜 확장에 활용되는 안전한 식별자

- JavaScript에서 garbage collection(가비지 컬렉션)의 동작 방식
    - 정의: 더 이상 도달할 수 없는 객체를 자동으로 메모리에서 제거하는 기능
    - JS는 자동 메모리 관리 언어 → 명시적 free/delete 없음
    - 주요 알고리즘: Mark-and-Sweep
    - 동작 원리
        - 루트 객체(globalThis, window)에서 접근 가능한 값 추적
        - 접근 가능한 객체는 "도달 가능(reachable)"로 표시
        - 그 외 나머지는 GC 대상 → 메모리 해제
        ```js
        let obj = { name: 'A' };
        obj = null; // 이제 참조 없음 → GC 대상
        ```
    - 주의점:
        - 순환 참조라도 외부에서 접근 불가능하면 GC 가능
        - 클로저, 전역 변수, 이벤트 핸들러 참조는 GC 방해 가능

    - 요약:
        - JS의 GC는 도달 불가능한 값만 자동 해제
        - 참조를 잘 끊어줘야 메모리 누수 방지 가능

- JavaScript에서 WeakMap과 WeakSet 사용 시점
    - WeakMap
        - 키 타입: 객체만 가능
        - GC 영향: 키가 더 이상 참조되지 않으면 GC 대상
        - 순회: 불가능 (forEach 등 없음)
    - WeakSet
        - 키 타입: 객체만 가능
        - GC 영향: 값이 더 이상 참조되지 않으면 GC 대상
        - 순회: 불가능
    - 사용 사례
        - DOM 요소를 키로 상태 저장 → 제거되면 자동 해제됨
        - 라이브러리 내부 캐싱, 프라이빗 데이터 저장에 사용
        ```js
        const wm = new WeakMap();
        const el = document.getElementById('btn');
        wm.set(el, { clicked: true });

        // el이 DOM에서 제거되면 자동으로 GC 대상
        ```
    - 요약:
        - WeakMap/WeakSet은 GC 친화적인 구조
        - 임시 객체 상태 저장, 메모리 누수 방지 목적에 사용

- JavaScript에서 Promise.all과 Promise.race의 차이
    - Promise.all
        - 모든 Promise가 성공 시 배열로 결과 반환
        - 하나라도 실패하면 reject
    - Promise.race
        - 가장 먼저 완료되는 프로미스(성공/실패 무관) 반환
        - 가장 빠른 결과에 따라 resolve/reject
    - 예시
        ```js
        const p1 = new Promise(res => setTimeout(() => res(1), 100));
        const p2 = new Promise(res => setTimeout(() => res(2), 200));

        Promise.all([p1, p2]).then(console.log); // [1, 2] (모두 완료 시)
        Promise.race([p1, p2]).then(console.log); // 1 (먼저 끝난 p1)
        ```
    - 요약:
        - all → 모두 성공해야 통과, 실패 하나라도 있으면 reject
        - race → 가장 먼저 끝난 Promise의 결과 반환


- JavaScript에서 옵저버 패턴(Observer Pattern)과 이벤트 기반 프로그래밍의 차이
    - 옵저버 패턴(Observer Pattern)
        - 정의: 한 객체(Subject)의 상태 변화에 따라 등록된 여러 옵저버가 자동으로 알림을 받는 구조
        - 구조 방식: 직접 구독/알림
        - 주요 구성:
            - Subject: 상태를 가진 객체
            - Observer: 변화에 반응하는 객체
            - 예시: RxJS, MutationObserver, Object.observe(폐기됨)
        - 예제
            ```js
            class Subject {
                constructor() {
                    this.observers = [];
                }
                subscribe(fn) { this.observers.push(fn); }
                notify(data) { this.observers.forEach(fn => fn(data)); }
            }
            ```
    - 이벤트 기반 프로그래밍
        - 정의: 특정 이벤트가 발생하면 이벤트 핸들러가 실행되는 구조
        - 구조 방식: 이벤트 발생 후 등록된 핸들러 실행
        - 비동기 처리, UI 반응 등에 적합
        - DOM의 addEventListener, Node.js EventEmitter 등
        - 예제
            ```js
            button.addEventListener('click', () => {
                console.log('Clicked!');
            });
            ```

- TypeScript와 JavaScript의 차이점
    - 자바스크립트
        - 타입 시스템: 동적 타입
        - 실행 환경: 브라우저/Node.js
        - 에러 발견 시점: 런타임
        - 특징: 유연하지만 버그 위험
    - 타입스크립트
        - 타입 시스템: 정적 타입
        - 실행 환경: 트랜스파일 후 JS로 실행
        - 에러 발견 시점: 컴파일 타임
        - 특징: 타입 기반으로 코드 안정성 향상
    - 추가 특징
        - TS는 인터페이스, 제네릭, Enum, 접근 제어자(public/private) 등 OOP 기능 제공
        - JS는 표준 기반 동작, ES6 이후 기능이 많이 고도화됨
    - 요약
        - JS는 실행 중심, TS는 타입 안정성과 생산성 향상용 슈퍼셋 언어

- TypeScript에서 타입 추론(Type Inference)
    - 정의
        - 명시적 타입을 작성하지 않아도 TS 컴파일러가 변수/함수의 타입을 자동으로 추론하는 기능
        - 예제
            ```ts
            let x = 'hello'; // TS는 x를 string으로 추론함
            x = 123; // 오류
            ```
    - 적용되는 곳:
        - 변수 초기화
        - 함수 반환값
        - 매개변수 기본값
        - 제네릭 컨텍스트 등
        ```ts
        function add(a: number, b = 10) {
            return a + b; // 반환 타입은 number로 추론
        }
        ```
    - 요약: 타입 추론은 명시적 타입 없이도 안전한 코드 작성을 가능하게 해주는 TypeScript의 핵심 기능

- TypeScript에서 enum 타입 사용 시점
    - 정의: 의미 있는 이름을 가진 상수 집합을 정의할 수 있는 타입
    - 용도:
        - 상태 값, 카테고리, 모드 등 유한한 값들을 명확하게 표현할 때 사용
        - 가독성과 자동완성 지원에 유리
    - 예제
        ```ts
        enum Direction {
            Up,
            Down,
            Left,
            Right,
        }

        function move(dir: Direction) {
            if (dir === Direction.Left) { ... }
        }
        ```
    - 특징:
        - 기본값은 0부터 시작 (숫자형 enum)
        - 문자열 enum도 가능 → enum Status { OK = 'ok', FAIL = 'fail' }

    - 요약: enum은 의미 있는 상수 집합을 안전하게 정의할 때 사용

- TypeScript에서 interface와 type alias의 차이점
    - interface
        - 주 사용 목적: 객체 구조 정의
        - 확장 방식: extends 사용 가능 (선언 병합 O)
        - 선언 병합: 가능
        - 사용 대상: 객체 타입 전용
    - type alias
        - 주 사용 목적: 다양한 타입 표현 (유니언, 튜플, 함수 등)
        - 확장 방식: &로 조합 (선언 병합 X)
        - 선언 병합: 불가능
        - 사용 대상: 모든 타입 (문자열 리터럴 등 포함)
    - 예제
        ```ts
        // 객체 타입 전용
        interface User {
            id: number;
            name: string;
        }

        // 모든 타입, 문자열 리터럴 등 사용 가능
        type Admin = {
            id: number;
            role: 'admin';
        };
        ```
    - 요약:
        - interface → 객체 구조 위주, 확장성 좋음
        - type → 객체 외 타입 조합도 가능, 유연한 표현에 강함

- TypeScript에서 readonly 키워드 사용 방법
    - 정의: 속성을 읽기 전용으로 만들어 재할당을 방지
    - 적용 대상:
        - 객체 속성
        - 배열 요소
        - 튜플
    - 예제
        ```ts
        interface User {
            readonly id: number;    // 아이디를 readonly로 설정
            name: string;
        }

        const user: User = { id: 1, name: 'Tom' };
        user.id = 2; // 오류, readonly 속성이므로.
        ```
    - 요약: readonly는 불변성 보장과 실수 방지를 위해 사용되는 키워드

- TypeScript에서 typeof, keyof, in 연산자 동작 방법/원리
    - typeof
        - 정의: 값의 타입을 추출하여 타입으로 사용할 수 있게 함
        - 용도: 기존 변수의 타입을 재사용할 때 유용
        - 예제
            ```ts
            const user = { name: 'Tom', age: 30 };
            type User = typeof user; // { name: string; age: number }
            ```

    - keyof
        - 정의: 객체 타입의 모든 키를 문자열 리터럴 유니언으로 반환
        - 예제
            ```ts
            type User = { name: string; age: number };
            type UserKeys = keyof User; // 'name' | 'age'
            ```

    - in
        - 정의: Mapped Type 생성 시 반복적으로 키를 순회할 때 사용
        ```ts
        type User = { name: string; age: number };
        type ReadonlyUser = {
            readonly [K in keyof User]: User[K];
        };
        ```

    - 요약:
        - typeof → 값으로부터 타입 추출
        - keyof → 객체 키 추출
        - in → Mapped Type 루프에 사용

- TypeScript에서 Partial<T>와 Required<T>의 차이
    - Partial<T>: 모든 속성을 optional로 변경
    - Required<T>: 모든 속성을 필수(required)로 변경
    - 예제
        ```ts
        interface User {
            name: string;
            age?: number;
        }

        type A = Partial<User>;  // name?: string, age?: number
        type B = Required<User>; // name: string, age: number
        ```
    - 요약:
        - Partial → 선택적으로 만들고 싶을 때
        - Required → 모든 속성 필수화할 때 사용

- TypeScript에서 함수 오버로딩(Function Overloading) 사용 방법
    - 정의: 하나의 함수에 대해 여러 시그니처(호출 방식)를 선언하여 다양한 인자를 처리할 수 있도록 함
    
    - 사용 방식:
        - 함수 시그니처만 선언
        - 실제 구현부는 하나

    - 예제
        ```ts
        function greet(name: string): string;
        function greet(age: number): string;
        function greet(value: string | number): string {
            if (typeof value === 'string') return `Hello, ${value}`;
            return `You are ${value} years old`;
        }

        greet('Tom');   // OK
        greet(30);      // OK
        ```
    - 주의: 구현부는 모든 시그니처를 커버해야 함 (중요한 포인트)
    - 요약: 함수 오버로딩은 다형성을 지원하며, 사용자에게 명확한 API 제공에 유용

- TypeScript에서 never 타입 사용 시점
    - 정의: 절대 값이 발생할 수 없는 타입
    - 사용 시점:
        - 함수가 항상 오류를 던져서 종료될 때
        - 끝나지 않는 함수 (while(true))
        - 조건 분기 후 도달 불가능한 경우
    - 예제
        ```ts
        function fail(msg: string): never {
            throw new Error(msg);
        }

        function loop(): never {
            while (true) {}
        }

        function check(x: string | number) {
            if (typeof x === 'string') return;
            if (typeof x === 'number') return;
            x; // x는 never로 추론됨
        }
        ```
    - 요약: never는 절대 발생하지 않는 상황을 타입으로 표현할 때 사용됨

- TypeScript에서 unknown과 any의 차이점
    - any
        - 타입 검사 없음, 모든 작업 허용
        - 타입 안전성 매우 낮음
        - 빠르게 넘기거나 외부 데이터 처리 시 사용
    - unknown
        - 타입 검사 있음 (사용 전 타입 좁히기 필요)
        - 타입 안전성 높음
        - 안전하게 알 수 없는 타입 처리 시
    - 예제
        ```ts
        // any 타입
        let val1: any = 'hello';
        val1.toFixed(); // 런타임 에러 발생 가능 (컴파일러 허용)

        // unknown 타입
        let val2: unknown = 'hello';
        // val2.toFixed(); 컴파일 에러, 타입 검사 안했으므로.

        // 타입 좁히기 필수
        if (typeof val2 === 'string') {
            console.log(val2.toUpperCase());
        }
        ```
    - 요약: any는 타입 검사 무시, unknown은 검사 강제 → 더 안전함

- TypeScript에서 extends 키워드 역할
    - 용도:
        - 제네릭 제약 조건 설정
            - → 특정 타입만 허용
        - 조건부 타입 정의
            - → T extends U ? X : Y 형태
    - 예제
        ```ts
        function printLength<T extends { length: number }>(value: T) {
            console.log(value.length);
        }

        type IsString<T> = T extends string ? 'Yes' : 'No';
        type A = IsString<'hi'>; // 'Yes'
        ```
    - 요약: extends는 타입 상속/제한 조건을 지정하는 데 사용됨

- TypeScript에서 interface를 확장하는 방법
    - 방법: extends 키워드로 다른 interface를 확장
    - 예제
        - 여러 개도 가능
            ```ts
            interface Animal {
                name: string;
            }

            interface Dog extends Animal {
                breed: string;
            }

            // Animal, Dog 인터페이스 내 정의된 속성들을 다 사용 가능
            const myDog: Dog = {
                name: 'Max',                // Animal interface
                breed: 'Golden Retriever'   // Dog interface
            };
            ```
        - 선언 병합도 가능: 같은 이름의 interface 여러번 선언 시 자동으로 합쳐짐
            ```ts
            interface User {
                id: number;
            }
            interface User {
                name: string;
            }
            // → User = { id: number; name: string }
            ```
    - 요약: interface는 extends로 구조 확장 가능하며, 선언 병합 지원까지 있음

- TypeScript의 타입 가드 (Type Guard)
    - 정의: 조건문을 통해 변수의 정확한 타입을 좁히는 기술
    - 종류:
        - typeof
        - instanceof
        - 사용자 정의 타입 가드 (is 키워드)
    - 예제
        ```ts
        function isString(val: unknown): val is string {
            return typeof val === 'string';
        }

        function print(val: string | number) {
            if (isString(val)) {
                console.log(val.toUpperCase()); // string으로 좁혀짐
            } else {
                console.log(val.toFixed());     // number
            }
        }
        ```
    - 요약: 타입 가드는 런타임 조건을 이용해 타입을 명확하게 좁히는 기술

- TypeScript의 템플릿 리터럴 타입
    - 정의: 문자열을 조합해서 새로운 문자열 리터럴 타입을 생성하는 문법
        ```ts
        type Color = 'red' | 'blue';
        type Variant = `bg-${Color}`; // 'bg-red' | 'bg-blue'
        ```

    - 활용 예: CSS 클래스, 이벤트 이름 등 고정된 문자열 패턴 타입화
        ```ts
        type Size = 'sm' | 'lg';
        type ClassName = `btn-${Color}-${Size}`;
        // 'btn-red-sm' | 'btn-red-lg' | ...
        ```

    - 요약: 템플릿 리터럴 타입은 문자열 패턴을 정적 타입으로 안전하게 표현
    
- TypeScript에서 Record<T, K> 유틸리티 타입 사용 시점
    - 정의: 키 T에 대해 값이 K인 객체 타입을 생성
    - 문법: Record<Keys, ValueType>
    - 예제
        ```ts
        // id 및 name에 해당하는 값을 string 타입으로 지정
        type User = Record<'id' | 'name', string>;
        // { id: string; name: string }

        type RoleMap = Record<'admin' | 'user', boolean>;
        // { admin: boolean; user: boolean }
        ```
    - 활용 상황:
        - 동일한 타입의 키-값 객체 만들 때
        - Enum 또는 유니언 타입 키 매핑

    - 요약: Record는 키 유니언 타입 기반의 정적 객체 생성에 적합

- TypeScript에서 Pick<T, K>과 Omit<T, K> 동작 원리/방법
    - Pick<T, K>
    - Omit<T, K>
    - 예제
        ```ts
        interface User {
            id: number;
            name: string;
            password: string;
        }

        type PublicUser = Omit<User, 'password'>;
        // { id: number; name: string }

        type BasicInfo = Pick<User, 'id' | 'name'>;
        // { id: number; name: string }
        ```
    - 요약:
        - Pick → 일부 속성만 골라 쓰기
        - Omit → 특정 속성 제외하고 재사용

- TypeScript에서 Mapped Types 정의 및 사용 방법
    - Mapped Types (맵드 타입)
        - 정의: 기존 타입의 키들을 반복적으로 순회하며 새로운 타입 생성
    - 예제
        ```ts
        type ReadonlyUser<T> = {
            readonly [K in keyof T]: T[K];
        };

        type User = { id: number; name: string };
        type ReadonlyUserType = ReadonlyUser<User>;
        // { readonly id: number; readonly name: string }
        ```
    - 요약: Mapped Type은 기존 타입의 구조를 반복 변형할 때 사용됨

- TypeScript에서 Conditional Types(조건부 타입) 동작 방법
    - 정의: T extends U ? X : Y 형식으로 타입을 조건에 따라 분기
    - 예제
        ```ts
        type IsString<T> = T extends string ? 'YES' : 'NO';

        type A = IsString<'hello'>; // 'YES'
        type B = IsString<123>;     // 'NO'
        ```
    - 활용 예:
        - 타입 좁히기, 타입에 따라 다른 구조 지정, 유니언 타입 처리 등
    - 요약: 조건부 타입은 타입 간 분기를 표현하여 타입 레벨 if문 역할을 함

- TypeScript에서 Infer 키워드 역할
    - 정의: 조건부 타입 내에서 타입 일부를 추론할 수 있게 해주는 키워드
    - 예제
        ```ts
        type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

        type A = ReturnType<() => string>; // string
        ```
    - 주요 사용처:
        - 함수 반환 타입 추출
        - Promise 결과 타입 추출
        - 튜플/배열 요소 타입 분리

    - 요약: infer는 조건부 타입 안에서 새로운 타입을 변수처럼 추론할 수 있게 해줌

- TypeScript에서 Discriminated Unions(태그된 유니온 타입) 사용 시점
    - 정의: 공통된 "tag" 속성을 기준으로 여러 타입을 구분하는 유니온
    - 장점: 타입 가드 없이도 switch 문이나 if문으로 타입 좁히기 가능
    - 예제
        ```ts
        type Shape =
            | { kind: 'circle'; radius: number }
            | { kind: 'square'; side: number };

        function area(shape: Shape) {
            switch (shape.kind) {
                case 'circle':
                    return Math.PI * shape.radius ** 2;
                case 'square':
                    return shape.side ** 2;
            }
        }
        ```
    - 요약: Discriminated Union은 공통 속성을 기준으로 안전하게 분기 처리할 수 있는 유니온 타입 설계 패턴

- TypeScript에서 Function Overloading(함수 오버로딩) 정의 방법
    - 정의: 함수 하나에 대해 여러 호출 시그니처를 정의하는 방식
    - 작성법:
        오버로드 시그니처 선언 (하나 이상)
        하나의 실제 구현부 (모든 케이스 처리)
    - 예제
        ```ts
        function greet(name: string): string;
        function greet(age: number): string;
        function greet(value: string | number): string {
            return typeof value === 'string'
                ? `Hello, ${value}`
                : `You are ${value} years old`;
        }

        greet('Tom'); // OK
        greet(30);    // OK
        ```
    - 요약: 오버로드는 다양한 인자 조합에 대해 하나의 함수로 대응할 수 있게 해줌

- TypeScript에서 Indexed Access Types 사용 방법
    - 정의: 객체 타입에서 속성의 타입만 추출하는 문법 (인덱스 접근 타입)
    - 형식: T[K]
    - 예제
        ```ts
        type User = {
            id: number;
            name: string;
        };

        type IdType = User['id']; // number
        ```
    - 활용 예
        - 동적 키 접근
        - 유틸리티 타입 구현 시 (예: Pick<T, K>, Record<K, T[K]>)
    - 요약: Indexed Access는 객체의 속성 타입을 추출하거나 재사용할 때 사용

- TypeScript에서 ReadonlyArray<T>와 Array<T>의 차이점
    - ReadonlyArray<T>
        - 변경 불가 (컴파일 에러)
        - 불변 배열 보장 (안전성 강화)
    - Array<T>
        - push, pop, 변경 가능
        - 일반적인 배열 처리
    - 예제
        ```ts
        const arr: ReadonlyArray<number> = [1, 2, 3];
        arr.push(4); // 오류: Property 'push' does not exist
        ```
    - 요약
        - 요약: ReadonlyArray는 배열을 읽기 전용으로 만들고, 수정 불가능하게 해줌

- TypeScript에서 Module Augmentation
    - 정의: 기존에 정의된 타입/모듈/인터페이스에 새 속성을 추가하거나 재정의하는 방식
    - 주로 사용 시점:
        - 라이브러리 타입 확장 (ex: express, react)
        - 글로벌 타입 보강, 커스텀 메서드 추가
    - 예제
        ```ts
        // express 확장 예시
        declare module 'express' {
            interface Request {
                user?: { id: string };
            }
        }
        ```
    - 요약: Module Augmentation은 외부 모듈의 타입을 안전하게 확장할 수 있게 해주는 기능

- TypeScript에서 Declaration Merging(선언 병합)
    - 정의
        - 동일한 이름의 선언이 여러 개 존재할 경우, TypeScript가 이를 하나로 병합하는 기능.

    - 주요 사용 사례
        - 인터페이스 병합: 동일한 이름의 인터페이스 속성이 합쳐짐
            ```ts
            interface User { name: string; }
            interface User { age: number; }
            // 병합 결과: { name: string; age: number }
            ```
        
        - Namespace + Function/Class 병합: 기능 확장용으로 자주 사용
            ```ts
            function greet() {}
            namespace greet {
                export const version = "1.0";
            }
            ```

        - 활용 예시
            - 라이브러리 확장 시 타입 보완, 전역 객체 확장 등

- JavaScript에서 WeakMap과 Map의 차이점
    - Map
        - 키로 객체 또는 원시값 사용 가능
        - 순회 가능 (forEach, for...of)
        - 강한 참조로 인해 키 객체가 메모리에서 수동으로 제거되기 전까지 유지됨

    - WeakMap
        - 키는 객체만 가능 (원시값은 키로 사용 불가)
        - 순회 불가, size도 없음
        - 키 객체에 대한 약한 참조 → 키 객체가 더 이상 참조되지 않으면 GC에 의해 자동 삭제

    - 주요 목적
        - Map: 일반 데이터 저장 및 순회
        - WeakMap: 메모리 누수 없이 비공개 데이터 저장 (ex: 클래스 private 필드)


- JavaScript에서 WeakSet과 Set의 차이점
    - Set
        - 중복 없는 값 저장 가능
        - 객체와 원시값 모두 저장 가능
        - 순회 가능 (forEach, for...of)
        - size 속성 존재

    - WeakSet
        - 객체만 저장 가능 (원시값은 저장 불가)
        - 순회 불가, size 없음
        - 저장된 객체에 대한 약한 참조 → GC 대상이 되면 자동 제거

    - 사용 목적 차이
        - Set: 일반적인 유일 값 관리
        - WeakSet: 비공개 객체 추적, 메모리 누수 방지

- JavaScript에서 Reflect API의 역할
    - 역할
        - 객체에 대한 내장 동작을 인터셉트하거나 재정의하지 않고 직접 호출할 수 있는 정적 메서드 제공

    - 주요 기능
        - Reflect.get, Reflect.set: 객체 프로퍼티 접근/설정
        - Reflect.has: in 연산자와 유사
        - Reflect.construct: new 연산자 역할
        - Reflect.defineProperty, Reflect.deleteProperty: 기존 Object API 대체 가능

    - 장점
        - Proxy 핸들러 트랩에서 내부 동작 위임 시 사용
        - 더 일관된 오류 처리 (예: 실패 시 false 반환)

    - 활용 예시
        - Proxy와 함께 복잡한 객체 행위 제어
        - 기존 객체 조작 메서드를 대체하여 통일성 확보

- JavaScript에서 Object.defineProperty() 활용 방법
    - 정의
        - 객체의 속성(property)에 대한 세밀한 설정을 가능하게 하는 메서드.

    - 주요 활용
        - 속성 제어: writable, enumerable, configurable 등 설정 가능
        - Getter/Setter 정의:
            ```js
            Object.defineProperty(obj, 'fullName', {
                get() { return this.first + ' ' + this.last; },
                set(value) { [this.first, this.last] = value.split(' '); }
            });
            ```
        - 불변 속성 설정: writable: false, configurable: false로 읽기 전용 설정 가능
        - 숨김 속성 생성: enumerable: false를 통해 for...in에서 제외
    
    - 실제 사용처
        - 라이브러리 내부 데이터 은닉, 프레임워크 내부 바인딩, 불변 속성 설정 등

- JavaScript에서 JSON.stringify()와 JSON.parse()의 내부 동작 원리
    - 목적
        - JSON.stringify(): JS 객체 → JSON 문자열 변환
        - JSON.parse(): JSON 문자열 → JS 객체 복원

    - stringify() 내부 동작
        - 순환 참조 객체는 TypeError 발생
        - 함수, undefined, symbol 속성은 제거됨
        - 배열에서 undefined는 null로 변환됨
        - 객체에 toJSON() 메서드가 있으면 그 반환값 기준으로 직렬화

    - parse() 내부 동작
        - 문자열을 기반으로 JSON 문법을 파싱
        - 잘못된 JSON 형식이면 SyntaxError 발생

- JavaScript에서 eval() 함수 사용 지양 이유
    - 보안 문제
        - 외부 입력을 그대로 실행 시 XSS 등 치명적인 보안 취약점 유발

    - 성능 문제
        - JS 엔진의 최적화 대상에서 제외되며 실행 속도 저하
        - 정적 분석 불가 → 코드 흐름 추적 어려움

    - 디버깅 어려움
        - 런타임 동적 실행으로 인해 오류 추적, 테스트 어려움

    - 대안
        - JSON.parse(), Function 생성자, 모듈 시스템 등 더 안전한 대안 존재

- JavaScript에서 with 문을 사용하면 발생할 수 있는 문제
    - 스코프 모호성
        - 내부에서 선언된 변수의 스코프가 예측 불가능해짐
        - 어떤 객체의 속성을 참조하는지 코드만 보고 명확히 판단하기 어려움

    - 최적화 방해
        - JS 엔진이 최적화 루틴을 적용하지 못함 → 성능 저하

    - 표준화 문제
        - strict mode에서 사용 불가능
        - 최신 코드에서는 거의 사용되지 않으며, 비추천

- JavaScript에서 try...catch의 성능 오버헤드 최적화 방식
    - 오버헤드 발생 지점
        - 예외가 실제로 발생할 때만 성능 저하가 두드러짐
        - 정상 실행 루틴과 예외 처리 루틴이 분리되면서 엔진 최적화 대상에서 제외됨

    - 최적화 전략
        - 오류 발생이 예상되는 최소 범위에만 try...catch 적용
        - try 블록 내부에는 가능한 한 간단한 로직만 작성
        - 자주 호출되는 핫패스 코드에서는 예외 대신 조건문 기반 오류 처리 선호

- JavaScript에서 document.createElement()와 innerHTML의 성능 차이
    - 개요
        - 둘 다 DOM 요소를 생성하는 방식이지만, 내부 동작 방식이 다름

    - document.createElement()
        - DOM API 기반으로 요소를 직접 생성
        - 속성, 자식 요소 등을 JS 코드로 명확히 제어 가능
        - 보안성 높음 (스크립트 주입 위험 없음)
        - 성능이 우수함 → 특히 복잡한 트리 조작 시 브라우저 최적화 가능

    - innerHTML
        - HTML 파서 기반 문자열 해석
        - 전체 innerHTML 갱신 시 기존 노드 파괴 및 재생성 → 성능 저하 유발 가능
        - XSS 취약점 우려
        - 빠르게 다수의 요소를 렌더링할 때는 초기 성능이 더 나을 수 있음

    - 결론
        - 단순하고 빠른 렌더링: innerHTML
        - 정밀 제어와 반복 DOM 조작: createElement() 추천

- JavaScript에서 ArrayBuffer와 TypedArray 사용 시점
    - ArrayBuffer
        - 원시 이진 데이터 저장용 고정 길이 버퍼
        - 메모리 블록 자체를 표현
        - 아무 타입 정보 없음 → 보기만으로 해석 불가능

    - TypedArray
        - ArrayBuffer를 정수, 부동소수점 등 형식에 맞게 해석하는 뷰
        - 예: Uint8Array, Float32Array, Int16Array 등
        - 성능 최적화된 바이너리 데이터 처리에 적합

    - 사용 예시
        - WebGL, WebAssembly, 파일 I/O, 네트워크 프로토콜, 이미지 처리 등
        - 대용량 이진 데이터 처리 시 필요

- JavaScript에서 Intl 객체 사용 용도
    - 역할
        - 국제화(Internationalization) 지원 (국제화 지원 (i18n)을 위한 표준 API 제공)
        - 브라우저에 내장된 로케일 기반 포맷 처리

    - 기능
        - 날짜/시간 포맷: Intl.DateTimeFormat
        - 숫자/통화 포맷: Intl.NumberFormat
        - 문자열 정렬 기준 (locale-aware): Intl.Collator
        - 언어 리스트: Intl.DisplayNames, Intl.ListFormat
        - 플루럴 룰: Intl.PluralRules
        - 메시지 포맷팅 (ECMA-402 확장): Intl.MessageFormat (라이브러리로 구현)

    - 사용 목적
        - 사용자 지역(locale)에 맞는 표현 제공
        - 복잡한 국제화 요구사항도 간단하게 처리 가능

    - 사용처
        - 다국어 서비스 제공
        - 국가별 날짜·통화 표현 차이 처리

- JavaScript에서 Function.prototype.toString() 사용 시 얻을 수 있는 정보
    - 역할: 함수의 소스 코드(문자열)를 반환
    - 반환 정보
        - 해당 함수의 소스 코드 문자열을 그대로 반환
        - 익명 함수, 화살표 함수, 클래스 메서드 등 모두 포함
    - 사용 목적
        - 디버깅 시 함수 내용 확인
        - 함수 코드 비교 (예: 프록시 감지)
        - 클로저 내부 파악 가능 (일부 경우)
    - 활용 사례
        - 함수 내부 확인 (디버깅, 테스트, 메타프로그래밍)
        - 코드 직렬화(예: 서버-클라이언트 간 함수 전달 시)
        - 함수가 native code인지 감별: function.toString().includes("[native code]")
    - 주의사항
        - 네이티브 함수는 [native code] 반환
        - 악의적 코드 분석에도 사용 가능 → 보안 유의
        - 보안 목적 사용 금지 (코드 유출 위험)
        - 난독화된 코드나 압축된 코드에서는 가독성이 낮음

- JavaScript에서 structuredClone()을 사용할 때의 장점
    - 목적
        - 객체를 깊은 복사(Deep Clone) 하기 위한 표준 내장 함수

    - 장점
        - 깊은 복사 가능: 중첩된 객체, 배열, Map, Set, Date, Blob 등 복사 지원
        - 순환 참조 지원: 순환 참조가 포함된 구조도 안전하게 복사 가능
        - 안전성 보장: JSON.parse(JSON.stringify())로는 처리 불가한 구조도 복사 가능
        - 간결하고 빠름: 별도 라이브러리 없이 브라우저 내장 최적화된 성능

    - 사용 예
        ```js
        const clone = structuredClone(originalObject);
        ```
        
- JavaScript에서 메모리 누수를 방지하는 방법
    - 불필요한 참조 제거
        - 사용이 끝난 객체나 변수는 null 또는 undefined로 명시적으로 참조를 해제.

    - 클로저 주의
        - 클로저(함수안의 함수)가 외부 변수(특히 DOM 객체)를 계속 참조하면 메모리 누수 발생 가능.
        - 함수 내에서만 필요한 변수로 한정하거나, 외부 참조 해제.

    - DOM 요소 정리
        - DOM 요소 제거 시, 관련된 이벤트 리스너, 타이머, 관찰자(observer)도 함께 제거 필요.

    - 전역 변수 남용 금지
        - 전역 스코프에 남아있는 변수는 GC의 대상이 되지 않아 누수 위험 증가.

    - WeakMap / WeakSet 사용
        - 참조된 객체가 사라지면 자동으로 GC 대상이 되도록 도와주는 자료구조 활용.

- JavaScript에서 Garbage Collector(GC)의 동작 방식
    - 참조 카운트 방식
        - 객체가 몇 번 참조되고 있는지 추적하여, 참조 수가 0이면 메모리 해제.

    - 마크 앤 스위프 방식
        - 루트 객체(window 등)에서 시작해 접근 가능한 객체만 남기고, 나머지는 수집.

    - 세대별 GC 전략
        - 새로 생성된 객체는 빠르게 수집(Young Generation), 오래된 객체는 느리게 수집(Old Generation)하여 효율성 증가.

    - V8 엔진 기반 최적화
        - 스카벤지, 마크-컴팩트, 인크리멘탈 GC 등 다양한 기법으로 처리 성능 향상.

- JavaScript에서 event listener 누수를 방지하는 방법
    - removeEventListener 명확하게 사용
        - DOM 요소 제거 전에 반드시 리스너를 제거하여 메모리 정리.

    - 한 번만 실행되는 리스너
        - { once: true } 옵션을 통해 이벤트가 한 번만 실행되도록 설정.

    - 동일한 참조 유지
        - addEventListener에 등록한 함수와 정확히 동일한 참조로 removeEventListener를 호출해야 정상 작동.

    - SPA에서 라우팅 시 정리
        - 컴포넌트 언마운트 시점에 이벤트 제거 필수 (ex. React의 useEffect cleanup).

    - MutationObserver 활용
        - 동적으로 추가된 요소의 이벤트 리스너 제거 자동화 가능.

- JavaScript에서 모바일 성능 최적화를 위해 고려해야 할 점
    - DOM 조작 최소화
        - DOM 변경은 비용이 크므로 배치 처리하거나 Virtual DOM으로 관리.

    - 리소스 최적화
        - WebP 이미지, lazy-loading 적용, 불필요한 리소스 지연 로딩 처리.

    - 코드 압축 및 번들링
        - Webpack, Rollup, Terser 등을 이용해 파일 사이즈 축소.

    - 비동기 처리 최적화
        - requestAnimationFrame, requestIdleCallback 사용하여 렌더링 차단 방지.

    - 효율적인 레이아웃 설계
        - 반응형 레이아웃 적용 시 미디어쿼리 과도 사용 방지, CSS 계산 간소화.

    - 메모리 사용량 관리
        - 타이머, 이벤트, 캐시 오브젝트 등을 주기적으로 정리해 리소스 절약.

- JavaScript에서 requestAnimationFrame()과 setTimeout()의 차이
    - 공통점
        - 일정 시간 후 작업을 실행하는 비동기 타이머 함수

    - requestAnimationFrame()
        - 화면 리프레시 주기(보통 60FPS)에 맞춰 콜백 실행
        - 브라우저 최적화에 맞게 렌더링 → 애니메이션에 적합
        - 백그라운드 탭에서 자동 중지되어 CPU 자원 절약

    - setTimeout()
        - 지정한 시간(ms) 후 콜백 실행 보장 없음 (지연 가능성 있음)
        - 브라우저와 무관하게 실행 예약
        - 정밀한 제어 X, 렌더링 프레임과 무관

    - 요약
        - 애니메이션: requestAnimationFrame()
        - 일반 비동기 지연: setTimeout()

- JavaScript에서 MutationObserver와 IntersectionObserver의 차이점
    - MutationObserver
        - DOM 구조의 변화 감지
            - 예: 노드 추가/삭제, 속성 변경, 텍스트 수정
        - DOM 변경을 감시하고 자동 반응하는 데 사용
        - 예시: Virtual DOM 구현, DOM 기반 동기화

    - IntersectionObserver
        - 요소가 뷰포트와 교차되는지 감지 (스크롤 기반)
            - 예: Lazy Load 이미지, 무한 스크롤
        - 브라우저 스크롤 이벤트 감시보다 성능 우수

    - 요약
        - DOM 구조 변경 감지: MutationObserver
        - 화면 노출 여부 감지: IntersectionObserver

- JavaScript에서 BigInt가 필요한 이유
    - 기존 문제점
        - 자바스크립트의 Number는 IEEE-754 64비트 부동소수점
        - 안전 정수 범위: -(2^53 - 1) ~ (2^53 - 1)
        - 그 이상 숫자는 정확도 손실 발생

    - BigInt 도입 이유
        - 정밀한 정수 연산 지원 (무제한 자릿수)
        - 금융, 블록체인, 암호화, 고정밀 데이터 처리에 적합

    - 예시
        ```js
        const big = 1234567890123456789012345678901234567890n;
        ```

- JavaScript에서 documentFragment를 활용하는 이유
    - 개념
        - 메모리에 존재하는 가상 DOM 컨테이너
        - DOM에 삽입되기 전까지는 렌더링되지 않음

    - 장점
        - DOM 조작 최소화로 성능 향상 (Reflow/Repaint 감소)
        - 다수의 요소를 한 번에 삽입 가능
        - 루프 내 DOM 추가 시 효율적

    - 사용 예시
        ```js
        const fragment = document.createDocumentFragment();
        for (let i = 0; i < 1000; i++) {
            const div = document.createElement("div");
            fragment.appendChild(div);
        }
        container.appendChild(fragment); // 단 한 번만 DOM 갱신
        ```

- JavaScript에서 Web Workers를 활용한 성능 최적화 방법
    - 목적
        - 메인 스레드(UI 쓰레드)와 분리된 별도 스레드에서 작업 수행
        - CPU 연산이 많은 작업을 비동기적으로 처리하여 UI 렌더링 지연 방지

    - 활용 사례
        - 대용량 데이터 처리
        - 이미지 필터 처리
        - 암호화/복호화, 파싱
        - WebSocket/데이터 스트림 처리

    - 기본 흐름
        ```js
        const worker = new Worker('worker.js');
        worker.postMessage(data); // 메인 → 워커
        worker.onmessage = (e) => { console.log(e.data); }; // 워커 → 메인
        ```
    
    - 장점
        - UI 블로킹 방지
        - 멀티스레딩처럼 동작하나, 공유 메모리는 없음 (메시지 기반)

- JavaScript에서 debounce()와 throttle()을 내부적으로 구현하는 방법
    - debounce (디바운스)
        - 이벤트가 연속 발생해도 마지막 호출만 실행
        - 주로 검색창, 자동완성 등에 사용
        - 예제
            ```js
            function debounce(fn, delay) {
                let timer;
                return (...args) => {
                    clearTimeout(timer);
                    timer = setTimeout(() => fn(...args), delay);
                };
            }
            ```
    - throttle (스로틀)
        - 일정 시간 간격으로만 함수 실행 허용
        - 스크롤, 리사이즈 등 고빈도 이벤트 최적화에 사용
        - 예제
            ```js
            function throttle(fn, limit) {
                let lastCall = 0;
                return (...args) => {
                    const now = Date.now();
                    if (now - lastCall >= limit) {
                        lastCall = now;
                        fn(...args);
                    }
                };
            }
            ```


- JavaScript에서 async function을 Promise 없이 사용할 수 있는지에 대한 설명
    - 본질
        - async 함수는 무조건 Promise를 반환함
        - (내부에서 return한 값은 자동으로 Promise.resolve(value)로 감싸짐)

    - 의미
        - 사용자는 await 없이 사용 가능하지만, 내부적으로는 항상 Promise

    - 예제
        ```js
        async function foo() {
            return 1;
        }
        foo().then(console.log); // 1 출력됨 (Promise 자동 래핑)
        ```

    - 결론
        - Promise를 명시적으로 작성하지 않아도, async 함수는 항상 Promise를 기반으로 동작함 → 완전한 대체는 불가능

- JavaScript에서 마이크로태스크(microtask)와 매크로태스크(macrotask)의 차이점
    - Microtask
        - 우선순위 높음, 이벤트 루프가 다음 작업으로 넘어가기 전 반드시 처리
        - 예: Promise.then, queueMicrotask, MutationObserver

    - Macrotask
        - 일반적인 비동기 작업 처리
        - 예: setTimeout, setInterval, setImmediate, I/O callbacks

    - 실행 순서
        - 콜스택이 비면 → 마이크로태스크 우선 실행
        - 마이크로태스크가 모두 끝나야 → 다음 매크로태스크로 이동

    - 예시
        ```js
        setTimeout(() => console.log('macrotask'));
        Promise.resolve().then(() => console.log('microtask'));
        // 출력: microtask → macrotask
        ```

- JavaScript에서 Optional Chaining (?.) 연산자
    - 목적
        - 중첩된 객체/속성 접근 시 에러 없이 안전하게 접근

    - 동작 방식
        - 왼쪽 값이 null 또는 undefined인 경우, 오류 대신 undefined 반환

    - 유용한 상황
        - API 응답에서 특정 경로의 데이터가 항상 보장되지 않을 때
        - 복잡한 객체에서 속성 존재 여부를 사전에 검사하지 않고도 안전하게 접근 가능

    - 예시
        ```js
        const user = { profile: null };
        console.log(user.profile?.name); // undefined, 에러 아님
        ```

- JavaScript에서 Nullish Coalescing (??) 연산자 동작 방법
    - 목적
        - null 또는 undefined인 경우에만 우측 값으로 대체

    - 동작 방식
        - false, 0, "" 같은 Falsy 값은 무시하고 유지
        - 오직 null/undefined만 대체

    - 비교: || vs ??
        ```js
        const val = 0;
        console.log(val || 100); // 100
        console.log(val ?? 100); // 0 (false, 0, "" 같은 Falsy 값은 무시하고 유지)
        ```

    - 사용 사례
        - 기본값 설정 시 값이 "0" 또는 빈 문자열일 수도 있을 때 유용

- JavaScript에서 Promise.allSettled()의 사용 사례
    - 동작 방식
        - 모든 Promise가 이행(resolve) 또는 거부(reject) 될 때까지 대기
        - 각 결과를 { status: "fulfilled" | "rejected", value | reason } 형식으로 반환

    - 유용한 경우
        - 여러 비동기 작업 중 성공/실패 여부와 관계없이 모든 결과를 수집해야 할 때
        - 예: 대시보드 API 응답 통합, 파일 업로드 결과 집계

    - 예시
        ```js
        const results = await Promise.allSettled([
            fetch('/a'), fetch('/b'), fetch('/c')
        ]);
        // 개별 성공/실패 여부 확인 가능
        ```

- JavaScript에서 Promise.any()의 동작 방식
    - 목적
        - 여러 Promise 중 하나라도 성공하면 그 값을 반환

    - 동작 방식
        - 가장 먼저 resolve된 Promise의 값을 반환
        - 모든 Promise가 reject될 경우 AggregateError 발생

    - 유용한 상황
        - 여러 서버 중 응답이 가장 빠른 것을 사용하고자 할 때
        - 여러 인증 방법 중 하나만 성공하면 통과시키고 싶을 때

    - 예시
        ```js
        const result = await Promise.any([
            fetchFromCache(), fetchFromCDN(), fetchFromOrigin()
        ]);
        // 가장 빨리 성공한 응답 반환
        ```

- JavaScript에서 WeakRef 사용되는 케이스
    - 개념
        - WeakRef는 객체에 대한 약한 참조(Weak Reference) 를 만들어, GC(가비지 컬렉터)가 해당 객체를 자유롭게 수거할 수 있도록 함

    - 특징
        - 객체가 다른 강한 참조가 없으면 GC에 의해 수거될 수 있음
        - 참조된 객체가 GC로 사라졌을 수 있으므로 사용 전에 살아있는지 확인 필요

    - 사용 시점
        - 캐시 구현 (메모리 부족 시 자동 수거)
        - 큰 객체를 조건부로 유지하고 싶을 때
        - 단, 신중히 사용해야 하며 일반적인 로직에는 부적합

    - 예시
        ```js
        let obj = { data: "hello" };
        const weakRef = new WeakRef(obj);
        obj = null; // GC 수거 대상이 됨

        const deref = weakRef.deref(); // undefined일 수 있음
        ```

- JavaScript에서 Top-Level await
    - 개념
        - 모듈 스코프 최상단에서 await 사용 가능
        - 즉, 함수 내부가 아니어도 await 가능

    - 제한 사항
        - ESM(ECMAScript Module) 환경에서만 사용 가능 (스크립트 type="module" 필요)
        - CommonJS나 브라우저 <script>에서는 사용 불가

    - 사용 이유
        - 초기 데이터 fetch, 설정 파일 로딩 등 비동기 작업 후 모듈 실행이 필요할 때 유용

    - 예시
        ```js
        const data = await fetchData();
        initApp(data);
        ```

- JavaScript에서 Intl.NumberFormat()과 Intl.DateTimeFormat()의 차이
    - 공통점
        - Intl 객체를 활용한 국제화(i18n) 포맷팅 도구
        - 로케일(locale)에 따라 포맷 자동 조정

    - Intl.NumberFormat()
        - 숫자, 통화, 백분율 등의 포맷 제공
        - 예: 통화 기호 붙이기, 천 단위 구분자
        ```js
        new Intl.NumberFormat('ko-KR', { style: 'currency', currency: 'KRW' }).format(10000);
        // "₩10,000"
        ```

    - Intl.DateTimeFormat()
        - 날짜 및 시간 포맷 제공
        - 연/월/일/시/분/초 등의 표시 형식 지정
        ```js
        new Intl.DateTimeFormat('en-US', { dateStyle: 'long' }).format(new Date());
        // "May 14, 2025"
        ```

- JavaScript에서 setTimeout()의 최소 실행 시간이 4ms 이상이 되는 이유
    - 동작 원리
        - HTML5 표준에서 정의: 중첩된 타이머(setTimeout 또는 setInterval)가 5회 이상 중첩될 경우, 최소 대기 시간은 4ms 이상으로 강제됨

    - 이유
        - CPU 자원 남용 방지
        - 무한 루프 형태의 setTimeout 호출 방지
        - 브라우저와 OS가 UI 렌더링 및 이벤트 처리에 시간을 할당하도록 보장

    - 예시
        ```js
        for (let i = 0; i < 10; i++) {
            setTimeout(() => console.log(i), 0); // 실제 실행은 최소 4ms 간격
        }
        ```

- JavaScript에서 import.meta 객체 사용 용도
    - 개념
        - ESM(ECMAScript Modules) 환경에서 사용 가능한 모듈 메타 정보 객체

    - 주요 용도
        - 현재 모듈에 대한 정보를 제공 (위치, 환경 등)

    - 주요 속성 및 예시
        - import.meta.url: 현재 모듈의 절대 URL
        ```js
        console.log(import.meta.url);
        // 예시: "file:///Users/user/project/module.js"
        ```

    - 활용 예시
        - 모듈 기반 앱에서 동적 import 경로 계산
        - WebAssembly, JSON, 이미지 등 동적 자원 로딩 시 유용

- JavaScript에서 modulepreload를 사용할 때의 장점
    - 개념
        - <link rel="modulepreload" href="...">
        - 브라우저가 해당 모듈을 미리 다운로드함

    - 장점
        - JS 모듈 로딩 지연 최소화
            - → 초기 렌더링 성능 개선 (특히 SPA, 코드 스플리팅 구조에서 중요)
        - 병목 없이 병렬 prefetch 가능

    - 사용 예시
        ```html
        <link rel="modulepreload" href="/main.js">
        ```

    - 실무 효과
        - 중요한 모듈을 미리 로드하여 First Input Delay (FID) 감소
        - 번들링 구조를 개선하지 않고도 로딩 속도 향상 가능

- JavaScript에서 Array.prototype.at()의 사용 사례
    - 개념
        - 배열에서 인덱스로 요소를 가져오는 메서드
        - 음수 인덱스도 지원하여 뒤에서 접근 가능

    - 장점
        - array.at(-1)로 마지막 요소 접근 → 가독성 향상
        - array[array.length - 1] 대신 간결한 표현

    - 예시
        ```js
        const arr = [10, 20, 30];
        arr.at(0);   // 10
        arr.at(-1);  // 30
        ```

    - 사용 사례
        - 스택/큐 구조에서 끝 요소 접근
        - 마지막 요소 검사, 페이징 처리 등

- JavaScript에서 Object.hasOwn()은 기존의 Object.prototype.hasOwnProperty()와 어떤 차이가 있는지 설명
    - Object.hasOwn() (ES2022 도입)
        - 순수한 함수 (prototype 오염과 무관)
        - 객체의 자체 속성만 존재 여부 검사

    - 기존 방식
        - obj.hasOwnProperty('key'): 프로토타입 체인에 영향 받음
        - 객체가 hasOwnProperty를 덮어썼거나 prototype이 null인 경우 오류 발생 가능

    - 예시
        ```js
        const obj = Object.create(null);
        obj.foo = 1;

        Object.hasOwn(obj, 'foo'); // true
        obj.hasOwnProperty('foo'); // TypeError (메서드 없음)
        ```

    - 결론
        - Object.hasOwn()은 보다 안전하고 모던한 방식
        - 특히 Object.create(null) 형태의 객체에 유용


- TypeScript에서 type alias와 interface를 혼합 사용 가능성
    - 가능 여부
        - Yes, 혼합 사용 가능하며, 실제로 자주 사용됨

    - 사용 방식
        - type으로 만든 타입을 interface에서 확장 가능
        - interface로 만든 타입을 type에서 조합 가능 (Intersection 사용)

    - 예시
        ```ts
        type Name = { name: string };
        interface Person extends Name {
            age: number;
        }
        type User = Person & { isAdmin: boolean };
        ```

    - 실전 팁
        - interface는 확장(extends) 에 유리하고
        - type은 유니온, 교차 타입 등 복잡한 조합에 유리

- TypeScript에서 extends와 implements의 차이점
    - extends
        - 클래스 → 클래스 상속, 또는 인터페이스/타입 → 인터페이스/타입 확장
        - 속성과 구조를 상속받아 새로운 타입 확장 가능
        ```ts
        interface Animal { name: string }
        interface Dog extends Animal { breed: string }
        ```

    - implements
        - 클래스가 특정 인터페이스의 구조를 구현
        - 실제 동작은 클래스 내부에서 정의
        ```ts
        interface Walkable { walk(): void }
        class Person implements Walkable {
            walk() { console.log("Walking"); }
        }
        ```

    - 핵심 차이
        - extends는 타입 상속
        - implements는 클래스가 타입을 "구현"

- TypeScript에서 mapped types을 사용하여 객체의 속성을 선택적으로 변경하는 방법
    - 개념
        - 객체 타입의 각 속성을 일괄적으로 수정할 수 있는 문법
    - 사용 예시
        - 모든 속성을 optional 로 바꾸기
        ```ts
        type Optional<T> = {
            [K in keyof T]?: T[K];
        };

        type User = { id: number; name: string };
        type OptionalUser = Optional<User>; // { id?: number; name?: string }
        ```
    - 변형 예
        - readonly, nullable, required 등 다양하게 응용 가능

- TypeScript에서 Key Remapping in Mapped Types
    - 개념
        - Mapped Type에서 키 이름 자체를 변경할 수 있는 기능 (TS 4.1+)
    - 문법
        ```ts
        type PrefixKeys<T> = {
            [K in keyof T as `prefix_${string & K}`]: T[K];
        };

        type Data = { name: string; age: number };
        type PrefixedData = PrefixKeys<Data>; 
        // { prefix_name: string; prefix_age: number }
        ```
    - 활용 예
        - API 응답 필드 이름을 변환하거나, 네이밍 규칙 자동 반영할 때 유용
        - 조건부 키 제거, 추가 접두어/접미어 등 고급 타입 조작 가능

- TypeScript에서 Extract<T, U>과 Exclude<T, U>의 차이점
    - 공통점
        - 둘 다 유니온 타입 필터링을 위한 유틸리티 타입

    - Extract<T, U>
        - T에서 U와 공통되는 타입만 추출
        ```ts
        type T = 'a' | 'b' | 'c';
        type U = 'a' | 'b';
        type R = Extract<T, U>; // 'a' | 'b'
        ```

    - Exclude<T, U>
        - T에서 U를 제외한 나머지 타입 반환
        ```ts
        type T = 'a' | 'b' | 'c';
        type U = 'a' | 'b';
        type R = Exclude<T, U>; // 'c'
        ```

    - 요약
        - Extract: 교집합
        - Exclude: 차집합

- TypeScript에서 infer 키워드를 활용한 조건부 타입 예제
    - 개념
        - infer는 타입 추론(inference) 을 조건부 타입 내부에서 수행할 수 있게 함

    - 예시: 배열 요소 타입 추출
        ```ts
        type ElementType<T> = T extends (infer U)[] ? U : T;

        type A = ElementType<number[]>; // number
        type B = ElementType<string>;   // string
        ```

    - 실전 응용
        - 함수 반환 타입 추출, 프로미스 결과 추론 등
        ```ts
        type ReturnTypeOf<T> = T extends (...args: any[]) => infer R ? R : never;
        ```

- TypeScript에서 Template Literal Types을 활용한 동적 타입 생성 방법
    - 개념
        - 문자열 조합을 통한 동적 키/값 생성 가능
    - 예시
        ```ts
        type Lang = 'ko' | 'en';
        type LabelKey = `label_${Lang}`;
        // 결과: 'label_ko' | 'label_en'
        ```
    - 응용 예시: API 응답 키 접두사
        ```ts
        type API<T extends string> = {
            [K in T as `get_${K}`]: () => Promise<any>;
        };

        type Routes = 'user' | 'product';
        type APIMap = API<Routes>;
        // { get_user: () => Promise<any>, get_product: () => Promise<any> }
        ```

- TypeScript에서 readonly 속성
    - 정의
        - readonly는 컴파일 타임에만 재할당 금지를 적용

    - 예시
        ```ts
        interface User {
            readonly name: string;
        }

        const u: User = { name: "John" };
        u.name = "Doe"; // 오류 (컴파일 시점)
        ```

    - 제한 사항
        - 불변성은 얕음(shallow)
        - 중첩된 객체나 배열 내부는 여전히 변경 가능
        ```ts
        interface Config {
            readonly settings: { theme: string };
        }
        const config: Config = { settings: { theme: "dark" } };
        config.settings.theme = "light"; // 가능 (내부는 readonly 아님)
        ```

    - 진정한 불변성?
        - 중첩까지 불변으로 하려면 Readonly<T> 또는 라이브러리 사용 필요 (예: deepFreeze, immer)


- TypeScript에서 never 타입과 unknown 타입이 사용되는 실제 사례
    - never 타입
        - 개념
            - 절대 도달하지 않는 값의 타입
            - 함수가 항상 예외를 던지거나 종료되지 않을 때 반환
        - 사용 사례
            - 안전한 exhaustive check (switch-case 검사)
            ```ts
            function assertNever(value: never): never {
                throw new Error(`Unhandled value: ${value}`);
            }

            type Shape = 'circle' | 'square';
            function getArea(shape: Shape) {
                switch (shape) {
                    case 'circle': return 3.14;
                    case 'square': return 4;
                    default: return assertNever(shape); // 컴파일러가 체크해줌
                }
            }
            ```
    - unknown 타입
        - 개념
            - 모든 타입의 슈퍼 타입 (any와 비슷하나 더 안전)
            - 사용할 때는 타입 좁히기 또는 타입 단언 필요

        - 사용 사례
            - 외부 데이터 또는 사용자 입력 처리 시
            ```ts
            function handleInput(data: unknown) {
                if (typeof data === 'string') {
                    console.log(data.toUpperCase());
                }
            }
            ```

        - 비교
            - any: 아무 제한 없이 사용 가능 (위험)
            - unknown: 먼저 검사 후 사용 가능 → 타입 안정성 확보

- TypeScript에서 Record<K, T>의 사용 사례
    - 개념
        - 객체의 key와 value 타입을 제한하는 유틸리티 타입

    - 일반적인 예시
        ```ts
        type UserRole = 'admin' | 'user' | 'guest';
        type RoleDescriptions = Record<UserRole, string>;

        const descriptions: RoleDescriptions = {
            admin: '관리자',
            user: '일반 사용자',
            guest: '게스트'
        };
        ```

    - 사용 사례
        - enum-like 객체 생성
        - Form 상태 관리, API 응답 매핑
        - 테이블 헤더 → 필드명 매칭

- TypeScript에서 typeof, keyof, in을 함께 사용 가능 여부
    - 가능 여부
        - Yes, 세 가지는 조합하여 고급 타입 생성에 자주 사용됨

    - 사용 예시
        ```ts
        const person = {
            name: "Alice",
            age: 30,
        };

        type Person = typeof person; // { name: string; age: number }
        type PersonKeys = keyof Person; // "name" | "age"

        type OptionalPerson = {
            [K in keyof Person]?: Person[K];
        };
        ```

    - 조합 목적
        - typeof: 값 → 타입 추출
        - keyof: 타입의 키 추출
        - in: 매핑 타입 반복 시 사용

- TypeScript에서 Declaration Merging의 실제 활용 사례
    - 개념
        - 같은 이름의 interface, namespace, function 등 선언이 자동으로 합쳐짐

    - 사용 예: interface 확장
        ```ts
        interface Window {
            appVersion: string;
        }

        window.appVersion = '1.0.0';
        ```

    - 다른 사례: 함수 + namespace
        ```ts
        function greet() {
            console.log("Hello");
        }

        namespace greet {
            export const version = "1.2.3";
        }

        greet(); // "Hello"
        console.log(greet.version); // "1.2.3"
        ```
    - 주요 활용처
        - 글로벌 객체 확장
        - 라이브러리 확장 (ex: Express의 Request, Response 인터페이스 확장)
        - 모듈 보강

- TypeScript에서 Module Augmentation을 사용해야 하는 경우
    - 정의
        - Module Augmentation은 기존 모듈(또는 타입)에 새로운 속성이나 타입을 추가하거나 확장할 때 사용하는 기능

    - 사용해야 하는 경우
        - 외부 라이브러리의 타입에 커스텀 속성을 추가할 때 (예: express.Request에 user 객체 추가)
        - 선언 병합(declaration merging)이 필요한 상황 (ex. 전역 객체 확장)
        - 이미 정의된 모듈을 로컬 컨텍스트에 맞게 보완하거나 타입 정의를 덮어써야 할 때

    - 예시
        ```ts
        // express 확장 예시
        declare module 'express' {
            export interface Request {
                user?: MyCustomUser;
            }
        }
        ```

- TypeScript에서 Tuple Types과 Variadic Tuple Types의 차이점
    - Tuple Types
        - 고정된 순서와 길이를 가지는 배열 타입
        - 각 인덱스의 타입이 다를 수 있음
        ```ts
        type Example = [string, number]; // 길이 2, 첫 번째는 string, 두 번째는 number
        ```

    - Variadic Tuple Types
        - 가변 길이의 튜플을 표현할 수 있음
        - 타입 추론 및 재사용성이 뛰어나고, 주로 제네릭과 함께 사용됨
        ```ts
        type Prepend<T, U extends any[]> = [T, ...U];
        type Example = Prepend<string, [number, boolean]>; // [string, number, boolean]
        ```

    - 차이점 요약
        - Tuple Types: 정해진 길이와 타입
        - Variadic Tuple Types: 일부 요소만 고정하고 나머지는 가변 가능 (Spread 문법 사용)

- TypeScript에서 Intersection Types과 Union Types을 조합하여 활용하는 방법
    - Intersection Types (&)
        - 모든 타입 조건을 동시에 만족해야 함
        - 객체의 속성 결합에 주로 사용
        ```ts
        type A = { name: string };
        type B = { age: number };
        type AB = A & B; // { name: string; age: number }
        ```

    - Union Types (|)
        - 둘 중 하나 이상의 타입만 만족해도 됨
        - 조건 분기, 다형성 처리에 유용
        ```ts
        type Result = string | number;
        ```

    - 조합 활용 예시
        - 조건에 따라 다양한 타입 처리 가능
        - 타입 가드를 통해 정확한 타입 분기 가능
        ```ts
        type Animal = { type: 'cat'; meow: () => void } | { type: 'dog'; bark: () => void };
        function makeSound(a: Animal) {
            if ('meow' in a) {
                a.meow();
            } else {
                a.bark();
            }
        }
        ```

    - 복합 구조 조합
        ```ts
        type Admin = { role: 'admin'; access: string[] };
        type User = { name: string };
        type AdminUser = Admin & User; // 이름과 권한을 모두 가진 사용자
        ```

- TypeScript에서 Assertion Functions 역할
    - 정의
        - Assertion Function은 조건을 만족하지 않으면 예외를 발생시키며, 만족할 경우 타입을 좁혀주는 함수

    - 목적
        - 사용자 정의 타입 가드로 사용됨
        - 특정 조건을 만족하는지 체크하면서 컴파일러에게 타입 보장을 전달함

    - 사용법
        ```ts
        function assertIsString(val: any): asserts val is string {
            if (typeof val !== 'string') {
                throw new Error('Not a string');
            }
        }

        function printLength(input: any) {
            assertIsString(input); // 여기서부터 input은 string으로 인식됨
            console.log(input.length);
        }
        ```

    - 장점
        - 런타임 체크 + 타입 좁히기(Type Narrowing)를 함께 수행
        - 라이브러리 내부에서 예외 처리 + 타입 안전성 향상

- TypeScript에서 satisfies 연산자 유용한 케이스
    - 정의
        - satisfies 연산자는 값의 구조가 특정 타입을 만족하는지 검증하면서, 타입 추론은 값 자체의 리터럴 형태로 유지하도록 함

    - 언제 유용한가
        - 객체 리터럴을 정의할 때, 타입은 제한하고 싶지만 추론된 리터럴 타입을 잃고 싶지 않을 때
        - 타입 체킹은 받고, 자동 완성도 풍부하게 유지하고 싶을 때

    - 예시
        ```ts
        type Person = {
            name: string;
            age: number;
        };

        const user = {
            name: "Alice",
            age: 30,
        } satisfies Person;
        // => user는 Person을 만족하는 구조이지만 name은 "Alice" 리터럴 타입으로 유지됨
        ```

    - 비교: 일반 타입 단언과 차이
        ```ts
        const user1 = { name: "Alice", age: 30 } as Person; // 타입만 Person, 리터럴 타입 정보는 사라짐
        ```

- TypeScript에서 const 어노테이션을 활용한 리터럴 타입 제한
    - 정의
        - as const는 객체, 배열, 문자열 등을 불변 리터럴 타입으로 고정시킴

    - 어디에 사용하나
        - enum-like 상수 정의
        - 리터럴 값 그대로 타입으로 추론되길 원할 때
        - switch문, discriminated union 등에 활용

    - 예시
        ```ts
        const colors = ["red", "green", "blue"] as const;
        // => readonly ["red", "green", "blue"]
        // => 각 요소는 "red" | "green" | "blue"로 추론됨

        type Color = typeof colors[number]; // "red" | "green" | "blue"
        ```

    - 일반 const와 차이
        ```ts
        const colors = ["red", "green", "blue"]; 
        // => string[]으로 추론됨 (리터럴 타입 아님)
        ```


- TypeScript에서 ReadonlyArray<T>와 readonly T[]의 차이
    - 차이점
        - ReadonlyArray<T>
            - 선언방식: 제네릭 타입 사용
            - 사용시점: 인터페이스나 함수 시그니처에 적합
            - 메서드 차이: 변경 불가능한 메서드만 허용
            - 타입 확장성: 명시적 타입 선언 시 더 자주 사용
        - readonly T[]
            - 선언방식: 배열 앞에 readonly 키워드 사용
            - 사용시점: 간단한 배열 선언 시 직관적
            - 메서드 차이: 동일
            - 타입 확장성: 간단한 상황에 적합

    - 예시
        ```ts
        function printList(list: ReadonlyArray<number>) {
            // list.push(1); 불가능
        }

        const data: readonly number[] = [1, 2, 3];
            // data[0] = 5; 수정 불가
        ```

    - 결론
        - 기능적으로는 거의 동일하며,
        - 스타일과 상황에 따라 선택. ReadonlyArray<T>는 명시적이고, readonly T[]는 간단한 선언에 적합.


- TypeScript에서 ModuleSpecifierResolution 설정이 중요한 이유
    - 정의
        - moduleSpecifierResolution은 TypeScript가 import 경로를 어떻게 해석할지를 지정하는 tsconfig.json 옵션

    - 주요 옵션
        - "classic": 예전 TypeScript 방식 (직접 지정된 경로만 탐색)
        - "node": Node.js 방식 (파일 확장자 자동 보완, index.ts 등 탐색)

    - 왜 중요한가
        - import 시 .ts, .js, /index.ts 등 누락된 경로 처리 방법이 달라짐
        - Node.js 환경, bundler 환경(Vite, Webpack 등)과의 호환성 확보
        - 모듈 경로 해석 문제 방지 (ex. "Cannot find module" 오류 방지)

    - 예시
        ```ts
        {
            "compilerOptions": {
                "moduleResolution": "node"
            }
        }
        ```

    - 실전 적용 팁
        - 대부분의 모던 프로젝트에서는 "node" 설정을 사용해야 안정적
        - "paths"와 "baseUrl"과 함께 사용하면 절대경로 import도 쉽게 설정 가능

- TypeScript에서 Intrinsic String Manipulation Types 유용한 케이스
    - 정의
        - Intrinsic String Manipulation Types는 TypeScript가 기본 제공하는 문자열 조작 타입

    - 주요 종류
        - Uppercase<T>: 모든 문자를 대문자로
        - Lowercase<T>: 모든 문자를 소문자로
        - Capitalize<T>: 첫 글자만 대문자
        - Uncapitalize<T>: 첫 글자만 소문자

    - 언제 유용한가
        - 문자열을 기반으로 타입을 동적으로 조합할 때
        - API 응답 타입, 객체 키 타입 등을 가공하여 리턴 타입을 구성할 때
        - 템플릿 리터럴 타입과 함께 유연한 타입 조작이 필요할 때

    - 예시
        ```ts
        type Greeting = 'hello';
        type Shout = Uppercase<Greeting>; // 'HELLO'

        type HttpMethod = 'get' | 'post';
        type HandlerName<T extends string> = `on${Capitalize<T>}`;
        type GetHandler = HandlerName<'get'>; // 'onGet'
        ```

- TypeScript에서 exactOptionalPropertyTypes 옵션을 사용할 때 주의할 점
    - 정의
        - 이 옵션을 켜면 옵셔널 프로퍼티(?)는 undefined가 자동 포함되지 않음
        ```ts
        {
            "compilerOptions": {
                "exactOptionalPropertyTypes": true
            }
        }
        ```

    - 기본 동작
        - 옵션 off: { foo?: string }은 foo가 없거나 string | undefined 가능
        - 옵션 on: { foo?: string }은 foo가 없을 수 있지만 undefined는 직접 명시해야

    - 주의할 점
        - 옵셔널 값에 undefined를 명시적으로 넣을 수 없습니다:
        ```ts
        const obj: { name?: string } = { name: undefined }; // 오류
        ```
        - Partial<T>나 Pick<T>을 사용할 때 타입이 다르게 해석될 수 있어 실행 오류 방지 코드가 더 필요해질 수 있음

    - 언제 사용하나
        - 보다 정확한 타입 설계가 필요한 라이브러리 개발 시
        - 불필요한 undefined 포함을 방지하고자 할 때

- TypeScript에서 noUncheckedIndexedAccess 옵션을 활성화하면 얻을 수 있는 장점
    - 정의
        - 이 옵션을 활성화하면 배열이나 객체에 인덱스로 접근할 때, 해당 값이 존재하지 않을 수 있음을 타입 시스템이 인식
        ```json
        {
            "compilerOptions": {
                "noUncheckedIndexedAccess": true
            }
        }
        ```

    - 기본 동작 (off)
        ```ts
        const user: { [key: string]: string } = {};
        const name = user['name']; // string (위험)
        ```

    - 옵션 on
        ```ts
        const name: string | undefined = user['name']; // 안전
        ```

    - 장점
        - 런타임에서 발생할 수 있는 undefined 오류를 컴파일 타임에 방지
        - 배열/객체 접근 안정성 증가
        - 더 많은 undefined 체크가 강제되어 안전한 코드 작성 가능

    - 주의할 점
        - 기존 코드에서 많은 타입 오류 발생 가능
        - 접근 후 반드시 undefined 체크를 해야 하므로 코드가 장황해질 수 있음

- TypeScript에서 ES Modules과 CommonJS를 함께 사용할 때 주의해야 할 점
    - ESModules (ESM) vs CommonJS (CJS)
        - ESM: import, export
        - CJS: require, module.exports

    - 혼용 시 문제점
        - default import 문제가 자주 발생:
            ```ts
            // CommonJS 모듈
            module.exports = someFunction;

            // ESM import
            import someFunction from './someModule'; // 오류 or undefined
            ```

        - 해결 방법: esModuleInterop, allowSyntheticDefaultImports 옵션 설정 필요
            ```json
            {
                "compilerOptions": {
                    "esModuleInterop": true,
                    "allowSyntheticDefaultImports": true
                }
            }
            ```

    - 주의사항
        - Node.js에서는 type: "module"과 .mjs, .cjs 확장자 구분 필요
        - 번들러(Webpack, Vite 등)에 따라 모듈 시스템 충돌 가능
        - __dirname, require 등 CJS 전용 API는 ESM에서 직접 사용할 수 없음

    - 권장사항
        - 프로젝트 초기부터 하나의 모듈 시스템으로 통일하는 것이 가장 바람직
        - 혼용이 필요하다면 Interop 설정 + 모듈 변환 전략을 명확히 구성할 것

- TypeScript를 JavaScript 프로젝트에 도입할 때 고려해야 할 사항
    - 점진적 마이그레이션 가능성
        - .js → .ts 혹은 .d.ts 기반의 gradual adoption
        - allowJs, checkJs 옵션을 활용하여 JS 코드에서 타입 체크 가능

    - 기존 코드와의 호환성
        - 레거시 코드가 많을수록 .d.ts로 타입 정의 보강이 중요

    - 빌드 파이프라인 정비 필요
        - Babel → TypeScript + tsconfig + bundler(Vite/Webpack 등) 구성 필요

    - 팀의 숙련도와 교육
        - 팀원들의 타입스크립트 이해 수준이 낮다면 학습 리소스 제공이 선행되어야 함

    - 타입 정의 활용 계획
        - 외부 라이브러리 타입 제공 여부 확인 (@types 또는 타입 내장 여부)

    - 도입 목적 명확화
        - 버그 예방? 코드 자동완성 개선? 문서화? → 도입 범위 결정 기준

- TypeScript를 사용하면 발생할 수 있는 오버헤드
    - 컴파일 및 개발 오버헤드
        - 빌드 시간 증가
            - 프로젝트가 커질수록 tsc 컴파일 시간이 늘어남

        - 타입 설계의 복잡성 증가
            - 복잡한 제네릭, 유틸리티 타입 등은 생산성보다 코드 가독성을 해칠 수 있음

        - 정적 타입의 유지보수 비용
            - API 변경 시 타입 수정도 함께 필요 (코드 리팩토링 시 추가 작업 유발)

        - 테스트 코드 중복 가능성
            - 런타임 에러가 줄지만 타입 + 테스트를 모두 작성하는 경우 중복되는 검증 발생

    - 운영 오버헤드는 없음
        - TypeScript는 런타임에 존재하지 않음 → 운영 성능에는 영향 없음

- JavaScript에서 Event Delegation을 활용한 성능 최적화 방법
    - Event Delegation
        - 많은 자식 요소에 각각 이벤트 리스너를 붙이는 대신, 공통 부모에 하나의 이벤트 리스너만 등록하고, 이벤트 버블링을 활용해 처리하는 방식

    - 성능 최적화 포인트
        - 리스너 개수 최소화
            - DOM 요소마다 리스너 붙이면 메모리와 처리 비용 증가 → 부모 한 곳에 위임하여 효율성 확보

        - 동적 요소 처리에 유리
            - 나중에 생성되는 요소도 이벤트 핸들링이 가능

    - 예시
        ```js
        document.getElementById('list').addEventListener('click', function (e) {
            if (e.target.matches('li')) {
                console.log('클릭된 항목:', e.target.textContent);
            }
        });
        ```

    - 주의점
        - 이벤트 타겟이 예상한 요소가 아닐 수 있으므로 e.target, e.currentTarget 체크 필수
        - 버블링이 지원되지 않는 이벤트 (예: blur, focus)에는 부적합

- JavaScript에서 Shadow DOM을 사용하면 얻을 수 있는 이점
    - Shadow DOM
        - 웹 컴포넌트에서 사용하는 캡슐화된 DOM 영역
        외부 CSS, JS로부터 격리된 자체 DOM 트리를 가짐

    - 이점
        - 스타일 캡슐화
            - 외부 스타일 침범 방지, 내부 스타일 누출 방지 → 예측 가능한 UI 구성

        - 컴포넌트 재사용성 향상
            - 자체 스타일/구조 포함된 독립형 UI 모듈로 설계 가능

        - 네이티브 DOM API로 구성
            - React/Vue 없이도 플랫폼 표준으로 모듈화 가능

        - 테스트 용이성
            - 외부 상태에 의존하지 않기 때문에 독립적인 단위 테스트가 쉬움

    - 예시
        ```js
        const shadowHost = document.querySelector('#my-component');
        const shadow = shadowHost.attachShadow({ mode: 'open' });
        shadow.innerHTML = `<style>:host { color: red; }</style><p>Hello!</p>`;
        ```

- JavaScript에서 Service Worker와 Web Worker의 차이점
    - 공통점
        - 둘 다 브라우저에서 메인 스레드와 분리된 백그라운드 스레드에서 실행됨
        - postMessage() 방식으로 메인 스레드와 통신

    - Web Worker
        - 목적: CPU 집약적인 작업(예: 계산, 파싱 등)을 메인 스레드에 영향 없이 수행
        - 수명: 페이지가 열려 있는 동안만 존재
        - 접근 가능: DOM 불가, window 객체 접근 불가
        - 주요 사용 사례:
            - 대용량 연산
            - 이미지/비디오 처리
            - JSON 파싱, 데이터 압축

    - Service Worker
        - 목적: 네트워크 요청 가로채기, 캐싱, 오프라인 경험 제공
        - 수명: 브라우저 전체에서 독립적으로 동작 (페이지 없어도 작동 가능)
        - 접근 가능: Fetch, Cache, Push API, Background Sync 등
        - 주요 사용 사례:
            - PWA (Progressive Web App)
            - 오프라인 페이지 지원
            - 백그라운드 푸시 알림

- JavaScript에서 Lazy Loading을 구현하는 방법
    - Lazy Loading 정의
        - 필요한 시점에 리소스(이미지, 컴포넌트 등)를 지연 로딩하여 초기 로딩 속도와 리소스 사용량을 줄이는 기법

    - 이미지 Lazy Loading
        ```html
        <img src="placeholder.jpg" data-src="real-image.jpg" loading="lazy" />
        ```
        ```js
        <!-- JS로 구현 방법 -->
        const images = document.querySelectorAll('img[data-src]');
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    observer.unobserve(img);
                }
            });
        });
        images.forEach(img => observer.observe(img));
        ```

    - 모듈/컴포넌트 Lazy Loading
        - import() 동적 import 사용 (코드 스플리팅)
            ```js
            button.addEventListener('click', async () => {
                const { heavyFunction } = await import('./heavyModule.js');
                heavyFunction();
            });
            ```

    - React Lazy Loading
        ```tsx
        const LazyComponent = React.lazy(() => import('./MyComponent'));
        ```


- TypeScript에서 strictNullChecks를 활성화하면 코드의 안전성이 어떻게 개선되는가?
    - 기본 동작 (비활성화 시)
        - null 또는 undefined가 모든 타입에 할당 가능
            - → string, number, object 등에도 예외 없이 들어갈 수 있어 런타임 오류 발생 위험

    - 활성화 시 효과
        - null과 undefined는 명시적으로 포함되지 않으면 허용되지 않음
        - 변수, 함수, 객체의 프로퍼티에서 null 체크 없이 접근 시 컴파일 오류
        - 실수 방지: 옵셔널 체이닝(?.), Nullish Coalescing(??) 등 활용 권장

    - 예시
        ```ts
        function greet(name: string | null) {
            console.log(name.toUpperCase()); // 컴파일 에러
        }
        ```

    - 개선 코드
        ```ts
        function greet(name: string | null) {
            if (name) {
                console.log(name.toUpperCase());
            }
        }
        ```

    - 결론
        - strictNullChecks는 널 안정성 향상, 버그 감소, 실행 전 검증에 매우 중요

- TypeScript에서 Partial<T>와 Pick<T, K>을 활용한 실용적인 예제
    - Partial<T>
        - 타입의 모든 속성을 옵셔널로 변경
        ```ts
        type User = { id: number; name: string; email: string };
        type UserUpdate = Partial<User>; 
        // { id?: number; name?: string; email?: string }

        function updateUser(id: number, update: UserUpdate) {
        // 필요한 필드만 전달 가능
        }
        ```

    - Pick<T, K>
        - 타입에서 특정 필드만 선택적으로 추출
        ```ts
        type UserPreview = Pick<User, 'id' | 'name'>; 
        // { id: number; name: string }

        function showUser(user: UserPreview) {
            console.log(user.name);
        }
        ```

    - 실전 예시: API 요청에서 활용
        ```ts
        // PATCH 요청에서 수정 가능한 필드만 허용
        function patchUser(id: number, body: Partial<Pick<User, 'name' | 'email'>>) {
            // name과 email만 수정 허용
        }
        ```

    - 결론
        - Partial → 유연한 업데이트 처리
        - Pick → 제한된 데이터 노출 또는 가공에 유용

- TypeScript에서 Utility Types을 적극적으로 활용하면 얻을 수 있는 장점
    - 주요 장점
        - 코드 재사용성 증가
            - 반복적인 타입 선언 없이 기존 타입을 변형하여 재활용 가능

        - 타입 정확성 향상
            - 유도된 타입을 기반으로 하므로 버그 감소 및 자동 완성 개선

        - 의도 표현 명확화
            - 예: Partial<T>, Readonly<T>를 통해 해당 타입의 사용 의도를 문서화 수준으로 명확하게 표현 가능

        - 유지보수성 향상
            - 타입이 변경되어도 유틸리티 타입을 통해 파생된 타입도 자동으로 추적됨

    - 자주 쓰는 유틸리티 타입
        - Partial<T>, Required<T>, Readonly<T>
        - Pick<T, K>, Omit<T, K>
        - Record<K, T>, Extract<T, U>, Exclude<T, U>

- TypeScript에서 Omit<T, K>과 Exclude<T, U>의 차이
    - Omit<T, K>
        - 객체 타입에서 속성 K를 제거한 타입 반환
        - 내부적으로는 Pick<T, Exclude<keyof T, K>>와 같음
        ```ts
        type Person = { name: string; age: number; gender: string };
        type WithoutAge = Omit<Person, 'age'>; // { name: string; gender: string }
        ```

    - Exclude<T, U>
        - 유니온 타입 T에서 U에 해당하는 타입을 제외
        - 객체 타입이 아니라 단순 타입 필터링에 사용
        ```ts
        type T = 'a' | 'b' | 'c';
        type R = Exclude<T, 'a' | 'b'>; // 'c'
        ```

    - 핵심 차이
        - Omit: 객체 속성 제거용
        - Exclude: 유니온 타입 필터링용

- TypeScript 프로젝트에서 tsconfig.json을 설정할 때 최적의 옵션
    - 필수 설정
        - "strict": true
            - 타입 안전성 극대화 (추론 오류 사전 방지)
        - "target": "ES2020" 이상
            - 최신 문법과 성능 향상 활용
        - "module": "ESNext" or "NodeNext"
            - ESM 기반 모듈 시스템 사용 시 필수
        - "moduleResolution": "node"
            - Node.js 스타일의 모듈 해석
        - "esModuleInterop": true, "allowSyntheticDefaultImports": true
             - CommonJS와의 호환성 확보
        - "skipLibCheck": true
            - 외부 라이브러리의 타입 검사 생략으로 컴파일 속도 향상

    - 권장 추가 옵션
        - "noUnusedLocals": true / "noUnusedParameters": true
            - 불필요한 코드 제거 유도
        - "baseUrl", "paths"
            - 절대경로 import 및 모듈 경로 alias 설정 가능

- JavaScript에서 Polyfill이 필요한 이유와 사용하는 방법
    - 필요 이유
        - 브라우저 간 호환성 확보
            - 최신 ECMAScript 기능이 오래된 브라우저에서 동작하지 않을 수 있음
        - 크로스 브라우징 문제 해결
            - 예: Promise, Array.prototype.includes, Object.entries 등
        - 표준 기능 미지원 환경에서 동일 동작 보장

    - 사용하는 방법
        - 수동 import 방식
            ```js
            import 'core-js/stable';
            import 'regenerator-runtime/runtime';
            ```

        - Babel + Polyfill 자동 삽입
            ```bash
            npm install --save core-js regenerator-runtime
            ```
            ```json
            {
                "presets": [
                    ["@babel/preset-env", {
                    "useBuiltIns": "usage",
                    "corejs": 3
                    }]
                ]
            }
            ```

        - CDN 방식
            ```html
            <script src="https://polyfill.io/v3/polyfill.min.js?features=Promise"></script>
            ```

- JavaScript에서 Deep Clone을 구현하는 다양한 방법
    - ① JSON 방식
        - JSON.stringify() → JSON.parse()로 깊은 복사
        - 간단하고 빠름
        - 함수, Date, Map, Set, undefined, symbol, 순환 참조 등은 지원 불가
        ```js
        const copy = JSON.parse(JSON.stringify(original));
        ```

    - ② 재귀 방식 (직접 구현)
        - 객체와 배열을 재귀적으로 순회하여 복사
        - 순환 참조 처리 시 WeakMap 사용 필요
        ```js
        function deepClone(obj, hash = new WeakMap()) {
            if (obj === null || typeof obj !== "object") return obj;
            if (hash.has(obj)) return hash.get(obj);

            const clone = Array.isArray(obj) ? [] : {};
            hash.set(obj, clone);

            for (const key in obj) {
                clone[key] = deepClone(obj[key], hash);
            }
            return clone;
        }
        ```

    - ③ structuredClone() (최신 브라우저)
        - 내장 API로 깊은 복사 + 순환 참조 지원
        - 가장 안전하고 빠른 방법 중 하나
        ```js
        const copy = structuredClone(original);
        ```

    - ④ 외부 라이브러리 활용
        - 예: Lodash의 _.cloneDeep()
        - 복잡한 객체, 안정성 확보
        ```js
        import cloneDeep from 'lodash/cloneDeep';
        const copy = cloneDeep(original);
        ```

- TypeScript에서 Decorator를 사용하면 얻을 수 있는 이점
    - 개념
        - 클래스, 메서드, 속성, 매개변수에 메타프로그래밍 방식의 부가 기능 주입

    - 주요 이점
        - 반복 로직 추상화
            - 로깅, 캐싱, 인증, 벤치마킹 등의 부가기능 분리 가능

        - 가독성 향상
            - 핵심 로직과 부가 로직을 명확히 분리

        - DI(의존성 주입) 프레임워크 기반 작업 가능
            - NestJS, Angular 등의 주요 프레임워크에서 핵심 기능으로 사용됨

    - 예시
        ```ts
        function Log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
            const original = descriptor.value;
            descriptor.value = function (...args: any[]) {
                console.log(`Call: ${propertyKey} with`, args);
                return original.apply(this, args);
            };
        }
        class UserService {
            @Log
            getUser(id: number) {
                return { id, name: "Alice" };
            }
        }
        ```

- TypeScript에서 Ambient Declarations(.d.ts 파일)의 역할
    - 개념
        - 구현 없이 타입만 정의하는 파일
        - TypeScript가 외부 자바스크립트 코드 또는 라이브러리의 타입 정보를 이해할 수 있게 해줌

    - 사용 목적
        - JS 라이브러리 타입 명세 제공
            - @types/jquery, @types/lodash 등

        - 전역 변수 선언
            - 예: declare const process: any;

        - 타입만 있는 모듈 선언
            ```ts
            // my-lib.d.ts
            declare module 'my-lib' {
                export function doSomething(): void;
            }
            ```
            
    - 사용 시점
        - 타입만 선언하고 실제 구현은 외부에 존재할 때 (JS 라이브러리, Web API 등)