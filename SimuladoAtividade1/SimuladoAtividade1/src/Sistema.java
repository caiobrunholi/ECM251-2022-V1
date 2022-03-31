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

    public boolean transferirDinheiro(double valor, Conta origem, Conta destino){
        if(!this.sacar(origem, valor)) return false;
        if(!this.receber(destino, valor)) return false;
        return true;
    }


    public boolean pagarQrCode(Conta origem, String qrcode){
        // procedimentos para pagamento 
        // identificação das contas
        // transferencia da conta de origem para conta obtida pelo qrcode 
        return true;
    }

}
