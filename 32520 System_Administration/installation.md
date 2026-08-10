# Apple Silicon (M2) 맥북 — 31338 Network Servers 설치 가이드

주요 변경점 두 가지: **CentOS는 UTM 대신 Fusion**으로 (Lab 1a가 VMware 실습이라서), **Windows는 ISO 설치 전에 OVA 변환 먼저** (몇 시간 절약 + Lab 조건 일치).

Centos 일반계정
Full Name: Jinkyung Kim
Username: student14657314
password: student123!

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

**설치 확인** (2026-08-05 기준 전부 완료)

| # | 도구 | 상태 |
|---|---|---|
| 1 | UTM | ✅ |
| 2 | qemu 11.0.3 | ✅ |
| 3 | telnet | ✅ |
| 4 | VMware Fusion 13.6.4 | ✅ |

---

## 0-1단계 — ISO 다운로드 기다리는 동안 (병렬 진행)

[] # 4-1  Fusion 첫 실행 → 라이선스·권한 처리 (지금 해두면 나중에 막히지 않음)
```bash
open -a "VMware Fusion"
```
- 라이선스 화면에서 **Personal Use License** 선택 (무료, 결제 아님)
- **시스템 확장 승인 요구 시**: 시스템 설정 → 개인정보 보호 및 보안 → 하단 "차단됨" 항목 허용
- **재부팅을 요구할 수 있습니다** ← ISO 다운로드 중이면 완료 후에 재부팅하세요

[] # 4-2  Windows Server 2025 OVA 다운로드 시작 (2단계 12번을 미리 당겨서 실행)
```bash
open "https://studentutsedu.sharepoint.com/sites/CombinedLecture3133832520/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FCombinedLecture3133832520%2FShared%20Documents%2FServers%2FWindows%20Server%202025%2Eova&parent=%2Fsites%2FCombinedLecture3133832520%2FShared%20Documents%2FServers"
```
> ISO 다운로드가 끝난 뒤 시작하는 게 안전합니다 (동시 다운로드 시 대역폭을 나눠 써서 둘 다 느려지고, 중단 위험도 커집니다).
> CentOS OVA는 받을 필요 없습니다 — ARM64 ISO로 설치하므로 x86 OVA는 못 씁니다.

---

## 1단계 — CentOS (Lab 1a, 1b / 학습목표 1~5)

```bash
[x] # 5  ISO 폴더 생성
mkdir -p ~/VMs/iso && cd ~/VMs/iso

[x] # 6  CentOS Stream 10 ARM64 다운로드 — aria2 사용 (curl 금지, 아래 주의사항 참고)
#    -c          : 이어받기 (중단돼도 같은 명령어 재실행하면 손상 구간만 복구)
#    -x 8 -s 8   : 연결 8개 분할 — 빠르고 하나 끊겨도 나머지가 계속
#    --max-tries=0: 무한 재시도 (curl --retry 와 달리 진행분을 날리지 않음)
brew install aria2
cd ~/VMs/iso
aria2c -c -x 8 -s 8 --max-tries=0 --retry-wait=5 --http-accept-gzip=false \
  https://mirror.aarnet.edu.au/pub/centos-stream/10-stream/BaseOS/aarch64/iso/CentOS-Stream-10-20260803.0-aarch64-dvd1.iso

[x] # 7  다운로드 완료 + 무결성 검증 (해시 계산에 1~2분 소요)
#    ⚠️ 파일 크기로 완료 판단 금지! aria2는 시작 시 10GB를 미리 할당하므로
#       ls -l / du 둘 다 처음부터 전체 크기를 보여줍니다.
#       진짜 완료 신호는 ".aria2 제어 파일이 사라지는 것" 입니다.
cd ~/VMs/iso
ISO=CentOS-Stream-10-20260803.0-aarch64-dvd1.iso
EXPECT=8c9d50178741256676b8878fe36e953088e34936d8b3a189a007a3e04e13d7dd

[ ! -f "$ISO.aria2" ] \
  && [ "$(stat -f%z "$ISO")" = "10003546112" ] \
  && [ "$(shasum -a 256 "$ISO" | cut -d' ' -f1)" = "$EXPECT" ] \
  && echo "✅ 무결성 정상 — 설치 진행 가능" \
  || echo "❌ 미완료 또는 손상 — 6번 명령어 재실행 (이어받기)"

[x] # 8  Fusion 실행
open -a "VMware Fusion"
```

