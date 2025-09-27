import csv

input_file = 'sales_data.csv'
output_file = 'filtered_sales_data.csv'

min_quantity = 10

filtered_data = [] # 필터링된 데이터를 저장할 빈 리스트 초기화

try:
    with open(input_file, 'r', newline='', encoding='utf-8') as file: # 입력 CSV 파일을 읽기 모드('r')로 열고, UTF-8 인코딩으로 한글/특수문자 문제 방지. newline=''은 OS간(mac, window) 줄바꿈 차이로 인한 CSV 파싱 오류 방지. 목적: CSV 파일을 읽거나 쓸 때 줄바꿈 문자로 인한 데이터 파싱 오류나 불필요한 공백 줄 삽입을 방지한다. 특히 Windows에서 CSV 파일을 쓸 때 \r\n이 기본값인데, 
        # newline=''를 설정하면 csv 모듈이 줄바꿈을 올바르게 처리해 데이터 무결성을 유지한다.
        reader = csv.DictReader(file) # CSV 파일을 딕셔너리 형태로 읽기 위해 DictReader 사용
        print("reader : ", reader) # print(reader)가 데이터를 보여주지 않는 이유는 DictReader가 데이터를 직접 저장하는 리스트가 아니라, 파일 스트림을 읽는 이터레이터이기 때문이야.
        headers = reader.fieldnames # CSV 파일의 헤더(열 이름)를 저장
        for row in reader: # DictReader는 CSV 파일을 한 줄씩 읽어서 각 줄을 딕셔너리 형태로 반환하는 이터레이터야. 즉, for row in reader:는 파일의 각 행을 하나씩 가져와 row 변수에 딕셔너리로 할당하는 거야.
            print("reader row", row)
            if int(row['quantity']) >= min_quantity:
                filtered_data.append(row)
    if filtered_data:
        with open(output_file, 'w', newline='', encoding='utf-8') as file: # 출력 CSV 파일을 쓰기 모드('w')로 열고, UTF-8 인코딩 사용. newline=''은 줄바꿈 처리 일관성 유지
            writer = csv.DictWriter(file, fieldnames=headers) # DictWriter를 사용해 딕셔너리 데이터를 CSV로 쓰기 위한 객체 생성
            writer.writeheader() # 출력 파일에 헤더(열 이름)를 작성
            for row in filtered_data:
                print("writer row", row)
                writer.writerow(row) # 각 행을 CSV 파일에 작성
    print(f"filtered data was stored in {output_file}")
except FileNotFoundError:
    print(f"Error: The file {input_file} was not found.")
except Exception as e: # 기타 예외 상황 처리
    print(f"An error occurred: {e}") # 발생한 예외의 세부 정보를 출력