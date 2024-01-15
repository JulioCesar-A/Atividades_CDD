package strings;
import java.util.StringTokenizer;
public class exercicio01 {

	public static void main(String[] args) {
		String str = "Hello";
		String str2 = "HELLO";
		
		
		boolean b1 = str.equals("Hello");
		boolean b2 = str.equals(str2);
		boolean b3 = str.equalsIgnoreCase(str2);
		boolean b4 = str.equalsIgnoreCase("azul");


		String resultado = str.toUpperCase();
		String resultado2 = str.toLowerCase();
		String resultado3 = str.trim();
		char resultado4 = str.charAt(1);
		int resultado5 = str.length();
		
		System.out.println(resultado);		
		System.out.println(resultado2);
		System.out.println(resultado3);
		System.out.println(resultado4);
		System.out.println(resultado5);
		System.out.println(b1);
		System.out.println(b2);
		System.out.println(b3);
		System.out.println(b4);

		String valor = "CDD 4.0 - Java";
		System.out.println(valor.compareTo("CDD 4.0 - Java") == 0? true : false);
		System.out.println(valor.compareTo("CDD 4.0 - JAVA") == 0? true : false);
		System.out.println(valor.compareToIgnoreCase("CDD 4.0 - JAVA") == 0? true : false);

		StringTokenizer exemplo = new StringTokenizer("O mundo não é mais o mesmo mas não iremos desistir nunca");
		System.out.println(exemplo.countTokens());
		}

}
