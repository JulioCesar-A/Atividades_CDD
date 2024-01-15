package strings;

public class exercicio04 {

	public static void main(String[] args) {
		String texto01 = "Sera que sao iguais?";
		String texto02 = "Sera que sao iguais?";
		
		boolean comparar = texto01.equals(texto02);
		System.out.println(comparar == true? "Os textos sao iguais(plagio??????)":"Os textos sao diferentes" );

	}

}
