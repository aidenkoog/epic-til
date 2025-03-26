# Concepts, Features, Types and Pros and Cons

Organize concepts, features, types and Pros and Cons

## iOS, Swift

- iOS의 주요 아키텍처와 컴포넌트 설명
  - iOS의 주요 아키텍처 개요
    - iOS 애플리케이션은 크게 5계층(5-Tier Architecture) 으로 구성

  - 주요 아키텍쳐
    - Core OS
	  - iOS의 가장 하위 계층, 하드웨어 및 시스템 수준의 기능을 제공
	  - 핵심 역할: 메모리 관리, 파일 시스템, 네트워크 보안, Bluetooth, 암호화 등
	  - 관련 프레임워크
	    - Kernel (XNU): iOS의 Unix 기반 커널
	    - Security Framework: 암호화 및 보안 관련 기능
	    - Core Bluetooth: 블루투스 통신 지원

    - Core Services
	  - 앱 개발에서 가장 많이 사용되는 기본 서비스 제공 계층
	  - 핵심 역할: 데이터 저장, 네트워크 통신, 로케이션 서비스 제공
	  - 관련 프레임워크:
	    - Foundation Framework: 컬렉션(Array, Dictionary 등), 파일 입출력, 날짜 및 시간 처리.
	    - Core Data: 객체 기반 데이터 저장소 (ORM 역할)
	  - CloudKit: iCloud 연동
      - Core Location: GPS 및 위치 기반 서비스

    - Media
	  - 멀티미디어 처리 및 UI 표현을 담당
	  - 핵심 역할: 그래픽, 오디오, 비디오 재생 및 이미지 처리
	  - 관련 프레임워크
	    - AVFoundation: 오디오 및 비디오 처리
	    - Core Animation: UI 애니메이션 효과 제공
	    - Core Graphics: 2D 그래픽 렌더링
	    - Metal: GPU 최적화 그래픽 프로그래밍

    - Cocoa Touch (UIKit)
	  - 사용자 인터페이스(UI) 및 사용자 경험(UX) 제공 계층
	  - 핵심 역할: 버튼, 텍스트 필드, 테이블 뷰, 제스처 등을 제공하여 UI 구현
	  - 관련 프레임워크
	    - UIKit: iOS의 기본 UI 프레임워크
	    - SwiftUI: 선언형 UI 프레임워크 (iOS 13부터 지원)
	    - EventKit: 캘린더 및 일정 관리
	    - Contacts: 주소록 데이터 관리

    - Application Layer
	  - 실제 앱이 동작하는 계층
	  - 개발자가 구현하는 비즈니스 로직, UI 레이아웃, 데이터 처리 등이 포함

  - iOS 주요 디자인 패턴 (아키텍처 패턴)
    - 개요
      - iOS 개발에서는 코드의 재사용성, 유지보수성, 테스트 용이성을 높이기 위해 아키텍처 패턴을 적용
    - MVC (Model-View-Controller)
      - iOS의 기본 아키텍처 패턴
      - Apple이 공식적으로 권장하지만, ViewController에 너무 많은 로직이 집중되는 문제가 있음 (Massive View Controller 문제)
      - 구성요소 및 설명
        - Model: 데이터 및 비즈니스 로직 담당
        - View: UI 및 사용자 인터페이스 표시
        - Controller: View와 Model을 연결하는 중간 역할 (UIViewController)
    - MVVM (Model-View-ViewModel)
      - UI 로직을 ViewModel로 분리하여 테스트 가능성을 높이고 유지보수를 쉽게 하는 패턴
      - SwiftUI 및 Combine과 함께 사용하기 적합
      - 구성요소 및 설명
        - Model: 데이터 구조 및 비즈니스 로직
        - ViewModel: UI에서 사용할 데이터를 가공하여 View에 전달
        - View: UI를 담당 (SwiftUI 또는 UIViewController)
    - VIPER (View-Interactor-Presenter-Entity-Router)
      - iOS에서 가장 분리도가 높은 구조로, 대규모 프로젝트에 적합
      - 테스트가 용이하고 유지보수가 쉬운 구조
      - 구성요소 및 설명
        - View: UI 표시
        - Interactor: 비즈니스 로직 및 데이터 처리
        - Presenter: View와 Interactor 간 데이터 변환
        - Entity: 데이터 모델
        - Router: 화면 이동 (네비게이션 관리)
  - iOS 주요 컴포넌트
    - ViewController (UIViewController)
	  - 화면을 구성하는 가장 기본적인 컴포넌트.
	  - 라이프사이클 (viewDidLoad, viewWillAppear, viewDidDisappear) 관리.
    - TableView & CollectionView (UITableView, UICollectionView)
	  - 리스트 UI를 구성할 때 사용.
	  - UITableView → 단순 리스트
	  - UICollectionView → 그리드 형태 리스트
    - UserDefaults & Core Data
	  - UserDefaults → 간단한 데이터 저장 (예: 설정 값)
	  - Core Data → ORM 기반 로컬 데이터 저장소
    - URLSession
	  - 네트워크 통신을 위한 API (GET, POST 요청 처리)
    - Combine & SwiftUI
	  - Combine → 비동기 데이터 스트림 관리 (Publisher, Subscriber)
	  - SwiftUI → 선언형 UI 프레임워크

- Swift의 주요 특징은?
    - 개요
        - Apple이 개발한 프로그래밍 언어로, iOS, macOS, watchOS, tvOS 애플리케이션을 개발하기 위해 사용
        - 안전성, 성능, 간결성을 고려하여 설계된 언어로, 기존 Objective-C보다 더 직관적이고 효율적인 코드 작성을 지원
    - Swift의 목표
        - 안전한(Safe) 코드 → 메모리 충돌 방지, 타입 안정성
        - 빠른(Fast) 실행 속도 → LLVM 기반 컴파일러 사용
        - 간결한(Simple) 문법 → 개발자가 쉽게 배울 수 있도록 설계
    - Swift 주요 활용 분야
	       - iOS 앱 개발 (iPhone, iPad)
	       - macOS 앱 개발
	       - watchOS, tvOS 앱 개발
	       - 서버 개발 (Vapor, Kitura 프레임워크 활용)
    - 주요 특징
        - 간결, 직관적인 문법
        - 타입 안정성(Type Safety) 및 타입 추론(Type Inference)
            - 엄격한 타입 시스템을 적용하여 오류를 줄이고, 타입을 자동으로 추론
        - 옵션(Optional) 타입 - Null Safety 지원
            - Null 값(= nil) 사용을 엄격하게 제한하여 런타임 오류를 방지
								    - 옵셔널(Optional)을 사용하여 값이 존재할 수도 있고, 존재하지 않을 수도 있는 상황을 명확하게 처리
        - 함수형 프로그래밍 지원 (Functional Programming)
            - 고차 함수(Higher-Order Functions) 를 제공하여 함수형 프로그래밍 패러다임을 지원
        - 메모리 안전성 (Automatic Memory Management - ARC)
            - ARC(Automatic Reference Counting) 를 사용하여 메모리를 자동으로 관리하므로, 개발자가 직접 메모리를 해제할 필요가 없음
        - 프로토콜 지향 프로그래밍 (Protocol-Oriented Programming, POP)
            - 객체 지향 프로그래밍(OOP)보다 프로토콜 지향 프로그래밍(POP)을 강조하여 코드의 유연성과 확장성을 높임
        - 안전한 에러 처리 (Error Handling)
            - do-try-catch 구문을 사용하여 예외를 명확하게 처리할 수 있도록 함
        - 강력한 확장 기능 (Extensions)
            - 확장(Extension) 기능을 사용하면 기존 클래스, 구조체, 열거형에 새로운 기능을 추가 가능
        - 멀티스레딩 및 동시성(Concurrency) 지원
            - 비동기 프로그래밍을 쉽게 구현할 수 있도록 async/await을 지원
    - 결론
        - Swift는 Apple의 공식 프로그래밍 언어로 iOS, macOS, watchOS, tvOS 앱 개발에 사용됨
        - 간결하고 직관적인 문법, 타입 안정성, 옵셔널, 함수형 프로그래밍 지원
        - ARC를 통한 자동 메모리 관리, 프로토콜 지향 프로그래밍(POP) 지원
        - 비동기 프로그래밍(Concurrency), 에러 처리, 확장성(Extension) 기능 제공
        - Objective-C보다 성능이 뛰어나며, 최신 Apple 생태계에 최적화된 언어
        - Swift는 안전하고 빠르며, 개발자 친화적인 최신 프로그래밍 언어

