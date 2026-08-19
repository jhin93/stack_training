# Lab Quiz 1 — 개념 정리

**형식:** 객관식 10문항 / 20분 / 5점 / 대면 개별 평가
**범위:** "networking concepts covered so far" → **Week 4 DHCP (70%) + Week 3 정적 네트워킹 (25%)**

> Week 1(GRUB, systemd, 로그)·Week 2(man, dnf, 프로세스, 파티션)는 네트워킹 주제가 아니므로 우선순위 낮음.
> 단, Week 4 강의가 슬라이드 2~5를 **Lab 3a Recapture**에 썼으므로 Week 3는 확실히 출제 범위.

---

## 1. 왜 DHCP가 필요한가

컴퓨터가 네트워크에서 통신하려면 최소 4가지가 필요합니다.

| 항목 | 역할 |
|---|---|
| **IP address** | 내 주소 |
| **Subnet mask** | 어디까지가 우리 동네인지 |
| **Default gateway** | 동네 밖으로 나가는 출구 |
| **DNS server** | 이름을 주소로 바꿔주는 곳 |

**Static IP configuration**(정적 설정)은 이 4가지를 관리자가 손으로 넣는 방식.
강의 슬라이드의 질문: *"How to cope with **10000 machines**?"*

**DHCP (Dynamic Host Configuration Protocol)** = 서버가 자동으로 나눠주는 방식.

> ★ DHCP의 목적 = **reduces network complexity and administration**

---

## 2. 호텔 비유로 전체 그림

| DHCP 용어 | 호텔로 치면 |
|---|---|
| **DHCP server** | 프런트 데스크 |
| **Scope** | 배정 가능한 객실 번호 범위 |
| **Lease** | 숙박권 — **기간이 정해져 있음** |
| **Lease renewal** | 연장 |
| **Reservation** | VIP 전용 지정 객실 |
| **Exclusion range** | 배정에서 빼둔 방 |

핵심: DHCP 주소는 "주는" 게 아니라 **빌려주는(lease)** 것. 기간이 끝나면 회수.

> ★ lease는 **특정 adapter의 MAC address**에 대해 **정해진 기간** 동안 발급되며, 시간이 지나면 **바뀔 수 있음**.

---

## 3. Broadcast와 포트

**문제:** 갓 켜진 클라이언트는 자기 IP도, 서버 위치도 모름 → 동네 전체에 소리침 = **broadcast**

```
Broadcast 주소 : 255.255.255.255
```

같은 local network의 모든 장비가 수신.

| 포트 | 누가 씀 |
|---|---|
| **UDP 67** | **Server** |
| **UDP 68** | **Client** |

> ★ **UDP**입니다. 객관식에서 "TCP 67/68" 오답이 잘 나옴.

---

## 4. DORA — Lease Generation 4단계 ★★★ 최빈출

주소를 **처음 받을 때**의 4단계.

| 순서 | 메시지 | 보내는 쪽 | 내용 |
|---|---|---|---|
| **D** | **DHCPDISCOVER** | **Client** → broadcast | "DHCP 서버 계세요?" |
| **O** | **DHCPOFFER** | **Server**(들) → broadcast | "이 주소 어때요?" (lease 정보 포함) |
| **R** | **DHCPREQUEST** | **Client** → broadcast | "1번 서버 것으로 할게요" |
| **A** | **DHCPACK** | **선택된 Server** | "확정" |

**왜 REQUEST도 broadcast인가** — 서버가 여러 대일 수 있음. 1번을 골랐다고 broadcast로 알려야 **2번 서버가 자기 OFFER를 회수**함.

> ★ 함정: 순서 뒤섞기 / OFFER를 client가 보낸다 / ACK를 client가 보낸다

---

## 5. DORA 외의 메시지 3개

| 메시지 | 누가 | 언제 |
|---|---|---|
| **DHCPNAK** | Server | 요청을 **거부**할 때 (ACK의 반대) |
| **DHCPDECLINE** | **Client** | 받은 주소가 **이미 사용 중(duplicate)** 일 때 |
| **DHCPRELEASE** | Client | 주소를 **반납**할 때 |

> ★ **DECLINE은 client가 보냄**. 키워드는 "duplicate address".

---

