# Self-Assessment Vue.js

This page summarizes the main concepts, features, pros and cons of Vue.js.
All Vue.js related content on this page has been organized.

## Vue.js의 반응형(Reactive) 시스템 동작 설명
  - 개요
    - Vue.js의 반응형 시스템은 데이터가 변경되면 자동으로 UI가 업데이트되도록 설계된 핵심 메커니즘
    - Vue는 프록시(Proxy) 기반의 반응형(Reactivity) 시스템을 사용하여 데이터 변경을 감지하고, 필요할 때만 DOM을 업데이트
  - Vue.js 반응형 시스템의 핵심 개념
    - "데이터 변경 감지” + “필요한 부분만 업데이트” 를 결합하여 최적화된 UI 렌더링을 수행
    - 핵심 개념
      - 반응형 데이터 감지
        - Vue는 Proxy (Vue 3) 또는 Object.defineProperty (Vue 2) 를 이용해 데이터 변경을 감지.
	    - ref() 또는 reactive()를 사용하여 반응형 데이터 생성.
      - 종속성 추적 (Dependency Tracking)
	    - Vue의 반응형 시스템은 데이터가 어떤 컴포넌트에서 사용되는지 추적
	    - 특정 데이터가 변경될 때 관련된 컴포넌트만 업데이트
      - 효율적인 DOM 업데이트
	    - 변경된 데이터와 관련된 Virtual DOM 부분만 업데이트하여 성능 최적화
  - Vue의 반응형 시스템이 DOM을 업데이트하는 과정
    - 데이터 변경 감지 (Proxy set 트랩 실행)
    - 종속성 추적 (어떤 컴포넌트에서 해당 데이터가 사용되는지 기록)
    - Virtual DOM 업데이트 (변경된 부분만 업데이트하여 성능 최적화)
    - 실제 DOM 업데이트 (최적화된 패치 적용)
  - 결론 (Vue 반응형 시스템 핵심 요약)
    - Vue는 Proxy 기반(3.x) 또는 Object.defineProperty()(2.x)로 반응형 시스템을 구현
    - 종속성 추적을 통해 변경된 부분만 업데이트하여 성능 최적화
    - reactive(), ref(), computed(), watch() 같은 API를 활용하여 상태 관리 가능
    - Virtual DOM을 활용하여 효율적으로 실제 DOM 업데이트 수행
    - Vue의 반응형 시스템은 데이터 변경을 자동으로 감지하고, 필요한 부분만 업데이트하여 효율적인 UI 렌더링을 제공

## Vue.js에서 Vuex와 Pinia의 차이점
  - Vuex와 Pinia 개요
    - Vuex
      - 2015년 출시 (Vue2)
      - Vue 공식 지원	Vue 2, Vue 3 지원
      - 중앙 집중식(store, mutations, actions)
      - mutations, actions, getters 사용
      - 타입스크립트 지원 관련해서 타입 지원이 복잡함
      - Vue.observable 사용한 반응형 지원
      - 보일러플레이트 코드가 많음
      - 지원 (Vuex 패널 필요)
    - Pinia
      - 2021년 출시 (Vue3 공식 추천)
      - Vue 3 공식 상태 관리 라이브러리
      - 모듈 기반 (defineStore())
      - state, actions, getters 간결화
      - 타입 지원이 복잡함	기본적으로 타입스크립트 친화적
      - reactive() 기반의 반응형 상태
      - 코드가 간결하고 직관적
      - 지원 (Vue DevTools 기본 제공)

  - Vuex 개념 및 사용법
    - Vuex 특징
	    - 중앙 집중식 상태 관리 패턴 (Flux 패턴 기반)
	    - mutations을 통해서만 상태 변경 가능 (동기적 변경)
	    - 비동기 작업(actions)과 동기 작업(mutations)이 구분됨
	    - Vue 2, Vue 3 모두 지원하지만, Vue 3에서는 Pinia를 공식 추천.

  - Vuex의 문제점
	    - mutations, actions을 따로 정의해야 하므로 코드가 복잡해짐
	    - mapState(), mapMutations() 등을 사용해야 하므로 가독성이 떨어짐
      - 리액트의 리덕스와 유사

  - Pinia 개념 및 사용법
    - Pinia 특징
	    - Vue 3 공식 상태 관리 라이브러리 (Vuex의 차세대 버전).
	    - Composition API와 Reactivity 기반 (reactive, computed, ref).
	    - mutations 없이 직접 상태 변경 가능.
	    - Typescript 친화적이며 코드가 간결.
	    - Vue DevTools와 기본적으로 통합됨.

    - Pinia의 장점
	    - mutations 없이 상태 직접 변경 가능
	    - Composition API를 활용하여 사용법이 직관적
	    - 코드가 간결하고 유지보수하기 쉬움

- 결론
  - Vuex는 Vue 2 시절부터 사용된 전통적인 상태 관리 라이브러리지만, 보일러플레이트 코드가 많아 유지보수가 어려움
  - Pinia는 Vue 3 공식 상태 관리 라이브러리로, 코드가 간결하고 TypeScript 지원이 뛰어나며 Composition API와 잘 어울림
  - Vue 3에서는 Pinia를 기본 선택으로 고려하는 것이 좋으며, 기존 Vuex 프로젝트는 필요 시 마이그레이션 가능

- Vue.js의 Computed Property와 Watcher의 차이점
  - Computed Property
    - 종속된 반응형 데이터가 변경될 때 자동으로 다시 계산되는 속성
    - 캐싱을 지원하여 같은 값이라면 다시 연산하지 않음
  - Watcher
    - 특정 데이터의 변경을 감지하고, 비동기 처리나 API 호출과 같은 추가적인 동작을 수행할 때 사용

- Vue.js에서 Composition API와 Options API의 차이점
  - Composition API: setup() 함수를 활용하여 로직을 명확하게 분리할 수 있으며, 재사용성이 뛰어남 (Vue 3에서 도입)
  - Options API: data, methods, computed, watch 등의 옵션을 사용하여 구성하는 기존 방식 (Vue 2와 호환성이 높음)

- Vue.js에서 Teleport 기능
  - 특정 컴포넌트의 렌더링 위치를 지정하여 다른 DOM 노드로 이동시키는 기능
  - 모달, 툴팁 같은 UI 요소를 body 태그 아래에 렌더링할 때 유용

- Vue.js에서 Lazy Loading을 구현하는 방법
  - defineAsyncComponent를 사용하여 동적으로 컴포넌트를 로드할 수 있으며, Vue Router에서는 component: () => import('컴포넌트 경로')를 활용하여 페이지 단위로 Lazy Loading 적용 가능

- Vue.js에서 Virtual DOM 동작 설명
  - 실제 DOM을 조작하는 것이 아니라 메모리에서 가상의 DOM을 생성하고, 변경 사항을 비교(diffing)하여 최소한의 실제 DOM 업데이트를 수행

- Vue.js에서 Suspense를 사용하는 이유
  - 비동기 컴포넌트의 로딩 상태를 쉽게 관리하고, fallback 슬롯을 활용하여 로딩 UI 표시 가능

- Vue.js에서 Slots를 활용하는 방법
  - 부모 컴포넌트에서 자식 컴포넌트 내부의 특정 영역을 동적으로 채울 수 있도록 하는 기능
  - default, named slots, scoped slots를 제공

- Vue Router에서 History Mode와 Hash Mode의 차이점
  - History Mode
    - URL에 #이 포함되지 않으며, 브라우저의 히스토리 API를 활용
    - 서버에서 적절한 설정이 필요하다.
  - Hash Mode
    - #을 사용하여 페이지 경로를 변경하며, 서버 설정 없이도 작동

- Vue.js에서 Composition API의 provide/inject를 활용하는 방법
  - provide()를 사용하여 부모 컴포넌트에서 데이터를 제공하고, inject()를 사용하여 자식 컴포넌트에서 해당 데이터를 사용 가능

- Vue.js에서 Mixin과 Composition API의 차이점
  - Mixin: 여러 컴포넌트에서 재사용할 로직을 정의할 수 있으나, 네임스페이스 충돌 가능성 존재
  - Composition API: setup()을 사용하여 로직을 재사용할 수 있으며, 코드의 가독성이 높아짐

- Vue.js에서 Web Component를 만들 때 주의할 점
  - Shadow DOM을 사용할 경우 스타일 격리가 발생할 수 있으며, Vue의 반응형 시스템이 Web Component 내부에서는 동작하지 않을 수 있음

- Vue.js에서 Reactivity Transform이 필요한 이유
  - ref를 사용할 때 .value를 반복적으로 참조하는 불편함을 해소하고, 더 직관적인 코드 작성을 가능하게 함

- Vue.js에서 keep-alive의 역할
  - 동적 컴포넌트의 상태를 유지하여 재랜더링 시 초기화되지 않도록 함 (캐싱 역할을 수행)

- Vue.js에서 Transition과 Animation을 활용하는 방법
  - transition 태그를 사용하여 CSS 애니메이션 및 JavaScript 훅을 적용 가능

- Vue.js에서 SSR(Server-Side Rendering)을 적용하는 방법
  - Nuxt.js와 같은 프레임워크를 사용하여 서버에서 Vue 애플리케이션을 렌더링한 후 클라이언트에서 Hydration을 수행

- Vue.js에서 Suspense와 async setup()을 활용하는 방법
  - Suspense를 사용하여 async setup()을 처리할 수 있으며, 데이터를 로딩하는 동안 fallback을 제공할 수 있음

- Vue.js에서 Teleport를 사용하는 시나리오
  - 모달, 드롭다운, 툴팁과 같은 UI 요소를 body의 최상위 계층에 렌더링할 때 사용된다.

- Vue.js에서 PWA(Progressive Web App)를 구현하는 방법
  - @vue/cli-plugin-pwa 플러그인을 사용하여 Service Worker를 등록하고, 웹앱 매니페스트 파일을 구성

- Vue.js의 반응형(Reactive) 시스템 동작 설명
  - Vue는 Proxy를 사용하여 반응형 데이터를 감지하고, 변경이 발생하면 의존성이 있는 컴포넌트를 자동으로 업데이트

- Vue.js에서 ref()와 reactive()의 차이점
  - ref(): 단일 값에 대한 반응성을 제공하며 .value로 접근해야 함
  - reactive(): 객체 전체에 대한 반응성을 제공하며, .value 없이 사용 가능

- Vue.js에서 watch()와 watchEffect()의 차이점
  - watch(): 특정 데이터를 감시하고, 명시적으로 감시할 데이터를 지정해야 함
  - watchEffect(): 자동으로 종속성을 추적하며, 즉시 실행됨

