# Roadmap.sh
## Devops project
#### 1. server stats (https://roadmap.sh/projects/server-stats)

#### How to Run Script

1. **Clone the repository**
   ```shell
   git clone https://github.com/jhin93/stack_training.git
   cd stack_training

2. Run the script
   ```shell
   sh devops/server-stats.sh

## Python training


## C#(.NET)
# 32998_.NET_Application_Developments

#### Class: Student
#### Constructor : public Student(string name, int rollNumber, double grade)
#### Object: John doe, Nabin

```C#
using System;

namespace StudentDemo
{
    // Class: Defines a blueprint for a Student
    public class Student
    {
        // Fields: Store data for the student
        public string Name;
        public int RollNumber;
        public double Grade;

        // Constructor: Initialize the student object
        public Student(string name, int rollNumber, double grade)
        {
            Name = name;
            RollNumber = rollNumber;
            Grade = grade;
        }

        // Method: Display student information
        public void DisplayInfo()
        {
            Console.WriteLine($"Student Name: {Name}, Roll Number: {RollNumber}, Grade: {Grade}");
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            // Object: Create an instance of the Student class
            Student student1 = new Student("Nabin Sharma", 1091, 95.5);

            // Object: Create another instance of the Student class
            Student student2 = new Student("John Doe", 1092, 88.0);

            // Call method to display information for each object
            Console.WriteLine("Student 1 Information:");
            student1.DisplayInfo();

            Console.WriteLine("\nStudent 2 Information:");
            student2.DisplayInfo();

            Console.ReadKey();
        }
    }
}
```

#### multi-dimensional array
```C#
using System;

namespace ConsoleApp2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double[,] array = new double[2, 2]; // Declare a 2x2 multidimensional array

            // Explicitly assign values to match the JavaScript structure
            array[0, 0] = 10.0; // First row, first column
            array[0, 1] = 11.2; // First row, second column
            array[1, 0] = 38.1; // Second row, first column
            array[1, 1] = 0.0;  // Second row, second column

            // Display the array contents
            Console.WriteLine("Array contents:");
            Console.WriteLine($"[{array[0, 0]}, {array[0, 1]}]");
            Console.WriteLine($"[{array[1, 0]}, {array[1, 1]}]");
            Console.ReadKey();
        }
    }
}

// or

double[,] array = new double[,] { { 10.0, 11.2 }, { 38.1, 0.0 } };
```

#### pass parameter by reference(ref)
메소드로 원래 존재했던 변수를 변경하는 것. ref(참조)를 통해 원본 변수를 변경하는 것. 원본 변수에 초기값 필요
```C#
using System;

namespace ReferenceParameterDemo
{
    internal class Program
    {
        // Method: Swap the values of two variables by reference
        public static void SwapNumbers(ref int a, ref int b)
        {
            int temp = a; // Store the value of a in a temporary variable
            a = b;        // Assign b's value to a
            b = temp;     // Assign the temporary value to b
        }

        static void Main(string[] args)
        {
            int number1 = 10; // Initial value set (ref requires an initial value)
            int number2 = 20;

            Console.WriteLine("Before Swapping: number1 = {0}, number2 = {1}", number1, number2);
            SwapNumbers(ref number1, ref number2); // Pass by reference
            Console.WriteLine("After Swapping: number1 = {0}, number2 = {1}", number1, number2);

            Console.ReadKey();
        }
    }
}
```

#### pass parameter by output(out)
out 키워드는 빈 변수에 값을 전달 (초기값 불필요, 메서드 내에서 반드시 설정).
```C#
using System;

namespace OutParameterDemo
{
    internal class Program
    {
        // Method: Accept user input and store it in output parameters
        public static void GetUserInput(out int number, out string name)
        {
            Console.Write("Enter a number: ");
            number = Convert.ToInt32(Console.ReadLine()); // Assign value to number (no initial value needed)

            Console.Write("Enter a name: ");
            name = Console.ReadLine(); // Assign value to name
        }

        static void Main(string[] args)
        {
            int userNumber; // No initial value
            string userName;

            GetUserInput(out userNumber, out userName); // Pass by output

            Console.WriteLine("Received values: number = {0}, name = {1}", userNumber, userName);

            Console.ReadKey();
        }
    }
}
```
#### ArrayList
```csharp
using System;
using System.Collections;

class Program
{
    static void Main()
    {
        // ArrayList 생성
        ArrayList list = new ArrayList();

        // 다양한 타입의 요소 추가
        list.Add(42);           // 정수
        list.Add("Hello");      // 문자열
        list.Add(3.14);        // 실수

        // 요소 출력
        Console.WriteLine("ArrayList 요소:");
        foreach (object item in list)
        {
            Console.WriteLine(item);
        }

        // 특정 인덱스 요소 접근
        Console.WriteLine("\n인덱스 1의 요소: " + list[1]); // "Hello"

        // 요소 제거
        list.Remove(42); // 42 제거

        // 요소 개수 확인
        Console.WriteLine("\n제거 후 요소 개수: " + list.Count);

        // 정렬 (동일한 타입의 요소일 경우에만 의미 있음)
        ArrayList stringList = new ArrayList { "Banana", "Apple", "Cherry" };
        stringList.Sort();
        Console.WriteLine("\n정렬된 문자열 리스트:");
        foreach (object item in stringList)
        {
            Console.WriteLine(item);
        }
    }
}
```