## 6. Lease Renewal — 갱신 ★★

```
Lease duration의 50%가 지나면
   Client → DHCPREQUEST
   Server → DHCPACK
```

| | Lease Generation | Lease Renewal |
|---|---|---|
| 단계 수 | **4단계 (DORA)** | **2단계** |
| 흐름 | DISCOVER→OFFER→REQUEST→ACK | **REQUEST→ACK** |
| 시점 | 최초 접속 | **50% 경과** |

**왜 DISCOVER가 없나** — 이미 서버를 알고 있으니 찾을 필요 없음.

> ★ **50%** 와 **2단계**. "75%", "100%", "4단계"가 오답으로 나옴.

---

## 7. Scope — 임대할 주소의 범위

```
scope = range of IP addresses for leasing
```

Windows 용어. Linux(kea)에서는 **pool** 또는 **range**.

**Scope의 7가지 속성**

| Property | 의미 |
|---|---|
| **Network ID** | 주소 범위의 네트워크 ID |
| **Subnet mask** | 서브넷 마스크 |
| **Network IP address range** | 클라이언트에게 줄 주소 범위 |
| **Lease duration** | 서버가 주소를 붙잡아두는 **기간** |
| **Router** | 클라이언트가 **remote network**에 접근하게 해주는 옵션 (= gateway) |
| **Scope name** | 관리용 이름 (기능 없음) |
| **Exclusion range** | 범위 안에서 **임대 제외**할 주소들 |

> ★ **Exclusion range** 정의: "scope 안에 있지만 임대되지 않는 주소 범위"

---

## 8. Reservation — 특정 장비 고정 IP ★★

```
Reservation = fixed IP address for a specific DHCP client
```

- **MAC address**로 장비를 식별
- server, printer처럼 주소가 바뀌면 곤란한 장비에 사용
- 슬라이드 표현: *"to avoid assigning inadvertently to another device"*

### Exclusion range vs Reservation

| | Exclusion range | Reservation |
|---|---|---|
| 하는 일 | 그 주소를 **아무에게도 안 줌** | 그 주소를 **특정 MAC에게만 줌** |
| 결과 | 주소가 비어 있음 | 지정 장비가 항상 같은 주소 |

### MAC 표기법 — 함정 ★

| 시스템 | 구분자 | 예시 |
|---|---|---|
| **Linux (kea)** | **colon `:`** | `1a:1b:1c:1d:1e:1f` |
| **Windows DHCP Manager** | **dash `-`** | `1A-1B-1C-1D-1E-1F` |

Lab04b 원문: *"MAC address must be entered in the format with **dashes**"*

---

## 9. 80:20 Rule ★

DHCP 서버 **두 대** 운영 시 주소 분배 비율.

```
DHCP Server1 : 80%   (192.168.1.60 – 192.168.1.254)
DHCP Server2 : 20%   (192.168.1.10 – 192.168.1.59)
```

> ★ 목적 = **fault tolerance / availability 향상**. "속도 향상", "보안"은 오답.

---

## 10. Linux 구현 — kea ★

| 항목 | 값 |
|---|---|
| Package | **`kea`** (구식: `dhcp-server`, `dhclient`, `dhcpd`) |
| 설치 | `dnf install kea` |
| Config file | **`/etc/kea/kea-dhcp4.conf`** |
| 문법 검사 | `kea-dhcp4 -t kea-dhcp4.conf` |
| Service | `systemctl start\|status **kea-dhcp4**` |
| Lease log | **`/var/lib/kea/kea-leases4.csv`** |

**방화벽 — CentOS는 기본 차단**
```bash
firewall-cmd --add-service=dhcp --permanent
firewall-cmd --reload
```

**설정 파일 핵심 항목**
```json
"interfaces": ["ens192"]                         어느 NIC에서 서비스할지
"subnet": "10.0.2.0/24"                          서브넷
"pools": [{"pool": "10.0.2.101 - 10.0.2.200"}]   임대 범위
"routers" → "10.0.2.1"                           게이트웨이
"domain-name-servers" → "8.8.8.8"                DNS
"domain-search" → "it.uts.edu.au"                검색 도메인
"reservations" → hw-address + ip-address         예약
```

---

## 11. Windows 구현

