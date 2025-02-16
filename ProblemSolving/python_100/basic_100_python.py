# 6001, 출력 연습
print("Hello")

# 6002, 출력 연습
print("Hello World")

# 6003, 출력 연습
print("Hello")
print("World")

# 6004, 출력 연습
print("'Hello'")

# 6005, 출력 연습
print('"Hello World"')

# 6006, 출력 연습
print("\"!@#$%^&*()\'")

# 6007, 출력 연습
print("\"C:\\Download\\\'hello\'.py\"")

# 6008, 출력 연습
print("print(\"Hello\\nWorld\")")

# 6009, 문자 1개 입력받아 그대로 출력하기
value=input()
print(value)

# 6010, 정수 1개 입력받아 int로 변환하여 출력하기
value=input()
value=int(value)
print(value)

# 6011, 실수 1개 입력받아 그대로 출력하기
f=input()
f=float(f) # convert to float
print(f)

# 6012, 정수 2개 입력받아 그대로 출력하기
a=input()
b=input()
a=int(a) # convert to integer
b=int(b)
print(a)
print(b)

# 6013, 문자 2개 입력받아 순서 바꿔 출력하기
a=input()
b=input()
print(b)
print(a)

# 6014, 실수 1개 입력받아 3번 출력하기
f=input()
f=float(f) # convert to float
print(f)
print(f)
print(f)

# 6015, 정수 2개 입력받아 그대로 출력하기
a,b=input().split()
a=int(a)
b=int(b)
print(a)
print(b)

# 6016, 문자 2개 입력받아 순서 바꿔 출력하기
a,b=input().split()
print(b,a)

# 6017, 문장 1개 입력받아 3번 출력하기
s=input()
print(s,s,s)

# 6018 (sep -> separator), 시간 입력받아 그대로 출력하기
a,b=input().split(":")
print(a,b,sep=":")

# 6019 (f"{x}"), 연월일 입력받아 형태 바꿔 출력하기
y, m, d = input().split('.')
print(f"{d}-{m}-{y}")

# 6020, 주민번호 입력받아 형태 바꿔 출력하기
id_number = input() # 주민번호 입력받기
print(id_number.replace('-', ''))   # '-' 제거 후 출력

# 6021, 단어 1개 입력받아 나누어 출력하기
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 6022, 연월일 입력받아 나누어 출력하기
s = input()
print(s[0:2])   # 0 ~ 1 (2-1)
print(s[2:4])   # 2 ~ 3 (4-1)
print(s[4:6])   # 4 ~ 5 (6-1)

# 6023, 시분초 입력받아 분만 출력하기
time = input()  # 시:분:초 형식으로 입력받기
print(time.split(':')[1])   # ':'을 기준으로 분 추출 후 출력

# 6024, 단어 2개 입력받아 이어 붙이기
w1, w2 = input().split()    # hello world 입력
result = w1 + w2    # hello + world
print(result)   # hello world 출력

# 6025, 정수 2개 입력받아 합 계산하기
a, b = input().split()
c = int(a) + int(b) # convert value and then plus them
print(c)

# 6026, 실수 2개 입력받아 합 계산하기
a = float(input())  # 2개의 실수가 줄을 바꿔 입력된다.
b = float(input())
print(a + b)    # 두 실수의 합 출력

# 6027, 10진 정수 입력받아 16진수로 출력하기
a = input()
n = int(a)      # 입력된 a를 10진수 값으로 변환해 변수 n에 저장
print('%x'% n)  # n에 저장되어 있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력
print('%o'% n)  # n에 저장되어 있는 값을 8진수 소문자 형태 문자열로 출력

# 6028, 10진 정수 입력받아 16진수로 출력하기
a = input()
n = int(a)
print('%X'% n)  # n에 저장되어 있는 값을 16진수 대문자 형태 문자열로 출력

# 6029, 16진 정수 입력받아 8진수로 출력하기
a = input()
n = int(a, 16)   # 입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' % n)  # n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

# 6030, 영문자 1개 입력받아 10진수로 변환하기
n = ord(input()) # 영문자 1개를 입력받아 10진수 유니코드 값으로 출력
print(n)

# 6031, 정수 입력받아 유니코드 문자로 변환하기
c = int(input())
print(chr(c))  #c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다. 
# chr( )는 정수값->문자, ord( )는 문자->정수값 형태로 바꿔주는 서로 반대 방향으로 바꾸어 주는 기능을 한다.

# 6032, 입력된 정수의 부호를 바꾸어 출력, 정수 1개 입력받아 부호 바꾸기
a = input()
a = int(a)
print(-a)

# 6033, 문자 하나 입력 받아 다음 문자 출력하기
# 문자 입력 받기
char = input()

# 다음 문자 출력
# ord(char)는 입력된 문자의 ASCII(유니코드) 값을 반환
print(chr(ord(char) + 1))

# 6034, 정수 2개 입력받아 차 계산하기
a,b = input().split()
a = int(a)
b = int(b)
print(a-b)