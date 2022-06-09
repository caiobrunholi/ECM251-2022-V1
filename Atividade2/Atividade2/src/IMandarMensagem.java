public interface IMandarMensagem {
     public static String mandarMensagem(Membro member){
        if (member.getTurno().equals(EnumTurno.REGULAR)){
            System.out.println(member.getRegularMessage());
            return member.getRegularMessage();
        }else{
            System.out.println(member.getExtraMessage());
            return member.getExtraMessage();
        }
    }
    
}
