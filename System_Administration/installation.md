# Apple Silicon (M2) 맥북 — 31338 Network Servers 설치 가이드

주요 변경점 두 가지: **CentOS는 UTM 대신 Fusion**으로 (Lab 1a가 VMware 실습이라서), **Windows는 ISO 설치 전에 OVA 변환 먼저** (몇 시간 절약 + Lab 조건 일치).

---

## 0단계 — 도구 설치

```bash
[x] # 1  UTM 설치 (Windows Server 에뮬레이션용)
brew install --cask utm

[x] # 2  OVA 변환 도구
brew install qemu

[x] # 3  telnet (Lab 1c 호스트 테스트용)
brew install telnet

[x] # 4  VMware Fusion 다운로드 페이지 열기 (Broadcom 계정 가입 → Fusion Pro 받아서 설치)
open "https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Fusion"
```

---

## 1단계 — CentOS (Lab 1a, 1b / 학습목표 1~5)

```bash
[x] # 5  ISO 폴더 생성
mkdir -p ~/VMs/iso && cd ~/VMs/iso

[] # 6  CentOS Stream 10 ARM64 다운로드 (AARNet 호주 미러 — 약 10MB/s)
#    -C -   : 중단된 다운로드 이어받기 (처음 받는 경우에도 그대로 동작)
#    --retry: 연결 끊김 시 자동 재시도
cd ~/VMs/iso
curl -C - -L -O --retry 10 --retry-delay 5 --retry-all-errors \
  https://mirror.aarnet.edu.au/pub/centos-stream/10-stream/BaseOS/aarch64/iso/CentOS-Stream-10-latest-aarch64-dvd1.iso

[] # 7  다운로드 확인 + 무결성 검증 (체크섬 계산에 1~2분 소요)
cd ~/VMs/iso
ls -lh CentOS-Stream-10-latest-aarch64-dvd1.iso
curl -sO https://mirror.aarnet.edu.au/pub/centos-stream/10-stream/BaseOS/aarch64/iso/CHECKSUM
grep -qi "$(shasum -a 256 CentOS-Stream-10-latest-aarch64-dvd1.iso | cut -d' ' -f1)" CHECKSUM \
  && echo "✅ 무결성 정상 — 설치 진행 가능" \
  || echo "❌ 불일치 — 파일 삭제 후 6번 다시 실행"

[] # 8  Fusion 실행
open -a "VMware Fusion"
```

> **미러 주의**
> - `mirror.stream.centos.org` (원본): 575KB/s로 느림 — 완료까지 4시간 이상
> - `ftp.swin.edu.au`: 파일 크기가 7.6GB로 **다른 빌드** — 이어받기 시 파일 깨짐
> - `mirror.aarnet.edu.au`: 9,993,977,856 bytes로 원본과 일치 + 10MB/s ← **이것만 사용**

[] **9. Fusion에서 VM 생성**

`File → New → Install from disc or image` → 위 ISO 선택

CPU **4** / RAM **4096MB** / 디스크 **40GB** / Network **Bridged**

[] **10. CentOS 설치 화면에서 (중요)**

- Software Selection → **Server with GUI** ← `graphical.target` 실습에 필수
- Root Account → **Enable root account**, 비밀번호 **`student123!`** ← Lab 문서와 일치

[] **11. 설치 완료 후 게스트 안에서**

```bash
sudo dnf install -y net-tools      # Lab 1a의 ifconfig
sudo dnf upgrade --refresh -y
uname -m                           # aarch64 나오면 성공
```

---

## 2단계 — Windows Server (Lab 1c / 학습목표 6~8)

### 2-A. OVA 변환 먼저 시도 (권장)

[] **12. SharePoint에서 OVA 다운로드** (UTS 로그인 필요)

```bash
open "https://studentutsedu.sharepoint.com/sites/CombinedLecture3133832520/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FCombinedLecture3133832520%2FShared%20Documents%2FServers%2FWindows%20Server%202025%2Eova&parent=%2Fsites%2FCombinedLecture3133832520%2FShared%20Documents%2FServers"
```