#### Boxing, Unboxing
```C#
using System;
using System.Collections;

class Program
{
    static void Main()
    {
        // ArrayList 생성
        ArrayList list = new ArrayList();
        
        // int 값을 boxing하여 추가
        int num = 42;
        object boxed = num; // Boxing
        list.Add(boxed);
        list.Add(100);     // 자동 Boxing
        list.Add("Hello"); // 문자열 (이미 참조 형식)

        // ArrayList 출력
        foreach (var item in list)
        {
            Console.WriteLine(item);
        }
    }
}
```

1. **Console.ReadLine()**
   - **설명**: 이 메서드는 표준 입력 스트림에서 사용자가 입력한 전체 줄을 읽습니다. 일반적으로 Enter 키를 누를 때까지 입력된 모든 문자를 캡처하며, 입력은 문자열로 반환됩니다.
   - **기능**: 문장이나 전체 이름과 같은 다중 문자 입력을 얻기 위해 주로 사용됩니다.
   - **예제**: `String userInput; userInput = Console.ReadLine();`는 사용자가 입력한 줄을 `userInput` 변수에 할당하는 과정을 보여줍니다.

2. **Console.Read()**
   - **설명**: 이 메서드는 표준 입력 스트림에서 다음 문자를 읽어와, 해당 문자의 유니코드 값을 정수로 반환합니다. 입력을 한 문자씩 처리합니다.
   - **기능**: Enter 키를 기다리지 않고 단일 키 입력을 읽어야 하는 시나리오에 적합합니다.
   - **예제**: `String userInput; userInput = Console.Read();`는 다음 문자의 유니코드 값을 `userInput`에 할당합니다.

3. **Console.ReadKey()**
   - **설명**: 이 메서드는 사용자가 누른 다음 키를 가져옵니다. 키 입력과 함께 해당 키에 대한 정보를 제공하며, 일반적으로 프로그램의 진행을 제어하거나 사용자 입력을 확인하는 데 사용됩니다.
   - **기능**: 사용자가 키를 누를 때까지 대기하며, 주로 "Press any key to continue..."와 같은 메시지와 함께 사용됩니다.
   - **예제**: `Console.WriteLine("Press any key to continue..."); Console.ReadKey();`는 사용자가 키를 누를 때까지 프로그램을 일시 중지합니다.

4. **Console.WriteLine() 및 Console.Write()**
   - **설명**: 
     - `Console.WriteLine()`은 제공된 문자열을 출력하고 새 줄을 추가하여 다음 출력을 새 줄에서 시작하게 합니다.
     - `Console.Write()`는 제공된 문자열을 출력하지만 새 줄을 추가하지 않아 출력이 동일한 줄에 이어집니다.
   - **기능**: `WriteLine()`은 각 출력 후 줄 바꿈이 필요한 경우에 유용하며, `Write()`는 연속적인 출력이 필요한 경우에 적합합니다. `{0}`는 변수의 자리 표시자로 사용됩니다.
   - **예제**: `Console.WriteLine("The userInput is {0}", userInput);`는 `userInput` 값을 출력하고 새 줄을 추가하며, `{0}`은 `userInput` 값으로 대체됩니다.

```C#
// .Read() 예시: 한 글자를 입력받아 유니코드 값 출력
int ch = Console.Read();
Console.WriteLine("입력한 문자의 유니코드 값: " + ch);

// .ReadLine() 예시: 한 줄을 입력받아 그대로 출력
string line = Console.ReadLine();
Console.WriteLine("입력한 문자열: " + line);

// .ReadKey() 예시: 아무 키나 누르면 해당 키 정보 출력
Console.WriteLine("아무 키나 누르세요.");
ConsoleKeyInfo keyInfo = Console.ReadKey();
Console.WriteLine("\n누른 키: " + keyInfo.Key);

// .Write() 예시: 줄바꿈 없이 출력
Console.Write("줄바꿈 없이 출력합니다.");

// .WriteLine() 예시: 줄바꿈과 함께 출력
Console.WriteLine("줄바꿈과 함께 출력합니다.");
```




