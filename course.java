public class course {

    private int course_ID;       //Course ID
    private String course_name;  //Course Name
    private String faculty_name; //Faculty Name
    private int seats;           //Number of seats available

    //Constructor
    public course(){  ;}

    //Modifiers - Functions to change the private variables values.
    public void change_course_ID(String input_course_ID) { course_ID = input_course_ID; }
    public void change_course_name(String input_course_name) { course_name = input_course_name; }
    public void change_faculty_name(String input_faculty_name) { faculty_name = input_faculty_name; }
    public void change_seats(int input_seats) { seats = input_seats;}

    //Retrievers - Functions to get the values from the private variables.
    public String get_course_ID( return course_ID;)
    public String get_course_name( return course_name;)
    public String get_faculty_name( return faculty_name;)
    public String get_seats( return seats;)

}
