import java.util.Scanner;
//made by ujjman
public class TowerOfHanoi {
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of blocks: ");
        int n=sc.nextInt();
        int x=1, y=2, z=3;
        toh(n,z,y,z);

    }
    public static void toh(int n,int a,int b,int c){
        if(n==0)
            return;
        toh(n-1,a,c,b);
        System.out.println(n+ "["+a +"->" + b+"]");
        toh(n-1,c, b, a);

    }
}