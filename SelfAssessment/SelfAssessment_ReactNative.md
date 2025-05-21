# Concepts, Features, Types and Pros and Cons

Organize concepts, features, types and Pros and Cons

## React Native (+HTML, CSS, Javascript, Typescript)

- React Native와 React의 차이점
  - 공통 사항
    - 둘 다 리액트 라이브러리 기반하나 사용 목적과 실행 환경에서의 차이

  - 개념 (React.js / React Native)
    - 설명
      - 웹 애플리케이션 개발을 위한 UI 라이브러리
      - 모바일 앱(Android/iOS) 개발을 위한 프레임워크
    - 실행 환경
      - 브라우저 (Chrome, Firefox 등)
      - 모바일 앱 (Android, iOS)
    - 렌더링 방식
      - HTML + CSS 사용
      - 네이티브 UI 컴포넌트 사용 (View, Text 등)
    - 사용 언어
      - JavaScript, JSX, CSS
      - JavaScript, JSX, 스타일은 React Native 스타일 객체 사용
    - 배포 방식
      - 웹사이트 URL로 접근
      - Android/iOS 앱스토어에 배포

  - 주요 차이점
    - UI 요소 (HTML vs 네이티브 컴포넌트)
      - React는 웹을 위한 HTML 태그(div, span, button, input 등) 을 사용.
      - React Native는 네이티브 모바일 UI 요소(View, Text, Button, ScrollView 등)를 사용.

    - 스타일링 방식 (CSS vs React Native Styles)
      - React에서는 CSS 또는 CSS-in-JS 사용.
      - React Native에서는 StyleSheet API를 사용하여 스타일 적용

    - 네비게이션 방식 (React Router vs React Navigation)
      - React (웹)에서는 react-router-dom을 사용하여 URL 기반 라우팅을 함
      - React Native (모바일)에서는 react-navigation을 사용하여 화면 간 이동을 처리.

  - API 접근 방식
    - React (웹)
      - fetch 또는 axios로 API 호출
      - 브라우저 기반 API 사용 (예: localStorage, sessionStorage, document 등)

    - React Native (모바일)
	    - fetch 또는 axios로 API 호출
      - 네이티브 기능 접근 가능 (카메라, GPS, 센서 등)
        - react-native-camera → 카메라 사용
        - react-native-geolocation → GPS 사용
        - AsyncStorage → 로컬 데이터 저장

  - 사용 목적에 따른 선택
    - 웹사이트 개발: 리액트
    - 모바일 앱 개발: 리액트 네이티브
    - 데스크톱 앱 개발: 리액트 (Electron 사용 가능)
    - 하이브리드 개발 (웹+앱): 리액트 (PWA 가능) / 리액트 네이티브 (크로스플랫폼 앱 가능)

