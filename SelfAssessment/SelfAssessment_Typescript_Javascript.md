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

    - 클로저의 핵심 개념
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

- JavaScript에서 garbage collection(가비지 컬렉션)의 동작 방식은?
- JavaScript에서 WeakMap과 WeakSet은 언제 사용하는가?
- JavaScript에서 Promise.all과 Promise.race의 차이는?
- JavaScript에서 옵저버 패턴(Observer Pattern)과 이벤트 기반 프로그래밍의 차이는?
- TypeScript와 JavaScript의 차이점은?
- TypeScript에서 타입 추론(Type Inference)이란?
- TypeScript에서 enum 타입은 언제 사용하는가?
- TypeScript에서 interface와 type alias의 차이는?
- TypeScript에서 readonly 키워드는 어떻게 사용하는가?
- TypeScript에서 typeof, keyof, in 연산자는 어떻게 동작하는가?
- TypeScript에서 Partial<T>와 Required<T>의 차이는?
- TypeScript에서 함수 오버로딩(Function Overloading)은 어떻게 사용하는가?
- TypeScript에서 never 타입은 어떤 경우에 사용되는가?
- TypeScript에서 unknown과 any의 차이점은?
- TypeScript에서 extends 키워드는 어떤 역할을 하는가?
- TypeScript에서 interface를 확장하는 방법은?
- TypeScript에서 Record<T, K> 유틸리티 타입은 언제 사용되는가?
- TypeScript에서 Pick<T, K>과 Omit<T, K>는 어떻게 동작하는가?
- TypeScript에서 Mapped Types은 무엇이며, 어떻게 사용하는가?
- TypeScript에서 Conditional Types(조건부 타입)은 어떻게 동작하는가?
- TypeScript에서 Infer 키워드는 어떤 역할을 하는가?
- TypeScript에서 Discriminated Unions(태그된 유니온 타입)은 언제 사용하는가?
- TypeScript에서 Function Overloading(함수 오버로딩)을 어떻게 정의하는가?
- TypeScript에서 Indexed Access Types는 어떻게 사용하는가?
- TypeScript에서 ReadonlyArray<T>와 Array<T>의 차이점은?
- TypeScript에서 Module Augmentation은 무엇인가?
- TypeScript에서 Declaration Merging(선언 병합)이란?
- JavaScript에서 WeakMap과 Map의 차이점은?
- JavaScript에서 WeakSet과 Set의 차이점은?
- JavaScript에서 Reflect API는 어떤 역할을 하는가?
- JavaScript에서 Object.defineProperty()는 어떻게 활용되는가?
- JavaScript에서 JSON.stringify()와 JSON.parse()의 내부 동작 원리는?
- JavaScript에서 eval() 함수는 왜 사용을 지양해야 하는가?
- JavaScript에서 with 문을 사용하면 발생할 수 있는 문제는?
- JavaScript에서 try...catch의 성능 오버헤드는 어떤 방식으로 최적화할 수 있는가?
- JavaScript에서 document.createElement()와 innerHTML의 성능 차이는?
- JavaScript에서 ArrayBuffer와 TypedArray는 어떤 경우에 사용되는가?
- JavaScript에서 Intl 객체는 어떤 용도로 사용하는가?
- JavaScript에서 Function.prototype.toString()을 사용하면 어떤 정보를 얻을 수 있는가?
- JavaScript에서 structuredClone()을 사용할 때의 장점은?
- JavaScript에서 메모리 누수를 방지하는 방법에는 어떤 것들이 있는가?
- JavaScript에서 **Garbage Collector(GC)**의 동작 방식은?
- JavaScript에서 event listener 누수를 방지하는 방법은?
- JavaScript에서 모바일 성능 최적화를 위해 고려해야 할 점은?
- JavaScript에서 requestAnimationFrame()과 setTimeout()의 차이는?
- JavaScript에서 MutationObserver와 IntersectionObserver의 차이점은?
- JavaScript에서 BigInt가 필요한 이유는?
- JavaScript에서 documentFragment를 활용하는 이유는?
- JavaScript에서 Web Workers를 활용한 성능 최적화 방법은?
- JavaScript에서 debounce()와 throttle()을 내부적으로 구현하는 방법은?
- JavaScript에서 async function을 Promise 없이 사용할 수 있는가?
- JavaScript에서 마이크로태스크(microtask)와 매크로태스크(macrotask)의 차이점은?
- JavaScript에서 Optional Chaining (?.) 연산자는 어떤 경우에 유용한가?
- JavaScript에서 Nullish Coalescing (??) 연산자는 어떻게 동작하는가?
- JavaScript에서 Promise.allSettled()의 사용 사례는?
- JavaScript에서 Promise.any()의 동작 방식은?
- JavaScript에서 WeakRef는 어떤 경우에 사용될 수 있는가?
- JavaScript에서 Top-Level await이란 무엇인가?
- JavaScript에서 Intl.NumberFormat()과 Intl.DateTimeFormat()의 차이는?
- JavaScript에서 setTimeout()의 최소 실행 시간이 4ms 이상이 되는 이유는?
- JavaScript에서 import.meta 객체는 어떤 용도로 사용되는가?
- JavaScript에서 modulepreload를 사용할 때의 장점은?
- JavaScript에서 Array.prototype.at()의 사용 사례는?
- JavaScript에서 Object.hasOwn()은 기존의 Object.prototype.hasOwnProperty()와 어떤 차이가 있는가?
- TypeScript에서 type alias와 interface를 혼합해서 사용할 수 있는가?
- TypeScript에서 extends와 implements의 차이점은?
- TypeScript에서 mapped types을 사용하여 객체의 속성을 선택적으로 변경하는 방법은?
- TypeScript에서 Key Remapping in Mapped Types이란 무엇인가?
- TypeScript에서 Extract<T, U>과 Exclude<T, U>의 차이점은?
- TypeScript에서 infer 키워드를 활용한 조건부 타입 예제는?
- TypeScript에서 Template Literal Types을 활용한 동적 타입 생성 방법은?
- TypeScript에서 readonly 속성이 불변성을 보장하는가?
- TypeScript에서 never 타입과 unknown 타입이 사용되는 실제 사례는?
- TypeScript에서 Record<K, T>의 사용 사례는?
- TypeScript에서 typeof, keyof, in을 함께 사용할 수 있는가?
- TypeScript에서 Declaration Merging의 실제 활용 사례는?
- TypeScript에서 Module Augmentation을 사용해야 하는 경우는?
- TypeScript에서 Tuple Types과 Variadic Tuple Types의 차이점은?
- TypeScript에서 Intersection Types과 Union Types을 조합하여 활용하는 방법은?
- TypeScript에서 Assertion Functions는 어떤 역할을 하는가?
- TypeScript에서 satisfies 연산자는 어떤 경우에 유용한가?
- TypeScript에서 const 어노테이션을 활용한 리터럴 타입 제한은?
- TypeScript에서 ReadonlyArray<T>와 readonly T[]의 차이는?
- TypeScript에서 ModuleSpecifierResolution 설정이 중요한 이유는?
- TypeScript에서 Intrinsic String Manipulation Types은 어떤 경우에 유용한가?
- TypeScript에서 exactOptionalPropertyTypes 옵션을 사용할 때 주의할 점은?
- TypeScript에서 noUncheckedIndexedAccess 옵션을 활성화하면 얻을 수 있는 장점은?
- TypeScript에서 ES Modules과 CommonJS를 함께 사용할 때 주의해야 할 점은?
- TypeScript를 JavaScript 프로젝트에 도입할 때 고려해야 할 사항은?
- TypeScript를 사용하면 발생할 수 있는 오버헤드는 무엇인가?
- JavaScript에서 Event Delegation을 활용한 성능 최적화 방법은?
- JavaScript에서 Shadow DOM을 사용하면 얻을 수 있는 이점은?
- JavaScript에서 Service Worker와 Web Worker의 차이점은?
- JavaScript에서 Lazy Loading을 구현하는 방법은?
- TypeScript에서 strictNullChecks를 활성화하면 코드의 안전성이 어떻게 개선되는가?
- TypeScript에서 Partial<T>와 Pick<T, K>을 활용한 실용적인 예제는?
- TypeScript에서 Utility Types을 적극적으로 활용하면 얻을 수 있는 장점은?
- TypeScript에서 Omit<T, K>과 Exclude<T, U>의 차이는?
- TypeScript 프로젝트에서 tsconfig.json을 설정할 때 최적의 옵션은?
- JavaScript에서 Polyfill이 필요한 이유와 사용하는 방법은?
- JavaScript에서 Deep Clone을 구현하는 다양한 방법은?
- TypeScript에서 Decorator를 사용하면 얻을 수 있는 이점은?
- TypeScript에서 Ambient Declarations(.d.ts 파일)의 역할은?