- struct와 class의 차이점
    - 개요
        - struct(구조체)와 class(클래스)의 주요 차이점은 값 타입과 참조 타입의 차이
    - 값 타입, 참조 타입
        - Struct: 값 타입
            - 값을 직접 저장하며, 변수에 할당하거나 함수의 인자로 전달될 때 복사됨
            - 각각의 인스턴스가 독립적인 데이터를 가짐
        - Class: 참조 타입
            - 인스턴스를 변수에 할당하거나 함수의 인자로 전달할 때 참조(주소)가 전달됨
            - 같은 인스턴스를 여러 변수에서 공유할 수 있음
        - 예제
          ```Swift
          struct UserStruct {
              var name: String
          }

          class UserClass {
              var name: String
              
              init(name: String) {
                  self.name = name
              }
          }

          var struct1 = UserStruct(name: "Alice")
          var struct2 = struct1  // 값 복사
          struct2.name = "Bob"

          var class1 = UserClass(name: "Alice")
          var class2 = class1  // 참조 전달
          class2.name = "Bob"

          print(struct1.name)  // "Alice" (독립적인 값), struct2.name을 Bob으로 변경해도 struct1의 name은 변경되지 않음
          print(class1.name)   // "Bob" (같은 객체 참조), class2.name을 변경했는데 class1.name 도 변경, 참조관계
          ```
    - 메모리 관리
        - Struct
            - 스택 메모리에 저장됨
            - 빠르고 자동으로 메모리에서 제거됨(ARC 영향 없음)
        - Class
            - 힙 메모리에 저장됨 (자바와 동일)
            - ARC(Automatic Reference Counting)에 의해 메모리를 관리함
            - 순환 참조(Retain Cycle)가 발생할 수 있음
    - 상속(Inherirance) 
        - Struct 상속 불가능
        - Class 상속 가능
    - Mutability (불변성)
        - Struct
            - let 키워드로 선언된 struct 인스턴스는 내부 속성도 변경 불가
            - 내부 속성 변경하려면 mutating 키워드 사용 필수
              ```Swift
              struct Car {
                  var model: String
                  // mutating keyword
                  mutating func changeModel(to newModel: String) {
                      self.model = newModel
                  }
              }
              var myCar = Car(model: "BMW")
              myCar.changeModel(to: "Tesla") 
              ```
        - Class
            - let 키워드로 선언된 class 인스턴스라도 내부 속성 변경 가능
    - Protocol Conformance
        - Struct & Class 모두 프로토콜을 채택 가능
        - struct는 상속이 불가능하므로 프로토콜 기반의 확장을 더 많이 활용
          ```Swift
          protocol Driveable {
              func drive()
          }
          struct Bike: Driveable {
              func drive() {
                  print("Riding a bike")
              }
          }
          ```
    - 사용 사례
        - Struct 사용
            - 값이 독립적이고 변경이 적은 경우
            - 데이터 중심(모델)
            - SwiftUI에서 ViewModel
            - Codable 데이터 모델 
        - Class 사용 
            - 상태를 변경하거나 공유해야 하는 경우
            - 객체 지향 프로그래밍(OOP) 필요
            - UIKit 기반 UI 코드
            - 네트워크, 데이터베이스, 싱글톤 패턴
    - 결론
        - 값 타입(struct)은 복사되어 독립적인 데이터를 가짐 > SwiftUI 등에서 많이 사용됨
        - 참조 타입(Class)은 참조되어 여러 객체에서 공유됨 > UIKit 기반 개발에 유용
        - Struct가 기본적으로 더 안전하고 성능이 좋음 > 기본적으로 Struct를 사용하고 필요할 때 Class 를 사용
        - Swift에서는 가능하면 Struct를 기본으로 사용하고, 상속이나 참조가 필요할 때 Class를 고려하는 것이 좋은 방향
 
- optional이란 무엇이고, !와 ?의 차이
    - 개요
        - Swift에서 Optional은 값이 있을 수도 있고 없을 수도 있는 변수를 나타내는 타입
    - Optional 정의
        - Optional은 값이 nil일 가능성이 있는 변수나 상수를 안전하게 다루기 위해 사용
        - 일반적으로 ?를 붙여서 선언
    - ?와 !의 차이
        - ? (Optional)
            - ?는 값이 있을 수도 있고 없을 수도 있음을 나타냄
            - 값을 직접 사용하려면 언래핑이 필요합니다.
    - 안전한 언래핑
        ```swift
        var name: String? = "Aiden"
        print(name) // Optional("Aiden")
        // 안전한 언래핑 (Optional Binding)
        if let unwrappedName = name {
            print(unwrappedName) // Aiden
        }
        // Nil-Coalescing Operator (기본값 제공)
        print(name ?? "Unknown") // Aiden
        ```
    - ! (Forced Unwrapping)
        - !는 강제로 언래핑하여 값을 가져오는 방법
        - nil이면 앱이 크래시 발생
    - 언제 ?와 ! 사용
        - ? → 값이 nil일 수도 있는 경우, 안전한 처리 필요
        - ! → 값이 nil이 될 수 없다고 확신하는 경우 (하지만 주의해서 사용해야 함)
            - 가능하면 ?를 사용하고, if let 또는 guard let을 활용하여 안전하게 언래핑하는 것이 좋은 방향

- guard와 if let의 차이
    - 개요
        - Swift에서 옵셔널 바인딩(Optional Binding)을 사용할 때, guard let과 if let은 모두 옵셔널 값을 안전하게 언래핑하는 방법

    - if let
        - if let은 옵셔널 값이 존재할 경우 블록 내에서 안전하게 사용할 수 있도록 바인딩하는 방식
        - 예제
            - 설명
                - if let unwrappedName = name에서 name이 nil이 아닐 경우 unwrappedName에 값을 할당하고, 블록 내에서 사용 가능
	            - nil이면 else 블록이 실행됨.
                - 옵셔널 값이 있을 경우 블록 내에서만 사용 가능.
	            - 중첩된 로직이 많아질 경우 가독성이 떨어질 수 있음.
            - 코드
                ```swift
                let name: String? = "Swift"
                if let unwrappedName = name {
                    print("이름은 \(unwrappedName)입니다.")
                } else {
                    print("이름이 없습니다.")
                }
                ```

    - guard let
        - 옵셔널 값이 없을 경우 즉시 함수를 빠져나가거나 오류를 반환하는 방식
        - 예제
            - 설명
                - guard let을 사용하면 nil일 경우 즉시 return을 실행하여 코드의 흐름을 빠르게 정리할 수 있음.
	            - unwrappedName은 guard let 이후의 코드 블록에서 계속 사용 가능
                - 함수 초기에 nil을 검사하고 조기 반환(Early Exit)하여 가독성을 높임
	            - 이후의 코드에서 unwrappedName을 계속 사용할 수 있음
            - 코드
                ```swift
                func greet(name: String?) {
                    guard let unwrappedName = name else {
                        print("이름이 없습니다.") // `nil`이면 즉시 종료
                        return
                    }
                    
                    print("안녕하세요, \(unwrappedName)님!") // 옵셔널 값이 있을 때 실행
                }
                reet(name: "Swift")     // 출력: 안녕하세요, Swift님!
                greet(name: nil)        // 출력: 이름이 없습니다.
                ```

    - if let vs guard let 선택 기준
        - 옵셔널 값이 존재할 때만 특정 작업을 수행해야 하는 경우: if let 사용
        - 옵셔널 값이 없을 경우 빠르게 종료해야 하는 경우 (Early Exit): guard let 사용
        - 중첩을 줄이고 가독성을 높이고 싶은 경우: guard let 사용
        - else 블록에서 return, throw, fatalError() 등을 호출해야 하는 경우: guard let 사용

    - 결론
        - if let은 옵셔널 값이 존재할 경우 특정 블록 내에서만 사용할 때 적합
        - guard let은 옵셔널 값이 없을 경우 즉시 함수나 루프를 종료할 때 적합 (Early Exit 패턴)
        - Swift에서는 가독성과 유지보수를 고려할 때, 대부분 guard let을 선호하는 경우가 많음

- weak, strong, unowned의 차이는?
- ARC(Automatic Reference Counting)란 무엇인가?
- protocol과 extension의 역할과 활용 사례는?
    - ✅ 1. weak, strong, unowned의 차이점
📌 strong
기본 참조 방식으로 객체의 **참조 카운트(reference count)**를 증가시킨다.

strong으로 선언된 변수는 해당 객체를 소유하고 있으며, 참조가 있는 한 메모리에서 해제되지 않음.

**순환 참조(Circular Reference)**가 생길 수 있음.

swift
복사
편집
class A {
    var b: B? // 기본은 strong
}

class B {
    var a: A? // 이 또한 strong이면 순환 참조 발생 가능
}
📌 weak
참조 카운트를 증가시키지 않음.

객체가 해제되면 해당 변수는 자동으로 nil로 설정됨.

항상 Optional 타입이어야 함 (var x: SomeClass? 형태).

주로 delegate 패턴에 사용됨.

swift
복사
편집
class A {
    weak var delegate: BDelegate? // ARC 순환 방지
}
📌 unowned
weak처럼 참조 카운트를 증가시키지 않지만, 절대 nil이 되지 않음.

객체가 해제되었는데 접근하면 런타임 crash 발생.

주로 초기화 시 서로 참조하는 경우 사용됨.

swift
복사
편집
class A {
    unowned let b: B
    init(b: B) {
        self.b = b
    }
}
✅ 2. ARC (Automatic Reference Counting)
개념
Swift의 메모리 관리 시스템으로, 객체의 생명 주기를 자동으로 관리해주는 시스템.

객체를 참조하는 strong 참조의 카운트가 0이 되면 메모리에서 자동으로 해제된다.

주요 특징
개발자가 직접 retain, release하지 않아도 된다.

하지만 **순환 참조(Circular Reference)**가 생기면 ARC가 객체를 해제하지 못함 → weak 또는 unowned 참조로 해결.

예시
swift
복사
편집
class Person {
    var name: String
    init(name: String) {
        self.name = name
        print("\(name) 생성됨")
    }
    deinit {
        print("\(name) 메모리 해제됨")
    }
}
✅ 3. protocol과 extension의 역할 및 활용 사례
📌 protocol이란?
기능 명세서로, 어떤 속성과 메서드를 구현해야 하는지 정의함.

클래스, 구조체, 열거형 모두 채택 가능.

**의존성 역전 원칙(DIP)**이나 delegate 패턴, mock 테스트에 자주 사용됨.

swift
복사
편집
protocol Flyable {
    func fly()
}

