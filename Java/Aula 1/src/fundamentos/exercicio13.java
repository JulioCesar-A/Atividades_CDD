package fundamentos;
import java.util.Scanner;
public class exercicio13 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		String morf;
		System.out.println("Digite M or F: ");
		morf = entrada.next();
		if (morf.equals ("F") || morf.equals("f")) {
			System.out.println("Feminino");
		}
		else {
			if (morf.equals ("M") || morf.equals("m")) {
				System.out.println("Masculino");
			}
		}

}
}