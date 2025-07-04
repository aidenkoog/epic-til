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

- React에서 useEffect 훅의 역할
  - 개념
    - 사이드 이펙트(부수 효과)를 처리하기 위한 React 훅
    - 컴포넌트가 렌더링된 이후 실행되는 로직을 정의할 수 있음

  - 주요 용도
    - API 요청, 데이터 fetch
    - DOM 조작, 외부 라이브러리 연동
    - 타이머(setTimeout, setInterval)
    - 구독(subscribe)/정리(cleanup)

  - 기본 구조
    ```jsx
    useEffect(() => {
      // 실행할 로직
      return () => {
        // 컴포넌트 언마운트 시 정리 작업
      };
    }, [deps]); // deps가 변경될 때마다 재실행
    ```

  - 실행 시점
    - 마운트 시 1회 실행 ([])
    - 특정 값 변경 시 재실행 ([value])
    - 리렌더링마다 실행 (생략 시)

- useMemo와 useCallback의 차이점
  - 차이점
    - useMemo
      - 목적: 값을 메모이제이션
      - 반환 값: 계산된 결과값
      - 사용 예시: 무거운 계산식, 파생 상태
    - useCallback
      - 목적: 함수를 메모이제이션
      - 반환 값: 메모이제이션된 함수 참조
      - 사용 예시: 자식 컴포넌트에 함수 props 전달 시

  - 예시: useMemo
    ```js
    const expensiveValue = useMemo(() => computeHeavy(a, b), [a, b]);
    ```

  - 예시: useCallback
    ```js
    const handleClick = useCallback(() => {
      console.log('clicked');
    }, []);
    ```

  - 요약
    - useMemo: 계산 결과 재사용
    - useCallback: 함수 참조 재사용 → 불필요한 리렌더링 방지

- React에서 이벤트 핸들링
  - 기본 원리
    - React는 브라우저의 기본 DOM 이벤트를 추상화한 SyntheticEvent 시스템 사용
    - 브라우저 간 호환성과 성능 최적화를 위해 자체 이벤트 큐를 관리함

  - 사용 예시
    ```jsx
    function MyComponent() {
      const handleClick = (event) => {
        console.log(event.target);
      };

      return <button onClick={handleClick}>Click me</button>;
    }
    ```

  - 특징
    - onClick, onChange, onSubmit 등 이벤트는 camelCase 사용
    - 이벤트 핸들러는 일반적으로 함수로 정의하고 JSX에서 전달

  - 주의점
    - 기본 동작 방지 시 event.preventDefault() 호출 필요
    - 이벤트 객체는 SyntheticEvent → 비동기 핸들링 시 event.persist() 사용하거나 구조분해 할당으로 미리 값 추출 필요


- React의 컴포넌트 라이프사이클
  - 개념
    - 컴포넌트가 화면에 나타나고 유지되며 사라지는 과정을 라이프사이클
    - 함수형 컴포넌트에서는 useEffect() 훅을 통해 라이프사이클 제어

  - 주요 단계 (함수형 기준)
    - Mount:
      - 컴포넌트가 DOM에 처음 렌더링됨 (useEffect(() => {}, []))
    - Update:
      - props 또는 state가 변경되어 재렌더링됨 (useEffect(() => {}, [deps]))
    - Unmount
      - 컴포넌트가 DOM에서 제거됨 (useEffect의 return 함수로 cleanup 처리)

  - 클래스형 컴포넌트 비교
    - componentDidMount → Mount 시
    - componentDidUpdate → Update 시
    - componentWillUnmount → Unmount 시

- React에서 불필요한 리렌더링을 방지하는 방법
  - React.memo()
    - 컴포넌트를 props 변경 시에만 리렌더링 하도록 최적화
    ```jsx
    const MyComponent = React.memo((props) => { /* ... */ });
    ```

  - useMemo / useCallback
    - 계산결과(useMemo)나 함수(useCallback)를 메모이제이션하여 참조값 변경 방지

  - shouldComponentUpdate (클래스형)
    - 조건에 따라 리렌더링 여부 제어

  - key 잘못된 사용 피하기
    - 반복 요소에서 index 사용 시 오히려 불필요한 리렌더링 유발 가능

  - Context 분리
    - Context 는 모든 하위 컴포넌트를 리렌더링 시키므로, 역할별로 Context를 나눔

- React에서 상태(state)를 변경할 때 주의할 점
  - 직접 변경 금지
    - 불변성 유지 필수
      - state.value = 1 → setState({ ...state, value: 1 })

  - 비동기적 처리
    - 상태 업데이트는 즉시 반영되지 않고 비동기적으로 처리됨
    - 상태에 의존하는 연산은 콜백 또는 useEffect를 사용
    ```jsx
    setCount(count + 1); // count는 이전 값일 수 있음
    setCount(prev => prev + 1); // 안전한 방식
    ```

  - 병합 주의
    - 객체/배열 상태 변경 시 spread 연산자 등을 사용해 복사 후 변경
    ```js
    setUser(prev => ({ ...prev, name: 'John' }));
    ```

  - 의존성 배열 누락 주의
    - useEffect, useCallback, useMemo 등에서 상태를 참조하면, 해당 상태는 반드시 의존성 배열에 포함

- React에서 Suspense와 Error Boundary의 차이점
  - Suspense
    - 비동기 로딩 상태 처리를 위한 리액트 기능
    - lazy()로 불러오는 컴포넌트나 data fetching 중 로딩 UI를 보여주기 위함
    - 로딩 fallback UI를 지정할 수 있음
      ```js
      const LazyComponent = React.lazy(() => import('./MyComponent'));

      <Suspense fallback={<div>Loading...</div>}>
        <LazyComponent />
      </Suspense>
      ```

  - Error Boundary
    - 렌더링 중 발생한 JavaScript 에러를 잡아내고, 대체 UI를 보여주는 컴포넌트
    - 앱 전체 크래시 방지, 사용자 친화적 에러 대응 가능
      ```jsx
      class MyErrorBoundary extends React.Component {
        state = { hasError: false };
        static getDerivedStateFromError(error) {
          return { hasError: true };
        }
        componentDidCatch(error, info) {
          logErrorToService(error, info);
        }
        render() {
          return this.state.hasError ? <h1>Something went wrong.</h1> : this.props.children;
        }
      }
      ```

    - 차이점 요약
      - Suspense
        - 처리 대상: 로딩 지연
        - 사용 목적: 비동기 UI 처리
        - 렌더링 영향: fallback UI로 일시 대체
      - Error Boundary
        - 처리 대상: Javascript 런타임 에러
        - 사용 목적: 오류 복구와 대체 UI 제공
        - 렌더링 영향: componentDidCatch로 복구 처리

- React의 Concurrent Mode
  - 개념
    - React가 렌더링을 인터럽트 가능한 작업 단위로 분할하여 처리하는 비동기 렌더링 모드
    - 사용자 인터랙션 중에도 앱이 부드럽게 반응하도록 렌더링 우선순위를 제어함

  - 주요 특징
    - 렌더링 중단/재개 가능 → 장시간 렌더링으로 인한 UI 블로킹 방지
    - useTransition, startTransition, Suspense, deferredValue 등과 연계됨
    - React 18부터 기본 렌더링 엔진에 통합 (부분적 사용 가능)

  - 실전 활용 예
    ```jsx
    const [input, setInput] = useState('');
    const [list, setList] = useState([]);

    const handleChange = (e) => {
      const value = e.target.value;
      setInput(value);
      startTransition(() => {
        setList(expensiveFilter(value));
      });
    };
    ```

- SEO (Search Engine Optimization)
  - SEO 개요
    - 웹 사이트가 검색 엔진에서 더 높은 순위에 노출되도록 최적화하는 과정
    - 특정 키워드를 검색했을 때 사용자들이 원하는 정보를 쉽게 찾을 수 있도록 웹사이트를 최적화하는 것

  - SEO 주요 목표
    - 검색 엔진에서 웹사이트의 가시성 향상
      - 특정 키워드를 검색했을 때 웹사이트가 검색 결과 상위에 노출되도록 함
    - 웹사이트 트래픽 증가
      - 검색 결과 상위에 노출될수록 웹사이트 방문자가 증가
    - 고객 참여도 향상
      - 웹사이트 방문자가 증가하면 자연스럽게 고객 참여도 높아짐
    - 브랜드 신뢰도 향상
      - 검색 결과 상위에 노출되면 브랜드 신뢰도가 높아짐

  - SEO 주요 작업
    - 키워드 연구
      - 사용자들이 어떤 키워드를 검색하는지 분석, 웹사이트의 콘텐츠와 관련된 키워드를 선정
    - 온페이지 SEO
      - 웹사이트 자체를 최적화하는 작업
      - 웹사이트 구조, 제목, 설명, 콘텐츠 등을 개선
    - 오프페이지 SEO
      - 외부 웹사이트에서 웹사이트로 링크를 확보하는 작업
      - 백링크를 구축하여 웹사이트의 신뢰도 증가
    - 기술적 SEO
      - 웹사이트의 기술적인 부분을 최적화하는 작업
      - 웹사이트의 속도, 모바일 친화성 등을 개선
    - 콘텐츠 마케팅
      - 유익하고 매력적인 콘텐츠를 제공하여 사용자들의 웹사이트 방문 유도

  - SEO 중요성
    - 웹사이트를 운영하는 데 있어서 매우 중요한 요소
    - SEO를 통해 웹사이트의 가시성을 높이고, 트래픽을 증가시켜 비즈니스를 성장시키는 데 도움이 됨

- Server-side Rendering(SSR)과 Client-side Rendering(CSR)의 차이점
  - Server-side Rendering (SSR)
    - 초기 HTML을 서버에서 렌더링 → 클라이언트로 전달
    - SEO, 초기 로딩 속도에 유리
      - 참고: SEO -> Search Engine Optimization
      - 설명: SEO -> 웹사이트가 검색 엔진에서 더 높은 순위에 노출되도록 최적화하는 과정
      ```js
      // Next.js 예시 (SSR)
      export async function getServerSideProps() {
        const data = await fetchData();
        return { props: { data } };
      }
      ```

  - Client-side Rendering (CSR)
    - 초기에는 최소 HTML만 제공, 이후 JavaScript로 렌더링
    - 첫 로딩은 느릴 수 있지만, 이후 페이지 전환은 빠름
      ```js
      // CRA 등 SPA 방식
      useEffect(() => {
        fetch('/api/data').then(res => res.json()).then(setData);
      }, []);
      ```

  - 차이점
    - SSR
      - 초기 렌더링 위치: 서버 (Node.js 등)
      - SEO: 매우 우수
      - 첫 페이지 로딩: 빠름 (HTML 바로 도착)
      - 사용자 경험: 빠른 첫 렌더링
    - CSR
      - 초기 렌더링 위치: 클라이언트 (브라우저)
      - SEO: 기본적으로 불리
      - 첫 페이지 로딩: 느릴 수 있음 (JS 로딩 후 렌더링)
      - 사용자 경험: 페이지 전환이 빠름

