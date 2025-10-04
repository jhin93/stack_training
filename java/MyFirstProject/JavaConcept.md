
### memory management 
Stack : stores primitive data types and references to objects in heap, LIFO
Heap : stores objects and arrays, dynamic memory allocation
Queue : stores asynchronous tasks (callbacks, promises), FIFO

특징         스택                       힙
메모리형태    고정 크기, 연속적"            "동적 크기, 비연속적"
할당 방식    컴파일러가 자동 할당           개발자가 수동 할당
관리 주체    시스템(컴파일러)              개발자
속도        빠름 (단순한 포인터 이동)       느림 (복잡한 메모리 관리)
용도        "지역 변수, 함수 호출 스택"     "동적 데이터 (배열, 객체 등)"
크기 제한    제한적 (스택 오버플로우 가능)    운영체제 메모리 제한까지 가능

**큐(queue)**는 스택이나 힙과 달리 논리적 자료 구조입니다.
큐는 데이터를 FIFO(First In, First Out) 방식으로 관리하는 추상적인 개념이며, 실제 데이터는 스택 메모리나 힙 메모리에 저장됩니다

큐를 스택 메모리에 구현하면 시스템이 메모리를 자동 관리합니다(예: 고정 배열).
큐를 힙 메모리에 구현하면 개발자가 메모리를 수동으로 관리합니다(예: 동적 배열, 연결 리스트).

### variable
1. Primitive Data Types : simple value stored directly in memory (stack)
   ex) int, char, boolean, float, double, byte, short, long
2. Reference Data Types : memory address (stack) that points to the (heap)
    ex) String, Arrays, Classes, Interfaces


- nextInt() 뒤에 nextLine()을 사용해야 하는 이유

import java.util.Scanner;
```java
public class Main {
    public static void main(String[] args) {
            Scanner scannerPractice = new Scanner(System.in);
    
            System.out.println("Enter your age:");
            int age = scannerPractice.nextInt(); 
            // nextInt()는 숫자만 읽고 엔터(\n)는 버퍼에 남겨둡니다. 
            // 이 엔터를 그냥 넘어가면 남은 버퍼를 다음 nextLine()이 다음 input을 입력받기 전에 해당 엔터를 읽고 넘어감. 
    
            // .nextLine()을 한 번 더 호출하여 버퍼에 남아있는 엔터를 제거합니다.
            scannerPractice.nextLine();
    
            System.out.println("Enter your favorite color:");
            String color = scannerPractice.nextLine();
    
            System.out.println("Your age is: " + age);
            System.out.println("Your favorite color is: " + color);
            
            scannerPractice.close();
        }
}

```
