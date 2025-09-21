## URL : Roadmap.sh
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
```python
# list vs tuple
# list는 수정 가능, tuple은 수정 불가능
# list는 [], tuple은 ()

name = input("Enter your name: ")
age = int(input("Enter your age: "))

is_adult = age >= 18
greeting = f"Hello, {name}! You are {'adult' if is_adult else 'not adult'}."
print(greeting)

user_info_dictionary = {"name :": name, "age :": age}
user_info_list = [name, age]
user_info_tuple = (name, age)

tuple_in_dict = {(1, 2): "point"}  # 튜플은 딕셔너리 키로 사용 가능
# list_in_dict = {[1, 2]: "point"}  # 리스트는 키로 사용 불가: TypeError
user_info_list.append("seoul")
print("added user_info_list : ", user_info_list)
# user_info_tuple[0] = 10 # 에러 발생. 튜플은 수정 불가.

# Tuple은 수정할 수 없지만, += (추가하려는값 ,) 을 통해 기존 튜플에 새로운 값을 concatenate하여  새로운 튜플을 만들어낼 수 있다.
print("기존 튜플 :", user_info_tuple, "ID", id(user_info_tuple))
user_info_tuple += ("seoul",)
print("새로운 튜플 :", user_info_tuple, "ID", id(user_info_tuple))

### List comprehension

import random

random.seed(10)

result = 0

def Lab4Exc6():

    global result
    input_num = int(input("input : "))
    numbers = [random.randint(1,100) for _ in range(input_num)]
    print(*numbers)
    result = sum(num for num in numbers if num % 2 == 0)
    print(result)

Lab4Exc6()

evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)
출력: [2, 4, 6, 8, 10]

words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)
출력: [5, 5, 6]

numbers = [1, 2, 3, 4]
strings = [str(num) for num in numbers]
print(strings)
출력: ['1', '2', '3', '4']

### Slicing
- start: 슬라이싱 시작 인덱스 (포함)
- stop: 슬라이싱 종료 인덱스 (제외)
- step: 인덱스 증가 단위 (양수면 왼쪽에서 오른쪽, 음수면 오른쪽에서 왼쪽)

lst = [1, 2, 3, 4, 5]
print(lst[::-1])
출력: [5, 4, 3, 2, 1]

test = 'abcde'
print(test[1:4:-1])
출력: ''. 역방향이므로 start가 stop보다 커야 함. 근데 아님. 그래서 해당되는 문자열 없음.
print(test[4:1:-1])
출력: 'edc'
print(test[::2])
출력: 'ace' (앞에 2칸씩 뒤)
print(test[::-2])
출력: 'eca' (뒤에서 2칸씩 앞으로)

#lambda function

## lambda의 역할은 함수 이름 없이 간단하게 함수를 만들고 싶을 때 사용합니다. 보통 콜백 함수나 한 번만 쓸 간단한 함수를 만들 때 많이 씁니다.
def add(x, y):
    return x + y

add = lambda x, y: x + y

#For in
# 1부터 5까지 숫자를 출력
# for in 문은 (0, n)이면 0부터 n-1까지 돈다
for i in range(1, 6):
    print(i)

#While
# 1부터 5까지 숫자를 출력
num = 1
while num <= 5:
    print(num)
    num += 1

#List repeat loop
# 리스트를 정의합니다.
fruits = ["사과", "바나나", "오렌지", "망고"]

# for 루프를 사용하여 리스트의 각 요소를 출력합니다.
for fruit in fruits:
    print(f"현재 과일: {fruit}")

#Tuple While loop
# 튜플을 정의합니다.
coordinates = (10, 20, 30, 40)

# while 루프와 인덱스를 사용하여 튜플의 각 요소를 출력합니다.
index = 0
while index < len(coordinates):
    print(f"좌표값 {index + 1}: {coordinates[index]}")
    index += 1

#Zip function
# 두 리스트 정의
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# zip으로 쌍을 묶음
paired = zip(names, ages)

# 결과를 리스트로 변환해 출력
print(list(paired))  # 출력: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Zip function with two different length list
letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3]

# zip으로 묶음
result = zip(letters, numbers)

# 결과 출력
print(list(result))  # 출력: [('a', 1), ('b', 2), ('c', 3)]

#Unzip
paired = list(zip(names, ages))
unzipped_names, unzipped_ages = zip(*paired)
print(unzipped_names)  # 출력: ('Alice', 'Bob', 'Charlie')
print(unzipped_ages)   # 출력: (25, 30, 35)
```