- Vue.js에서 computed 속성을 사용할 때의 장점
  - 종속된 데이터가 변경될 때만 다시 계산되며, 불필요한 연산을 줄여 성능 최적화에 도움

- Vue.js에서 v-if와 v-show의 차이점
  - v-if: 조건을 만족하면 요소를 DOM에 추가하고, 만족하지 않으면 제거
  - v-show: 항상 DOM에 존재하며, CSS display 속성을 변경하여 보이거나 숨길 수 있음

- Vue.js에서 v-for와 key 속성을 함께 사용해야 하는 이유
  - Vue의 가상 DOM이 효율적으로 변경 사항을 추적하도록 하며, 리스트 렌더링 시 올바르게 업데이트될 수 있도록 함

- Vue.js에서 props와 emit을 활용한 컴포넌트 간 데이터 전달 방법
  - 부모에서 props를 통해 자식에게 데이터를 전달하고, 자식은 emit()을 사용하여 부모에게 이벤트를 전달할 수 있음

- Vue.js에서 slot과 scoped slot의 차이점
  - slot: 부모가 전달한 콘텐츠를 자식 컴포넌트에서 렌더링할 수 있도록 함
  - scoped slot: 부모가 자식의 데이터를 사용할 수 있도록, 데이터가 포함된 슬롯을 제공

- Vue.js에서 teleport의 역할
  - 특정 HTML 요소 밖으로 특정 컴포넌트의 렌더링을 이동시키는 기능
  - 예를 들어, 모달 창, 툴팁 같은 UI 요소를 body 태그 하위에 직접 추가할 때 유용
  - 예제
    ```html
    <template>
      <teleport to="body">
        <div class="modal">Modal Content</div>
      </teleport>
    </template>
    ```
- Vue.js에서 provide()와 inject()를 사용하는 이유
  - provide()와 inject()는 부모-자식 관계에서 데이터를 전역적으로 공유할 수 있도록 도와줌
  - Props와 Emit을 사용하지 않고도 여러 단계 아래의 컴포넌트에서 데이터를 받을 수 있음
    ```javascript
    // 부모 컴포넌트
    provide('theme', 'dark');
    // 자식 컴포넌트
    const theme = inject('theme');
    ```

- Vue.js의 Composition API와 Options API의 차이점
  - Composition API: setup() 함수에서 상태와 로직을 구성하며, 코드 재사용성과 모듈화가 용이
  - Options API: data, methods, computed, watch 등 기존 방식으로 로직을 구성

- Vue.js에서 $nextTick()의 역할
  - DOM 업데이트가 완료된 후 특정 로직을 실행하고 싶을 때 사용
    ```javascript
    this.$nextTick(() => {
      console.log('DOM 업데이트 후 실행');
    });
    ```

- Vue.js에서 setup() 함수의 실행 순서
  - (1) setup() 실행
  - (2) reactive 상태 정의
  - (3) computed 및 watch 설정
  - (4) 템플릿과 연결
  - (5) onMounted 실행

- Vue.js에서 Lifecycle Hooks의 실행 순서
  - (1) beforeCreate
  - (2) created
  - (3) beforeMount
  - (4) mounted
  - (5) beforeUpdate
  - (6) updated
  - (7) beforeUnmount
  - (8) unmounted

- Vue.js에서 v-model을 활용하여 양방향 바인딩을 구현하는 방법
  - 아래와 같이 사용하면 text 값이 자동으로 업데이트됨
  - 예제 코드
    ```javascript
    <input v-model="text" />
    ```

- Vue.js에서 async setup()을 사용할 때의 주의점
  - 비동기 데이터를 가져오면서 초기 로딩 처리가 필요
  - Suspense를 사용하여 비동기 데이터를 안전하게 처리 가능

- Vue.js에서 Vue.use()가 Composition API에서는 필요 없는 이유
  - Composition API 에서는 setup() 내부에서 직접 필요한 기능을 import하여 사용할 수 있기 때문임

- Vue.js에서 isRef()와 toRefs()의 차이점
  - isRef(): ref 객체인지 확인하는 함수
  - toRefs(): reactive() 객체의 속성을 ref로 변환

- Vue.js에서 $attrs와 $listeners 개념과 역할
  - $attrs: 부모 컴포넌트에서 전달된 props 중 정의되지 않은 것
  - $listeners: 부모로부터 전달된 이벤트 리스너

- Vue.js에서 Suspense 컴포넌트를 활용하여 비동기 데이터를 다루는 방법
  - 예제
    ```javascript
    <Suspense>
      <template #default>
          <AsyncComponent />
      </template>
      <template #fallback>
          Loading...
      </template>
    </Suspense>
    ```

- Vue.js에서 Fragment 기능을 활용하는 이유
  - 여러 개의 루트 노드를 가질 수 있도록 허용하여 불필요한 <div> 생성 방지

- Vue.js에서 isProxy()와 toRaw()의 역할
  - isProxy(): 객체가 reactive 인지 확인
  - isRaw(): reactive 객체를 원래 객체로 변환

- Vue.js에서 dynamic component를 렌더링하는 방법
  - 예제 코드
    ```javascript
    <component :is="currentComponent" />
    ```

- Vue.js에서 key 속성을 활용하여 리스트 렌더링 시 발생할 수 있는 문제를 방지하는 방법
  - 각 항목에 key 속성을 추가하여 가상 DOM이 변경 사항을 올바르게 감지할 수 있도록 함

- Vue.js에서 v-bind와 v-on을 줄여서 사용하는 방법
  - v-bind: :
  - v-on: @
    ```javascript
    <input :value="message" @input="updateMessage" />
    ```

- Vue.js에서 watch() 내부에서 상태를 변경할 때 발생할 수 있는 문제
  - Vue의 watch()는 특정 반응형 상태(reactive state)를 감시하고, 값이 변경될 때 특정 로직을 실행하는 데 사용됨
  - watch() 내부에서 상태를 변경하면 무한 루프나 예상치 못한 동작 발생 가능성 존재

- Vue.js에서 errorCaptured()를 활용하여 에러를 처리하는 방법
  - 에러 처리 방법
    ```javascript
    errorCaptured(err, vm, info) {
      console.error(err);
      return false;
    }
    ```

- Vue.js에서 template refs를 활용하여 DOM 요소에 접근하는 방법
  - 개요
    - template refs(ref)를 사용하여 DOM 요소나 컴포넌트 인스턴스에 직접 접근할 수 있음
    - 주로 DOM 조작, 포커스 설정, 스크롤 컨트롤, Canvas API 활용 등의 경우에 사용됨
  - 접근 방법
    - ref="name"을 사용하여 특정 DOM 요소나 컴포넌트 참조 가능
    - ref.value를 통해 요소에 접근하고 DOM 조작 가능
    - onMounted()에서 ref를 안전하게 사용 가능
    - defineExpose()를 사용하면 자식 컴포넌트의 메서드를 부모에서 호출 가능
  - 결론
    - Vue에서 직접 DOM을 조작하는 일은 지양
    - focus(), scrollIntoView() 등의 필요한 경우에는 template refs를 활용하면 유용

- Vue.js에서 keep-alive의 역할과 사용 예제
  - 컴포넌트를 캐싱하여 성능 최적화
  - 예제
    ```javascript
    <keep-alive>
      <component :is="currentView" />
    </keep-alive>
    ```

- Vue.js에서 mixins와 composables의 차이점
  - Mixins: 기존 Options API에서 코드 재사용을 위한 방법
  - Composables: Composition API에서 setup() 내부에서 함수로 로직을 관리

- Vue.js에서 Vuex와 Pinia의 차이점
  - Vuex: 기존 상태 관리 라이브러리 (복잡한 구조, Boilerplate 코드 많음)
  - Pinia: Vue 3에서 권장하는 상태 관리 라이브러리 (더 간결하고 사용하기 쉬움)

- Vue.js에서 상태 관리를 중앙에서 관리해야 하는 이유
  - 데이터 일관성 유지
    - 여러 컴포넌트에서 같은 데이터를 공유할 경우, 개별적으로 관리하면 일관성이 깨질 수 있음.
    - 중앙 상태를 사용하면 모든 컴포넌트에서 동일한 데이터에 접근 가능.

  - 컴포넌트 간 데이터 전달 문제 해결
    - props와 emit을 통해 데이터를 전달하는 방식은 깊이 있는 컴포넌트 트리에서 비효율적임.
    - 중앙 상태를 활용하면 props drilling(계층 구조를 따라 데이터 전달) 없이 바로 데이터에 접근 가능.

  - 비동기 처리와 상태 동기화 용이
    - API 호출 결과를 여러 컴포넌트에서 공유할 경우, 개별적으로 관리하면 중복 호출 및 불필요한 상태 변화 발생.
    - 중앙 관리 시스템을 사용하면 데이터 요청과 상태 변경을 효율적으로 관리할 수 있음.

  - 디버깅과 유지보수 용이
    - Vue DevTools 등을 사용하여 상태를 한 곳에서 추적 가능하여 디버깅이 쉬움.
    - 상태 변화를 추적하고 로그를 남길 수 있어 버그 발생 시 원인 분석이 쉬워짐.

- Vue.js에서 Pinia를 사용하여 전역 상태를 관리하는 방법
  - Pinia는 Vuex보다 간단하고 타입스크립트 지원이 강력한 Vue3의 상태관리 라이브러리
  - Pinia 장점
    - Vuex보다 코드 간결하고 타입 지원 좋음
    - Composition API와 잘 통합됨
    - Module 구조가 필요 없음, 여러 개의 Store를 직접 만들 수 있음

- Vue.js에서 Vuex modules을 사용하는 이유
  - Vuex는 전역 상태를 한 곳에서 관리하지만, 프로젝트가 커질수록 store가 커져 유지보수가 어려워짐.
  - 이를 해결하기 위해 모듈(Module) 방식을 사용하여 Store를 분리할 수 있음.
  - Vuex 모듈 사용의 장점
    - 스토어의 분리 가능 → 여러 기능을 독립적으로 관리 가능.
    - 이름 공간 (namespace) 지원 → 특정 모듈만 참조 가능 (auth/login).
    - 대규모 애플리케이션에서 유지보수 용이.

- Vue.js에서 Vuex의 getters와 actions의 차이점
  - getters
    - 상태(state)를 기반으로 값을 계산하여 반환
    - 동기적 (비동기 작업 불가)
    - 계산된 데이터 (computed property와 유사)
  - actions
    - 상태를 변경하거나 비동기 작업 수행
    - 비동기 가능 (API 호출 가능)
    - 주로 mutations를 호출하여 상태 변경

