public class student {

    private String Fname;     //First Name
    private String Lname;     //Last Name
    private int numID;        //Student ID
    private String address;   //Street Address
    private String city;      //City
    private String state;     //State
    private String zipcode;   //Zip Code
    private String major;     //Major
    private int phone;        //Phone Number
    private double gpa;       //Total GPA
    private String level;     //Student Level: freshman, junior...
    private String email;     //Email Address
    private String course1;   //Course Enrolled
    private String course2;   //Course Enrolled
    private String course3;   //Course Enrolled
    private String course4;   //Course Enrolled
    private String course5;   //Course Enrolled
    private String course6;   //Course Enrolled

    //Modifiers - Functions to change the private variables values.
    public void change_name(String input_fname, String  input_lname)
    {
    fname = input_fname;
    lname = input_lname;
    }
    public void change_numID(int input_numID) {numID = input_numID;}
    public void change_address(String input_address, String input_city, String input_state, String input_zipcode)
    {
    adress = input_address;
    city = input_city;
    state = input_state;
    zipcode = input_zipcode;
    }
    public void change_major(String input_major) {major = input_major;}
    public void change_phone(int input_phone) {phone = input_phone;}
    public void change_gpa(double input_gpa) {gpa = input_gpa;}
    public void change_level(double input_level) {level = input_level;}
    public void change_email(double input_email) {email = input_email;}
    public void change_course1(String input_course1) { course1 = input_course1;}
    public void change_course2(String input_course2) { course2 = input_course2;}
    public void change_course3(String input_course3) { course3 = input_course3;}
    public void change_course4(String input_course4) { course4 = input_course4;}
    public void change_course5(String input_course5) { course5 = input_course5;}
    public void change_course6(String input_course6) { course6 = input_course6;}

    //Retrievers - Functions to get the values from the private variables.
    public String get_fname() { return fname;}
    public String get_lname() { return lname;}
    public int get_numID() { return numID;}
    public int get_address() { return address;}
    public String get_major() { return major;}
    public int get_phone() { return phone;}
    public double get_gpa() { return gpa;}
    public double get_level() { return level;}
    public double get_email() { return email;}
    public String get_course1(String input_course1) { return course1;}
    public String get_course2(String input_course2) { return course2;}
    public String get_course3(String input_course3) { return course3;}
    public String get_course4(String input_course4) { return course4;}
    public String get_course5(String input_course5) { return course5;}
    public String get_course6(String input_course6) { return course6;}
}
