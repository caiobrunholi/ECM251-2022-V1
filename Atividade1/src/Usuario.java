public class Usuario {
    private String nome;
    private int rg;
    private String email;
    private Veiculo veiculo;
    
    public Usuario(String nome, int rg, String email, Veiculo veiculo) {
        this.nome = nome;
        this.rg = rg;
        this.email = email;
    }
    
    public Usuario(String nome, int rg, String email) {
        this.nome = nome;
        this.rg = rg;
        this.email = email;
    }
    public Veiculo getVeiculo() {
        return veiculo;
    }
    public void setVeiculo(Veiculo veiculo) {
        this.veiculo = veiculo;
    }
    public String getNome() {
        return nome;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public int getRg() {
        return rg;
    }
    public void setRg(int rg) {
        this.rg = rg;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public String toString() {
        return "Usuario [email=" + email + ", nome=" + nome + ", rg=" + rg + ", veiculo=" + veiculo + "]";
    }

    public void pegarEmprestado (Veiculo veiculo){
        setVeiculo(veiculo);
    }

    public void devolver (){
        setVeiculo(null);
    }
    
}