- React Native에서 Navigation을 구현하는 방법
  - React Native에서 Navigation이 필요한 이유
    - 모바일 앱은 여러 개의 화면(Screen)으로 구성되며, 사용자가 화면 간 이동이 필요함
    - 웹과 달리 브라우저 히스토리(window.history)가 없으므로 별도의 내비게이션 라이브러리 필요
    - React Native에서는 react-navigation을 사용하여 네이티브 수준의 내비게이션 기능을 제공

  - React Navigation 라이브러리 사용
    - 가장 많이 사용되는 내비게이션 라이브러리는 react-navigation

  - 설치 명령어
    ```bash
    npm install @react-navigation/native
    npm install react-native-screens react-native-safe-area-context react-native-gesture-handler react-native-reanimated react-native-vector-icons react-native-dev-menu
    npm install @react-navigation/stack
    ```

  - 설치 후 babel.config.js 설정 (react-native-reanimated 활성화)
    ```js
    module.exports = {
      presets: ['module:metro-react-native-babel-preset'],
      plugins: ['react-native-reanimated/plugin'], // 추가
    };
    ```

  - Android에서 MainActivity.java 수정 (제스처 기능 활성화)
    ```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(null);
    }
    ```

  - Stack Navigation (기본적인 화면 이동)
    - Stack Navigation은 화면을 쌓는 형태(스택)로 구성되어 push, pop 방식으로 동작
    - 뒤로가기 버튼이 자동 생성됨 (iOS는 좌측 스와이프, Android는 BackHandler)
    - 예제: Stack Navigation 구현
      ```jsx
      import React from 'react';
      import { View, Text, Button } from 'react-native';
      import { createStackNavigator } from '@react-navigation/stack';
      import { NavigationContainer } from '@react-navigation/native';

      // 홈 화면
      const HomeScreen = ({ navigation }) => {
        return (
          <View>
            <Text>Home Screen</Text>
            <Button title="Go to Details" onPress={() => navigation.navigate('Details', { itemId: 42 })} />
          </View>
        );
      };

      // 상세 화면
      const DetailsScreen = ({ route, navigation }) => {
        const { itemId } = route.params;
        return (
          <View>
            <Text>Details Screen - Item ID: {itemId}</Text>
            <Button title="Go Back" onPress={() => navigation.goBack()} />
          </View>
        );
      };

      // Stack Navigator 생성
      const Stack = createStackNavigator();

      export default function App() {
        return (
          <NavigationContainer>
            <Stack.Navigator>
              <Stack.Screen name="Home" component={HomeScreen} />
              <Stack.Screen name="Details" component={DetailsScreen} />
            </Stack.Navigator>
          </NavigationContainer>
        );
      }
      ```
    - 설명
	    - Stack.Navigator로 화면 이동을 관리
	      - navigation.navigate('Details', { itemId: 42 })로 파라미터 전달 가능
	      - navigation.goBack()으로 이전 화면으로 돌아감

  - Tab Navigation (하단 탭 내비게이션)
    - 개요
      - 하단 탭 메뉴를 사용하여 화면 전환하는 방식
      - 일반적으로 createBottomTabNavigator를 사용

    - 설치
      - npm install @react-navigation/bottom-tabs
      - npm install react-native-vector-icons

    - 예제: Bottom Tab Navigation 구현
      ```jsx
      import React from 'react';
      import { View, Text } from 'react-native';
      import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
      import { NavigationContainer } from '@react-navigation/native';
      import Icon from 'react-native-vector-icons/Ionicons';

      const HomeScreen = () => (
        <View>
          <Text>Home Screen</Text>
        </View>
      );

      const ProfileScreen = () => (
        <View>
          <Text>Profile Screen</Text>
        </View>
      );

      // Tab Navigator 생성
      const Tab = createBottomTabNavigator();

      export default function App() {
        return (
          <NavigationContainer>
            <Tab.Navigator
              screenOptions={({ route }) => ({
                tabBarIcon: ({ color, size }) => {
                  let iconName = route.name === 'Home' ? 'home-outline' : 'person-outline';
                  return <Icon name={iconName} size={size} color={color} />;
                },
              })}
            >
              <Tab.Screen name="Home" component={HomeScreen} />
              <Tab.Screen name="Profile" component={ProfileScreen} />
            </Tab.Navigator>
          </NavigationContainer>
        );
      }
      ```

    - 설명
	    - createBottomTabNavigator()를 사용하여 하단 탭 내비게이션 구현.
	    - tabBarIcon을 사용하여 아이콘 추가 (react-native-vector-icons 필요).

  - Drawer Navigation (사이드 메뉴)
    - 개요
      - 왼쪽에서 밀어서 나오는 드로어(햄버거 메뉴) 내비게이션
      - 대부분의 Android 앱에서 사용되며, React Navigation에서 지원

    - 설치
      - npm install @react-navigation/drawer

    - 예제: Drawer Navigation 구현
      ```jsx
      import React from 'react';
      import { View, Text } from 'react-native';
      import { createDrawerNavigator } from '@react-navigation/drawer';
      import { NavigationContainer } from '@react-navigation/native';

      const HomeScreen = () => (
        <View>
          <Text>Home Screen</Text>
        </View>
      );

      const SettingsScreen = () => (
        <View>
          <Text>Settings Screen</Text>
        </View>
      );

      // Drawer Navigator 생성
      const Drawer = createDrawerNavigator();

      export default function App() {
        return (
          <NavigationContainer>
            <Drawer.Navigator initialRouteName="Home">
              <Drawer.Screen name="Home" component={HomeScreen} />
              <Drawer.Screen name="Settings" component={SettingsScreen} />
            </Drawer.Navigator>
          </NavigationContainer>
        );
      }
      ```
    - 설명
	    - createDrawerNavigator()를 사용하여 왼쪽에서 나오는 사이드 메뉴(햄버거 메뉴) 구현.

  - Stack, Tab, Drawer 조합하여 사용하기
    - 개요
      - 여러 개의 내비게이션을 조합하여 사용 가능
      - 예제: Stack + Tab Navigation 혼합
        ```jsx
        import React from 'react';
        import { View, Text } from 'react-native';
        import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
        import { createStackNavigator } from '@react-navigation/stack';
        import { NavigationContainer } from '@react-navigation/native';

        // Home Screen
        const HomeScreen = ({ navigation }) => (
          <View>
            <Text>Home Screen</Text>
            <Button title="Go to Details" onPress={() => navigation.navigate('Details')} />
          </View>
        );

        // Details Screen (Stack)
        const DetailsScreen = () => (
          <View>
            <Text>Details Screen</Text>
          </View>
        );

        // Profile Screen (Tab)
        const ProfileScreen = () => (
          <View>
            <Text>Profile Screen</Text>
          </View>
        );

        // Stack Navigator (Home + Details)
        const Stack = createStackNavigator();
        const HomeStack = () => (
          <Stack.Navigator>
            <Stack.Screen name="Home" component={HomeScreen} />
            <Stack.Screen name="Details" component={DetailsScreen} />
          </Stack.Navigator>
        );

        // Bottom Tab Navigator
        const Tab = createBottomTabNavigator();
        export default function App() {
          return (
            <NavigationContainer>
              <Tab.Navigator>
                <Tab.Screen name="HomeStack" component={HomeStack} />
                <Tab.Screen name="Profile" component={ProfileScreen} />
              </Tab.Navigator>
            </NavigationContainer>
          );
        }
        ```
      - 설명
	      - HomeStack을 만들어 Stack Navigation(Home, Details) + Tab Navigation(Profile) 조합

