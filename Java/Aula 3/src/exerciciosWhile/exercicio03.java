package exerciciosWhile;

import java.util.Scanner;

public class exercicio03 {
	public static void main (String[]Args) {
		int x = 0;
		int par= 0;
		int impar = 0;
		int input;
		Scanner entrada = new Scanner(System.in);
		
		System.out.print("Digite um numero: ");
		input = entrada.nextInt();
		System.out.print("Numeros pares: ");
		while (x <= input)
		{	
		System.out.print(x%2==0? x+" ":"");
		par = ((x%2==0)? ++par: ++impar);
		x++;
		}
		System.out.print("\nTemos " + par + " numeros pares");
		x = 0;
		System.out.print("\nNumeros impares: ");
		while (x <= input)
		{	
		System.out.print(x%2!=0? x+" ":"");
		x++;
		}
		System.out.print("\nTemos " + impar + " numeros impares");
	}
}