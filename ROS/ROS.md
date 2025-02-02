# ROS

정리될 내용들은 아래와 같습니다.

- 개념 / 용어 정의, 사용 이유
- Interview Question, Answer

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