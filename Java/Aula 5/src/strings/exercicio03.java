package strings;

import java.util.Scanner;
import java.util.StringTokenizer;
public class exercicio03 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um texto: ");
		String texto = entrada.nextLine();

		StringTokenizer result = new StringTokenizer(texto);
		System.out.println("Total de palavras: " + result.countTokens());
	}

}
