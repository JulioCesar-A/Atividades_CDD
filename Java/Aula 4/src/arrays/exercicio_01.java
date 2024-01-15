package arrays;

public class exercicio_01 {

	public static void main(String[] args) {
		int intArrayb[] = new int[5];
		int intArray[] = {2,5,46,12,34};
		for(int i = 0 ; i < intArray.length ; i++ )
		{
		System.out.print(intArray[i] + " ");
		}
		
		System.out.println();
		
		for(int d = 4; d >=0 ; d--)
		{
		intArrayb[d] = intArray[4-d];
		}
		for(int x = 0 ; x < intArray.length ; x++ ) {
		System.out.print(intArrayb[x] + " ");
	}
	}
}