- Vue.js에서 Vuex의 mutations과 actions의 차이점
  - mutations
    - 상태 변경
    - 직접적인 상태 변경 가능
    - 동기적 (비동기 불가)
  - actions
    - 비동기 로직 처리 후 mutations 호출
    - 직접적인 상태 변경 불가능 (mutations을 호출해야 함)
    - 비동기 가능 (API 호출 등)

- Vue.js에서 Vuex를 비동기적으로 처리할 때의 주의점
  - Mutations에서 비동기 코드 사용 금지
    - mutations는 반드시 동기적이어야 하며, 비동기 코드는 actions에서 처리해야 함.
    - 비동기 작업이 mutations에 포함되면 디버깅이 어려워짐.

  - API 요청 중 상태가 변경되지 않도록 주의
    - 예를 들어, 여러 API 요청이 동시에 실행되면 이전 요청 결과가 덮어쓰기될 수 있음.
    - 이를 방지하려면 AbortController 또는 cancelToken을 사용.

- Vue.js에서 localStorage, sessionStorage, cookies를 활용한 상태 유지 방법
  - 개요
    - Vue 애플리케이션이 새로고침되면 store 상태는 초기화되지만, localStorage, sessionStorage, cookies를 활용하면 상태를 유지할 수 있음
  - 스토리지 별 유지시간 및 사용 예
    - localStorage: 사용자가 삭제할때까지 영구 저장 (로그인 정보, 사용자 설정 저장)
    - sessionStorage: 브라우저 탭을 닫을 때까지 유지 (일시적인 상태 저장)
    - cookie: 만료 기간 설정 가능 (인증 토큰 저장 (보안이 중요할 때 사용))

- Vue.js에서 Lazy Loading을 적용하는 방법
  - Lazy Loading 개념
    - 지연 로딩은 초기 로딩 속도를 줄이기 위해 특정 리소스(컴포넌트, 이미지, 데이터 등)를 필요할 때 로드하는 기법
    - 컴포넌트, 라우트, 이미지, API 데이터 등을 Lazy Loading 방식으로 로드 가능

  - 컴포넌트의 Lazy Loading (Dynamic Import)
    - defineAsyncComponent()를 사용하여 동적 컴포넌트 로딩 가능
      - definedAsyncComponent 장점
        - 초기 번들 크기 감소: 필요한 경우에만 해당 컴포넌트를 로드
        - 비동기 컴포넌트 사용 가능: 로딩 중, 에러 발생 시 대체 UI를 제공 가능
  - Vue Router에서 Lazy Loading 적용 (Lazy Load Routes)
    - Vue Router에서는 import()를 사용하여 라우트별로 필요한 컴포넌트만 로그 가능
      - Vue Router에서 Lazy Loading 적용의 장점
        - 초기 로딩 속도 향상: 사용자가 특정 페이지를 방문하기 전까지 해당 페이지의 JS 파일을 다운로드하지 않음
        - SPA에서 초기 렌더링 성능 개선
  - 이미지 Lazy Loading → Intersection Observer API 활용
  - Suspense 활용 → 로딩 중 화면을 표시할 때 유용
  - API 데이터 Lazy Loading → onMounted()에서 비동기 요청

- Vue.js에서 code splitting을 적용하여 성능을 최적화하는 방법
  - 개요
    - Code Splitting(코드 분할)은 JavaScript 번들 크기를 줄이고, 필요한 코드만 로드하여 애플리케이션의 성능을 향상시키는 기법
    - Vue.js에서는 Webpack, Vite, Dynamic Import (import()) 등을 사용하여 코드 분할 수행 가능

  - Code Splitting 주요 방법
    - Vue Router와 함께 사용 (라우트 기반 코드 분할)
      - 특정 페이지에 접근할 때만 필요한 컴포넌트를 로드할 수 있습니다.
        - 장점: 초기 번들 크기 감소, 페이지별 로딩 최적화
        ```javascript
        import { createRouter, createWebHistory } from 'vue-router';

        // 동적 import를 사용하여 Lazy Loading 적용
        const Home = () => import('@/views/Home.vue');
        const About = () => import('@/views/About.vue');

        const routes = [
          { path: '/', component: Home },
          { path: '/about', component: About }
        ];

        const router = createRouter({
          history: createWebHistory(),
          routes
        });

        export default router;
        ```

    - defineAsyncComponent()를 사용하여 컴포넌트 코드 분할
      - 컴포넌트가 필요할 때만 로드되도록 설정할 수 있습니다.
        - 장점: 특정 조건에서만 로딩되어 초기 렌더링 성능 개선
        ```javascript
        <script setup>
        import { defineAsyncComponent } from 'vue';

        // 동적 컴포넌트 로딩
        const AsyncComponent = defineAsyncComponent(() => import('@/components/MyComponent.vue'));
        </script>

        <template>
          <div>
            <AsyncComponent />
          </div>
        </template>
        ```
    
    - Webpack의 splitChunks를 활용한 코드 분할
      - Webpack 설정에서 splitChunks를 사용하여 공통 라이브러리를 별도 파일로 분리 가능
        - 장점: 동일한 코드가 여러 번 로드되지 않고 공통 파일로 관리됨
        ```javascript
        module.exports = {
          optimization: {
            splitChunks: {
              chunks: 'all',
              minSize: 20000,
              maxSize: 250000
            }
          }
        };
        ```

- Vue.js에서 Prefetching과 Preloading의 차이점
  - 개요
    - Prefetching과 Preloading은 브라우저가 필요한 리소스를 미리 다운로드하여 성능을 최적화하는 기법
  - Prefetching
    - 현재 페이지에서는 사용되지 않지만 사용될 가능성이 높은 리소스를 미리 다운로드
    - 브라우저의 Idle Time(유휴 시간)을 활용하여 리소스를 미리 가져옴
      - 나중에 필요할 가능성이 있는 리소스를 미리 가져옴
    - Vue에서는 webpackPrefetch를 사용하여 적용할 수 있음
    - 장점: 사용자가 다음 페이지로 이동할 경우, 즉시 렌더링 가능

  - Preloading
    - 현재 페이지 로딩과 동시에 필요한 리소스를 즉시 다운로드
    - 중요한 리소스를 빠르게 로드할 때 사용됨
      - 현재 페이지에서 즉시 필요한 리소스
    - Vue에서는 webpackPreload를 사용하여 적용 가능
    - 장점: 현재 페이지에서 즉시 필요한 리소스를 빠르게 로딩하여 성능 최적화

- Vue.js에서 Tree Shaking을 활용하여 불필요한 코드 제거하는 방법
  - 개요
    - 트리 쉐이킹은 애플리케이션에서 사용되지 않는 코드(Dead Code)를 자동으로 제거하여 번들 크기를 줄이는 기법

  - Tree Shaking 적용 방법
    - (1) ES6 모듈 (import/export) 활용
      - import를 사용할 때, 사용하지 않는 코드는 번들에서 제거됨

    - (2) Webpack에서 Tree Shaking 활성화
      - Webpack의 mode: 'production'을 설정하면 자동으로 Tree Shaking이 활성화
      - 장점: 사용되지 않는 코드를 제거하여 최적의 번들 크기 유지

- Vue.js에서 Vue Router의 Lazy Loading을 활용하는 방법
  - Vue Router에서 Lazy Loading을 활용하면 특정 페이지를 방문할 때만 해당 페이지의 컴포넌트를 로드할 수 있음
  - 장점: 초기 로딩 시 불필요한 코드 로드 방지하여 성능 최적화

- Vue.js에서 debounce와 throttle을 활용하여 이벤트 핸들링을 최적화하는 방법
  - 개요
    - Debounce와 Throttle은 이벤트 발생 빈도를 조절하여 성능을 최적화하는 기법
  - Debounce (디바운스)
    - 사용자의 입력이 끝난 후 일정 시간이 지난 뒤에만 실행됨
    - 주로 검색 입력, 자동 저장 기능 등에 사용됨
    - 장점: 입력이 연속적으로 발생해도 API 호출 횟수를 줄여 네트워크 부하 감소
  - Throttle (쓰로틀)
    - 지정된 시간 간격마다 한번씩 실행됨
    - 주로 스크롤 이벤트, 버튼 클릭 제한 등에 사용됨
    - 장점: 자주 발생하는 이벤트(스크롤, 클릭 등)의 부하를 줄여 성능 최적화

- Vue.js에서 watch()를 과도하게 사용했을 때 발생할 수 있는 문제
  - 문제점
    - 불필요한 성능 저하
      - watch()는 값이 변경될 때마다 실행되므로, 과도하게 사용하면 성능 문제가 발생할 수 있음.
      - 특히, 비효율적인 watch() 사용은 불필요한 연산을 반복하여 UI 성능을 저하시킴.
    - 의존성 문제
      - watch() 내부에서 여러 개의 상태를 변경하면 무한 루프가 발생할 가능성이 있음.
    - 복잡한 디버깅
      - 여러 개의 watch()가 중첩되면 특정 값이 변경될 때 어떤 watch()가 실행되는지 추적하기 어려움.
  - 해결 방법
    - computed()를 먼저 고려하고, 꼭 필요한 경우에만 watch() 사용
    - watchEffect()를 활용하여 더 직관적인 반응형 코드 작성
    - immediate: false를 활용하여 불필요한 첫 번째 실행 방지

- Vue.js에서 ref()와 computed()를 활용하여 성능을 개선하는 방법
  - ref() 사용하여 반응형 데이터 관리
    - ref()는 Vue의 반응형 상태를 제공하는 기본적인 방법, 필요한 데이터만 반응형으로 관리 가능
    - 너무 많은 데이터가 반응형으로 설정되면 성능 저하 발생 가능성
    - 필요한 값만 반응형 상태로 유지하여 불필요한 성능 부담 줄임

  - computed()를 사용하여 성능 최적화
    - 의존성이 변경될 때만 다시 계산되므로, 불필요한 연산을 방지할 수 있음
    - 렌더링할 때마다 불필요한 연산을 반복하지 않음

- Vue.js에서 Vue DevTools을 활용하여 성능을 분석하는 방법
  - Vue DevTools 주요 기능
    - 컴포넌트 상태 확인
      - 컴포넌트의 상태, Props, computed 값 등을 실시간으로 확인 가능
    - 반응형 데이터 추적
      - watch() 및 computed()가 어떻게 작동하는지 확인하여 불필요한 상태 업데이트 탐색
    - 성능 프로파일링
      - 렌더링 속도를 분석하여 불필요한 렌더링을 감지하고 최적화 가능

  - 사용 방법
    - Vue DevTools 설치
      - 크롬 또는 파이어폭스 확장 프로그램 설치
    - Vue 앱에서 DevTools 활성화
      - app.config.devtools = true;
    - 성능 문제 확인 및 최적화
      - 불필요한 상태 변경 탐색 후 computed()로 변경하거나 watch() 최적화

