# -----------------------------------------------------------------------------------------
# 6001 ~ 6008, 출력 연습
# 분석: 단순 출력, 따옴표 출력 방법, 특수문자 출력, 슬래시 표현
# -----------------------------------------------------------------------------------------
print("Hello")
print("Hello World")
print("Hello")
print("World")
print("'Hello'")
print('"Hello World"')
print("\"!@#$%^&*()\'")
print("\"C:\\Download\\\'hello\'.py\"")
print("print(\"Hello\\nWorld\")")

# -----------------------------------------------------------------------------------------
# 6009 ~ 6017, 입력받고 (변환 후) 출력 연습
# 분석: 입력 받기, 정수/실수 변환, 여러 인자 입력받기 (input().split())
# 분석2: print 문 사용법
# -----------------------------------------------------------------------------------------
value=input()
print(value)

value=input()
value=int(value)
print(value)

f=input()
f=float(f)
print(f)

a=input()
b=input()
a=int(a)
b=int(b)
print(a)
print(b)

a=input()
b=input()
print(b)
print(a)

f=input()
f=float(f)
print(f)
print(f)
print(f)

a,b=input().split()
a=int(a)
b=int(b)
print(a)
print(b)

a,b=input().split()
print(b,a)

s=input()
print(s,s,s)

# -----------------------------------------------------------------------------------------
# 6018 ~ 6019, 출력 연습 (Separator)
# 분석: Separator, print 내 sep 사용, 스트링 안에 값 표현
# -----------------------------------------------------------------------------------------
a,b=input().split(":")
print(a,b,sep=":")

y, m, d = input().split('.')
print(f"{d}-{m}-{y}")

# -----------------------------------------------------------------------------------------
# 6020 ~ 6021, 문자열 내 일부 문자 변환
# 분석: replace 사용법, 문자열 배열 방식 처리
# -----------------------------------------------------------------------------------------
id_number = input()
print(id_number.replace('-', ''))

s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# -----------------------------------------------------------------------------------------
# 6022, 입력 데이터 쪼개기
# 분석: slicing 처리 (:), 슬라이싱 시 범위 개념 (0:2) -> 0, 1 index
# -----------------------------------------------------------------------------------------
s = input()
print(s[0:2])
print(s[2:4])
print(s[4:6])

# -----------------------------------------------------------------------------------------
# 6023, 시분초 입력받아 분만 출력하기
# 분석: 문자열 split 후 배열처럼 사용 방법
# -----------------------------------------------------------------------------------------
time = input()  # 시:분:초 형식으로 입력받기
print(time.split(':')[1])

# -----------------------------------------------------------------------------------------
# 6024, 단어 2개 입력받아 이어 붙이기
# 분석: 문자열 연결 방법, input().split() 시 구분 방식(공백)
# -----------------------------------------------------------------------------------------
w1, w2 = input().split()
result = w1 + w2 
print(result)

# -----------------------------------------------------------------------------------------
# 6025, 정수 2개 입력받아 합 계산하기
# 분석: 정수 변환, 정수 합 표현
# -----------------------------------------------------------------------------------------
a, b = input().split()
c = int(a) + int(b)
print(c)

# -----------------------------------------------------------------------------------------
# 6026, 실수 2개 입력받아 합 계산하기
# 분석: input() 따로 작성 시 동작 방식 파악, 실수 변환, 실수 합 표현
# -----------------------------------------------------------------------------------------
a = float(input())
b = float(input())
print(a + b)

# -----------------------------------------------------------------------------------------
# 6027 ~ 6031, 10/8/16진 데이터 표현
# 분석: 출력 방법 숙지 (print('%x' % value)), 대/소문자 표현법
# 분석2: 유니코드 변환방법(ord), 유니코드 > 문자 변환(chr)
# -----------------------------------------------------------------------------------------
a = input()
n = int(a)
print('%x'% n)
print('%o'% n)

a = input()
n = int(a)
print('%X'% n)

a = input()
n = int(a, 16)
print('%o' % n)

n = ord(input())
print(n)

c = int(input())
print(chr(c))

# -----------------------------------------------------------------------------------------
# 6032, 입력된 정수의 부호를 바꾸어 출력, 정수 1개 입력받아 부호 바꾸기
# 분석: - 부호 사용
# -----------------------------------------------------------------------------------------
a = input()
a = int(a)
print(-a)

# -----------------------------------------------------------------------------------------
# 6033, 입력된 정수의 부호를 바꾸어 출력, 정수 1개 입력받아 부호 바꾸기
# 분석: chr (유니코드 > 문자 변환) / ord (문자 > 유니코드 변환)
# -----------------------------------------------------------------------------------------
char = input()
print(chr(ord(char) + 1))