```
설치  : Server Manager → Manage → Add Roles and Features → DHCP Server
관리  : Server Manager → Tools → DHCP → DHCP Manager
Scope : IPv4 우클릭 → New Scope
예약  : Scope 확장 → Reservations
```

**Windows 클라이언트 명령어** ★

| 명령어 | 동작 |
|---|---|
| `ipconfig /release` | 리스 **반납** (DHCPRELEASE) |
| `ipconfig /renew` | 리스 **갱신 요청** |
| `ipconfig /all` | 전체 설정 확인 |

---

## 12. Week 3 복습 — nmconnection 파일 ★★

**위치:** `/etc/NetworkManager/system-connections/<이름>.nmconnection`

| 키 | 의미 |
|---|---|
| **`method=auto`** | **DHCP로 자동 할당** ← 동적 |
| **`method=manual`** | **정적 설정** |
| **`autoconnect=true`** | 부팅 시 자동 활성화 |
| `address1=10.0.2.1/24` | IP/prefix |
| `gateway=10.0.2.1` | 게이트웨이 |
| `dns=1.1.1.1;2.2.2.2;` | DNS (세미콜론 구분) |
| `dns-search=it.uts.edu.au;` | search domain |

> ★ **`method=auto` = DHCP**, **`method=manual` = static**

**관련 명령어**
```bash
nmcli con reload|down|up <ens160|ens192>
nmtui                          대화형 도구
hostnamectl set-hostname Linux
cat /etc/hostname              호스트명 확인
cat /etc/resolv.conf           DNS/search domain 확인
route -n                       라우팅 테이블
ifconfig ens192 / ip addr show ens192
```

---

## 13. 토폴로지 — 문제 지문 배경 ★

```
VMnet2 (private)  10.0.2.0/24
   ├─ CentOS        ens192
   └─ Windows       Ethernet1

NAT               192.168.228.0/24
   ├─ CentOS        ens160
   └─ Windows       Ethernet0
```

- 각 VM은 **v-NIC(virtual Network Interface Card) 2개**
- **The gateway will be the CentOS machine** — CentOS가 사설망의 라우터
- 사설망 범위: `10.0.2.0/24` ~ `10.0.2.254`

---

## 최종 암기 카드

| 질문 | 답 |
|---|---|
| DHCP 포트 | **UDP 67 (server) / 68 (client)** |
| Broadcast 주소 | **255.255.255.255** |
| Lease 생성 순서 | **DISCOVER → OFFER → REQUEST → ACK (DORA)** |
| Lease 갱신 시점 | **50%** |
| Lease 갱신 단계 | **REQUEST → ACK (2단계)** |
| 중복 주소 발견 시 | **DHCPDECLINE** (client가 보냄) |
| 서버의 거부 응답 | **DHCPNAK** |
| Scope | 임대할 IP 주소 **범위** |
| Reservation | **MAC 기반** 고정 IP |
| Exclusion range | scope 안에서 **임대 제외**되는 범위 |
| 80:20 rule 목적 | **fault tolerance / availability** |
| Linux DHCP 패키지 | **kea** |
| Linux 설정 파일 | **/etc/kea/kea-dhcp4.conf** |
| Lease 로그 | **/var/lib/kea/kea-leases4.csv** |
| DHCP = 동적 (nmconnection) | **method=auto** |

---

# 오답 노트

> 연습문제에서 틀린 내용을 여기에 누적합니다.
> 형식: **문제 요지 → 내가 고른 답(오답) → 정답 → 왜 틀렸나**

<!-- 아래에 계속 추가 -->

### 오답 1 — DHCP는 TCP가 아니라 UDP

- **문제:** DHCP communication uses TCP ports 67 and 68
- **내 답:** 맞다고 선택 (오답)
- **정답:** 틀림 — **UDP** 67/68
- **왜:** DHCP 시작 시점의 client는 ① 자기 IP가 없고 ② 서버 위치도 모름.
  TCP는 3-way handshake를 위해 양쪽 주소를 알아야 하므로 사용 불가.
  → **connectionless인 UDP + broadcast**가 유일한 방법.

### 오답 2 — Broadcast는 router를 넘지 못한다

