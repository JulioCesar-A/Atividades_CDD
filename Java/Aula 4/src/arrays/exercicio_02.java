package arrays;

public class exercicio_02 {

	public static void main(String[] args) {
		int[] arrayNum = {87,68,52,5,49,83,45,12,64};
		int total = 0;
		for(int i : arrayNum) {
			total+=i;
		}
		System.out.printf("Total do valor dos elementos arrayNum: %d\n", total);
	}

}
