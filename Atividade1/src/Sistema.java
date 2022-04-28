public class Sistema {
    public void run(){
        Carro carro = new Carro("carro", 1000, "Honda", "NSX");
        Moto moto = new Moto("moto", 20000);
        Bicicleta bicicleta = new Bicicleta("bicicleta", 30000);
        Patinete patinete = new Patinete("patinete", 40000);

        System.out.println(carro);

        Usuario senna = new Usuario("Senna", 111111111, "airton@mclaren.com");
        senna.pegarEmprestado(carro);
        Usuario mcqueen = new Usuario("McQueen", 22222222, "bullit@universal.com");
        mcqueen.pegarEmprestado(moto);
        Usuario eleanor = new Usuario("Eleanor", 333333333, "mustang@60seconds.com");
        eleanor.pegarEmprestado(bicicleta);
        Usuario mate = new Usuario("Mate", 444444444, "towmatter@cars.com");
        mate.pegarEmprestado(patinete);

        trocar(senna, mcqueen);
        trocar(eleanor, mate);

        mate.devolver();
        System.out.println(mate);
    }

    public void trocar (Usuario u1, Usuario u2){
        System.out.println("\nTroca entre: " + u1.getNome() + " e " + u2.getNome());
        System.out.println(u1);
        System.out.println(u2);
        Veiculo veiculoU1 = u1.getVeiculo();
        Veiculo veiculoU2 = u2.getVeiculo();
        u1.setVeiculo(veiculoU2);
        u2.setVeiculo(veiculoU1);
        System.out.println("Troca Realizada!");
        System.out.println(u1);
        System.out.println(u2);
        veiculoU1 = u1.getVeiculo();
        veiculoU2 = u2.getVeiculo();
        System.out.println("Testar");
        veiculoU1.testar();
        veiculoU2.testar();
        System.out.println("Pronto!\n");
    }

}
