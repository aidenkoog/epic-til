# Concepts, Features, Types and Pros and Cons

Organize concepts, features, types and Pros and Cons

## React.js (+HTML, CSS, Javascript, Typescript)

- React의 핵심 개념은 무엇인가?
  - 간략 개요
    - 컴포넌트: UI를 구성하는 기본 단위
    - JSX: JavaScript에서 XML-like 문법을 사용
    - State: 변경 가능한 컴포넌트의 상태
    - Props: 부모에서 자식으로 전달하는 데이터
    - 이벤트 핸들링: onClick, onChange 등 이벤트 처리
    - Hooks: 함수형 컴포넌트에서 상태 및 라이프사이클 관리
    - Context API: 글로벌 상태 관리 (useContext)
    - Redux: 복잡한 전역 상태 관리 라이브러리
    - React Router: SPA에서 페이지 이동을 위한 라우팅
    - 가상 DOM: 성능 최적화를 위한 업데이트 방식
    - SSR (Next.js): 서버 사이드 렌더링으로 SEO 및 성능 개선

  - 핵심 개념 상세
    - 컴포넌트 (Component)
      - UI를 구성하는 최소 단위
      - 재사용 가능하며, 작은 단위로 나누어 개발 가능
      - 함수형 컴포넌트와 클래스형 컴포넌트가 있으나, 최근에는 함수형 컴포넌트 + 훅(Hooks)이 주로 사용

    - JSX (JavaScript XML)
	    - JavaScript 내에서 XML-like 문법을 사용하여 UI를 정의하는 방식
	    - Babel이 JSX를 React.createElement() 형태로 변환하여 실행
        - const element = <h1>Hello, World!</h1>;
        - const element = React.createElement('h1', null, 'Hello, World!');

    - 상태 (State)
      - 컴포넌트 내부에서 변경될 수 있는 데이터
      - useState 훅을 사용하여 상태를 관리

    - 속성 (Props)
	    - 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달하는 방법.
	    - 읽기 전용(immutable)

    - 이벤트 핸들링 (Event Handling)
	    - React에서는 onClick, onChange 등의 이벤트 핸들러를 사용.

    - 훅 (Hooks)
	    - 클래스형 컴포넌트에서 제공되던 기능(state, lifecycle)을 함수형 컴포넌트에서도 사용할 수 있도록 도와주는 기능
      - 대표적인 훅:
        - useState → 상태 관리
        - useEffect → 컴포넌트 라이프사이클 관리
        - useContext → 전역 상태 관리
        - useReducer → 복잡한 상태 로직 관리
        - useRef → DOM 요소 접근 및 유지

    - 컨텍스트 (Context API)
	    - 전역 상태 관리를 위한 기능
	    - useContext 훅을 활용하여 컴포넌트 트리에서 깊이 전달해야 하는 데이터를 쉽게 공유 가능

    - 리덕스 (Redux)
	    - React에서 상태 관리를 위한 대표적인 라이브러리
      - useReducer와 유사하지만, 전역 상태 관리 기능을 제공

    - React Router
	    - SPA(Single Page Application)에서 페이지 이동을 구현하기 위한 라이브러리
	    - react-router-dom을 사용하여 라우팅 처리 가능.

    - 가상 DOM (Virtual DOM)
	    - React는 변경 사항을 가상 DOM에서 먼저 비교하고, 실제 DOM에 최소한의 변경만 적용하여 성능을 최적화.
	    - diffing algorithm을 사용하여 효율적으로 UI 업데이트.

    - 서버 사이드 렌더링 (SSR)
	    - React는 기본적으로 클라이언트 사이드 렌더링(CSR)을 사용
      - Next.js 같은 프레임워크를 사용하면 서버에서 HTML을 미리 렌더링 가능.