# -----------------------------------------------------------------------------------------
# 6034, 정수 2개 입력받아 차 계산하기
# 분석: 일반적인 뺄셈
# -----------------------------------------------------------------------------------------
a,b = input().split()
a = int(a)
b = int(b)
print(a-b)

# -----------------------------------------------------------------------------------------
# 참고) 문자열 거꾸로 출력하기
# 분석: [::-1] 슬라이싱 기법 사용, 문자열[start:end:step] 기본 구조 확인
# 분석2: ::-1 -> start, end 생략 -> 처음부터 끝까지의 의미, -1은 역순 의미
# -----------------------------------------------------------------------------------------
string = 'Welcome SJKOding!'
print(string[::-1])

# -----------------------------------------------------------------------------------------
# 참고) 중복 제거하기
# 분석: 중복 없는 Set에 대한 이해
# 분석2: 리스트를 집합 자료형으로 변환, Set은 중복을 자동으로 제거하는 특징
# 분석3: set(temp) -> {1,2,3,4,5}
# 분석4: list(set(temp)) -> [1,2,3,4,5
# 분석5: set은 요소의 순서 보장하지 않으므로 결과 리스트의 순서는 달라질 수 있음
# 참고 정보) 순서보장 희망 시 > list(dict.fromkeys(temp))
# -----------------------------------------------------------------------------------------
temp = [1, 1, 2, 2, 3, 4, 4, 5]
print(list(set(temp)))

# -----------------------------------------------------------------------------------------
# 참고) list(dict.fromkeys(temp)) 의 동작원리
# 분석: dict.fromkeys(iterable)은 주어진 반복 가능 객체의 요소들을
# 딕셔너리의 키로 사용하여 딕셔너리를 생성하는 함수
# 분석2: 딕셔너리는 중복 키 허용하지 않아서 자동으로 중복 제거되며 삽입 순서 유지됨
# 분석3: dict.fromkeys(temp) -> {1: None, 2: None, 3: None, 4: None, 5: None}
# 분석4: None은 기본 할당 값이며 중요하지 않음
# 분석5: dict.fromkeys(temp) -> {1,2,3,4,5}
# 분석6: list(dict.fromkeys(temp)) -> [1,2,3,4,5]
# -----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
# 6035, 실수 2개 입력받아 곱 계산하기
# 분석: float(f1) 방식의 형변환
# -----------------------------------------------------------------------------------------
f1, f2 = input().split()
f1 = float(f1)
f2 = float(f2)
print(f1 * f2)

# -----------------------------------------------------------------------------------------
# 6036, 단어 여러 번 출력하기
# 분석: 문자 * 횟수 연산
# -----------------------------------------------------------------------------------------
w, n = input().split()
n = int(n)
result = w * n
print(result)

# -----------------------------------------------------------------------------------------
# 6037, 문장 여러번 출력하기
# 분석: 문자열 * 횟수 연산, 횟수 먼저 입력 후 줄바꿈 후 여러번 출력할 문장 입력 순
# -----------------------------------------------------------------------------------------
number = input()
myString = input()
print(myString * int(number))

# -----------------------------------------------------------------------------------------
# 6038, 정수 2개 입력받아 거듭제곱 계산하기
# 분석: 거듭제곱근 표현법
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
i1 = int(i1)
i2 = int(i2)
print(i1**i2)

# -----------------------------------------------------------------------------------------
# 6039, 실수 2개 입력받아 거듭제곱 계산하기
# 분석: 거듭제곱근 표현법
# -----------------------------------------------------------------------------------------
f1, f2 = input().split()
print(float(f1)**float(f2))

