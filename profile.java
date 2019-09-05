public class profile {
    
    private String Name;
    private int numID;
    private String address;
    
    //modifiers
    public void change_Name(String Input_Name){Name = Input_Name;}
    public void change_numID(int input_numID) {numID = input_numID;}
    public void change_address(int input_address) {adress = input_address;}
    
    //retrievers 
    public String get_Name() { return Name; }
    public int get_numID() { return numID; }
    public int get_address() { return address; }
}
