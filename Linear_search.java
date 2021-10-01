import java.util.Scanner;

public class Linear_search{

	public static void main(String[] args){

	Scanner sc = new Scanner(System.in);

	System.out.println("Enter size of array");
	int size = sc.nextInt();

	int[] a = new int[size];
	
	System.out.println("Enter array elements:");
	for(int i =0;i<a.length;i++){
		a[i] = sc.nextInt();
	}
	
	System.out.println("Array:");
	for(int i =0;i<a.length;i++){
		System.out.println(a[i]);
	}

	//linear search
	System.out.println("Enter the number you want to search");
	int key = sc.nextInt();
	boolean found = false;
	for(int i=0;i<a.length;i++){
	if(a[i] == key){
		System.out.println("Found at index:"+i);
		found  = true;
		break;
	}

	}
	if(found == false){

	System.out.println("Not found");
	}

	
	}

}