- Virtual DOM 개념 및 동작 방법
  - Virtual DOM 개념
    - Virtual DOM(Virtual Document Object Model, 가상 DOM)
    - 웹 브라우저의 실제 DOM을 직접 조작하는 대신, 가상의 DOM을 사용하여 성능을 최적화하는 기법
    - React, Vue 등 프론트엔드 라이브러리에서 효율적인 렌더링을 위해 사용됨
    - 실제 DOM 조작은 비용이 크므로, Virtual DOM을 활용하여 최소한의 변경만 실제 DOM에 반영

  - Virtual DOM의 동작 방식
    - 핵심 개념
      - 비교(Diffing) → 최소 업데이트(Reconciliation)
    - 동작 방식
      - Initial Render (초기 렌더링)
	      - 앱이 처음 실행될 때, Virtual DOM을 생성하고 이를 실제 DOM에 반영

      - 상태(State) 변경 발생
	      - 사용자의 이벤트(onClick, onChange 등) 또는 데이터 변경(State Update) 발생
	      - React 등에서는 setState(), useState() 등의 함수로 상태를 변경

      - Virtual DOM 생성 및 Diffing (비교)
	      - 변경된 상태를 반영한 새로운 Virtual DOM을 생성
	      - 이전 Virtual DOM과 새로운 Virtual DOM을 비교하는 Diffing Algorithm(차이 비교 알고리즘) 실행

      - 최소한의 변경만 실제 DOM에 적용 (Reconciliation)
	      - 변경된 부분만 찾아서 실제 DOM에 최소한의 업데이트 수행
	      - 전체 DOM을 다시 그리지 않고, 변경된 요소만 효율적으로 수정.

  - Virtual DOM의 동작 과정 예제
    - 예제: 상태(State) 변경 시 Virtual DOM 동작
      ```javascript
      import React, { useState } from "react";

      function Counter() {
        const [count, setCount] = useState(0);

        return (
          <div>
            <h1>현재 카운트: {count}</h1>
            <button onClick={() => setCount(count + 1)}>+1 증가</button>
          </div>
        );
      }
      export default Counter;
      ```
      - 동작 흐름
	      - 초기 렌더링: count = 0 → Virtual DOM 생성 → 실제 DOM 반영
	      - 버튼 클릭(setCount(count + 1)):
	        - count 상태가 1로 변경됨.
	        - 새로운 Virtual DOM을 생성하여 기존 Virtual DOM과 비교(diff).
	        - <h1>현재 카운트: 1</h1> 부분만 변경됨을 감지.
	        - 변경된 부분만 실제 DOM에 반영.

  - Virtual DOM vs 실제 DOM 차이점
    - Virtual DOM은 메모리에 저장된 가상 DOM이며, 실제 DOM은 브라우저가 직접 렌더링하는 DOM

  - Virtual DOM의 장점
    - 성능 최적화: 변경된 부분만 실제 DOM에 반영하여 렌더링 성능 향상
    - 브라우저 렌더링 부하 감소: 직접적인 DOM 변경이 줄어들어 렌더링 속도 개선
    - 코드 유지보수성 증가:	개발자가 직접 DOM을 다루지 않아도 되므로 코드가 간결해짐
    - React, Vue 등의 프레임워크에서 효율적인 UI 업데이트 가능: 상태 기반 UI 관리가 쉬워짐

  - 결론
    - Virtual DOM은 실제 DOM보다 빠른 성능을 제공하며, React/Vue 같은 라이브러리에서 효율적인 UI 업데이트를 위해 사용됨
    - 기존 DOM을 직접 조작하는 것보다 최소한의 변경만 반영하여 렌더링 성능을 최적화
    - Diffing 알고리즘을 활용하여 변경된 요소만 찾아서 업데이트하는 것이 핵심 원리
    - Virtual DOM은 웹 애플리케이션의 성능을 향상시키고, 유지보수를 쉽게 만들어 주는 중요한 기술

- React의 State와 Props의 차이점
  - State (상태)
    - 컴포넌트 내부에서 관리되는 데이터
    - 변경 가능 (mutable) – useState, setState 등을 통해 변경
    - UI 렌더링에 영향을 주는 동적인 값

  - Props (속성)
    - 부모 컴포넌트가 자식 컴포넌트에 전달하는 읽기 전용 데이터
    - 변경 불가 (immutable)
    - 컴포넌트 간 데이터 전달에 사용

  - 핵심 차이
    - State
      - 소유자: 자신 (컴포넌트 내부)
      - 수정 가능성: 가능 (setState)
      - 역할: 동적 상태 관리
    - Props
      - 소유자: 부모 컴포넌트
      - 수정 가능성: 불가능 (읽기 전용)
      - 역할: 외부로부터 받은 설정값

