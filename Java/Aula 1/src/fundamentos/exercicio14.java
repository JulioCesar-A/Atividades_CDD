package fundamentos;
import java.util.Scanner;
public class exercicio14 {
	public static void main(String[] args) {
		int Participa = 0;
		Scanner entrada = new Scanner(System.in);
		String pergunta;
		System.out.println("Digite o nome do investigado: ");
		String nome = entrada.nextLine();
		System.out.println("Telefonou para a vitima? (S/N) > ");
		pergunta = entrada.nextLine();
		if (pergunta.equalsIgnoreCase("S")) {
			Participa++;
		}
		System.out.println("Esteve no local? (S/N) > ");
		pergunta = entrada.nextLine();
		if (pergunta.equalsIgnoreCase("S")) {
			Participa++;
		}
		System.out.println("Mora perto da vitima? (S/N) > ");
		pergunta = entrada.nextLine();
		if (pergunta.equalsIgnoreCase("S")) {
			Participa++;
		}
		System.out.println("Devia para a vitima? (S/N) > ");
		pergunta = entrada.nextLine();
		if (pergunta.equalsIgnoreCase("S")) {
			Participa++;
		}
		System.out.println("Ja trabalhou com a vitima? (S/N) > ");
		pergunta = entrada.nextLine();
		if (pergunta.equalsIgnoreCase("S")) {
			Participa++;
		}
		if (Participa == 1 || Participa == 0) {
			System.out.println(nome + " e inocente");
		}
		else {
			if (Participa == 2) {
				System.out.println("Suspeitamos que " + nome + " esteja envolvido(a) no assassinato da vitima");
			}	
			else {
				if (Participa == 3 || Participa == 4) {
					System.out.println(nome + " e cumplice do assassinato da vitima");
				}
				else {
					if (Participa == 5) {
						System.out.println(nome + " Assassinou a vitima");
			}
		}
	}
		}
}
	}