- Vue.js에서 Virtual Scroll을 활용하여 성능을 최적화하는 방법
  - Virtual Scroll 개념
    - 리스트가 너무 길어질 경우, 모든 항목을 렌더링하지 않고 화면에 보이는 항목만 렌더링하는 기법
    - 예: 무한 스크롤 리스트, 데이터 테이블 최적화
  - 구현 방법: vue-virtual-scroller 라이브러리 사용 (대량의 데이터도 부드럽게 스크롤 가능, 메모리 사용량 감소)

- Vue.js에서 Intersection Observer API를 활용하여 Lazy Loading을 구현하는 방법
  - Lazy Loading 개념
    - 스크롤할 때 화면에 보이는 요소만 로드하여 성능을 개선하는 기법
  - 구현 방법
    - Intersection Observer 활용
    - 스크롤이 끝날 때까지 불필요한 리소스 로드를 방지하여 성능 최적화 가능

- Vue.js에서 async setup()을 사용할 때 성능 최적화하는 방법
  - 문제점
    - async setup()은 비동기 데이터를 가져올 때 초기 렌더링을 지연시킬 수 있음
  - 해결 방법
    - Suspense를 사용하여 로딩 상태를 표시
    - 초기 렌더링을 빠르게 하기 위해 shallowRef() 사용
      - 초기 렌더링을 차단하지 않고 데이터 로딩 진행 가능

- Vue.js에서 shallowRef()와 shallowReactive()를 활용하여 성능을 최적화하는 방법
  - 문제점
    - ref()와 reactive()는 깊은 반응성을 제공하므로 데이터 크기가 클 경우 불필요한 렌더링이 발생할 수 있음
  - 해결 방법
    - shallowRef() 사용
      - 반응성을 얕게 적용하여 성능을 최적화
    - shallowReactive() 사용
      - 객체의 최상위 속성만 반응형으로 만들고 내부 객체는 반응형을 적용하지 않음
    - 반응형 객체의 크기가 크면 shallowRef() 또는 shallowReactive() 사용하여 성능 최적화

- Vue.js에서 Teleport를 사용하여 성능을 최적화하는 방법
  - Teleport 개념
    - 특정 HTML 요소 바깥으로 컴포넌트 렌더링을 이동하는 기능
  - 최적화
    - DOM 구조를 단순화하여 렌더링 성능을 향상

- Vue.js에서 Memoization을 활용하여 성능을 향상시키는 방법
  - Memoization 개념
    - 동일한 입력값이 들어오면 이전 결과를 캐싱하여 불필요한 연산을 방지하는 기법

  - computed() 활용한 Memoization 처리
    - 이전 결과를 캐싱하여 불필요한 연산 방지함으로써 성능 최적화가 가능

- Vue.js에서 Service Worker를 활용하여 PWA를 구현하는 방법
  - Service Worker 개념
    - PWA(Progressive Web App)의 핵심 기능으로, 브라우저와 네트워크 사이에서 동작하는 스크립트
    - 오프라인 지원, 푸시 알림, 백그라운드 데이터 동기화 등의 기능을 제공

  - Vue에서 Service Worker 적용 방법
    - PWA 플러그인 설치 (vue add pwa)
    - Service Worker 설정 (vue.config.js)
    - 배포 후 캐시 기능 테스트
      - Chrome DevTools → Application → Service Workers에서 확인
    - 네트워크 연결이 끊겨도 앱이 동작 가능하도록 구성할 수 있음.

- Vue.js에서 Nuxt.js를 활용하여 SEO를 최적화하는 방법
  - Nuxt.js를 활용한 SEO 최적화 방법
    - 서버 사이드 렌더링(SSR) 활성화
      ```javascript
      export default {
        ssr: true
      };
      ```
    - 메타 태그 및 Open Graph 설정 (nuxt.config.js)
      ```javascript
      export default {
        head: {
          title: "SEO 최적화된 Vue 앱",
          meta: [
            { name: "description", content: "Vue + Nuxt.js를 활용한 SEO 최적화" },
            { property: "og:title", content: "SEO 최적화 Vue 앱" },
            { property: "og:description", content: "검색 엔진 친화적인 Vue 앱" }
          ]
        }
      };
      ```
  - Nuxt.js는 SSR을 통해 검색 엔진 최적화(SEO)에 유리함

- Vue.js에서 Suspense를 활용하여 초기 로딩 속도를 개선하는 방법
  - Suspense 개념
    - Vue 3에서 비동기 컴포넌트가 로딩될 때까지 대체 UI를 표시하는 기능
  - 개선 방법
    - 초기 로딩을 비동기로 처리하여 UX를 개선하고 성능 최적화 가능
    ```javascript
    <Suspense>
      <template #default>
          <AsyncComponent />
      </template>
      <template #fallback>
          <LoadingSpinner />
      </template>
    </Suspense>
    ```

- Vue.js에서 CSR과 SSR의 차이점과 성능 차이
  - CSR (Client-Side Rendering)
    - 모든 렌더링이 브라우저에서 이루어짐
    - 초기 로딩 속도가 느리지만, 이후 인터랙션 속도가 빠름

  - SSR (Server-Side Rendering)
    - HTML을 서버에서 미리 렌더링하여 브라우저에 제공.
    - SEO에 유리하고, 초기 로딩 속도가 빠름

  - SSR은 SEO 최적화 및 초기 로딩 속도 개선에 유리, CSR은 동적 데이터 처리가 쉬움

- Vue.js에서 Hydration 개념과 성능 최적화 방법
  - Hydration 개념
    - 서버에서 렌더링된 HTML을 클라이언트에서 Vue.js가 재사용하는 과정
  - 성능 최적화 방법
    - defer 속성을 사용하여 스크립트 로딩 최적화
    - 불필요한 컴포넌트 Hydration 방지 (v-once 사용)
    - 서버에서 최소한의 데이터만 렌더링하고, 클라이언트에서 추가 처리
  - Hydration은 SSR과 연계하여 성능을 최적화하는 핵심 기법.

- Vue.js에서 Web Workers를 활용하여 무거운 연산을 최적화하는 방법
  - Web Workers 개념
    - 백그라운드에서 무거운 연산을 실행하여 UI가 멈추지 않도록 도와주는 기능
  - 최적화 방법
    - Web Workers 생성
    - Vue 컴포넌트에서 Worker 사용
  - 복잡한 연산을 별도의 스레드에서 처리하여 UI성능을 유지 가능
  - Web Workers는 무거운 작업을 분리하여 메인 스레드를 최적화

- Vue.js에서 Optimistic UI 패턴을 활용하여 성능을 개선하는 방법
  - Optimistic UI
    - 사용자의 입력에 즉각적인 피드백을 제공하고 서버 응답을 기다리지 않음
  - 성능 개선 적용 예제
    - 서버 응답을 기다리지 않고 UI 반응성을 개선할 수 있음
    ```javascript
    async function updateData() {
      const previousData = state.value;
      state.value = "업데이트 중...";
      
      try {
        await api.update();
      } catch (error) {
        state.value = previousData;
      }
    }
    ```