- React Native에서 상태 관리 방법
  - (1) 기본 방식
    - useState: 컴포넌트 내부의 간단한 상태를 관리할 때 사용.
    - useReducer: 상태 업데이트 로직이 복잡하거나 상태 객체가 클 경우 사용.

  - (2) 전역 상태 관리
    - Context API: 간단한 전역 상태 공유에 적합. 그러나 상태가 커지면 성능 저하 가능.

    - Redux: 가장 보편적인 전역 상태 관리 라이브러리. 액션, 리듀서, 스토어 개념을 기반으로 한다. (액션 > 리듀서 > 스토어)

    - MobX: 관찰 가능한 상태를 기반으로 자동 반응. 코드가 간결하지만 학습 곡선이 존재할 수 있음.

    - Zustand, Recoil, Jotai: 최근 각광받는 간단하고 직관적인 상태 관리 라이브러리.

    - React Query / SWR: 서버 상태(data fetching, caching) 관리를 위한 라이브러리.

    - 실무에서는 Context + useReducer 또는 Redux Toolkit, Zustand 조합이 많이 사용됨.

- React Native에서 AsyncStorage의 역할
  - AsyncStorage 역할
    - 로컬 비동기 키-값 저장소 역할.
    - 브라우저의 LocalStorage와 비슷하지만 비동기적으로 동작.
    - 앱을 종료해도 데이터가 유지됨 (영구 저장).
    - 주로 사용하는 용도:
      - 로그인 토큰 저장
      - 간단한 설정값 캐싱
      - 사용자 정보 저장 등

    - @react-native-async-storage/async-storage 패키지를 사용함.

  - 예시
    ```ts
    // 예시
    import AsyncStorage from '@react-native-async-storage/async-storage';

    await AsyncStorage.setItem('token', 'abc123');
    const token = await AsyncStorage.getItem('token');
    ```
