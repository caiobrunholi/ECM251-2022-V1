public class Transacoes {
    
    public static String GerarQrCode(Conta conta, double valor){
        String qrcode = (conta.getIdConta() + ";" + conta.getCliente().getNome() + ";" + valor);

        return qrcode; 
    }
    
}
