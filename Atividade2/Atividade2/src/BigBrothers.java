public class BigBrothers extends Membro{
    public BigBrothers(String userName, String email, EnumFuncao funcao, EnumTurno turno) {
        super(userName, email, funcao, turno);
        //TODO Auto-generated constructor stub
        setRegularMessage(regularMessage);
        setExtraMessage(extraMessage);
    }

    private final String regularMessage = "Sempre ajudando as pessoas membros ou nao S2!";
    private final String extraMessage = "...";
    
}
