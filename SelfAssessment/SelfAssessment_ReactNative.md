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

- React Native에서 useEffect의 메모리 누수를 방지하는 방법
  - 문제가 되는 경우
    - useEffect 내부에서 비동기 작업(fetch, timer, event listener 등)을 시작하고 컴포넌트 언마운트 시 정리(clean-up)를 안 하면 메모리 누수 발생.

  - 해결 방법: return을 사용한 정리
    ```ts
    useEffect(() => {
      const subscription = eventEmitter.addListener('someEvent', handler);

      return () => {
        // cleanup
        subscription.remove();
      };
    }, []);
    ```
    
  - 비동기 처리 시 주의
    - 비동기 작업 취소, listener 제거, timer clear 등이 핵심.
    ```ts
    useEffect(() => {
      let isMounted = true;

      const fetchData = async () => {
        const data = await fetch(...);
        if (isMounted) {
          setState(data);
        }
      };

      fetchData();

      return () => {
        isMounted = false;
      };
    }, []);
    ```

- React Native에서 Gesture Handling을 구현하는 방법
  - 기본 방법
    - TouchableOpacity, TouchableHighlight, TouchableWithoutFeedback 등의 기본 제공 컴포넌트 사용

  - 고급 제스처: react-native-gesture-handler
    - 스와이프, 드래그, 핀치 등 고성능 제스처 구현에 사용
    - 네이티브에서 제스처를 처리하므로 부드럽고 안정적

  - 예시
    ```bash
    npm install react-native-gesture-handler
    ```
    ```tsx
    import { GestureHandlerRootView, PanGestureHandler } from 'react-native-gesture-handler';

    <GestureHandlerRootView>
      <PanGestureHandler onGestureEvent={onPan}>
        <Animated.View>{/* 움직일 컴포넌트 */}</Animated.View>
      </PanGestureHandler>
    </GestureHandlerRootView>
    ```
    - Reanimated와 함께 사용하면 애니메이션도 자연스럽게 처리 가능

- React Native에서 push notification을 설정하는 방법
  - 대표 라이브러리: react-native-firebase/messaging
    - Android와 iOS 모두 FCM(Firebase Cloud Messaging) 기반
      ```bash
      npm install @react-native-firebase/app @react-native-firebase/messaging
      ```

  - 설정 절차 요약
    - Firebase 콘솔 프로젝트 생성 및 앱 등록
    - google-services.json (Android), GoogleService-Info.plist (iOS) 추가
    - 권한 요청: requestPermission()
    - 디바이스 토큰 등록: getToken()
    - 백그라운드/포그라운드/종료 상태별 수신 처리
      ```ts
      messaging().onMessage(async remoteMessage => {
        Alert.alert('알림', remoteMessage.notification?.title ?? '');
      });
      ```
      -  iOS의 경우 APNs 설정 필요 (개발자 계정, 인증서 필수)

- React Native에서 App State를 관리하는 방법
  - AppState API
    - 앱의 현재 상태 감지 가능: active, background, inactive
  
  - 예시
    ```ts
    import { AppState } from 'react-native';

    useEffect(() => {
      const subscription = AppState.addEventListener('change', nextState => {
        console.log('AppState:', nextState);
      });

      return () => subscription.remove();
    }, []);
    ```

  - 주요 활용
    - 앱이 background로 갔을 때 리소스 정리
    - foreground로 복귀할 때 데이터 갱신
    - 세션 유지, 타이머 관리 등

- React Native에서 Hot Reloading과 Fast Refresh의 차이점
  - Hot Reloading (구버전)
    - 작동방식: 상태(state)를 유지한 채 JS 변경 적용
    - 신뢰성: 불안정 (종종 작동 안 함)
    - 상태 유지: 가능하나 불완전함
    - 변경 적용 범위: 전체 파일 감지 기준
    
  - Fast Refresh (현재 기본)
    - 작동방식: 자동으로 안전하게 컴포넌트만 다시 로딩
    - 신뢰성: 매우 안정적
    - 상태 유지: 대부분의 경우 상태 유지 가능
    - 변경 적용 범위: 변경된 모듈만 리프레시

  - Fast Refresh는 React Native 0.61 이후 기본 활성화된 기능이며 Hot Reloading은 더 이상 권장되지 않음

- 서버에서 실시간 영상 데이터를 앱으로 전송하는 방식 (영상의 특성과 요구사항에 따라 여러가지 방식 존재)
  - HLS (HTTP Live Streaming)
    - 원리: 서버에서 영상을 .ts 단위로 잘라서 보내고, .m3u8 인덱스 파일로 클라이언트가 재생.
    - 장점: CDN 캐시, 유튜브/넷플릭스 등 대규모 서비스에서 많이 사용. 네이티브 지원도 좋음.
    - 단점: 몇 초 단위의 지연(2~10초). 초저지연 필요 시 부적절.
    - 리액트 네이티브 사용법:
      - react-native-video 라이브러리 사용 가능.
      - iOS는 AVPlayer, Android는 ExoPlayer로 HLS 지원.

  - RTMP (Real-Time Messaging Protocol)
    - 원리: TCP 기반의 Adobe Flash Video 전송 프로토콜.
    - 장점: 낮은 지연 시간(1~2초), 설정 쉬움.
    - 단점: 모바일에서 직접 지원 어려움, React Native에서 직접 재생 불가. 중간 서버 필요 (예: HLS 변환).
    - 활용법:
      - 서버에서 RTMP 수신 → 변환 서버(Nginx-RTMP 등) → HLS로 변환 → 앱에서 재생.

  - WebRTC (Web Real-Time Communication)
    - 원리: P2P 기반 초저지연 스트리밍. 양방향 음성/영상 통신에 최적.
    - 장점: 초저지연(<0.5초), 양방향 지원, 실시간 회의/영상통화 등에 적합.
    - 단점: 모바일에서 구현 복잡. React Native에서 직접 구현하려면 네이티브 브리징 필요.
    - 사용법:
      - react-native-webrtc 사용 가능 (네이티브 코드 연동 필요).
      - 서버는 SFU (예: Janus, Mediasoup, Kurento) 필요.

  - MJPEG (Motion JPEG)
    - 원리: JPEG 이미지를 계속 전송하며 실시간처럼 보여줌.
    - 장점: 구현 매우 간단. 단순 카메라 모니터링 등에 사용.
    - 단점: 압축률 낮고 고화질 영상에는 부적합.
    - 리액트 네이티브에서 처리:
      - <Image> 태그로 스트림 주소를 주기적으로 갱신하거나 웹뷰로 표시.

  - WebSocket + Binary Streaming
    - 원리: WebSocket으로 영상을 바이너리로 직접 전송 (예: mp4 fragment, H264 frame).
    - 장점: 커스터마이징 유연, 비표준 상황에 사용 가능.
    - 단점: 앱 단에서 디코딩 직접 구현 필요, 복잡.
    - 적용 예:
      - 서버에서 H264 raw frame 전송 → 앱에서 ffmpeg wasm 또는 native decoder 연동하여 디코딩.

  - 실무에서는 어떤 방식을 쓰나?
    - HLS: 라이브 방송처럼 수천명이 시청하는 상황, 또는 녹화/재생 겸용.

    - WebRTC: 실시간 모니터링, 원격 제어, 통신, 회의 등 초저지연이 필수일 때.

    - RTMP → HLS: 방송 서버에서 영상 받아 앱에 보여줄 때 (중간에 변환 필요).

    - MJPEG: 저비용 저성능 IoT 카메라 모니터링 등에 사용.

  - 정리
    - 실시간성 가장 중요 (<1초): WebRTC
    - 일정 지연 허용 가능, 쉬운 구현: HLS
    - 서버에서 RTMS로 송출 중: RTMS -> HLS
      - RealTime Messaging Protocol, HTTP Live Streaming
    - 간단한 IP 카메라 뷰어: MJPEG
    - 완전 커스텀 스트리밍 필요 -> WebSocket + Binary

- CDN (Content Delivery Network)
  - 개념
    - 전 세계 여러 위치에 분산된 서버 네트워크를 통해 사용자에게 콘텐츠 (예: 영상, 이미지, JS, HTML 등)를 가까운 서버에서 빠르게 제공하는 기술 (가까운 서버에서 빠르게 제공이 핵심)

  - 목적:
    - 사용자에게 빠른 응답 속도 제공 (가까우니까)
    - 서버 부하 분산
    - 전송 지연(latency) 최소화
    - 대용량 트래픽 대응

  - 동작 구조:
    - 사용자가 https://example.com/video.m3u8 요청
    - CDN 네트워크는 사용자의 지역에 가장 가까운 엣지 서버(Edge Server)로 요청을 라우팅
    - 엣지 서버에 캐시가 있으면 바로 응답
    - 없으면 오리진(Origin, 원본 서버)에서 받아오고 캐시에 저장 후 응답

