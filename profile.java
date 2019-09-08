public class profile {

    private String Name;
    private int numID;
    private String address;
    private String major;
    private int phone;
    private double gpa;
    private String course1;
    private String course2;
    private String course3;
    private String course4;
    private String course5;
    private String course6;

    //modifiers
    public void change_Name(String Input_Name){Name = Input_Name;}
    public void change_numID(int input_numID) {numID = input_numID;}
    public void change_address(int input_address) {adress = input_address;}
    public void change_major(String input_major) {major = input_major;}
    public void change_phone(int input_phone) {phone = input_phone;}
    public void change_gpa(double input_gpa) {gpa = input_gpa;}
    public void change_course1(String input_course1) { course1 = input_course1;}
    public void change_course2(String input_course2) { course2 = input_course2;}
    public void change_course3(String input_course3) { course3 = input_course3;}
    public void change_course4(String input_course4) { course4 = input_course4;}
    public void change_course5(String input_course5) { course5 = input_course5;}
    public void change_course6(String input_course6) { course6 = input_course6;}

    //retrievers
    public String get_Name() { return Name;}
    public int get_numID() { return numID;}
    public int get_address() { return address;}
    public String get_major() { return major;}
    public int get_phone() { return phone;}
    public double get_gpa() { return gpa;}
    public String get_course1(String input_course1) { return course1;}
    public String get_course2(String input_course2) { return course2;}
    public String get_course3(String input_course3) { return course3;}
    public String get_course4(String input_course4) { return course4;}
    public String get_course5(String input_course5) { return course5;}
    public String get_course6(String input_course6) { return course6;}
}
