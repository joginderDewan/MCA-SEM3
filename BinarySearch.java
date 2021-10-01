import java.util.Scanner;

// Binary Search in Java

class Main {
  public static int BinarySearch(int array[], int element, int low, int high) {


    while (low <= high) {
      int mid = low + (high - low) / 2;
      if (array[mid] == element)
        return mid;
      if (array[mid] < element)
        low = mid + 1;
      else
        high = mid - 1;
    }
    return -1;
  }

  public static void main(String args[]) {
    int[] array = { 3, 4, 5, 6, 7, 8, 9 };
    int n = array.length;
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the element to be searched: ");
    int element = sc.nextInt();
    sc.close();
    int result = BinarySearch(array, element, 0, n - 1);
    if (result == -1)
      System.out.println("Element Not found");
    else
      System.out.println("Element found at index " + result);
  }
}