# -----------------------------------------------------------------------------------------
# 6040, 정수 2개 입력받아 나눈 몫 계산하기
# 분석: 몫 계산 표현법
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
print(int(i1)//int(i2))

# -----------------------------------------------------------------------------------------
# 6041, 정수 2개 입력받아 나눈 나머지 계산하기
# 분석: 나머지 계산 표현법
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
print(int(i1)%int(i2))

# -----------------------------------------------------------------------------------------
# 6042, 실수 1개 입력받아 소숫점이하 자리 변환하기
# 분석: 소숫점이하 자리 변환 방법 (.2f)
# -----------------------------------------------------------------------------------------
val = input()
val = float(val)
result = format(val, ".2f")
print(result)

# -----------------------------------------------------------------------------------------
# 6043, 실수 2개 입력받아 나눈 결과 계산하기
# 분석: ".3f" formatting, 나누기 표현
# -----------------------------------------------------------------------------------------
f1, f2 = input().split()    # f1, f2 = map(float, input().split())
f1 = float(f1)
f2 = float(f2)
result = f1 / f2
# format 함수를 사용하여 result 값을 소숫점 셋째 자리까지 반올림한 문자열로 변환
print("{:.3f}".format(result))  # print(format(result, ".3f"))

# -----------------------------------------------------------------------------------------
# 6044, 정수 2개 입력받아 자동 계산하기 (합,차,곱,몫,나머지,나눈 값)
# 분석: //, / 동작 차리
# 분석2: 파이썬에서 / 연산자는 실제 나눗셈(진짜 나눗셈) 을 수행하며, 결과가 항상 실수(float)로 반환
# 분석3: // 연산자는 바닥 나눗셈(플로어 디비전) 을 수행하는데, 이는 나눗셈 결과에서 소수점 이하를 버리고 
# 가장 작은 정수(또는 float의 경우 소수점 이하가 없는 값)를 반환
# 분석4:
# 7 / 3은 2.3333... (실수 값)을 반환
# 7 // 3은 2를 반환
# -7 / 3은 -2.3333... 반환
# -7 // 3은 -3을 반환 (-2.3333이 -2가 아니라, 바닥값인 -3에 해당)
# -----------------------------------------------------------------------------------------
v1, v2 = input().split()
v1 = int(v1)
v2 = int(v2)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 // v2)
print(v1 % v2)
print(format(v1 / v2, ".2f"))

# -----------------------------------------------------------------------------------------
# 6045, 정수 3개 입력받아 합과 평균 출력하기
# 분석: ".2f", / 사용법
# -----------------------------------------------------------------------------------------
i1, i2, i3 = input().split()
i1 = int(i1)
i2 = int(i2)
i3 = int(i3)
sum = i1 + i2 + i3
average = sum / 3
print(sum, format(average, ".2f"))

# -----------------------------------------------------------------------------------------
# 6046, [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기
# 분석: << 연산, >> 연산
# 추가 설명:
# 2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
# 지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,
# 왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
# 오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,
# 가장 오른쪽에 있는 1비트는 사라짐
# -----------------------------------------------------------------------------------------
v = input()
v = int(v)
print(v << 1)   # 2배 곱 (*2)

# -----------------------------------------------------------------------------------------
# 6047, [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기
# 분석: "a << b", 시프트 연산 시 2의 거듭제곱 연산
# 분석2: 이진법 원리, 1, 2, 4, 8, 16, ... 2024 ...
# -----------------------------------------------------------------------------------------
v1, v2 = input().split()
v1 = int(v1)
v2 = int(v2)
shiftResult = v1 << v2
print(shiftResult)

# -----------------------------------------------------------------------------------------
# 6048, 정수 2개 입력받아 비교하기 (<, >)
# 분석: 비교 연산 결과 True / False
# -----------------------------------------------------------------------------------------
a, b = input().split()
a = int(a)
b = int(b)
result = a < b
print(result)

# -----------------------------------------------------------------------------------------
# 6049, 정수 2개 입력받아 비교하기 (==)
# -----------------------------------------------------------------------------------------
a, b = input().split()
a = int(a)
b = int(b)
print(a == b)

# -----------------------------------------------------------------------------------------
# 6050, 정수 2개 입력받아 비교하기 (<=, >=)
# -----------------------------------------------------------------------------------------
a, b = input().split()
a = int(a)
b = int(b)
print(a <= b)

# -----------------------------------------------------------------------------------------
# 6051, 정수 2개 입력받아 비교하기 (!=)
# -----------------------------------------------------------------------------------------
a, b = input().split()
a = int(a)
b = int(b)
print(a != b)

# -----------------------------------------------------------------------------------------
# 6052, 정수 입력받아 참 거짓 평가하기
# 분석: Python에서 0은 False, 나머지 정수값은 True
# -----------------------------------------------------------------------------------------
i = input()
i = int(i)
print(bool(i))

# -----------------------------------------------------------------------------------------
# 6053, 참 거짓 바꾸기
# 분석: not keyword
# -----------------------------------------------------------------------------------------
i = input()
i = int(i)
print(not bool(i))

# -----------------------------------------------------------------------------------------
# 6054, 둘 다 참일 경우만 참 출력하기
# 분석: and 연산자
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
i1 = int(i1)
i2 = int(i2)
result = bool(i1) and bool(i2)
print(result)

# -----------------------------------------------------------------------------------------
# 6055, 하나라도 참이면 참 출력하기
# 분석: or 연산자
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
i1 = int(i1)
i2 = int(i2)
print(bool(i1) or bool(i2))

# -----------------------------------------------------------------------------------------
# 6056, 참/거짓이 서로 다를 때에만 참 출력하기
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
i1 = int(i1)
i2 = int(i2)
b1 = bool(i1)
b2 = bool(i2)
result = b1 != b2
# print((b1 and (not b2)) or ((not b1) and b2))
print(result)

# -----------------------------------------------------------------------------------------
# 6057, 참/거짓이 서로 같을 때에만 참 출력하기 (True == True or False == False)
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
i1 = int(i1)
i2 = int(i2)
print(bool(i1) and bool(i2) or not bool(i1) and not bool(i2))

# -----------------------------------------------------------------------------------------
# 6058, 둘 다 거짓일 경우만 참 출력하기
# 분석: not A and not B -> not(A or B)
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
i1 = int(i1)
i2 = int(i2)
result = not bool(i1) and not bool(i2)
print(result)

# -----------------------------------------------------------------------------------------
# 6059, 비트단위로 NOT 하여 출력하기
# 분석: ~정수
# -----------------------------------------------------------------------------------------
i1 = input()
i1 = int(i1)
print(~i1)

# -----------------------------------------------------------------------------------------
# 6060, 비트단위로 AND 하여 출력하기
# 분석: a & b
# 분석2: 네트워크에 연결되어 있는 두 개의 컴퓨터가 데이터를 주고받기 위해
# 같은 네트워크에 있는지 아닌지를 판단하는데 사용
# 이러한 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서
# 마스크연산(특정 부분을 가리고 출력하는)을 수행하는 데에도 효과적으로 사용
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
i1 = int(i1)
i2 = int(i2)
print(i1 & i2)

# -----------------------------------------------------------------------------------------
# 6061, 비트단위로 OR 하여 출력하기
# 분석: a | b
# 분석2: 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서도 효과적으로 사용
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
i1 = int(i1)
i2 = int(i2)
print(i1 | i2)

# -----------------------------------------------------------------------------------------
# 6062, 비트단위로 XOR 하여 출력하기
# 분석: a ^ b
# 분석2: 두 장의 이미지가 겹쳐졌을 때 색이 서로 다른 부분만 처리 가능
# 배경이 되는 그림과 배경 위에서 움직이는 그림이 있을 때,
# 두 그림에서 차이만 골라내 배경 위에서 움직이는 그림의 색으로 바꿔주면
# 전체 그림을 구성하는 모든 점들의 색을 다시 계산해 입히지 않고
#보다 효과적으로 그림을 처리할 수 있게 되는 것 -> 비행기 슈팅 게임
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
i1 = int(i1)
i2 = int(i2)
print(i1 ^ i2)

# -----------------------------------------------------------------------------------------
# 6063, 정수 2개 입력받아 큰 값 출력하기
# 분석: result = a if (a>=b) else b
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
i1 = int(i1)
i2 = int(i2)
result = i1 if (i1 >= i2) else i2
print(result)

# -----------------------------------------------------------------------------------------
# 6064, 정수 3개 입력받아 가장 작은 값 출력하기
# 분석: result = a if (a < b) else b
# -----------------------------------------------------------------------------------------
i1, i2, i3 = input().split()
i1 = int(i1)
i2 = int(i2)
i3 = int(i3)
firstResult = i1 if (i1 < i2) else i2
lastResult = firstResult if (firstResult < i3) else i3
print(lastResult)
# or print((i1 if (i1 < i2) else i2) if ((i1 if (i1 < i2) else i2) < i3) else i3)

# -----------------------------------------------------------------------------------------
# 6065, 정수 3개 입력받아 짝수만 출력하기
# 분석: if (a % 2 == 0):
# -----------------------------------------------------------------------------------------
i1, i2, i3 = input().split()
i1 = int(i1)
i2 = int(i2)
i3 = int(i3)
if (i1 % 2 == 0):
    print(i1)
if (i2 % 2 == 0):
    print(i2)
if (i3 % 2 == 0):
    print(i3)

# -----------------------------------------------------------------------------------------
# 6066, 정수 3개 입력받아 짝/홀 출력하기
# 분석: if (a % 2 == 0): ... else: ...
# -----------------------------------------------------------------------------------------
i1, i2, i3 = input().split()
i1 = int(i1)
i2 = int(i2)
i3 = int(i3)
if (i1 % 2 == 0):
    print("even")
else:
    print("odd")
if (i2 % 2 == 0):
    print("even")
else:
    print("odd")
if (i3 % 2 == 0):
    print("even")
else:
    print("odd")

# -----------------------------------------------------------------------------------------
# 6067, 정수 1개 입력받아 분류하기
# 분석: 중첩 if (): else:
# -----------------------------------------------------------------------------------------
v = int(input())
if (v < 0):
    if (v % 2 == 0):
        print('A')
    else:
        print('B')
else:
    if (v % 2 == 0):
        print('C')
    else:
        print('D')

# -----------------------------------------------------------------------------------------
# 6068, 정수 1개 입력받아 평가 출력하기
# 분석: if, elif, else 구문
# -----------------------------------------------------------------------------------------
v = int(input())
if (v >= 90):
    print('A')
elif (v >= 70):
    print('B')
elif (v >= 40):
    print('C')
else:
    print('D')

# -----------------------------------------------------------------------------------------
# 6069, 평가 입력받아 다르게 출력하기
# 분석: input().strip()
# 분석2: input().strip()을 사용하여 사용자 입력 받기
# 분석3: strip()을 사용하면 입력값 앞뒤 공백을 제거하여 오작동 방지 가능
# -----------------------------------------------------------------------------------------
c = input().strip()  # 입력값을 문자열로 저장
if c == 'A':
    print("best!!!")
elif c == 'B':
    print("good!!")
elif c == 'C':
    print("run!")
elif c == 'D':
    print("slowly~")
else:
    print("what?")

# -----------------------------------------------------------------------------------------
# 6070, 월 입력받아 계절 출력하기
# 문제 설명: 12, 1, 2 : winter / 3, 4, 5 : spring / 6, 7, 8 : summer / 9, 10, 11 : fall
# 분석: // 연산자, 수의 규칙 관찰
# -----------------------------------------------------------------------------------------
v = int(input())
v = v // 3
if (v == 4 or v == 0):
    print("winter")
elif (v == 1):
    print("spring")
elif (v == 2):
    print("summer")
else:
    print("fall")

# -----------------------------------------------------------------------------------------
# 6071, 0 입력될 때까지 무한 출력하기
# 분석: while
# -----------------------------------------------------------------------------------------
n = 1   # 초기 while 문 진입을 위해 1로 셋팅
while(n != 0):
    n = int(input())
    if (n != 0):
        print(n)
    else:
        break

# -----------------------------------------------------------------------------------------
# 6072, 정수 1개 입력받아 카운트다운 출력하기 (5,4,3,2,1)
# -----------------------------------------------------------------------------------------
n = int(input())
while(n != 0):
    print(n)
    n -= 1

# -----------------------------------------------------------------------------------------
# 6073, 정수 1개 입력받아 카운트다운 출력하기 (4,3,2,1,0)
# -----------------------------------------------------------------------------------------
n = int(input())
while n > 0:
    n -= 1
    print(n)

# -----------------------------------------------------------------------------------------
# 6074, 문자 1개 입력받아 알파벳 출력하기
# 분석: 문자 -> 정수값 변환: ord()
# 분석2: 정수 -> 문자 변환: chr()
# 분석3: print문 추가 인자, print(..., end=' ') <- 마지막에 줄을 바꾸지 않고 빈칸만 띄움
# 분석4: end='\n'로 작성하거나 생략하면, 값을 출력한 후 마지막(end)에 줄바꿈(newline) 처리
# -----------------------------------------------------------------------------------------
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1

# -----------------------------------------------------------------------------------------
# 6075, 정수 1개 입력받아 그 수까지 출력하기
# 분석: 문제 잘 읽기, 그 수까지이므로 예를 들어 5를 입력했다면, 0,1,2,3,4,5 까지 출력되어져야 함
# -----------------------------------------------------------------------------------------
n = int(input())
i = 0
while i <= n:
    print(i)
    i+=1

# -----------------------------------------------------------------------------------------
# 6076, 정수 1개 입력받아 그 수까지 출력하기
# 분석: 문제 잘 읽기, 그 수까지이므로 예를 들어 5를 입력했다면, 0,1,2,3,4,5 까지 출력되어져야 함
# 분석2: for i in range(...)
# 분석3: range(끝) / range(시작, 끝) / range(시작, 끝, 증감)
# 시작 수는 포함이고, 끝 수는 포함되지 않음 (시작, 끝) -> (0, 5) -> 0,1,2,3,4 까지
# 증감할 수를 작성하지 않으면 +1만큼 증가 처리
# -----------------------------------------------------------------------------------------
n = int(input())
for i in range(n+1) :
  print(i)

# -----------------------------------------------------------------------------------------
# 6077, 짝수 합 구하기
# 분석: += 연산, range(시작, 끝) / 시작값 설정, 짝수/홀수 구하는 방법(i%2==0)
# -----------------------------------------------------------------------------------------
n = int(input())
s = 0
for i in range(1, n+1):
  if i%2==0:
    s += i
print(s)

# -----------------------------------------------------------------------------------------
# 6078, 원하는 문자가 입력될 때까지 반복 출력하기
# 분석: while True, 문자 비교
# -----------------------------------------------------------------------------------------
while True:
    c = input()
    print(c)
    if (c == 'q'):
        break

# -----------------------------------------------------------------------------------------
# 6079, 언제까지 더해야 할까?
# 분석: for i in range(1, n+1), sum 계산법, break
# -----------------------------------------------------------------------------------------
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
    if (sum >= n):
        print(i)
        break

# -----------------------------------------------------------------------------------------
# 6080, 주사위 2개 던지기
# 분석: 중첩 for문, map(int, [])
# -----------------------------------------------------------------------------------------
n,m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)