## C#(.NET)
# 32998_.NET_Application_Developments

#### Class: Student
#### Constructor : public Student(string name, int rollNumber, double grade)
#### Object: John doe, Nabin

```csharp
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
```csharp
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
```csharp
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
```csharp
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
```csharp
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

```csharp
List<int> numbers = new List<int> { 1, 2, 3 };

// 지연 실행
var query = numbers.Where(x => x > 1);
numbers.Add(4); // 새 데이터 추가
Console.WriteLine(query.Count()); // 3개 (2, 3, 4)

// 즉시 실행  
var list = numbers.Where(x => x > 1).ToList();
numbers.Add(5); // 새 데이터 추가
Console.WriteLine(list.Count); // 4개 (2, 3, 4만, 5는 포함 안됨)
```

LINQ
```csharp
LINQ(Language Integrated Query)는 C#에서 데이터를 쿼리(query)하는 강력한 도구야. 데이터를 쉽게 필터링, 정렬, 그룹화하거나 변환할 수 있도록 도와주는 문법으로, 실무에서 리스트, 배열, 데이터베이스 같은 데이터 소스를 다룰 때 자주 쓰여. SQL 비슷하지만 C# 코드 안에서 자연스럽게 사용할 수 있는 게 특징이야.

### 핵심 포인트
- **목적**: `List<T>`, 배열, XML, 데이터베이스 같은 데이터 소스에서 원하는 데이터를 간결하게 추출/조작.
- **주요 메서드**:
  - `Where`: 조건에 맞는 데이터 필터링 (예: `list.Where(x => x.Age > 20)`).
  - `Select`: 데이터 변환 또는 특정 속성 선택 (예: `list.Select(x => x.Name)`).
  - `OrderBy`: 데이터 정렬 (예: `list.OrderBy(x => x.Name)`).
  - `GroupBy`, `Sum`, `Average` 등: 그룹화, 집계 등 다양한 작업 가능.
- **문법**: 두 가지 스타일이 있어.
  - **메서드 구문**: `list.Where(p => p.Age < 30).OrderBy(p => p.Name)`.
  - **쿼리 구문**: SQL 비슷한 형태, 예: `from p in list where p.Age < 30 orderby p.Name select p`.
- **실무 활용**: 데이터베이스 쿼리, 리스트 필터링, 데이터 분석 등에서 시간 절약과 가독성 향상에 도움.

### 간단한 예시
var numbers = new List<int> { 1, 2, 3, 4, 5 };
var evenNumbers = numbers.Where(n => n % 2 == 0).ToList(); // 2, 4
```

#### C# 주요 연산자 (Common Operators)

**산술 연산자 (Arithmetic Operators)**
```csharp
int a = 10, b = 3;
Console.WriteLine(a + b);  // 13 (덧셈)
Console.WriteLine(a - b);  // 7  (뺄셈)
Console.WriteLine(a * b);  // 30 (곱셈)
Console.WriteLine(a / b);  // 3  (나눗셈)
Console.WriteLine(a % b);  // 1  (나머지)
```

**비교 연산자 (Comparison Operators)**
```csharp
int x = 5, y = 10;
Console.WriteLine(x == y);  // False (같음)
Console.WriteLine(x != y);  // True  (다름)
Console.WriteLine(x < y);   // True  (작음)
Console.WriteLine(x > y);   // False (큼)
Console.WriteLine(x <= y);  // True  (작거나 같음)
Console.WriteLine(x >= y);  // False (크거나 같음)
```

**논리 연산자 (Logical Operators)**
```csharp
bool p = true, q = false;
Console.WriteLine(p && q);  // False (AND)
Console.WriteLine(p || q);  // True  (OR)
Console.WriteLine(!p);      // False (NOT)
```

**할당 연산자 (Assignment Operators)**
```csharp
int num = 10;
num += 5;   // num = num + 5  (15)
num -= 3;   // num = num - 3  (12)
num *= 2;   // num = num * 2  (24)
num /= 4;   // num = num / 4  (6)
num %= 5;   // num = num % 5  (1)
```

**증감 연산자 (Increment/Decrement)**
```csharp
// 전위 증가 (++i): 먼저 증가시킨 후 값을 반환
int i = 5;
int result1 = ++i;  // i를 6으로 증가시킨 후 result1에 6 할당
Console.WriteLine($"i: {i}, result1: {result1}");  // i: 6, result1: 6