- React에서 상태 관리 방법
  - 기본 방식
    - useState() 훅을 사용하여 함수형 컴포넌트 내에서 상태 관리
      ```jsx
      const [count, setCount] = useState(0);
      ```

  - 고급 상태 관리 방법
    - useReducer
      - 복잡한 상태 로직을 reducer 패턴으로 분리
      - 예: Form 입력, 상태 트랜지션 등

    - Context API
      - 전역 상태 공유가 필요한 경우 사용 (테마, 언어, 로그인 상태 등)

    - 외부 라이브러리
      - Redux, Recoil, Zustand, Jotai 등 상태 관리 전용 솔루션 활용

- Redux와 Context API의 차이점
  - 공통점
    - 둘 다 전역 상태 공유에 사용 가능

  - Context API
    - React 내장 기능 (외부 라이브러리 불필요)
    - 간단한 전역 상태 공유에 적합 (예: 테마, 언어, 사용자 정보)
    - 상태 업데이트 로직이 비교적 단순
    - 단점
      - 상태가 많아지면 렌더링 최적화 어려움
      - 깊은 트리 구조에서는 성능 문제 발생 가능

  - Redux
    - 명확한 구조 (액션 → 리듀서 → 상태)
    - 미들웨어, DevTools, 비동기 처리 등 대규모 앱에 최적화
    - 상태 변경 흐름이 예측 가능하고 디버깅 용이
    - 단점
      - 보일러플레이트 코드 많음 (RTK로 개선됨)
      - 학습 곡선 있음

  - 요약
    - Context API
      - 목적: 간단한 전역 상태 공유
      - 설치 필요 여부: 설치 불필요, 내장
      - 상태 구조: 자유롭고 단순함
      - 렌더링 성능: 재렌더링 최적화 어려움
    - Redux
      - 목적: 복잡하고 규모가 큰 상태 관리
      - 설치 필요 여부: 외부 라이브러리 필요
      - 상태 구조: 정형화된 구조 (액션 -> 리듀서)
      - 렌더링 성능: 미들웨어와 구조로 성능 최적화 가능

- React에서 useEffect 훅의 역할은?
- useMemo와 useCallback의 차이점은?
- React에서 이벤트 핸들링은 어떻게 하는가?

- React의 컴포넌트 라이프사이클을 설명하시오.
- React에서 불필요한 리렌더링을 방지하는 방법은?
- React에서 상태(state)를 변경할 때 주의할 점은?

- React에서 Suspense와 Error Boundary의 차이점은?
- React의 Concurrent Mode란 무엇인가?
- Server-side Rendering(SSR)과 Client-side Rendering(CSR)의 차이점은?

- Next.js를 사용할 때의 장점은?
- React에서 HOC(High Order Component)란?
- React의 Reconciliation 알고리즘이란?

- React에서 상태를 전역으로 관리하는 방법에는 무엇이 있는가?
- useReducer를 사용하는 경우는 언제인가?
- React에서 useRef의 용도는?

- React에서 Portals란 무엇인가?
- React에서 Synthetic Event란?
- React에서 key props가 필요한 이유는?

- React에서 Suspense를 이용해 데이터를 비동기적으로 로딩하는 방법은?
- React의 hydrate 기능은 무엇인가?
- React에서 새로운 상태를 만들지 않고 이전 상태를 직접 변경하면 왜 안 되는가?

- React에서 Lazy Loading을 구현하는 방법은?
- React.memo()를 사용하는 이유는?
- React에서 Fragment란 무엇인가?

- React에서 Error Boundary를 구현하는 방법은?
- React에서 Strict Mode를 사용하는 이유는?
- React에서 Synthetic Events와 Native Events의 차이점은?

- React의 forwardRef를 사용해야 하는 경우는?
- React에서 createContext()와 useContext()의 차이점은?
- React에서 JSX의 역할과 내부적으로 변환되는 방식은?

- React에서 useEffect의 실행 순서는 어떻게 결정되는가?
- React의 useLayoutEffect와 useEffect의 차이점은?
- React에서 Fragment와 div를 사용할 때의 차이점은?