# -----------------------------------------------------------------------------------------
# 6081, 16진수 구구단 출력하기
# 분석: 중첩 for문, map(int, [])
# -----------------------------------------------------------------------------------------
hex_input = input()
num = int(hex_input, 16)    # 16진수형 정수로 변환
for i in range(1, 16):
    hex_result = format(num * i, "X")   # 16진수 대문자로 변환
    hex_i = format(i, "X")  # 곱하는 i 즉, int 형 i도 대문자형 16진수로 변환
    print(f"{hex_input}*{hex_i}={hex_result}")


# -----------------------------------------------------------------------------------------
# 6082, 3 6 9 게임의 왕이 되자
# 분석: str(), 숫자 -> 문자열 변환
# 분석2: 나머지 연산, 나눗셈 등만 생각해서 풀려고 했으나 잘되지 않았음
# 분석3: 문자열로 변환해서 풀어볼 생각은 하지 않았음
# 코드 설명:
# 1) 사용자 입력을 int(input())으로 받아 정수형으로 변환
# 2) 1부터 n까지 for 반복문을 사용하여 순회
# 3) str(i)를 이용하여 현재 숫자를 문자열로 변환한 뒤 "3", "6", "9"가 포함되어 있는지 확인
# 4) 포함되어 있다면 "X"를 출력하고, 그렇지 않다면 원래 숫자를 출력
# 5) print(..., end=' ')를 사용하여 출력값을 공백(띄어쓰기)로 구분
# -----------------------------------------------------------------------------------------
n = int(input())
for i in range(1, n+1):
    # 숫자를 문자열로 변환하여 3, 6, 9가 포함되어 있는지 확인
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        print("X", end=' ')  # 3,6,9가 포함되면 X 출력
    else:
        print(i, end=' ')  # 그렇지 않으면 숫자 출력

