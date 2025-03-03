def spiral_sum(matrix):
    if not matrix or not matrix[0]:  # 예외 처리 (빈 배열)
        return 0

    top, bottom = 0, len(matrix) - 1  # 상단, 하단 경계
    left, right = 0, len(matrix[0]) - 1  # 좌측, 우측 경계
    total_sum = 0

    while top <= bottom and left <= right:
        # 상단 행 순회 (왼쪽 → 오른쪽)
        for i in range(left, right + 1):
            total_sum += matrix[top][i]
        top += 1  # 상단 경계 줄이기

        # 우측 열 순회 (위 → 아래)
        for i in range(top, bottom + 1):
            total_sum += matrix[i][right]
        right -= 1  # 우측 경계 줄이기

        # 하단 행 순회 (오른쪽 → 왼쪽)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                total_sum += matrix[bottom][i]
            bottom -= 1  # 하단 경계 줄이기

        # 좌측 열 순회 (아래 → 위)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                total_sum += matrix[i][left]
            left += 1  # 좌측 경계 줄이기

    return total_sum


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

result = spiral_sum(matrix)
print("Spiral Sum:", result)