- Next.js를 사용할 때의 장점
  - SSR 및 SSG 지원
    - 페이지 단위로 Server-Side Rendering (SSR) 또는 Static Site Generation (SSG) 선택 가능
    - 검색엔진 최적화(SEO)와 빠른 초기 로딩 성능 확보

  - 파일 기반 라우팅
    - pages/ 폴더 구조만으로 자동 라우팅 → 코드 간결화

  - API Routes 내장
    - pages/api/*.ts에 서버 코드 작성 가능 → 별도 백엔드 없이 간단한 API 제공

  - 이미지 최적화 및 성능 향상
    - next/image, 자동 코드 분할, lazy loading, prefetch 등 제공

  - 타입스크립트, ESLint, Prettier 기본 통합 지원
    - 팀 협업 및 품질 관리에 유리

  - Edge Function, Middleware 등 최신 기능 지원
    - Vercel 환경과 통합 시 강력한 클라우드 최적화

- React에서 HOC(High Order Component)
  - 개념
    - 컴포넌트를 인자로 받아 새로운 컴포넌트를 반환하는 함수
    - 로직 재사용 및 관심사 분리에 유리

  - 참고
    - 고차함수: 함수를 파라미터로 받거나 연산의 결과로 반환해주는 메서드

  - 사용 예시
    ```tsx
    function withLoading(Component) {
      return function WrappedComponent({ isLoading, ...props }) {
        return isLoading ? <div>Loading...</div> : <Component {...props} />;
      };
    }
    ```

  - 주요 용도
    - 인증 처리, 권한 제어
    - 공통 로딩/에러 처리
    - 공통 로직 추출

  - 주의 사항
    - props 전달 누락, 디버깅 어려움, 컴포넌트 중첩 문제 등이 발생할 수 있음 → React Hooks 도입 이후 일부 대체됨 (useXXX)

- React의 Reconciliation 알고리즘
  - 개념
    - React가 상태/props 변화로 인해 Virtual DOM이 변경될 때, 실제 DOM에 반영할 최소 변경 사항을 계산하는 과정

  - 핵심 원리
    - Virtual DOM을 비교(diffing)하고, 실제 DOM을 효율적으로 업데이트
    - 기존 DOM을 재사용하며 변경된 부분만 업데이트 → 성능 최적화

  - 주요 규칙
    - 같은 타입의 요소 → 속성만 업데이트
    - 다른 타입의 요소 → 해당 노드 전체 재생성
    - key 값을 기준으로 리스트 요소를 효율적으로 비교
      - → key는 변하지 않는 고유값을 사용해야 최적화 가능

  - 성능 최적화 팁
    - key 충돌 방지
    - 불필요한 재조정 방지 (ex: memo, pure component)

- React에서 상태를 전역으로 관리하는 방법
  - Context API
    - React 내장 기능으로 전역 상태 공유
    - 간단한 앱, 로그인/테마/언어 등
  - Redux
    - 액션 > 리듀서 > 스토어 구조
    - 대규모 앱, 예측 가능한 상태 흐름
  - Recoil / Zustand / Jotai / MobX
    - 경량 상태 관리 라이브러리
    - 선언형, 코드 간결, 학습 곡선 낮음

  - 선택 기준
    - Context API: 전역 공유만 필요할 때 (ex. 로그인 상태)
    - Redux: 복잡한 상태 관리, 미들웨어/DevTools 활용 시
    - Recoil/Zustand: 적은 코드로 간편하게 상태 관리하고 싶을 때

- useReducer를 사용하는 경우
  - 사용 목적
    - 복잡한 상태 로직을 컴포넌트 내부에서 분리/관리할 때
    - 다수의 상태 값이 있고, 하나의 이벤트가 여러 상태를 갱신할 때

  - 예시
    ```js
    const initialState = { count: 0 };

    function reducer(state, action) {
      switch (action.type) {
        case 'increment': return { count: state.count + 1 };
        case 'decrement': return { count: state.count - 1 };
        default: return state;
      }
    }

    const [state, dispatch] = useReducer(reducer, initialState);
    ```

  - 사용 시점
    - 상태 전이(state transition)가 명확할 때 (action → result)
    - useState로 관리하면 로직이 너무 복잡하거나 중복될 때

- React에서 useRef의 용도
  - ① DOM 접근
    - 특정 DOM 요소에 직접 접근할 때 사용 (ex. focus 제어, scroll 조작)
      ```js
      const inputRef = useRef(null);
      <input ref={inputRef} />
      <input onClick={() => inputRef.current.focus()} />
      ```

  - ② 상태 저장 (렌더링과 무관한 값 보관)
    - 렌더링을 유발하지 않는 값을 저장할 때
    - 이전 값 저장, 타이머 ID 저장 등에 유용
      ```js
      const countRef = useRef(0);
      useEffect(() => {
        countRef.current += 1; // 렌더링 없이 값 누적
      }, []);
      ```

  - ③ 이전 값 기억
    ```js
    const prevCount = useRef();
    useEffect(() => {
      prevCount.current = count;
    }, [count]);
    ```

- React에서 Portals 개념, 사용목적, 예시
  - 개념
    - 부모 컴포넌트의 DOM 계층을 벗어나 다른 DOM 노드에 자식을 렌더링할 수 있는 기능
    - ReactDOM.createPortal(child, container)를 사용

  - 사용 목적
    - 모달, 팝오버, 툴팁처럼 레이아웃 제약을 받지 않아야 하는 UI에 적합

  - 예시
    ```js
    return ReactDOM.createPortal(
      <div className="modal">Hello Modal</div>,
      document.getElementById('modal-root') // HTML의 별도 DOM 노드
    );
    ```

  - 장점
    - 시각적으로 DOM 트리 바깥에 있어도, React 트리 안에서 동작 (이벤트 버블링 유지됨)

- React에서 Synthetic Event
  - 개념
    - React가 브라우저의 네이티브 DOM 이벤트를 추상화한 이벤트 객체
    - 이벤트 간 브라우저 간 호환성을 보장하고, 성능 최적화에 유리

  - 특징
    - 모든 이벤트는 풀링(pooled) 되어 재사용됨 (React 16 이하)
    - React의 이벤트 핸들러는 버블링 중심으로 작동
      - (onClick, onChange, onSubmit 등은 캡처 대신 버블링 처리)

  - 예시
    ```js
    function handleClick(event) {
      console.log(event.type); // "click" (SyntheticEvent)
    }
    ```

  - 사용 주의점
    - 비동기 사용 시 event.persist() 또는 구조분해 할당 필요 (React 16 이하에서는 자동 소멸됨)

- React에서 key props가 필요한 이유
  - 목적
    - 리스트 렌더링 시 항목을 구별하여 최소한의 DOM 변경을 하기 위함
    - key는 React의 Reconciliation(조정) 알고리즘에서 항목을 추적하는 기준

  - 올바른 key 사용 예
    ```js
    {items.map(item => <li key={item.id}>{item.name}</li>)}
    ```

  - 잘못된 예 (index 사용)
    ```js
    {items.map((item, index) => <li key={index}>{item.name}</li>)} // 위험
    ```

  - 이유
    - index를 key로 사용하면 항목의 순서나 내용이 바뀔 때 잘못된 diffing이 발생할 수 있음
    - 예: 입력 필드, 드래그 앤 드롭 UI에서 의도치 않은 재사용 발생

- React에서 Suspense를 이용해 데이터를 비동기적으로 로딩하는 방법
  - 기본 개념
    - React.Suspense는 비동기 로딩 컴포넌트를 기다리는 동안 fallback UI를 보여주는 기능
    - 원래는 코드 분할(lazy loading)용이었지만, React 18부터는 데이터 페칭도 지원

  - 사용 방법 (React 18 이상 + use or React.lazy 기반)
    ```tsx
    <Suspense fallback={<div>로딩 중...</div>}>
      <MyAsyncComponent />
    </Suspense>
    ```

  - 데이터 로딩 예 (React 18 + use() 활용)
    ```tsx
    // utils/fetchUser.ts
    export function fetchUser(userId: string) {
      const promise = fetch(`/api/user/${userId}`).then(res => res.json());
      return wrapPromise(promise);
    }

    // 컴포넌트
    const user = fetchUser('123').read(); // read()는 throw pending promise
    ```

  - wrapPromise()는 Suspense가 이해할 수 있는 형태로 Promise를 감쌈
    ```tsx
    function wrapPromise(promise) {
      let status = 'pending';
      let result;
      const suspender = promise.then(
        r => { status = 'success'; result = r; },
        e => { status = 'error'; result = e; }
      );
      return {
        read() {
          if (status === 'pending') throw suspender;
          if (status === 'error') throw result;
          return result;
        }
      };
    }
    ```
    - 실무에서는 Relay, React Query(실험적) 등과 연계해 활용됨.


- React의 hydrate 기능
  - 개념
    - 서버에서 렌더링된 HTML을 클라이언트에서 "살리는" 작업
    - 클라이언트 JS가 서버에서 받은 정적 HTML과 일치하는지 확인하고, 이벤트 바인딩을 수행

  - 사용 예시 (Next.js, React DOM)
    ```tsx
    import { hydrateRoot } from 'react-dom/client';
    hydrateRoot(document.getElementById('root'), <App />);
    ```

  - 사용 목적
    - Server-Side Rendering(SSR) 시 렌더링된 HTML을 다시 그리지 않고, 이벤트만 연결
    - 최초 로딩 속도 향상과 SEO 확보르 동시에 가능하게 함

  - 주의 사항
    - 서버에서 렌더링한 결과와 클라이언트 렌더링 결과가 다르면 경고 발생 (Content Mismatch)
    - 동적 데이터/시간 기반 렌더링 시 반드시 클라이언트-서버 일치에 주의

- React에서 새로운 상태를 만들지 않고 이전 상태를 직접 변경하면 안되는 이유
  - 상태(State)는 불변성(Immutability)이 기본 원칙
    - 직접 변경하는 잘못된 예시
      ```tsx
      const [user, setUser] = useState({name: 'Tom', age: 20 });
      user.age = 21; // 상태 직접 변경 불가
      setUser(user); // 리렌더링 안 될 수 있음
      ```

  - 이유
    - 변화 감지 실패
      - 리액트는 Object.is로 이전/다음 값을 비교 -> 참조가 같으면 "변화 없음"으로 간주
    - 리렌더링 트리거 안 됨
      - 동일 참조 -> shouldComponentUpdate, memo, useEffect 등이 반응 안 함
    - 디버깅, 테스트 어려움
      - 이전 상태가 예측 불가능하게 변경될 수 있음 (side effect)

  - 올바른 방식 -> 불변 객체로 갱신
    ```tsx
    setUser(prev => ({ ...prev, age: 21 }));
    ```
    - 참고: 불변 객체 (Immutable Object)
      - 한 번 생성된 이후 내부 상태가 변경되지 않는 객체
      - 즉, 값을 변경할 때 기존 객체를 직접 수정하지 않고, 새로운 객체를 생성하는 방식

    - 코드 동작 설명
      - prev는 기존 상태 객체
      - { prev..., age: 21 }는 전개 연산자, spread operator를 이용해 기존 값을 복사하면서 일부 속성만 변경
        - 새 객체가 생성되었고, age값만 변경됨
      - 이 새 객체는 이전 user 객체와는 메모리 주소(참조값)가 다름
        - 즉, 새로운 객체 생성함으로써 불변성을 유지하고 리액트가 상태 변화로 정확히 인식할 수 있도록 해줌, 권장 방식

    - 추가 설명
      - 리액트의 상태 변경 감지는 이전 상태와 다른 값일 때 리렌더링
      - user.age = 21; 이런식으로 값 수정 시 user는 여전히 동일한 객체(동일한 참조) 이므로 리액트는 상태가 바뀌었다고 판단하지 못함
      - 결과적으로 리렌더링도 되지 않으며, 버그 발생

- React에서 Lazy Loading을 구현하는 방법
  - 개념
    - 필요한 시점에만 컴포넌트를 로드하여 초기 번들 크기를 줄이고 성능을 향상시키는 기법
    - React.lazy() + Syspense 조합으로 구현

  - 기본 사용법
    ```tsx
    import React, { Suspense } from 'react';

    const MyComponent = React.lazy(() => import('./MyComponent'));

    function App() {
      return (
        <Suspense fallback={<div>Loading...</div>}>
          <MyComponent />
        </Suspense>
      );
    }
    ```

  - 주요 포인트
    - React.lazy()는 동적 import() 를 사용함
    - Suspense는 로딩 중 보여줄 fallback UI를 제공

- React.memo()를 사용하는 이유
  - 개념
    - props가 변경되지 않으면 리렌더링을 방지하는 고차 컴포넌트(HOC)
    - 함수형 컴포넌트의 불필요한 리렌더링을 막아 성능 최적화에 사용

  - 사용 예시
    ```tsx
    const MyComponent = React.memo(function MyComponent({ name }) {
      return <div>Hello, {name}</div>;
    });
    ```

  - 사용 시점
    - 컴포넌트가 props에 의해서만 렌더링될 때
    - 자식 컴포넌트가 무거운 연산이나 렌더링 비용이 클 때
    - 부모 컴포넌트가 자주 리렌더링될 때

  - 주의점
    - 얕은 비교(shallow compare)만 하기 때문에, 객체나 배열을 불변성 없이 전달하면 무용지물

- React에서 Fragment 개념/정의
  - 개념
    - 여러 요소를 불필요한 추가 DOM 없이 그룹화할 수 있도록 해주는 React 기능
    - HTML 구조에 불필요한 <div> 삽입 없이 렌더링 가능

  - 기본 문법
    ```tsx
    return (
      <React.Fragment>
        <h1>Title</h1>
        <p>Paragraph</p>
      </React.Fragment>
    );
    ```

  - 축약 문법
    ```tsx
    return (
      <>
        <h1>Title</h1>
        <p>Paragraph</p>
      </>
    );
    ```

   - 주요 장점
    - 렌더링 성능 최적화 (불필요한 DOM 트리 방지)
    - JSX에서 다중 노드 반환이 필요할 때 유용

- React의 forwardRef를 사용해야 하는 경우
  - 개념
    - 부모 컴포넌트가 자식 컴포넌트의 DOM 요소에 접근할 수 있게 해주는 함수형 API
    - 기본적으로 ref는 DOM 또는 클래스 컴포넌트에만 전달되며, 함수형 컴포넌트에는 전달되지 않기 때문에 필요함

  - 사용 예시
    ```tsx
    const CustomInput = React.forwardRef((props, ref) => (
      <input ref={ref} {...props} />
    ));

    function Parent() {
      const inputRef = useRef();
      return <CustomInput ref={inputRef} />;
    }
    ```

  - 사용 시기
    - 커스텀 컴포넌트 내부에서 input, div 등의 DOM 요소에 외부에서 접근이 필요할 때
    - 예: focus, scroll, 측정 등

  - 주의점
    - forwardRef는 래핑된 컴포넌트에만 DOM 접근을 허용함 → props와 함께 ref 전달도 의도적으로 처리해야 함

- React에서 createContext()와 useContext()의 차이점
  - createContext()
    - 역할: Context 객체 생성
    - 사용 위치: 루트 또는 외부 정의
    - 반환값: { Provider, Consumer } 포함 객체
  - useContext()
    - 역할: Context 값 읽기
    - 사용 위치: 컴포넌트 내부에서만 사용 가능
    - 반환값: 현재 컨텍스트 값

  - createContext() 예시
    ```tsx
    const ThemeContext = React.createContext('light');
    ```

  - useContext() 예시
    ```tsx
    const theme = useContext(ThemeContext);
    ```

  - 결론
    - createContext()는 Context 생성을 위한 선언
    - useContext()는 생성된 Context로부터 값 사용

- React에서 JSX의 역할과 내부적으로 변환되는 방식
  - JSX 개념
    - JavaScript 안에 HTML처럼 보이는 문법을 작성할 수 있게 해주는 React의 문법 확장
    - 문자 그대로 HTML은 아니며, 컴파일러(Babel)가 함수 호출로 변환함

  - 내부 변환 방식
      ```tsx
      const element = <h1>Hello</h1>;
      // 컴파일 후:
      const element = React.createElement('h1', null, 'Hello');
      ```

  - 변환 결과의 의미
    - React.createElement(type, props, ...children) 형식으로 변환
    - 이 객체는 Virtual DOM의 노드가 됨

  - 장점
    - 선언형 UI 표현 → 가독성, 유지보수성 향상
    - JSX → Virtual DOM → 실제 DOM 반영을 위한 효율적인 중간 표현

- React에서 Error Boundary를 구현하는 방법
  - 개념
    - 렌더링 중 JavaScript 에러를 잡아내고, 앱이 크래시되는 것을 막기 위해 대체 UI를 보여주는 컴포넌트

  - 구현 조건
    - 클래스 컴포넌트로만 구현 가능
    - 두 가지 메서드를 사용:
      - static getDerivedStateFromError()
      - componentDidCatch()

  - 기본 예시
    ```tsx
    class ErrorBoundary extends React.Component {
      state = { hasError: false };

      static getDerivedStateFromError(error) {
        return { hasError: true };
      }

      componentDidCatch(error, info) {
        console.error("Error caught:", error, info);
      }

      render() {
        if (this.state.hasError) {
          return <h1>문제가 발생했습니다.</h1>;
        }
        return this.props.children;
      }
    }
    ```

  - 사용 방법
    ```tsx
    <ErrorBoundary>
      <MyComponent />
    </ErrorBoundary>
    ```

  - 처리 대상
    - 렌더링 중 오류, 라이프사이클 메서드 오류, constructor 오류
    - 캐치 가능: 자식 컴포넌트의 JS 오류
    - 캐치 불가능: 이벤트 핸들러 내부 오류, 비동기 함수 내부 오류

- React에서 Strict Mode를 사용하는 이유
  - 개념
    - React의 개발 모드에서 잠재적 문제를 감지하고 경고를 출력해주는 기능
    - 실제로는 UI에 영향을 주지 않음 (렌더링 결과는 동일)

  - 주요 기능
    - 의도치 않은 부작용 감지
    - 레거시 API 사용 경고 (ex: componentWillMount)
    - 두 번 렌더링 시뮬레이션으로 불순한 컴포넌트 로직 검출

  - 사용 예시
    ```tsx
    <React.StrictMode>
      <App />
    </React.StrictMode>
    ```

  - 주의 사항
    - 개발 환경에서만 동작
    - 렌더링/언마운트/재렌더링을 두 번 실행하여 문제 검출 → 실제 렌더링과 다르게 느껴질 수 있음

- React에서 Synthetic Events와 Native Events의 차이점
  - Synthetic Event (합성이벤트)
    - 리액트가 만든 추상화된 이벤트 객체
    - 브라우저간 호환성과 최적화 목적
    - 일관된 API 제공, 자동 풀링(16 이하), 버블링 지원
    - onClick, onChange, onSubmit등 리액트 이벤트 핸들러

  - Native Event (브라우저 고유 이벤트)
    - 브라우저가 제공하는 DOM 이벤트
    - 브라우저마다 동작이 다를 수 있음, 직접 접근 가능
    - element.addEventListener("click", handler)

  - 주요 차이
    - Synthetic Event
      - 리액트 내부 정의
      - API 일관성 있음
      - 이벤트 풀링 있음 (리액트 16이하)
      - 리액트가 성능 최적화 처리
    - Native Event
      - 브라우저 환경에 정의
      - API는 브라우저마다 다를 수 있음
      - 이벤트 풀링 없음
      - 성능 최적화는 직접 제어 필요

  - 필요 시 native event 사용 가능
    ```tsx
    <button onClick={(e) => {
      e.nativeEvent.stopPropagation(); // native event 접근
    }} />
    ```

- React에서 useEffect의 실행 순서 결정 방법
  - 실행 타이밍
    - 렌더링 이후 -> DOM 업데이트가 완료된 후 실행 (비동기)
    - 브라우저가 화면을 그린 다음에 실행

  - 실행 순서
    - (1) 컴포넌트 렌더링
    - (2) 화면에 반영 (페인팅 완료)
    - (3) useEffect() 안의 콜백 실행
    - (4) 다음 렌더 이전에 cleanup() 함수가 먼저 호출 (의존성 배열 기준)

  - 실행 조건
    - []: 컴포넌트 마운트 시 1회만 실행
    - [deps]: 의존성 변경 시에만 실행
    - 생략 시: 매 렌더링 후 실행

  - 예시
    ```tsx
    useEffect(() => {
      console.log("렌더 후 실행");

      return () => {
        console.log("다음 렌더링 실행 전 cleanup");
      };
    }, [count]);
    ```

- React의 useLayoutEffect와 useEffect의 차이점
  - useEffect
    - 실행 시점: 렌더링 후, 브라우저 페인팅 후 실행
    - 동기/비동기: 비동기
    - 주 사용 목적: API 요청, 이벤트 핸들러 등록 등
    - 성능 영향: 렌더링에 영향 없음

  - useLayoutEffect
    - 실행 시점: 렌더링 후, 브라우저 페인팅 전
    - 동기/비동기: 동기 (렌더 차단)
    - 주 사용 목적: DOM 측정, 스크롤 위치, 레이아웃 보정 등
    - 성능 영향: 렌더링 지연 가능성 존재

  - 예시: DOM 측정 시
    ```tsx
    useLayoutEffect(() => {
      const height = ref.current.offsetHeight; // 정확한 DOM 값 측정 필요
    });
    ```
    - useEffect는 사용자에게 그려진 후 실행되므로, 레이아웃 보정에는 늦음

- React에서 Fragment와 div를 사용할 때의 차이점
  - Fragment
    - 생성되는 DOM 없음, 가상의 래퍼
    - 불필요한 DOM 노드 생략 목적으로 사용
    - 깔끔한 DOM 트리 유지

  - div
    - 실제 <div> 태그가 DOM에 추가됨
    - 스타일링, 레이아웃 목적
    - 중첩 구조 증가 -> 스타일 충돌 가능성

  - Fragment 사용 예시
    ```tsx
    <>
      <h1>Title</h1>
      <p>Paragraph</p>
    </>
    ```

  - Fragment 사용 시점
    - 여러 요소를 그룹핑하면서 추가 DOM 노드 없이 렌더링하고 싶을 때
    - CSS Flex/Grid 등에서 불필요한 부모 노드 삽입을 피하고 싶을 때
    - 불필요한 DOM 생성없이 구조만 그룹핑

- React에서 이벤트 버블링을 방지하는 방법
  - 이벤트 버블링 Concept
    - 이벤트가 자식 → 부모로 전파되는 동작
    - 예: <button> 클릭 시 div의 onClick도 실행되는 현상

  - 방지 방법
    - event.stopPropagation() 사용
      - 해당 이벤트가 상위로 전파되지 않도록 막음
      ```jsx
      function ChildComponent() {
        return (
          <div onClick={(e) => e.stopPropagation()}>
            클릭 시 부모로 전파되지 않음
          </div>
        );
      }
      ```

    - event.nativeEvent.stopImmediatePropagation()
      - 이벤트 리스너 중복 실행까지 방지하고 싶을 때 사용 (드물게 사용)

  - 주로 사용되는 시점
    - 모달 외부 클릭 시 닫기, 드롭다운, 토글 버튼 등에서 자주 사용됨

- React에서 useState의 이전 상태를 기반으로 새 상태를 설정하는 방법
  - 문제
    - 상태 변경이 비동기적이기 때문에, 연속 업데이트 시 현재 상태가 아닌 이전 상태가 기준이 될 수 있음

  - 해결 방법
    - 상태 설정 함수에 함수형 업데이트 방식 사용
      ```jsx
      const [count, setCount] = useState(0);

      // 잘못된 방식 (현재 값이 stale할 수 있음)
      setCount(count + 1);
      setCount(count + 1);

      // 올바른 방식
      setCount(prev => prev + 1);
      setCount(prev => prev + 1); // 결과적으로 +2 됨
      ```

  - 사용 예
    - 상태 누적, 토글, 배열 push 등에서 이전 값을 기준으로 변경해야 할 때 필수

- React에서 React.lazy()를 사용 시 장점
  - 개념
    - React.lazy()는 컴포넌트를 동적으로 import 하여 코드 스플리팅을 가능하게 함
      ```jsx
      const MyComponent = React.lazy(() => import('./MyComponent'));
      ```

  - 장점
    - 초기 로딩 최적화	
      - 필요한 시점에만 로드 → 번들 크기 감소
    - 성능 개선	
      - 초기 진입 속도 향상, 모바일에서 유리
    - 유지보수 용이	
      - 페이지/컴포넌트 단위 분할 용이
    - Suspense와 연계 가능	
      - 로딩 중 fallback UI 표시 가능

  - 예시
    ```jsx
    <Suspense fallback={<div>Loading...</div>}>
      <MyComponent />
    </Suspense>
    ```

- React에서 Suspense와 Concurrent Mode의 연관성
  - 개념
    - Suspense
      - 컴포넌트의 비동기 로딩 상태를 처리하기 위한 리액트 기능
    - Concurrent Mode
      - 리액트 18에서 도입된 비동기 렌더링 아키텍쳐, 중단/재개 가능한 렌더링 지원

  - 연관성
    - Concurrent Mode가 있어야 Suspense가 비동기 데이터에 대해 작동 가능
    - 기존 React에서는 Suspense가 lazy 컴포넌트에만 적용 가능했지만
      - → Concurrent Mode에서는 데이터 fetch에도 Suspense 적용 가능

  - 예시 흐름
    ```tsx
    <Suspense fallback={<Loading />}>
      <DataComponent /> {/* 데이터가 준비되지 않으면 fallback UI */}
    </Suspense>
    ```

  - 실전 적용: React 18 + use() API
    - 서버 컴포넌트, async data fetching 등에서 지연 렌더링을 자연스럽게 처리 가능
      - → startTransition(), useTransition() 등도 함께 사용됨

- React에서 setState()가 비동기로 동작하는 이유
  - 이유: 성능 최적화 및 일괄 처리(batch update)
    - setState()는 바로 실행되는 것이 아니라, React의 이벤트 루프 종료 후 일괄 처리(batch) 됨
    - 이는 렌더링 횟수를 최소화하고 성능을 높이기 위한 설계

  - 예시
    ```tsx
    setState(1);
    setState(2);
    console.log(state); // 이전 값이 출력될 수 있음
    ```

  - 해결 방법
    - 최신 값을 기반으로 상태를 설정하려면 함수형 업데이트를 사용해야 함
    ```tsx
    setState(prev => prev + 1);
    ```

  - 추가 개념
    - React 18에서는 setState()가 DOM 이벤트 핸들러 외부에서는 자동 batch 되지 않음
      - → flushSync(), unstable_batchedUpdates() 등 사용 필요

- React에서 컴포넌트 최적화를 위해 shouldComponentUpdate()를 활용하는 방법
  - 개념
    - 클래스형 컴포넌트에서 불필요한 리렌더링을 방지하기 위한 생명주기 메서드
    - 새 props 또는 state가 이전과 다를 때만 리렌더링되도록 제어

  - 기본 예시
    ```tsx
    class MyComponent extends React.Component {
      shouldComponentUpdate(nextProps, nextState) {
        return nextProps.value !== this.props.value;
      }

      render() {
        return <div>{this.props.value}</div>;
      }
    }
    ```

  - 최적화 효과
    - 변경되지 않은 props/state로 인한 불필요한 DOM 계산 및 리렌더링을 차단
    - 성능 이슈가 있는 리스트 항목, 고정된 UI, 무거운 렌더링 비용이 있는 컴포넌트에서 유용

  - 함수형 컴포넌트에서 대안
    - React.memo() + areEqual() 함수로 같은 효과 구현 가능
    ```tsx
    const MyMemoComponent = React.memo(Component, (prevProps, nextProps) => {
      return prevProps.value === nextProps.value;
    });
    ```

- React에서 children props를 활용하는 방식
  - 개념:
    - children은 컴포넌트 내부에 포함된 자식 요소를 나타내는 내장 prop
    - 부모 컴포넌트가 자식 컴포넌트를 사용할 때 <Component>내용</Component> 구조로 자식 요소를 넘기면, 이 내용은 props.children으로 접근 가능

  - 사용 예시:
    ```tsx
    const Card = ({ children }) => (
      <div className="card">
        {children}
      </div>
    );

    <Card>
      <h1>Hello</h1>
      <p>This is content inside the card.</p>
    </Card>
    ```
    - 위 예제에서 <h1>과 <p>는 Card 컴포넌트의 props.children으로 들어간다.
    - 결과적으로 Card 컴포넌트 내부에서 유연하게 UI를 구성 가능

  - 실무 활용 포인트:
    - 레이아웃 컴포넌트, Modal, Button 등 재사용 가능한 컴포넌트 만들 때 자주 사용.
    - children은 단순 텍스트부터 컴포넌트 트리까지 모든 JSX를 받을 수 있음.

- React에서 상태(state) 변경이 반영되지 않는 이유
  - 가능한 원인과 설명:
    - (1) 상태가 불변성을 유지하지 않고 직접 수정된 경우
      ```tsx
        const [list, setList] = useState([1, 2, 3]);

      // 잘못된 방식 (직접 변경)
      list.push(4);
      setList(list); // 변경 감지 안 됨
      ```
      - React는 참조 변경으로 상태 변경을 감지
      - 배열/객체는 불변성 유지를 위해 spread 등을 활용해야 함

      - 올바른 예시
        ```tsx
        setList([...list, 4])
        ```

    - (2) 비동기 상태 변경을 연달아 했을 때
      ```tsx
      setCount(count + 1);
      setCount(count + 1);
      ```
      - 위 코드에서는 count 값이 동일하게 참조되므로 결국 한 번만 증가

      - 올바른 예시
        ```tsx
        setCount(prev => prev + 1);
        setCount(prev => prev + 1); // 총 2 증가
        ```

    - (3) 상태 변경 후 바로 그 값을 사용하려고 할 때
      ```tsx
      setValue('new');
      console.log(value); // 여전히 이전 값
      ```
      - setState는 비동기이므로, 변경 직후엔 이전 값을 참조
      - useEffect나 setState의 콜백에서 접근해야 함

    - (4) 그외 컴포넌트가 리렌더링되지 않는 구조일 때
      - 메모이제이션, React.memo, useCallback 등으로 인해
      - 의존성 누락 시 리렌더 안됨

- React에서 서버와 클라이언트 상태를 함께 관리하는 방법
  - 개요
    - 클라이언트 상태
      - UI 상태 (모달 열림 여부, 토글 값 등)
      - 사용자 입력값, 현재 페이지 등

    - 서버 상태
      - 외부 API에서 받아온 데이터
      - 비동기 응답 (예: 목록, 상세 정보, 인증 상태 등)

  - 통합 관리 전략
    - ① React Query, TanStack Query
      - 서버 상태 전용 관리 라이브러리
      - 자동 캐싱, 리패칭, 상태 구분 (isLoading, isError, data 등)
      - 예시
        ```tsx
        const { data, isLoading } = useQuery(['user', userId], () => fetchUser(userId));
        ```
      - 클라이언트 상태와 useState/useReducer로 분리해 함께 사용

    - ② 상태 관리 라이브러리 + API 연동
      - Recoil, Zustand, Redux, Jotai 등 클라이언트 상태를 저장하면서, 서버 데이터도 함께 관리 가능
      - 예: Zustand에서 비동기 데이터 fetch와 로컬 상태를 한곳에서 다룸
        ```tsx
        const useStore = create((set) => ({
          user: null,
          fetchUser: async () => {
            const data = await fetch('/api/user').then(res => res.json());
            set({ user: data });
          }
        }));
        ```

    - ③ useEffect + fetch 직접 사용
      - 간단한 경우엔 useEffect에서 fetch하여 useState로 상태 저장
        ```tsx
        useEffect(() => {
          fetch('/api/data')
            .then(res => res.json())
            .then(data => setData(data));
        }, []);
        ```

  - 실무에서의 베스트 프랙티스
    - 클라이언트 UI 상태: useState, useReducer, Zustand
    - 서버 비동기 데이터: React Query, SWR
    - 둘 다 필요할 때: 서버 상태는 React Query로, 클라이언트 상태는 local state로 역할 분리

- React에서 Redux Thunk와 Redux Saga의 차이점
  - 공통점
    - 둘 다 Redux의 middleware로 사용되어, 비동기 로직 (API 호출 등) 을 Redux에서 처리할 수 있게 도와줌.

  - Redux Thunk
    - 개념
      - Thunk는 action creator가 함수를 반환하도록 허용함.
      - 반환된 함수 안에서 dispatch, getState 등을 통해 비동기 로직 실행 가능.

    - 특징
      - 간단한 로직에 적합
      - 배우기 쉽고 코드가 직관적
      - 네이티브 JavaScript로 작성 가능

    - 예시:
      ```tsx
      export const fetchUser = (id) => async (dispatch) => {
        dispatch({ type: 'FETCH_USER_START' });
        const res = await fetch(`/api/user/${id}`);
        const data = await res.json();
        dispatch({ type: 'FETCH_USER_SUCCESS', payload: data });
      };
      ```

  - Redux Saga
    - 개념
      - Saga는 Generator 함수 기반의 미들웨어
      - 비동기 흐름을 제어하고, 복잡한 사이드이펙트를 쉽게 테스트하고 추적 가능

    - 특징
      - 액션 흐름을 감시(watch)하고, 복잡한 시나리오 제어에 강함 (예: retry, cancel, debounce)
      - watch, takeLatest 등 사용 가능
      - 학습 난이도 있음
      - 테스트 가능성과 유지보수성이 우수, 코드 가독성은 복잡할수록 명확해지는 경향이 있음

    - 예시:
      ```tsx
      function* fetchUserSaga(action) {
        try {
          yield put({ type: 'FETCH_USER_START' });
          const data = yield call(fetch, `/api/user/${action.payload}`);
          const result = yield data.json();
          yield put({ type: 'FETCH_USER_SUCCESS', payload: result });
        } catch (e) {
          yield put({ type: 'FETCH_USER_ERROR', error: e });
        }
      }
      ```

- React에서 Server Components의 개념과 활용 방법
  - 개념
    - React Server Components (RSC)는 React 18부터 지원되며, 서버에서 렌더링한 컴포넌트를 클라이언트 JS 없이 HTML로 보내는 기능.
      - 컴포넌트 자체가 서버에서 실행됨
      - 클라이언트에서 JS 번들로 내려가지 않음
      - 초기 렌더 속도 향상, 데이터 보안 강화

  - 특징
    - 서버에서 렌더: React 컴포넌트가 서버에서 실행되어 HTML 생성
    - JS 번들 없음: 클라이언트로 JS가 전달되지 않아 더 가볍고 빠름
    - 상태 없음: useState, useEffect 사용 불가
    - props로 클라이언트 컴포넌트 포함 가능: 필요 시 클라이언트 컴포넌트를 props를 내려줌

  - 예시 (Next.js 13 + App Router 기준)
    ```tsx
    // app/page.tsx (Server Component)
    import ProductList from './ProductList';

    export default async function Page() {
      const products = await fetchProducts(); // 서버에서 직접 fetch
      return <ProductList products={products} />;
    }
    ```
    ```tsx
    // ProductList.tsx (Client Component)
    'use client';
    import { useState } from 'react';

    export default function ProductList({ products }) {
      const [filter, setFilter] = useState('');
      return (
        <>
          <input value={filter} onChange={e => setFilter(e.target.value)} />
          <ul>
            {products.filter(p => p.name.includes(filter)).map(p => (
              <li key={p.id}>{p.name}</li>
            ))}
          </ul>
        </>
      );
    }
    ```

- React에서 hydration이 실패하는 이유
  - Hydration 개념
    - 서버에서 렌더링된 HTML을 클라이언트에서 React가 다시 연결(bind) 하여 인터랙티브하게 만드는 과정

  - 실패 원인 3대 요인
    - (1) 클라이언트와 서버의 렌더링 결과 불일치
      - 예: Math.random(), Date.now() 같은 비결정적 값 사용
        ```tsx
        // 서버와 클라이언트에서 결과가 다름 → hydration mismatch
        <span>{Math.random()}</span>
        ```

    - (2) 조건부 렌더링 차이
      - 예: window 객체 사용 또는 media query 처리 등 클라이언트 환경 전용 코드
        ```tsx
        if (typeof window !== 'undefined') {
          return <div>Only in browser</div>;
        }
        ```

    - (3) 상태 초기값 불일치
      - 클라이언트 상태 초기화 값이 서버와 다를 때

  - 해결 방법
    - 랜덤 값 사용: useEffect 내에서 처리하거나 SSR 제외
    - 윈도우 객체 접근: useEffect 안에서만 접근
    - 날짜/시간 표시: 서버/클라이언트에 동일한 값 주입 또는 클라이언트에서 처리
    - 동적 로딩 요소: suppressHydrationWarning 또는 use client 분리

  - 에러 예시
    ```bash
    Warning: Text content did not match. Server: "Hello" Client: "Hi"
    ```
    - → HTML은 "Hello"인데, JS 렌더는 "Hi"이기 때문에 hydration mismatch.

- React에서 Suspense로 데이터를 fetch할 때 발생할 수 있는 문제
  - 개념 요약
    - Suspense는 비동기 로딩 상태를 선언적으로 처리하기 위해 사용
    - React.lazy와 React 18에서의 Suspense for Data Fetching은 다르게 동작
    - 서버 컴포넌트(SSR) 또는 useTransition, useDeferredValue, use 훅과 함께 사용하면 매우 강력

  - 주요 문제점
    - 브라우저 지원 문제
      - 일부 실험적 기능은 브라우저에서 완전히 지원되지 않거나 React 버전 의존성이 강함.

    - 호환성 부족
      - Suspense는 React Query나 SWR 등의 라이브러리와 통합하지 않으면 단독 사용 시 데이터 fetching 흐름 제어가 어려움.

    - 에러 핸들링 미흡
      - Suspense는 로딩 상태는 잘 처리하지만, 오류 처리는 ErrorBoundary를 함께 사용해야 제대로 처리 가능.

    - Fallback 깜빡임
      - 서버 사이드 렌더링 시 fallback이 깜빡이거나 hydration mismatch가 발생할 수 있음.

    - Suspense boundary nesting
      - 여러 컴포넌트에 중첩된 Suspense boundary가 있을 경우 예기치 않은 리렌더링 지연이나 데이터 race condition이 생길 수 있음.

- React의 Concurrent Rendering이 UI 성능에 미치는 영향
  - 개념 요약
    - Concurrent Rendering은 React가 렌더링 작업을 중단하고 다시 시작할 수 있도록 만들어, 사용자의 인터랙션을 우선시하면서 앱을 더 부드럽고 반응성 있게 만드는 기능
    - React 18부터 기본 적용되지 않고, createRoot()를 사용해 opt-in 방식으로 활성화

  - 성능에 미치는 영향
    - 긍정적 영향
      - 렌더링 중단 및 재시작을 통해 우선순위 높은 작업(예: 사용자 입력)을 먼저 처리함.
      - Transition 기반의 UI 업데이트에서 지연 로딩이 가능하여 UX가 향상됨.
      - 앱이 큰 컴포넌트 트리를 가진 경우, 블로킹 없이 부드러운 렌더링이 가능함.

    - 부정적 영향
      - 상태 동기화가 까다로워져서, 올바르지 않은 렌더 순서로 인해 의도치 않은 UI가 보일 수 있음.
      - 효율적인 캐싱/메모이제이션 없이 사용할 경우 오히려 리렌더링이 많아져 성능 저하가 발생할 수 있음.
      - 디버깅이 어려움: 중단된 작업과 재시작된 작업 사이의 상태 추적이 어려워짐.

- React에서 useRef와 useState의 차이점
  - useRef
    - DOM 참조, 변경 가능한 변수 저장
    - 값 변경 시 리렌더링 없음
    - input 포커스 제어, 이전 값 기억, 타이머 ID 저장
    - 컴포넌트 생명주기 내에서 유지 (보존 여부)
    - ref.current를 통해 접근
  - useState
    - UI 상태 값 저장 및 리렌더 트리거
    - 값 변경 시 리렌더링 발생
    - 입력값 상태 관리, UI 갱신에 필요한 상태
    - 유지되나 변경 시 다시 렌더링됨
    - useState()의 setter로 상태 변경
  - 정리
    - 핵심 차이는 렌더링을 유발하는가 여부임
    - useRef는 렌더링에 영향을 주지 않으므로 값 보존이나 DOM 제어에 적합
    - useEffect는 리렌더링을 통해 UI를 업데이트해야 할 때 사용


- React에서 useReducer를 사용하는 시나리오
  - 개념 요약
    - useReducer는 상태를 업데이트하는 방식이 복잡하거나, 여러 액션 타입으로 나누어 처리해야 하는 상황에서 유용한 훅
    - useState보다 더 구조적인 상태 관리를 가능하게 만듬

  - 적용 시나리오
    - 복잡한 상태 로직: 상태가 단순하지 않고 여러 조건/액션에 따라 다른 방식으로 업데이트되는 경우 (if/switch가 많은 경우).
    - 상태가 객체 형태이고 부분적으로 갱신되어야 하는 경우.
    - 이전 상태를 기반으로 새로운 상태를 계산해야 할 때 (prevState를 참조할 필요가 있을 때).
    - Redux 스타일의 액션 중심 상태 관리가 필요한 경우.
    - 컴포넌트 트리에 깊이 있는 자식에게 상태와 디스패치 함수를 전달하려는 경우 (Context와 함께 사용).

  - 예시
    ```tsx
    const initialState = { count: 0 };

    function reducer(state, action) {
      switch (action.type) {
        case 'increment': return { count: state.count + 1 };
        case 'decrement': return { count: state.count - 1 };
        default: return state;
      }
    }

    const [state, dispatch] = useReducer(reducer, initialState);
    ```

- React의 Error Boundaries 유용한 상황
  - 개념 요약
    - Error Boundary는 렌더링 과정, 라이프사이클 메서드, 하위 트리에서 발생한 런타임 에러를 포착하여 전체 앱이 죽지 않도록 보호하는 컴포넌트

  - 유용한 상황
    - 서버에서 전달된 데이터 오류로 인한 UI 크래시 방지
    - 타사 라이브러리 또는 비정상적 사용자 입력으로 인한 컴포넌트 렌더 실패
    - 전체 UI가 멈추는 것을 방지하고, fallback UI 제공
    - 에러 발생 시 사용자에게 친절한 메시지나 복구 옵션을 보여주고 싶을 때

  - 예시
    ```tsx
    class ErrorBoundary extends React.Component {
      state = { hasError: false };
      static getDerivedStateFromError() {
        return { hasError: true };
      }
      render() {
        if (this.state.hasError) return <h1>문제가 발생했습니다.</h1>;
        return this.props.children;
      }
    }
    ```

- React에서 CSS-in-JS 라이브러리를 사용하는 이유
  - 개념 요약
    - CSS-in-JS는 JavaScript 파일 내에서 직접 CSS를 정의하고 사용할 수 있게 해주는 방식
    - 대표 라이브러리는 styled-components, emotion, JSS 등

  - 사용 이유 및 장점
    - 컴포넌트 단위 스타일링: 스타일이 컴포넌트와 함께 묶여 관리됨 → 유지보수 용이
    - 동적 스타일링: props나 상태에 따라 스타일을 동적으로 변경 가능
    - 클래스 이름 충돌 방지: 자동으로 고유한 className을 생성
    - 테마 지원: ThemeProvider를 통한 전역 테마 관리 가능
    - JavaScript의 힘 활용: 조건문, 계산식 등 논리적 제어 가능

  - 예시 (styled-components):
    ```tsx
    const Button = styled.button`
      background: ${(props) => (props.primary ? 'blue' : 'gray')};
      color: white;
    `;
    ```

- React에서 Refs를 활용해 DOM 요소를 조작하는 방법
  - 개념 요약
    - ref는 특정 DOM 요소에 직접 접근할 수 있도록 하는 React의 기능
    - 보통 input, canvas, 비디오 등 브라우저 DOM API에 접근할 필요가 있을 때 사용

  - 사용 방법
    - useRef()로 ref 객체 생성
    - JSX 요소에 ref 속성으로 연결
    - ref.current를 통해 DOM 요소에 접근 및 조작

  - 사용 예시
    ```tsx
    function MyComponent() {
      const inputRef = useRef<HTMLInputElement>(null);

      const focusInput = () => {
        inputRef.current?.focus(); // input DOM 요소에 직접 접근
      };

      return (
        <>
          <input ref={inputRef} type="text" />
          <button onClick={focusInput}>Focus</button>
        </>
      );
    }
    ```

  - 활용 사례
    - 포커스 이동 / 스크롤 제어
    - 비디오 재생/일시정지
    - 외부 라이브러리(D3, Chart.js 등)에서 DOM 요구 시
    - 이전 값 추적 (렌더링에는 영향 없음)

- React에서 비동기 상태 업데이트를 수행하는 방법
  - 개념 요약
    - React의 상태(useState) 업데이트는 본질적으로 비동기적이지만, 비동기 함수는 아님.
    - 즉, 상태가 즉시 반영되지 않고 다음 렌더 사이클에 반영되며, await setState()처럼 사용할 수는 없음.

  - 비동기 상태 처리 방식
    - 상태 업데이트 후 직접 값을 사용하지 말고 useEffect 등에서 후속 처리 필요
    - useEffect, useCallback, async/await 조합으로 로직 구성
    - 비동기 데이터 fetch 시에는 useEffect와 함께 setState 사용

  - 예시
    ```tsx
    const [data, setData] = useState(null);

    useEffect(() => {
      const fetchData = async () => {
        const res = await fetch("/api/data");
        const json = await res.json();
        setData(json); // 비동기적으로 반영됨
      };
      fetchData();
    }, []);
    ```

  - 주의점
    - setState 다음 줄에서 즉시 변경된 값을 사용하면 이전 값일 수 있음
    - 연속적인 setState 호출은 batching 처리되어 마지막 값만 반영될 수 있음

- React에서 Formik과 React Hook Form의 차이점
  - Formik
    - 상태 기반 방식 (state-driven)
    - 상태 업데이트가 많아질수록 성능 저하 발생
    - Yup과 통합 쉬움 (유효성 검사)
    - Controlled components 컨트롤 방식
    - 선언적, 직관적 구조 (Form 구성)

  - React Hook Form
    - 레퍼런스 기반 (ref-driven)
    - 리렌더 최소화로 성능 우수
    - 자체 방식 또는 Zod/Yup 통합 (유효성 검사)
    - Uncontrolled 기반 (controlled도 가능, 컨트롤 방식)
    - 훅 기반으로 유연 (Form 구성)

  - 요약
    - Formik: 직관적으로 사용 쉬운 편, 작은 프로젝트 적합
    - React Hook Form: 상대적으로 나은 성능, 큰 규모 프로젝트 적합, 리엔더링 최소화가 강점

- React에서 useImperativeHandle() 역할
  - 개념 요약
    - useImperativeHandle은 부모 컴포넌트가 자식 컴포넌트의 특정 메서드나 속성에 직접 접근하도록 허용할 때 사용
    - 일반적인 ref 사용과 달리, 커스텀 ref 노출 방식을 정의할 수 있음

  - 사용 예시
    ```tsx
    const CustomInput = forwardRef((props, ref) => {
      const inputRef = useRef();

      useImperativeHandle(ref, () => ({
        focus: () => inputRef.current.focus(),
        clear: () => (inputRef.current.value = "")
      }));

      return <input ref={inputRef} />;
    });

    // 부모에서 사용
    const parentRef = useRef();
    <CustomInput ref={parentRef} />;
    parentRef.current.focus(); // 자식이 노출한 메서드 호출
    ```

  - 사용하는 시점
    - 자식 컴포넌트 내부 구현을 감추면서 특정 동작만 외부에 노출하고 싶을 때
    - 외부에서 자식의 포커스, 초기화, 스크롤 제어 등의 동작을 직접 호출해야 할 때

- React에서 이벤트 핸들러를 바인딩하는 올바른 방법
  - 핵심 개념
    - React는 JSX 문법 내에서 핸들러를 전달할 때 this 바인딩이나 불필요한 리렌더를 피하는 방식으로 작성하는 것이 중요

  - Class 컴포넌트
    - 생성자(constructor)에서 this.handler = this.handler.bind(this) 사용
    - 또는 클래스 필드 문법을 사용 (handleClick = () => {})
    - 예시
      ```tsx
      class MyComponent extends React.Component {
        constructor(props) {
          super(props);
          this.handleClick = this.handleClick.bind(this); // 바인딩
        }

        handleClick() {
          console.log("Clicked");
        }

        render() {
          return <button onClick={this.handleClick}>Click me</button>;
        }
      }
      ```

  - 함수형 컴포넌트
    - useCallback() 훅을 사용해 불필요한 재생성을 막는 것이 권장
    - 예시
      ```tsx
      const MyComponent = () => {
        const handleClick = useCallback(() => {
          console.log("Clicked");
        }, []);

        return <button onClick={handleClick}>Click me</button>;
      };
      ```

  - 주의할 점
    - JSX 내에서 onClick={() => doSomething()}처럼 매번 새 함수 생성 시 성능 저하 가능
    - 핸들러에 파라미터 전달이 필요한 경우는 래핑 함수 사용하되, 캐싱도 고려 필요

- React에서 함수를 props로 전달할 때 발생할 수 있는 문제
  - 문제 개요
    - 부모 컴포넌트에서 자식 컴포넌트로 함수를 props로 전달할 때, 매 렌더링마다 새로운 함수가 생성되면 불필요한 리렌더링이 발생할 수 있습니다.

  - 대표적인 문제들
    - 불필요한 자식 컴포넌트 리렌더링
      - React는 props가 변경되면 자식 컴포넌트를 리렌더링
      - 함수가 매번 새롭게 생성되면 shallow 비교에서 항상 false가 되어 리렌더가 발생합니다.

    - React.memo 무력화
      - 자식 컴포넌트를 React.memo로 감싸도, 함수 props가 변경되면 효과가 없어집니다.

    - 성능 저하
      - 렌더 트리 깊이가 클수록 매 렌더마다 많은 컴포넌트가 리렌더링되어 성능에 악영향을 줄 수 있습니다.

  - 해결 방법
    - useCallback 훅을 사용하여 함수 재생성을 방지
    - 예시
      ```tsx
      const handleClick = useCallback(() => {
        console.log("clicked");
      }, []);
      ```

- React에서 useEffect를 활용한 Debounce 구현 방법
  - 개념 요약
    - Debounce는 특정 입력 후 일정 시간 동안 사용자 입력이 없을 때만 작업을 실행하는 방식
    - 검색, 자동 저장 등에 사용됨

  - 예시 코드
    ```tsx
    const [query, setQuery] = useState("");
    const [debouncedQuery, setDebouncedQuery] = useState(query);

    useEffect(() => {
      const handler = setTimeout(() => {
        setDebouncedQuery(query);
      }, 500); // 500ms 딜레이

      return () => clearTimeout(handler); // cleanup
    }, [query]);
    ```

  - 설명
    - query가 변경될 때마다 타이머를 새로 설정
    - 일정 시간 내에 다시 입력되면 이전 타이머는 취소
    - 일정 시간 유지되면 debouncedQuery 업데이트됨

  - 활용 예
    - API 호출 최적화
    - 실시간 입력 처리 제한

- React에서 useState를 배열이나 객체와 함께 사용할 때 주의할 점
  - 문제점
    - 불변성 유지 필수
      - 배열/객체는 참조 타입이기 때문에 직접 수정하면 상태 변경이 감지되지 않음
        - → UI가 업데이트되지 않을 수 있음

  - 주의사항
    - 반드시 새로운 배열/객체를 만들어 setState에 전달해야 함

  - 예시 비교
    ```tsx
    // 잘못된 예
    state.items.push(newItem);
    setState(state); // 변경 감지 X

    // 올바른 예
    setState(prev => ({ ...prev, items: [...prev.items, newItem] }));
    ```
    - 이전 상태에 의존할 경우 setState(prev => ...) 패턴을 사용할 것
    - useEffect 등에서 객체/배열을 dependency로 사용할 때 useMemo나 useCallback으로 관리해야 불필요한 호출 방지 가능

- React에서 useReducer를 사용하면 성능이 향상되는 이유
  - 핵심 개념
    - useReducer는 상태 업데이트 로직을 외부로 분리함으로써 복잡한 상태 변경을 관리하기 쉬우며, 성능상의 이점도 제공합니다.

  - 성능 향상 이유
    - 상태 로직 분리로 인해 컴포넌트 함수 재생성 최소화
    - 상태 변경 함수(reducer)가 stable하기 때문에 useCallback/React.memo와의 궁합이 좋음
    - 복잡한 상태에서 다수의 useState를 분리 관리하는 것보다 리렌더 최소화 및 상태 관리 효율성 증가
    - dispatch 함수 자체는 불변이므로 props로 내려줘도 리렌더 유발 없음

  - 예시
    ```tsx
    const [state, dispatch] = useReducer(reducer, initialState);
    // 상태 업데이트 로직이 reducer 함수에 집중되므로 가독성과 재사용성 ↑
    ```
  
  - 언제 사용하면 좋은가?
    - 상태 필드가 3개 이상이거나, 복잡한 조건에 따라 변경되는 경우
    - 상태 변경 타입이 명확히 나뉘는 경우 (ex. form 상태, 페이지 상태)

- React에서 React.createElement() 사용 시점
  - 개념 요약
    - React.createElement()는 JSX가 트랜스파일된 후 호출되는 함수로, 리액트 엘리먼트를 생성하는 가장 기본적인 방식
    - 즉, JSX는 React.createElement의 문법적 설탕(Syntax Sugar)
    - 예시
      ```jsx
      const element = <h1>Hello</h1>;
      // 트랜스파일 결과
      const element = React.createElement('h1', null, 'Hello');
      ```

  - 언제 직접 사용하는가?
    - JSX를 사용할 수 없는 환경 (예: 서버 렌더링, 테스트 도구, Babel 미적용 환경)
    - 동적으로 태그명 또는 컴포넌트 타입을 지정할 때
    - 예시
      ```tsx
      function createTag(tagName, content) {
        return React.createElement(tagName, null, content);
      }
      ```

  - 정리
    - 직접 사용은 드물고 대부분 JSX를 통해 간접적으로 사용되며, 리액트의 동작 원리를 이해할 때 중요한 함수

- React에서 이벤트 위임(event delegation)의 원리
  - 개념 요약
    - 이벤트 위임은 하위 DOM 요소마다 이벤트 리스너를 개별로 붙이는 대신, 상위 요소에 단 하나의 이벤트 리스너를 붙여서 이벤트를 처리하는 기법

  - React의 적용 방식
    - React는 모든 이벤트 리스너를 document 혹은 root 컨테이너에 한 번만 등록합니다.
    - 이후 발생한 이벤트는 버블링을 통해 루트로 올라오며, React는 해당 이벤트를 감지해 SyntheticEvent로 처리합니다.

  - 장점
    - DOM 요소 수가 많아도 메모리 효율적
    - 코드 유지보수가 쉬움 (리스너를 컴포넌트 내에서 통제)
    - 이벤트 제거/추가 관리가 단순화됨

  - 결론
    - React의 이벤트 시스템은 자동으로 이벤트 위임 방식으로 동작하며, 개발자는 신경 쓰지 않아도 되지만 퍼포먼스나 디버깅 시 이해하고 있으면 유리합니다.

- React에서 Lazy Loading과 Code Splitting을 적용하는 방법
  - 개념 요약
    - Lazy Loading은 필요한 시점에 리소스를 로드하는 기술이며,
    - Code Splitting은 앱을 작은 번들로 나눠서 초기 로딩 속도를 개선하는 기법

  - 적용 방법
    - (1) React.lazy() + Suspense 사용
      ```tsx
      const LazyComponent = React.lazy(() => import('./LazyComponent'));

      function App() {
        return (
          <Suspense fallback={<div>Loading...</div>}>
            <LazyComponent />
          </Suspense>
        );
      }
      ```

    - (2) 동적 import() + Webpack Chunk
      ```tsx
      import(/* webpackChunkName: "admin" */ './AdminPage')
      ```

    - (3) 라우팅 기반 Code Splitting (React Router 예시)
      ```tsx
      const AdminPage = React.lazy(() => import('./AdminPage'));

      <Route path="/admin" element={
        <Suspense fallback={<Loading />}>
          <AdminPage />
        </Suspense>
      } />
      ```

  - 장점
    - 초기 로딩 속도 개선
    - 사용자 경험 향상
    - 모바일 환경에서 데이터 비용 절감

- React에서 클라이언트 상태와 서버 상태의 차이점
  - 클라이언트 상태
    - 로컬에서만 관리되는 상태 (UI 상태, 입력값 등)
    - 도달 열림 여부, 폼 입력값, 다크모드 설정 등
    - useState, useReducer, Context 등
    - 앱 안에서만 존재하고 즉시 반응 가능
    - 동기화는 앱 내부 논리만 고려
  - 서버 상태
    - 서버에서 가져와야 하며 외부와 동기화 필요
    - 유저 정보, API 응답 데이터, 게시글 목록
    - React Query, SWR, Redux-Toolkit-Query 등
    - 네트워크 요청/응답, 캐싱, 에러 처리 필요
    - 동기화는 서버와의 일관성 유지 필수
  - 요약
    - 클라이언트 상태는 앱 내에서 직접 통제 가능
    - 서버 상태는 외부 요인(지연, 실패, 불일치 등) 고려해야 하므로 비동기 처리 및 캐싱 전략 중요

- React에서 useEffect와 useLayoutEffect를 함께 사용할 때 주의할 점
  - 개념 차이
    - useEffect는 브라우저 페인팅 이후에 실행 (비동기적으로 호출됨)
    - useLayoutEffect는 DOM 변경 직후, 페인팅 이전에 동기적으로 실행

  - 주의할 점
    - 렌더링 차단 위험: useLayoutEffect는 동기적이기 때문에 무거운 작업을 하면 UI 렌더링 지연이 발생할 수 있음.
    - 순서 주의: 두 훅을 함께 쓰면 useLayoutEffect가 먼저 실행됨 → 레이아웃 측정/스크롤 제어에 적합, 반면 useEffect는 네트워크, 비동기 타이머 등에 적합.
    - SSR 환경 주의: useLayoutEffect는 서버 렌더링 중 경고가 발생할 수 있으므로 조건부로 실행 (typeof window !== "undefined" 등).

  - 정리
    - DOM 측정/스타일 계산/스크롤 이동 → useLayoutEffect
    - API 호출/이벤트 리스너 등록/비동기 로직 → useEffect
    - 같이 사용할 땐 기능 목적을 명확히 분리해야 하며, useLayoutEffect는 최소한으로 사용해야 렌더링 병목을 방지할 수 있음.

- React에서 Server Components를 활용 시 이점
  - 개념 요약
    - Server Components는 React 18에서 도입된 기능으로, JS 번들에 포함되지 않고 서버에서만 실행되는 컴포넌트

  - 주요 이점
    - JS 번들 크기 감소: 클라이언트에 전송되지 않으므로 초기 JS 로드 속도 향상
    - 보안: 민감한 로직(API 키, DB 쿼리 등)이 클라이언트로 노출되지 않음
    - 직접 데이터 fetch 가능: 서버에서 직접 DB/API 접근 → 클라이언트까지 데이터 전달 필요 없음
    - SEO 친화적 SSR: 서버에서 완성된 HTML 제공 가능
    - 병렬 처리 및 성능 최적화: 서버에서 병렬적으로 여러 컴포넌트를 렌더링 가능

  - 활용 예시
    ```tsx
    // Server Component
    export default async function UserProfile() {
      const data = await getUserFromDB();
      return <div>{data.name}</div>;
    }
    ```

  - 주의사항
    - 클라이언트 기능 (상태 관리, 이벤트 핸들링 등)은 불가능 → 필요 시 use client를 통해 클라이언트 컴포넌트로 분리해야 함

- React의 Fiber Reconciliation 알고리즘
  - 개념 요약
    - Fiber는 React의 새로운 렌더링 엔진 구조로, 기존 재귀적 스택 기반 렌더링의 한계를 극복하고 작업을 쪼개어 처리하는 방식을 제공

  - 기능 및 구조
    - 작업 단위 분할: 각 컴포넌트를 "Fiber Node"로 만들어 렌더링을 작은 단위로 나눔
    - 중단 가능(render interruption): 긴 렌더링을 일시 중단하고 우선순위가 높은 작업을 먼저 처리 가능
    - 우선순위 기반 스케줄링: 중요한 작업(ex. 입력 응답)은 먼저, 덜 중요한 작업(ex. 이미지 로딩)은 나중에 처리
    - 비동기 렌더링 지원: Concurrent Mode와 Suspense 구현의 기반

  - 예시 흐름
    - 작업이 시작되면 Fiber Tree를 만들며 각 작업을 분할 처리
    - 중단 가능하도록 stack이 아닌 단일 linked list 구조로 구성
    - 완료된 작업은 commit phase에서 한번에 적용

  - 결과적 이점
    - 부드러운 UI 인터랙션
    - 낮은 프레임 드랍
    - 효과적인 에러 처리 및 recovery

- React에서 메모리 누수를 방지하는 방법
  - 메모리 누수 주요 원인
    - 비동기 작업 후 컴포넌트가 언마운트되었는데도 setState 호출
    - setInterval, setTimeout 등 클린업 누락
    - 이벤트 리스너나 외부 라이브러리 구독 해제 안 됨
    - DOM 참조(ref) 또는 전역 객체에 지속적으로 참조된 상태

  - 예방 방법
    - useEffect에서 클린업 함수 반환하기
      ```tsx
      useEffect(() => {
        const id = setInterval(() => console.log("tick"), 1000);
        return () => clearInterval(id); // 클린업
      }, []);
      ```

    - 비동기 작업 취소 패턴
      ```tsx
      useEffect(() => {
        let cancelled = false;
        async function loadData() {
          const data = await fetchData();
          if (!cancelled) setState(data);
        }
        loadData();
        return () => {
          cancelled = true;
        };
      }, []);
      ```

    - 외부 리소스 사용 시 해제 처리 (WebSocket, Observer 등)
      ```tsx
      useEffect(() => {
        const socket = new WebSocket("...");
        return () => socket.close();
      }, []);
      ```

  - 정리
    - React에서의 메모리 누수는 대부분 컴포넌트 언마운트 이후에도 지속되는 비동기 작업이나 리스너에서 발생하므로, useEffect의 클린업 함수와 상태 체크가 핵심 예방 전략

- React에서 hydrate() 함수의 역할
  - 개념 요약
    - hydrate()는 서버에서 렌더링된 HTML과 클라이언트의 React 앱을 연결(attach)해주는 함수
    - React 18부터는 ReactDOM.hydrateRoot()가 도입되었음

  - 역할
    - 서버에서 전달된 정적인 HTML을 클라이언트에서 대체하지 않고 유지한 채 이벤트 핸들러만 연결
    - 초기 렌더링 속도 개선 및 SEO 대응
    - 클라이언트와 서버의 렌더 결과가 다를 경우 "hydration mismatch" 경고 발생

  - 주의점
    - 서버와 클라이언트의 결과가 완전히 동일해야 함
    - 상태나 시간 기반 데이터는 서버에서 미리 설정하거나 클라이언트에서 따로 처리 필요

- React에서 Recoil과 Redux의 차이점
  - Recoil
    - 상태가 그래프처럼 구성 (Atoms & Selectors)
    - 비교적 간단하고 React 친화적
    - 비동기 처리 Selector에서 직접 가능 (async)
    - React 전용 설계 (훅 기반)
    - 세분화된 상태 단위 리렌더링

  - Redux
    - 전역 스토어, 단일 상태 트리
    - 보일러 플레이트가 많고 외부 미들웨어 필요
    - redux-thunk, redux-saga 등 외부 도구 필요
    - React 외 앱에도 사용 가능
    - 전체 스토어 기준 리렌더 발생 가능성

  - 요약 정리
    - Recoil은 간단한 구조, 훅 기반의 사용, 세분화된 리렌더링에 강점
    - Redux는 예측 가능성, 커뮤니티, 툴링에서 강력하나 복잡도 있음

- React에서 Zustand 상태 관리 라이브러리를 사용하는 이유
  - Zustand 특징 요약
    - 매우 가볍고 빠른 상태 관리 라이브러리
    - 전역 상태를 Hook 기반으로 선언하고, 불변성 관리 없이도 직관적인 사용 가능
    - Redux보다 훨씬 간결한 코드, React 외부에서도 사용 가능

  - 사용 이유 및 장점
    - 보일러플레이트 없음: 액션/리듀서 분리 불필요
    - 초간단 문법: create() 함수 하나로 store 생성
    - 자동 상태 최적화: 필요한 selector만 추출해 리렌더 최소화
    - Redux DevTools 통합 가능
    - SSR, Persist, Immer, Middleware 확장도 손쉬움

  - 예시
    ```tsx
    const useStore = create((set) => ({
      count: 0,
      increase: () => set((state) => ({ count: state.count + 1 })),
    }));
    ```

  - 요약
    - Zustand는 간결함과 퍼포먼스를 동시에 제공하며, Redux의 복잡성이 부담일 때 강력한 대안

- React에서 Suspense의 대체 기능
  - Suspense의 역할
    - 비동기 컴포넌트 로딩 중 fallback UI 렌더링
    - Code splitting 또는 Server Components와 함께 사용

  - 대체 또는 보완 기능들
    - (1) React Query / SWR
      - isLoading, isFetching 상태를 통해 로딩 UI 제어
      - Suspense 없이도 비동기 상태 관리 및 캐싱 수행
      - 필요 시 suspense: true 옵션으로 Suspense 연동도 가능

    - (2) Conditional Rendering
      - 단순한 로딩 처리에는 삼항 연산자나 조건부 렌더링 사용
        ```tsx
        {loading ? <Spinner /> : <DataComponent />}
        ```

    - (3) Custom Fallback Wrapper
      - 로딩 및 에러 처리를 포함하는 고차 컴포넌트
        ```tsx
        function withFallback(Component) {
          return function Wrapper({ isLoading, ...props }) {
            if (isLoading) return <Loading />;
            return <Component {...props} />;
          };
        }
        ```

    - 요약
      - Suspense는 React 내장 기능이지만, React Query, Zustand 등 외부 상태 관리 도구의 로딩 제어 기능이 실무에서는 더 많이 사용
      - Suspense는 반드시 필요한 기능이라기보다, 사용 목적과 복잡도에 따라 대체 가능한 역할을 함

- React에서 useImperativeHandle을 사용할 때의 장점
  - 개념 요약
    - useImperativeHandle은 부모가 자식 컴포넌트에 ref를 통해 직접적으로 특정 메서드나 속성만 사용할 수 있도록 제어하는 훅
    - forwardRef와 함께 사용됨

  - 장점
    - 캡슐화 유지: 내부 구현 세부사항은 숨기고 필요한 기능만 노출
    - 명확한 API 제공: ref를 통한 접근 범위를 제한하여 의도치 않은 접근 방지
    - 제어 가능한 DOM 접근: input 포커스, 재생 컨트롤 등 imperative 동작을 안전하게 제공

  - 예시
    ```tsx
    const CustomInput = forwardRef((props, ref) => {
      const inputRef = useRef();

      useImperativeHandle(ref, () => ({
        focus: () => inputRef.current.focus()
      }));

      return <input ref={inputRef} />;
    });
    ```

  - 요약
    - 직접 DOM 조작이 필요한 상황에서 자식 컴포넌트를 외부에 안전하고 명확하게 제어할 수 있는 API를 만들어줍니다.

- React에서 useId() Hook
  - 개념 요약
    - useId()는 React 18에서 도입된 훅으로, 고유하고 일관된 ID를 생성할 수 있습니다. 
    - SSR(Server Side Rendering)과 CSR(Client Side Rendering) 간의 ID mismatch 문제를 방지하는 데 유용합니다.

  - 사용 사례
    - <label htmlFor="id" /> + <input id="id" /> 조합
    - 여러 인스턴스에서 고유한 ID가 필요할 때
    - Form 컴포넌트나 컴포넌트 라이브러리에서 내부적으로 고유 키가 필요한 경우

  - 예시
    ```tsx
    const id = useId();
    return (
      <>
        <label htmlFor={id}>이름</label>
        <input id={id} type="text" />
      </>
    );
    ```

  - 요약
    - useId()는 HTML 요소의 id가 서버/클라이언트 사이에서 일치하도록 보장하며, 여러 컴포넌트 인스턴스에서도 충돌 없는 고유 ID를 만들어줍니다.

- React에서 Error Boundaries의 적용 사례
  - 개념 요약
    - Error Boundary는 컴포넌트 트리에서 예외가 발생했을 때 앱 전체가 크래시되는 것을 방지하고, fallback UI로 graceful degradation을 제공하는 기능

  - 적용 사례
    - 외부 라이브러리 오류 감지: 불안정한 써드파티 위젯을 안전하게 감쌀 때
    - 전체 앱 보호: 페이지 루트 컴포넌트에 적용하여 전체 앱이 멈추는 것을 방지
    - 특정 섹션 보호: 예를 들어 Chart, VideoPlayer, CustomEditor 같은 개별 기능 단위

  - 예시
    ```tsx
    <ErrorBoundary fallback={<ErrorFallback />}>
      <ComponentThatMayThrow />
    </ErrorBoundary>
    ```

  - 요약
    - 복잡한 컴포넌트 또는 외부 의존성이 많은 영역에서 예외 발생을 방지하고, 사용자에게 의미 있는 에러 UI를 제공하는 데 필수적

- React에서 Strict Mode가 useEffect에 미치는 영향
  - 개념 요약
    - React의 StrictMode는 개발 중 잠재적인 문제를 조기에 감지하기 위한 도구로, 프로덕션에는 영향을 미치지 않습니다.

  - useEffect에 미치는 영향
    - 마운트-언마운트-리마운트 시퀀스가 한 번 더 발생함
    - React는 이 과정을 통해 effect 클린업이 잘 작성되었는지 검증
      ```tsx
      useEffect(() => {
        console.log("mounted");
        return () => console.log("unmounted");
      }, []);
      ```
    - 위 코드는 StrictMode 하에서:
      - mounted -> unmounted -> mounted 순으로 실행

  - 주의할 점
    - 초기화 비용이 큰 작업은 반드시 cleanup을 명확히 해줘야 함
    - 외부 API 구독, 타이머, socket 연결 등은 중복 연결 방지 필요

  - 요약
    - StrictMode는 useEffect 클린업 함수의 정확성과 안전성을 테스트하기 위해 마운트/언마운트를 반복 호출하므로, 효과적인 정리(cleanup) 코드가 필요합니다.

- React에서 Refs의 활용 사례
  - 개념 요약
    - ref는 React에서 DOM 요소나 컴포넌트 인스턴스에 직접 접근할 수 있게 해주는 도구
    - useRef() 훅으로 생성하며 렌더 사이클과 무관한 데이터를 저장하거나 imperative한 조작에 사용

  - 주요 활용 사례
    - DOM 제어: 포커스 이동, 스크롤 위치 조정 등
      ```tsx
      const inputRef = useRef();
      useEffect(() => inputRef.current.focus(), []);
      ```

    - 비동기 작업 중 상태 추적: 최신 상태 값을 기억하여 race condition 방지
      ```tsx
      const latestData = useRef(data);
      useEffect(() => { latestData.current = data }, [data]);
      ```

    - 애니메이션 제어: canvas, SVG, GSAP 등과 연동
    - 타이머 및 interval ID 저장: 클린업용 ID 저장소
    - 외부 라이브러리 통합: Chart.js, D3, video/audio 등 DOM 접근 요구 시
    - Imperative Handle과 연계하여 부모가 자식 메서드를 호출하도록 허용

  - 요약
    - Refs는 렌더링 사이클을 거치지 않고도 상태를 보존하거나 DOM/외부 객체를 제어할 수 있어, UI 제어와 비동기 안정성 확보에 유리합니다.

- React에서 클라이언트 측에서 API 호출을 최적화하는 방법
  - 주요 전략
    - 의존성에 따른 조건부 호출: useEffect의 의존 배열에 정확한 deps 지정
    - Debounce / Throttle: 검색어 입력 등 빠른 변화에 대한 과도한 호출 방지
    - 캐싱: React Query, SWR 등 라이브러리 활용
    - 중복 호출 방지: 상태/플래그로 동일 API 다중 호출 방지
    - Pre-fetching: 사용자가 도달할 가능성이 높은 페이지 데이터를 미리 요청
    - Pagination / Infinite Scroll: 필요한 데이터만 단계적으로 호출
    - 서버 상태 관리 도구 사용: react-query, swr은 자동 리패치, 캐싱, 오류 재시도 등을 내장

  - 요약
    - API 최적화는 “불필요한 호출을 피하고, 필요한 데이터만 가져오며, 중복되지 않게 잘 저장하고 관리”하는 것이 핵심입니다.

- React에서 Custom Hooks를 만드는 원칙
  - 개념 요약
    - Custom Hook은 로직을 재사용하기 위해 use로 시작하는 함수
    - 일반적으로 useState, useEffect, useRef 등 내부에서 훅을 사용할 수 있습니다.

  - 제작 원칙
    - "use"로 시작: 훅이라는 신호를 React에게 전달 (컴포넌트 렌더링 추적 목적)
    - 다른 훅을 내부에서 호출 가능
    - 조건문 안에서 훅을 사용하면 안 됨
    - 단일 책임 원칙: 한 가지 목적에 집중한 훅
    - 재사용 가능한 인터페이스 설계: 컴포넌트 간 공유 가능한 API 제공

  - 예시
    ```tsx
    function useWindowWidth() {
      const [width, setWidth] = useState(window.innerWidth);
      useEffect(() => {
        const handleResize = () => setWidth(window.innerWidth);
        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
      }, []);
      return width;
    }
    ```

  - 요약
    - Custom Hook은 공통된 상태나 비즈니스 로직을 재사용하고 구조화하는 강력한 수단이며, 유지보수성과 테스트성 향상에 기여

- React에서 Props Drilling이 문제를 일으키는 이유
  - 개념 요약
    - 필요한 props를 직접 필요로 하지 않는 중간 컴포넌트들을 거쳐 하위 컴포넌트로 전달하는 것입니다.

  - 문제가 되는 이유
    - 컴포넌트 의존성 증가: 상위 구조가 변경되면 중간 컴포넌트들도 영향을 받음
    - 유지보수 어려움: 하위로 갈수록 어떤 값이 어디서 오는지 추적이 힘들어짐
    - 재사용성 저하: 중간 컴포넌트가 특정 props에 의존하게 되어 범용성이 떨어짐
    - 복잡한 트리 구조에서 성능 저하: 불필요한 리렌더링 유발

  - 해결책
    - Context API 사용: 전역 상태로 전달하여 깊은 트리에서 직접 접근
    - 상태 분리: 상태를 더 가까운 공통 조상 컴포넌트로 끌어올리기
    - 상태 관리 라이브러리: Redux, Recoil, Zustand 등 활용

  - 요약
    - Props Drilling은 UI 트리 구조가 깊어질수록 유지보수와 상태 흐름의 추적이 어려워지고, 이를 해결하려면 상태를 더 효율적인 방식으로 공유하거나 저장하는 방법이 필요합니다.

- React에서 React.memo()와 useMemo()의 차이점
  - React.memo()
    - 컴포넌트의 리렌더링 방지
    - 함수형 컴포넌트 전체 적용
    - props가 변경되지 않으면 컴포넌트 리렌더 생략
    - 내부적으로 props shallow 비교
    - <React.memo(MyComponent) />

  - useMemo()
    - 값 계산을 메모이제이션
    - 일반 변수나 계산식의 결과
    - 동일한 의존성이 유지되면 캐시된 값 반환
    - useMemo(fn, [deps])로 명시적 전달
    - const result = useMemo(() => expensiveCalc(), [input])

  - 요약
    - React.memo는 컴포넌트 리렌더 방지용
    - useMemo는 계산된 값 재사용용
      - 둘은 유사한 목적이나 적용 대상과 맥락이 다름

- React에서 웹 성능을 최적화하는 기법
  - 주요 최적화 전략
    - 코드 스플리팅 & Lazy Loading
      - React.lazy, Suspense, dynamic import 사용하여 초기 JS 로딩 최소화
    - 리렌더링 최소화
      - React.memo, useMemo, useCallback, key 설정 등 활용
    - 이미지 최적화
      - 적절한 이미지 포맷(WebP 등), lazy loading, responsive size
    - Virtualization
      - 많은 리스트를 효율적으로 렌더링 (react-window, react-virtualized)
    - 서버 상태 캐싱
      - React Query, SWR 등 사용하여 API 요청 중복 방지
    - 브라우저 캐싱 & CDN 사용
      - 정적 자산과 리소스를 효율적으로 배포
    - Critical CSS & 폰트 최적화
      - 렌더 블로킹 리소스를 최소화

  - 요약
    - 성능 최적화는 "필요할 때만 렌더, 필요한 만큼만 로드, 가능한 빨리 보여주기"가 핵심

- React에서 useEffect의 Dependency Array의 역할
  - 개념 요약
    - Dependency Array ([dep1, dep2])는 useEffect()가 언제 실행될지를 명시적으로 제어하는 역할

  - 동작 방식
    - []: 컴포넌트 마운트 시 1회만 실행
    - [a, b]: a 또는 b가 변경될 때마다 effect 실행
    - 생략 시: 매 렌더링마다 실행 → 성능 저하 위험

  - 의미
    - 의존성 배열은 React에게 “이 값들이 바뀌면 effect를 다시 실행해야 한다”는 신호
    - 배열이 불완전하거나 참조가 매번 바뀌는 값이 있다면, 의도치 않은 재실행 발생

  - 예시
    ```tsx
    useEffect(() => {
      fetchData();
    }, [id]); // id가 바뀔 때마다 호출됨
    ```

  - 정리
    - 정확한 의존성 배열은 불필요한 리렌더링 방지와 의도한 동작 보장에 중요

- React에서 useState와 useReducer 중 어떤 경우에 useReducer를 선택하는 것이 좋은가?
  - useState는 간단한 상태일 때 적합
    - 단일 값 (예: toggle, input)
    - 복잡한 로직 없이 바로 업데이트되는 상태

  - useReducer가 더 나은 경우
    - 상태 값이 객체 또는 배열로 구성된 복합 상태
    - 상태 업데이트가 다양한 액션에 따라 조건부로 분기
    - 여러 상태 업데이트가 서로 관련되거나 동시에 변경되어야 할 때
    - 상태 관리 로직을 외부로 추출하고 싶을 때 (가독성과 테스트성 ↑)
    - 복잡한 폼 상태, 다중 입력 처리, 상태 기반 UI 로직

  - 예시
    ```tsx
    const [state, dispatch] = useReducer(reducer, initialState);
    dispatch({ type: 'increment' });
    ```

  - 요약
    - useState: 간단하고 직관적인 상태에 적합
    - useReducer: 복잡한 상태 로직이나 상태 간 의존성이 있는 경우에 더 적합

- React에서 Strict Mode가 useEffect 내부의 cleanup 함수에 미치는 영향
  - 개념 요약
    - React의 StrictMode는 개발 환경에서만 동작하며, 잠재적인 사이드 이펙트나 메모리 누수를 조기에 감지하기 위해 일부 라이프사이클을 의도적으로 두 번 실행

  - useEffect에 대한 영향
    - StrictMode 하에서는 useEffect → cleanup → useEffect 순으로 한 번 더 실행됨
    - 이는 실제 동작과 다르지만, effect의 클린업이 제대로 작성되어 있는지 검증하는 용도
    - mount -> unmount -> mount 로 호출
      - OFF 일 때는 mount 만 호출되며 실제 컴포넌트가 사라질 때만 unmount 실행됨

  - 주의점
    - 외부 API, WebSocket, Timer 등을 다룰 때 중복 연결/요청 주의
    - 클린업 함수가 안정적이고 idempotent 하도록 구현해야 함

- React에서 Suspense를 활용하여 비동기 데이터를 처리하는 방법
  - 개념 요약
    - Suspense는 React에서 비동기 컴포넌트가 데이터를 로드하는 동안 대기 상태(fallback UI)를 표시할 수 있게 해주는 기능

  - 기본 사용 방식 (리액트 18 이상)
    ```tsx
    const userPromise = fetchUser(); // Promise 객체

    function UserInfo() {
      const user = use(userPromise); // React 18의 실험적 use()
      return <div>{user.name}</div>;
    }

    function App() {
      return (
        <Suspense fallback={<div>로딩 중...</div>}>
          <UserInfo />
        </Suspense>
      );
    }
    ```

  - React Query와 결합하여 Suspense 사용
    ```tsx
    const { data } = useQuery(['user'], fetchUser, { suspense: true });

    <Suspense fallback={<div>불러오는 중...</div>}>
      <UserComponent />
    </Suspense>
    ```

  - 장점
    - 로딩 상태를 컴포넌트 수준에서 선언적으로 처리 가능
    - 코드 분할과 데이터 로딩 UI를 통합 관리
    - 서버 컴포넌트(React Server Components)와도 잘 통합됨

  - 주의사항
    - use()와 Server Components는 아직 실험적 단계
    - 실무에서는 React Query, SWR처럼 라이브러리와 함께 사용하는 것이 일반적

- React에서 fetch API와 Axios의 차이점
  - fetch
    - 브라우저 내장
    - 수동 .json() 호출 필요
    - 에러 처리: 4xx/5xx도 성공으로 처리됨
    - AbortController 직접 구현으로 요청 취소
    - 인터셉터 없음
    - 최소한의 기능

  - Axios
    - 외부 라이브러리 설치 필요
    - 자동 파싱 (data에 바로 접근)
    - HTTP 에러 자동 catch 처리
    - 요청 취소를 위해 CancelToken or AbortController 지원
    - 인터셉터 요청/응답 가로채기 가능
    - 기본 헤더 설정, 타임아웃, 전역 설정 등 풍부

  - 요약
    - fetch: 기본적인 요청에 적합, 가볍고 설치 필요 없음
    - axios: 더 나은 DX (개발 경험)과 에러/인터셉터 지원 등으로 실무에서 자주 사용

- React에서 렌더링 최적화를 위해 할 수 있는 방법
  - 컴포넌트 최적화
    - React.memo()로 불필요한 리렌더링 방지
    - useMemo()로 계산 결과 캐싱
    - useCallback()으로 함수 재생성 방지

  - 상태 최적화
    - 상태를 필요한 컴포넌트에만 유지 (불필요한 상위 상태 지양)
    - Context 사용 시 useContextSelector, memo와 병행

  - 가상 리스트
    - 긴 리스트는 react-window, react-virtualized로 가상화 처리

  - 코드 분할 & Lazy Loading
    - React.lazy() + Suspense 사용
    - 라우팅 기반 코드 스플리팅 (React Router Lazy Routes)

  - 서버 상태 캐싱
    - React Query, SWR 등으로 API 데이터 캐싱 및 중복 요청 방지

  - 이미지 및 자산 최적화
    - WebP 등 경량 이미지 포맷 사용
    - <img loading="lazy" /> 또는 Lazy 컴포넌트

  - 요약
    - React의 렌더링 최적화는 렌더 트리 최소화, 계산 중복 방지, 비동기 처리 효율화를 통해 성능과 사용자 경험을 개선하는 것

- React에서 React.lazy()와 Loadable Components의 차이점
  - React.lazy()
    - 리액트 내장 (리액트 16.6+)
    - SSR 지원하지 않음
    - Preloading 지원은 직접 구현 필요
    - 로딩 상태는 Suspense와 함께 사용
    - 코드 분할 지원

  - Loadable Components
    - 외부 라이브러리 설치 필요
    - SSR 지원
    - .preload()등 제공
    - 자체 fallback 지원 (Suspense 선택 가능)
    - 코드 분할 지원, 더 유연한 지원 (React.lazy() 보다 유연)

  - 요약
    - React.lazy()는 간단한 클라이언트 전용 코드 스플리팅에 적합
    - Loadable Components는 SSR이 필요한 경우, 서버 + 클라이언트 모두 지원해야 할 때 사용

- React에서 useEffect의 cleanup 함수는 언제 호출되는가
  - 컴포넌트가 언마운트될 때
    - 예: 화면 전환, 조건부 렌더링 등으로 해당 컴포넌트가 제거되면
  - 의존성 배열이 변경될 때 ( [deps] )
    - 이전 effect를 정리하고, 새로운 값에 따라 다시 effect 실행
  - (개발 모드 한정) React.StrictMode로 인해 한 번 더 호출되는 경우
    - useEffect → cleanup → useEffect 순서로 호출되어 메모리 누수 여부 검증

- React에서 useCallback을 사용해야 하는 경우
  - 개요
    - useCallback(fn, deps)은 함수 참조가 매번 새로 생성되는 것을 막기 위한 훅입니다.

  - 사용해야 하는 대표 시나리오:
    - 함수를 자식 컴포넌트에 props로 전달할 때
      - → 자식이 React.memo로 감싸져 있는 경우, 함수 참조가 바뀌면 리렌더 발생

    - 함수가 의존성 배열에 포함되어야 할 때
      - → useEffect, useMemo 등에서 함수가 의존성일 경우 참조 안정성 확보

    - 빈번한 리렌더링이 있는 성능 민감한 컴포넌트에서
      - → 렌더링마다 함수가 재생성되면 불필요한 연산/효과 발생

  - 예시
    ```tsx
    const handleClick = useCallback(() => {
      doSomething();
    }, [dependency]);
    ```

  - 주의점
    - 불필요하게 모든 함수를 useCallback으로 감싸면 오히려 메모리 낭비나 복잡도 증가 가능. 리렌더링 영향이 있는 경우에만 사용 필요

- React에서 Forward Ref를 사용하는 시나리오
  - 개요
    - forwardRef는 부모가 자식 컴포넌트 내부의 DOM 또는 Imperative 메서드에 접근할 수 있게 해주는 기능

  - 사용 시나리오
    - 재사용 가능한 input 컴포넌트를 만들고 부모에서 포커스를 제어하고 싶을 때
      ```tsx
      const MyInput = forwardRef((props, ref) => <input ref={ref} {...props} />);
      ```

    - 모달/툴팁/비디오 등에서 외부에서 직접 조작이 필요한 경우
      - 예: scrollToTop(), play(), close() 등 외부에서 호출해야 할 함수

    - useImperativeHandle과 함께 제어된 기능만 외부로 노출할 때
      ```tsx
      useImperativeHandle(ref, () => ({
        focus: () => inputRef.current.focus(),
      }));
      ```

    - 폼 라이브러리에서 ref 기반 등록이 필요한 경우
      - 예: react-hook-form의 register()와 함께 사용하는 커스텀 컴포넌트

  - 요약
    - forwardRef는 컴포넌트 추상화와 외부 제어 사이의 균형을 잡기 위한 도구
    - DOM 조작, imperative 제어가 필요한 컴포넌트에 적합

- React에서 useRef를 활용하여 DOM 요소에 직접 접근하는 방법
  - 개요
    - useRef는 DOM 요소에 직접 접근하거나 값 저장소처럼 사용할 수 있는 훅

  - DOM 접근 예시
    ```tsx
    function MyComponent() {
      const inputRef = useRef<HTMLInputElement>(null);

      useEffect(() => {
        inputRef.current?.focus(); // 마운트 시 포커스
      }, []);

      return <input ref={inputRef} />;
    }
    ```

  - 활용 사례
    - 포커스 제어 (.focus())
    - 스크롤 이동 (scrollIntoView, scrollTop)
    - 비디오 제어 (play(), pause())
    - 외부 라이브러리(D3, Chart.js 등) DOM 연동

  - 요약
    - useRef는 렌더링에 영향을 주지 않고 DOM에 imperative하게 접근할 수 있는 가장 안전한 방법입니다.

- React에서 useEffect와 useMemo를 함께 사용할 때 주의할 점
  - 핵심 차이
    - useMemo: 계산된 값을 메모이제이션
    - useEffect: 사이드 이펙트 실행 (예: API 호출, 이벤트 등록)

  - 주의할 점
    - useMemo 내부에서 부수효과를 실행하지 말 것 → 이건 useEffect의 책임
      ```tsx
      // 부적절
      const data = useMemo(() => {
        fetch(...); // 부수효과 실행 X
        return value;
      }, [deps]);
      ```
    - useEffect에서 useMemo 결과에 의존할 경우 의존성 배열 정확히 설정
      ```tsx
      const memoizedValue = useMemo(() => computeValue(input), [input]);

      useEffect(() => {
        doSomethingWith(memoizedValue);
      }, [memoizedValue]);
      ```

  - 요약
    - useMemo: 순수 함수의 결과 캐싱
    - useEffect: 사이드 이펙트 전담
    - 함께 사용할 땐 역할 분리를 명확히 하고 의존성 배열 정확히 명시해야 함

- React에서 CSR과 SSR의 성능 차이는 어떤 요소에서 발생
  - CSR (Client-Side-Rendering)
    - 첫 페이지 표시 속도 느림 (JS 로딩 후 렌더)
    - SEO 대응력 약함 (크롤러가 JS 해석 핋요)
    - 초기 로딩 JS 크기 큼 (모든 UI 로직 포함)
    - TTV (Time to View): 느릴 수 있음
    - 인터렉션 가능 시점은 렌더링 완료 후 가능
    - 복잡도는 상대적으로 단순

  - SSR (Server-Side-Rendering)
    - 첫 페이지 표시 속도는 빠름 (HTML 바로 렌더) 
    - SEO 대응력 강함 (HTML 제공)
    - 초기 로딩 JS 크기 (상대적 감소)
    - TTV (Time to View): 빠르게 컨텐츠 표시 가능
    - 인터랙션 가능 시점은 hydration 까지 필요
    - 복잡도는 SSR 설정, 데이터 prefetch 복잡함

  - 요약
    - CSR: 빠른 개발, 초기 로딩 느릴 수 있음
    - SSR: SEO와 초기 UX에 유리, 하지만 서버 부하 높고 복잡성 높음

- React에서 서버 사이드 렌더링 시 데이터 페칭 처리 방법
  - 개요
    - SSE 환경에서 데이터 페칭을 처리하는 방식은 프레임워크에 따라 상이

  - Next.js 기준 (대표 SSR 프레임워크)
    - getServerSideProps(): SSR 시점에 실행되는 데이터 페칭 함수
      ```tsx
      export async function getServerSideProps(context) {
        const res = await fetch("https://api.example.com/data");
        const data = await res.json();

        return {
          props: { data },
        };
      }
      ```
    - getStaticProps() + revalidate: SSG + ISR(Incremental Static Regeneration)

  - Custom SSR 환경 (Express + React 등)
    - 서버에서 React 앱 렌더링 전 fetch() 등으로 데이터를 준비
    - ReactDOMServer.renderToString() 전에 props로 데이터 전달
    - 클라이언트에서 hydrate() 사용해 HTML에 이벤트 바인딩

  - 주의점
    - 서버에서는 브라우저 API(window, localStorage 등) 사용 불가
    - API 호출은 반드시 node-fetch 같은 서버용 클라이언트 사용

  - 요약
    - SSR 시에는 렌더링 전에 데이터를 준비해 props로 전달하거나, Next.js 같은 프레임워크의 전용 API를 사용하는 것이 일반적입니다.

- React에서 Styled Components를 사용할 때의 장점과 단점
  - 장점
    - 컴포넌트 단위의 스타일 캡슐화
    - props 기반 동적 스타일링 가능
    - 자동 클래스명 해시 처리 > 충돌 방지
    - SSR 및 테마 지원
    - JavaScript 내에서 조건/반복 가능

  - 단점
    - 런타임 비용 발생 (스타일 생성 시점)
    - 빌드 사이즈 증가
    - TypeScript와 함께 사용 시 타입 추론 제한
    - CSS in JS 자체의 성능 이슈: Large DOM 트리일수록 성능 저하 가능

  - 요약
    - Styled Components 는 개발 경험과 유지보수시 강점
    - 퍼포먼스 민감 앱/웹에서는 선택할지에 대한 고려 필요

- React에서 Redux를 사용하면 불필요한 렌더링이 발생할 수 있는 이유
  - 발생 이유 (참조형 비교, Shallow Comparison)
    - useSelector()는 상태의 참조형 비교(shallowEqual)를 기반으로 리렌더링 결정
    - 상태 객체(예: 배열, 객체)가 새로 생성되면 이전 값과 같더라도 리렌더링 발생
    - 모든 컴포넌트가 같은 전역 상태를 참조할 경우, 일부 변경에도 전역 리렌더링 발생 가능

  - 해결 방법
    - React.memo + shallowEqual 사용
    - reselect로 메모이제이션된 selector 사용
    - Slice를 나누어 최소 범위에서 구독

- React에서 Redux Persist를 사용하는 이유
  - 기능 요약
    - 리덕스 상태를 로컬 스토리지에 저장
    - 앱 새로고침 후에도 상태 유지 가능
    - 로그인 상태, 장바구니, UI 설정 등 사용자 세션 유지에 유용

  - Redux Persist 이점
    - 사용자 경험 향상
    - 복잡한 앱에서 초기화 방지
    - 스토어 재 Hydration 자동 처리

- React에서 Context API를 사용하면 발생할 수 있는 성능 이슈
  - 문제
    - Context.Provider의 value가 변경되면 해당 context를 구독 중인 모든 컴포넌트가 리렌더링됨

  - 예시
    ```tsx
    <MyContext.Provider value={{ count }}>
      <CompA />  // count와 관련 없음 → 그래도 리렌더
    </MyContext.Provider>
    ```

  - 해결 방법
    - value를 useMemo로 감싸거나
    - context-selector, zustand, Recoil 등 분리 가능한 상태 관리 라이브러리 사용

- React에서 리렌더링을 줄이기 위한 best practice
  - 컴포넌트 메모이제이션
    - React.memo(Component)
      - props가 변경되지 않으면 리렌더링 방지
        ```tsx
        const MyComponent = React.memo(({ title }) => {
          return <div>{title}</div>;
        });
        ```
        - 단, props가 객체/함수일 경우 참조가 바뀌면 무조건 리렌더됨 → useCallback, useMemo와 함께 써야 함
  - 불필요한 State 분리
  - 함수/객체는 useCallback/useMemo 로 캐싱
    ```tsx
    const handleClick = useCallback(() => {
      // 함수 내용
    }, [deps]);

    const memoizedValue = useMemo(() => {
      return computeHeavyValue(data);
    }, [data]);
    ```
    - props로 넘기는 함수/객체가 매번 새로 생성되면 하위 컴포넌트가 리렌더됨
    - React.memo와 함께 사용할 때 필수
  - Context 최소화 또는 분리
    - Context 업데이트는 context를 구독하는 모든 하위 컴포넌트를 리렌더링시킴
    - 해결 방법
      - Context를 작게 나누기 (예: ThemeContext, UserContext, ModalContext 등)
      - 정말 자주 바뀌는 데이터는 Zustand, Redux, Recoil 같은 외부 상태관리 도구로
  - 리스트 렌더링 최적화
    - key 속성을 항상 고유하게 설정
      ```tsx
      {items.map(item => (
        <Item key={item.id} data={item} />
      ))}
      ```
      - index를 key로 쓰면, 정렬/삭제 시 문제 발생 → 가상화된 리스트에서만 예외적으로 허용
  - 컴포넌트 분할
    - 큰 컴포넌트는 자주 바뀌는 부분과 안 바뀌는 부분을 분리
      ```tsx
      const Parent = () => {
        const [count, setCount] = useState(0);
        return (
          <>
            <StaticHeader /> {/* 리렌더 없음 */}
            <ChangingContent count={count} />
          </>
        );
      };
      ```
  - useDeferredValue로 저우선 렌더링 처리 (React 18+)
    - 입력값 변경은 즉시 반영하지만, 렌더링은 천천히 수행
  - 이벤트 핸들러에서 setState 최소화
    - 여러 상태를 동시에 변경하면, 하나로 묶어 처리
      ```tsx
      // 비효율적
      setA(1); setB(2);

      // 더 나은 방식
      setState({ a: 1, b: 2 });
      ```
  - 성능 측정 도구도 함께 활용
    - React DevTools -> Profiler 탭
      - 어떤 컴포넌트가 왜 리렌더되는지 확인
    - why-did-you-render 라이브러리
      - 불필요한 리렌더링 원인을 자동 추적

- React에서 Next.js의 getStaticProps와 getServerSideProps의 차이점
  - getStaticProps
    - 실행 시점: 빌드 타임(앱이 배포되기 전에 한 번 실행됨)
    - 용도: 정적인 콘텐츠 생성 (ex. 블로그, 제품 소개 페이지)
    - 특징:
      - CDN 캐시 가능 → 빠른 성능 제공
      - 데이터가 자주 변하지 않는 경우 적합
      - revalidate 옵션으로 ISR(Incremental Static Regeneration)도 가능

  - getServerSideProps
    - 실행 시점: 매 요청 시마다 서버에서 실행됨
    - 용도: 요청마다 최신 데이터가 필요한 페이지 (ex. 사용자 대시보드, 실시간 통계)
    - 특징:
      - 항상 최신 데이터를 보장
      - 서버 부하 증가 가능
      - 캐시가 어려움

- React에서 getInitialProps와 getServerSideProps의 차이
  - getInitialProps
    - 사용 가능 위치: _app, _document, 커스텀 페이지 컴포넌트
    - 렌더링 방식: 서버와 클라이언트 모두에서 실행 가능 (context에 따라 다름)
    - 단점:
      - 자동 Static Optimization 비활성화됨
      - 데이터 fetch가 느려질 수 있음
      - Next.js 최신 권장 방식 아님

  - getServerSideProps
    - Next.js 공식 권장 방식 (SSR 용도)
    - 서버에서만 실행 → 클라이언트에는 노출되지 않음
    - 최신 방식이며, 더 명확한 실행 시점과 분리된 역할 제공

- React에서 React Query를 사용할 때 얻을 수 있는 이점
  - 캐싱 및 상태 관리
    - 서버 상태를 클라이언트에서 효과적으로 캐싱하고 자동 갱신
    - 동일한 쿼리 키로 여러 컴포넌트에서 중복 요청을 피함

  - 자동 리페치 및 백그라운드 업데이트
    - 포커스될 때 자동으로 최신 데이터 불러오기
    - 특정 간격으로 백그라운드에서 데이터 갱신 가능

  - 로딩/에러/성공 상태 자동 관리
    - 각 상태를 명시적으로 구분하여 UX 개선에 도움

  - 개발 편의성
    - 쿼리 무효화, 프리패치, 페이징, 무한 스크롤 등 고급 기능 제공
    - 비동기 API 호출 로직을 중앙 집중식으로 관리 가능

- React에서 GraphQL을 사용할 때 고려해야 할 점
  - 데이터 설계
    - 스키마(타입 시스템)를 명확히 설계해야 함
    - 불필요한 오버패칭/언더패칭을 방지할 수 있음

  - 네트워크 비용
    - 단일 엔드포인트지만 복잡한 쿼리는 성능에 영향을 줄 수 있음
    - 정교한 쿼리 제한 및 캐싱 전략 필요

  - 클라이언트 라이브러리 선택
    - Apollo Client, urql 등 다양한 클라이언트가 있으며 프로젝트에 맞게 선택
    - 캐시 전략, 쿼리 작성 방식, SSR 지원 여부 등을 비교해야 함

  - 보안
    - 쿼리 조작, 너무 복잡한 요청 등에 대비한 쿼리 깊이 제한 필요
    - 인증/인가 전략도 REST와 다르게 설계해야 할 수 있음

- React에서 상태 관리 라이브러리를 사용하지 않고 상태를 관리하는 방법
  - 기본 방식
    - useState, useReducer: 컴포넌트 내부 상태 관리
    - useContext: 전역 상태처럼 공유할 수 있음

  - 구조적 예시
    - 상위 컴포넌트에서 상태를 만들고 props로 하위에 전달 (Prop drilling)
    - 필요 시 Context API와 useReducer를 조합해 간단한 전역 상태 관리도 가능

  - 한계
    - 중첩 구조에서 prop drilling 문제
    - 복잡한 비동기 흐름 및 캐싱은 별도 구현 필요

- React에서 Apollo Client를 사용할 때의 장점
  - GraphQL 전용 클라이언트
    - 요청, 응답, 상태 관리를 GraphQL에 최적화된 구조로 처리

  - 캐싱
    - 자동으로 결과를 캐싱하고, 동일 쿼리 시 빠른 재사용 가능
    - InMemoryCache를 통한 고성능 캐싱 제공

  - DevTools 및 쿼리 추적
    - Apollo DevTools로 쿼리 요청/응답, 캐시 상태 확인 가능

  - 다양한 기능 지원
    - 쿼리, 뮤테이션, 서브스크립션 모두 지원
    - SSR, 오류 처리, 리페치, 로딩 상태 관리 등 내장

- React에서 SWR과 React Query의 차이점
  - 공통점
    - 데이터 패칭 라이브러리
    - 캐싱, 자동 리페치, 에러/로딩 상태 관리 가능

  - SWR (by Vercel)
    - 더 단순하고 가벼움
    - 기본 철학: "Stale While Revalidate"
    - 주로 Next.js와 함께 사용됨
    - 커스터마이징 자유도가 적은 편

  - React Query (by TanStack)
    - 더 풍부한 기능: 쿼리 무효화, 무한스크롤, mutation, 비동기 전역상태 관리
    - 서버 상태 관리 도구로 쓰임
    - 커스터마이징 및 확장성 뛰어남

- React에서 Suspense를 활용한 데이터 캐싱 기법
  - Suspense 개념
    - 비동기 컴포넌트 렌더링 중 fallback UI를 보여줄 수 있는 리액트 기능

  - 사용 예시
    ```tsx
    <Suspense fallback={<Loading />}>
      <MyComponent />
    </Suspense>
    ```

  - 데이터 캐싱 활용
    - React 18 이후 use() API로 서버 사이드 렌더링(Suspense 지원 라이브러리)에서 활용 가능
    - react-fetch, Relay, React Query, SWR에서 experimental Suspense 연동 기능 지원

- React에서 Formik과 React Hook Form의 차이점
  - Formik
    - 클래스/함수 컴포넌트 모두 지원.
    - 상태를 내부적으로 useState로 관리 → 렌더링 횟수 많음.
    - validation: 자체 방식 + Yup 등 외부 라이브러리와 통합.
    - 초기 학습 난이도는 낮지만, 성능은 상대적으로 떨어짐.
    - 제어 컴포넌트 중심 (controlled input).

  - React Hook Form
    - ref 기반으로 DOM을 추적 → 렌더링 최소화.
    - 비제어 컴포넌트(uncontrolled input)를 기본으로 사용.
    - 폼이 클수록 성능 이점 큼.
    - Yup, Zod 등 스키마와 유연하게 통합 가능.
    - 초기 설정이 약간 까다로울 수 있으나 훨씬 경량.

  - 정리:
    - React Hook Form은 성능과 확장성 측면에서 최근 트렌드에 더 적합.
    - Formik은 간단한 폼에 빠르게 도입하기 좋음.

- React에서 Jest와 React Testing Library를 활용한 테스트 방법
  - Jest
    - 테스트 러너 및 어서션 도구.
    - 단위 테스트, 모킹, 스냅샷 등 전반적 테스트 도구 제공.
    - React에 국한되지 않고 범용적으로 사용 가능.
    - jest.mock() 등을 통해 종속성 주입을 쉽게 제어 가능.

  - React Testing Library (RTL)
    - 사용자 관점 중심의 DOM 상호작용 테스트.
    - getByText, getByRole 등 접근성 기반 쿼리 사용.
    - 내부 구현이 아닌, 외부 행동을 테스트하게 유도.
    - Jest와 함께 사용하는 것이 일반적 (RTL 단독 사용은 드뭄).

  - 정리:
    - RTL은 UI를 사용자처럼 테스트할 수 있게 해주고, Jest는 그 테스트를 구동하고 모킹할 수 있는 도구

- React에서 Cypress와 Jest의 차이점
  - Cypress
    - 브라우저 기반 E2E 테스트 도구.
    - 실제 DOM에서 마우스 클릭, 입력 등 실제 사용자 시뮬레이션.
    - 비동기 UI 테스트에 강하고 디버깅이 편함.
    - 개발 속도가 느리고, 테스트 환경 셋업이 비교적 무거움.

  - Jest
    - 단위/통합 테스트에 특화.
    - DOM이 아닌 JS 로직, 컴포넌트 단위 검증.
    - 브라우저 없이 실행되므로 빠름 (JSDOM 환경).
    - 실제 브라우저 상호작용은 제한적.

  - 정리:
    - Cypress → E2E 테스트용 (사용자 여정 검증).
    - Jest → 단위/통합 테스트용 (컴포넌트 로직 검증).

- React에서 테스트 코드 작성 시 고려해야 할 사항
  - 사용자 관점에서 시나리오 구성 (ex. 버튼 클릭 → 결과 출력).
  - 모킹 필요 최소화 → 실제 동작에 가까운 테스트 유지.
  - 단순 구현 테스트 X → 비즈니스 로직 중심 테스트.
  - 유지보수 가능성 고려 → 내부 로직보다 UI 변화에 유연해야 함.
  - 테스트 명세는 행동 중심으로 (ex. “사용자가 A를 하면 B가 보여야 한다”).

- React에서 상태 기반 렌더링을 수행할 때 성능을 최적화하는 방법
  - React.memo로 불필요한 재렌더링 방지.
  - useMemo, useCallback으로 연산/함수 재생성 최소화.
  - 컴포넌트 분리: 상태 변화 범위를 좁히기 위해 로컬화.
  - 상태 업데이트 배치(batch) 처리 → 여러 상태를 한 번에 변경.
  - 가상화(lazy rendering): 긴 리스트는 react-window 등 사용.

- React에서 ESM과 CommonJS의 차이점
  - CommonJS
    - require() 및 module.exports 방식.
    - 동기적 로딩: 서버 환경(Node.js) 최적화.
    - 기존 Node 프로젝트에서 여전히 사용됨.

  - ESM (ECMAScript Modules)
    - import / export 문법.
    - 비동기적 로딩 지원 → 브라우저 환경에 적합.
    - Tree Shaking 가능 → 번들 크기 감소.
    - 현대적인 JS 프로젝트의 표준.

  - 정리:
    - ESM은 브라우저와 모던 빌드 도구에 최적화된 방식, 앞으로의 표준
    - CommonJS는 Node.js 레거시 환경에서 주로 사용.

- React에서 Webpack과 Vite의 차이점
  - Webpack
    - 복잡한 설정 가능, 플러그인 생태계 풍부.
    - 번들링 중심 → 초기 빌드 속도 느림.
    - HMR(핫 모듈 리플레이스먼트)은 느릴 수 있음.
    - 대규모 엔터프라이즈에서 여전히 많이 사용됨.

  - Vite
    - ESM 기반 → 즉시 모듈 로딩.
    - 번들 없이 dev 서버 구동 가능 → 매우 빠름.
    - Rollup 기반의 프로덕션 빌드 → 경량 번들 생성.
    - React, Vue 등과의 통합 우수.

  - 정리:
    - Vite는 개발자 경험 중심의 차세대 번들러
    - Webpack은 고도화된 설정이 필요한 프로젝트에 적합

- React에서 Tree Shaking 개념
  - Tree Shaking 개념
    - 사용되지 않는 (dead code) Javascript 모듈을 최종 번들에서 제거하는 최적화 기법
    - 리액트 자체 기능 아니며, 웹팩, 롤업 등 모듈 번들러가 ESM(ES6 Module)을 분석하여 실행
  - React에서의 적용 예시
    - import { Button } from 'library' 처럼 필요한 모듈만 불러오면, 사용하지 않은 부분은 제거됨
    - default export 보다 named export를 사용하는 것이 tree-shake-friendly 함.

- React에서 Dynamic Import를 활용한 코드 스플리팅 기법
  - React.lazy()와 import()를 사용해 컴포넌트를 지연 로딩할 수 있음.
  - 페이지 단위 또는 특정 컴포넌트 단위로 번들을 분리해 초기 로딩 속도 개선.
  - Webpack이 자동으로 코드 청크를 분리하여 필요 시 로드

- React에서 Suspense의 기본 개념과 활용 방법
  - 비동기 컴포넌트 로딩 중 fallback UI를 표시할 수 있는 컴포넌트.
  - React.lazy()와 함께 사용하여 로딩 중 상태를 제어.
  - 향후 데이터 페칭 (e.g., React 18의 use API)에도 확장 가능.

- React에서 useDeferredValue()의 활용 사례
  - 값 업데이트를 지연시켜 UI의 렌더링 우선순위를 조절할 수 있음.
  - 고비용 연산을 포함한 하위 컴포넌트를 부드럽게 업데이트할 때 사용.
  - 입력창 반응성은 유지하면서, 값 반영은 비동기로 처리.

- React에서 useTransition()을 사용할 때 얻을 수 있는 이점
  - 상태 업데이트를 두 가지 우선순위로 나눔: urgent(즉시), transition(지연 가능).
  - 사용자는 입력을 즉시 반영하고, 무거운 작업(리스트 필터 등)은 부드럽게 처리.
  - UI 블로킹 없이 자연스러운 사용자 경험 제공.

- React에서 useSyncExternalStore()의 역할
  - 외부 상태 저장소(예: Redux, Zustand)와 React를 안정적으로 동기화하는 Hook.
  - React 18에서 도입되어 Concurrent Mode에서도 일관된 스냅샷 제공.
  - 외부 스토어 구독 및 스냅샷 값을 안전하게 읽도록 보장.

- React에서 Double Rendering이 발생하는 이유
  - React Strict Mode에서 개발 중 의도적으로 컴포넌트를 두 번 렌더링함.
  - 부작용(clean-up 등)의 정확성과 순수성 검증을 위해 실행됨.
  - 실제 배포에서는 단 한 번만 렌더링되므로 걱정할 필요 없음.

- React에서 Concurrent Mode가 UI 성능에 미치는 영향
  - 렌더링을 중단하고 재시작할 수 있어 응답성이 크게 향상됨.
  - 긴 작업을 나눠 처리하고, 우선순위가 높은 업데이트(입력 등)를 먼저 반영 가능.
  - 예: useTransition, Suspense 등이 이 모드에 최적화됨.

- React에서 Profiler API를 활용하여 성능 분석을 수행하는 방법
  - <Profiler> 컴포넌트로 특정 렌더링 시점의 성능 데이터 수집.
  - onRender 콜백을 통해 렌더링 시간, 횟수, 원인 등을 파악 가능.
  - React DevTools에서 시각적으로 분석도 가능.

- React에서 Strict Mode가 상태 업데이트에 미치는 영향
  - 상태 업데이트 함수나 이펙트가 의도치 않은 부작용을 발생시키는지 감지함.
  - useEffect 내부 로직이 mount → unmount → mount 순으로 실행됨.
  - 안정성 확보를 위한 개발 도우미이며, 실제 앱 동작에는 영향 없음.

- React에서 Strict Mode를 적용할 때 발생할 수 있는 문제
  - 개발 중 useEffect, useState, constructor 등의 코드가 2회 실행되어 부작용이 중복 발생할 수 있음.
  - 외부 API 호출, 타이머 설정 등 비순수한 로직에서 오류 유발 가능.
  - 실제 프로덕션에서는 1회 실행되므로, 개발 중 순수 함수 검증 목적으로만 발생.

- React에서 Next.js의 Edge Functions을 사용할 때 고려해야 할 사항
  - V8 기반 런타임에서 실행되므로 일부 Node.js API 사용 불가 (예: fs, net).
  - 빠른 응답 시간을 위해 cold start 최소화 설계 필요.
  - 지역(location) 기반 배포 고려 → 가까운 region 선택 중요.
  - 응답 크기와 실행 시간에 제한이 있으므로 경량화 필요.

- React에서 Redux Thunk를 사용하면 얻을 수 있는 장점
  - dispatch() 안에서 비동기 로직 처리 가능 (예: API 호출 후 상태 업데이트).
  - 비즈니스 로직을 Action creator에 위치시켜 컴포넌트는 순수하게 유지 가능.
  - 복잡한 흐름 제어(조건부 요청, 흐름 제어 등)에 유연하게 대응.

- React에서 Server Actions를 활용하는 방법
  - use server 디렉티브를 통해 컴포넌트 내부에서 서버 측 로직 실행 가능.
  - 클라이언트에서 서버로 함수 호출처럼 동작하며 API route 필요 없음.
  - 자동 직렬화 / 역직렬화 처리, 폼과 함께 사용 시 유용 (<form action={myServerAction}>).

- React에서 useOptimistic()을 활용한 낙관적 업데이트 구현 방법
  - 사용자의 입력에 대해 즉시 UI를 반영하되, 서버 응답 후 실제 데이터로 교체.
  - useOptimistic(prevState, updater) 패턴으로 구현.
  - 예: 댓글 작성 시 입력값을 먼저 리스트에 보여주고, 실패 시 롤백.

- React에서 React Native와 React의 차이점
  - 렌더링 대상이 다름: React는 DOM, React Native는 iOS/Android Native 컴포넌트. (DOM vs Native Component)
  - React는 HTML/CSS 사용, RN은 View/Text/StyleSheet 등 자체 UI 시스템 사용.
  - React Native는 브리지(Bridge)를 통해 네이티브 모듈과 통신함.

- React에서 Global State를 관리하는 다양한 방법
  - Context API: 간단한 전역 데이터 공유에 적합 (예: 테마, 사용자 정보).
  - Redux: 복잡한 상태, 중간 미들웨어 필요 시 유리.
  - Zustand, Jotai, Recoil: 보일러플레이트 적고 경량 전역 상태 관리 가능.
  - React Query / SWR: 서버 상태(캐싱, 동기화 등)에 특화된 글로벌 관리.
  - useContext + useReducer 조합도 간단한 대안 가능.

- React에서 Preact를 사용할 때 성능 향상을 기대할 수 있는 이유
  - React보다 훨씬 작은 번들 크기(3KB) 로 로딩 속도 향상.
  - DOM 조작이 더 가볍고 빠르게 구현되어 렌더링 성능 최적화.
  - React와 API가 유사해 마이그레이션이 쉬움.

- React에서 React.memo()를 사용하면 성능이 향상되는 원리
  - props가 변경되지 않으면 컴포넌트를 재렌더링하지 않음.
  - 불필요한 렌더링을 방지하여 CPU 사용 최소화.
  - 얕은 비교(Shallow compare)를 기반으로 작동.

- React에서 Suspense를 활용하여 데이터 로딩 경험을 개선하는 방법
  - 비동기 컴포넌트 로딩 중 fallback UI를 자연스럽게 보여줌.
  - React 18 이상에서는 서버 컴포넌트, streaming 렌더링과 함께 사용.
  - 사용자에게 즉각적인 피드백 제공으로 체감 성능 향상.

- React에서 useInsertionEffect()의 역할과 활용 사례
  - 스타일이 DOM에 삽입되기 전에 실행되는 이펙트.
  - CSS-in-JS 라이브러리(예: Emotion, Styled-Components)에서 스타일 우선순위 보장에 사용.
  - useLayoutEffect보다 더 이른 시점에 실행됨.
    - useInsertionEffect -> useLayoutEffect -> useEffect

- React에서 CSR을 사용할 때의 보안 이슈
  - 클라이언트에서만 렌더링되므로 초기 로딩 전 데이터가 보이지 않음 → SEO 취약.
  - 중요 정보나 권한 로직이 노출되면 위변조 위험.
  - 모든 데이터 요청이 API를 통해 이뤄지므로 API 인증 및 권한 검증이 필수.

- React에서 Server Actions와 useMutation()의 차이점
  - Server Actions: 서버 함수 직접 호출 (Next.js 기반), 별도 API 라우트 없이 처리 가능.
  - useMutation(): 클라이언트에서 API 호출 + 낙관적 업데이트 등 지원 (React Query 등 활용).
  - Server Actions는 서버 우선, useMutation은 클라이언트 주도 방식.

- React에서 Error Boundaries를 사용하면 얻을 수 있는 장점
  - 자식 컴포넌트의 JavaScript 오류를 감지해 앱 전체 크래시 방지.
  - fallback UI로 대체 렌더링 가능.
  - componentDidCatch와 getDerivedStateFromError를 통해 오류를 로깅하거나 복구 가능.

- React에서 useEffect와 useLayoutEffect를 함께 사용할 때 주의할 점
  - useLayoutEffect는 DOM 변경 직후 동기 실행 → 레이아웃 측정 등 정확한 타이밍 보장.
  - useEffect는 비동기로 실행되어 렌더링 완료 후 실행됨.
  - 함께 사용할 경우 레이아웃 점검은 layoutEffect로, 부수효과는 일반 effect로 분리.

- React에서 서버 렌더링된 페이지를 클라이언트에서 보강하는 과정
  - 서버에서 HTML을 미리 렌더링한 후, 클라이언트가 해당 DOM에 이벤트 핸들러 및 상태를 주입.
  - 이 과정을 Hydration(하이드레이션) 이라고 부름.
  - 하이드레이션 중 mismatch가 발생하면 경고 또는 깜빡임 현상 발생 가능.

- React에서 Refs를 활용한 동적 포커스 처리 방법
  - useRef()로 DOM 요소를 참조한 뒤, 원하는 시점에 .focus() 호출
  - 예시
    ```jsx
    const inputRef = useRef(null);
    useEffect(() => {
      inputRef.current?.focus();
    }, []);
    ```

- React에서 Refs를 활용한 DOM 조작의 장점과 단점
  - 장점
    - 직접 DOM 접근이 가능 (포커스, 스크롤, 텍스트 선택 등)
    - 외부 라이브러리와 통합 시 유용

  - 단점
    - React의 선언형 방식과 어긋남 → 코드 예측성 저하
    - 과도한 사용 시 유지보수 어려움

- React에서 Custom Hooks를 만들 때 고려해야 할 사항
  - 관심사의 분리: 로직을 재사용 가능한 단위로 추출
  - 명확한 네이밍: use 접두사로 시작 (useFetch, useForm 등)
  - Hook 규칙 준수: Top-level에서만 호출, 조건문 내 호출 금지
  - 캡슐화: 내부 상태와 로직은 숨기고 필요한 인터페이스만 외부로 노출

- React에서 API 호출 시 Loading, Success, Error 상태를 관리하는 방법
  - useState 또는 useReducer로 상태 분리
  - isLoading, data, error 상태로 관리
  - 예시:
    ```jsx
    const [loading, setLoading] = useState(true);
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
      fetchData()
        .then(setData)
        .catch(setError)
        .finally(() => setLoading(false));
    }, []);
    ```

- React에서 Suspense를 활용한 Skeleton UI 구현 방법
  - React.Suspense와 lazy()로 컴포넌트 로딩 시 대기 화면 제공
  - Skeleton 컴포넌트를 fallback으로 지정
  - 예시:
    ```jsx
    const LazyComponent = React.lazy(() => import('./MyComponent'));

    <Suspense fallback={<SkeletonUI />}>
      <LazyComponent />
    </Suspense>
    ```
    - ※ 데이터 로딩에는 아직 Suspense for Data Fetching이 실험적이므로 라이브러리 사용 (예: React Query + Suspense) 고려

- React에서 상태 관리의 대표적인 방식 3가지
  - Local State (useState, useReducer)
    - 컴포넌트 내부의 UI 상태 관리
    - 작고 단순한 상태에 적합

  - Context API
    - 전역 상태 공유
    - 규모가 커지면 성능 저하 우려

  - 외부 상태 관리 라이브러리 (Redux, Recoil, Zustand 등)
    - 복잡한 상태 로직 분리 및 유지보수 용이
    - 미들웨어, DevTools 등 생태계 지원 강점

- React에서 useDeferredValue()와 useTransition()의 차이점
  - useDeferredValue(value)
    - 특정 값의 변화를 낮은 우선순위로 처리
    - 예: 입력창 타이핑 중 필터링 결과 느리게 갱신

  - useTransition()
    - 상태 업데이트 자체를 낮은 우선순위로 분리
    - 예: 대량 렌더링 시 UI 멈춤 방지

  - 요약:
    - useDeferredValue: 값을 defer
    - useTransition: 업데이트 함수를 defer

- React에서 Server Components의 장점과 단점
  - 장점
    - 초기 렌더링 속도 개선 (서버에서 HTML 생성)
    - 클라이언트 JS 번들 크기 감소
    - 보안상 민감한 로직 서버에 유지 가능

  - 단점
    - 클라이언트 상호작용 제한
    - 개발 복잡도 증가 (Client vs Server 분리 필요)
    - React 18 이후 도입, 아직 생태계 미성숙

- React에서 GraphQL을 사용할 때 고려해야 할 보안 이슈
  - 과도한 쿼리 (Query Depth/Complexity) → DoS 공격 가능
  - Injection 공격 → 파라미터 검증 필요
  - Authorization 미비 → 필드 단위 권한 검증 필수
  - Introspection 비활성화 필요 (배포 시) → 스키마 노출 방지

- React에서 useSyncExternalStore()를 사용해야 하는 경우
  - 외부 스토어 상태를 React 렌더링 흐름과 정합성 있게 연결할 때 사용
  - 예: Redux, Zustand 등의 외부 상태 관리 도구에서 상태를 정확하게 구독할 때
  - React 18+에서 SSR 및 concurrent rendering을 고려한 안정적 구독 방식 제공

- React에서 Server Actions의 기본 개념
  - React 서버에서 직접 실행되는 함수
  - 클라이언트에서 form or 버튼으로 호출 → 서버에서 처리 후 응답
  - 예: 데이터베이스 쓰기, 인증 처리 등
  - Next.js App Router에서 지원
  - 클라이언트 → 서버 요청 간 API 경로 없이 함수 기반 호출

- React에서 useOptimistic()을 사용한 UI 업데이트 최적화 방법
  - 서버 응답을 기다리지 않고 낙관적으로 UI 선반영
  - 예: 댓글 작성 시 입력 즉시 반영하고 서버 응답으로 정합성 조정
  - 상태값과 업데이트 함수 제공:
    ```js
    const [optimisticComments, addOptimisticComment] = useOptimistic(comments);
    ```

- React에서 React.memo()를 올바르게 사용하는 방법
  - Pure Component처럼 props가 바뀌지 않으면 재렌더 방지
  - 예시
    ```js
    const MyComponent = React.memo(({ title }) => { ... });
    ```
  - 조건:
    - props가 자주 변경되지 않아야 함
    - props 비교 비용보다 재렌더 비용이 높아야 함
    - 필요 시 areEqual(prevProps, nextProps) 커스터마이징

- React Server Components(RSC)의 개념과 기존 CSR, SSR과의 차이점
  - RSC는 서버에서 React 컴포넌트를 렌더링하고, 클라이언트에는 HTML과 최소한의 상태만 전송하는 방식
  - CSR은 모든 렌더링을 클라이언트에서 처리하고, SSR은 서버에서 HTML을 먼저 렌더링한 후 클라이언트에서 하이드레이션한다.
  - RSC는 서버 컴포넌트와 클라이언트 컴포넌트를 혼합 사용하며, JS 번들 크기를 줄이고 보안을 강화할 수 있다.

- React 19에서 추가된 주요 기능과 성능 최적화 개선 사항
  - use() 훅 공식 지원: Promise를 직접 처리 가능
  - useOptimistic() 정식 도입: 낙관적 UI 업데이트 지원
  - Server Actions 정식 채택: API 없이 서버 함수 실행 가능
  - Form Actions 향상: <form> 직접 처리 가능
  - Transition 성능 향상: 병렬 처리 최적화
  - Suspense 개선: streaming 방식 강화로 초기 렌더링 속도 개선

- React에서 WASM(WebAssembly)을 활용하는 방법
  - WASM으로 작성된 성능 중심 모듈(C/C++/Rust 등)을 빌드하여 React에서 JS interop으로 호출
  - 예: wasm_exec.js 또는 WebAssembly.instantiate() API 사용
  - 이미지 처리, 수학 계산, 암호화 등 고성능 작업에 활용
  - React와 연동 시에는 useEffect 또는 Worker와 함께 사용하면 효율적

- React에서 Suspense와 Streaming을 결합하여 성능을 최적화하는 방법
  - Suspense는 컴포넌트 단위로 로딩 제어
  - Streaming은 서버에서 HTML을 점진적으로 전송
  - 둘을 결합하면 사용자에게 빠른 초기 화면을 보여주고, 이후 데이터를 점진적으로 로드
  - Next.js App Router에서 기본 적용 (RSC + Suspense 활용)

- React에서 Context API의 성능 이슈를 해결하는 방법
  - 컴포넌트가 불필요하게 전역 컨텍스트 변화로 리렌더링되는 문제
  - 해결책:
    - Context 분할 (단일 Context에 너무 많은 값 넣지 않기)
    - React.memo로 하위 컴포넌트 최적화
    - useContextSelector 또는 zustand 등 대안 고려

- React에서 SWR과 React Query의 내부 작동 방식 차이
  - 공통점: 캐싱, 재검증, 폴링, 뮤테이션 지원
  - SWR
    - Stale-While-Revalidate 전략 중심
    - 선언적, 단순한 API
    - lightweight, 내부 캐시는 key → response 중심
  - React Query
    - 상태 관리 포함
    - Query/Mutation 분리, DevTools 제공
    - 더 많은 옵션과 제어 가능 (예: retry, staleTime, GC)

- React의 Virtual DOM
  - Virtual DOM은 실제 DOM의 가벼운 자바스크립트 객체 표현
  - 변경 전후의 Virtual DOM을 비교(diffing)하여 최소 변경사항만 실제 DOM에 반영함으로써 렌더링 성능을 최적화

- React의 상태 관리 방법 (Redux, Context API 등)
  - Context API: 전역 상태 공유. 단순하지만 리렌더링 최적화가 어렵다.
  - Redux: 중앙 스토어 기반. 미들웨어, DevTools 등 생태계 강력. 불변성 유지 필수.
  - Zustand/Recoil/Jotai 등: 사용 편의성과 성능 중심의 대안. 필요에 따라 선택
  - 상황에 맞춰 로컬(local) vs 글로벌(global) 상태를 구분해서 선택하는 것이 핵심

- React의 Hooks 내부 동작 원리
  - Hooks는 함수 컴포넌트 호출 시 내부적으로 순서를 기반으로 작동하는 상태 머신 구조
    - 순서 기반 상태 머신 구조
  - useState, useEffect 등은 React 내부의 Hook dispatcher가 인덱스를 기준으로 각 호출을 추적하며, 컴포넌트 재실행 시 동일한 순서로 실행되어 상태를 유지
    - 훅 디스패쳐가 인덱스 기준으로 흐름 추적 > 재실행 > 동일한 순서로 실행 > 상태 유지
  - 조건문이나 반복문 안에서 Hook을 호출하면 이 순서가 깨져 렌더링 오류가 발생할 수 있다.
    - 조건문, 반복문 안에서 훅 호출은 금지 (순서 깨짐, 렌더링 오류)

- React의 Concurrent Mode와 Suspense
  - Concurrent Mode는 React가 렌더링을 중단하고 더 중요한 작업(예: 사용자 입력)을 먼저 처리하도록 만드는 비동기적 렌더링 모델
  - Suspense는 데이터를 기다리는 동안 UI의 일부를 fallback으로 대체해 로딩 경험을 향상시키는 기능 (유저 경험 증대)
  - 둘을 결합하면 사용자 경험을 유지하며 점진적 UI 로딩이 가능
  
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