- **문제:** A broadcast packet is forwarded by routers to hosts on all other subnets
- **내 답:** 맞다고 선택 (오답)
- **정답:** 틀림 — `255.255.255.255`는 **limited broadcast**로 **로컬 세그먼트에서 멈춤**
- **왜:** 이것이 **DHCP relay agent**가 존재하는 이유.
  서버가 다른 subnet에 있으면 broadcast가 도달 불가 →
  relay agent가 대신 받아 서버로 unicast 전달.
  슬라이드: *"DHCP server can be relayed through an agent"*
- **인과로 기억:** broadcast가 router를 못 넘음 → 그래서 relay agent 필요

### 오답 3 — Lease는 MAC address 기준으로 발급된다

- **문제:** A lease is issued for a specific adapter's MAC address
- **내 답:** 선택 안 함 (놓침)
- **정답:** 맞음
- **왜:** 슬라이드 원문 *"'lease' is for a specific adapter **MAC** & for **specified length of time**"*
- **lease의 속성 2가지:** ① 대상 = adapter의 **MAC address** ② 기간 = 정해진 시간
- **주의:** 같은 문장에서 "Will change over time"이 나오므로
  "영구적으로 유지된다"는 보기는 **오답**. 두 보기가 짝으로 출제되는 패턴.

### 오답 4 — DHCPREQUEST는 unicast가 아니라 broadcast

- **문제:** The client sends the DHCPREQUEST packet as a unicast directly to the chosen server only
- **내 답:** 맞다고 선택 (오답)
- **정답:** 틀림 — REQUEST도 **broadcast**
- **슬라이드 원문:** *"DHCP client **broadcasts** a DHCPREQUEST packet"*
- **왜 broadcast여야 하나:**
  - DISCOVER 하나에 Server1, Server2가 각각 OFFER를 보내고 **각자 주소를 임시 예약**함
  - REQUEST를 unicast로 Server1에만 보내면 → Server2는 소식을 몰라
    **자기가 제안한 주소를 타임아웃까지 계속 붙잡음 (주소 낭비)**
  - broadcast로 보내면 → Server2도 듣고 **제안 주소를 pool에 반납**
  - REQUEST 안에 "내가 고른 서버는 누구다"가 들어 있고, 모두가 듣게 만드는 것이 목적
- **★ 정리: DORA 중 D, O, R = broadcast / A(ACK) = 선택된 서버의 응답**

### 오답 5 — Scope의 정의를 놓침

- **문제:** A scope is a range of IP addresses available for leasing
- **내 답:** 선택 안 함 (놓침)
- **정답:** 맞음 — 슬라이드의 **정의 문장** 그 자체
- **슬라이드 원문:** `scope = range of IP addresses for leasing` (두 번 반복 등장)
- **함께 나온 오답:** "Scope name은 서버가 주소를 정하는 데 쓴다" → **틀림**.
  Scope name = *"An alphanumeric identifier for **administrative purposes**"*
  = 사람이 알아보기 위한 **이름표일 뿐**, 서버 동작에 관여하지 않음

### 오답 6 — Reservation은 MAC address로 식별한다

- **문제:** A reservation identifies the client by its MAC address
- **내 답:** 선택 안 함 (놓침)
- **정답:** 맞음
- **슬라이드 원문:** *"To configure a reservation, Server must obtain the device's **MAC address**."*
- **왜 MAC인가:** 주소를 주기 **전에** 상대를 알아볼 수단이 MAC뿐임
  - IP → 아직 안 줬으니 없음 / 호스트명 → 신뢰 불가, 변경 가능 / **MAC → NIC에 고정, 유일** ✅

### 오답 7 — MAC 표기법: Windows는 dash, Linux는 colon

- **문제:** On a Windows DHCP server, the MAC must be entered with **colons**
- **내 답:** 맞다고 선택 (오답)
- **정답:** 틀림 — Windows는 **dash `-`**
- **근거:**
  - Lab04a(Linux/kea): *"MAC address format is with **colons** between each pair of hex digits"*
  - Lab04b(Windows): *"must be entered in the format with **dashes** ... rather than colons"*
  - Lab04b 경고: 형식이 틀리면 *"The unique identifier you have entered may not be correct"* 오류

### 오답 8 — 80:20 rule은 서버 "두 대"로 나누는 것