// 후위 증가 (i++): 현재 값을 반환한 후 증가
int j = 5;
int result2 = j++;  // result2에 5 할당 후 j를 6으로 증가
Console.WriteLine($"j: {j}, result2: {result2}");  // j: 6, result2: 5

// 전위 감소 (--i): 먼저 감소시킨 후 값을 반환
int k = 5;
int result3 = --k;  // k를 4로 감소시킨 후 result3에 4 할당
Console.WriteLine($"k: {k}, result3: {result3}");  // k: 4, result3: 4

// 후위 감소 (i--): 현재 값을 반환한 후 감소
int l = 5;
int result4 = l--;  // result4에 5 할당 후 l을 4로 감소
Console.WriteLine($"l: {l}, result4: {result4}");  // l: 4, result4: 5

// 반복문에서의 사용 예
for (int m = 0; m < 3; m++)  // 후위 증가 사용
{
    Console.WriteLine($"Loop: {m}");  // 0, 1, 2 출력
}
```

**비트 연산자 (Bitwise Operators)**
```csharp
int a = 12;  // 1100 (이진수)
int b = 10;  // 1010 (이진수)

// AND (&): 두 비트가 모두 1일 때만 1
Console.WriteLine(a & b);   // 8 (1000)

// OR (|): 두 비트 중 하나라도 1이면 1
Console.WriteLine(a | b);   // 14 (1110)

// XOR (^): 두 비트가 다르면 1
Console.WriteLine(a ^ b);   // 6 (0110)

// NOT (~): 비트 반전
Console.WriteLine(~a);      // -13 (보수)

// 왼쪽 시프트 (<<): 비트를 왼쪽으로 이동
Console.WriteLine(a << 2);  // 48 (110000, a * 4와 같음)

// 오른쪽 시프트 (>>): 비트를 오른쪽으로 이동
Console.WriteLine(a >> 2);  // 3 (0011, a / 4와 같음)

// 실용적인 예: 플래그 처리
[Flags]
enum Permission
{
    None = 0,     // 0000
    Read = 1,     // 0001
    Write = 2,    // 0010
    Execute = 4   // 0100
}

Permission userPerm = Permission.Read | Permission.Write;  // 0011
bool canRead = (userPerm & Permission.Read) != 0;         // true
bool canExecute = (userPerm & Permission.Execute) != 0;   // false
```

**복합 할당 비트 연산자 (Compound Bitwise Assignment)**
```csharp
int x = 12;  // 1100
x &= 10;     // x = x & 10, 결과: 8 (1000)
x |= 5;      // x = x | 5,  결과: 13 (1101)
x ^= 3;      // x = x ^ 3,  결과: 14 (1110)
x <<= 1;     // x = x << 1, 결과: 28 (11100)
x >>= 2;     // x = x >> 2, 결과: 7 (111)
```

**삼항 연산자 (Ternary Operator)**
```csharp
int age = 20;
string result = age >= 18 ? "성인" : "미성년자";
Console.WriteLine(result);  // "성인"
```

**null 병합 연산자 (Null-Coalescing Operators)**
```csharp
string name = null;
string displayName = name ?? "Unknown";  // null이면 "Unknown" 사용
Console.WriteLine(displayName);  // "Unknown"

// null 조건부 연산자
string text = null;
int? length = text?.Length;  // text가 null이면 null 반환
Console.WriteLine(length);   // null
``` Main()
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

#### Console 입출력 메서드

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

```csharp
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





