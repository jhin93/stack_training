import java.util.Random;

public class Main {
    public static void main(String[] args) {
        
        Random rand = new Random();
        
        boolean isHeads;
        
        isHeads = rand.nextBoolean();
        
        if(isHeads){
            System.out.println("Heads");
        }
        else {
            System.out.println("Tails");
        }
        
    }
}
