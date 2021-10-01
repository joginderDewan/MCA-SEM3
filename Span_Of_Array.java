/* link:-
https://www.pepcoding.com/resources/online-java-foundation/function-and-arrays/span-of-array-official/ojquestion */
import java.io.*;
import java.util.*;

public class Span_Of_Array{

public static void main(String[] args) throws Exception {
    // write your code here
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] a = new int[n];
    for(int i=0;i<a.length;i++){
        a[i] = sc.nextInt();
        
    }
    int min = a[0];
    int max=a[0];
    for(int i=1;i<a.length;i++){
        if(a[i]>max){
            max=a[i];
        }
        if(a[i]<min){
            min = a[i];
        }
    }
    int span = max - min;
    System.out.println(span);
    
 }

}