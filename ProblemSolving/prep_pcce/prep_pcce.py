# 1. 문자 출력
message = "Let's go!"

# 단순하게 개행 문자를 사이사이 추가하였음.
print("3\n2\n1")
print(message)

# 2. 각도 합치기
angle1 = int(input())
angle2 = int(input())

# 입력받은 정수형의 두 값의 합이 360도보다 크면 360으로 나머지 연산 수행
# 360보다 작거나 같으면 두 값의 합을 그대로 출력
sum_angle = (angle1 + angle2) % 360 if angle1 + angle2 > 360 else angle1 + angle2

# 아래와 같이 간단하게도 구현 가능, 360도면 0, 280도 이면 280 반환
# sum_angle = (angle1 + angle2) % 360

print(sum_angle)

# 3. 수 나누기
number = int(input())

answer = 0

# 기존 코드의 이슈는 for i in range(1): 루프는 한번만 실행되므로 두자리씩 자르는 작업이 한번만 수행된다는 점.
# 예: 666666
# 1. number: 666666 > 0 
# >> answer에 66 추가 >> number: 6666 
# 2. number: 6666 > 0
# >> answer에 66 추가 >> number: 66
# 3. number: 66 > 0
# >> answer에 66 추가 >> number: 0
# 4. Loop 종료
while number > 0:
    answer += number % 100
    number //= 100

print(answer)