> **✅ 검증 완료 (2026-08-05)**
> 크기 10,003,546,112 bytes / SHA256 `8c9d5017...d7dd` 일치 확인

> **⚠️ 빌드 고정이 중요한 이유 (실제로 겪은 문제)**
> `CentOS-Stream-10-**latest**-...iso` 는 심볼릭 링크라 새 빌드가 나오면 가리키는 대상이 바뀝니다.
> 7/29에 받기 시작 → 8/3에 새 빌드(20260803.0) 릴리스 → 8/5에 이어받기 하자
> **앞부분은 옛 빌드, 뒷부분은 새 빌드**가 섞여 파일이 깨졌습니다 (크기도 9,993,977,856 → 10,003,546,112로 변경).
> 며칠에 걸쳐 받을 때는 반드시 **버전 고정 파일명**을 쓰세요.
>
> **⚠️ curl `--retry` 를 쓰지 마세요 (실제로 겪은 문제)**
> `curl -C - --retry` 조합은 재시도할 때 출력 파일을 다시 열면서 **받아둔 진행분을 통째로 버립니다.**
> 4.5GB까지 받은 상태에서 HTTP/2 스트림이 끊기자(`curl: (92) ... CANCEL (err 8)`)
> 재시도가 0부터 다시 시작해 4.5GB가 날아갔습니다.
> aria2는 `.aria2` 제어 파일에 구간별 상태를 기록해서 이런 일이 없습니다.
>
> **미러 주의**
> - `mirror.stream.centos.org` (원본): 575KB/s — 4시간 이상
> - `ftp.swin.edu.au`: 다른 빌드를 서빙 — 사용 금지
> - `mirror.aarnet.edu.au`: 10MB/s ← **이것만 사용**
>
> **체크섬 파일 경로:** `CHECKSUM` 이 아니라 `<ISO파일명>.SHA256SUM` 입니다.
> 새 빌드로 갱신할 때는 여기서 확인:
> `https://mirror.aarnet.edu.au/pub/centos-stream/10-stream/BaseOS/aarch64/iso/`

[x] **9. Fusion에서 VM 생성**

`File → New → Install from disc or image` → 위 ISO 선택
→ Choose Operating System에서 **Linux → Red Hat Enterprise Linux 9 64-bit Arm**
→ **Customize Settings** 클릭 시 저장 대화상자가 먼저 뜸 (정상). 이름 `CentOS10-NetServers` 로 저장하면 설정 창이 열림

CPU **4** / RAM **4096MB** / 디스크 **40GB** / Network **Bridged**

[x] **10. CentOS 설치 화면에서 (중요) — Installation Summary 4곳**

- **Software Selection** → **Server with GUI** ← 기본값이 GUI 없는 Server. `graphical.target` 실습에 필수
- **Network & Hostname** → 우측 토글 **ON** (기본 OFF!) + 호스트명 `centos10` ← 안 켜면 설치 후 `dnf` 불가
- **Installation Destination** → 디스크 선택 후 Done. 파티션은 **Automatic** 유지 ← Lab 2d가 `/boot` + LVM 구조를 전제
- **Root Account** → **Enable root account**, 비밀번호 **`student123!`** (약한 비밀번호 경고 시 Done 두 번)

> 설치 후 재부팅하면 GNOME 초기 설정이 **일반 사용자 생성을 요구**합니다 (건너뛸 수 없음).
> Username은 소문자 **`student`** / 비밀번호 `student123!` 로 만드세요.
> Lab01a의 `SuperUser` 는 계정명이 아니라 **root를 가리키는 표현**입니다 ("Log in as the root user, also known as the superuser").
> 일반 계정이 있어야 Lab01a가 가르치는 `su` 실습이 성립합니다.
> Online Accounts 화면은 **Skip** (Lab01a 지시사항).

[x] **11. 설치 완료 후 게스트 안에서**

```bash
uname -m                           # aarch64 나오면 성공
ip link show                       # 인터페이스 이름 확인 (Lab02b의 ens160)

su -                               # 비밀번호 student123! → 프롬프트가 # 로 변경
dnf install -y net-tools open-vm-tools-desktop
dnf upgrade --refresh -y
reboot
```

