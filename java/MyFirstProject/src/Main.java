import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        double width = 0;
        double height = 0;
        double area = 0;
        
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the width :");
        width = input.nextDouble();

        System.out.println("Enter the height :");
        height = input.nextDouble();
        
        area = width * height;

        System.out.println("The area of the rectangle is : " + area + "cm²");
        
        
        input.close();
    }
}
