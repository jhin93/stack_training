import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scannerPractice = new Scanner(System.in);

        System.out.println("Enter your age:");
        int age = scannerPractice.nextInt(); // nextInt()는 숫자만 읽고 엔터(\n)는 버퍼에 남겨둡니다. 

        // .nextLine()을 한 번 더 호출하여 버퍼에 남아있는 엔터를 제거합니다.
        scannerPractice.nextLine();

        System.out.println("Enter your favorite color:");
        String color = scannerPractice.nextLine();

        System.out.println("Your age is: " + age);
        System.out.println("Your favorite color is: " + color);
        
        scannerPractice.close();
    }
}