# -----------------------------------------------------------------------------------------
# 6082-개선편, 3 6 9 게임의 왕이 되자 (짝짝 동작도 고려)
# 분석: str(), 숫자 -> 문자열 변환, sum, if c in "..", range(start, end), end 미포함(미만)
# 코드 설명:
# 1) input()은 기본적으로 문자열을 반환하므로, int()를 사용해 정수로 변환
# 2) 1부터 n까지 반복문 실행
# 3) str(i): 숫자 i를 문자열로 변환 → "13", "36" 등, for c in str(i): 문자열을 문자 단위로 순회 → "13"이면 c = "1", c = "3"
# 3-1) if c in "369": c가 "3", "6", "9" 중 하나인지 확인
# 3-2) sum(1 for c in str(i) if c in "369"): "3" 또는 "6" 또는 "9"가 포함될 때마다 1을 더함
# -----------------------------------------------------------------------------------------
n = int(input())
for i in range(1, n+1):
    count = sum(1 for c in str(i) if c in "369")  # 3,6,9 개수 세기
    if count > 0:
        print("X" * count, end=' ')  # 개수만큼 "X" 출력
    else:
        print(i, end=' ')

# -----------------------------------------------------------------------------------------
# 6083, 빛 섞어 색 만들기
# 분석: 중첩 3중 for문, map(int, [])
# 분석2: 출력 결과 > 0,0,0 / 0,0,1 / 0,1,0 / 0,1,1 / 1,0,0 / 1,0,1 / 1,1,0 / 1,1,1
# -----------------------------------------------------------------------------------------
# r, g, b 값 입력받기
r, g, b = map(int, input().split())

