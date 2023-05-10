import java.util.Scanner;

public class SelectionSort {
    
    public static Scanner sc = new Scanner(System.in);

    private static int[] inputArray(int a[]) {
		for(int i = 0; i < a.length; i++) {
			a[i] = sc.nextInt();
		}
		return a;
	}

    private static void swap(int a[], int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
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
        selectionSort(array);
        long endTime = System.currentTimeMillis();
        long totalTime = endTime - startTime;
        System.out.println();
        System.out.println("Running time: " + totalTime + "ms");
    }
}