class Bird: Flyable {
    func fly() {
        print("날아간다")
    }
}
📌 extension이란?
기존 타입(클래스, 구조체 등)에 기능을 추가할 수 있음.

상속 없이도 기존 타입을 확장할 수 있어서 유용함.

swift
복사
편집
extension Int {
    func squared() -> Int {
        return self * self
    }
}
print(5.squared()) // 25
📌 함께 사용하는 사례
프로토콜을 정의하고, 그 프로토콜에 대한 기본 구현을 extension으로 제공할 수 있음.

swift
복사
편집
protocol Greetable {
    func greet()
}

extension Greetable {
    func greet() {
        print("Hello!")
    }
}

struct Person: Greetable {}
let p = Person()
p.greet() // "Hello!"
✨ 요약 정리
항목	설명
strong	기본 참조 방식, 참조 카운트 증가
weak	참조 카운트 증가 X, 자동 nil, Optional 필수
unowned	참조 카운트 증가 X, nil 허용 X, 해제 후 접근 시 crash
ARC	자동으로 메모리 관리, 참조 카운트 기반
protocol	공통 인터페이스 정의, 추상화 가능
extension	기존 타입 확장, 기능 추가, 프로토콜 기본 구현 가능


- enum과 associated value를 활용하는 방법은?
- closure란 무엇이며, 캡처 리스트([weak self])를 사용하는 이유는?
- UIKit과 SwiftUI의 차이는?
    - ✅ 1. enum과 associated value의 활용
개념
Swift의 enum은 단순한 열거형 이상의 기능을 한다. associated value를 사용하면 각 케이스에 값을 동반해서 저장할 수 있다. 이를 통해 하나의 enum으로 다양한 형태의 데이터를 표현할 수 있다.

주요 활용
상태 표현 (예: 로딩, 성공, 실패)

네트워크 결과 처리

UI 상태 관리

예시: 네트워크 응답 처리
swift
복사
편집
enum NetworkResult {
    case success(data: Data)
    case failure(error: Error)
    case loading
}
위처럼 정의하면, 상태에 따라 각기 다른 정보를 담을 수 있고, switch문을 통해 안전하게 분기 처리 가능하다.

swift
복사
편집
func handle(result: NetworkResult) {
    switch result {
    case .success(let data):
        print("데이터 수신 완료: \(data)")
    case .failure(let error):
        print("에러 발생: \(error.localizedDescription)")
    case .loading:
        print("로딩 중...")
    }
}
장점
가독성이 좋고, 안전하게 분기 처리를 할 수 있음

복잡한 상태를 하나의 타입으로 표현할 수 있어 상태 모델링에 강력

✅ 2. 클로저(Closure)와 [weak self] 캡처 리스트
클로저란?
클로저는 익명 함수 또는 코드 블록으로, 변수나 상수에 할당하거나 인자로 전달할 수 있는 기능이다. Swift에서는 클로저를 통해 비동기 처리, 콜백, 필터링 등 다양한 기능을 구현할 수 있다.

swift
복사
편집
let greet = { (name: String) in
    print("Hello, \(name)")
}
greet("Swift") // Hello, Swift
클로저의 캡처 동작
클로저는 자신이 선언된 외부의 변수나 객체를 참조할 수 있는데, 이 때 클로저는 해당 객체를 **강하게 참조(strong reference)**하게 된다.

이로 인해 클래스 내에서 클로저가 self를 참조하고 있고, 클로저가 클래스 인스턴스에 의해 유지되고 있다면 **순환 참조(메모리 누수)**가 발생할 수 있다.

[weak self] 사용 이유
이를 방지하기 위해 캡처 리스트를 사용하여 self를 **약한 참조(weak)**로 지정한다. 이렇게 하면 클로저 내부에서 self는 선택적 값이 되고, 메모리 누수를 방지할 수 있다.

swift
복사
편집
class ViewController: UIViewController {
    var name = "iOS"

    func fetchData(completion: @escaping () -> Void) {
        someAsyncMethod { [weak self] in
            guard let self = self else { return }
            print("Hello, \(self.name)")
            completion()
        }
    }
}
[unowned self]는 언제?
self가 항상 존재한다고 확신할 수 있을 때 사용

만약 해제된 후 접근하면 크래시 발생하므로 주의가 필요

✅ 3. UIKit과 SwiftUI의 차이
UIKit
기존의 iOS 앱 UI 프레임워크

Imperative(명령형) 방식으로, View를 생성하고 속성을 수동으로 설정함

UIView, UIViewController 기반

Interface Builder(스토리보드)와 코드 둘 다 사용 가능

더 많은 레거시 시스템 및 라이브러리와 호환

런타임에서 유연한 제어 가능

swift
복사
편집
let label = UILabel()
label.text = "Hello"
view.addSubview(label)
SwiftUI
Apple이 새롭게 제안한 선언형 UI 프레임워크

Declarative(선언형) 방식으로, 상태(state)에 따라 UI가 자동으로 갱신됨

@State, @Binding, @ObservedObject 등을 통해 UI와 상태를 연결

코드만으로 UI 구성 → 생산성 향상

비교적 최신 버전(iOS 13 이상)부터 지원

swift
복사
편집
struct ContentView: View {
    @State private var name = "SwiftUI"

    var body: some View {
        Text("Hello, \(name)")
    }
}
핵심 차이
UIKit은 수동 제어 중심, SwiftUI는 상태 중심의 선언적 접근

SwiftUI는 구조체 기반이며, 코드의 양이 적고 테스트나 유지보수가 편함

다만 SwiftUI는 최신 OS 버전에서만 완전 지원되므로, 레거시 지원은 UIKit이 우세




- UIView와 CALayer의 차이는?
- Auto Layout과 Constraint의 원리 및 사용 방법은?
- frame과 bounds의 차이는?
    - ✅ 1. UIView와 CALayer의 차이
UIView란?
iOS에서 사용자 인터페이스를 구성하는 기본 단위로, 버튼, 라벨, 이미지 등 모든 UI 요소는 UIView를 상속함.

터치 이벤트를 포함한 사용자 상호작용, 레이아웃 설정, 애니메이션 적용 등 다양한 기능을 제공함.

CALayer를 내부적으로 포함하고 있으며, 실제 화면에 표시되는 시각적 요소는 CALayer가 담당한다.

CALayer란?
Core Animation에서 제공하는 그래픽 렌더링의 핵심 객체.

시각적인 내용만을 담당하며, 사용자와의 상호작용 기능은 없음.

그림자, 테두리, 모서리 둥글게 처리, 트랜스폼 등 고성능의 시각 효과를 제공함.

UIView의 layer 프로퍼티로 접근 가능.

핵심 차이점
UIView는 인터페이스와 사용자 상호작용 담당, CALayer는 시각적 표현과 고급 그래픽 처리 담당.

UIView는 이벤트를 받고 레이아웃도 담당하지만, CALayer는 단지 픽셀을 렌더링하는 객체에 가까움.

필요 시 CALayer만을 사용하여 고성능 그래픽 작업을 수행할 수도 있음.

✅ 2. Auto Layout과 Constraint의 원리 및 사용 방법
Auto Layout이란?
iOS에서 다양한 화면 크기와 방향에 대응하기 위한 동적 레이아웃 시스템.

뷰들 간의 관계(거리, 크기, 정렬 등)를 **제약조건(Constraint)**으로 설정하여, 런타임에서 적절한 레이아웃을 계산함.

Constraint란?
Auto Layout의 핵심 요소로, 뷰 간의 공간적 관계를 정의하는 규칙.

예: "이 버튼은 왼쪽에서 20pt 떨어져 있어야 한다", "이 라벨은 부모 뷰 중앙에 있어야 한다", "이미지는 너비가 고정되어야 한다" 등.

작동 원리
iOS는 모든 제약 조건을 수학적으로 계산하여 뷰들의 위치와 크기를 결정함.

이 과정은 내부적으로 선형 방정식 시스템을 통해 해결되며, 우선순위(priority)를 부여해 유연한 레이아웃도 가능함.

사용 방법
코드 사용: NSLayoutConstraint, NSLayoutAnchor

스토리보드: 마우스로 드래그하여 제약 설정 가능

SwiftUI에서는 Auto Layout 대신 Frame, Spacer, GeometryReader 등을 활용함

swift
복사
편집
view1.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    view1.leadingAnchor.constraint(equalTo: superview.leadingAnchor, constant: 20),
    view1.trailingAnchor.constraint(equalTo: superview.trailingAnchor, constant: -20),
    view1.topAnchor.constraint(equalTo: superview.topAnchor, constant: 40),
    view1.heightAnchor.constraint(equalToConstant: 100)
])
✅ 3. frame과 bounds의 차이
frame이란?
상위(superview) 기준 좌표계에서 자신의 위치와 크기를 나타냄.

origin은 상위 뷰의 좌상단을 기준으로 한 자신의 시작점 위치

주로 레이아웃 계산 시 사용되며, 화면에서 뷰의 실제 위치를 판단할 때 유용함

swift
복사
편집
print(view.frame) 
// origin: (50, 100), size: (200, 100)
bounds란?
자기 자신의 좌표계 기준에서 자신의 크기와 시작점을 나타냄.

대부분 origin은 (0,0)이며, size는 frame과 동일

내부 콘텐츠를 어떻게 배치할지를 설정할 때 사용됨

swift
복사
편집
print(view.bounds)
// origin: (0, 0), size: (200, 100)
핵심 차이점
frame: 부모 뷰 기준의 위치 + 크기

bounds: 자신의 기준에서의 위치(보통 (0,0)) + 크기

