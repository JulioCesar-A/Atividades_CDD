package arrays;
import java.util.Scanner;
public class exercicio_03 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		int arrayA[] = new int[10];
		int arrayB[] = new int[10];
		int arrayC[] = new int[10];
		int arrayD[] = new int[10];
		
		for(int x = 0 ; x < arrayA.length ; x++) {
			System.out.print("Digite um valor(arrayA): ");
			arrayA[x] = entrada.nextInt();
		}
		for(int x = 0 ; x < arrayB.length ; x++) {
			System.out.print("Digite um valor(arrayB): ");
			arrayB[x] = entrada.nextInt();
		}
		for(int x = 0 ; x < arrayC.length ; x++) {
			System.out.print("Digite um valor(arrayC): ");
			arrayC[x] = entrada.nextInt();
		}
		for(int x = 0 ; x < arrayD.length ; x++) {
			System.out.print("Digite um valor(arrayD): ");
			arrayD[x] = entrada.nextInt();
		}
		for(int x = 0 ; x < 10 ; x++) {
			System.out.print(arrayA[x]+ " ");
		}
			System.out.println();
		for(int x = 0 ; x < 10 ; x++) {
			System.out.print(arrayB[x]+ " ");
		}
			System.out.println();
		for(int x = 0 ; x < 10 ; x++) {
			System.out.print(arrayC[x]+ " ");
		}
			System.out.println();
		for(int x = 0 ; x < 10 ; x++) {
			System.out.print(arrayD[x]+ " ");
		}
			System.out.println();

		}

}