import java.util.Arrays;
import java.util.Scanner;

public class AdvancedSorting {

    private static Scanner sc = new Scanner(System.in);

    public static int[] inputArray(int a[]) {
		for(int i = 0; i < a.length; i++) {
			a[i] = sc.nextInt();
		}
		return a;
	}

    private static int partition(int[] a, int start, int end) {
        int i = start + 1;
        int j = end;
        int pivot = a[start];
        while (i <= j) {
            while (i <= end && a[i] < pivot) {
                i++;
            }
            while (j >= start + 1 && a[j] >= pivot) {
                j--;
            }
            if (i < j) {
                swap(a, i, j);
                i++;
                i--;
            }
        }
        swap(a, start, j);
        return j;
    }

    private static void swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    private static void quickSort(int[] a, int start, int end) {
        if (start < end) {
            int j = partition(a, start, end);
            quickSort(a, start, j - 1);
            quickSort(a, j + 1, end);
        }
    }

    public static void sort1(int[] a) {
        quickSort(a, 0, a.length - 1);
    }

    public static void sort(int[] a, int start, int end) {
        if (start < end) {

            int middle = start + (end - start) / 2;
            sort(a, start, middle);
            sort(a, middle + 1, end);
            merge(a, start, middle, end);
        }

    }

    public static void merge(int[] a, int start, int middle, int end) {
        int[] b = new int[a.length];
        for (int i = start; i <= end; i++) {
            b[i] = a[i];
        }
        int i = start;
        int j = middle + 1;

        for (int k = start; k <= end; k++) {
            if (i <= middle && j <= end) {
                if (b[i] < b[j]) {
                    a[k] = b[i++];
                } else {
                    a[k] = b[j++];
                }
            } else {
                if (i > middle) {
                    a[k] = b[j++];
                } else {
                    a[k] = b[i++];
                }
            }
        }
    }

    public static void sort2(int[] a) {
        sort(a, 0, a.length - 1);

    }

    public static void heapSort(int[] a) {
        int n = a.length - 1;
        for (int k = n / 2; k > 0; k--) {
            downheap(a, k, n);
        }

        int t = n;
        while (t > 1) {
            swap(a, 1, t);
            t--;
            downheap(a, 1, t);
        }
    }

    private static void upheap(int[] a, int k) {
        while (k > 1 && a[k] > a[k / 2]) {
            swap(a, k, k / 2);
            k = k / 2;
        }
    }

    private static void downheap(int[] a, int k, int n) {
        while (2 * k < n) {
            int j = 2 * k;
            if (a[j] < a[j + 1]) {
                j++;
            }

            if (a[k] >= a[j]) {
                break;
            }

            swap(a, k, j);
            k = j;
        }
    }

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        System.out.print("Number of elements: ");
            int n = sc.nextInt();
        int[] array = new int[n];
        inputArray(array);
        sort1(array);
        // sort2(array);
        // heapSort(array);
        System.out.println(Arrays.toString(array));
        long endTime = System.currentTimeMillis();
        long totalTime = endTime - startTime;
        System.out.println();
        System.out.println("Running time: " + totalTime + "ms");

    }
}
