import java.util.*;

class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner scn = new Scanner(System.in);
		int n = scn.nextInt();
		Stack<Integer> st = new Stack<>();
		for(int i=0;i<n;i++){
			int ele = scn.nextInt();
			st.push(ele); 
		} 
		//check wheter n is odd using bit manupilation
		if( (n & 1) != 0){
			st.pop();
		}
		while(st.size() > 0){
			int e1 = st.pop();
			int e2 = st.pop();
			int diff = Math.abs(e1 - e2);
			if(diff > 1){
				System.out.println(false);
				return;
			} 
			
		}
		System.out.println(true);
        scn.close();

	}
}

