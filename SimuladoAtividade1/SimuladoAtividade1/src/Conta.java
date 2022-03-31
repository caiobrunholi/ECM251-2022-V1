import java.util.StringTokenizer;

public class Conta {
    private String idConta;
    private String cliente;
    private double saldo;
    
        //Construtor
    public Conta (String idConta, String cliente, double saldo){
        this.setIdConta(idConta);
        this.setCliente(cliente);
        this.setSaldo(saldo);
    }

    public String getCliente() {
        return cliente;
    }

    public void setCliente(String cliente) {
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
    
    
}
