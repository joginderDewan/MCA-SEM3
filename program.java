import java.util.Scanner;


public class pattern {


	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		System.out.println("Enter the size:");
		int n = s.nextInt();
		//i is for row
		//j is for column
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				if(j==0 || i==0 || i == n-1 || i == n/2) {
					System.out.print("*");
				}
			}
			System.out.println();
		}
		


	}


}
sa
