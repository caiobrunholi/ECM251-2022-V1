public class Conta {
    private String idConta;
    private Usuario cliente;
    private double saldo;
    
        //Construtor
    public Conta (String idConta, Usuario cliente, double saldo){
        this.setIdConta(idConta);
        this.setCliente(cliente);
        this.setSaldo(saldo);
    }

    public Usuario getCliente() {
        return cliente;
    }

    public void setCliente(Usuario cliente) {
        this.cliente = cliente;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public String getIdConta() {
        return idConta;
    }

    public void setIdConta(String idConta) {
        this.idConta = idConta;
    }

    public String toString(){
        return "ID:" + idConta + 
        " - Cliente:" + cliente.getNome() +
        " - Saldo:" + getSaldo();
    }
    
    
}