### Python Error
```bash
# externally-managed-environment 에러.

(base) ➜  youtube-api-test git:(master) ✗ pip3 install google-api-python-client google-auth-oauthlib google-auth-httplib2

error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try brew install
    xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a Python library that isn't in Homebrew,
    use a virtual environment:
    
    python3 -m venv path/to/venv
    source path/to/venv/bin/activate
    python3 -m pip install xyz
    
    If you wish to install a Python application that isn't in Homebrew,
    it may be easiest to use 'pipx install xyz', which will manage a
    virtual environment for you. You can install pipx with
    
    brew install pipx
    
    You may restore the old behavior of pip by passing
    the '--break-system-packages' flag to pip, or by adding
    'break-system-packages = true' to your pip.conf file. The latter
    will permanently disable this error.
    
    If you disable this error, we STRONGLY recommend that you additionally
    pass the '--user' flag to pip, or set 'user = true' in your pip.conf
    file. Failure to do this can result in a broken Homebrew installation.
    
    Read more about this behavior here: <https://peps.python.org/pep-0668/>

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
(base) ➜  youtube-api-test git:(master) ✗ 

# Cause:  
Why create a virtual environment?  
1. Package isolation: Different versions of libraries can be used for each project.  
2. System protection: Does not affect the system Python.  
3. Dependency management: Install only the packages needed for each project.  

Relation to macOS security policies:  
Since macOS Monterey (12.3), **System Integrity Protection (SIP)** has been strengthened:  
- System Python protection: Restricts direct package installation to /usr/bin/python3.  
- Externally-managed-environment error: Error occurs during pip install.  
- Homebrew Python also affected: Prevents system-level installations.

# Solution
1. Create a virtual environment
python3 -m venv venv
2. Activate virtual environment
source venv/bin/activate
3. Install packages safely
pip install fastapi uvicorn
```

## AWS

####SES, SQS

-SQS 큐 생성
```
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name secureshifts-notifications 실행결과
```
Result:
{ "QueueUrl": "http://sqs.ap-southeast-2.localhost.localstack.cloud:4566/000000000000/secureshifts-notification" } ~ ~ ~ ~ ~ ~ ~ ~ (END)

이 결과는 LocalStack에서 SQS 큐가 정상적으로 생성되었음을 의미합니다.

