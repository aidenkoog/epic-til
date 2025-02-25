# ROS

정리될 내용들은 아래와 같습니다.

- 개념 / 용어 정의, 사용 이유


## 로봇 운영체제(ROS,Robot Operating System)

- 로봇 응용 프로그램을 개발할 때 필요한 
  - 하드웨어 추상화
  - 하위 디바이스 제어
  - 일반적으로 사용되는 기능의 구현
  - 프로세스간의 메시지 패싱
  - 패키지 관리
  - 개발환경에 필요한 라이브러리와 다양한 개발 및 디버깅 도구를 제공

- ROS는 로봇 응용 프로그램 개발을 위한 운영체제와 같은 로봇 플랫폼
- Robot Operation System이라는 말과는 다르게, ROS는 운영체제가 아니라
- 로봇 개발을 위한 라이브러리(혹은 프레임워크)

## ROS 개요 (위 내용 재정리)

- ROS는 로봇 소프트웨어 개발을 위한 오픈소스 프레임워크로, 로봇 애플리케이션 개발을 쉽게 하기 위해 다양한 기능을 제공
  - 분산 프로세스 통신: 여러 노드(Node)가 네트워크를 통해 서로 데이터를 주고받음.
  - 모듈화된 구조: 여러 개의 패키지(Package)로 구성되어 있어 특정 기능만 추가하거나 수정 가능.
  - 강력한 커뮤니티 및 생태계: 다양한 오픈소스 패키지 제공.

- ROS 버전
  - ROS 1: 기존 ROS로, roscore 실행이 필요하고 roscpp, rospy 등의 라이브러리를 사용.
  - ROS 2: 개선된 버전으로, DDS(Data Distribution Service) 기반으로 만들어져 실시간성을 강화함. rclcpp, rclpy 사용.

## ROS 기본 개념

- 노드, 토픽, 서비스, 액션, 메세지, 파라미터 개념 존재
- 노드(Node)
  - ROS에서 실행되는 독립적인 프로세스로, 특정 기능을 담당하는 프로그램을 의미해.
  - rosrun package_name node_name

- 토픽(Topic)
  - 노드 간 비동기 방식으로 데이터를 주고받을 때 사용하는 채널.
    - 퍼블리셔(Publisher): 데이터를 보내는 노드
    - 서브스크라이버(Subscriber): 데이터를 받는 노드.
  - rostopic pub /topic_name std_msgs/String "Hello, ROS!"
  - rostopic echo /topic_name

- 서비스(Service)
  - 요청-응답 방식의 통신을 제공하는 기능.
    - 서비스 서버(Service Server): 요청을 처리하는 노드.
    - 서비스 클라이언트(Service Client): 요청을 보내는 노드.
  - rosservice call /service_name "request_data"

- 액션(Action)
  - 서비스보다 더 확장된 개념으로, 진행 상태를 지속적으로 반환하는 비동기 작업 수행

- 메시지(Message)
  - 토픽, 서비스, 액션에서 사용되는 데이터 구조.
  - rosmsg show std_msgs/String

- 파라미터(Parameter)
  - 전역적으로 설정할 수 있는 변수로, rosparam을 통해 저장 및 조회 가능

## ROS 핵심요소, 환경셋업, 노드작성, 필수명령어, 토픽 발행/구독, 서버/클라이언트, 실행/테스트

- 개요
  - ROS( Robot Operating System): 로봇 개발을 위한 오픈소스 프레임워크

- ROS의 기본 개념
  - ROS 핵심 요소
    - 노드(Node):	ROS에서 실행되는 하나의 프로그램(프로세스)
    - 토픽(Topic): 노드 간의 메시지 전달을 위한 통신 채널 (Publish/Subscribe 방식)
    - 메시지(Message): 노드 간 데이터를 주고받는 데이터 형식 (std_msgs/String, sensor_msgs/Image 등)
    - 서비스(Service): 요청(Request)과 응답(Response)을 처리하는 방식
    - 액션(Action): 서비스와 유사하지만, 장시간 실행되는 비동기 작업 수행
    - 패키지(Package): ROS에서 코드, 실행 파일, 메시지 등을 관리하는 단위
    - 워크스페이스(Workspace): ROS 프로젝트를 관리하는 작업 공간 (catkin_ws 등)

  - ROS 환경 설정 및 기본 명령어
    - (1) ROS 설치 및 초기 설정
	    - ROS를 설치한 후, 매 실행 시 환경 변수를 설정해야 함.
        - source /opt/ros/noetic/setup.bash  # ROS Noetic 환경 설정 (Ubuntu 20.04 기준)
      - 여러 워크스페이스를 사용할 경우:
        - source ~/catkin_ws/devel/setup.bash  # 내 워크스페이스 설정
      - 자동 실행을 위해 .bashrc에 추가:
        - echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
        - source ~/.bashrc

    - (2) ROS 필수 명령어
      - roscore: ROS 마스터 노드 실행 (ROS 시스템 시작)
      - rosnode list: 현재 실행 중인 모든 노드 목록 출력
      - rosnode info <노드명>: 특정 노드의 정보 확인
      - rostopic list: 현재 활성화된 모든 토픽 확인
      - rostopic echo <토픽명>: 특정 토픽의 메시지 출력
      - rosservice list: 사용 가능한 서비스 목록 출력
      - rosservice call <서비스명>: 특정 서비스 호출
      - roslaunch <패키지명> <launch 파일명>: launch 파일을 실행하여 여러 노드를 동시에 실행
      - catkin_make: ROS 패키지 빌드 (컴파일)

  - ROS 패키지 생성 및 빌드
    - 새 패키지 생성
      - cd ~/catkin_ws/src
      - catkin_create_pkg my_robot std_msgs rospy roscpp
      - cd ~/catkin_ws
      - catkin_make
      - source devel/setup.bash
    - 설명
	    - my_robot 패키지를 생성하면서 의존성(std_msgs, rospy, roscpp)을 추가
	    - catkin_make로 패키지를 빌드 후, 환경 변수 설정

  - ROS 노드(Node) 작성
    - (1) Python 노드 작성
    - (2) C++ 노드 작성

  - ROS 토픽(Topic) 통신
    - 1) Python 노드에서 토픽 구독 (Subscriber)

  - ROS 서비스(Service)
    - (1) 서비스 서버 (Python)
    - (2) 서비스 클라이언트 (Python)

  - ROS 실행 및 테스트
    - (1) ROS 시스템 실행
    - (2) 노드 실행
    - (3) 메시지 확인
    - (4) 서비스 호출

  - 결론
    - ROS는 노드 기반의 분산 시스템으로, 노드 간 통신(Topic), 요청-응답(Service), 장기 실행(Action) 등의 개념을 이해하는 것이 필수
    - Python을 활용한 노드 구현이 기본이며, C++을 사용할 수도 있음
    - rostopic, rosnode, rosservice 등 기본 명령어를 익히고, catkin_make를 활용한 빌드 프로세스를 이해하는 것이 중요