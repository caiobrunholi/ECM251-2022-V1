public class TestDriveArray{
    public static void main(String[] args) {
        //Cria um array de int 
        int[] meuArray;
        //Intsancia o array
        meuArray = new int[4];
        //Colocando valores
        meuArray[0] = 45;
        meuArray[1] = 12;
        meuArray[2] = 9;
        meuArray[3] = 5;

        //Criadno um ERRO
        meuArray[10] = -1;
    }
}