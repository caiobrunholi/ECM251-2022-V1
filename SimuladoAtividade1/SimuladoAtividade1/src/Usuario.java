public class Usuario {
    private String nome;
    private String senha;
    private String email;

    //Construtor 
    public Usuario(String nome, String senha, String email){
        this.setNome(nome);
        this.setSenha(senha);
        this.setEmail(email);
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

}
