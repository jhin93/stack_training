import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scannerPractice = new Scanner(System.in);

        System.out.println("Enter your name: ");
        String name = scannerPractice.nextLine();

        System.out.println("Enter your age: ");
        int age = scannerPractice.nextInt();

        System.out.println("What is your gpa: ");
        double gpa = scannerPractice.nextDouble();

        System.out.println("Are you a student (true/false): ");
        boolean isStudent = scannerPractice.nextBoolean();
        
        System.out.println("You are " + age + " years old.");
        System.out.println("Your gpa is " + gpa + ".");
        if (isStudent) {
            System.out.println("You are a student.");
        } else {
            System.out.println("You are not a student.");
        }
        
        scannerPractice.close();
    }
}