# 모든 색 조합 출력
count = 0  # 색 조합 개수 세기
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)  # 색 조합 출력
            count += 1  # 개수 증가

# 총 조합 개수 출력
print(count)

# -----------------------------------------------------------------------------------------
# 6084, 소리 파일 저장용량 계산하기
# 분석: 8비트 > 1바이트, 1키로바이트 > 1024바이트, 1메가바이트 > 1024키로바이트 구조
# 분석2: f string (포매팅 문자열) 사용법, format(value, ".xf")
# -----------------------------------------------------------------------------------------
a,b,c,d = map(int, input().split())
result = a*b*c*d/8/1024/1024
formatted = format(result, ".1f")
print(f"{formatted} MB")

# -----------------------------------------------------------------------------------------
# 6085, 그림 파일 저장용량 계산하기
# 분석: 8비트 > 1바이트, 1키로바이트 > 1024바이트, 1메가바이트 > 1024키로바이트 구조
# 분석2: f string (포매팅 문자열) 사용법, format(value, ".xf")
# -----------------------------------------------------------------------------------------
a,b,c = map(int, input().split())
result = a*b*c/8/1024/1024
formatted = format(result, ".2f")
print(f"{formatted} MB")

# -----------------------------------------------------------------------------------------
# 6086, 거기까지! 이제 그만~
# 분석: 입력된 값까지 1부터 순차적으로 합계를 구하다가 입력된 값과 같거나 커지면 값을 출력한 뒤 loop 중단 처리
# 분석2: for 문 사용법 재확인, for i in range(1, x+1):
# -----------------------------------------------------------------------------------------
v = int(input())
sum = 0
for i in range(1, v+1):
    sum += i
    if (sum >= v):
        print(sum)
        break