- CDN 캐시 개념
  - 개념
    - CDN의 엣지 서버(지역 분산 서버)에 임시 저장된 콘텐츠 의미

  - 왜 사용하는가?
    - 오리진 서버 요청을 줄여 트래픽 비용 절감
    - 응답 시간 단축 (캐시된 콘텐츠는 즉시 제공)
    - 글로벌 서비스에서 지연 최소화

  - 예:
    - .m3u8, .ts 파일, 이미지, JS, CSS 등 정적 콘텐츠가 주로 캐싱됨
    - 캐시 정책은 TTL(Time-To-Live), 헤더 기반으로 설정 가능

- MJPEG 스트리밍과 주기적 주소 갱신
  - MJPEG 방식 개념
    - http://camera-ip/mjpeg-stream 과 같은 URL로 접속하면,
    - JPEG 이미지들이 multipart/x-mixed-replace 형태로 연속 전송됨
    - 영상처럼 보이지만 실제로는 "이미지 슬라이드쇼"임

  - React Native에서 MJPEG 갱신 베스트 프랙티스
    - WebView 사용
      - 가장 간단한 방식 (내장 브라우저로 MJPEG URL 스트리밍)
      - 단점: 늘 그렇듯이 웹뷰는 네이티브 제어 어려움, 렌더링 퍼포먼스 떨어질 수 있음
      - 예시
        ```tsx
        <WebView
          source={{ uri: 'http://camera-ip/mjpeg-stream' }}
          allowsInlineMediaPlayback
          javaScriptEnabled
          domStorageEnabled
          style={{ width: '100%', height: 300 }}
        />
        ```

    - Image 컴포넌트 + 주기적 리프레시
      - 장점: 간단, 이미지 캐싱 방지를 위해 timestamp 파라미터로 URL 매번 변경
      - 단점: 진짜 영상처럼 부드럽진 않음
      ```tsx
      const [imageUrl, setImageUrl] = useState('');
      useEffect(() => {
        const interval = setInterval(() => {
          setImageUrl(`http://camera-ip/snapshot.jpg?t=${Date.now()}`);
        }, 200); // 200ms 마다 새로고침
        return () => clearInterval(interval);
      }, []);
      ```

  - 베스트 프랙티스
    - WebView: MJPEG 스트림을 브라우저처럼 로드, 구현 간단, 성능 낮음, 제어 어려움
    - Image + setInterval: snapshot.jpg를 주기적으로 로딩, 제어 쉬우나 부드럽지 않음
    - native module (추천): Android/iOS MJPEG Decoder 활용, 최적의 성능, 직접 구현/연동작업 필요

- 이미지 캐싱 방지를 위한 timestamp 파라미터 추가 건 설명
  - 개요
    - 브라우저(또는 네이티브 이미지 로더)의 캐시 메커니즘을 우회하기 위한 트릭

  - TimeStamp 붙이는 이유
    - 브라우저나 네이티브 이미지 로더는 같은 URL의 이미지는 캐시에 저장하고, 다시 로딩하지 않으려는 성질 존재
    - 즉, http://camera-ip/snapshot.jpg를 반복해서 불러도 한 번 로딩한 이미지를 계속 보여줄 수 있음

  - 해결 방법
    - 매번 URL이 달라지기 때문에
    - 새로운 리소스로 인식되어 항상 서버에서 최신 이미지를 가져오게 됨
    ```tsx
    `http://camera-ip/snapshot.jpg?t=${Date.now()}`
    ```

- 멀티파트 (Muitipart)
  - 개념
    - multipart는 HTTP 요청/응답에서 여러 개의 데이터를 하나의 메시지에 포함시켜 전송할 수 있도록 하는 콘텐츠 타입(Content-Type)

  - 주요 Content-Type 종류
    - multipart/form-data: HTML <form> 전송 시 사용. 파일 업로드에 사용됨
    - multipart/related: 데이터 간 관계가 있을 때 (예: HTML + 이미지)
    - multipart/mixed: 독립적인 데이터 묶음
    - multipart/x-mixed-replace: 특수한 타입. 데이터를 지속적으로 교체하며 전송 (스트리밍에 사용됨)

- multipart/x-mixed-replace 개념
  - 정의
    - 연속된 데이터를 서버가 실시간으로 전송하며, 클라이언트는 그것을 순차적으로 교체해가며 표시하는 방식
    - 이 형식은 주로 실시간 MJPEG 스트리밍에서 주로 사용
    - 즉, 하나의 HTTP 연결 안에서 여러 장의 JPEG 이미지를 계속 보내고, 클라이언트는 그것을 교체하면서 영상처럼 보여주는 것

  - 헤더 예시
    ```http
    HTTP/1.0 200 OK
    Content-Type: multipart/x-mixed-replace; boundary=--frame
    ```
    - 이 응답은 여러 파트로 구성됨
    - 각 파트는 --frame이라는 boundary(경계)로 구분됨

  - 실제 데이터 구조 예시
    - 이렇게 하나의 HTTP 응답에서 JPEG 이미지들이 끊기지 않고 계속 전송됨
    - 클라이언트는 각 이미지를 실시간으로 교체하며 영상처럼 렌더링
    ```http
    --frame
    Content-Type: image/jpeg
    Content-Length: 12345

    <바이트 이미지 데이터 1>

    --frame
    Content-Type: image/jpeg
    Content-Length: 12300

    <바이트 이미지 데이터 2>

    --frame
    Content-Type: image/jpeg
    Content-Length: 12000

    <바이트 이미지 데이터 3>
    ...
    ```

  - 왜 유용한가?
    - 하나의 연결로 실시간 스트리밍 가능 (WebSocket 없이도!)
    - 매우 단순한 카메라(예: IP 카메라)나 서버 구현에서 쉽게 사용
    - HTTP/1.1로도 충분히 처리 가능

  - 브라우저/앱에서의 처리 방식
    - 브라우저: <img src="mjpeg-stream-url" /> 사용 시 자동 처리
    - React Native: WebView로 열면 자동 재생됨 (하지만 커스터마이징은 어려움)
    - 고급 앱	MJPEG 파서를 직접 구현하거나 native decoder 연동 필요

- Native Module 사용 이유
  - Image + setInterval 방식은 다음과 같은 단점 존재
    - setInterval로 계속 리렌더링 → CPU 사용량 증가
    - 이미지 간 부드러운 전환이 어려움 → 프레임 드랍
    - JPEG 이미지 간 연결 불연속 → 화면 깜빡임

  - 실시간 MJPEG 스트리밍을 끊김 없이(부드럽게) 처리하려면 Android/iOS의 MJPEG 디코더를 직접 사용하는 네이티브 모듈 방식이 베스트

  - 아키텍쳐 개요
    - React Native는 MJPEG을 직접 해석 못 하므로, 네이티브 영역에서 MJPEG 프레임을 읽고 화면에 그리는 방식을 사용
    ```plaintext
    [ MJPEG 서버 (IP 카메라 등) ]
            ↓ MJPEG (multipart/x-mixed-replace)
    [ React Native 앱 ]
            ↓
    [ Custom Native Module ]
            ↓
    [ SurfaceView (Android) / UIImageView (iOS) ]
    ```

  - Android에서 구현 방식
    - MJPEG Decoder + SurfaceView
      - 네이티브(Java/Kotlin)에서 HttpURLConnection 또는 OkHttp로 MJPEG 스트림을 연다
      - multipart boundary 기준으로 JPEG 이미지를 분리
      - BitmapFactory.decodeStream()으로 JPEG 디코딩
      - SurfaceView 또는 TextureView에 이미지 반복 렌더링

    - 주요 코드 흐름 (Kotlin 예시)
      ```kotlin
      val url = URL("http://camera-ip/mjpeg")
      val conn = url.openConnection() as HttpURLConnection
      conn.doInput = true
      conn.connect()

      val inputStream = conn.inputStream
      while (true) {
          val frame = readNextJpegFrame(inputStream) // boundary 기준으로 읽음
          val bitmap = BitmapFactory.decodeByteArray(frame, 0, frame.size)
          surfaceHolder.lockCanvas()?.let { canvas ->
              canvas.drawBitmap(bitmap, 0f, 0f, null)
              surfaceHolder.unlockCanvasAndPost(canvas)
          }
      }
      ```

  - iOS에서 구현 방식
    - MJPEG Parser + UIImageView
      - URLSession으로 MJPEG 스트림을 수신
      - boundary 기준으로 JPEG 파싱
      - UIImage(data:)로 디코딩
      - UIImageView에 실시간 적용

    - 주요 코드 흐름 (Swift 예시)
      ```swift
      let url = URL(string: "http://camera-ip/mjpeg")!
      let task = URLSession.shared.dataTask(with: url) { data, response, error in
          // boundary로 이미지 분리 → UIImage로 변환 → DispatchQueue.main에서 렌더링
      }
      ```
- React Native 에서 실시간 영상 스트리밍을 출력하는 방법과 상세 내용
  - 실시간 영상 출력 방식 개요
    - HLS (HTTP Live Streaming)
      - 가장 널리 쓰이는 방식, .m3u8 + .ts 조합, 수 초 지연 있음
    - RTSP (Real Time Streaming Protocol)
      - 많이 사용하나 모바일 브라우저/RN에서 직접적인 재생 불가
    - MJPEG (Motion JPEG)
      - 이미지 연속 출력 방식, 구현 쉬우나 저화질용
    - WebRTC
      - 초저지연 P2P 방식, 복잡하지만 고성능

  - 실용적인 선택 조합: HLS + react-native-video
    - 왜 HLS 선택하는가?
      - 대부분의 CCTV NVR이나 서버는 RTSP → HLS 변환 게이트웨이를 제공함 (예: FFmpeg, Nginx, Media Server)
      - React Native 앱에서는 HLS만으로 영상 재생이 가능하며 유지보수도 쉬움

  - HLS 방식 실시간 영상 출력 - 예시
    - (1) 설치
      ```bash
      npm install react-native-video
      ```

    - (2) 예제 코드
      ```tsx
      import React from 'react';
      import { View, StyleSheet, Dimensions } from 'react-native';
      import Video from 'react-native-video';

      const RealTimePlayer = () => {
        return (
          <View style={styles.container}>
            <Video
              source={{ uri: 'https://example.com/stream.m3u8' }} // HLS URL
              style={styles.video}
              controls={true}
              resizeMode="cover"
              bufferConfig={{
                minBufferMs: 5000,
                maxBufferMs: 10000,
                bufferForPlaybackMs: 1000,
                bufferForPlaybackAfterRebufferMs: 2000,
              }}
            />
          </View>
        );
      };

      const styles = StyleSheet.create({
        container: {
          flex: 1,
          backgroundColor: '#000',
        },
        video: {
          width: Dimensions.get('window').width,
          height: Dimensions.get('window').width * 9 / 16,
        },
      });

      export default RealTimePlayer;
      ```

  - RTSP밖에 지원하지 않을 때
    - RTSP는 RN에서 직접 재생 불가하여 중간 서버 필요
      - 방법: RTSP -> HLS 변환
        - 서버 예시(FFmpeg)
          ```bash
          ffmpeg -rtsp_transport tcp -i rtsp://camera-ip/stream \
          -c:v libx264 -hls_time 2 -hls_list_size 3 -f hls stream.m3u8
          ```
          - 변환된 HLS 파일(.m3u8)을 웹 서버로 호스팅
          - React Native에서는 이 URL로 재생

  - MJPEG 방식 (간단한 카메라용)
    - WebView 활용
      ```tsx
      import React from 'react';
      import { View, StyleSheet } from 'react-native';
      import { WebView } from 'react-native-webview';

      const MJPEGStream = () => {
        return (
          <View style={styles.container}>
            <WebView
              source={{ uri: 'http://camera-ip/mjpeg-stream' }}
              style={styles.webview}
            />
          </View>
        );
      };

      const styles = StyleSheet.create({
        container: { flex: 1 },
        webview: { flex: 1 },
      });

      export default MJPEGStream;
      ```

  - 고급 방식: WebRTC 기반 CCTV 연동
    - 실시간성이 매우 중요한 상황 (딜레이 < 500ms)이라면 WebRTC가 필요하지만, React Native에서 WebRTC를 구현하려면 native 연동이 필요

    - WebRTC 연동
      - 패키지: react-native-webrtc
      - 서버: Janus, Kurento, Mediasoup 등의 SFU 필요
      - 복잡도 높지만 음성/화상/양방향 제어에 적합
        - 실시간 통화, 원격 제어, 로봇 스트리밍 등에서 사용

  - 개발 시 유의 사항
    - 로딩 지연, 끊김 등 대비를 위해 onBuffer, onError, onLoadStart 핸들러 처리 반드시 필요
    - VPN, 방화벽 등 네트워크 환경도 중요한 고려 요소

- React Native에서 RTSP 만 지원하는 영상을 네이티브 단에서 처리하는 방법
  - 전체 구조
    ```scss
    [CCTV RTSP 스트림]
            ↓ (RTSP 전용 네이티브 라이브러리)
    [Native Layer: Android/iOS]
            ↓ (비디오 렌더링, 디코딩)
    [React Native: Native UI Component]
            ↓
    앱 화면에 실시간 영상 출력
    ```

  - Android RTSP 처리
    - 사용 가능한 라이브러리
      - VLC Android SDK
        - RTSP/HLS/MP4 등 거의 모든 프로토콜 지원
        - 안정적, 고성능, 오픈소스
        - GitHub: https://code.videolan.org/videolan/libvlc-android
      - FFmpeg 기반 플레이어 (ExoPlayer + FFmpeg 확장)
        - 복잡하며,유지보수 어려움
        - 커스터마이징 필요
      - VLC 추천 (구현 간단, 안정적)

    - 안드로이드 구현 흐름
      - 안드로이드 모듈에서 VLC 기반 커스텀 SurfaceView 또는 TextureView 생성
      - ReactPackage로 해당 ViewManager 등록
      - React Native 에서 <RTSPPlayer /> 컴포넌트처럼 사용

    - 핵심 코드 예시
      ```kotlin
      class RTSPPlayerView(context: Context): SurfaceView(context), IVLCVout.Callback {
          private var mediaPlayer: MediaPlayer? = null

          fun play(rtspUrl: String) {
              val libVLC = LibVLC(context, listOf("--no-drop-late-frames", "--no-skip-frames"))
              mediaPlayer = MediaPlayer(libVLC)
              mediaPlayer?.vlcVout?.setVideoView(this)
              mediaPlayer?.vlcVout?.attachViews()
              mediaPlayer?.media = Media(libVLC, Uri.parse(rtspUrl))
              mediaPlayer?.play()
          }

          override fun onSurfacesCreated(vout: IVLCVout?) {}
          override fun onSurfacesDestroyed(vout: IVLCVout?) {}
      }
      ```

  - iOS에서 RTSP 처리
    - 사용할 수 있는 라이브러리
      - MobileVLCKit (VLC iOS SDK)
        - CocoaPods 설치 가능
        - RTSP 스트리밍을 UIView에 출력 가능
      - FFmpeg iOS Framework
        - 빌드 복잡, 유지보수 어려움
        - 커스텀 디코딩 필요
      - VLC 기반 MobileVLCKit 추천

    - iOS 구현 흐름
      - Swift/Objective-C로 UIView 기반 플레이어 구현
      - RCTViewManager로 React Native 브릿지 생성
      - React Native에서 <RTSPPlayer />로 사용

    - 핵심 코드 예시
      ```swift
      import MobileVLCKit

      class RTSPPlayerView: UIView {
          private var mediaPlayer: VLCMediaPlayer?

          func play(url: String) {
              mediaPlayer = VLCMediaPlayer()
              mediaPlayer?.drawable = self
              mediaPlayer?.media = VLCMedia(url: URL(string: url)!)
              mediaPlayer?.play()
          }
      }
      ```

  - React Native 연동
    - Android/iOS 공통: Native UI 컴포넌트로 등록
      - Android: RTSPPlayerPackage.kt
        ```kotlin
        class RTSPPlayerPackage : ReactPackage {
            override fun createViewManagers(...) = listOf(RTSPPlayerViewManager())
        }
        ```
      - iOS: RTSPPlayerViewManager.swift
        ```swift
        @objc(RTSPPlayerViewManager)
        class RTSPPlayerViewManager: RCTViewManager {
            override func view() -> UIView {
                return RTSPPlayerView()
            }
        }
        ```
      - React Native 측 사용 예:
        ```tsx
        import { requireNativeComponent } from 'react-native';

        const RTSPPlayerView = requireNativeComponent('RTSPPlayerView');

        export default function CCTVViewer() {
          return (
            <RTSPPlayerView
              style={{ width: '100%', height: 300 }}
              streamUrl="rtsp://camera-ip/live"
            />
          );
        }
        ```
        - 필요하면 prop 전달 (streamUrl)이나 상태 이벤트 (onError, onReady)도 브리지로 넘길 수 있음.

  - 장점 및 주의사항
    - 장점
      - 지연 최소화: HLS 대비 RTSP는 수 초 빠름
      - 고성능 디코딩: VLC/FFmpeg는 하드웨어 디코딩 지원
      - CCTV 하드웨어 호환성 높음

    - 주의사항
      - VLC 라이브러리는 앱 용량 증가 (수 MB 이상)
      - iOS는 App Store 정책상 RTSP 보안 문제 검토 필요
      - 네트워크 상태에 따라 reconnect 로직 필요

- React Native에서 Dynamic Linking
  - Native 코드 (iOS의 .framework, Android의 .so)와 JS 코드 간 연결을 런타임에 설정하는 것.
  - 예를 들어, 일부 라이브러리는 빌드시가 아닌 앱 실행 시 native 모듈을 로드할 수 있도록 구성되며, 이를 동적 연결이라고 함.
  - 주로 수동 native 설정이나 외부 바이너리 연동 시 사용됨.

- React Native에서 Code Splitting이 필요한 이유
  - 앱의 초기 로딩 속도 개선
  - 큰 JS 번들을 여러 청크로 나누어 필요한 시점에만 코드 로드 가능
  - Web에서는 흔하지만, React Native에서는 공식적으로 지원되지 않아 수동 구현 또는 라이브러리(react-native-dynamic-bundle 등) 필요

- React Native에서 Flipper를 사용하는 이유
  - 강력한 디버깅 도구 제공
    - 네트워크 요청 확인
    - Redux 상태 추적
    - Native logs 보기
    - 레이아웃 시각화
  - Android/iOS 모두 지원하며, 디버깅과 성능 분석에 매우 유용함

- React Native의 Metro Bundler와 Webpack의 차이점
  - Metro Bundler
    - React Native 기본 번들러
    - 빠른 HMR(Hot Reload), React Native에 최적화
    - 설정이 간단하고 JS 트랜스파일에 특화됨

  - Webpack
    - 주로 Web에서 사용됨
    - 고급 설정 및 다양한 플러그인 지원
    - React Native에는 별도로 설정하지 않으면 직접 사용하지 않음

- React Native에서 Hermes 엔진을 사용하는 장점
  - Facebook이 개발한 경량 JavaScript 엔진
  - 장점:
    - 앱 시작 속도 향상
    - 메모리 사용량 감소
    - APK 크기 감소
    - GC(가비지 컬렉션) 최적화
  - 특히 저사양 Android 기기에서 효과적

- React Native에서 SafeAreaView의 역할
  - iOS의 노치, 상태바, 홈 인디케이터 등 시스템 UI를 피해서 콘텐츠 배치
  - 장치별 안전 영역(safe area) 안에서 레이아웃이 자동 조정되도록 함
  - react-native-safe-area-context 패키지와 함께 사용하면 더 정교한 제어 가능

- React Native에서 Dynamic Styles을 적용하는 방법
  - 조건에 따라 스타일을 동적으로 변경하는 기법
  - 대표 예시:
    ```js
    const styles = {
      container: {
        backgroundColor: isDarkMode ? 'black' : 'white',
      },
    };
    ```
  - StyleSheet.create() 또는 객체 리터럴을 활용
  - 테마, 상태, props 등에 따라 실시간 스타일 변경 가능

- React Native에서 Performance Profiling을 수행하는 방법
  - Performance Profiling은 앱의 렌더링 속도, JS 스레드 병목, 메모리 사용 등을 분석하기 위한 과정
  - 주요 방법
    - Flipper + Hermes Debugger
      - Flipper에서 React DevTools 플러그인으로 렌더링 트리/스케줄 분석 가능
      - Hermes 엔진 활성화 시 JS 힙, CPU 프로파일링 지원
    - React Native Dev Menu
      - "Enable Perf Monitor": FPS, JS/Native Bridge 시간 확인
    - Xcode/Android Profiler
      - 네이티브 성능 분석 (CPU, 메모리, GPU 렌더링 등)
    - React Profiler
      - react-devtools로 컴포넌트 단위 렌더 시간 분석
      
  - 성능 이슈는 대부분 JS 스레드 block or re-render 문제 → useMemo, useCallback, FlatList 최적화 등이 핵심

- React Native에서 Detox와 Appium의 차이점
  - Detox
    - React Native에 특화된 E2E 테스트 프레임워크
    - 네이티브 이벤트 루프를 고려해 더 빠르고 안정적
    - Android/iOS 둘 다 지원, JavaScript 기반
    - CI/CD에 잘 통합됨 (예: GitHub Actions)

  - Appium
    - 플랫폼에 독립적인 범용 E2E 테스트 툴
    - 다양한 언어(Java, Python 등)와 플랫폼(Android, iOS, 웹) 지원
    - 설정이 복잡하고 실행 속도 느림
    - 리액트 네이티브 전용은 아님

- React Native에서 Firebase를 연동하는 방법
  - npm install @react-native-firebase/app
  - 필요한 서비스별 설치 (예: auth, firestore 등)
    - 예: npm install @react-native-firebase/auth
  - Android: google-services.json 추가, build.gradle 설정
  - iOS: GoogleService-Info.plist 추가, pod install

- React Native에서 Clipboard API를 사용하는 방법
  - 패키지 설치 : npm install @react-native-clipboard/clipboard
  - 사용 예
    ```js
    import Clipboard from '@react-native-clipboard/clipboard';

    Clipboard.setString('텍스트 복사');
    const text = await Clipboard.getString();
    ```

- React Native에서 StatusBar를 동적으로 변경하는 방법
  - StatusBar 변경 방법
    ```js
    import { StatusBar } from 'react-native';

    // 예시
    <StatusBar barStyle="light-content" backgroundColor="#000000" />
    ```
    - barStyle: 텍스트 색상 (light-content, dark-content)
    - backgroundColor: 배경 색상 (Android 한정)

- React Native에서 Redux Toolkit을 사용하는 이유
  - 보일러플레이트 감소 (createSlice, configureStore)
  - Immer.js 내장 → 불변성 신경 안 써도 됨
  - RTK Query로 API 연동 간편화 가능
  - 타입스크립트 호환성이 뛰어남

- React Native에서 AsyncStorage와 SecureStore의 차이점
  - AsyncStorage
    - 비암호화 로컬 저장소
    - 일반적인 키-값 데이터 저장용
    - @react-native-async-storage/async-storage

  - SecureStore
    - 암호화된 저장소 (iOS Keychain / Android EncryptedSharedPrefs)
    - 민감 정보 저장용 (토큰, 패스워드)
    - Expo 환경에서 기본 제공 (expo-secure-store)

- React Native에서 React Navigation과 React Router의 차이점
  - React Navigation
    - 모바일 앱 전용 네비게이션, 거의 표준
    - Stack, Tab, Drawer 등 모바일 친화적인 네비게이션 구조
    - Android/iOS 네이티브 UX에 최적화
    - React Native 전용으로 설계됨
    - 사용 예: @react-navigation/native, stackNavigator, tabNavigator 등
  - React Router
    - 웹 전용으로 시작, 웹 + 네이티브 지원
    - Route 중심의 선언형 네비게이션
    - 웹 중심의 라우팅 개념을 확장
    - React Native Web 또는 별도 설정 필요
    - react-router-native, react-router-dom 등
  - 정리
    - RN에서는 React Navigation이 표준처럼 사용
    - React Router는 웹 개발자가 기존 코드 공유 시 사용하거나 웹과의 크로스플랫폼을 고려할 때 활용

- React Native에서 ScrollView와 FlatList의 차이점
  - ScrollView
    - 모든 자식을 한 번에 렌더링
    - 많은 데이터에 비효율적 (메모리 과다 사용)
    - 기본적으로 수직/수평 지원
    - 단순 스크롤 용도
    - 항목 수가 적을 때 사용
  - FlatList
    - 필요한 항목만 렌더링 (가상화)
    - 대량 리스트에 최적화
    - 기본적으로 수직/수평 지원
    - Lazy Loading, Pull-to-Refresh, Pagination 지원
    - 항목이 많을 때 (10개 이상이면 FlatList 권장)

- React Native에서 Dynamic Styles을 적용하는 방법
  - 동적 스타일은 조건에 따라 스타일 객체를 조합하는 방식으로 처리
  - 예시 1: 조건 기반
    ```js
    <View style={[styles.container, isDarkMode && styles.darkMode]} />
    ```
  - 예시 2: 인라인 스타일 사용
    ```js
    <View style={{ backgroundColor: isActive ? 'blue' : 'gray' }} />
    ```
  - 예시 3: 함수형 스타일
    ```js
    const getButtonStyle = (pressed) => ({
      backgroundColor: pressed ? 'lightgray' : 'white',
      padding: 10,
    });
    ```

- React Native에서 Performance Profiling을 수행하는 방법
  - Flipper
    - Meta가 만든 공식 디버깅 도구
    - React DevTools, Hermes Debugger, 네트워크/스토리지 확인 가능
  - React Native Performance Monitor
    - Shake > Show Perf Monitor로 FPS 및 JS Thread 사용량 확인
  - Hermes Profiler
    - Hermes 엔진 사용 시 trace를 통해 JS 실행 타임라인 분석 가능
  - Profiling with Chrome DevTools
    - Debug JS Remotely 사용 시 크롬의 Performance 탭 활용 가능

- React Native에서 Detox와 Appium의 차이점
  - Detox
    - React Native 앱에 특화된 E2E 테스트
    - 자바스크립트, 제스트 기반
    - 빠름 (네이티브 접근)
    - 비교적 복잡 (CI/CD 연동 시 어려움)
    - React Native 프로젝트 전용 E2E
  - Appium
    - 범용 모바일 테스트 프레임워크
    - 여러 언어(자바, 파이썬, JS 등)
    - 상대적으로 느림 (WebDriver 기반)
    - 다양한 플랫폼 지원, 복잡도 있음
    - 크로스 플랫폼 앱, 복잡한 시나리오 필요 시

- React Native에서 Firebase를 연동하는 방법
  - 라이브러리 설치
    ```bash
    npm install @react-native-firebase/app
    npm install @react-native-firebase/auth
    npx pod-install
    ```
  - Firebase 프로젝트 연동
    - 파이어베이스 콘솔에서 앱 추가 (iOS/Android)
    - google-services.json (Android) 및 GoogleService-Info.plist (iOS) 파일 추가
    - Android: android/build.gradle, app/build.gradle 수정
    - iOS: ios/Podfile 확인 후 pod install
  - 사용 예시
    ```js
    import auth from '@react-native-firebase/auth';

    auth()
      .signInWithEmailAndPassword('email@example.com', 'password')
      .then(user => console.log(user))
      .catch(error => console.error(error));
    ```

- React Native에서 Clipboard API를 사용하는 방법
  - 설치
    ```bash
    npm install @react-native-clipboard/clipboard
    npx pod-install
    ```

  - 사용 예시
    ```js
    import Clipboard from '@react-native-clipboard/clipboard';

    // 복사하기
    Clipboard.setString('Hello, world!');

    // 붙여넣기
    Clipboard.getString().then((text) => {
      console.log('Clipboard text:', text);
    });
    ```

- React Native에서 StatusBar를 동적으로 변경하는 방법
  - 개요
    - 상태바 컴포넌트를 사용하여 색상, 스타일, 표시 여부 등을 동적으로 제어 가능

  - 예시
    ```js
    import { StatusBar } from 'react-native';

    <StatusBar
      barStyle="light-content" // or 'dark-content'
      backgroundColor="#6a51ae"
      translucent={true}
    />
    ```
  - 조건에 따라 동적으로 변경
    ```js
    useEffect(() => {
      StatusBar.setBarStyle('dark-content', true);
      StatusBar.setBackgroundColor('#ffffff');
    }, []);
    ```

- React Native에서 Native Module을 직접 구현하는 방법
  - 개요
    - Java(Android), Objective-C/Swift(iOS)로 네이티브 기능을 확장 가능
  
  - 예시
    - (1) 모듈 생성
      ```java
      package com.yourapp;

      import com.facebook.react.bridge.ReactApplicationContext;
      import com.facebook.react.bridge.ReactContextBaseJavaModule;
      import com.facebook.react.bridge.ReactMethod;

      public class MyModule extends ReactContextBaseJavaModule {
          public MyModule(ReactApplicationContext context) {
              super(context);
          }

          @Override
          public String getName() {
              return "MyModule";
          }

          @ReactMethod
          public void showMessage(String msg) {
              Toast.makeText(getReactApplicationContext(), msg, Toast.LENGTH_SHORT).show();
          }
      }
      ```
    - (2) Package 등록
      ```java
      public class MyPackage implements ReactPackage {
        @Override
        public List<NativeModule> createNativeModules(...) {
          return Arrays.asList(new MyModule(reactContext));
        }
      }
      ```

    - (3) JavaScript에서 사용
      ```js
      import { NativeModules } from 'react-native';
      NativeModules.MyModule.showMessage('Hello from Native!');
      ```

- React Native에서 Gesture Handler를 설정하는 방법
  - 개요
    - 고성능 제스처 처리를 위한 라이브러리
  - 설치
    ```bash
    npm install react-native-gesture-handler
    npx pod-install
    ```
  - 안드로이드 설정
    - MainActivity.java 수정 (ReactActivityDelegate 설정 필요)
  - 사용 예시
    ```js
    import { GestureHandlerRootView, TapGestureHandler } from 'react-native-gesture-handler';

    const App = () => (
      <GestureHandlerRootView style={{ flex: 1 }}>
        <TapGestureHandler onActivated={() => console.log('Tapped')}>
          <View style={{ flex: 1, backgroundColor: 'white' }} />
        </TapGestureHandler>
      </GestureHandlerRootView>
    );
    ```
    - 제스처는 Pan, Tap, LongPress, Pinch, Fling 등 지원

- React Native에서 Hermes의 주요 기능
  - 개요
    - 리액트 네이티브 전용, 최적화된 경량 자바스크립트 엔진
  - 주요 기능
    - 빠른 앱 시작 시간: 바이트코드 precompile로 초기 로딩 속도 개선
    - 낮은 메모리 사용량: 불필요한 JS 객체 관리 최소화
    - JIT 미사용: 정적으로 컴파일하여 예측 가능한 성능
    - 디버깅 도구 지원: Flipper, Chrome Debugger와 연동 가능
    - 배터리 절약: GC 최적화로 백그라운드 전력 소모 감소
  - 참고
    - 리액트 네이티브 0.70+부터 Hermes가 기본으로 활성화

- React Native에서 Expo를 사용할 때의 장단점
  - 장점
    - 빠른 개발 시작 (Zero Config)
    - eas build로 간편한 배포
    - 많은 모듈 내장(expo-camera, expo-image-picker 등)
    - Hot Reload, OTA 업데이트 제공
    - 공식 문서와 예제 풍부
  - 단점
    - Custom Native 코드 제한
    - 자체 Native 빌드 필요 시 eject 필요
    - 일부 고급 기능 미지원
    - 앱 사이즈 커질 가능성 존재
    - 비공식 라이브러리 호환성 이슈 있을 수 있음

- React Native에서 Animated API를 활용한 애니메이션 구현 방법
  - 개요
    - Animated 는 고성능 애니메이션을 구현할 수 있는 리액트 네이티브 내장 API
  - 기본 예제: Opacity 애니메이션
    ```js
    import { Animated } from 'react-native';
    import { useRef, useEffect } from 'react';

    const FadeInView = () => {
      const fadeAnim = useRef(new Animated.Value(0)).current;

      useEffect(() => {
        Animated.timing(fadeAnim, {
          toValue: 1,
          duration: 1000,
          useNativeDriver: true,
        }).start();
      }, []);

      return (
        <Animated.View style={{ opacity: fadeAnim }}>
          <Text>Fade In Text</Text>
        </Animated.View>
      );
    };
    ```
  - 주요 애니메이션 종류
    - Animated.timing() – 지속적 변화
    - Animated.spring() – 스프링 물리효과
    - Animated.loop() – 무한 반복
    - Animated.sequence() / Animated.parallel() – 순차/동시 애니메이션

- React Native에서 Deep Linking을 적용하는 방법
  - 개요
    - 딥링킹은 앱이 외부 URL로 호출될 때 특정 화면을 열도록 설정하는 것
  - 안드로이드 설정
    - AndroidManifest.xml에 intent filter 추가
      ```xml
      <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT"/>
        <category android:name="android.intent.category.BROWSABLE"/>
        <data android:scheme="myapp" android:host="profile" />
      </intent-filter>
      ```
  - iOS 설정
    - Info.plist에 URL types 설정
      ```xml
      <key>CFBundleURLTypes</key>
      <array>
        <dict>
          <key>CFBundleURLSchemes</key>
          <array>
            <string>myapp</string>
          </array>
        </dict>
      </array>
      ```
  - 코드 예시
    ```js
    import { Linking } from 'react-native';

    useEffect(() => {
      const handleUrl = ({ url }) => {
        console.log('Deep link:', url);
      };
      Linking.addEventListener('url', handleUrl);
      Linking.getInitialURL().then((url) => {
        if (url) handleUrl({ url });
      });

      return () => Linking.removeAllListeners('url');
    }, []);
    ```

- React Native에서 AppState를 활용하는 방법
  - 개요: AppState는 앱의 현재 상태 (active, background, inactive)를 감지하는 데 사용

  - 예시
    ```js
    import { AppState } from 'react-native';
    import { useEffect, useRef } from 'react';

    const App = () => {
      const appState = useRef(AppState.currentState);

      useEffect(() => {
        const subscription = AppState.addEventListener('change', nextAppState => {
          console.log('App state changed to', nextAppState);
        });

        return () => subscription.remove();
      }, []);
    };
    ```
    - 앱 백그라운드 진입 시 데이터 저장, 정지 처리 등에 유용

- React Native에서 SafeAreaView의 역할
  - SafeAreaView 역할
    - iOS의 노치, 홈 인디케이터 영역 등 안전한 영역(safe area) 내에서만 UI를 표시하도록 보장
    - iPhone X 이후 디바이스에서 레이아웃이 잘리는 문제를 방지
  - 사용 예시
    ```js
    import { SafeAreaView } from 'react-native';

    <SafeAreaView style={{ flex: 1, backgroundColor: 'white' }}>
      <Text>안전한 영역 안의 내용</Text>
    </SafeAreaView>
    ```
    - react-native-safe-area-context 사용 시 더 정밀한 처리 가능

- React Native에서 CodePush를 활용하여 앱을 배포하는 방법
  - 개요
    - CodePush는 앱스토어 재심사없이 JS코드와 리소스를 OTA 업데이트할 수 있는 서비스
  - 설치
    ```bash
    npm install react-native-code-push
    npx pod-install
    ```
  - App 등록 (App Center에서)
    - App Center에서 앱 등록 후 API Key 확보
  - App에 연결
    ```js
    import codePush from 'react-native-code-push';

    let App = () => {
      return <MainApp />;
    };

    App = codePush({
      checkFrequency: codePush.CheckFrequency.ON_APP_START,
    })(App);

    export default App;
    ```
  - 배포 명령어
    ```bash
    appcenter codepush release-react -a <owner>/<app-name> -d Production
    ```

- React Native에서 Splash Screen을 최적화하는 방법
  - 라이브러리 사용 (권장)
    ```bash
    npm install react-native-splash-screen
    npx pod-install
    ```
  - 네이티브 설정
    - 안드로이드: styles.xml, MainActivity.java 설정
    - iOS: LaunchScreen.storyboard 수정
  - JS 코드에서 숨기기
    ```js
    import SplashScreen from 'react-native-splash-screen';

    useEffect(() => {
      SplashScreen.hide(); // 앱 로딩 후 호출
    }, []);
    ```
    - 최적화 팁: 실제 초기 데이터 로딩 완료 후에 hide() 호출

- React Native에서 Background Task를 실행하는 방법
  - 개요
    - 리액트 네이티브는 기본적으로 백그라운드 실행이 제한되므로 별도 라이브러리 사용이 필요

  - 기능
    - 주기적 백그라운드 작업
      - react-native-background-fetch, 백그라운드에서 주기적으로 작업 수행 (iOS 제한)
    - 장시간 실행
      - react-native-background-timer, JS 타이머를 background에서 유지 (Android 한정)
    - 푸시 기반 wake-up
      - Firebase Cloud Messaging, 푸시 수신 시 앱을 깨움
    - 고급 제어
      - Headlees JS (Android 전용), 앱 종료 후에도 백그라운드 서비스 등록 가능

  - 예시: react-native-background-fetch
    ```bash
    npm install @transistorsoft/react-native-background-fetch
    npx pod-install
    ```
    ```js
    import BackgroundFetch from 'react-native-background-fetch';

    BackgroundFetch.configure({
      minimumFetchInterval: 15,
      stopOnTerminate: false,
      startOnBoot: true,
    }, async () => {
      console.log('[BackgroundFetch] task executed');
      BackgroundFetch.finish();
    });
    ```
    - iOS는 백그라운드 제약이 크므로 주의

- React Native에서 WebSockets을 사용하는 방법
  - 기본 API: WebSocket (브라우저 표준과 동일)
  - 예시
    ```tsx
    const socket = new WebSocket('wss://example.com/socket');

    socket.onopen = () => {
      socket.send('Hello Server!');
    };

    socket.onmessage = (e) => {
      console.log('Received:', e.data);
    };

    socket.onerror = (e) => {
      console.error('Socket error:', e.message);
    };

    socket.onclose = (e) => {
      console.log('Socket closed:', e.code);
    };
    ```
  - 대안 라이브러리
    - socket.io-client (서버가 socket.io 기반일 때)
    - react-native-websocket (간단 래핑용)

- React Native에서 Fast Refresh가 동작하는 방식
  - Fast Refresh는 코드 변경 시 앱 상태를 유지하면서 UI를 실시간 반영해주는 기능
  - 동작 방식
    - 코드 변경 시 Babel이 코드 재빌드 → JS bundle reload
    - 컴포넌트 상태(state, hooks)는 가능한 한 유지됨
    - Hook 오류 발생 시 해당 컴포넌트만 리셋됨
  - 상태를 유지하려면 퓨어 컴포넌트 구조를 지켜야 함
  - useEffect나 상태 관련 코드가 잘못되면 자동으로 해당 컴포넌트만 리셋됨

- React Native에서 TurboModules의 역할
  - TurboModules는 React Native의 Native Module 시스템의 차세대 구조
  - 목적:
    - Native <-> JS 브릿지 성능 향상 (동기 호출 가능)
    - 사용 시점에 로딩 → 앱 초기 로딩 시간 단축
    - C++ 기반 브릿지 → 효율적인 메모리 사용 및 타입 안정성
  - 예전의 NativeModules는 JS <-> Native 간 통신이 느림 (비동기만 가능)
  - 활성화 조건:
    - React Native 0.71 이후 일부 라이브러리에서 적용 가능
    - JSI 기반으로 동작

- React Native에서 Flipper 디버깅 툴을 활용하는 방법
  - 개요
    - Flipper는 Facebook이 만든 React Native 전용 디버깅 도구
  - 기능
    - 콘솔 로그, 네트워크 요청, 성능 모니터링
    - React DevTools, Layout Inspector, Crash reporter
    - SQLite, Redux, AsyscStorage 플러그인
  - 설정 (안드로이드)
    ```gradle
    debugImplementation 'com.facebook.flipper:flipper:0.125.0'
    ```
  - JS 설정
    ```ts
    if (__DEV__) {
      require('react-native-flipper');
    }
    ```
  - 추가 플러그인으로 Firebase, GraphQL, Recoil 디버깅도 가능

- React Native에서 Accessibility를 개선하는 방법
  - 기본 속성
    - accessible={true}: 스크린 리더 탐지 대상
    - accessibilityLabel="Submit": 읽히는 텍스트
    - accessibilityHint="Submits the form": 동작 설명
    - accessibilityRole="button": 역할 선언
  - 예시
    ```tsx
    <TouchableOpacity
      accessible={true}
      accessibilityLabel="Go to Profile"
      accessibilityRole="button"
      onPress={...}
    />
    ```
  - 팁
    - VoiceOver(iOS) / TalkBack (Android) 환경에서 테스트 필수
    - 포커스 순서 제어는 importantForAccessibility 활용

- React Native에서 Gesture Responder System이 동작하는 방식
  - 개요
    - Gesture Responder System은 RN이 터치 이벤트를 처리하는 핵심 시스템
  - 동작 흐름
    - (1) 터치 발생 > 이벤트 전파 시작 (onStartShouldSetResponder)
    - (2) 최상위 responder 결정 > 이후 모든 이벤트를 해당 responder 가 처리
    - (3) onResponderMove, onResponderRelease, onResponderTerminate 등으로 후속 처리
  - 예시
    ```tsx
    <View
      onStartShouldSetResponder={() => true}
      onResponderMove={(e) => console.log(e.nativeEvent)}
      onResponderRelease={() => console.log('released')}
    />
    ```
  - PanResponder, react-native-gesture-handler 는 이 시스템 위에서 동작

- React Native에서 Firebase Firestore와 Realtime Database의 차이점
  - FireStore
    - 문서 기반 (Collection-Document)
    - 강력한 필터링/정렬, 복합 쿼리 가능
    - 실시간 지원 가능
    - 대규모 앱에 적합
    - 가격은 문서 단위 과금
  - Realtime Database
    - 트리 기반 JSON
    - 제한적 (key 기준, 단일 필터)
    - 실시간 가능 (조금 더 빠름)
    - 소규모 앱/센서/실시간 채팅에 적합
    - 가격은 다운로드 양 기반한 산정
  - 정리
    - RN에서는 둘다 react-native-firebase로 통합 지원 가능
    - Firestore가 더 현대적이며 유지관리 용이

- React Native에서 Camera 기능을 구현하는 방법
  - 라이브러리: react-native-vision-camera
  - 설치
    - npm install react-native-vision-camera
    - npx pod-install
  - 사용 예시
    ```tsx
    import { Camera } from 'react-native-vision-camera';

    const cameraRef = useRef<Camera>(null);

    <Camera
      ref={cameraRef}
      style={StyleSheet.absoluteFill}
      device={device}
      isActive={true}
    />
    ```
  - 카메라 권한 요청은 Camera.requestCameraPermission() 사용
  - 대안: react-native-camera (구버전, 유지보수 중단)

- React Native에서 Dark Mode를 적용하는 방법
  - 개요
    - useColorScheme() 훅을 활용
  - 예제
    ```tsx
    import { useColorScheme } from 'react-native';

    const isDark = useColorScheme() === 'dark';

    const styles = StyleSheet.create({
      text: {
        color: isDark ? '#fff' : '#000',
      },
    });
    ```
  - 또는 react-native-paper, styled-components 등의 theming 시스템 활용

- React Native에서 Multi-Threading을 구현하는 방법
  - 개요
    - RN은 기본적으로 싱글 스레드 기반, 병렬 작업은 다음 방식으로 가능
  - 구현 방법
    - JSThread 외부 처리
      - react-native-threads: JS Worker 스레드 생성
      - react-native-worker: WebWorker 스타일
    - Native Module 이용 (C++/Kotlin/Swift)
      - JSI 기반으로 Background 작업 처리
    - 사용 예
      ```js
      import { Thread } from 'react-native-threads';

      const thread = new Thread('./worker.js');
      thread.onmessage = (msg) => console.log(msg);
      thread.postMessage('hello');
      ```

- React Native에서 React Query를 사용하는 이유
  - 개요
    - React Query는 서버 상태(server state) 관리 라이브러리로 다음과 같은 이점 존재
      - 자동 캐싱: 동일 요청 재시도 없이 캐시에서 사용
      - Background Fetch: 화면 전환 시 자동 재요청
      - 쿼리 무효화: invalidateQueries()로 특정 쿼리 갱신
      - 로딩/에러 상태 관리: useQuery 자체로 상태 관리 가능
  - 예제
    ```tsx
    const { data, isLoading } = useQuery(['user', id], () => fetchUser(id));
    ```
    - react-query는 zustand, redux 같은 클라이언트 상태와 별개로 사용됨

- React Native에서 WebView를 활용하는 방법
  - 라이브러리: react-native-webview
  - 설치
    ```bash
    npm install react-native-webview
    npx pod-install
    ```
  - 예제
    ```tsx
    import { WebView } from 'react-native-webview';

    <WebView source={{ uri: 'https://example.com' }} />
    ```
  - JS ↔ Native 메시지 통신: onMessage, postMessage 사용
  - PDF 뷰어, 결제, 인증 페이지 등에 유용

- React Native에서 Reanimated 라이브러리를 사용하는 방법
  - 라이브러리: react-native-reanimated
  - 설치
    ```bash
    npm install react-native-reanimated
    ```
  - 예제
    ```tsx
    const offset = useSharedValue(0);

    const animatedStyle = useAnimatedStyle(() => ({
      transform: [{ translateX: offset.value }],
    }));

    <Animated.View style={animatedStyle} />
    ```
  - 장점:
    - Native thread에서 실행되는 초고성능 애니메이션
    - Gesture, Scroll, Transition 애니메이션 구현 가능

- React Native에서 Lottie를 활용한 애니메이션을 적용하는 방법
  - 라이브러리: lottie-react-native
  - 설치
    ```bash
    npm install lottie-react-native
    npx pod-install
    ```
  - 예제
    ```tsx
    import LottieView from 'lottie-react-native';

    <LottieView source={require('./loading.json')} autoPlay loop />
    ```
  - After Effects → Lottie JSON으로 변환한 애니메이션 사용 가능

- React Native에서 Google Maps를 적용하는 방법
  - 라이브러리: react-native-maps
  - 설치
    ```bash
    npm install react-native-maps
    npx pod-install
    ```
  - 안드로이드 설정
    - AndroidManifest.xml에 API Key 추가
  - 예제
    ```tsx
    <MapView
      style={{ flex: 1 }}
      initialRegion={{
        latitude: 37.78825,
        longitude: -122.4324,
        latitudeDelta: 0.0922,
        longitudeDelta: 0.0421,
      }}
    />
    ```
  - 마커, 커스텀 지도 스타일, 지도 이벤트 지원
  - Google Maps SDK와 연동된 네이티브 수준 성능 제공

- React Native에서 Video Streaming을 구현하는 방법
  - 라이브러리: react-native-video
  - 설치
    - npm install react-native-video
    - npx pod-install
  - 기본 사용
    ```tsx
    import Video from 'react-native-video';

    <Video
      source={{ uri: 'https://example.com/video.m3u8' }}  // HLS/MPEG-DASH 지원
      controls
      resizeMode="contain"
      style={{ width: '100%', height: 200 }}
    />
    ```
  - RTMP, HLS, MPEG-DASH 등 지원
  - 실시간 스트리밍은 별도 Player (예: ffmpeg, ExoPlayer) 커스터마이징 필요

- React Native에서 Native Bridge를 사용하는 이유
  - 개요
    - JS에서 네이티브 기능을 호출할 수 있도록 하는 통로
  - 사용 이유
    - JS에서 접근할 수 없는 플랫폼 기능 호출 (블루투스, NFC, MediaCodec)
    - 성능/하드웨어 기반 처리가 필요한 기능 (OpenGL, ARKit)
    - 네이티브 SDK 연동 (카카오 로그인, 티맵 SDK 등)
  - 최신 방식: TurboModule + JSI (JS Interface)로 전환 추세

- React Native에서 Native Event Emitter의 역할
  - 개요: JS <> 네이티브 간 이벤트 기반 통신 처리
  - 사용 예
    ```tsx
    import { NativeEventEmitter, NativeModules } from 'react-native';

    const eventEmitter = new NativeEventEmitter(NativeModules.MyModule);

    eventEmitter.addListener('onDataReceived', (data) => {
      console.log('Received from native:', data);
    });
    ```
  - 예: 센서 변화, 백그라운드 위치, 네이티브 라이브러리 콜백 수신 등에 사용

- React Native에서 터치 이벤트를 처리하는 방법
  - 기본 방식
    - TouchableOpacity, TouchableWithoutFeedback
    - Pressable: React Native 0.63+ 도입된 더 강력한 터치 컴포넌트

  - 고급 제스처:
    - react-native-gesture-handler
    - PanGestureHandler, TapGestureHandler, GestureDetector

  - 예시
    ```tsx
    <Pressable onPress={() => console.log('pressed')}>
      <Text>Tap me</Text>
    </Pressable>
    ```

- React Native에서 Push Notification을 설정하는 방법
  - 추천 도구: react-native-firebase/messaging
  - Android 설정:
    - Firebase Console → Cloud Messaging 설정
    - google-services.json 추가
    - AndroidManifest.xml 권한 추가
  - iOS 설정:
    - info.plist 권한 설정
    - APNs 인증 키 등록
    - UNUserNotificationCenter 권한 요청
  - 코드:
    ```tsx
    import messaging from '@react-native-firebase/messaging';

    await messaging().requestPermission();
    const token = await messaging().getToken();

    messaging().onMessage(remoteMessage => {
      Alert.alert('Push Received', JSON.stringify(remoteMessage));
    });
    ```

- React Native에서 Apple Pay와 Google Pay를 연동하는 방법
  - 대표 라이브러리: tipsi-stripe, [react-native-payments]
    - Stripe 기반 Apple/Google Pay 연동이 일반적

  - Apple Pay:
    - merchant ID 발급
    - Entitlements 및 Capabilities 설정
    - Stripe SDK 연동 필요

  - Google Pay:
    - PaymentMethodTokenizationSpecification JSON 설정
    - Google Play Console에서 API 활성화 필요

  - Expo에서는 EAS + stripe-react-native 연동 방식 권장

- React Native에서 환경 변수(.env) 파일을 사용하는 방법
  - 라이브러리: react-native-dotenv or react-native-config
  - .env 예
    ```env
    API_URL=https://api.example.com
    APP_ENV=production
    ```
  - 사용 예 (react-native-config)
    ```ts
    import Config from 'react-native-config';
    console.log(Config.API_URL);
    ```
  - 빌드 시점에 .env 값 주입
  - Android/iOS의 Gradle, Info.plist에서도 사용 가능

- React Native에서 EAS(Expo Application Services)를 활용하는 방법
  - 개요
    - Expo가 제공하는 빌드, 배포, 업데이트, 인증서 관리 등 통합 DevOps 플랫폼
  - 핵심 기능
    - EAS Build: 클라우드 빌드 (Custom Native Code 포함 가능)
    - EAS Update: OTA 업데이트 (앱 재배포 없이 JS 코드 핫픽스)
    - EAS Submit: 앱 스토어 자동 제출
    - EAS Secrets: 빌드시 환경 변수 암호화 관리
  - 설치 및 사용
    ```bash
    npm install -g eas-cli
    eas login
    eas build:configure
    eas build --platform android
    ```
  - Expo SDK 43+ 이상, eas.json 설정 필수
  - eas update로 앱을 즉시 업데이트 가능 (Code Push 대안)

- React Native에서 앱 크기를 최적화하는 방법
  - 최적화 방법
    - Proguard / R8: Android에서 불필요한 코드 제거 (minifyEnabled)
    - Hermes 활성화: JS 엔진 크기 감소 (hermes_enabled: true)
    - Unused assets 제거: 사용하지 않는 이미지, 폰트 제거
    - Code Splitting / Lazy Load: 조건부 import로 번들 크기 최소화
    - PNG->WebP: 이미지 최적화
    - Dynamic import, tree-shaking: 필요시에만 import (Webpack과 유사하게 처리)
  - 안드로이드는 android/app/build.gradle의 release 설정 중요
  - iOS는 bitcode, strip unused architectures 확인

- React Native에서 서버와의 실시간 동기화를 구현하는 방법
  - 사용 기술
    - WebSocket: 양방향 통신, 이벤트 기반 동기화
    - Firebase Realtime DB / FireStore: 실시간 데이터 변경 자동 반영
    - SSE (Server Sent Events): 서버에서 Push-Only, 간단한 동기화
    - Polling + ETag: 변경 여부만 확인하여 요청 최적화

- React Native에서 File Upload 기능을 구현하는 방법
  - 라이브러리
    - react-native-document-picker (파일 선택)
    - react-native-image-picker (이미지/동영상 선택)
    - axios or fetch + FormData
  - 예제
    ```js
    const formData = new FormData();
    formData.append('file', {
      uri: file.uri,
      type: file.type,
      name: file.name,
    });

    await fetch('https://api.example.com/upload', {
      method: 'POST',
      body: formData,
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    ```

- React Native에서 Custom Fonts를 적용하는 방법
  - assets/fonts 폴더에 .ttf 또는 .otf 파일 추가
  - react-native.config.js
    ```js
    module.exports = {
      assets: ['./assets/fonts'],
    };
    ```
  - npx react-native link 실행
  - 스타일 적용
    ```tsx
    <Text style={{ fontFamily: 'YourFontName' }}>Hello</Text>
    ```

- React Native에서 Local Authentication(지문, 얼굴 인식)을 적용하는 방법
  - 라이브러리
    - react-native-local-authentication or expo-local-authentication
  - 예시
    ```js
    import * as LocalAuthentication from 'expo-local-authentication';

    const isSupported = await LocalAuthentication.hasHardwareAsync();
    const result = await LocalAuthentication.authenticateAsync();
    if (result.success) {
      // 인증 성공
    }
    ```
  - iOS: NSFaceIDUsageDescription 필요
  - Android: USE_BIOMETRIC 권한 필요


- React Native에서 Dynamic Linking
  - 개요
    - Dynamic Linking은 앱 외부에서 특정 화면으로 직접 진입할 수 있는 URL 기능
    - 예
      - myapp://profile/123
      - https://example.com/products/456
  - 라이브러리
    - react-native-app-link, react-native-deep-linking, React Navigation의 Linking 지원
  - 예제
    ```js
    Linking.addEventListener('url', ({ url }) => {
      const route = extractRouteFromUrl(url);
      navigation.navigate(route.name, route.params);
    });
    ```

- React Native에서 Third-Party 모듈을 효과적으로 관리하는 방법
  - 패키지 버전 고정: 정확한 버전 지정 (^ 또는 ~피하기)
  - 패키지 레벨 관리: yarn outdated, npm audit 등으로 보안/업데이트 확인
  - 중요 모듈만 사용: 경량 라이브러리 우선, 범용 대신 목적별
  - 벤더화 고려: 수정한 외부 패키지는 별도로 관리 (fork or vendors)
  - Expo 사용 시 제한 확인: Expo Go에서 지원되는 모듈인지 확인 필요

- React Native에서 Multi-Platform을 위한 코드 구조화 방법
  - Platform API 분기
    - Platform.OS === 'android' ? ... : ...
  - .ios.js / .android.js
    - 플랫폼별 컴포넌트 분리
  - 폴더 구조 분리
    - src/platforms/web/, src/platforms/native/
  - 환경 변수 활용
    - .env.web, .env.mobile 등 환경 구분
  - 공통 유틸리티/훅 추출
    - UI와 로직 분리 (예: useLogin, useFetch)
  - expo, react-native-web, next.js 기반 통합 개발 시에도 사용 가능

- React Native에서 MobX와 Redux의 차이점
  - MobX
    - 작은 앱 => MobX 빠름
    - OOP + Reactive
    - 설정 간단, observable, action
    - 상태 자동 추적 (proxy 기반)
    - 학습 곡선: 학습 빠르나 디버깅 어려울 수 있음
    - 커뮤니티는 작음
  - Redux
    - 팀 협업/디버깅 => Redux 안전하고 명확
    - FP + 명시적 Flux 구조
    - 상대적으로 복잡 (actions, reducers, store)
    - 명시적 상태 변경
    - 직관적이나 보일러플레이트 많음
    - 크고 방대한 미들웨어 생태계/커뮤니티 존재

- React Native에서 Accessibility를 최적화하는 방법
  - 핵심 속성
    - accessible: 해당 요소를 스크린리더 대상 포함 여부
    - accessibilityLabel: 읽히는 대체 텍스트
    - accessibilityHint: 수행 동작 설명
    - accessibilityRole: 역할 지정 (button, link, header 등)
    - importantForAccessibility: 포커스 포함 여부 조정 (auto, yes, no)
  
  - TIP
    - 터치 가능한 영역은 충분한 크기 (최소 44x44pt)
    - iOS VoiceOver / Android TalkBack 테스트 필수
    - Focus 순서 제어 → accessibilityViewIsModal, focusOnView()

- React Native에서 WebView와 iframe의 차이점
  - WebView (React Native)
    - Native 앱에서 외부 웹 페이지 표시
    - react-native-webview 패키지 사용
    - sandbox 가능 / 통신 제어 가능
      - Refs (Sandbox): 외부 프로그램이나 코드를 안전하게 테스트하거나 실행하기 위해 격리된 환경을 제공하는 보안 기술
      - 시스템의 다른 부분에 영향을 주지 않고 잠재적으로 위험할 수 있는 코드를 실행할 수 있도록 해줍니다
    - JS < > Native 통신 (postMessage)
    - WebView는 네이티브 권한 처리 가능
  - iframe (Web)
    - 웹페이지 내에서 다른 HTML 삽입
    - HTML 내 <iframe> 사용
    - 비교적 낮은 보안, clickjacking 우려
    - 제한된 cross-origin 통신
    - iframe은 브라우저 권한만 사용 가능
  - 정리
    - WebView는 브라우저 대체물
    - iframe은 HTML 레벨에서의 삽입 기능

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