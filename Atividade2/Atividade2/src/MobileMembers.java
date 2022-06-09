public class MobileMembers extends Membro{
    public MobileMembers(String userName, String email, EnumFuncao funcao, EnumTurno turno) {
        super(userName, email, funcao, turno);
        //TODO Auto-generated constructor stub
        setRegularMessage(regularMessage);
        setExtraMessage(extraMessage);
    }
    private final String regularMessage = "Happy Coding!";
    private final String extraMessage = "MAsK_S0c13ty";
    
}