```bash
# 13  압축 해제
cd ~/Downloads && tar -xvf "Windows Server 2025.ova"

# 14  내용물 확인 (.ovf, .mf, .vmdk)
ls -lh

# 15  VMDK → qcow2 변환
qemu-img convert -p -O qcow2 *.vmdk ~/VMs/winserver2025.qcow2

# 16  UTM 실행
open -a UTM
```

[] **17. UTM에서 VM 생성**

`+` → **Emulate** → **Other** → **Skip ISO boot**

Architecture **x86_64** / System **Q35** / CPU **2** / RAM **4096MB**

[] **18. VM 설정 편집**

- 기본 디스크 삭제 → **Import Drive** → `~/VMs/winserver2025.qcow2`
- 디스크 인터페이스 **SATA** ← 부팅 성공률 핵심
- 네트워크 어댑터 **2개**, 둘 다 **Bridged** ← Lab 1c의 Ethernet0/Ethernet1
- **Force multicore 체크 해제**

[] **19. 부팅 → 로그인** (Administrator / `student123!`) → 검증

```cmd
systeminfo | findstr /B /C:"OS Name" /C:"System Type"
```

성공하면 **2-B 건너뛰고 23번으로**.

### 2-B. 변환 실패 시에만 — ISO 설치

```bash
# 20  평가판 ISO 받기 (브라우저)
open "https://www.microsoft.com/en-us/evalcenter/download-windows-server-2025"
```

[] **21. UTM에서 VM 생성**

`+` → **Emulate** → **Windows** → **x86_64** → ISO 선택

CPU **2** / RAM **4096MB** / 디스크 **64GB** / 네트워크 어댑터 **2개 Bridged** / **Force multicore 해제**

[] **22. 설치 옵션**

- **Desktop Experience** 선택 ← Server Manager 필요
- Administrator 비밀번호 **`student123!`**

---

## 3단계 — 마무리 설정

[] **23. Windows 게스트 안에서 속도 개선** (관리자 PowerShell)

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
SystemPropertiesPerformance.exe
```

[] **24. Windows 게스트에서 Lab 1c 준비**

- Server Manager → 시간대 **(UTC+10:00) Canberra, Melbourne, Sydney**
- Telnet Client + Simple TCP/IP Services 기능 추가
- 방화벽 규칙:

```cmd
netsh advfirewall firewall add rule name="TCP Port 17" dir=in action=allow protocol=TCP localport=17
```

[] **25. 맥(호스트)에서 연결 테스트**

```bash
telnet <윈도우서버_IP> 13
telnet <윈도우서버_IP> 17
```

---

## 체크리스트

| 단계 | 소요 | 완료 시 |
|---|---|---|
| 1~4 | 30분 | 도구 준비 |
| 5~11 | 1시간 | 학습목표 1~5 ✅ |
| 12~19 | 1시간 | 학습목표 6~8 ✅ |
| 20~22 | 하룻밤 | (17번 실패 시에만) |
| 23~25 | 30분 | Lab 1c 실습 준비 |

디스크 사용량 52GB, 설치 후 74GB 남습니다.

---

## 참고 — 학습목표 대조

| # | 학습 목표 | 맥북 도구 | 판정 |
|---|---|---|---|
| 1 | Navigate through the VMware | Fusion | ✅ |
| 2 | Log in as root, shut down Linux | Fusion + CentOS ARM64 | ✅ |
| 3 | Boot single-user shell (boot loader) | GRUB2 (ARM64 동일) | ✅ |
| 4 | Explore/modify startup scripts | systemd (동일) | ✅ |
| 5 | Examine system log information | journalctl (동일) | ✅ |
| 6 | Startup Windows Server 2025 | UTM Emulate | ⚠️ 느림 |
| 7 | Manage Windows Server 2025 | UTM Emulate | ⚠️ 느림 |
| 8 | Use PowerShell in Windows Server | UTM Emulate | ⚠️ 느림 |
