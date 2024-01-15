package fundamentos;
import java.util.Scanner;
public class exercicio11 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		int dia;
		
		System.out.println("Digite um numero de 1 a 7: ");
		dia = entrada.nextInt();
		
		if (dia < 0 || dia > 7) {
			System.out.println("Valor inválido: ");
		}
		else {
			if(dia == 1) {
				System.out.println("Segunda-feira (odeio)");
			}
			if(dia == 2) {
				System.out.println("Terça-feira");
			}
			if(dia == 3) {
				System.out.println("Quarta-feira");
			}
			if(dia == 4) {
				System.out.println("Quinta-feira");
			}
			if(dia == 5) {
				System.out.println("Sexta-feira");
			}
			if(dia == 6) {
				System.out.println("Sábado");
			}
			if(dia == 7) {
				System.out.println("Domingo");
			}
		}

	}

}
