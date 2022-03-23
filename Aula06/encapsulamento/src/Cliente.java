public class Cliente {
    private String cpf;
    private String nome;
    private String email;
    private Conta conta;

    public void visualizarCliente(){
        System.out.println("Dados do Cliente:");
        System.out.println("Nome:" + nome);
        System.out.println("CPF:" + cpf);
        System.out.println("E-mail:" + email);
        System.out.println("Conta:" + conta);
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }
}