# -----------------------------------------------------------------------------------------
# 6087, 3의 배수는 통과
# 분석: continue 키워드 사용법, print(x, end='') <-- end 파라미터 사용법
# -----------------------------------------------------------------------------------------
v = int(input())
for i in range(1, v+1):
    if (i%3==0):
        continue
    print(i, end=' ')

# -----------------------------------------------------------------------------------------
# 6088, 수 나열하기 (등차수열)
# 분석: 등차수열 n번째 항 계산방법 > 시작값 + (n - 1)번째 * 등차값 = n번째 값
# -----------------------------------------------------------------------------------------
# 시작 값(a), 등차(d), n번째 수 입력받기
a, d, n = map(int, input().split())

# 등차수열의 n번째 항 계산
result = a + (n - 1) * d    # 예: 1,4,7,10,13,16

print(result)

# -----------------------------------------------------------------------------------------
# 6088-1, 수 나열하기 (등차수열) - For 문 이용한 방법
# -----------------------------------------------------------------------------------------
# 시작 값(a), 등차(d), n번째 수 입력받기
a, d, n = map(int, input().split())

# 초기값 설정
result = a

# for문을 사용하여 n-1번 등차를 더하기
for _ in range(n - 1):
    result += d

print(result)


# -----------------------------------------------------------------------------------------
# 6089, 수 나열하기 (등비수열)
# -----------------------------------------------------------------------------------------
# 시작 값(a), 등비(r), 원하는 항(n) 입력받기
a, r, n = map(int, input().split())

# 등비수열의 n번째 항 계산
result = a * (r ** (n - 1))

print(result)

# -----------------------------------------------------------------------------------------
# 6089-1, 수 나열하기 (등비수열) - For 문 이용한 방법
# -----------------------------------------------------------------------------------------
# 시작 값(a), 등비(r), 원하는 항(n) 입력받기
a, r, n = map(int, input().split())

# 초기값 설정
result = a

# for문을 사용하여 등비수열 계산
for _ in range(n - 1):
    result *= r  # 등비만큼 곱하기

print(result)

# -----------------------------------------------------------------------------------------
# 6090, 수 나열하기
# -----------------------------------------------------------------------------------------
# 시작 값(a), 곱할 값(m), 더할 값(p), 몇 번째인지를 나타내는 정수(n)가 입력
s, m, p, n = map(int, input().split())
result = s
for _ in range(n-1):    # n-1번 반복하면서 새로운 값을 계산
    result = result * m + p
print(result)

# -----------------------------------------------------------------------------------------
# 6091, 함께 문제 푸는 날
# 분석: 최소공배수, LCM (Least Common Multiple), GCD (Greatest Common Divisor)
# 문제 설명: 같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는, 방문 주기가 공백을 두고 입력된다.
# 문제 설명2: (단, 입력값은 100이하의 자연수이다.)
# -----------------------------------------------------------------------------------------
# 첫번째 풀이 방법: Python 3.9 이상, 최소공배수 사용
# -----------------------------------------------------------------------------------------
import math