스크롤 처리나 내부 콘텐츠 오프셋 처리 시 bounds의 origin을 조작하는 경우가 있음

예: 이미지 줌, 스크롤 등에서 bounds.origin을 움직여 콘텐츠 위치를 제어할 수 있음.

- TableView와 CollectionView의 차이점과 사용 사례는?
- SwiftUI에서 State, Binding, ObservedObject, EnvironmentObject의 차이는?
- UIKit에서 ViewController 생명주기는?
    - ✅ 1. TableView와 CollectionView의 차이점과 사용 사례
TableView란?
세로 방향으로만 스크롤되는 단일 열(1열) 리스트를 표현할 때 사용.

셀은 한 줄에 하나씩 배치되고, 그룹화된 섹션이나 인덱스를 붙이는 것도 가능함.

단순 리스트형 UI에 적합 (예: 연락처 목록, 설정 화면, 채팅 목록 등)

CollectionView란?
다중 열 또는 다중 행의 아이템들을 유연하게 구성할 수 있음.

셀 레이아웃을 커스터마이징 할 수 있는 UICollectionViewFlowLayout 또는 직접 만든 UICollectionViewLayout을 사용 가능.

격자(grid), 슬라이더, 가로 스크롤, 카드 뷰 등 다양한 UI 구성에 적합.

사용 예시
TableView: 메일 앱 리스트, 채팅 메시지 목록

CollectionView: 사진 갤러리, 상품 카드 리스트, 가로 슬라이더 형태의 추천 콘텐츠

✅ 2. SwiftUI에서 State, Binding, ObservedObject, EnvironmentObject의 차이
@State
뷰 내부에서 사용하는 로컬 상태.

값이 변경되면 뷰가 다시 렌더링됨.

외부에서 접근할 수 없으며 해당 뷰 내부에서만 읽고 쓸 수 있음.

swift
복사
편집
@State private var isOn: Bool = false
@Binding
다른 뷰에서 소유하고 있는 상태를 하위 뷰에서 수정할 수 있도록 전달.

@State 변수와 연결되어 있어 값을 공유함.

swift
복사
편집
Binding<Bool> // 값을 직접 소유하지 않음
@ObservedObject
여러 뷰가 공유할 수 있는 참조 타입 상태.

ObservableObject를 따르는 클래스를 감시하고, 값이 변경되면 뷰를 업데이트함.

swift
복사
편집
class ViewModel: ObservableObject {
  @Published var count: Int = 0
}
@EnvironmentObject
앱 전체 또는 특정 뷰 트리에서 공유되는 전역 상태.

뷰 계층 구조에 주입되어 있어, 복잡한 데이터 전달을 간소화할 수 있음.

주의: 상위 뷰에서 반드시 .environmentObject(...)로 주입해줘야 함.

✅ 3. UIKit에서 ViewController 생명주기
viewDidLoad
뷰 컨트롤러의 뷰가 메모리에 로드될 때 한 번만 호출됨.

초기화 작업, 데이터 바인딩, 하위 뷰 추가 등의 초기 세팅에 사용.

viewWillAppear
뷰가 화면에 나타나기 직전 호출됨.

화면 갱신, 애니메이션 준비, 네비게이션 바 설정 등에 활용.

viewDidAppear
뷰가 화면에 완전히 나타난 후 호출됨.

애니메이션 시작, 트래킹 시작, 비동기 요청 시작 등 타이밍이 중요한 작업에 적합.

viewWillDisappear
뷰가 사라지기 직전 호출됨.

타이머 중지, 알림 제거, 임시 저장 등 정리 작업에 사용됨.

viewDidDisappear
뷰가 완전히 사라진 후 호출됨.

뷰가 메모리에서 내려간 이후 처리가 필요할 경우 사용함.

deinit
뷰 컨트롤러가 메모리에서 해제될 때 호출됨.

리소스 해제, 옵저버 제거 등 클린업 작업 필수.



- SwiftUI에서 View의 생명주기는?
- NavigationView와 TabView의 기본 동작 원리는?
- UIKit에서 커스텀 셀을 만들 때 고려해야 할 사항은?
    - ✅ 1. SwiftUI에서 View의 생명주기
View는 값 타입(Value Type)
SwiftUI의 View는 구조체(struct)이고, 값 타입이기 때문에 상태가 바뀌면 전체 View가 새로 만들어짐.

기존의 뷰를 재사용하는 것이 아니라, 상태(State)에 따라 뷰를 다시 구성하는 방식.

생명주기 흐름
SwiftUI에서는 UIKit처럼 명시적인 viewDidLoad()나 viewWillAppear()는 없음.

대신 다음과 같은 방법으로 상태 변화에 대응함:

onAppear
뷰가 화면에 나타날 때 1회 실행됨.

네트워크 요청, 애니메이션 시작 등에 사용.

onDisappear
뷰가 사라질 때 실행.

타이머 종료, 리소스 해제, 로그 전송 등에 활용.

swift
복사
편집
Text("Hello")
  .onAppear {
      print("Appeared")
  }
  .onDisappear {
      print("Disappeared")
  }
상태에 따른 생명주기 변화
상태가 바뀌면 SwiftUI는 뷰를 다시 계산해서 바뀐 부분만 갱신함.

때문에 @State, @Binding, @ObservedObject, @EnvironmentObject 같은 데이터 드리븐 방식이 중심이 됨.

✅ 2. NavigationView와 TabView의 기본 동작 원리
NavigationView
계층적(스택 기반) 화면 전환을 제공하는 컨테이너.

내부에 NavigationLink를 사용해서 다른 화면으로 push 방식 전환.

백버튼, 내비게이션 바, 타이틀 등을 자동으로 관리해줌.

swift
복사
편집
NavigationView {
    NavigationLink("다음 화면", destination: Text("다음 화면"))
}
SwiftUI 2.0 이상에서는 NavigationStack이 등장하면서 더 세밀한 상태 관리 가능.

TabView
탭 기반의 화면 전환을 제공.

각 탭마다 독립적인 뷰를 가지고 있으며, 하단에 탭 바를 자동 구성.

swift
복사
편집
TabView {
    Text("홈").tabItem { Label("홈", systemImage: "house") }
    Text("설정").tabItem { Label("설정", systemImage: "gear") }
}
selection 바인딩을 통해 현재 선택된 탭을 외부에서 제어할 수 있음.

✅ 3. UIKit에서 커스텀 셀을 만들 때 고려해야 할 사항
셀 재사용(reuse)의 이해
UITableView나 UICollectionView는 성능을 위해 셀을 재사용 큐에 넣고 꺼내서 사용함.

따라서 셀을 초기화할 때만 설정해야 할 것과, 매번 갱신해야 할 것을 구분해야 함.

커스텀 셀 구성 시 핵심 요소
식별자 등록과 연결

register(_:forCellReuseIdentifier:)로 등록하고, dequeueReusableCell(withIdentifier:)로 꺼냄.

레이아웃 정의

UITableViewCell을 상속받아 UILabel, UIImageView 등을 코드 또는 XIB로 배치.

오토레이아웃 제약조건을 정확히 설정해야 화면 깨짐 없음.

초기화 타이밍과 재사용 처리

init(style:reuseIdentifier:) 혹은 awakeFromNib()에서 초기 세팅.

prepareForReuse()에서 이전 상태 초기화 반드시 처리해야 함.

데이터 바인딩 방식

configure(with:) 메서드 패턴을 활용해 외부에서 데이터를 주입.

이미지 로딩 등 비동기 처리 시, 셀 재사용으로 인한 데이터 꼬임 주의.

성능 고려

이미지 로딩, 그림자 효과, 둥근 모서리 등은 성능 이슈 유발 가능.

셀이 많아질 경우 셀 내 draw 오버라이딩 또는 rasterization 고려.

- iOS에서 네트워킹을 처리하는 방법은?
- URLSession을 활용한 네트워킹 구현 방법은?
- JSON을 파싱하는 방법과 Codable의 역할은?
    - ✅ 1. iOS에서 네트워킹을 처리하는 방법
기본 네트워크 프레임워크
iOS에서는 주로 **URLSession**을 사용해 HTTP 통신을 처리.

그 외에도 다음과 같은 고급 프레임워크 또는 라이브러리를 사용할 수 있음:

Alamofire: URLSession 기반의 네트워크 라이브러리. 코드 간결.

Combine: iOS13 이상에서 사용 가능. URLSession.DataTaskPublisher로 반응형 방식 지원.

Async/Await: iOS15 이상부터 비동기 처리 간결하게 가능.

네트워크 통신 흐름
URL 생성

URLRequest 구성 (method, headers 등)

URLSession을 통해 요청 전송

응답 처리 (데이터, 상태 코드, 에러)

JSON 파싱 또는 데이터 가공

✅ 2. URLSession을 활용한 네트워킹 구현 방법
기본 사용 예시
swift
복사
편집
guard let url = URL(string: "https://api.example.com/data") else { return }

let task = URLSession.shared.dataTask(with: url) { data, response, error in
    if let error = error {
        print("❌ 에러 발생: \(error)")
        return
    }

    guard let data = data else {
        print("❌ 데이터 없음")
        return
    }

    // JSON 디코딩
    do {
        let result = try JSONDecoder().decode(MyModel.self, from: data)
        print("✅ 결과: \(result)")
    } catch {
        print("❌ 디코딩 에러: \(error)")
    }
}
task.resume()
POST 요청 예시
swift
복사
편집
var request = URLRequest(url: URL(string: "https://api.example.com/post")!)
request.httpMethod = "POST"
request.setValue("application/json", forHTTPHeaderField: "Content-Type")

