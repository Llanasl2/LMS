public class profiles {
    
    private String Name;
    private int numID;
    
    //modifiers
    public void change_Name(String Input_Name){Name = Input_Name;}
    public void change_numID(int input_numID) {numID = input_numID;}
    
    //retrievers 
    public String get_Name() { return Name; }
    public int get_numID() { return numID; }
}