- React Native에서 Reanimated
  - Reanimated 개념
    - 고성능 애니메이션 라이브러리.
    - react-native-reanimated는 JavaScript 스레드가 아닌 UI 스레드에서 직접 실행되어 더 부드럽고 끊김 없는 애니메이션을 제공.
    - Gesture Handler와 함께 자주 사용되며, 복잡한 제스처 및 애니메이션에 적합.
    - v2부터는 worklet과 shared value를 사용하여 선언형 스타일로 애니메이션을 정의함.
    - 기존의 Animated API 보다 성능, 자연스러움, 유연성 면에서 훨씬 우수

  - 예시
    ```ts
    import { useSharedValue, withSpring, useAnimatedStyle } from 'react-native-reanimated';

    const offset = useSharedValue(0);

    const animatedStyle = useAnimatedStyle(() => ({
      transform: [{ translateX: offset.value }],
    }));

    offset.value = withSpring(100);  // 부드러운 애니메이션 이동
    ```

- React Native에서 Native Module
  - 개념
    - React Native(JavaScript)에서 Android(Java/Kotlin), iOS(Objective-C/Swift) 네이티브 기능을 호출하기 위한 브리지 모듈.
    - 예: 카메라, Bluetooth, 암호화, 생체인식 등 JS로 직접 제어할 수 없는 네이티브 기능을 사용할 때.

  - 특징
    - JavaScript ↔ Native 사이 양방향 통신 가능.
    - Android: @ReactMethod로 메서드 노출
    - iOS: RCT_EXPORT_METHOD 또는 Swift에서 @objc 사용

  - 예시
    - Android: MyNativeModule.java
    - JavaScript: NativeModules.MyNativeModule.doSomething()

- React Native에서 Expo와 Bare Workflow의 차이점
  - 차이점
    - Expo
      - 빠른 개발, 설정 최소화
      - 네이티브 코드 수정 불가능, Expo CLI 사용
      - 앱 크기는 상대적으로 증가
      - MVP, 빠른 프로토타입 필요 시 사용
    - Bare Workflow
      - 커스터마이징, 네이티브 기능 통합
      - 네이티브 코드 수정 가능
      - Xcode / Android Studio 사용한 빌드 방식
      - 앱 크기 최적화 가능
      - 고급 앱, 복잡한 기능 필요한 경우 사용
  
  - 참고
    - Expo도 EAS Build와 Custom Dev Client 도입으로 점점 유연해지고 있음

- React Native에서 성능 최적화 방법
  - JS 측 최적화
    - FlatList의 keyExtractor, initialNumToRender, windowSize 설정
    - useMemo, useCallback으로 불필요한 리렌더링 방지
    - React.memo / PureComponent로 컴포넌트 최적화
    - VirtualizedList, SectionList 적극 활용

  - 네이티브 성능 최적화
    - Image 로딩 최적화 (예: FastImage)
    - UI 애니메이션: Reanimated, Gesture Handler 사용
    - JS Thread와 UI Thread 분리
    - WebView, 지도, 영상 등은 가능한 네이티브 모듈로 대체

  - 기타
    - 앱 초기화 속도 개선 (Splash Screen 등)
    - 무거운 연산은 Web Worker / Background Thread로 분리

- React Native에서 useEffect의 메모리 누수를 방지하는 방법은?