# 세 개의 방문 주기 입력 받기
a, b, c = map(int, input().split())

# 최소공배수(Lowest Common Multiple) 계산
result = math.lcm(a, b, c)

# 결과 출력
print(result)

# -----------------------------------------------------------------------------------------
# 두번째 풀이 방법: Python 3.8 이하, 최대공약수, 두 수씩 최소공배수 사용
# -----------------------------------------------------------------------------------------
import math

def lcm(x, y):
    return x * y // math.gcd(x, y)  # 최소공배수 공식: (a * b) / gcd(a, b)

# 세 개의 수 입력
a, b, c = map(int, input().split())

# 세 수의 최소공배수 구하기
result = lcm(lcm(a, b), c)

print(result)

# -----------------------------------------------------------------------------------------
# 세번째 풀이 방법 - 반복문을 통한 최소공배수 구하기
# 모든 숫자의 배수를 찾아 나가는 방식 (비효율적이지만 개념 이해에 유용함)
# 최소공배수를 찾을 때까지 1씩 증가하며 반복
# 큰 숫자가 입력될 경우 성능이 좋지 않음 (시간 복잡도 O(N))
# -----------------------------------------------------------------------------------------
a, b, c = map(int, input().split())

d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1

print(d)

# -----------------------------------------------------------------------------------------
# 참고, for i in range(x) 구문 연습
# -----------------------------------------------------------------------------------------
for i in range(5):  # 인덱스 0 ~ 4까지의 범위
    print(i)  # 0, 1, 2, 3, 4 출력

# -----------------------------------------------------------------------------------------
# 6092, 이상한 출석 번호 부르기
# 분석: 배열 사용 응용
# 문제 설명: 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 문제 설명2: 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
# 문제 설명3: 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.
# -----------------------------------------------------------------------------------------
n = int(input())        # 개수를 입력받아 n에 정수로 저장
a = input().split()     # 공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n) :     # 0부터 n-1까지...
  a[i] = int(a[i])      # a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

d = []                  # d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
for i in range(24) :    # [0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
  d.append(0)           # 각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.

for i in range(n) :     # 번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
  d[a[i]] += 1

for i in range(1, 24) : # 카운트한 값을 공백을 두고 출력
  print(d[i], end=' ')

# 참고
# d = []              #어떤 데이터 목록(list) 을 순서대로 저장하기 위해 아무것도 없는 리스트 변수 만들기
# d.append(값)  #d 리스트의 마지막에 원하는 값을 추가(append)해 넣음 
# d[a[i]] += 1     #2중 리스트 참조 : 만약 a[i]의 값이 1이었다면? d[1] += 1 이 실행되는 것이다. 1번 카운트 1개 증가..


# -----------------------------------------------------------------------------------------
# 6093, 이상한 출석 번호 부르기
# 분석: 배열 사용 응용, for i in range(n-1, -1, -1) 의미
# 문제 설명: 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 문제 설명2: 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
# 문제 설명3: 출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.
# -----------------------------------------------------------------------------------------
n = int(input())        # 개수를 입력받아 n에 정수로 저장
a = input().split()     # 공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n) :     # 0부터 n-1까지...
  a[i] = int(a[i])      # a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

d = []                  # d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
for i in range(24) :    # [0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
  d.append(0)           # 각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.

for i in range(n) :     # 번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
  d[a[i]] += 1

for i in range(n-1, -1, -1) :
  print(a[i], end=' ')

# 참고
# 번호를 부른 순서를 리스트에 순서대로 기록해 두었다가, 기록한 값들을 거꾸로 출력하면 된다.
# range(시작, 끝, 증감) #시작 수는 포함, 끝 수는 포함하지 않음. [시작, 끝)
# range(n-1, -1, -1) #n-1, n-2, ..., 3, 2, 1, 0


# -----------------------------------------------------------------------------------------
# 6094, 이상한 출석 번호 부르기
# 분석: 배열 최소값 구하기, 정렬 함수 사용
# -----------------------------------------------------------------------------------------
n = int(input())        # 개수를 입력받아 n에 정수로 저장
a = input().split()     # 공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n) :     # 0부터 n-1까지...
  a[i] = int(a[i])      # a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

# 부른 출석 번호 중 가장 작은 번호 출력, 아무런 옵션 지정 없을 시 오름차순 자동 정렬
a.sort()
print(a[0])