- **문제:** It splits a scope's addresses between two DHCP servers
- **내 답:** 선택 안 함 (놓침)
- **정답:** 맞음
- **왜:** 80:20의 전제 자체가 **DHCP 서버 2대**. 한 대면 나눌 이유가 없음.
  목적이 **이중화(fault tolerance / availability)** 이므로 당연히 2대.

---

## ★ 약점 보강 — MAC address 집중 정리

> Set 1 Q3-1, Set 3 Q8-2를 **연속으로 놓침**. MAC 관련 보기가 반복 약점.

DHCP에서 MAC이 나오는 곳은 **3군데**:

| 위치 | 내용 |
|---|---|
| **Lease** | lease는 특정 adapter의 **MAC**에 대해 발급됨 |
| **Reservation** | **MAC**으로 클라이언트를 식별해 고정 IP 부여 |
| **표기법** | Linux(kea) = **colon `:`** / Windows = **dash `-`** |

**보기에 "MAC address"가 보이면 일단 맞을 확률이 높다.**
DHCP에서 MAC은 클라이언트를 식별하는 **유일한 수단**이기 때문.

---

## ★ 선택 경향 메모

- Set 1: **과다 선택** (틀린 보기를 포함)
- Set 3: **과소 선택** (맞는 보기를 누락)
- 대응: 보기 하나하나를 **독립적으로 O/X 판단**할 것.
  "이 정도면 맞나?" 대신 **"슬라이드에 이 문장이 있었나?"** 로 판단.

---

### 오답 9 — `--permanent` 만으로는 적용되지 않는다

- **문제:** `firewall-cmd --reload` must be run for the permanent rule to take effect
- **내 답:** 선택 안 함 (놓침)
- **정답:** 맞음 — 두 명령은 **항상 세트**
- **왜:** firewalld는 규칙을 두 곳에 보관
  - **Runtime** = 지금 동작 중인 규칙 (재부팅 시 소멸)
  - **Permanent** = 설정 파일에 저장 (재부팅해도 유지)
  - `--permanent` → **설정 파일에만 씀**, 동작 중인 방화벽은 그대로
  - `--reload` → 설정 파일을 다시 읽어 **runtime에 반영**
- `--permanent` 만 하면 **재부팅 전까지 DHCP가 차단된 상태**로 남음

### 오답 10 — `ipconfig /release` 는 표시가 아니라 반납

- **문제:** On a Windows client, `ipconfig /release` displays the full network configuration
- **내 답:** 맞다고 선택 (오답)
- **정답:** 틀림 — 표시는 `/all`

| 명령어 | 하는 일 | 대응 DHCP 메시지 |
|---|---|---|
| `ipconfig /release` | 리스 **반납** | **DHCPRELEASE** |
| `ipconfig /renew` | 리스 **요청/갱신** | DHCPDISCOVER 또는 DHCPREQUEST |
| `ipconfig /all` | 설정 **표시** | (없음) |

- **연결 기억:** DHCPRELEASE 메시지를 실제로 발생시키는 명령이 `/release`

### 오답 11 — `kea-dhcp4 -t` 는 설정 문법 검사

- **문제:** `kea-dhcp4 -t kea-dhcp4.conf` checks the configuration file syntax
- **내 답:** 선택 안 함 (놓침)
- **정답:** 맞음. `-t` = **test**
- **근거:** Lab04a Task 2 — *"Check the syntax using `kea-dhcp4 -t kea-dhcp4.conf`"*
- 서비스를 시작하기 **전에** JSON 문법이 올바른지 확인하는 용도

---

## ★ CentOS DHCP 서버 구축 6단계 (통암기)

```
1. dnf install kea                              설치
2. /etc/kea/kea-dhcp4.conf 편집                 설정
3. kea-dhcp4 -t kea-dhcp4.conf                  문법 검사
4. firewall-cmd --add-service=dhcp --permanent
   firewall-cmd --reload                        방화벽 (2줄 세트)
5. systemctl start kea-dhcp4                    서비스 시작
6. tail /var/lib/kea/kea-leases4.csv            리스 확인
```

경로 함정: 설정은 **/etc/kea/**, 리스 로그는 **/var/lib/kea/**