| 패키지 | 이유 |
|---|---|
| `net-tools` | Lab 1a의 `ifconfig` |
| `open-vm-tools-desktop` | 맥↔VM 클립보드 공유 + 화면 자동 리사이즈 (실습 편의상 필수) |

[x] **11-1. 스냅샷 (필수)**

**Virtual Machine → Snapshots → Take Snapshot** → 이름 `clean-install`

> 확인 방법: Snapshots 창에 `clean-install` → `Current State` 로 연결된 트리가 보이면 성공 (약 8.5GB 사용).
> 복구할 때는 `clean-install` 썸네일 선택 → 상단 되돌리기 아이콘 클릭.

[] **11-2. ISO 삭제로 디스크 확보 (2단계 시작 전 권장)**

```bash
# 순서 중요: 먼저 Virtual Machine → Settings → CD/DVD 연결 해제 후 삭제
rm ~/VMs/iso/CentOS-Stream-10-20260803.0-aarch64-dvd1.iso   # 9.3GB 확보
```

> 2단계 변환 과정에서 OVA(7GB) + VMDK(25GB) + qcow2(25GB)가 동시에 존재하는 구간이 있어
> 여유가 17GB까지 떨어집니다. ISO를 미리 지우면 26GB로 올라가 안전합니다.
> 재설치가 필요하면 6번으로 다시 받으면 됩니다 (17분).

> Lab 1b에서 GRUB 부트 파라미터를 편집해 single-user 모드로 진입합니다. 망가뜨려도 여기로 복구 가능.
> Lab02d도 "Remember to take a snapshot of the virtual machines!" 라고 명시.

---

## 2단계 — Windows Server (Lab 1c / 학습목표 6~8)

### 2-A. OVA 변환 먼저 시도 (권장)

[x] **12. SharePoint에서 OVA 다운로드** (UTS 로그인 필요)

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

[x] **17. UTM에서 VM 생성**

`+` → **Emulate** → **Other**
- Boot Device: **None** ← 최신 UTM에서 `Skip ISO boot` 가 이걸로 바뀜
- **UEFI Boot: 체크 유지** ← 필수. 수업 OVA는 GPT/UEFI 설치본
- Hardware: Machine **Intel ICH9 based PC (2009, x86_64)** (= Q35) / Memory **4096** MiB / CPU Cores **2**
- Storage: **1GB** (임시, 18번에서 삭제)

> **UEFI 여부 확인법** (다른 OVA를 쓸 때):
> ```bash
> qemu-img dd -f qcow2 -O raw if=~/VMs/winserver2025.qcow2 of=head.img bs=512 count=64
> xxd -s 512 -l 16 head.img   # "EFI PART" 보이면 GPT → UEFI Boot 켜기
> xxd -s 450 -l 1  head.img   # 0xEE 면 보호용 MBR → GPT 확정
> rm head.img
> ```

[x] **18. VM 설정 편집** (VM 우클릭 → Edit → 사이드바 맨 아래 **Drives**)

- 1GB 임시 디스크 선택 → **Delete**
- **+ New... → Import Drive** → `~/VMs/winserver2025.qcow2`
- 디스크 인터페이스 **IDE 유지** ← ⚠️ UTM에 SATA 항목은 없음. **Q35에서는 IDE가 곧 AHCI(SATA)**
  (실패 시 대안 순서: IDE → NVMe → SCSI. **VirtIO는 금지** — Windows에 기본 드라이버 없어 무조건 BSOD)
- 네트워크 어댑터 **2개**, 둘 다 **Bridged** ← Lab 1c의 Ethernet0/Ethernet1
- System → **Force Multicore 꺼짐** 확인

[x] **19. 부팅 → 로그인** (Administrator / `student123!`) → 검증

> 잠금화면에서 키보드가 안 먹히면 **VM 화면 안을 먼저 클릭**해 입력 포커스를 넘긴 뒤
> `Ctrl` + `Option(⌥)` + `Fn` + `Delete` (맥의 Delete는 Backspace라 `Fn` 필요).
> 그래도 안 되면 툴바의 **커서 아이콘**으로 입력 캡처 후 재시도 (해제는 `Ctrl`+`Option`).

```cmd
systeminfo | findstr /B /C:"OS Name" /C:"System Type"
ipconfig /all
```

> **✅ 2026-08-11 부팅 성공.** Server Manager 정상 실행 확인.
> ISO 재설치(2-B) 불필요 — **20~22번 건너뛰고 23번으로**.

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
