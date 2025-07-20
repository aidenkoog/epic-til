# C, C++

- C언어, C++ 관련 내용을 정리합니다

## C언어 프로그램 실행

- 맥북(macOS)에서 C 코드 실행
  - C 컴파일러 설치 확인
  - clang 설치여부 확인
    - clang --version
  - 미설치 시 Xcode Command Line Tools 설치
    - xcode-select --install
  - 컴파일
    - clang hello.c -o hello
  - 실행
    - ./hello

- 리눅스(서버 PC)에서 C 코드 실행
  - 참고: ARM 기반이라면 크로스 컴파일이 필요
  - C 컴파일러 설치
    - gcc가 기본적으로 설치되어 있을 가능성
    - 미설치 시 아래와 같이 설치 진행
      - sudo apt update && sudo apt install gcc (Ubuntu 계열)
      - sudo yum install gcc (CentOS 계열)
    - 설치 여부 확인
      - gcc --version
    - 내 PC에서 서버PC로 파일 복사
      - scp hello.c user@server-pc-ip:/home/user/
    - 컴파일 및 실행
      - gcc hello.c -o hello
      - ./hello

- 맥북에서 컴파일한 실행 파일을 리눅스에서 실행하는 방법
  - 맥북과 리눅스는 운영체제가 다르기 때문에, 맥북에서 빌드한 실행 파일을 그대로 리눅스에서 실행 불가능
    - 방법 1: 서버 PC에서 직접 컴파일
    - 방법 2: 리눅스용 실행 파일을 크로스 컴파일
  - 맥북에서 크로스 컴파일을 위해 설치 필요 항목
    - gcc-arm-linux-gnueabi 또는 gcc-aarch64-linux-gnu 같은 크로스 컴파일러
      - brew install x86_64-elf-gcc (x86_64 리눅스용 실행 파일 빌드)
      - brew install aarch64-linux-gnu-gcc (ARM 리눅스용 실행 파일 빌드)
  - 컴파일
    - aarch64-linux-gnu-gcc hello.c -o hello_arm
  - 서버 PC로 전송
    - 이렇게 생성한 실행 파일(hello_arm)을 scp로 서버PC에 복사하고 실행
  - 참고: PC가 어떤 CPU 아키텍쳐인지 확인하는 방법
    - uname -m 명령어를 실행하면 아키텍처를 알 수 있음

- 다이아몬드 상속