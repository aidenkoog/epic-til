public class ArraySpiralSum {
    public static void main(String[] args) {
        int[][] array = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12},`
            {13, 14, 15, 16}
        };

        int sum = spiralSum(array);
        System.out.println("Spiral Sum: " + sum);
    }

    public static int spiralSum(int[][] array) {
        if (array == null || array.length == 0) {
            return 0;
        }

        int top = 0; // 상단 경계
        int bottom = array.length - 1; // 하단 경계
        int left = 0; // 좌측 경계
        int right = array[0].length - 1; // 우측 경계
        int sum = 0;

        // 나선형 순회
        while (top <= bottom && left <= right) {
            // 상단 행 순회
            for (int i = left; i <= right; i++) {
                sum += array[top][i];
            }
            top++;

            // 우측 열 순회
            for (int i = top; i <= bottom; i++) {
                sum += array[i][right];
            }
            right--;

            // 하단 행 순회 (아래에서 위로 가는 경우 방지)
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    sum += array[bottom][i];
                }
                bottom--;
            }

            // 좌측 열 순회 (오른쪽에서 왼쪽으로 가는 경우 방지)
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    sum += array[i][left];
                }
                left++;
            }
        }

        return sum;
    }
}