let body: [String: Any] = ["key": "value"]
request.httpBody = try? JSONSerialization.data(withJSONObject: body)

URLSession.shared.dataTask(with: request) { data, response, error in
    // 응답 처리
}.resume()
iOS15 이상 async/await 사용 예시
swift
복사
편집
func fetchData() async {
    let url = URL(string: "https://api.example.com/data")!
    do {
        let (data, _) = try await URLSession.shared.data(from: url)
        let result = try JSONDecoder().decode(MyModel.self, from: data)
        print(result)
    } catch {
        print("에러: \(error)")
    }
}
✅ 3. JSON을 파싱하는 방법과 Codable의 역할
JSON 파싱이란?
서버로부터 받은 JSON 데이터를 앱에서 사용 가능한 Swift 타입으로 변환하는 과정.

JSONSerialization을 통해 수동으로 딕셔너리 파싱할 수도 있지만, 대부분은 Codable을 사용해 간결하고 타입 안정적으로 처리.

Codable이란?
Encodable + Decodable 프로토콜을 의미하는 합성 프로토콜.

JSON을 Swift 객체로 변환하거나, 반대로 Swift 객체를 JSON으로 인코딩할 수 있게 함.

예시
swift
복사
편집
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}
swift
복사
편집
let jsonData = ... // 서버에서 받은 Data
do {
    let user = try JSONDecoder().decode(User.self, from: jsonData)
    print(user.name)
} catch {
    print("디코딩 실패: \(error)")
}
커스텀 키 매핑
서버 JSON 키가 Swift 변수명과 다를 경우 CodingKeys를 사용

swift
복사
편집
struct User: Codable {
    let userId: Int
    let userName: String

    enum CodingKeys: String, CodingKey {
        case userId = "id"
        case userName = "name"
    }
}


- 비동기 네트워킹을 처리할 때 async/await과 completion handler의 차이는?
- Core Data와 Realm의 차이는?
- UserDefaults, Keychain, File System의 차이와 각각의 사용 사례는?
    - ✅ 1. async/await vs completion handler
Completion Handler 방식
클로저를 통해 비동기 작업이 완료되면 결과를 넘겨주는 전통적인 방식.

중첩이 많아질수록 코드가 복잡하고 가독성이 떨어질 수 있음. (일명 “콜백 지옥”)

예외 처리 시 Result 타입이나 do-catch 블럭을 사용해야 해서 코드가 장황해짐.

예시

swift
복사
편집
fetchData { result in
    switch result {
    case .success(let data):
        // 처리
    case .failure(let error):
        // 에러 처리
    }
}
async/await 방식
Swift 5.5+ (iOS 15+)부터 도입된 구조.

비동기 코드를 마치 동기 코드처럼 작성 가능해서 가독성이 뛰어남.

do-catch와 함께 사용해 에러 처리도 간결함.

예시

swift
복사
편집
do {
    let data = try await fetchData()
    // 처리
} catch {
    // 에러 처리
}
차이 요약
가독성: async/await > completion handler

호환성: completion handler는 구버전에서도 사용 가능

복잡한 흐름 제어: async/await이 더 직관적

✅ 2. Core Data vs Realm
Core Data
Apple이 제공하는 공식 ORM 기반 로컬 DB 프레임워크.

객체 그래프 관리와 영속성 저장에 최적화됨.

iCloud 동기화, Undo/Redo, 관계형 모델 등 고급 기능 제공.

설계는 복잡하지만, 애플 생태계와 깊게 통합됨.

Realm
MongoDB에서 만든 경량형 로컬 데이터베이스.

Core Data보다 단순하고 직관적인 문법.

실시간 업데이트, 쓰레드 간 데이터 공유 등에서 유리함.

플랫폼 간 호환성도 높음 (iOS, Android 등)

실전 선택 기준
복잡한 관계형 데이터 + Apple 기술 스택 중심: Core Data

빠른 개발 + 간단한 구조 + 크로스 플랫폼 고려: Realm

✅ 3. UserDefaults vs Keychain vs File System
UserDefaults
앱 설정, 간단한 플래그값 저장에 사용 (예: 로그인 여부, 테마 설정 등)

내부적으로 plist 형태로 저장되며, 보안은 강하지 않음

앱 삭제 시 데이터도 삭제됨

사용 예

swift
복사
편집
UserDefaults.standard.set(true, forKey: "isLoggedIn")
let status = UserDefaults.standard.bool(forKey: "isLoggedIn")
Keychain
보안이 중요한 정보 저장 (예: 토큰, 비밀번호, 인증서 등)

시스템 보안 모듈 기반, 암호화되어 안전하게 저장됨

앱을 삭제해도 데이터는 유지될 수 있음 (조건에 따라)

사용 예 (간단화)

swift
복사
편집
KeychainWrapper.standard.set("abc123", forKey: "authToken")
let token = KeychainWrapper.standard.string(forKey: "authToken")
File System (Document/Cache 디렉토리 등)
이미지, PDF, 로그파일, JSON 데이터 등 대용량 또는 구조화된 파일 저장에 사용

직접 파일을 생성/읽기/삭제해야 하므로 유연성은 높지만 복잡도도 있음

Document는 백업 대상이고, Cache는 시스템이 자동으로 삭제할 수 있음

사용 예

swift
복사
편집
let path = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first!
let fileURL = path.appendingPathComponent("data.json")
try? data.write(to: fileURL)
정리
간단한 설정값: UserDefaults

민감한 정보: Keychain

대용량 파일, 이미지, JSON: File System


- REST API와 GraphQL의 차이는?
- iOS에서 메모리 누수가 발생하는 원인과 해결 방법은?
- DispatchQueue.main.async을 사용하는 이유는?
- Grand Central Dispatch(GCD)와 OperationQueue의 차이는?
    - ✅ 1. REST API와 GraphQL의 차이
REST API
HTTP 메서드(GET, POST, PUT, DELETE)를 사용한 전통적인 API 통신 방식.

각 리소스는 고유한 URL에 매핑됨. 예: /users/1, /posts/12/comments

요청마다 고정된 데이터 구조가 반환됨 → 과다요청(overfetching) 또는 과소요청(underfetching) 문제 발생 가능

장점

간단하고 표준화되어 있으며, 대부분의 서버 및 클라이언트에서 널리 지원됨

단점

필요한 데이터만 요청하기 어려움

여러 리소스를 조합하려면 여러 번 API 호출 필요

GraphQL
Facebook이 만든 쿼리 기반 API 기술로, 하나의 endpoint(/graphql)에 쿼리를 날려 원하는 데이터만 응답받을 수 있음.

클라이언트가 반환될 데이터의 구조를 직접 정의할 수 있음

장점

과다/과소 요청 문제 해결

한 번의 요청으로 여러 데이터 fetch 가능

클라이언트에 최적화된 유연한 데이터 요청이 가능

단점

학습 곡선 있음, 캐시 전략 복잡

서버 구현 복잡도 증가 가능

✅ 2. iOS에서 메모리 누수(Memory Leak)의 원인과 해결 방법
주요 원인
강한 순환 참조(Strong Reference Cycle): 서로가 서로를 strong으로 참조할 때 발생 (ViewController ↔ delegate, closure, timer, etc.)

클로저 내부에서 self 캡처: 클로저가 self를 강하게 참조하면서 해제가 안 되는 경우

Timer, NotificationCenter 등록 후 해제 안 함: 타이머나 옵저버가 계속 메모리에 남아있는 경우

해결 방법
[weak self], [unowned self] 캡처 리스트 사용으로 순환 참조 방지

NotificationCenter.removeObserver, timer.invalidate()로 해제 명확히

delegate를 weak 키워드로 선언 (weak var delegate: SomeDelegate?)

✅ 3. DispatchQueue.main.async를 사용하는 이유
개념
iOS 앱은 UI 업데이트는 반드시 메인 스레드(Main Thread) 에서만 수행해야 함.

백그라운드에서 네트워크 요청, 파일 처리 등의 작업 후, UI 반영이 필요할 때 DispatchQueue.main.async로 메인 큐에 UI 작업을 보냄

예시

swift
복사
편집
DispatchQueue.global().async {
    let image = downloadImage()
    DispatchQueue.main.async {
        imageView.image = image // 반드시 메인 쓰레드에서 실행
    }
}
목적
UI 관련 작업을 안전하게 실행

앱이 뻗거나, UI가 갱신되지 않는 현상을 방지

✅ 4. Grand Central Dispatch(GCD) vs OperationQueue
GCD (Grand Central Dispatch)
경량 비동기 처리 도구

DispatchQueue를 통해 동기/비동기 작업을 지정

간단한 코드로 빠르게 쓰레드 작업 구현 가능

장점

코드가 짧고 간단함

성능이 우수하고 lightweight함

단점

작업 취소, 우선순위 조절 등 고급 제어 어려움

OperationQueue
Foundation 프레임워크 기반 큐 시스템

Operation 객체를 통해 작업 정의, OperationQueue에 추가하여 실행

큐의 우선순위, 의존성, 취소 등 세밀한 제어 가능

장점

작업 간 의존성 설정 가능 (operation1.addDependency(operation2))

작업 중간에 취소 가능 (operation.cancel())

단점

GCD보다 코드가 다소 복잡함

- iOS에서 성능 최적화를 위해 고려해야 할 사항은?
- 앱의 메모리 사용량을 줄이는 방법은?
- Instruments에서 메모리 릭을 탐지하는 방법은?
- 스레드 안전성을 보장하는 방법은?
    - ✅ 1. iOS에서 성능 최적화를 위해 고려해야 할 사항
