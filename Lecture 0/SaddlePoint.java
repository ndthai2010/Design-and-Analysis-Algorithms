import java.util.Scanner;

public class SaddlePoint {

    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int arr[][] = new int[10][10];
        inputArray(arr);
        printArray(arr);
        System.out.println(findSaddlePoint(arr));
    }

    public static void inputArray(int arr[][]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Rows: ");
        int rows = sc.nextInt();
        System.out.print("Nhap so hang: ");
        int cols = sc.nextInt();
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print("array[" + i + " ; " + j + "] = ");
                arr[i][j] = sc.nextInt();
            }
        }
    }

    public static void printArray(int arr[][]) {
        System.out.println("Matrix: ");
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                System.out.printf("%5d", arr[i][j]);
            }
            System.out.println();
        }
    }

    public static boolean findSaddlePoint(int[][] array) {
        int[] rowMin = new int[array.length];
        int[] colMax = new int[array[0].length];

        for (int i = 0; i < array.length; i++) {
            rowMin[i] = array[i][0];
            for (int j = 1; j < array[i].length; j++) {
                if (array[i][j] < rowMin[i]) {
                    rowMin[i] = array[i][j];
                }
                if (array[i][j] > colMax[j]) {
                    colMax[j] = array[i][j];
                }
            }
        }
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                if (array[i][j] == rowMin[i] && array[i][j] == colMax[j]) {
                    System.out.println("Saddle point found at (" + i + ", " + j + ")");
                }
                return true;
            }
        }
        return false;
    }
}
