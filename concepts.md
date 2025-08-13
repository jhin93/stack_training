# Training Source: https://roadmap.sh/

## Python

```python
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

```