- React에서 이벤트 버블링을 방지하는 방법은?
- React에서 useState의 이전 상태를 기반으로 새 상태를 설정하는 방법은?
- React에서 React.lazy()를 사용하면 어떤 장점이 있는가?

- React에서 Suspense와 Concurrent Mode의 연관성은?
- React에서 setState()가 비동기로 동작하는 이유는?
- React에서 컴포넌트 최적화를 위해 shouldComponentUpdate()를 활용하는 방법은?

- React에서 children props를 활용하는 방식은?
- React에서 상태(state) 변경이 반영되지 않는 이유는?
- React에서 서버와 클라이언트 상태를 함께 관리하는 방법은?

- React에서 Redux Thunk와 Redux Saga의 차이점은?
- React에서 Server Components의 개념과 활용 방법은?
- React에서 hydration이 실패하는 이유는?

- React에서 Suspense로 데이터를 fetch할 때 발생할 수 있는 문제는?
- React의 Concurrent Rendering이 UI 성능에 미치는 영향은?
- React에서 useRef와 useState의 차이점은?

- React에서 useReducer를 사용하는 시나리오는?
- React의 Error Boundaries는 어떤 상황에서 유용한가?
- React에서 CSS-in-JS 라이브러리를 사용하는 이유는?

- React에서 Refs를 활용해 DOM 요소를 조작하는 방법은?
- React에서 비동기 상태 업데이트를 수행하는 방법은?
- React에서 Formik과 React Hook Form의 차이점은?

- React에서 useImperativeHandle()은 어떤 역할을 하는가?
- React에서 이벤트 핸들러를 바인딩하는 올바른 방법은?
- React에서 함수를 props로 전달할 때 발생할 수 있는 문제는?

- React에서 useEffect를 활용한 Debounce 구현 방법은?
- React에서 useState를 배열이나 객체와 함께 사용할 때 주의할 점은?
- React에서 useReducer를 사용하면 성능이 향상되는 이유는?

- React에서 React.createElement()는 언제 사용되는가?
- React에서 이벤트 위임(event delegation)의 원리는?
- React에서 Lazy Loading과 Code Splitting을 적용하는 방법은?