레이아웃 최적화
Auto Layout 제약 조건을 너무 복잡하게 사용하지 않도록 주의

복잡한 뷰 계층(View Hierarchy)을 피하고, setNeedsLayout() / layoutIfNeeded() 호출 최소화

이미지 최적화
이미지 크기를 UI에 맞게 줄이고, 필요 시 압축 또는 @2x, @3x를 적절히 사용

메모리에 오래 유지될 이미지는 캐시 사용 (NSCache or third-party)

메모리 관리
사용하지 않는 뷰, 객체를 즉시 해제

strong reference cycle 방지 (특히 delegate, closure)

비동기 처리
무거운 작업은 반드시 Background Queue에서 처리하고, UI 작업은 Main Queue에서만 수행

테이블/컬렉션 뷰 최적화
셀 재사용 (dequeueReusableCell) 철저히

비동기 이미지 로딩 + 캐싱 적용

heightForRowAt에서 복잡한 계산 지양

✅ 2. 앱의 메모리 사용량을 줄이는 방법
리소스 최적화
이미지, 영상, 사운드 등 리소스는 필요한 시점에만 로드하고, 사용 후 메모리에서 제거

데이터 구조 개선
Array, Set, Dictionary 등 컬렉션은 필요 이상으로 할당되지 않도록 관리

중복 객체 사용 줄이기

ARC(자동 참조 카운트) 적극 활용
불필요한 strong 참조 대신 weak, unowned 사용

메모리 순환 참조(Strong Reference Cycle)를 차단하여 누수 방지

캐시 관리
캐시가 과도하게 쌓이지 않도록 적절한 NSCache 또는 URLCache 사이즈 설정

✅ 3. Instruments에서 메모리 릭(Memory Leak)을 탐지하는 방법
Instruments > Leak 선택
Xcode에서 Product > Profile을 눌러 Instruments 실행

Leaks 템플릿 선택 후 앱 실행

분석 방법
사용 중인 객체의 그래프와 참조 흐름(Reference Cycles)을 추적 가능

일정 시간이 지난 후에도 해제되지 않은 객체가 있을 경우 Leaks로 표시됨

누수가 의심되는 객체를 더블클릭하면 소스 위치 추적 가능

힙 스냅샷 비교
특정 시점에 스냅샷을 찍고, 이후 상황과 비교해 메모리 차이를 분석

Allocations 도구를 병행해 객체의 생성/해제를 추적 가능

✅ 4. 스레드 안전성을 보장하는 방법
동기화(Synchronization)
DispatchQueue(label:attributes:)를 통한 Serial Queue 사용

DispatchSemaphore, NSLock, NSRecursiveLock 등의 락을 이용해 데이터 보호

Main Thread에서만 접근
UI 업데이트는 반드시 DispatchQueue.main.async로 실행

Model, ViewModel에서 UI 접근은 금지

Atomic한 프로퍼티 처리
@MainActor, @Sendable, @Published, @StateObject 등 Swift 속성 래퍼로 데이터 보호

@Synchronized는 지원되지 않으므로 락 직접 구현 필요

Thread-safe 컬렉션 사용
Swift는 기본적으로 Thread-Unsafe하므로, DispatchQueue.sync/async를 활용하거나 thread-safe 구조 직접 구현



- iOS에서 자주 사용되는 디자인 패턴은?
- MVC, MVVM, VIPER의 차이점과 장단점은?
- 의존성 주입(Dependency Injection)이란?
- Singleton 패턴이 가지는 문제점과 해결 방법은?
    - ✅ 1. iOS에서 자주 사용되는 디자인 패턴
MVC (Model-View-Controller)
Apple이 공식적으로 채택한 전통적인 아키텍처

Model: 데이터와 비즈니스 로직

View: 사용자에게 보여지는 UI

Controller: View와 Model을 연결

단점은 ViewController에 많은 코드가 몰려서 Massive View Controller가 되기 쉬움.

MVVM (Model-View-ViewModel)
View와 Model 사이에 ViewModel을 두어 데이터 바인딩과 UI 로직을 분리

View는 ViewModel을 구독하고 UI 업데이트

SwiftUI와의 궁합이 매우 좋음 (@Published, @StateObject 등과 자연스럽게 연동됨)

장점은 테스트 용이성과 코드 분리. 단점은 구조가 복잡해지고 학습 곡선이 있음.

Singleton
앱 전체에서 하나의 인스턴스만 존재하는 객체 패턴

대표적으로 UserDefaults, URLSession.shared, FileManager.default 등이 있음

상태를 공유해야 할 때 유용하지만, 테스트가 어려워지고 의존성이 강해지는 단점이 있음.

Delegate, Observer, Notification
Delegate: 이벤트를 한 객체가 위임하여 처리

Observer/NotificationCenter: 여러 객체가 하나의 이벤트를 관찰

둘 다 객체 간의 느슨한 연결을 돕는 중요한 패턴

✅ 2. MVC, MVVM, VIPER의 차이점과 장단점
MVC
장점: 단순하고 직관적, 빠른 프로토타이핑 가능

단점: 뷰컨에 로직이 몰리면 유지보수가 힘들어짐

MVVM
장점: ViewModel에 로직을 분리해 UI 코드가 깔끔, SwiftUI와 잘 어울림

단점: 바인딩 로직이 복잡해지고, ViewModel이 지나치게 커질 수 있음

VIPER (View, Interactor, Presenter, Entity, Router)
장점: 역할이 명확히 분리되어 대규모 팀 협업에 적합

단점: 파일과 코드 수가 많아져 관리가 어려움. 오버엔지니어링 우려 있음

✅ 3. 의존성 주입(Dependency Injection)이란?
객체가 직접 의존 객체를 생성하지 않고, 외부에서 주입받는 방식

예시: init(service: LoginService) 형태로 주입

장점:

테스트 용이 (Mock 주입 가능)

유연한 구조 구성 가능 (Loose Coupling)

재사용성과 확장성 향상

종류:

생성자 주입 (가장 흔함)

프로퍼티 주입

메서드 주입

iOS에서는 Swift DI 프레임워크 없이도 충분히 수동 주입 가능하며, 규모가 크면 Swinject 같은 DI 프레임워크 활용 가능.

✅ 4. Singleton 패턴이 가지는 문제점과 해결 방법
문제점
앱 전역에서 상태 공유 → 테스트 어려움

라이프사이클 통제가 어려움

의존성 숨김 → 코드 추적이 어려움

의도치 않은 사이드 이펙트 발생 가능

해결 방법
최대한 의존성 주입으로 대체

싱글톤을 직접 참조하기보다 인터페이스(Protocol) 로 추상화

테스트 시 Mock 객체로 교체 가능하게 설계

예시:

swift
복사
편집
protocol AuthServiceProtocol {
    func login()
}

class AuthService: AuthServiceProtocol {
    static let shared = AuthService()
    private init() {}
}

class LoginViewModel {
    let authService: AuthServiceProtocol
    init(authService: AuthServiceProtocol) {
        self.authService = authService
    }
}
→ 실제 사용 시에는 AuthService.shared 주입, 테스트 시에는 Mock 주입



- Combine 프레임워크를 활용하는 방법은?
- Swift에서 Delegate 패턴과 Notification 패턴의 차이는?
- iOS 앱을 App Store에 배포하는 과정은?
- Ad Hoc, Enterprise, App Store 배포 방식의 차이는?
    - ✅ 1. Combine 프레임워크를 활용하는 방법
Combine은 Apple에서 만든 반응형 프로그래밍 프레임워크로, 비동기 이벤트 스트림을 선언적 방식으로 처리할 수 있게 해준다. SwiftUI와 궁합이 뛰어남.

핵심 개념
Publisher: 값을 비동기적으로 발행하는 객체 (Just, URLSession.DataTaskPublisher, NotificationCenter.publisher)

Subscriber: Publisher의 값을 구독하고 처리하는 객체 (sink, assign)

Operators: 값의 흐름을 변경하거나 조합 (map, filter, debounce, combineLatest 등)

@Published: 속성을 퍼블리셔로 만들어줌

@StateObject, @ObservedObject: Combine 기반 객체의 변화를 SwiftUI에서 감지하게 함

예제
swift
복사
편집
class MyViewModel: ObservableObject {
    @Published var searchText: String = ""
    private var cancellables = Set<AnyCancellable>()

    init() {
        $searchText
            .debounce(for: .milliseconds(300), scheduler: RunLoop.main)
            .sink { text in
                print("Search text changed: \(text)")
            }
            .store(in: &cancellables)
    }
}
✅ 2. Delegate 패턴과 Notification 패턴의 차이
Delegate 패턴
1:1 통신 구조

한 객체가 특정 이벤트를 다른 객체에게 위임

명확한 관계, 강한 타입 안정성

예: UITableViewDelegate, UITextFieldDelegate

Notification 패턴
1:N 통신 구조

하나의 이벤트에 대해 여러 객체가 관찰자로 등록 가능

느슨한 결합 가능하지만, 디버깅이 어려울 수 있음

예: NotificationCenter.default.post(name:), .addObserver(...)

선택 기준
이벤트 수신자가 명확하고 하나라면 Delegate

여러 객체에게 동시에 알릴 필요가 있거나 독립적인 컴포넌트 간 소통이면 Notification

✅ 3. iOS 앱을 App Store에 배포하는 과정
1단계: 준비
Xcode 프로젝트 설정 (버전, 번들 ID, 서명, 배포 대상 등)

App Store Connect 계정 필요 (Apple Developer Program 등록)

2단계: 아카이브 생성
Xcode에서 Product > Archive 메뉴 사용