- React Native에서 Gesture Handling을 구현하는 방법은?
- React Native에서 push notification을 설정하는 방법은?
- React Native에서 App State를 관리하는 방법은?
- React Native에서 Hot Reloading과 Fast Refresh의 차이점은?
- React Native에서 Dynamic Linking이란?
- React Native에서 Code Splitting이 필요한 이유는?
- React Native에서 Flipper를 사용하는 이유는?
- React Native의 Metro Bundler와 Webpack의 차이점은?
- React Native에서 Hermes 엔진을 사용하는 장점은?
- React Native에서 SafeAreaView의 역할은?
- React Native에서 Dynamic Styles을 적용하는 방법은?
- React Native에서 Performance Profiling을 수행하는 방법은?
- React Native에서 Detox와 Appium의 차이점은?
- React Native에서 Firebase를 연동하는 방법은?
- React Native에서 Clipboard API를 사용하는 방법은?
- React Native에서 StatusBar를 동적으로 변경하는 방법은?
- React Native에서 Redux Toolkit을 사용하는 이유는?
- React Native에서 AsyncStorage와 SecureStore의 차이점은?
- React Native에서 React Navigation과 React Router의 차이점은?
- React Native에서 ScrollView와 FlatList의 차이점은?
- React Native에서 Dynamic Styles을 적용하는 방법은?
- React Native에서 Performance Profiling을 수행하는 방법은?
- React Native에서 Detox와 Appium의 차이점은?
- React Native에서 Firebase를 연동하는 방법은?
- React Native에서 Clipboard API를 사용하는 방법은?
- React Native에서 StatusBar를 동적으로 변경하는 방법은?
- React Native에서 Native Module을 직접 구현하는 방법은?
- React Native에서 Gesture Handler를 설정하는 방법은?
- React Native에서 Hermes의 주요 기능은?
- React Native에서 Expo를 사용할 때의 장단점은?
- React Native에서 Animated API를 활용한 애니메이션 구현 방법은?
- React Native에서 Deep Linking을 적용하는 방법은?
- React Native에서 AppState를 활용하는 방법은?
- React Native에서 SafeAreaView의 역할은?
- React Native에서 CodePush를 활용하여 앱을 배포하는 방법은?
- React Native에서 Splash Screen을 최적화하는 방법은?
- React Native에서 Background Task를 실행하는 방법은?
- React Native에서 WebSockets을 사용하는 방법은?
- React Native에서 Fast Refresh가 동작하는 방식은?
- React Native에서 TurboModules의 역할은?
- React Native에서 Flipper 디버깅 툴을 활용하는 방법은?
- React Native에서 Accessibility를 개선하는 방법은?
- React Native에서 Gesture Responder System이 동작하는 방식은?
- React Native에서 Firebase Firestore와 Realtime Database의 차이점은?
- React Native에서 Camera 기능을 구현하는 방법은?
- React Native에서 Dark Mode를 적용하는 방법은?
- React Native에서 Multi-Threading을 구현하는 방법은?
- React Native에서 React Query를 사용하는 이유는?
- React Native에서 WebView를 활용하는 방법은?
- React Native에서 Reanimated 라이브러리를 사용하는 방법은?
- React Native에서 Lottie를 활용한 애니메이션을 적용하는 방법은?
- React Native에서 Google Maps를 적용하는 방법은?
- React Native에서 Video Streaming을 구현하는 방법은?
- React Native에서 Native Bridge를 사용하는 이유는?
- React Native에서 Native Event Emitter의 역할은?
- React Native에서 터치 이벤트를 처리하는 방법은?
- React Native에서 Push Notification을 설정하는 방법은?
- React Native에서 Apple Pay와 Google Pay를 연동하는 방법은?
- React Native에서 환경 변수(.env) 파일을 사용하는 방법은?
- React Native에서 EAS(Expo Application Services)를 활용하는 방법은?
- React Native에서 앱 크기를 최적화하는 방법은?
- React Native에서 서버와의 실시간 동기화를 구현하는 방법은?
- React Native에서 File Upload 기능을 구현하는 방법은?
- React Native에서 Custom Fonts를 적용하는 방법은?
- React Native에서 Local Authentication(지문, 얼굴 인식)을 적용하는 방법은?
- React Native에서 Dynamic Linking이란 무엇인가?
- React Native에서 Third-Party 모듈을 효과적으로 관리하는 방법은?
- React Native에서 Multi-Platform을 위한 코드 구조화 방법은?
- React Native에서 MobX와 Redux의 차이점은?
- React Native에서 Accessibility를 최적화하는 방법은?
- React Native에서 WebView와 iframe의 차이점은?
- React Native에서 배터리 소모를 줄이기 위한 방법은?
- React Native에서 Bluetooth 기능을 구현하는 방법은?
- React Native에서 Offline Mode를 구현하는 방법은?
- React Native에서 앱에서 로그를 수집하는 방법은?
- React Native에서 AI 모델을 활용하는 방법은?
- React Native에서 Face Recognition을 적용하는 방법은?
- React Native에서 AsyncStorage의 대체 기술은?
- React Native에서 JWT 인증을 구현하는 방법은?
- React Native에서 Background Fetch를 활용하는 방법은?
- React Native에서 GraphQL을 활용한 데이터 관리 방법은?
- React Native에서 프로젝트 구조를 설계할 때 고려해야 할 사항은?
- React Native에서 백그라운드에서 앱이 실행되도록 유지하는 방법은?
- React Native에서 앱이 종료되었을 때도 알림을 받을 수 있도록 하는 방법은?
- React Native에서 CI/CD를 구축하는 방법은?
- React Native에서 Redux를 사용할 때 발생할 수 있는 문제점과 해결 방법은?
- React Native에서 Splash Screen이 오래 걸리는 문제를 해결하는 방법은?
- React Native에서 앱 로딩 속도를 개선하는 방법은?
- React Native에서 Expo에서 Bare Workflow로 마이그레이션하는 방법은?
- React Native에서 CI/CD 파이프라인을 구축하는 방법은?
- React Native에서 Custom Hooks를 효과적으로 활용하는 방법은?
- React Native에서 앱 실행 중 동적 모듈 로딩을 수행하는 방법은?
- React Native에서 Global State 관리를 위한 최적의 방법은?
- React Native에서 Navigation 상태를 동적으로 관리하는 방법은?
- React Native에서 AI 기반 음성 인식 기능을 추가하는 방법은?
- React Native에서 Flutter와 비교했을 때의 장점은?
- React Native에서 Expo Managed Workflow와 Bare Workflow의 차이점은?
- React Native에서 Google Sign-In을 적용하는 방법은?
- React Native에서 WebRTC를 활용한 영상 통화를 구현하는 방법은?
- React Native에서 프로젝트를 TypeScript로 마이그레이션하는 방법은?
- React Native에서 UI 성능을 개선하는 방법은?
- React Native에서 FlatList의 성능 최적화를 위해 고려해야 할 점은?
- React Native에서 AsyncStorage의 데이터를 암호화하는 방법은?
- React Native에서 프로젝트에서 코드 스플리팅을 적용하는 방법은?
- React Native에서 Internationalization(다국어 지원)을 구현하는 방법은?
- React Native에서 앱을 A/B 테스트하는 방법은?
- React Native에서 In-App Purchase를 구현하는 방법은?
- React Native에서 Expo Go를 활용하는 방법은?
- React Native에서 Apple의 App Tracking Transparency(ATT)를 적용하는 방법은?
- React Native에서 UI/UX를 개선하는 방법은?
- React Native에서 GPU 성능 최적화를 수행하는 방법은?
- React Native에서 Security Vulnerability를 해결하는 방법은?
- React Native에서 Context API를 Redux 대체제로 사용하는 방법은?
- React Native에서 Navigation Stack을 효율적으로 관리하는 방법은?
- React Native에서 Native Code와의 통신을 최적화하는 방법은?
- React Native에서 Jetpack Compose와의 연동 방법은?
- React Native에서 JSI(JavaScript Interface)의 역할과 활용 방법은?
- React Native에서 Fabric Renderer의 개념과 기존 Bridge와의 차이점은?
- React Native에서 TurboModules의 동작 원리와 성능 개선 방법은?
- React Native에서 Hermes 엔진을 사용하는 이유는?
- React Native와 Native 개발의 차이점은 무엇인가요?
- React Native에서의 성능 최적화 방법을 설명해주세요.
- React Native의 Bridge와 TurboModules에 대해 설명해주세요.
- React Native의 Hermes 엔진 사용 경험을 설명해주세요.
- React Native의 JSI(JavaScript Interface)와 Fabric 아키텍처에 대해 설명해주세요.
- React Native에서 Fabric과 기존 렌더링 방식의 차이점은?
- React Native에서 Metro Bundler와 Webpack의 차이점은?
- React Native에서 Gesture Handler를 최적화하는 방법은?
- React Native에서 Dynamic Code Push를 적용하는 방법은?
- React Native에서 Hermes 엔진을 사용할 때의 장점은?
- React Native에서 Accessibility를 최적화하는 방법은?
- React Native에서 Custom Native Module을 작성하는 방법은?
- React Native와 Flutter의 차이점은?
- React Native에서 native module을 추가하는 방법은?
- React Native에서 성능 최적화를 위해 어떤 기법을 적용하는가?
- React Native의 useEffect가 componentDidMount와 componentWillUnmount와 어떻게 비교되는가?
- React Native에서 AsyncStorage와 SecureStore의 차이는?
- React Native에서 Animation을 구현하는 방법은?
- React Native에서 네이티브 코드(Android, iOS)와 연동하는 방법은?
- React Native에서 TurboModules와 Fabric의 개념을 설명하라.
- React Native에서 JSC와 Hermes 엔진의 차이는?
- React Native의 Flipper 디버깅 도구를 활용하는 방법은?
- React Native에서 네이티브 모듈을 직접 구현할 때 주의해야 할 사항은?
- React Native의 Bridge 통신 방식과 성능 최적화 기법은?
- React Native의 기본 개념 및 차이점
- React Native에서 Virtual DOM이 어떻게 작동하는가?
- React Native의 JSX와 HTML의 차이점은?
- React Native의 View, Text, Image와 같은 기본 컴포넌트는 어떻게 동작하는가?
- React Native에서 DOM이 없는 환경에서 스타일을 어떻게 적용하는가?
- React Native에서 CSS 대신 StyleSheet.create를 사용하는 이유는?
- React와 React Native에서 onClick과 onPress 이벤트의 차이점은?
- React Native에서 iOS와 Android의 네이티브 코드 차이를 어떻게 다루는가?
- React Native에서 상태 관리를 위한 다양한 방법(Redux, Recoil, Zustand, MobX 등)을 비교해보세요.
- React Native에서 Context API와 Redux를 비교하고, 언제 Context API를 사용할지 설명하세요.
- React Native에서 useReducer를 상태 관리에 활용하는 방법은?
- React Native에서 상태 관리를 최적화하는 방법은? (e.g., 불필요한 리렌더링 방지)
- React Native에서 React.memo와 useMemo의 차이점과 사용 사례는?
- React Native에서 React Query와 SWR을 사용할 때의 차이점은?
- React Native에서 fetch API와 Axios의 차이점은?
- React Native에서 WebSocket과 HTTP Polling의 차이점은?
- React Native에서 GraphQL을 활용하는 방법은?
- React Native에서 API 호출을 최적화하는 방법은? (e.g., 캐싱, 중복 요청 방지)
- React Native에서 Background Fetch와 Foreground Fetch의 차이는?
- React Native에서 Long Polling을 구현하는 방법은?
- React Native에서 메모리 누수를 방지하는 방법은?
- React Native에서 Lazy Loading을 적용하는 방법은?
- React Native에서 앱 크기를 줄이는 방법은?
- React Native에서 FlatList의 getItemLayout을 활용하는 방법은?
- React Native에서 Animated API와 Reanimated의 차이점은?
- React Native에서 Fast Refresh가 어떻게 동작하는가?
- React Native에서 Hermes를 사용할 때 성능 이점은?
- React Native에서 Metro Bundler의 역할과 최적화 방법은?
- React Native에서 JavaScript 코드와 네이티브 코드가 어떻게 통신하는가?
- React Native에서 Custom Native Module을 구현하는 방법은?
- React Native에서 TurboModules와 기존 Native Module의 차이점은?
- React Native에서 Fabric Renderer가 기존 브릿지 방식과 어떻게 다른가?
- React Native에서 Native Event Emitter를 활용하는 이유는?
- React Native에서 Bluetooth 통신을 구현하는 방법은?
- React Native에서 react-native link와 autolinking의 차이점은?
- React Native에서 OAuth를 구현하는 방법은?
- React Native에서 JWT 토큰을 안전하게 저장하는 방법은?
- React Native에서 SecureStore와 AsyncStorage의 차이점은?
- React Native에서 Code Injection을 방지하는 방법은?
- React Native에서 App Transport Security (ATS)를 활성화하는 방법은?
- React Native에서 WebView 보안을 강화하는 방법은?
- React Native에서 Unit Test와 E2E Test를 수행하는 방법은?
- React Native에서 Jest와 Detox의 차이점은?
- React Native에서 CodePush를 활용하여 앱을 업데이트하는 방법은?
- React Native에서 App Store와 Google Play 배포 프로세스를 설명하세요.
- React Native에서 CI/CD 파이프라인을 구축하는 방법은?
- React Native에서 Firebase Test Lab을 활용하는 방법은?
- React Native에서 크래시 리포팅을 설정하는 방법은?
- React Native에서 SQLite와 Realm의 차이점은?
- React Native에서 AsyncStorage 대신 사용할 수 있는 데이터 저장 방법은?
- React Native에서 데이터를 암호화하는 방법은?
- React Native에서 실시간 동기화를 구현하는 방법은? (Firebase, WebSockets 등)
- React Native에서 Redux Persist와 MMKV의 차이점은?
- React Native에서 Apollo Client를 사용할 때의 장점은?
- React Native에서 i18n(다국어 지원)을 구현하는 방법은?
- React Native에서 Dynamic Font Scaling을 적용하는 방법은?
- React Native에서 Accessibility(접근성)를 강화하는 방법은?
- React Native에서 RTL (Right-to-Left) 언어를 지원하는 방법은?
- React Native에서 카메라와 갤러리를 사용하는 방법은?
- React Native에서 Face ID와 Touch ID를 적용하는 방법은?
- React Native에서 NFC 기능을 구현하는 방법은?
- React Native에서 GPS 및 위치 기반 서비스를 구현하는 방법은?
- React Native에서 AR(Augmented Reality) 기능을 적용하는 방법은?
- React Native에서 머신러닝 모델을 활용하는 방법은? (TensorFlow.js, ML Kit 등)
- React Native의 최신 트렌드 및 업데이트된 기능은 무엇인가?
- React Native에서 New Architecture(Fabric & TurboModules)를 적용하는 방법은?
- React Native와 Flutter를 비교할 때, React Native의 강점과 약점은?
- React Native의 JSI(JavaScript Interface)는 무엇이며, 어떻게 동작하는가?
- React Native에서 Expo Router를 사용하면 어떤 장점이 있는가?
- React Native에서 새로운 패키지를 선택할 때 고려해야 할 점은?