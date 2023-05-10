import java.util.Scanner;

public class BasicSorting {
    
    public static Scanner sc = new Scanner(System.in);

    public static int[] inputArray(int a[]) {
		for(int i = 0; i < a.length; i++) {
			a[i] = sc.nextInt();
		}
		return a;
	}

    public static void swap(int a[], int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    public static void bubbleSort(int a[]) {
        for (int i = 0; i < a.length; i++) {
            for (int j = i + 1; j < a.length; j++) {
                if (a[i] > a[j]) {
                    swap(a, i, j);
                }
            }
        }
    }

    public static void selectionSort(int[] a) {
        for (int i = 0; i < a.length; i++) {
            for (int j = i + 1; j < a.length; j++) {
                int min = a[i];
                if (min > a[j]) {
                    swap(a, i, j);
                }
            }
        }
    }

    public static void shiftElement(int[] a, int i) {
        int iValue = a[i];
        while (i > 0 && a[i - 1] > iValue) {
            a[i] = a[i - 1];
            i--;
        }
        a[i] = iValue;
    }

    public static void insertionSort(int[] a, int n) {
        for (int i = 1; i < n; i++) {
            if (a[i] < a[i - 1]) {
                shiftElement(a, i);
            }
        }
    }

    public static void printArray(int[] a){
        for(int i = 0; i < a.length; i++){
            System.out.println(a[i] + " ");
        }
    }

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        System.out.print("Number of elements: ");
            int n = sc.nextInt();
        int[] array = new int[n];
        inputArray(array);
        bubbleSort(array);
        // selectionSort(array);
        // printArray(array);
        // insertionSort(array, n);
        long endTime = System.currentTimeMillis();
        long totalTime = endTime - startTime;
        System.out.println();
        System.out.println("Running time: " + totalTime + "ms");
    }
}