아카이브가 완료되면 Organizer 창에서 확인 가능

3단계: 배포
Distribute App 선택 → App Store Connect → 자동 또는 수동 서명

업로드 후, App Store Connect에서 빌드 수동 선택

4단계: 메타데이터 입력
앱 이름, 설명, 키워드, 스크린샷 등 작성

5단계: 리뷰 제출
내부 테스트 후 Submit for Review

심사 통과 후 App Store에 게시됨

✅ 4. Ad Hoc, Enterprise, App Store 배포 방식의 차이
App Store 배포
일반 사용자가 App Store를 통해 앱을 다운로드

Apple 심사를 반드시 통과해야 함

일반 소비자용 앱에 적합

Ad Hoc 배포
최대 100대의 등록된 테스트 디바이스에 설치 가능

테스트 목적 (TestFlight 이전 방식)

UDID 등록 필요

Enterprise 배포
Apple Developer Enterprise Program 가입 필요

내부 조직 전용 앱 배포에 사용 (직원용 앱 등)

심사 없이 자체 배포 가능하지만 보안 및 배포 관리 책임이 있음

- iOS 앱의 테스트 종류(Unit Test, UI Test 등)와 활용 방법은?
- XCTest에서 UI 테스트를 구현하는 방법은?
- TestFlight를 이용한 베타 테스트 방법은?
- Crashlytics를 활용하여 크래시 로그를 분석하는 방법은?
    - ✅ 1. iOS 앱의 테스트 종류와 활용 방법
iOS에서 테스트는 주로 3가지 레벨로 나눠 수행할 수 있어.

Unit Test (단위 테스트)
목적: 하나의 함수, 클래스, 컴포넌트가 정확히 동작하는지 검증

프레임워크: XCTest

예시: ViewModel에서 데이터 필터링 로직, 계산 로직 테스트

UI Test (사용자 인터페이스 테스트)
목적: 앱의 실제 UI 흐름을 자동화하여 사용자 관점의 시나리오를 검증

도구: XCTest UI Test, XCUITest

예시: 로그인 화면에서 버튼을 누르고 결과 화면이 뜨는지 확인

Snapshot Test / Visual Regression Test
목적: UI가 변경되지 않았는지 이미지 비교로 검증

도구: iOSSnapshotTestCase, SnapshotTesting

Integration Test
목적: 여러 컴포넌트가 함께 동작할 때 오류 없는지 검증 (e.g., ViewModel ↔ API ↔ DB)

✅ 2. XCTest에서 UI 테스트를 구현하는 방법
XCTest를 활용한 UI 테스트는 XCUITest를 기반으로 하며, 실제 사용자 조작을 시뮬레이션함.

기본 구성
⌘ + U 또는 Xcode > New UI Test Target 생성

UI 요소를 accessibilityIdentifier로 구분

테스트 함수는 test로 시작하는 함수명 사용

예제
swift
복사
편집
func testLoginButtonExists() {
    let app = XCUIApplication()
    app.launch()

    let loginButton = app.buttons["loginButton"]
    XCTAssertTrue(loginButton.exists)
    loginButton.tap()

    let welcomeText = app.staticTexts["welcomeMessage"]
    XCTAssertTrue(welcomeText.exists)
}
핵심 팁
waitForExistence(timeout:)을 활용해 비동기 UI 처리 가능

안정적인 테스트를 위해 accessibilityIdentifier 적극 활용

✅ 3. TestFlight를 이용한 베타 테스트 방법
TestFlight는 Apple이 제공하는 공식 베타 배포 플랫폼으로, 외부 테스터에게 앱을 배포하고 피드백을 받을 수 있어.

사용 절차
Xcode에서 Archive → Distribute → App Store Connect 업로드

App Store Connect 접속 → 앱 선택 → TestFlight 탭

Internal Testers: 팀원에게 바로 배포 (심사 불필요)

External Testers: 이메일 초대 / 공개 링크 생성 가능 (Apple 심사 필요)

테스터가 이메일 또는 링크를 통해 TestFlight 앱에서 설치

이점
실기기 테스트

crash 리포트 자동 수집

앱 피드백 수집

최대 10,000명까지 초대 가능

✅ 4. Crashlytics를 활용하여 크래시 로그를 분석하는 방법
Firebase Crashlytics는 앱에서 발생한 비정상 종료(Crash)를 수집해주며, 구체적인 스택 트레이스를 제공해 디버깅을 도와줌.

기본 사용 방법
Firebase Console에서 프로젝트 생성

앱에 Firebase SDK 및 Crashlytics 추가 (pod 'Firebase/Crashlytics')

GoogleService-Info.plist 프로젝트에 추가

AppDelegate 또는 App 초기화 시 Firebase 설정

swift
복사
편집
import Firebase

FirebaseApp.configure()
크래시 발생 시 자동 보고됨

로그 수동 기록:

swift
복사
편집
Crashlytics.crashlytics().log("사용자 로그인 시도")
사용자 정보 추가:

swift
복사
편집
Crashlytics.crashlytics().setUserID("user_1234")
활용 이점
스택 트레이스를 통해 크래시 발생 위치 추적

버전별 크래시 발생률 확인 가능

특정 유저 ID 기반 분석 가능

Firebase Analytics와 연동되어 사용자 행동 흐름 분석 가능

✅ 정리
UnitTest: 로직 검증

UI Test: 사용자 흐름 자동화

TestFlight: 베타 앱 배포 및 피드백 수집

Crashlytics: 안정성과 사용자 경험 개선을 위한 핵심 도구



- Keychain을 활용하여 민감한 데이터를 저장하는 방법은?
- iOS에서 HTTPS를 강제하는 방법은?
- 앱의 보안을 강화하는 방법은?
- Face ID 및 Touch ID를 활용하는 방법은?


- Dynamic Type과 VoiceOver를 지원하는 방법은?
- iOS 앱에서 사용자 데이터를 보호하기 위한 방법은?
- iOS 최신 버전에서 추가된 주요 기능은?
- Swift Concurrency(async/await)와 기존 GCD의 차이점은?


- Apple Silicon에서 iOS 앱이 어떻게 동작하는가?
- WidgetKit, App Clips, Swift Charts 등 최신 프레임워크를 활용하는 방법은?
- Vision, ARKit, CoreML 등 최신 기술을 프로젝트에서 어떻게 활용할 수 있는가?
- Swift에서 copy-on-write(COW)란? 어떤 자료형에서 활용되는가?


- Swift에서 dynamic 키워드는 언제 사용되는가?
- associatedtype을 활용한 제네릭 프로토콜을 정의하는 방법은?
- Swift의 Property Wrapper를 활용하는 방법과 사용 사례는?
- lazy var와 computed property의 차이점은?


- Swift에서 Equatable, Comparable 프로토콜을 직접 구현하는 방법은?
- async let과 Task {}의 차이점은?
- Swift의 Result<T, Error> 타입을 활용하는 방법은?
- actor와 기존 DispatchQueue.sync를 비교하면 어떤 차이가 있는가?


- Memory Layout<T>을 활용하여 메모리 구조를 확인하는 방법은?
- UIBezierPath와 CAShapeLayer를 활용하여 커스텀 UI를 만드는 방법은?
- UIView 애니메이션에서 spring damping이란 무엇이며 어떻게 활용하는가?
- CALayer에서 shadowPath를 직접 설정하면 성능이 왜 향상되는가?


- SwiftUI에서 PreferenceKey를 활용하는 방법과 사례는?
- GeometryReader의 역할과 성능 최적화 방안은?
- UIKit에서 layoutSubviews()와 draw(_:)의 차이는?
- UIStackView가 실제로 내부에서 어떻게 동작하는가?


- SwiftUI에서 ViewBuilder는 어떻게 작동하는가?
- URLSessionDataTask, URLSessionDownloadTask, URLSessionUploadTask의 차이점은?
- HTTP/2와 HTTP/3의 차이는?
- URLCache를 활용하여 네트워크 응답을 캐싱하는 방법은?


- WebSocket과 HTTP Long Polling의 차이점은?
- multipart/form-data 요청을 iOS에서 처리하는 방법은?
- Core Data의 NSPersistentContainer와 NSPersistentStoreCoordinator의 차이는?
- Core Data의 merge policy 옵션이란?


- Core Data에서 NSFetchedResultsController는 언제 사용되는가?
- Realm을 사용할 때 @Persisted와 기존 List<>의 차이점은?
- CloudKit을 활용한 데이터 동기화의 원리는?
- RunLoop의 개념과 활용 사례는?


- autoreleasepool이 필요한 경우는?
- malloc과 free는 iOS에서 어떻게 동작하는가?
- Object Graph와 Reference Counting의 관계는?
- NSCache와 UserDefaults의 차이는?


- NSOperationQueue와 DispatchQueue의 차이점과 적절한 사용 사례는?
- Swift의 UnsafePointer<T>와 OpaquePointer의 차이는?
- iOS에서 Lazy Loading을 구현하는 방법은?
- NSThread와 pthread의 차이는?


- iOS에서 Backtrace를 활용하여 메모리 릭을 찾는 방법은?
- Clean Architecture를 iOS 프로젝트에서 적용하는 방법은?
- Interactor, Presenter, Repository는 각각 어떤 역할을 하는가?
- RxSwift와 Combine의 차이점은?


- Coordinator Pattern이 필요한 이유는?
- Dependency Injection을 활용하여 ViewController의 의존성을 관리하는 방법은?
- SOLID 원칙을 iOS 개발에서 적용하는 방법은?
- Protocol-Oriented Programming(POP)이 객체 지향 프로그래밍(OOP)과 비교했을 때 가지는 장점은?


