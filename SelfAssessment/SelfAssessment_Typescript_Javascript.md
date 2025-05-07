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

- TypeScript의 Mapped Types와 Conditional Types은 어떻게 동작하는가?
- JavaScript에서 WeakMap, WeakSet의 사용 사례는?
- JavaScript에서 Proxy와 Reflect API는 어떤 경우에 유용한가?
- TypeScript에서 Utility Types를 활용하여 코드 재사용성을 높이는 방법은?
- JavaScript의 var, let, const의 차이점은?
- ==와 ===의 차이점은?
- JavaScript에서 null과 undefined의 차이는?
- JavaScript에서 typeof 연산자는 어떤 값을 반환하는가?
- JavaScript에서 데이터 타입은 몇 가지가 있는가?
- Hoisting(호이스팅)이란 무엇이며, 어떻게 동작하는가?
- IIFE(즉시 실행 함수, Immediately Invoked Function Expression)의 역할은?
- JavaScript에서 truthy와 falsy 값에는 무엇이 있는가?
- JavaScript에서 deep copy와 shallow copy의 차이는?
- JavaScript에서 Object.freeze(), Object.seal(), Object.assign()의 차이점은?
- JavaScript에서 Object.create(null)를 사용하면 어떤 차이가 있는가?
- JavaScript에서 함수 선언과 함수 표현식의 차이는?
- JavaScript에서 bind, call, apply의 차이점은?
- JavaScript에서 setTimeout과 setInterval은 어떻게 동작하는가?
- JavaScript에서 Map과 Object의 차이점은?
- JavaScript에서 forEach, map, filter, reduce의 차이점은?
- JavaScript에서 동기 코드와 비동기 코드의 차이는?
- JavaScript의 실행 컨텍스트(Execution Context)는 무엇인가?
- JavaScript에서 arguments 객체는 어떻게 동작하는가?
- JavaScript에서 use strict의 역할은?
- JavaScript에서 함수형 프로그래밍을 적용하는 방법은?
- JavaScript에서 setTimeout(fn, 0)은 어떻게 동작하는가?
- JavaScript에서 Event Delegation(이벤트 위임)이란?
- JavaScript에서 this가 동적으로 바뀌는 경우는 언제인가?
- JavaScript에서 비동기 프로그래밍을 다루는 방법은?
- JavaScript의 Generator 함수와 일반 함수의 차이점은?
- JavaScript에서 Symbol 타입은 왜 필요한가?
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