from datetime import datetime

def log_message(file_path, message, level="INFO"):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {level}: {message}\n"
    try:
        with open(file_path, 'a') as file:
            file.write(log_entry)
    except (FileNotFoundError, PermissionError) as e:
        print(f"로그 쓰기 실패: {str(e)}")

def read_logs(file_path, level=None):
    try:
        with open(file_path, 'r') as file:
            logs = file.readlines()
            if level:
                return [log.strip() for log in logs if f" {level}: " in log]
            return [log.strip() for log in logs]
    except FileNotFoundError:
        print("로그 파일을 찾을 수 없습니다.")
        return []
    except PermissionError:
        print("파일 읽기 권한이 없습니다.")
        return []

# 사용 예시
log_file = 'app.log'
log_message(log_file, "Application started", "INFO")
log_message(log_file, "Database connection failed", "ERROR")
log_message(log_file, "User request processed", "INFO")
log_message(log_file, "Invalid input detected", "ERROR")

# 전체 로그 읽기
print("=== 전체 로그 ===")
logs = read_logs(log_file)
for log in logs:
    print(log)

# ERROR 로그만 필터링
print("\n=== ERROR 로그만 ===")
error_logs = read_logs(log_file, level="ERROR")
for log in error_logs:
    print(log)