- Higher-Order Function이란 무엇이며 Swift에서 어떤 예제가 있는가?
- State Restoration이란 무엇이며, iOS에서 어떻게 적용하는가?
- Bitcode의 개념과 iOS 앱 빌드 과정에서의 역할은?
- dSYM 파일의 역할과 Crash 로그 분석 방법은?


- Xcode의 Build Phases에서 Run Script를 활용하는 방법은?
- XCTestCase에서 setUp()과 tearDown()은 각각 언제 호출되는가?
- iOS에서 Fastlane을 활용한 자동 배포 방법은?
- iOS 앱의 크기를 최적화하는 방법은?


- In-App Purchase에서 Receipt Validation을 처리하는 방법은?
- iOS의 On Demand Resources (ODR)란?
- Xcode Cloud와 기존 CI/CD 도구(GitHub Actions, Bitrise) 비교 분석
- App Transport Security (ATS)란?


- Keychain을 활용하여 민감한 데이터를 저장할 때 고려해야 할 사항은?
- iOS에서 Secure Enclave를 활용하는 방법은?
- JWT (JSON Web Token)을 활용한 인증 방식은?
- Biometric Authentication을 적용할 때 LocalAuthentication 프레임워크의 역할은?


- 앱이 Background 상태에서 네트워크 통신을 보안적으로 유지하는 방법은?
- iOS Sandboxing이란?
- iOS Privacy Manifest와 앱 개인정보 보호 정책 작성 방법은?
- Swift 5.9에서 추가된 주요 기능은?


- Swift Concurrency의 structured concurrency 개념이 무엇인가?
- Metal을 활용하여 iOS 앱에서 그래픽 성능을 최적화하는 방법은?
- ARKit과 RealityKit의 차이점은?
- iOS에서 Passkeys를 지원하는 방법은?


- Live Activities를 구현하는 방법은?
- Dynamic Island에서 실시간 업데이트를 처리하는 방법은?
- Swift의 주요 특징과 Objective-C와의 차이점은 무엇인가요?
- iOS 앱의 생명주기에 대해 설명해주세요.


- SwiftUI와 UIKit의 차이점은 무엇인가요?
- Swift의 ARC(Automatic Reference Counting)와 메모리 관리 방법을 설명해주세요.
- Combine 프레임워크 사용 경험을 설명해주세요.
- Swift의 Result Builder와 Property Wrapper의 사용 사례를 설명해주세요.


- Swift의 Concurrency 모델(Async/Await)에 대해 설명해주세요.
- Swift에서 struct와 class의 차이점은?
- Swift에서 Combine과 RxSwift의 차이점은?
- Swift에서 Result 타입을 사용하는 이유는?


- Swift의 Codable과 JSONSerialization의 차이점은?
- SwiftUI에서 @State, @ObservedObject, @EnvironmentObject의 차이점은?
- SwiftUI에서 LazyVStack과 LazyHStack을 사용하는 이유는?
- Swift의 guard와 if let의 차이는?


- ARC(Automatic Reference Counting)란 무엇인가?
- Swift의 Protocol-Oriented Programming(POP)이란 무엇인가?
- Swift의 Result 타입은 어떤 용도로 사용되는가?
- Grand Central Dispatch(GCD)와 OperationQueue의 차이점은?


- UIViewController의 라이프사이클을 설명하라.
- weak와 unowned의 차이는?
- Swift의 Combine 프레임워크를 사용해본 경험이 있는가?
- iOS의 Core Data와 Realm의 차이점과 성능 비교는?


- Swift의 Property Wrappers(@State, @Binding, @ObservedObject)는 어떻게 동작하는가?
- Swift에서 Key-Value Observing (KVO)의 동작 방식과 한계는?
- iOS의 SceneDelegate와 AppDelegate의 차이점과 역할은?
- Combine 프레임워크에서 Publisher와 Subscriber의 동작 방식은?


- Swift의 Memory Management와 ARC에서 Retain Cycle을 방지하는 방법은?
- iOS 앱에서 Background Execution이 필요한 경우와 구현 방식은?
- Swift에서 Result Builder를 활용하는 방법은?
- Swift에서 some 키워드는 언제 사용되는가?


- Noncopyable 프로토콜이 무엇이며, 언제 활용할 수 있는가? (Swift 5.10 이상)
- Swift에서 defer 문을 활용하는 경우는?
- Swift에서 Codable과 Decodable, Encodable의 차이는?
- Swift에서 KeyPath와 @dynamicMemberLookup을 활용하는 방법은?


- Swift에서 Set과 Array의 차이점은?
- Hashable 프로토콜을 직접 구현하는 방법과 그 용도는?
- Swift의 Lazy Sequence는 무엇이며 언제 사용하는가?
- Swift에서 Mirror API를 활용하여 런타임에 객체 정보를 조회하는 방법은?


- Swift의 SPM(Swift Package Manager)을 활용하여 모듈을 관리하는 방법은?
- Swift에서 Opaque Types(some keyword)과 Generics의 차이는?
- Swift에서 throw, rethrows, try?, try!의 차이점은?
- Swift에서 Equatable과 Identifiable을 구현해야 하는 경우는?


- Swift에서 Capture List([weak self])을 사용해야 하는 경우는?
- Swift에서 @autoclosure의 역할과 활용 방법은?
- Swift에서 Copy-on-Write(COW)가 적용되는 자료형과 동작 방식은?
- Swift에서 Memory Layout<T>을 활용하여 메모리 구조를 확인하는 방법은?


- Swift에서 UnsafePointer<T>와 OpaquePointer의 차이는?
- autoreleasepool을 사용해야 하는 경우는?
- Swift의 Pointer와 Buffer를 활용하여 성능을 최적화하는 방법은?
- Swift의 Concurrency (비동기 프로그래밍)


- async let과 Task {}의 차이점은?
- TaskGroup과 AsyncStream을 활용하여 비동기 작업을 처리하는 방법은?
- Global Actor(@MainActor)와 Detached Task의 차이점은?
- Swift에서 CheckedContinuation을 활용하여 기존의 Completion Handler 패턴을 변환하는 방법은?


- Swift의 Task Priority 설정이 실행 성능에 미치는 영향은?
- Swift에서 Continuations을 활용한 비동기 API 래핑 방법은?
- Swift에서 Parallel Execution을 효율적으로 처리하는 방법은?
- LazyVStack과 LazyHStack의 차이점과 성능 최적화 사례는?


- SwiftUI에서 PreferenceKey를 활용하는 방법과 사례는?
- GeometryReader를 사용할 때 성능을 최적화하는 방법은?
- UIHostingController와 UIViewControllerRepresentable의 차이는?
- UIViewController와 SwiftUI View 간 데이터 바인딩을 최적화하는 방법은?


- SwiftUI에서 Transaction과 Animation의 차이는?
- SwiftUI에서 @StateObject와 @ObservedObject의 차이는?
- Swift에서 multipart/form-data 요청을 처리하는 방법은?
- iOS에서 NSURLSessionWebSocketTask을 활용하여 WebSocket을 처리하는 방법은?


- iOS에서 URLSession의 HTTP/2 및 HTTP/3 지원 여부와 그 차이는?
- iOS에서 GraphQL을 활용한 네트워크 요청을 처리하는 방법은?
- CoreData와 Realm에서 Schema Migration을 수행하는 방법은?
- UserDefaults, Keychain, File System, CloudKit의 차이점과 사용 사례는?


- URLSessionDataTask, URLSessionDownloadTask, URLSessionUploadTask의 차이는?
- iOS 앱에서 메모리 사용량을 줄이는 방법은?
- RunLoop의 개념과 활용 사례는?
- iOS에서 Background Task를 활용하여 네트워크 요청을 최적화하는 방법은?


- CALayer에서 shadowPath를 직접 설정하면 성능이 왜 향상되는가?
- iOS에서 프레임 드롭(Frame Drop)을 방지하기 위한 성능 최적화 기법은?
- NSCache와 UserDefaults의 차이는?
- Image Rendering Mode를 설정하면 성능이 어떻게 최적화되는가?


- Core Animation과 Metal을 활용하여 UI 성능을 최적화하는 방법은?
- iOS 앱을 App Store에 배포하는 과정을 설명하시오.
- Xcode Cloud와 기존 CI/CD 도구(GitHub Actions, Bitrise)의 차이는?
- TestFlight를 활용한 베타 테스트 프로세스는?


- iOS에서 Fastlane을 활용하여 자동 배포를 설정하는 방법은?
- App Transport Security (ATS)란?
- Bitcode가 iOS 앱 배포 과정에서 가지는 역할은?
- iOS에서 Secure Enclave를 활용하는 방법은?


- iOS 앱에서 Face ID 및 Touch ID를 활용하는 방법은?
- iOS에서 JWT (JSON Web Token)을 활용한 인증 방식은?
- App Privacy Manifest와 앱 개인정보 보호 정책을 작성하는 방법은?
- iOS Sandboxing이란?


- iOS 앱에서 In-App Purchase의 보안을 강화하는 방법은?
- iOS 최신 버전에서 추가된 주요 기능은?
- Live Activities를 구현하는 방법은?
- Dynamic Island에서 실시간 업데이트를 처리하는 방법은?


- iOS에서 Passkeys를 지원하는 방법은?
- Swift 5.10에서 추가된 새로운 기능은?
- RealityKit과 ARKit의 차이는?


- iOS에서 Metal을 활용하여 그래픽 성능을 최적화하는 방법은?
- WidgetKit을 활용하여 iOS 위젯을 만드는 방법은?