- React에서 클라이언트 상태와 서버 상태의 차이점은?
- React에서 useEffect와 useLayoutEffect를 함께 사용할 때 주의할 점은?
- React에서 Server Components를 활용하면 어떤 이점이 있는가?
- React의 Fiber Reconciliation 알고리즘을 설명하시오.
- React에서 메모리 누수를 방지하는 방법은?
- React에서 hydrate() 함수의 역할은?
- React에서 Recoil과 Redux의 차이점은?
- React에서 Zustand 상태 관리 라이브러리를 사용하는 이유는?
- React에서 Suspense의 대체 기능은?
- React에서 useImperativeHandle을 사용할 때의 장점은?
- React에서 useId() 훅은 언제 유용한가?
- React에서 Error Boundaries의 적용 사례는?
- React에서 Strict Mode가 useEffect에 미치는 영향은?
- React에서 Refs의 활용 사례는?
- React에서 클라이언트 측에서 API 호출을 최적화하는 방법은?
- React에서 Custom Hooks를 만드는 원칙은?
- React에서 Props Drilling이 문제를 일으키는 이유는?
- React에서 React.memo()와 useMemo()의 차이점은?
- React에서 웹 성능을 최적화하는 기법은?
- React에서 useEffect의 Dependency Array의 역할은?
- React에서 useState와 useReducer 중 어떤 경우에 useReducer를 선택하는 것이 좋은가?
- React에서 Strict Mode가 useEffect 내부의 cleanup 함수에 미치는 영향은?
- React에서 Suspense를 활용하여 비동기 데이터를 처리하는 방법은?
- React에서 fetch API와 Axios의 차이점은?
- React에서 렌더링 최적화를 위해 할 수 있는 방법은?
- React에서 React.lazy()와 Loadable Components의 차이점은?
- React에서 useEffect의 cleanup 함수는 언제 호출되는가?
- React에서 useCallback을 사용해야 하는 경우는?
- React에서 Forward Ref를 사용하는 시나리오는?
- React에서 useRef를 활용하여 DOM 요소에 직접 접근하는 방법은?
- React에서 useEffect와 useMemo를 함께 사용할 때 주의할 점은?
- React에서 CSR과 SSR의 성능 차이는 어떤 요소에서 발생하는가?
- React에서 서버 사이드 렌더링 시 데이터 페칭을 어떻게 처리하는가?
- React에서 Next.js의 getStaticProps와 getServerSideProps의 차이점은?
- React에서 getInitialProps와 getServerSideProps의 차이는?
- React에서 Styled Components를 사용할 때의 장점과 단점은?
- React에서 Redux를 사용하면 불필요한 렌더링이 발생할 수 있는 이유는?
- React에서 Redux Persist를 사용하는 이유는?
- React에서 Context API를 사용하면 발생할 수 있는 성능 이슈는?
- React에서 React Query를 사용할 때 얻을 수 있는 이점은?
- React에서 GraphQL을 사용할 때 고려해야 할 점은?
- React에서 상태 관리 라이브러리를 사용하지 않고 상태를 관리하는 방법은?
- React에서 Apollo Client를 사용할 때의 장점은?
- React에서 SWR과 React Query의 차이점은?
- React에서 Suspense를 활용한 데이터 캐싱 기법은?
- React에서 리렌더링을 줄이기 위한 best practice는?
- React에서 Formik과 React Hook Form의 차이점은?
- React에서 Jest와 React Testing Library를 활용한 테스트 방법은?
- React에서 Cypress와 Jest의 차이점은?
- React에서 테스트 코드 작성 시 고려해야 할 사항은?
- React에서 상태 기반 렌더링을 수행할 때 성능을 최적화하는 방법은?
- React에서 ESM과 CommonJS의 차이점은?
- React에서 Webpack과 Vite의 차이점은?
- React에서 Tree Shaking이란 무엇인가?
- React에서 Dynamic Import를 활용한 코드 스플리팅 기법은?
- React에서 Suspense의 기본 개념과 활용 방법은?
- React에서 useDeferredValue()의 활용 사례는?
- React에서 useTransition()을 사용할 때 얻을 수 있는 이점은?
- React에서 useSyncExternalStore()의 역할은?
- React에서 Double Rendering이 발생하는 이유는?
- React에서 Concurrent Mode가 UI 성능에 미치는 영향은?
- React에서 Profiler API를 활용하여 성능 분석을 수행하는 방법은?
- React에서 Strict Mode가 상태 업데이트에 미치는 영향은?
- React에서 Strict Mode를 적용할 때 발생할 수 있는 문제는?
- React에서 Next.js의 Edge Functions을 사용할 때 고려해야 할 사항은?
- React에서 Redux Thunk를 사용하면 얻을 수 있는 장점은?
- React에서 Server Actions를 활용하는 방법은?
- React에서 useOptimistic()을 활용한 낙관적 업데이트 구현 방법은?
- React에서 React Native와 React의 차이점을 비교하시오.
- React에서 Global State를 관리하는 다양한 방법을 설명하시오.
- React에서 Preact를 사용할 때 성능 향상을 기대할 수 있는 이유는?
- React에서 React.memo()를 사용하면 성능이 향상되는 원리는?
- React에서 Suspense를 활용하여 데이터 로딩 경험을 개선하는 방법은?
- React에서 useInsertionEffect()의 역할과 활용 사례는?
- React에서 CSR을 사용할 때의 보안 이슈는?
- React에서 Server Actions와 useMutation()의 차이점은?
- React에서 Error Boundaries를 사용하면 얻을 수 있는 장점은?
- React에서 useEffect와 useLayoutEffect를 함께 사용할 때 주의할 점은?
- React에서 서버 렌더링된 페이지를 클라이언트에서 보강하는 과정은?
- React에서 Refs를 활용한 동적 포커스 처리 방법은?
- React에서 Refs를 활용한 DOM 조작의 장점과 단점은?
- React에서 Custom Hooks를 만들 때 고려해야 할 사항은?
- React에서 API 호출 시 Loading, Success, Error 상태를 관리하는 방법은?
- React에서 Suspense를 활용한 Skeleton UI 구현 방법은?
- React에서 상태 관리의 대표적인 방식 3가지를 설명하시오.
- React에서 useDeferredValue()와 useTransition()의 차이점은?
- React에서 Server Components의 장점과 단점은?
- React에서 GraphQL을 사용할 때 고려해야 할 보안 이슈는?
- React에서 useSyncExternalStore()를 사용해야 하는 경우는?
- React에서 Server Actions의 기본 개념을 설명하시오.
- React에서 useOptimistic()을 사용한 UI 업데이트 최적화 방법은?
- React에서 React.memo()를 올바르게 사용하는 방법은?
- React Server Components(RSC)의 개념과 기존 CSR, SSR과의 차이점은?
- React 19에서 추가된 주요 기능과 성능 최적화 개선 사항은?
- React에서 WASM(WebAssembly)을 활용하는 방법은?
- React에서 Suspense와 Streaming을 결합하여 성능을 최적화하는 방법은?
- React에서 Context API의 성능 이슈를 해결하는 방법은?
- React에서 SWR과 React Query의 내부 작동 방식 차이는?
- React의 Virtual DOM에 대해 설명해주세요.
- React의 상태 관리 방법에 대해 설명해주세요. (Redux, Context API 등)
- React의 Hooks 내부 동작 원리에 대해 설명해주세요.
- React의 Concurrent Mode와 Suspense에 대해 설명해주세요.
- React에서 Concurrent Rendering이 성능 최적화에 어떤 영향을 미치는가?
- React에서 Server Components란 무엇인가?
- React에서 Suspense와 Error Boundary를 활용하는 방법은?
- React에서 React.memo()와 PureComponent의 차이점은?
- React에서 Recoil과 Zustand의 차이점은?
- React에서 PWA(Progressive Web App)를 구현하는 방법은?
- React의 Virtual DOM은 어떻게 동작하는가?
- React에서 useEffect와 useLayoutEffect의 차이는?
- React의 상태 관리 라이브러리(Redux, Recoil, Zustand)를 사용해본 경험이 있는가?
- React에서 context API는 언제 사용하는가?
- React에서 useMemo와 useCallback의 차이는?
- React에서 forwardRef는 언제 사용하는가?
- React의 Server Components와 Client Components의 차이는?
- React에서 Suspense와 Error Boundary는 어떻게 활용하는가?
- React의 Reconciliation 알고리즘은 어떻게 동작하는가?
- React에서 useReducer를 사용하는 이유와 useState와의 차이점은?
- React에서 memoization을 활용하여 성능 최적화하는 방법은?
- Server Components의 동작 방식과 기존 CSR/SSR 방식과의 차이는?
- React에서 Hydration이란 무엇인가?
- React 18의 Automatic Batching이란 무엇이며, 기존 동작 방식과의 차이는?
- React에서 Suspense를 활용한 데이터 패칭 전략을 설명하라.
- React의 JSX는 내부적으로 어떻게 변환되는가?
- React에서 class component와 function component의 차이점은?
- React에서 prop drilling이란 무엇이며, 이를 해결하는 방법은?
- React에서 one-way data binding이란 무엇인가?
- React에서 two-way data binding이 필요할 때는 언제인가?
- React의 reconciliation 알고리즘이 성능 최적화에 어떤 영향을 미치는가?
- React에서 isomorphic rendering이란 무엇이며, 이를 어떻게 구현할 수 있는가?
- React에서 useEffect의 cleanup 함수는 언제 실행되는가?
- React에서 useEffect가 의존성 배열이 비었을 때 어떻게 동작하는가?
- React의 useMemo와 React.memo()의 차이점은?
- React에서 useState와 useRef의 차이점은?
- React에서 useReducer를 사용하면 성능이 향상되는 이유는?
- React에서 useContext를 사용하면 발생할 수 있는 성능 이슈는?
- React에서 useCallback을 사용할 때 주의해야 할 점은?
- React에서 useTransition을 사용할 때의 장점은?
- React의 useDeferredValue와 useTransition의 차이는?
- React의 useSyncExternalStore는 어떤 상황에서 사용하는가?
- React에서 useInsertionEffect()를 사용해야 하는 경우는?
- React에서 React.memo()를 올바르게 사용하는 방법은?
- React에서 React.lazy()를 활용하여 성능을 개선하는 방법은?
- React에서 event delegation을 활용하면 성능이 어떻게 개선되는가?
- React에서 tree shaking이란 무엇이며, 어떻게 적용하는가?
- React에서 code splitting을 적용하는 방법은?
- React에서 React Profiler를 사용하여 성능을 분석하는 방법은?
- React에서 Double Rendering이 발생하는 원인은?
- React에서 Automatic Batching이란 무엇이며, 기존 동작 방식과의 차이는?
- React에서 hydration이 실패하는 이유는?
- React에서 Virtual DOM의 렌더링 성능을 최적화하는 방법은?
- React에서 useReducer와 Redux를 비교했을 때 언제 useReducer를 사용하는 것이 좋은가?
- React에서 Redux Thunk와 Redux Saga의 차이점은?
- React에서 Recoil과 Zustand의 차이점은?
- React에서 zustand를 사용하면 얻을 수 있는 장점은?
- React에서 server state와 client state의 차이는?
- React에서 React Query를 사용하면 어떤 장점이 있는가?
- React에서 SWR과 React Query의 차이점은?
- React에서 Apollo Client를 사용하면 어떤 이점이 있는가?
- React에서 Global State를 관리하는 다양한 방법을 비교하시오.
- React에서 Context API를 사용할 때 발생할 수 있는 성능 이슈는?
- React에서 CSR(Client-Side Rendering)과 SSR(Server-Side Rendering)의 차이점은?
- React에서 Next.js의 getStaticProps와 getServerSideProps의 차이점은?
- React에서 getInitialProps와 getServerSideProps의 차이는?
- React에서 Server Components의 개념과 기존 CSR, SSR과의 차이점은?
- React에서 Streaming SSR이란 무엇이며, 어떻게 활용하는가?
- React에서 Incremental Static Regeneration(ISR)이란 무엇인가?
- React에서 Edge Functions를 사용하면 어떤 장점이 있는가?
- React에서 Server Actions를 활용하는 방법은?
- React에서 fetch API와 Axios의 차이점은?
- React에서 GraphQL을 사용할 때 고려해야 할 점은?
- React에서 Apollo Client를 사용할 때의 장점은?
- React에서 SWR과 React Query의 차이점은?
- React에서 Suspense를 활용한 데이터 캐싱 기법은?
- React에서 API 호출 시 Loading, Success, Error 상태를 관리하는 방법은?
- React에서 낙관적 업데이트(Optimistic UI)를 구현하는 방법은?
- React에서 useOptimistic()을 활용하여 UI 업데이트를 최적화하는 방법은?
- React에서 서버와 클라이언트 상태를 함께 관리하는 방법은?
- React에서 XSS(Cross-Site Scripting)을 방지하는 방법은?
- React에서 CSRF(Cross-Site Request Forgery)를 방지하는 방법은?
- React에서 JWT(JSON Web Token)을 활용한 인증 방식은?
- React에서 OAuth 인증을 구현하는 방법은?
- React에서 CORS 정책을 해결하는 방법은?
- React에서 React Testing Library와 Enzyme의 차이점은?
- React에서 Jest와 Cypress의 차이점은?
- React에서 e2e(end-to-end) 테스트를 수행하는 방법은?
- React 19에서 추가된 주요 기능과 성능 최적화 개선 사항은?
- React에서 WASM(WebAssembly)을 활용하는 방법은?
- React에서 Suspense와 Streaming을 결합하여 성능을 최적화하는 방법은?
- React에서 Context API의 성능 이슈를 해결하는 방법은?
- React에서 Concurrent Rendering이 UI 성능에 미치는 영향은?
- React에서 React Server Components(RSC)의 개념과 기존 CSR, SSR과의 차이점은?
- React에서 Edge Functions를 사용하면 어떤 장점이 있는가?
- React에서 PWA(Progressive Web App)를 구현하는 방법은?
- React에서 Server Actions와 useMutation()의 차이점은?
- React에서 Streaming SSR과 Static Rendering의 차이는?
- React에서 Preact를 사용하면 성능 향상을 기대할 수 있는 이유는?
- React에서 useInsertionEffect()의 역할과 활용 사례는?