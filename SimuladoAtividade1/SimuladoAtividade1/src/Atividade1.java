public class Atividade1 {
    public void run(){
        Usuario u1 = new Usuario("Picard", "ncc1701d", "picard@enterprise.com");
        Conta conta1 = new Conta("0" , u1 , 1000);
        Usuario u2 = new Usuario("Riker", "Jazz", "williamtr@enterprise.com");
        Conta conta2 = new Conta("1" , u2 , 250);
        Usuario u3 = new Usuario("Data", "ImArealHuman", "data@enterprise.com");
        Conta conta3 = new Conta("3" , u3 , 3000);

        System.out.println("Estado Inicial:");
        System.out.println(conta1);
        System.out.println(conta2);
        System.out.println(conta3);
        
        

        System.out.println(Transacoes.GerarQrCode(conta1,250.0));
        String qrcode1 = Transacoes.GerarQrCode(conta1,250.0);
        //Implementação dos pagamentos

        System.out.println(Transacoes.GerarQrCode(conta2,1000.0));
        String qrcode2 = Transacoes.GerarQrCode(conta2,1000.0);
        //Implementação dos pagamentos

        System.out.println("Estado Final:");
        System.out.println(conta1);
        System.out.println(conta2);
        System.out.println(conta3);
        
    }
    
}