- Vue Router에서 History Mode와 Hash Mode의 차이점
  - Hash Mode (#): URL에 #이 포함됨 (예: example.com/#/about)
  - History Mode:	# 없이 깔끔한 URL (예: example.com/about)
  - SEO를 고려한다면 History Mode 사용이 권장

- Vue Router에서 beforeEnter()와 beforeEach()의 차이점
  - beforeEnter(): 특정 라우트에만 적용됨
  - beforeEach(): 모든 라우트 변경 전에 실행됨
  - 전역적인 인증 체크에는 beforeEach()를 사용하고, 특정 라우트에 대한 검사에는 beforeEnter()를 활용

- Vue Router에서 Navigation Guards를 활용한 인증 처리 방법
  - beforeEach()를 이용한 인증 확인 방법
    ```javascript
    router.beforeEach((to, from, next) => {
      if (to.meta.requiresAuth && !isAuthenticated()){
        next("/login");
      } else {
        next();
      }
    });
    ```
  - 로그인 여부를 확인하고, 인증이 필요한 페이지로 접근 시 로그인 페이지로 리다이렉션 가능

- Vue.js에서 REST API와 GraphQL을 비교했을 때의 차이점
  - 데이터 요청 방식
    - REST API: 여러 엔드포인트에서 데이터 요청
    - GraphQL: 단일 엔드포인트에서 필요한 데이터만 요청

  - 오버페칭 (Overfetching)
    - REST API: 필요 없는 데이터까지 불러올 가능성 있음
    - GraphQL: 필요한 데이터만 선택적으로 가져올 수 있음

  - 언더페칭 (Underfetching)
    - REST API: 여러 요청을 해야 데이터가 완성됨
    - GraphQL: 한 번의 요청으로 필요한 데이터를 모두 가져올 수 있음

  - GraphQL은 네트워크 요청을 줄이고 최적화된 데이터 페칭이 가능함

- Vue.js에서 Axios를 활용한 API 호출 방법
  - Axios 사용 예제
    ```javascript
    import axios from "axios";

    axios.get("/api/data")
      .then(response => console.log(response.data))
      .catch(error => console.error(error));
    ```
  - fetch()보다 직관적인 API와 자동 JSON 변환 기능을 제공

- Vue.js에서 fetch()와 Axios의 차이점
  - JSON 변환
    - fetch(): response.json() 필요
    - Axios: 자동 변환
  - 에러 처리
    - fetch(): HTTP 에러가 catch()에 잡히지 않음
    - Axios: HTTP 에러도 catch()에서 처리 가능
  - 요청 취소
    - fetch(): 기본적으로 지원하지 않음
    - Axios: AbortController 사용 가능
  - Axios는 편의성이 높고, fetch()는 네이티브 API로 가벼움.

- Vue.js에서 CORS 오류를 해결하는 방법
  - 개요
    - CORS(Cross-Origin Resource Sharing) 오류는 클라이언트가 다른 도메인의 API에 요청할 때 발생하는 보안 정책 문제
  - 해결 방법
    - 백엔드에서 CORS 설정
    - Vue 개발 환경에서 프록시 설정 (vue.config.js)
    - 클라이언트에서 fetch 시 Named 파라미터 추가 ({mode: 'cors'})
  - CORS 설정은 백엔드에서 해결하는 것이 가장 효과적

- Vue.js에서 JWT를 활용하여 인증을 구현하는 방법
  - 개요
    - JWT(JSON Web Token)활용하면 사용자 인증을 위한 토큰 기반 인증 시스템 구현 가능
  - JWT 인증 구현 방법
    - 로그인 시 JWT 발급
      ```javascript
      axios.post('/api/login', { username, password })
      .then(response => {
        localStorage.setItem('token', response.data.token);
      });
      ```
    - API 요청 시 JWT 포함
      ```javascript
      axios.get('/api/user', {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      });
      ```
    - Vue Router에서 인증이 필요한 페이지 보호
      ```javascript
      router.beforeEach((to, from, next) => {
        if (to.meta.requiresAuth && !localStorage.getItem('token')) {
          next('/login');
        } else {
          next();
        }
      });
      ```
    - JWT는 보안성을 높이고, API 요청마다 인증 검증 가능

- Vue.js에서 Vue Query를 활용한 데이터 페칭 방법
  - 개요: Vue Query는 비동기 데이터 가져오기, 캐싱, 갱신을 간편하게 처리하는 라이브러리
  - Vue Query 활용한 데이터 Fetching 방법
    - Vue Query 설치 및 사용
      - 설치
        ```bash
        npm install @tanstack/vue-query
        ```
      - 데이터 Feaching 예제
        ```javascript
        import { useQuery } from '@tanstack/vue-query';

        const { data, error, isLoading } = useQuery(['userData'], () =>
          fetch('/api/user').then(res => res.json())
        );
        ```
    - Vue Query는 캐싱 기능을 제공하여 네트워크 요청을 줄이고 성능을 최적화할 수 있음.

- Vue.js에서 WebSockets을 활용한 실시간 데이터 업데이트 방법
  - 개요: WebSocket을 사용하면 서버와 클라이언트 간의 실시간 데이터 전송이 가능
  - WebSocket 실시간 데이터 처리 방법
    ```javascript
    const socket = new WebSocket("wss://example.com/socket");

    socket.onmessage = event => {
      console.log("새로운 데이터:", event.data);
    };

    socket.send(JSON.stringify({ message: "Hello Server!" }));
    ```
  - WebSocket은 실시간 채팅, 알림 시스템, 실시간 데이터 스트리밍에 유용

- Vue.js에서 Lazy Loading Routes를 적용하는 방법
  - 개요: Lazy Loading을 적용하면 필요한 페이지만 로드하여 초기 로딩 속도를 최적화 가능
  - Vue Router Lazy Loading 설정
    ```javascript
    const routes = [
      {
        path: '/about',
        component: () => import('@/views/About.vue')
      }
    ];
    ```
  - 라우트별로 동적 import를 사용하면 성능을 최적화 가능

- Vue.js에서 Dynamic Route Matching을 활용하는 방법
  - 개요: Dynamic Route Matching은 URL의 특정 부분을 동적으로 변경할 때 사용
  - 동적 라우트 설정
    ```javascript
    const routes = [
      { path: '/user/:id', component: UserProfile }
    ];
    ```
  - 동작 파라미터 접근
    ```javascript
    const route = useRoute();
    console.log(route.params.id);
    ```
  - 사용자 ID, 게시글 ID 등과 같이 URL 기반 데이터에 적합

- Vue.js에서 keep-alive를 활용하여 페이지 상태를 유지하는 방법
  - 개요: <keep-alive>를 사용하면 페이지 이동 후에도 컴포넌트 상태 유지 가능
  - 예제
    ```javescript
    <keep-alive>
      <router-view />
    </keep-alive>
    ```
  - 탭 간 전환이 잦은 앱에서 성능 향상 가능

- Vue.js에서 Prefetching을 활용하여 네트워크 요청 최적화하는 방법
  - Prefetching 개념
    - 사용자가 필요할 가능성이 높은 데이터를 미리 로드하여 속도를 높이는 기법
  - 사용 예
    ```html
    <link rel="prefetch" href="/assets/large-image.jpg">
    ```
  - 페이지 전환을 부드럽게 만들고 사용자 경험 개선 가능

- Vue.js에서 Server-Side Rendering(SSR)을 활용하는 이유
  - SSR의 장점
    - SEO 최적화 (검색 엔진 크롤러가 HTML을 쉽게 분석)
    - 빠른 초기 로딩 속도
    - 페이지 콘텐츠가 미리 렌더링됨
  - Nuxt.js를 사용하면 Vue.js에서 쉽게 SSR을 적용할 수 있음

- Vue.js에서 Nuxt.js를 활용하여 SSR을 구현하는 방법
  - 개요: Nuxt.js를 사용하면 자동으로 서버에서 Vue 컴포넌트 렌더링 가능
  - 구현 절차
    - Nuxt.js 프로젝트 생성 (npx create-nuxt-app my-app)
    - 페이지 설정
      ```javascript
      <template>
        <div>
          <h1>{{ data }}</h1>
        </div>
      </template>

      <script setup>
      const { data } = useFetch('/api/data');
      </script>
      ```
  - SEO가 중요한 프로젝트에 Nuxt.js를 활용하면 유리

- Vue.js에서 GraphQL을 활용하여 데이터를 가져오는 방법
  - 개요: REST API보다 유연하게 데이터를 가져올 수 있음
  - Apollo Client 사용 예제
    - 설치
    - 쿼리 실행
  - GraphQL은 REST API보다 유연하고 필요한 데이터만 가져올 수 있음

- Vue.js에서 Suspense와 async components를 함께 사용 가능 여부
  - 가능 여부
    - Suspense를 활용하면 비동기 컴포넌트가 로딩되는 동안 UI를 관리할 수 있음
  - 예제
    ```javascript
    <Suspense>
      <template #default>
        <AsyncComponent />
      </template>
      <template #fallback>
        <LoadingSpinner />
      </template>
    </Suspense>
    ```
  - 비동기 컴포넌트를 효율적으로 로딩하고 사용자 경험을 개선할 수 있음

- Vue.js에서 Vue Resource와 Axios의 차이점
  - Vue Resource 는 더 이상 유지보수 되지 않으며, Axios 사용 권장
  - Vue Resource 는 JSON 자동 변환 X, 공식 지원 종료

- Vue.js에서 API 응답을 캐싱하는 방법
  - 캐싱 방법
    - localStorage, sessionStorage 사용
    - Vue Query의 캐싱 기능 활용
    - HTTP 응답 헤더에서 Cache-Control 설정
  - API 호출 횟수를 줄이고 성능을 최적화 가능

- Vue.js의 Composition API에서 Pinia를 활용한 고급 상태 관리 패턴
  - Pinia는 Vue 3의 공식 상태 관리 라이브러리로, Composition API와 자연스럽게 결합
  - Composition API + Pinia를 활용하면 모듈화된 스토어를 생성하고, setup() 내에서 직접 상태를 관리 가능
  - Pinia의 고급 패턴
    - Getter + Computed 활용 (반응형 상태 관리)
    - Action에서 비동기 작업 수행
    - State Persist(로컬 스토리지 저장)
    - Setup Store vs Option Store 패턴 활용

- Vue.js에서 Teleport와 Suspense를 조합하여 최적화하는 방법
  - Teleport: 특정 요소를 DOM의 원하는 위치로 이동시키는 기능
  - Suspense: 비동기 컴포넌트가 데이터를 로드할 때 로딩 상태를 표시하는 기능
  - 조합 예제
    ```javascript
    <template>
      <Teleport to="body">
        <Suspense>
          <template #default>
            <AsyncComponent />
          </template>
          <template #fallback>
            <p>Loading...</p>
          </template>
        </Suspense>
      </Teleport>
    </template>
    ```
    - 활용 시나리오
      - Teleport → 모달, 알림창을 body로 이동해 레이아웃 문제 해결
      - Suspense → 데이터 로딩 시 깜빡임 없이 스켈레톤 UI 구현 가능

- Vue.js에서 Vite와 Webpack의 차이점 및 성능 비교
  - 번들링 방식
    - Vite: ES 모듈 기반
    - Webpack: 모든 파일을 하나로 번들링
  - 빌드 속도	
    - Vite: 매우 빠름 (HMR 즉시 반영)
    - Webpack: 느림 (번들링 후 HMR)
  - 개발 서버
    - Vite: ESM 기반 핫 리로드 (HMR) 지원
    - Webpack: 번들링 후 서버 실행
  - 코드 스플리팅
    - Vite: 자동 지원
    - Webpack: 설정 필요
  - SSR 지원
    - Vite: 기본 지원
    - Webpack: 추가 설정 필요
  - Vite는 ES 모듈(ESM) 기반으로 개발 서버가 즉시 실행되어 빠른 개발 경험을 제공
  - Webpack은 대규모 프로젝트에서 여전히 강력한 설정이 가능하지만, 느림
  - Vue 3 공식 도구는 Vite 기반이므로 최신 프로젝트는 Vite 사용을 추천

- Vue.js에서 isRef(), shallowRef(), customRef()의 차이점
  - isRef(value): value가 ref()인지 확인 (true/false 반환)
  - shallowRef(value): 객체 내부까지 반응형이 아님 (깊은 반응성 X)
  - customRef(): 사용자 정의 Ref 생성 가능 (디바운스 적용 가능)

- Vue.js에서 SSR(Server-Side Rendering)과 SSG(Static Site Generation)의 차이점
  - 렌더링 시점
    - SSR: 요청 시 서버에서 HTML 생성
    - SSG: 빌드 시 정적인 HTML 생성
  - 초기 로딩 속도
    - SSR: 빠름 (SEO 최적화)
    - SSG: 매우 빠름 (캐시 가능)
  - 동적 데이터
    - SSR: 가능 (실시간 API 호출)
    - SSG: 제한적 (사전 빌드된 데이터)
  - 사용 예시
    - SSR: Vue + Nuxt 3
    - SSG: Vue + Nuxt 3 (Static Mode)
  - SEO(검색 엔진 최적화) 목적이라면 SSR을, 빠른 정적 페이지 제공이 목표라면 SSG를 선택

- Vue.js의 주요 특징과 React와의 차이점
  - 렌더링 방식
    - Vue.js: 가상 DOM + 템플릿
    - React: 가상 DOM + JSX
  - 상태 관리
    - Vue.js: Pinia, Vuex
    - React: Redux, Zustand
  - 컴포넌트 스타일
    - Vue.js: SFC (Single File Component)
    - React: JSX 스타일
  - 라우팅
    - Vue.js: Vue Router
    - React: React Router
  - Vue는 SFC 기반으로 HTML/CSS/JS를 분리하여 사용이 직관적
  - React는 JSX를 활용하여 동적 UI 구현이 유연함

- Vuex를 사용한 상태 관리 경험을 설명
  - Vuex는 Vue 2/3에서 공식 상태 관리 라이브러리 (현재는 Pinia가 권장됨)
  - Mutation을 활용한 상태 변경, Action을 통한 비동기 처리 경험
  - Vuex는 중앙 집중식 상태 관리가 가능하지만, 코드가 많아져 Pinia로 대체되는 추세

- Vue.js에서의 라우팅 처리 방법
  - Vue Router를 사용하여 페이지 간 네비게이션 관리
  - SPA(Single Page Application)에서 동적 라우팅을 제공하여 효율적인 내비게이션 구현 가능

- Vue.js의 Reactivity 시스템 내부 동작 원리
  - Vue는 Proxy API를 활용하여 반응형(Reactivity) 시스템을 구현
  - effect() 함수를 사용하여 의존성 추적 및 자동 업데이트
  - Vue 3의 Proxy 기반 반응형 시스템은 성능이 개선됨

- Vue.js의 Composition API와 Options API의 차이점
  - 코드 구조
    - Composition API: setup() 함수 사용
    - Options API: data, methods, computed 사용
  - 재사용성
    - Composition API: Composable 함수 활용
    - Options API: Mixin 사용
  - Vue 3 최적화
    - Composition API: 권장
    - Options API: 기존 방식 유지
  - Composition API는 더 유연하고, Vue 3에서 공식적으로 권장됨

- Vue.js의 Virtual DOM Diffing 알고리즘
  - Vue.js는 Virtual DOM을 사용하여 효율적인 렌더링을 수행
  - Vue 3에서는 "Block Tree Optimization"과 "Static Hoisting"을 추가하여 최적화
  - Diffing 알고리즘 주요 과정
    - 새로운 Virtual DOM을 생성 (render())
    - 이전 Virtual DOM과 비교하여 변경 사항을 찾음 (patch())
    - 변경된 부분만 실제 DOM에 적용하여 성능 최적화
  - Vue 3의 최적화 기법
    - Block Tree Optimization → 변경된 노드만 업데이트하여 속도 향상
    - Static Hoisting → 변하지 않는 정적 노드는 재사용하여 성능 개선

- Vue.js의 Server-Side Rendering(SSR)과 Static Site Generation(SSG)
  - SSR (서버사이드 렌더링) → Nuxt.js 활용
  - SSG (정적 사이트 생성) → Nuxt.js target: static 활용
  - SEO 최적화 필요 시 SSR 사용, 속도 최적화 필요 시 SSG 사용

- Vue.js의 단방향 데이터 흐름(One-way data flow)과 양방향 바인딩(Two-way binding)의 차이점
  - 설명
    - 단방향 데이터 흐름: 부모 → 자식 데이터 전달
    - 양방향 바인딩: 부모 ↔ 자식 데이터 동기화
  - 사용 예제
    - 단방향 데이터 흐름: props 사용
    - 양방향 바인딩: v-model 사용
  - 장점
    - 단방향 데이터 흐름: 데이터 흐름이 명확
    - 양방향 바인딩: 편리한 양방향 데이터 처리
  - 단점
    - 단방향 데이터 흐름: 수동적으로 값 변경해야 함
    - 양방향 바인딩: 데이터 흐름이 복잡해질 수 있음

- Vue.js에서 v-model과 @input 이벤트의 차이
  - v-model은 내부적으로 @input과 :value를 조합한 것
  - @input 이벤트를 직접 사용할 수도 있음

- Vue.js에서 v-bind와 v-on을 단축해서 사용할 수 있는 방법
  - v-bind → : (콜론)으로 단축
  - v-on → @ (골뱅이)로 단축

- Vue.js에서 ref()와 reactive()를 사용하는 기준
  - 반응형 대상
    - ref(): 기본형 (String, Number)
    - reactive(): 객체 & 배열
  - 접근 방식
    - ref(); .value 사용
    - reactive(): 직접 접근 가능
  - Vue 3에서 추천
    - ref(): 기본 데이터 타입 관리
    - reactive(): 객체 상태 관리

- Vue.js에서 computed() 속성을 사용할 때 성능 최적화 효과가 있는 이유
  - computed()는 종속된 값이 변경될 때만 재계산됨
  - watch()와 다르게 캐싱(Cache) 기능 제공
  - 반응형 데이터가 변경될 때만 실행되므로 성능 최적화 효과가 있음

- Vue.js의 watch()와 watchEffect()의 차이점과 각각의 사용 사례
  - 트리거 방식
    - watch(): 특정 데이터 변경 감지
    - watchEffect(): 내부에서 자동 감지
  - 반응형 데이터 접근 방식
    - watch(): 명시적으로 지정
    - watchEffect(): 자동으로 종속성 추적
  - 사용 예제	
    - watch(): watch(count, (newVal) => {})
    - watchEffect(): watchEffect(() => console.log(count.value))
  - watchEffect()는 자동으로 종속성을 추적하여 더 유연하게 사용 가능

- Vue.js의 v-if, v-else-if, v-show의 차이점
  - v-if는 DOM 조작 비용이 크지만 성능이 좋고, v-show는 초기 렌더링 비용이 있지만 빠르게 토글 가능

- Vue.js에서 v-for와 key 속성을 함께 사용하는 이유
  - v-for는 리스트를 렌더링할 때 새로운 항목을 추가하거나 삭제할 경우 기존 DOM을 재사용
  - key 속성이 없으면 Vue가 DOM 요소를 효율적으로 업데이트하지 못하고 예상치 못한 UI 버그가 발생할 수 있음
  - key를 고유한 값(예: ID)으로 지정하면 Vue가 변경된 요소를 올바르게 감지하고, 최소한의 DOM 변경으로 성능을 최적화할 수 있음
  - 올바른 key 설정을 통해 리스트 렌더링 성능을 최적화하고 UI 오류를 방지

- Vue.js에서 setup() 함수 내부에서 this를 사용할 수 없는 이유
  - setup()은 Vue 3의 Composition API에서 사용되며, Options API의 this와는 완전히 다른 개념.
  - Options API에서는 this가 Vue 인스턴스를 가리키지만, setup()에서는 Vue 인스턴스가 생성되기 전이므로 this를 사용할 수 없음.
  - 대신 ref(), reactive(), computed() 등을 활용하여 상태를 관리하고 반환해야 함
  - setup 내부에서는 this를 사용할 수 없으며, 상태를 반환하여 템플릿에서 사용해야 함

- Vuex와 Pinia의 차이점과 Pinia가 Vuex보다 유리한 점
  - Pinia는 더 간단한 API, 자동 타입 지원, Composition API 친화적인 구조로 Vuex보다 사용하기 쉽고 효율적

- Vue.js에서 Vuex modules를 사용하는 이유
  - 대규모 애플리케이션에서 상태 관리를 모듈 단위로 분리하여 유지보수성과 가독성을 높이기 위함
  - 전역 스토어가 한 파일에 모든 데이터를 관리하면 복잡성이 증가 → 모듈을 사용하면 기능별로 분리 가능.
  - 네임스페이스(namespace) 지정 가능 → 특정 모듈에서만 접근할 수 있도록 관리 가능.
  - 모듈화를 통해 상태 관리의 복잡성을 줄이고, 유지보수를 용이하게 함

- Vue.js에서 Vuex getters와 actions의 차이점
  - Getters는 상태를 가공하여 제공하고, Actions는 비동기 작업을 처리하는 역할

- Vue.js에서 Vuex mutations과 actions의 차이점
  - Mutations는 동기적으로 상태를 변경하고, Actions는 비동기 처리를 담당

- Vue.js에서 Vuex의 비동기 처리를 할 때 고려해야 할 사항
  - 비동기 작업은 반드시 Actions에서 처리
    - Mutations는 동기적으로 작동하므로, 비동기 처리 후 상태 변경 시 문제 발생 가능
    - Actions 내부에서 API 요청을 실행한 후, commit()을 통해 Mutation을 호출해야 함

  - Promise 또는 async/await을 활용하여 오류 처리
    - API 요청 실패 시 try-catch 블록을 활용하여 예외를 처리해야 함.
  - 비동기 처리는 Actions에서 수행하고, 오류 처리를 고려해야 함

- Vue.js에서 Pinia를 활용하여 전역 상태를 관리하는 방법
  - Pinia는 Vuex보다 간결하고, TypeScript 지원이 우수하며, Composition API 친화적
    - Pinia 스토어 생성 (store.js)
    - 스토어 사용 (App.vue)

- Vue.js에서 localStorage, sessionStorage, cookies를 활용한 상태 관리 방법
  - localStorage는 장기 저장
  - sessionStorage는 탭 종료 시 삭제
  - cookies는 서버와 인증 정보 공유에 적합

- Vue.js에서 reactivity transform이 상태 관리에서 어떤 역할
  - Vue 3.3에서 도입된 Reactivity Transform은 ref()를 더 간편하게 사용할 수 있도록 개선된 기능
  - ref()를 사용할 때 .value를 명시적으로 호출해야 하지만, Reactivity Transform을 사용하면 이를 생략할 수 있음.
  - 자동 reactive() 변환 기능을 통해 ref()와 reactive()를 혼합하여 사용할 수 있어 코드를 더 직관적이고 간결하게 유지할 수 있음.
  - Reactivity Transform을 사용하면 ref()의 .value를 생략할 수 있어 코드 가독성과 유지보수성이 향상

- Vue.js에서 shallowRef()와 shallowReactive()를 사용하는 이유
  - shallowRef(): 값이 변경될 때만 반응하고, 내부 객체 변경은 감지하지 않음
  - shallowReactive(): 객체의 최상위 속성만 반응형으로 처리됨
  - shallowRef()와 shallowReactive()는 성능 최적화를 위해 필요하며, 불필요한 반응형 상태를 줄일 수 있음

- Vue.js에서 props와 emit을 활용한 컴포넌트 간 데이터 전달 방법
  - Props는 부모 → 자식, emit은 자식 → 부모 데이터 전달을 위해 사용됨 (defineEmits)

- Vue.js에서 slot과 scoped slot의 차이점
  - 일반 slot: 부모가 제공하는 HTML이 자식 컴포넌트 내부에 삽입됨
  - Scoped slot: 자식이 제공하는 데이터를 부모가 활용할 수 있음	
  - Scoped slot을 활용하면 자식 컴포넌트의 데이터를 부모가 활용할 수 있어 유연한 UI 구성이 가능

- Vue.js에서 Teleport의 역할과 사용 사례
  - Teleport는 특정 HTML 요소로 직접 렌더링할 수 있도록 도와주는 기능
  - 사용 사례: 모달, 툴팁, 드롭다운 등 특정 DOM 계층에서 벗어나야 하는 요소
  - Teleport를 사용하면 특정 요소를 원하는 DOM 위치에 렌더링할 수 있어 UI가 더 깔끔해짐

- Vue.js에서 keep-alive의 역할
  - keep-alive는 동적으로 변경되는 컴포넌트를 메모리에 유지하여 성능을 최적화
  - 사용 사례: 탭 전환 시 이전 상태 유지
  - keep-alive를 사용하면 컴포넌트가 재랜더링될 때 상태를 유지할 수 있어 성능이 향상됨

- Vue.js에서 mixins과 composables의 차이점
  - Vue 3에서는 Mixins보다 Composables를 사용하여 상태와 로직을 더 직관적으로 분리할 수 있음

- Vue.js에서 Fragment 기능을 활용하는 이유
  - Fragment는 불필요한 부모 태그 없이 여러 요소를 렌더링할 수 있도록 지원
  - Vue 2에서는 div 등의 부모 요소가 필요했지만, Vue 3에서는 불필요한 wrapping을 제거 가능
  - Fragment를 사용하면 불필요한 wrapping을 제거하여 코드가 더 깔끔해짐

- Vue.js에서 dynamic component를 렌더링하는 방법
  - component 태그를 사용하여 동적으로 컴포넌트를 변경 가능
  - Dynamic Component를 사용하면 상태에 따라 컴포넌트를 동적으로 변경 가능

- Vue.js에서 key 속성을 활용하여 리스트 렌더링 성능을 최적화하는 방법
  - key 속성은 리스트가 변경될 때 기존 요소를 효율적으로 재사용하는 데 도움을 줌.
  - index를 key로 사용하면 성능이 저하될 수 있으므로 고유한 값(예: id)을 사용해야 함
  - 고유한 key 값을 사용하면 리스트 업데이트 성능을 최적화할 수 있음

- Vue.js에서 lazy loading을 구현하는 방법
  - Vue 3에서는 dynamic import를 활용하여 Lazy Loading을 구현 가능

- Vue.js에서 template refs를 활용하여 DOM 요소에 접근하는 방법
  - template refs를 활용하면 특정 DOM 요소에 직접 접근할 수 있음

- Vue.js에서 watch()를 과도하게 사용할 때 발생할 수 있는 문제
  - 불필요한 watch 사용으로 인해 렌더링 성능 저하 가능
  - watch 내부에서 상태를 변경하면 무한 루프가 발생할 위험 있음.
  - watch()를 남용하면 성능이 저하될 수 있으므로, computed() 또는 watchEffect()를 고려해야 함

- Vue.js에서 ref()와 computed()를 활용하여 성능을 개선하는 방법
  - ref(): 단순 상태 저장
  - computed(): 계산된 값을 캐싱하여 불필요한 연산 방지
  - computed()를 사용하면 성능을 최적화하고 불필요한 연산을 방지할 수 있음

- Vue.js에서 Vue DevTools을 활용하여 성능을 분석하는 방법
  - Vue DevTools는 Vue 애플리케이션의 상태 및 성능을 분석하는 Chrome/Firefox 확장 프로그램
  - 주요 기능
    - Component Tree: 현재 렌더링된 모든 컴포넌트의 상태를 확인 가능
    - Vuex/Pinia 상태 확인: Vuex 및 Pinia의 상태 변화를 실시간으로 추적
    - Performance Timeline: 컴포넌트 렌더링 시간을 측정하여 최적화 포인트 파악
    - Event Inspector: 컴포넌트 간 이벤트 흐름을 분석
  - Vue DevTools를 활용하면 상태 변경 및 성능 병목을 직관적으로 파악할 수 있음

- Vue.js에서 Virtual Scroll을 활용하여 성능을 최적화하는 방법
  - Virtual Scroll은 대량의 리스트를 렌더링할 때 보이는 항목만 동적으로 렌더링하여 성능을 최적화하는 기법.
  - vue-virtual-scroller 또는 vue3-virtual-scroller 같은 라이브러리를 사용 가능
  - Virtual Scroll을 사용하면 DOM에 렌더링되는 엘리먼트 수를 줄여 성능이 향상됨

- Vue.js에서 Intersection Observer API를 활용하여 Lazy Loading을 구현하는 방법
  - Intersection Observer API를 사용하면 요소가 화면에 보이는 순간만 렌더링하도록 설정 가능
  - Intersection Observer API를 사용하면 불필요한 렌더링을 방지하고, 성능을 최적화할 수 있음
  - 구현 방법
    ```javascript
    <template>
      <img v-if="isVisible" src="image.jpg" />
    </template>

    <script setup>
    import { ref, onMounted } from 'vue';

    const isVisible = ref(false);
    const observer = new IntersectionObserver(([entry]) => {
      isVisible.value = entry.isIntersecting;
    });

    onMounted(() => {
      observer.observe(document.querySelector('img'));
    });
    </script>
    ```

- Vue.js에서 async setup()을 사용할 때 성능 최적화하는 방법
  - async setup() 내부에서 비동기 데이터를 병렬로 가져오거나 Suspense와 함께 사용
  - Suspense와 함께 사용하면 초기 로딩 경험이 개선됨

- Vue.js에서 Tree Shaking을 활용하여 불필요한 코드 제거하는 방법
  - 사용하지 않는 모듈을 제거하여 번들 크기를 줄이는 최적화 기법
  - Vite나 Webpack에서 자동 적용되지만, import { specificFunction } from 'lodash-es' 같은 방식으로 모듈 단위로 가져와야 함
  - Tree Shaking을 활용하면 앱 번들 크기가 줄어들고, 성능이 향상됨

- Vue.js에서 debounce와 throttle을 활용하여 이벤트 핸들링을 최적화
  - debounce: 일정 시간 동안 입력이 없으면 실행
  - throttle: 일정 시간 간격으로 실행
  - Debounce와 Throttle을 활용하면 불필요한 연산을 줄여 성능을 최적화할 수 있음

- Vue.js에서 memoization을 활용하여 성능을 최적화하는 방법
  - computed()를 사용하여 불필요한 재계산을 방지
  - Memoization을 활용하면 동일한 입력에 대해 결과를 캐싱하여 성능을 최적화할 수 있음

- Vue.js에서 Prefetching과 Preloading의 차이점
  - Preloading은 즉시 로드, Prefetching은 사용 가능성을 고려한 로드
  - Prefetching: 사용자 요청 전에 리소스를 미리 로드
    - 페이지 전환 시 미리 불러오기
  - Preloading: 페이지가 로드될 때 즉시 로드 (우선순위 높음)
    - 중요한 리소스 미리 로드

- Vue.js에서 History Mode와 Hash Mode의 차이점
  - History Mode
    - example.com/page URL 구조
    - SEO 가능
    - 설정 방법: mode: 'history'
      - 깔끔한 URL 제공 가능하나 서버 설정이 필요
  - Hash Mode
    - example.com/#/page URL 구조
    - SEO 불가능
    - 설정 방법: 기본 설정

- Vue.js에서 beforeEnter()와 beforeEach()의 차이점
  - beforeEach(): 모든 라우트 전환마다 실행
  - beforeEnter(): 특정 라우트로 진입할 때만 실행
  - beforeEach()는 전역, beforeEnter()는 특정 라우트에서 실행됨

- Vue.js에서 Navigation Guards를 활용한 인증 처리 방법
  - 예를 들어 로그인 여부 확인 후 특정 페이지 접근 제한 처리
  - Navigation Guards를 사용하면 인증이 필요한 페이지에 대한 접근 제어 가능

- Vue.js에서 Lazy Loading Routes를 적용하는 방법
  - defineAsyncComponent 또는 import()를 활용
  - Lazy Loading을 적용하면 초기 번들 크기를 줄일 수 있음

- Vue.js에서 Dynamic Route Matching을 활용하는 방법
  - 동적인 값(:id)을 포함하는 라우트 정의
    - 예: '/user/:id'
  - Dynamic Route Matching을 활용하면 특정 데이터 기반의 URL을 만들 수 있음

- Vue.js에서 keep-alive를 활용하여 페이지 상태를 유지하는 방법
  - 예제 코드
    ```javascript
    <keep-alive>
      <component :is="activeComponent" />
    </keep-alive>
    ```
  - keep-alive를 사용하면 컴포넌트의 상태를 유지하면서 성능을 최적화할 수 있음

- Vue.js에서 REST API와 GraphQL을 비교했을 때의 차이점
  - GraphQL은 필요한 데이터만 요청할 수 있어 성능 최적화에 유리함
  - GraphQL은 유연성이 높으며 필요한 데이터만 요청 가능

- Vue.js에서 Axios를 활용한 API 호출 방법
  - 예제
    ```javascript
    import axios from 'axios';

    axios.get('/api/data')
      .then(response => console.log(response.data));
    ```
  - Axios는 직관적인 API 요청을 지원하며, Vue.js와 함께 사용하기 편리함

- Vue.js에서 fetch()와 Axios의 차이점
  - fetch는 기본 제공(기본 내장), Axios는 별도 설치 필요
  - Axios는 자동 JSON 변환 기능 탑재, 요청 취소 가능
  - Axios는 JSON 변환이 편리하며, 추가 기능이 많아 Vue 프로젝트에서 자주 사용

- Vue.js에서 CORS 오류를 해결하는 방법
  - CORS(교차 출처 리소스 공유) 오류는 서버와 클라이언트의 도메인이 다를 때 발생
  - 해결 방법
    - 백엔드에서 CORS 허용하는 방법 (권장 해결책)
      ```javascript
      res.setHeader('Access-Control-Allow-Origin', '*');
      ```
    - 프록시 서버 설정 (vue.config.js)
      ```javascript
      module.exports = {
        devServer: {
          proxy: 'http://backend.com'
        }
      };
      ```

- Vue.js에서 JWT를 활용하여 인증을 구현하는 방법
  - 개요
    - JWT(JSON Web Token)은 사용자 인증 및 상태를 유지하는 방식
  - 구현 방법
    - 사용자가 로그인 → 백엔드에서 JWT 발급
    - Vue.js에서 JWT를 localStorage 또는 Vuex에 저장
    - 모든 API 요청 시 Authorization 헤더에 JWT 포함
    - 백엔드에서 JWT 검증 후 응답
  - JWT는 토큰 기반 인증 방식으로, 세션을 저장할 필요 없이 사용 가능

- Vue.js에서 Vue Query를 활용한 데이터 페칭 방법
  - Vue Query는 데이터를 자동으로 캐싱하고 업데이트하는 라이브러리
  - 예제 코드
    ```javascript
    import { useQuery } from '@tanstack/vue-query';

    const { data, isLoading } = useQuery(['todos'], fetchTodos);
    ```
  - 캐싱, 자동 갱신, 비동기 상태 관리를 간편하게 구현 가능

- Vue.js에서 WebSockets을 활용한 실시간 데이터 업데이트
  - 개요
    - WebSockets은 클라이언트와 서버 간 양방향 통신 가능
    - 실시간 채팅, 주식가격 업데이트 등에 사용
  - 구현 방법: socket 생성 > onmessage 로 이벤트 감지
  - HTTP 요청 없이 실시간 데이터 업데이트 가능

- Vue.js에서 API 응답을 캐싱하는 방법
  - Vue Query 또는 localStorage 를 사용
  - Vue Query
    ```javascript
    useQuery(['users'], fetchUsers, { staleTime: 60000 });
    ```
  - Axios 캐싱
    ```javascript
    const cache = new Map();
    function fetchData(url) {
      if (cache.has(url)) return Promise.resolve(cache.get(url));
      return axios.get(url).then(response => {
        cache.set(url, response.data);
        return response.data;
      });
    }
    ```
  - 캐싱을 활용하면 네트워크 요청을 줄여 성능을 최적화할 수 있음

- Vue.js에서 SSR(Server-Side Rendering)을 활용하는 이유
  - SEO 최적화 (서버 부하 증가의 이슈는 존재)
  - 초기 로딩 속도 빠름 (개발 복잡도 증가 이슈는 존재)
  - 소셜 미디어 미리보기 지원
  - SSR은 SEO가 중요한 경우 필수

- Vue.js에서 CSR(Client-Side Rendering)과 SSR(Server-Side Rendering)의 차이점
  - CSR은 브라우저, SSR은 서버 렌더링
  - CSR은 SEO 지원 약하며, SSR은 SEO 지원 좋음
  - 초기 로딩 속도는 SSR이 빠름
  - SEO가 필요하면 SSR, 인터렉션이 많으면 CSR 선택

- Vue.js에서 Static Site Generation(SSG)과 Server-Side Rendering(SSR)의 차이점
  - SSG는 빌드 시 페이지 생성, SSR은 요청할 때 생성
  - SSG는 속도가 매우 빠르며 SSR은 느릴 수도 있음
  - SSG는 유지보수 쉬우며 SSR은 어려움
  - 정적인 블로그는 SSG, 동적인 데이터는 SSR 사용

- Vue.js에서 Hydration 개념과 성능 최적화 방법
  - Hydration: SSR로 렌더링된 HTML을 브라우저에서 다시 활성화하는 과정
  - 최적화 방법
    - defer 또는 async 스크립트 로드
    - lazy 속성을 사용해 필요한 부분만 활성화
    - Suspense 활용
  - Hydration 최적화하면 초기 로딩 속도가 개선됨

- Vue.js에서 Nuxt.js를 활용하여 SEO를 최적화하는 방법
  - Nuxt.js는 SEO 최적화가 가능한 SSR 지원 Vue 프레임워크.
  - Meta 태그 설정
    ```javascript
    useHead({
      title: 'SEO 최적화',
      meta: [{ name: 'description', content: 'Nuxt.js를 사용한 SEO' }]
    });
    ```
  - Nuxt.js는 SEO 필수 프로젝트에서 유용함

- Vue.js에서 Incremental Static Regeneration(ISR)
  - 기존 SSG에서 특정 페이지만 동적으로 재생성 가능
  - Next.js에서는 지원하지만 Nuxt.js는 아직 미지원.
  - ISR은 정적 페이지를 동적으로 업데이트할 수 있는 기능

- Vue.js에서 Edge Functions를 사용 시 장점
  - 서버리스 환경에서 실행 가능
  - CDN 가까운 곳에서 실행되어 성능 향상
  - 예시: Vercel Edge Functions, Cloudflare Workers
  - 사용자 위치 기반으로 빠른 응답 가능

- Vue.js에서 Static Rendering과 Streaming SSR의 차이
  - Streaming SSR은 초기 로딩을 빠르게 함

- Vue.js에서 Composition API와 Options API의 차이점
  - Composition API: 함수 기반 코드 구조, 복잡한 로직 > 효율적
  - Options API: 객체 기반의 코드 구조, 복잡한 로직 > 가독성 낮음

- Vue.js에서 Teleport와 Suspense를 조합하여 성능을 최적화하는 방법
  - Teleport + Suspense를 사용하면 비동기 로딩을 최적화 가능
  - 예제 코드
    ```javascript
    <Suspense>
      <template #default>
        <AsyncComponent />
      </template>
      <template #fallback>
        Loading...
      </template>
    </Suspense>
    ```

- Vue.js에서 Vite와 Webpack의 차이점 및 성능 비교
  - Vite: 속도 매우 빠름, 모듈 기반 빌드 방식
  - Webpack: 속도 느림, 번들링 빌드 방식
  - 개발 속도가 중요하다면 Vite 사용 권장

- Vue.js에서 Server Components를 활용 시 이점
  - 개요
    - 서버에서 컴포넌트를 렌더링하여 클라이언트로 전달하는 방식
    - React의 Server Components 개념과 유사하며, Vue에서도 연구 중
  - 이점
    - 클라이언트에서 JavaScript 실행 최소화 → 초기 로딩 속도 개선.
    - 서버에서 직접 데이터 가져오기 가능 → API 호출 최소화.
    - 보안 강화 → 클라이언트에 노출되지 않는 서버 전용 컴포넌트 활용 가능.
    - SEO 최적화 가능 → HTML을 서버에서 완성하여 전달.
  - 단점
    - 현재 Vue 공식 지원은 부족하며, Nuxt 3와 같은 SSR 기반 프레임워크 활용이 필요

- Vue.js에서 Tree Shaking과 Dead Code Elimination의 차이점
  - Tree Shaking
    - 사용되지 않는 코드를 제거하는 최적화 기법
    - 번들링 단계(웹팩, 바이트) 때 실행
    - import 된 모듈을 분석하여 불필요한 코드 제거
  - Dead Code Elimination
    - 컴파일러가 실행되지 않는 코드를 자동 제거
    - 컴파일 단계 (JS 엔진, Terser) 때 실행
    - 실행되지 않는 코드를 정적으로 분석하여 제거
  - 정리
    - Tree Shaking은 번들러(Webpack, Vite)가 불필요한 코드를 제거하는 기법
    - Dead Code Elimination은 컴파일러 레벨에서 실행되지 않는 코드를 제거하는 최적화 기법

- Vue.js에서 Vue 3.3 이후 추가된 주요 기능
  - (1) defineModel()
  - (2) v-memo
  - (3) Suspense 개선

- Vue.js에서 GraphQL을 사용할 때 고려해야 할 보안 이슈
  - 과도한 요청(Over-fetching)
    - 클라이언트가 불필요한 데이터까지 요청
    - Schema를 최소화하고 필요 데이터만 반환하여 해결
  - 무한 반복 쿼리(Recursive Query Attack)
    - 쿼리가 무한 중첩되어 서버 과부하 발생
    - Query Depth 제한하여 해결
  - 배치 요청으로 인한 DDoS 위험
    - 하나의 요청으로 과도한 데이터 요청 가능
    - 요청당 rate limit 적용하여 해결
  - GraphQL Injection
    - SQL Injection과 유사하게 악성 쿼리 삽입 가능
    - 입력 데이터 검증(GraphQL Shield 사용) 통한 해결

- SSR이 SEO(Search Engine Optimization)에 효과적인 이유
  - 웹사이트가 사용자에게 보여지는 과정 (2가지 방식)
    - CSR: 웹페이지가 브라우저에서 만들어짐 (사용자 PC에서)
    - SSR: 웹페이지가 서버에서 먼저 만들어져 사용자에게 전달됨
  - 검색엔진(구글, 네이버)에서 웹사이트를 잘 인식할 수 있는지 여부에서 큰 차이가 있음

  - CSR 방식의 문제점
    - 개념: CSR 방식은 웹사이트를 사용자의 브라우저에서 직접 만들어서 보여주는 방식
    - 예제
      - 사용자가 www.example.com을 방문하면, 처음에는 빈 화면이 나오고, 이후에 자바스크립트(JS) 가 실행되면서 페이지 내용이 채워짐
    - 문제는 구글, 네이버 같은 검색엔진도 웹사이트를 방문할 때 이와 같은 방식으로 본다는 것
      - 즉, 검색엔진이 웹사이트를 방문했을 때 아무것도 없는 빈 화면을 보게 됨
    - 그러면 웹사이트의 내용을 제대로 이해할 수 없고, 검색결과에 잘 노출되지 않음

    - CSR이 SEO에 불리한 이유
      - 검색엔진이 웹사이트를 방문했을 때 콘텐츠가 보이지 않음
      - 검색엔진이 제대로 웹사이트 내용을 색인(indexing)하지 못함
      - 검색결과에서 순위가 낮아짐 (SEO 성능 저하)

  - SSR (Server-Side Rendering, 서버 렌더링)이 SEO에 효과적인 이유
    - 개념: SSR 방식은 웹페이지를 먼저 서버에서 만들어서 사용자에게 보내는 방식
    - 예제
      - 사용자가 www.example.com을 방문하면, 서버가 미리 완성된 HTML 페이지를 만들어 바로 보여줌
    - 이 방식은 검색엔진이 웹사이트를 방문할 때도 똑같이 적용됨
      - 즉, 검색엔진이 방문했을 때, 웹사이트의 모든 내용을 바로 볼 수 있음
    - 그러면 검색엔진이 웹사이트 내용을 제대로 이해하고 색인할 수 있음
    - 검색결과에서 높은 순위에 노출될 가능성이 커짐

    - SSR이 SEO에 효과적인 이유
      - 검색엔진이 웹사이트를 방문하면 이미 완성된 콘텐츠를 확인 가능
      - 검색엔진이 웹사이트를 빠르게 색인(indexing) 할 수 있음
      - 검색결과에서 순위가 높아질 가능성이 커짐 (SEO 성능 향상)

  - SSR이 꼭 필요한 경우
    - 검색엔진 최적화(SEO)가 중요한 블로그, 뉴스 사이트
    - 네이버, 구글 등에서 검색 노출이 중요한 웹사이트
    - 빠른 첫 화면 로딩이 중요한 웹사이트

  - CSR이 더 나은 경우
    - 검색이 필요 없는 내부 관리자 페이지
    - 매우 동적인 인터페이스를 가진 애플리케이션 (예: 채팅앱, 대시보드)
    - SPA (Single Page Application, 단일 페이지 앱)

  - 정리
    - SSR은 검색엔진이 웹사이트를 방문했을 때 이미 완성된 페이지를 제공하여, 검색 결과에서 상위에 노출될 가능성이 커짐
    - CSR은 검색엔진이 웹사이트를 방문했을 때 빈 화면을 보게 되어 검색 순위가 낮아질 수 있음
    - 결론: "검색에 잘 걸리는 웹사이트를 만들고 싶다면 SSR이 필수"
    - (구글, 네이버에서 내 웹사이트가 잘 검색되게 하려면 SSR을 사용해야 함)