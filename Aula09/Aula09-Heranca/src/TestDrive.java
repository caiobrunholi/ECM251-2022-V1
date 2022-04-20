public class TestDrive{
    //static indica que é uma função da Classe, não do objeto. Ou seja, existe sem que exista um objeto do tipo Test Drive
    public static void executar(){
        Dado d1 = new Dado("1234");
        System.out.println("Dado Criado:"+ d1);
        System.out.println("Face atual:"+ d1.faceAtual());
        //Sorteia nova face
        d1.rodar();
        System.out.println("Face atual:"+ d1.faceAtual());
    }


}