"QueueUrl" 값은 새로 생성된 SQS 큐의 엔드포인트 URL입니다.
이 URL(http://sqs.ap-southeast-2.localhost.localstack.cloud:4566/000000000000/secureshifts-notification)을 통해 큐에 메시지를 보내거나 받을 수 있습니다.
실제 AWS가 아닌 LocalStack 환경에서만 동작하는 테스트용 큐 URL입니다.
즉, SQS 큐 생성이 성공적으로 완료되었고, 이후 코드나 AWS CLI에서 이 URL을 사용하면 됩니다.

-SES 인증확인 방법
SES 이메일 인증이 잘 되었는지 확인하려면 아래 방법을 사용하세요.


AWS CLI로 인증 상태 조회
아래 명령어를 실행하면 인증된 이메일 목록을 볼 수 있습니다.
```
aws --endpoint-url=http://localhost:4566 ses list-identities --identity-type EmailAddress
```
결과에 test@example.com이 있으면 인증이 등록된 것입니다.


인증 상세 정보 확인
이메일 인증 상태를 확인하려면 다음 명령어를 사용하세요.
```
aws --endpoint-url=http://localhost:4566 ses get-identity-verification-attributes --identities test@example.com
```
LocalStack에서는 실제 인증 메일이 오지 않으니, 위 명령어 결과만 확인하면 충분합니다.


## .NET

#### dotnet add
dotnet ***add package 패키지이름***은 .NET에서 NuGet 패키지를 프로젝트에 추가하는 명령어이고,
***npm install 패키지이름***은 Node.js에서 npm 패키지를 프로젝트에 추가하는 명령어입니다.
둘 다 외부 라이브러리를 프로젝트에 설치해서 사용할 수 있게 해주는 역할을 합니다.
결과의 VerificationStatus가 Success면 인증이 완료된 것입니다.



## DevOps
Shell
```shell
cpu_total_usage=$(top -l 1| grep "CPU" | awk '{print $3+$5"%"}')
#$()
#명령어 치환(command substitution)입니다. 괄호 안의 명령어를 실행한 결과(출력값)를 변수에 저장하거나 다른 명령어의 인자로 사용할 수 있게 해줍니다.

#top -l 1
#macOS에서 시스템의 현재 상태(프로세스, CPU, 메모리 등)를 한 번만 샘플링해서 출력하는 명령어입니다.
#-l 1에서 -l은 샘플 개수 옵션이고, 1은 한 번만 결과를 보여주라는 의미입니다

#|
#파이프(pipe)입니다. 앞의 명령어 출력을 뒤의 명령어 입력으로 전달합니다.

#grep "CPU usage"
#입력된 텍스트에서 "CPU usage"라는 문자열이 포함된 줄만 추출합니다.

#awk
#텍스트 데이터를 행과 열로 나눠서 처리할 수 있는 강력한 텍스트 처리 도구입니다.
#파이프(|)로 전달된 출력에서 원하는 열(필드)만 추출하거나, 계산, 변환, 필터링 작업을 할 때 사용합니다.
#예: awk '{print $3+$5"%"}'는 세 번째와 다섯 번째 필드를 더해서 %를 붙여 출력합니다.

#head
#파일이나 입력의 처음 몇 줄만 출력하는 명령어입니다.
#-n 옵션으로 출력할 줄 수를 지정할 수 있습니다.
#예: head -n 1은 첫 번째 줄만 출력, head -n 6은 처음 6줄 출력

#ps aux
#현재 실행 중인 모든 프로세스의 상세 정보를 보여주는 명령어입니다.
#a: 모든 사용자의 프로세스, u: 사용자 친화적 형식, x: 터미널에 연결되지 않은 프로세스도 포함

#sort
#텍스트 줄을 정렬하는 명령어입니다.
#-n: 숫자 정렬, -r: 역순 정렬, -k: 특정 열(필드) 기준 정렬
#예: sort -nrk 3은 3번째 열을 숫자로 역순 정렬

#tail
#파일이나 입력의 마지막 몇 줄만 출력하는 명령어입니다.
#-n 옵션으로 출력할 줄 수를 지정할 수 있습니다.
#예: tail -n 1은 마지막 줄만 출력

#df
#디스크 사용량을 보여주는 명령어입니다.
#-h: 사람이 읽기 쉬운 형식(K, M, G 단위)으로 출력
#예: df -h /는 루트 파티션의 디스크 사용량을 보여줌

#echo
#텍스트를 출력하는 명령어입니다.
#변수나 문자열을 화면에 표시할 때 사용합니다.

#if [[ ]]
#조건문입니다. 대괄호 두 개([[ ]])는 확장된 테스트 명령어로 더 많은 기능을 제공합니다.
#문자열 패턴 매칭, 정규식 등을 지원합니다.
#예: if [[ $var == *G ]]는 변수가 G로 끝나는지 확인

#sed
#스트림 편집기로 텍스트를 검색하고 치환하는 명령어입니다.
#'s/old/new/' 형식으로 문자열을 치환합니다.
#예: sed 's/G//'는 G 문자를 제거

#$(())
#산술 연산을 수행하는 구문입니다.
#정수 계산을 할 때 사용합니다.
#예: $((100 - used_percent))는 100에서 used_percent를 뺀 값

#printf
#형식화된 출력을 하는 명령어입니다.
#C언어의 printf와 유사하게 형식 지정자를 사용할 수 있습니다.
#예: printf "%.2f"는 소수점 둘째 자리까지 출력

#${}
#변수 확장(parameter expansion) 구문입니다.
#변수명을 명확히 구분하거나 변수 조작을 할 때 사용합니다.
#예: ${mem_used_percent}%는 변수 뒤에 %를 붙임

```

#### IP Concept
⏺ IP 주소의 기본 개념부터 설명

1. IP 주소란?

- Internet Protocol Address의 약자
- 네트워크상의 컴퓨터를 구분하는 주소 (집 주소와 비슷)
- 예: 192.168.1.1 형태의 숫자 조합

2. 공인 IP vs 사설 IP

공인 IP (Public IP)
- 인터넷에서 직접 접속 가능한 IP
- 전 세계에서 유일한 주소
- 예: 52.78.123.45 (예시 EC2)

사설 IP (Private IP)
- 내부 네트워크에서만 사용
- 인터넷에서 직접 접속 불가
- 예: 172.31.15.88 (예시 EC2 내부 IP)
- 사설 IP 대역:
    - 10.0.0.0 ~ 10.255.255.255
    - 172.16.0.0 ~ 172.31.255.255
    - 192.168.0.0 ~ 192.168.255.255

3. 왜 사설 IP가 필요한가?

집을 예로 들면:
- 공인 IP = 집 주소 (서울시 강남구 xxx)
- 사설 IP = 집 안의 방 번호 (큰방, 작은방)

회사를 예로 들면:
- 공인 IP = 회사 건물 주소
- 사설 IP = 사원 자리 번호 (3층 301호)

4. AWS VPC란?

VPC (Virtual Private Cloud)
- AWS에서 제공하는 가상의 사설 네트워크
- 당신만의 격리된 네트워크 공간
- 기본 VPC IP 대역: 172.31.0.0/16

5. EC2 상황 예시

인터넷 ←→ [52.78.123.45] ←→ AWS 라우터 ←→ [172.31.15.88] EC2 서버
(공인 IP/탄력적 IP)                (사설 IP/VPC 내부 IP)

실제 동작:
1. 외부에서 52.78.123.45으로 요청
2. AWS가 내부적으로 172.31.15.88로 전달
3. EC2 서버가 응답
4. AWS가 다시 외부로 전달

6. 왜 이렇게 나누나?

보안:
- 내부 IP는 외부에서 직접 공격 불가
- 방화벽으로 보호 가능

IP 절약:
- IPv4 주소 부족 문제 해결
- 하나의 공인 IP로 여러 내부 서버 운영 가능

관리:
- 내부 네트워크 구조를 숨길 수 있음
- 유연한 네트워크 구성 가능

7. 정리

EC2 서버 예시:
- 52.78.123.45 = 인터넷에서 접속할 때 쓰는 주소 (현관문)
- 172.31.15.88 = AWS 내부에서만 아는 주소 (실제 위치)
- SSH 접속 후 ubuntu@ip-172-31-15-88이 보이는 이유 = 서버 자신은 내부 IP만 알고 있음

#### NAT 개념
IPv4 주소 부족 문제와 해결책

1. IPv4 주소 부족 문제

IPv4 주소의 한계:
- 총 개수: 약 43억개 (2^32)
- 전 세계 인구: 80억명
- 스마트폰, 컴퓨터, IoT 기기 등... 주소가 모자람!

2. NAT으로 문제 해결

NAT (Network Address Translation) = 주소 변환 기술

집에서의 예시:
인터넷 ←→ [공유기: 1개 공인 IP] ←→ 집 안의 여러 기기
115.23.187.92         - 아빠 노트북: 192.168.0.11
- 엄마 폰: 192.168.0.12
- 내 컴퓨터: 192.168.0.13
- TV: 192.168.0.14
- 공인 IP 1개로 집안의 모든 기기가 인터넷 사용!

3. AWS에서의 활용

시나리오 1: 여러 EC2 서버 운영
인터넷 ←→ [NAT Gateway: 1개 공인 IP] ←→ VPC 내부 서버들
13.209.87.234           - 웹서버: 172.31.32.10
- DB서버: 172.31.32.11
- 백업서버: 172.31.32.12

시나리오 2: 로드 밸런서 사용
사용자들 ←→ [로드밸런서: 1개 공인 IP] ←→ 여러 웹서버
example-site.com         - 서버1: 172.31.8.21
- 서버2: 172.31.8.22
- 서버3: 172.31.8.23

4. 실제 예시: 카페

스타벅스 WiFi:
인터넷 ←→ [스타벅스 공인 IP 1개] ←→ 카페 안 손님들
121.134.95.200        - 손님A 폰: 10.0.1.101
- 손님B 노트북: 10.0.1.102
- 손님C 태블릿: 10.0.1.103
... 100명이 와도 OK!

5. 비용 절감 효과

공인 IP 각각 할당시:
- 서버 10대 = 공인 IP 10개 필요
- AWS 탄력적 IP 비용: 월 $3.6 × 10 = $36

NAT 사용시:
- 서버 10대 = 공인 IP 1개만 필요
- 비용: $3.6 (90% 절감!)

6. 현재 상황 예시

지금은 EC2 1대라서 직접 공인 IP 할당:
인터넷 ←→ [52.78.123.45] ←→ EC2 서버

나중에 서버가 늘어나면:
인터넷 ←→ [로드밸런서] ←→ EC2 서버1 (172.31.x.x)
←→ EC2 서버2 (172.31.x.x)
←→ EC2 서버3 (172.31.x.x)

핵심: 공인 IP 1개로 수백, 수천 대의 내부 서버를 운영할 수 있음!

## Java

#### Annotation
```java
  // 어노테이션이 없다면 직접 작성해야 함
  public class User {
      private String name;

      // Getter
      public String getName() {
          return name;
      }

      // Setter
      public void setName(String name) {
          this.name = name;
      }

      // 생성자들
      public User() {}
      public User(String name) {
          this.name = name;
      }
  }

  // 어노테이션 사용시
  @Getter
  @Setter
  @NoArgsConstructor
  @AllArgsConstructor
  public class User {
      private String name;
      // 끝! 위 코드들이 자동 생성됨
  }

```