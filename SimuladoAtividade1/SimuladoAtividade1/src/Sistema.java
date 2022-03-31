public class Sistema {
    public boolean sacar(Conta conta, double valor){
        if (valor > conta.getSaldo()) return false;
        if (valor < 0) return false;
        conta.setSaldo(conta.getSaldo() - valor);
        return true;

    }

    public boolean receber(Conta conta, double valor){
        if(valor < 0) return false;
        conta.setSaldo(conta.getSaldo() + valor);
        return true;

    }

    boolean transferirDinheiro(double valor, Conta origem, Conta destino){
        if(!this.sacar(origem, valor)) return false;
        if(!this.receber(destino, valor)) return false;
        return true;
    }


}
