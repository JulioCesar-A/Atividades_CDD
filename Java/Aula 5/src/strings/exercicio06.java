package strings;

public class exercicio06 {

	public static void main(String[] args) {
	String texto[] = {"a","vida","e","bela"};
	String novoTexto = new String();
	
	for(int x = 0 ; x < texto.length; x++) {
		novoTexto += texto[x] + " ";
	}
	String maius = new String(novoTexto.toUpperCase());
	
	System.out.println(maius);
	
	novoTexto = "";
	
	for(int x = 3; x >=0 ;x--) {
		novoTexto += texto[x] + " ";
	}
	String minus = new String(novoTexto.toUpperCase());
	
	System.out.println(minus);
	
	
	}

}
