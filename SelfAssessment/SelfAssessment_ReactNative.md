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