# 49202 Communication Protocols — Final Theory Exam 전 범위 개념 정리

> **시험 범위**: Module 1 ~ Module 6 (IP addressing 계산 제외)
> **시험 형식**: MCQ + 계산 문제, 60분, A4 2장 노트 지참 가능
> **목표**: 누가 봐도 한 번에 이해되도록 핵심 개념 + 예시 + 그림 설명

---

## 📚 시작하기 전에 — 큰 그림

### 왜 "프로토콜"이 필요한가?

서울에 있는 친구한테 편지를 보낸다고 생각해봐. 편지 봉투에는:
- **누가 보내는지** (출발지)
- **누가 받는지** (목적지)
- **편지 내용** (페이로드)

이게 다 적혀있어야 우체국이 처리할 수 있지. 인터넷도 똑같음. 컴퓨터들끼리 데이터를 주고받으려면 "어떤 형식으로, 어떤 순서로, 어떻게 처리할지" 약속해야 함. **이 약속이 프로토콜(protocol)**.

### TCP/IP는 5층 건물

인터넷 통신은 **5개 층(layer)으로 나눈 건물**이라고 보면 됨. 각 층은 자기 일만 하고 위/아래 층은 신경 안 씀. 마치 회사에서 부서별로 일을 나눠서 하는 것처럼.

```
┌─────────────────────────────────────────────┐
│ 5. Application Layer (응용)                  │ ← 사람이 쓰는 것 (웹브라우저, Zoom)
│    프로토콜: HTTP, SMTP, DNS                 │   PDU: Messages
├─────────────────────────────────────────────┤
│ 4. Transport Layer (전송)                    │ ← 신뢰성 / 다중화
│    프로토콜: TCP, UDP                        │   PDU: Segment / 주소: Port #
├─────────────────────────────────────────────┤
│ 3. Network Layer (네트워크)                  │ ← 다른 네트워크로 보내기
│    프로토콜: IP                              │   PDU: Datagram / 주소: IP address
├─────────────────────────────────────────────┤
│ 2. Data Link Layer (데이터 링크)             │ ← 같은 네트워크 안에서 보내기
│    프로토콜: Ethernet, WiFi                  │   PDU: Frame / 주소: MAC address
├─────────────────────────────────────────────┤
│ 1. Physical Layer (물리)                     │ ← 진짜 신호 (전기/빛/전파)
│    프로토콜: 10BaseT, 802.11                 │   PDU: Bits
└─────────────────────────────────────────────┘
```

이 구조를 머리에 박아두면 모든 모듈이 다 연결됨.

---

# Module 1 — Introduction & The Internet

## 🎯 한 줄 요약
인터넷은 **여러 네트워크들이 모인 네트워크**(inter-network)이고, **5층 구조(TCP/IP)** 로 동작한다.

---

## 1.1 인터넷이란?

- **여러 LAN(근거리 네트워크) + WAN(광역 네트워크)** 가 서로 연결된 거대한 망
- **분산 구조** — 한 회사가 운영하는 게 아니라, 수많은 **AS(Autonomous System, 자율 시스템)** 가 각자 운영
  - AS 예시: UTS 네트워크, Telstra(통신사), Google 등
- AS끼리 서로 연결돼서 인터넷이 됨

**비유**: 호주 우체국, 한국 우체국, 일본 우체국이 각자 자기 나라 안에서 편지 배달하면서, 국제 우편 협약으로 서로 연결돼 있는 것.

---

## 1.2 왜 계층(Layer)을 나눠?

웹 브라우저는 **웹브라우저 일**만 하면 됨. 그게 이더넷 위에서 돌든, WiFi 위에서 돌든, 4G 위에서 돌든 **신경 안 씀**.

이걸 가능하게 하려고 **기능별로 계층을 나눠서** 각 층이 자기 일만 처리하게 만든 게 TCP/IP 스택.

### 5계층의 역할

| 계층 | 이름 | 무슨 일을 하나 | 비유 |
|---|---|---|---|
| 5 | Application | 사람이 쓰는 프로그램 (HTTP, DNS, SMTP) | 편지 내용 |
| 4 | Transport | 신뢰성, 어느 앱한테 줄지 결정 (TCP, UDP) | 등기/일반 우편 선택 |
| 3 | Network | 다른 네트워크로 보내기 (IP) | 도시간 배송 |
| 2 | Data Link | 같은 네트워크 안에서 보내기 (Ethernet, WiFi) | 동네 안 배송 |
| 1 | Physical | 진짜 신호 (전기, 빛, 전파) | 트럭/오토바이 |

---

## 1.3 캡슐화(Encapsulation) — 핵심 개념

데이터가 **위에서 아래로** 내려가면서 각 층마다 **헤더(header)** 가 하나씩 붙음. 이게 캡슐화.

### 그림으로 이해하기

```
[Application]   Data                                     ← 원본 데이터
[Transport]     [TCP|  Data        ]                     ← TCP 헤더 추가 → "Segment"
[Network]       [IP |TCP|  Data    ]                     ← IP 헤더 추가 → "Datagram"
[Data Link]     [ETH|IP |TCP|Data|TR]                    ← Ethernet 헤더+trailer 추가 → "Frame"
[Physical]      010101110010101010110...                 ← 비트로 변환해서 전송
```

### 예시: 웹 브라우저로 페이지 열기

1. 브라우저가 HTML 요청 만듦 → "Data"
2. TCP가 헤더 붙임 → "TCP Segment" (포트 번호, 시퀀스 번호 등 포함)
3. IP가 헤더 붙임 → "IP Datagram" (출발지/목적지 IP 주소 포함)
4. Ethernet이 헤더+trailer 붙임 → "Ethernet Frame" (출발지/목적지 MAC 주소 포함)
5. 비트 스트림으로 변환되어 케이블이나 전파로 전송

받는 쪽은 **반대로**(decapsulation) 위로 올라가면서 헤더를 하나씩 떼어냄.

### 시험 포인트
- 각 계층의 PDU 이름: **Message → Segment → Datagram → Frame → Bits**
- IP 주소(Layer 3)는 출발지부터 목적지까지 **변하지 않음**
- MAC 주소(Layer 2)는 **각 네트워크 구간마다 바뀜**(라우터 거칠 때마다)

---

## 1.4 프로토콜의 두 가지 큰 분류

### 연결 지향(Connection-oriented) vs 비연결(Connectionless)

| 항목 | Connection-oriented | Connectionless |
|---|---|---|
| 비유 | 전화 걸기 | 엽서 보내기 |
| 연결 설정 | 필요 (악수 필요) | 없음 (그냥 보냄) |
| 신뢰성 | 보장 | 보장 안 함 |
| 오버헤드 | 큼 | 작음 |
| 첫 패킷 지연 | 큼 | 작음 |
| 예시 | TCP | UDP, IP |

### 손실 민감 vs 지연 민감

| 애플리케이션 종류 | 특징 | 예시 |
|---|---|---|
| **Loss-sensitive, delay-tolerant** | 데이터 손실 안 됨, 좀 늦어도 OK | 웹, 이메일, 파일 전송 |
| **Loss-tolerant, delay-sensitive** | 좀 잃어도 됨, 늦으면 안 됨 | 화상통화(Zoom), 게임 |

→ 첫 번째는 **TCP** 쓰고, 두 번째는 **UDP** 씀.

---

# Module 2 — Application Layer

## 🎯 한 줄 요약
사람이 직접 쓰는 계층. **HTTP, DNS, 이메일** 같은 게 여기 속함. TCP/UDP를 도구로 사용해서 동작.

---

## 2.1 응용 계층은 뭐 하는 곳?

직접 우리가 쓰는 것들:
- 웹 브라우징 (HTTP/HTTPS)
- 이메일 (SMTP, IMAP)
- 화상통화 (Zoom, Teams)
- 게임, 파일공유 (BitTorrent), Netflix 등

**보조 서비스**(직접 안 쓰지만 인프라 역할):
- **DNS** (Domain Name System): `uts.edu.au` 같은 이름을 IP 주소로 바꿔줌
- **DHCP**: 네트워크 자동 설정 (IP 주소 자동 할당)
- **VPN**: 안전한 가상 네트워크
- **LDAP, Kerberos**: 인증 서비스

---

## 2.2 응용 분류 1 — 서비스 요구사항으로

| 분류 | 특징 | 예시 |
|---|---|---|
| Delay-tolerant, loss-sensitive | 손실 ❌, 지연 OK | 웹, 파일 전송, 단방향 영상 스트리밍 |
| Loss-tolerant, delay-sensitive | 손실 OK, 지연 ❌ | 실시간 음성/영상 통화, 게임 |

---

## 2.3 응용 분류 2 — 아키텍처로

### 클라이언트-서버 (Client-Server)
- **별 모양(star topology)** 구조
- 가운데 서버 1개, 주변에 클라이언트들
- 예: 웹 브라우저(클라이언트) ↔ 웹 서버

```
       Client A
          |
Client B—[Server]—Client C
          |
       Client D
```

### 피어-투-피어 (Peer-to-Peer, P2P)
- **그물 모양(mesh topology)** 구조
- 모든 호스트가 동등하게 서로 주고받음
- 예: BitTorrent, TOR

```
   Peer A ─── Peer B
     │  ╲   ╱  │
     │   ╲ ╱   │
     │   ╱ ╲   │
     │  ╱   ╲  │
   Peer C ─── Peer D
```

---

## 2.4 연결 지향 vs 비연결 — 응용 관점에서

### Connection-oriented (TCP 위에서 동작)
**전화 거는 것**처럼:
1. **연결 설정** — 양쪽이 "준비됐어?" 확인
2. **데이터 전송** — 요청/응답 주고받음
3. **연결 종료** — "잘 가" 인사

특징:
- 데이터가 **순서대로**, **빠짐없이**, **손상 없이** 도착해야 함
- 손실 민감 앱에 적합
- 단점: 복구하느라 약간의 지연(latency overhead) 발생

### Connectionless (UDP 위에서 동작)
**엽서 보내는 것**처럼:
- 그냥 짧은 메시지를 독립적으로 휙휙 던짐
- 도착 보장 없음, 순서 보장 없음
- 빠르고 가벼움 → 실시간 앱에 적합

---

## 2.5 소켓(Socket) 개념

**소켓 = (IP 주소, 포트 번호)** 한 쌍.

- IP 주소: 어느 컴퓨터인지
- 포트 번호: 그 컴퓨터의 어느 앱인지

예: `192.168.1.10:80` = 192.168.1.10 컴퓨터의 80번 포트(웹서버)

응용 프로그램은 **소켓 API**를 통해서 OS한테 "데이터 보내줘/받아줘"라고 시킴. 소켓은 **응용 계층과 전송 계층의 인터페이스**.

### 시험 포인트
- DNS는 보통 **UDP** 사용 (빠르고 가벼워야 하니까, 패킷 1개로 끝남)
- HTTP는 **TCP** 사용 (안정적인 전달 필요)
- Zoom 음성/영상은 **UDP** (실시간성 우선)

---

# Module 3 — Transport Layer (TCP & UDP)

## 🎯 한 줄 요약
**End-to-end 계층**. 양 끝(엔드포인트, 호스트)에만 존재하고, 중간 라우터엔 없음.
**TCP** = 신뢰성 있는 byte stream / **UDP** = 빠르고 단순한 message

---

## 3.1 Transport Layer는 왜 필요한가?

Network Layer(IP)는 **best effort**(최선만 다함, 보장 X). 즉:
- 패킷 손실될 수 있음
- 순서 바뀔 수 있음
- 중복될 수 있음

이걸 응용에 따라 **보완하거나 그대로 쓰는** 역할이 Transport Layer.

### Transport Layer가 제공하는 것들
- **다중화/역다중화**(multiplexing/demultiplexing) — 여러 앱이 동시에 네트워크 쓸 수 있게
- 메시지 전달 보장 (TCP만)
- 순서대로 전달 보장 (TCP만)
- 중복 제거 (TCP만)
- 흐름 제어, 혼잡 제어 (TCP만)

### 핵심 사실
- TCP/UDP는 **양 끝(endpoint)에만 존재**
- 중간 라우터(R1, R2)는 IP까지만 봄, TCP는 안 봄

```
[Host A: App|TCP|IP|ETH]──Eth──[R1: IP|ETH]──Eth──[R2: IP|ETH]──Eth──[Host B: App|TCP|IP|ETH]
```

---

## 3.2 TCP — Transmission Control Protocol

### 어디 쓰나?
**손실 민감 + 지연 허용** 앱:
- 웹(HTTP/HTTPS), 이메일(SMTP/IMAP), 파일전송(FTP), 인증

### TCP의 5가지 핵심 특징

| 특징 | 의미 |
|---|---|
| **Connection-oriented** | 데이터 보내기 전에 연결 설정 (3-way handshake) |
| **Byte-stream** | 메시지 단위 ❌, 바이트 흐름 단위 ⭕ |
| **Reliability** | 데이터 전달 + 순서 보장 |
| **Flow control** | 받는 쪽이 처리 못하게 안 만듦 |
| **Congestion control** | 네트워크가 과부하되게 안 만듦 |
| **Full duplex** | 양방향 동시 통신 가능 |

### Byte-stream이란?

TCP는 데이터를 "메시지"가 아니라 **연속된 바이트 흐름**으로 봄. 송신자가 파일에 쓰고 수신자가 읽는 것처럼:

```
송신자 App → [Send buffer] → segment, segment, segment → [Receive buffer] → 수신자 App
```

응용 계층에서 보내고 싶은 만큼 보내면, TCP가 알아서 잘게 쪼개서(segment) 보내고 받는 쪽에서 다시 합쳐줌.

---

## 3.3 TCP Segment & MSS

네트워크는 한 번에 보낼 수 있는 크기에 제한이 있음(**MTU**, Maximum Transmission Unit). Ethernet 기본값은 **1500 bytes**.

```
Ethernet payload: 1500 bytes
- IPv4 header:    20 bytes
- TCP header:     20 bytes
─────────────────────────────
TCP payload(MSS): 1460 bytes  ← TCP가 한 번에 보낼 수 있는 데이터
```

**MSS (Maximum Segment Size)** = TCP가 한 segment에 담을 수 있는 데이터 크기

---

## 3.4 TCP Header 구조

```
0           4    10   16                              31
┌─────────────────┬──────────────────┬────────────────┐
│ Source Port     │ Destination Port                   │
├─────────────────┴────────────────────────────────────┤
│ Sequence number                                       │
├─────────────────────────────────────────────────────┤
│ Acknowledgment number                                 │
├────┬──────┬──────┬──────────────────────────────────┤
│ HL │Unused│Flags │ Advertised window                 │
├────┴──────┴──────┴──────────────────────────────────┤
│ Checksum        │ Urgent Pointer                     │
├─────────────────┴────────────────────────────────────┤
│ Options (0 or more 32-bit words)                     │
├─────────────────────────────────────────────────────┤
│ Data                                                  │
└─────────────────────────────────────────────────────┘
```

### Flags 6개 — 외워두기
| Flag | 의미 |
|---|---|
| **SYN** | Synchronize, 연결 시작 |
| **ACK** | Acknowledgment, 받았다는 표시 |
| **FIN** | Finish, 연결 종료 |
| **RST** | Reset, 강제 종료 |
| **PSH** | Push, 즉시 전달해 |
| **URG** | Urgent, 긴급 데이터 |

---

## 3.5 Port Numbers

| 범위 | 이름 | 용도 |
|---|---|---|
| 0–1023 | Well-known ports | 표준 서비스 (HTTP=80, HTTPS=443, DNS=53) |
| 1024–49151 | Registered ports | 등록된 서비스 |
| 49152–65535 | Dynamic/Ephemeral ports | 클라이언트가 임시로 사용 |

### TCP 연결 식별 — 4-tuple

각 TCP 연결은 **(출발지 IP, 출발지 포트, 목적지 IP, 목적지 포트)** 4개로 유일하게 구별됨.

**예시**: 같은 컴퓨터에서 같은 웹사이트에 두 탭으로 접속
- 연결 1: `(IP_A, 37869, IP_B, 80)`
- 연결 2: `(IP_A, 37870, IP_B, 80)`
- 출발지 포트만 다르면 **다른 연결**로 인식

---

## 3.6 3-Way Handshake (연결 설정)

```
Client                            Server
  │                                  │
  │── SYN, Seq=x ─────────────────→ │   ① 클라이언트가 SYN 보냄 (랜덤 시퀀스 x)
  │                                  │
  │ ←──────── SYN+ACK, Seq=y, Ack=x+1 │ ② 서버가 SYN+ACK로 응답 (랜덤 시퀀스 y, x+1 ack)
  │                                  │
  │── ACK, Ack=y+1 ───────────────→ │   ③ 클라이언트가 ACK 보냄 → ESTABLISHED!
  │                                  │
  │ ===== 데이터 교환 가능 =====    │
```

**핵심 규칙**: 응답 acknowledgment 번호 = 받은 sequence 번호 + 1

---

## 3.7 TCP Connection Termination (연결 종료)

3-way handshake와 달리 **4단계 (또는 양쪽이 독립적인 2개 핸드셰이크)**:

```
Host A                            Host B
  │── FIN, Seq=p ──────────────→ │   ① A가 "끝낼게"
  │ ←─ ACK, Ack=p+1 ──────────── │   ② B가 인정
  │                                │
  │ ←─ FIN, Seq=q ──────────────  │   ③ B도 "끝낼게"
  │── ACK, Ack=q+1 ─────────────→ │   ④ A가 인정 → 연결 종료
```

---

## 3.8 TCP State Machine (상태 다이어그램)

TCP 연결은 여러 상태(state)를 거쳐감. 핵심 상태들:

| 상태 | 의미 |
|---|---|
| **CLOSED** | 닫힘 (시작 상태) |
| **LISTEN** | 서버가 연결 기다림 |
| **SYN_SENT** | 클라이언트가 SYN 보냄 |
| **SYN_RECEIVED** | 서버가 SYN 받고 SYN+ACK 보냄 |
| **ESTABLISHED** | 연결됨 (데이터 교환) |
| **FIN_WAIT_1** | FIN 보냄 (능동 종료) |
| **FIN_WAIT_2** | FIN의 ACK 받음 |
| **CLOSE_WAIT** | 상대방이 FIN 보냄 (수동 종료) |
| **LAST_ACK** | 내 FIN의 ACK 기다림 |
| **TIME_WAIT** | 잠시 대기 후 닫힘 |
| **CLOSING** | 동시 종료 |

### 일반적인 종료 경로
- **연결을 먼저 끊는 쪽 (Active close)**: ESTABLISHED → FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT → CLOSED
- **상대가 끊은 쪽 (Passive close)**: ESTABLISHED → CLOSE_WAIT → LAST_ACK → CLOSED

---

## 3.9 Flow Control — 받는 쪽 보호

### 목적
받는 쪽 버퍼가 가득 차면 데이터를 처리할 수 없으니, **송신자에게 "이만큼만 보내줘"** 라고 알려줌.

### 작동 방식
- 받는 쪽이 자기 **현재 비어있는 버퍼 크기**를 TCP 헤더의 `Advertised Window` 필드에 적어서 보냄
- 송신자는 `min(보낼 데이터량, AdvertisedWindow - 미확인 데이터)` 만큼만 보낼 수 있음

### 예시 흐름
```
받는 쪽 버퍼 크기 = 4096 bytes
→ ACK, Win=4096   (4096 byte까지 받을 수 있어)
→ Win=2048        (지금은 2048밖에 못 받아)
→ Win=0           (꽉 찼어, 잠깐 멈춰)
→ Win=2047        (이제 다시 받을 수 있어)
```

---

## 3.10 Congestion Control — 네트워크 보호 (★★★ 시험 핵심)

### 목적
네트워크 중간 라우터들의 버퍼가 넘치지 않게 **송신 속도를 조절**.

### 핵심 변수
- **CongestionWindow (cwnd)**: 송신자가 한 번에 보낼 수 있는 미확인 데이터 최대량
- **CongestionThreshold (ssthresh)**: Slow Start와 AIMD의 경계선 (초기값: 64KB)

### 합쳐진 윈도우
```
MaxWindow = min(CongestionWindow, AdvertisedWindow)
```
→ Flow control + Congestion control **같이** 동작

---

## 3.11 AIMD (Additive Increase, Multiplicative Decrease)

**핵심 원칙**: 서서히 늘리고, 문제 생기면 확 줄임.

| 상태 | 행동 |
|---|---|
| 혼잡 없음 (정상) | cwnd를 **선형적으로** 천천히 증가 (+1 per RTT) |
| 혼잡 발생 (timeout) | cwnd를 **반으로** 확 줄임 (×0.5) |

### AIAD vs AIMD — 왜 AIMD가 좋나?
- **AIAD**(둘 다 선형): 공정성(fairness) 안 맞춰짐
- **AIMD**(곱셈으로 감소): 시간이 지나면 모든 연결이 같은 속도로 수렴 → **공정함**

---

## 3.12 Slow Start

### 문제
연결 시작할 때 cwnd=1로 시작하면, AIMD로 +1씩 늘리면 너무 느림.

### 해결: Slow Start
**ACK 받을 때마다 cwnd를 +1씩 증가** → 결과적으로 RTT마다 cwnd가 **2배**로 증가 (지수적 증가)

### 예시
```
cwnd=1 → 1 segment 보냄 → 1 ACK 받음 → cwnd=2
cwnd=2 → 2 segments 보냄 → 2 ACK 받음 → cwnd=4
cwnd=4 → 4 segments 보냄 → 4 ACK 받음 → cwnd=8
cwnd=8 → 8 segments 보냄 → 8 ACK 받음 → cwnd=16
...
```

### Slow Start와 AIMD 전환
```
if cwnd < CongestionThreshold:
    Slow Start (ACK당 +1, RTT당 ×2)
else:
    AIMD (RTT당 +1)
```

### Slow Start는 언제 쓰나? (2가지)
1. **TCP 연결 시작할 때** — 네트워크 혼잡 상태를 모르니까 조심스럽게
2. **Timeout 발생 후** — 혼잡이 심하다는 뜻이니 다시 처음부터

---

## 3.13 Timeout 발생 시 (TCP Tahoe)

```
1. CongestionThreshold = CongestionWindow × 0.5    (현재의 절반으로)
2. CongestionWindow = 1                              (다시 1부터)
3. Slow Start로 새 threshold까지 빠르게 회복
4. threshold 도달 후 AIMD로 전환
```

---

## 3.14 Fast Retransmit & Fast Recovery (TCP Reno)

### Duplicate ACK가 뭐?
같은 ACK 번호가 여러 번 오는 것. 두 가지 원인:
1. 패킷이 손실됨
2. 패킷이 순서 바뀌어 도착

### Fast Retransmit
**3개의 duplicate ACK** 받으면 timeout 안 기다리고 **즉시 재전송**

### Fast Recovery
재전송 후 **Slow Start로 가지 않고**, cwnd를 **반으로만 줄임**:
```
CongestionWindow = CongestionWindow × 0.5
```
이러면 회복이 더 빠름 → AIMD의 톱니파(sawtooth) 모양 그래프

---

## 3.15 TCP Tahoe vs TCP Reno

| 항목 | TCP Tahoe | TCP Reno |
|---|---|---|
| 도입 | 1988 | Tahoe + Fast Recovery |
| 메커니즘 | AIMD + Slow Start + Fast Retransmit | Tahoe + **Fast Recovery** |
| Timeout 시 | cwnd=1, Slow Start | cwnd=1, Slow Start |
| 3 dup ACK 시 | cwnd=1, Slow Start | **cwnd×0.5**, AIMD 계속 |

---

## 3.16 RTT 추정 — Adaptive Retransmission

### 왜 필요?
Timeout 시간을 잘 정해야 함. 너무 짧으면 멀쩡한 패킷도 재전송, 너무 길면 손실 감지 늦음.

### 공식 (★ 시험 출제 가능 — 외워야 함)

**평균 RTT 추정** (지수가중이동평균):
$$\overline{RTT_n} = (1-a) \times \overline{RTT_{n-1}} + a \times RTT_{measured}$$

**평균 편차(Mean Deviation)**:
$$Mdev_n = (1-b) \times Mdev_{n-1} + b \times |\overline{RTT_n} - RTT_{measured}|$$

**Retransmission Timeout (RTO)**:
$$RTO_n = \overline{RTT_n} + 4 \times Mdev_n$$

- $a$, $b$: 0~1 사이 가중치 (보통 a=0.125, b=0.25)
- 4를 곱하는 이유: 가우시안 분포라면 **평균+4σ 너머에 도착할 확률은 0.003%** → 거의 안전

---

## 3.17 UDP — User Datagram Protocol

### 특징 (TCP의 정반대)
- **Connectionless** — 연결 설정 없음
- **Message-oriented** — 바이트 스트림 ❌
- **Optional checksum** — 무결성 검증만 선택적
- **신뢰성 없음** (delivery 보장 ❌)
- **순서 보장 없음**
- **Flow/Congestion control 없음**

### 단순한 만큼 빠르고 가벼움. 8 byte 헤더만 있음:
```
0              16              31
┌──────────────┬──────────────┐
│ Source Port  │ Dest Port    │
├──────────────┼──────────────┤
│ Length       │ Checksum     │
└──────────────┴──────────────┘
       Data...
```

### UDP 쓰는 앱
- **DNS** (질의 1개 → 응답 1개, 빠름)
- **VoIP** / 화상통화 (Skype, Zoom — 실시간성 우선, 약간의 손실은 허용)
- **온라인 게임** (FPS 같은 실시간 게임)
- 신뢰성이 필요하면 응용 계층에서 직접 처리

---

## 3.18 TCP/UDP 상호작용 — 공정성 문제

TCP는 혼잡 시 양보하지만, UDP는 신경 안 쓰고 계속 보냄. 그래서:
- 같은 링크에 TCP와 UDP가 같이 있으면 **UDP가 대역폭을 다 차지**
- TCP는 계속 줄어들어서 **불공정한** 결과 발생

---

## 3.19 무선 환경에서의 TCP 문제 — Local (Layer 2) Repair

### 문제
무선 링크는 **혼잡 없이도** 패킷이 잘 손실됨 (간섭, 거리 등). 그런데 TCP는 손실=혼잡으로 오해해서 cwnd를 줄임 → 성능 저하.

### 해결책
Layer 2 (데이터 링크 계층) 자체에서 빠르게 재전송:
- 한 hop의 RTT는 매우 짧음 (마이크로초 단위)
- Timeout을 매우 짧게 잡고 즉시 재전송
- → TCP 입장에선 그냥 "약간 RTT가 늘어났을 뿐"으로 보임
- TCP의 cwnd 줄이기 / Slow Start 안 일어남

---

# Module 4 — Network Layer (IP, Routing 개념)

> ⚠️ **시험 범위 주의**: 공지에 따르면 **subnetting / VLSM / CIDR 계산 문제는 출제 안 됨**. 그러나 **router의 동작 원리**, **routing table 사용법**, **IP datagram을 어떻게 forward하는지**는 출제 가능. 그래서 이 모듈은 **개념 위주로** 정리.

## 🎯 한 줄 요약
**서로 다른 네트워크 사이로** 데이터(IP datagram)를 전달. 라우터가 IP 주소 보고 어디로 보낼지 결정.

---

## 4.1 Network Layer가 하는 일

- **한 네트워크의 호스트 → 다른 네트워크의 호스트**로 데이터그램 전달
- TCP/IP의 IPv4(또는 IPv6)는 **datagram-based** — 각 datagram은 독립적으로 처리됨 (편지처럼)
- **Best-effort service**: 신뢰성/순서/무결성 보장 ❌, 그냥 최선만 다함
- 데이터그램별로 **우선순위(ToS)** 정도는 라우터에 부탁할 수 있음

---

## 4.2 Routing 기본 — 라우터가 하는 일

### 핵심 동작
각 패킷이 라우터에 도착하면, 라우터는:
1. 데이터그램의 **목적지 IP 주소** 확인
2. 자기 **routing table** 검색
3. **Longest prefix match**(가장 긴 일치)로 다음 hop 결정
4. 새 Layer 2 frame으로 캡슐화해서 전달

→ **목적지 IP 주소와 routing table** 외에는 보통 아무것도 안 봄.

---

## 4.3 IPv4 Datagram Header (★ 외워야 함)

```
Bit:   0       4    8         16    19              31
       ┌─────┬─────┬─────────┬──────────────────────┐
       │Vers │ IHL │  ToS    │ Total Length         │
       ├─────┴─────┴─────────┼──────┬───────────────┤
       │  Identification     │Flags │Fragment Offset│
       ├─────────┬───────────┼──────┴───────────────┤
       │  TTL    │  Protocol │  Header Checksum     │
       ├─────────┴───────────┴──────────────────────┤
       │           Source Address (32 bit)           │
       ├──────────────────────────────────────────────┤
       │           Destination Address (32 bit)       │
       ├──────────────────────────────────────────────┤
       │           Options + Padding                  │
       └──────────────────────────────────────────────┘
                        20 octets (기본)
```

### 핵심 필드 의미

| 필드 | 크기 | 의미 |
|---|---|---|
| **Version** | 4 bit | IPv4=4, IPv6=6 |
| **IHL** | 4 bit | 헤더 길이 (32-bit word 단위, 기본 5 = 20 byte) |
| **ToS** | 8 bit | 우선순위 정보 (DSCP 6bit + ECN 2bit) |
| **Total Length** | 16 bit | 전체 길이 (header + payload), 최대 65535 byte |
| **Identification** | 16 bit | 단편화된 패킷 식별 (같은 datagram의 fragment끼리 같은 값) |
| **Flags** | 3 bit | DF (Don't Fragment), MF (More Fragments) |
| **Fragment Offset** | 13 bit | 단편의 위치 (8-byte 단위) |
| **TTL** | 8 bit | Time To Live, 라우터 거칠 때마다 -1, 0되면 폐기 |
| **Protocol** | 8 bit | 위 계층 프로토콜 (TCP=6, UDP=17, ICMP=1) |
| **Header Checksum** | 16 bit | 헤더 무결성 |
| **Source/Dest Address** | 32 bit each | IP 주소 |

### TTL (★)
- 무한 루프 방지용
- 라우터 거칠 때마다 **-1** 감소
- **0이 되면 패킷 폐기** + ICMP "Time Exceeded" 메시지를 출발지로 보냄
- traceroute 명령은 이 원리를 이용 (TTL 1, 2, 3...로 보내서 각 hop 알아냄)

---

## 4.4 라우팅 과정 — 실제 예시

### 시나리오
```
                Router (180.45.32.254 외부 / 138.25.47.254 왼쪽 / 130.130.88.254 오른쪽)
                  │
   ┌──────────────┼──────────────┐
   │  Switch 1    │   Switch 2   │
   └──────────────┼──────────────┘
       │                  │
   Host 1            Host 2
   138.25.47.5      130.130.88.2
   
   왼쪽 네트워크: 138.25.47.0/24
   오른쪽 네트워크: 130.130.88.0/24
```

### Host 1 → Host 2로 패킷 보내기

#### Step 1. Host 1이 datagram 만듦
- 출발지 IP: `138.25.47.5`
- 목적지 IP: `130.130.88.2`

#### Step 2. Host 1이 자기 routing table 보기

```
$ route -n
Destination     Gateway          Genmask         Iface
0.0.0.0         138.25.47.254    0.0.0.0         eth0   ← 기본 경로(default)
138.25.47.0     0.0.0.0          255.255.255.0   eth0   ← 자기 네트워크
```

- 첫 번째: **default route**, 모든 목적지 매칭
- 두 번째: 자기 네트워크 (게이트웨이 불필요)

→ `130.130.88.2`는 자기 네트워크가 아님 → **default route 사용** → 게이트웨이 = 138.25.47.254 (라우터)

#### Step 3. Layer 2 frame 만들어서 라우터로 보냄
- 출발지 MAC: Host 1
- 목적지 MAC: 라우터의 왼쪽 인터페이스
- 라우터가 frame 받음 (목적지 MAC이 자기 거니까)

#### Step 4. 라우터가 datagram 받고 자기 routing table 검색

```
$ route -n
Destination     Gateway          Genmask         Iface
0.0.0.0         180.45.32.254    0.0.0.0         eth2  ← 인터넷
138.25.47.0     0.0.0.0          255.255.255.0   eth0  ← 왼쪽
130.130.88.0    0.0.0.0          255.255.255.0   eth1  ← 오른쪽
```

목적지 130.130.88.2는 **세 번째 항목과 매칭** (longest prefix match) → eth1로 내보냄

#### Step 5. 라우터가 **새로운** Layer 2 frame 만듦
- 출발지 MAC: 라우터의 오른쪽 인터페이스
- 목적지 MAC: Host 2
- → 프레임 보냄, Host 2가 받음

### 핵심 관찰 (★ 시험 빈출)
- **IP 주소(출발지/목적지)는 처음부터 끝까지 절대 안 바뀜**
- **MAC 주소는 hop마다 바뀜** (라우터의 인터페이스 → 다음 노드)

---

## 4.5 Longest Prefix Match (가장 긴 prefix 일치)

라우팅 테이블에 여러 항목이 매칭되면 **가장 긴(구체적인) prefix가 우선**.

예시 (간단화):
```
Destination          Iface
0.0.0.0/0            eth2    ← 0 bit 매칭 (가장 짧음, 마지막 fallback)
138.25.0.0/16        eth0    ← 16 bit 매칭
138.25.47.0/24       eth1    ← 24 bit 매칭 (가장 길고 구체적)
```

목적지 138.25.47.5에 대해서: **24-bit 매칭이 우선** → eth1 사용

---

## 4.6 IP 주소의 역할 (개념만)

> 시험 범위에서 제외되는 부분: 클래스 분류, 서브넷 마스크 비트 계산, VLSM 계산, CIDR 슈퍼넷 계산.
> 그래도 이런 게 있다는 것 정도는 알고 가자.

- IP 주소: 32비트 (IPv4) — 4개의 0~255 숫자 (예: `192.168.1.1`)
- **Network 부분 + Host 부분**으로 나뉨 (netmask로 구분)
- `192.168.1.1/24` 같은 표기 = 앞 24비트가 network 부분
- 라우터는 **network 부분만 보고** 라우팅 결정

---

# Module 5 — Network Layer Part 2 & 3

## 🎯 한 줄 요약
Module 4의 IP 라우팅을 보완하는 추가 메커니즘들:
**Fragmentation, ICMP, NAT, DHCP, IPv6, Routing Protocols (RIP/OSPF/BGP)**

---

## 5.1 Fragmentation & Reassembly (★ 계산 출제 가능)

### 왜 필요?
네트워크마다 **MTU(Maximum Transmission Unit)** 가 다름. 큰 패킷이 작은 MTU 네트워크로 가려면 **잘게 쪼개야** 함.

- Ethernet MTU: 1500 bytes (기본)
- 어떤 네트워크는 9000 bytes (Jumbo frame)
- 어떤 네트워크는 더 작을 수도 있음

### 사용되는 IP 헤더 필드
| 필드 | 용도 |
|---|---|
| **Identification** | 같은 원본의 fragment끼리 같은 값 |
| **Fragment Offset** | 이 fragment가 원본의 어디부터인지 (8-byte 단위) |
| **Flags - More(MF)** | 1=뒤에 더 있음, 0=마지막 fragment |
| **Flags - DF** | 1=쪼개지 마, 0=쪼개도 됨 |
| **Total Length** | 이 fragment의 크기 |

### Fragmentation 규칙 (★)
1. 페이로드를 **8-byte의 배수**로 나눔
2. 각 fragment에 헤더 + 데이터가 MTU 이내가 되도록
3. **마지막 fragment**: MF = 0
4. **나머지 fragment**: MF = 1
5. **재조립은 목적지에서만** 함 (라우터에서 안 함)

### 왜 라우터에서 재조립 안 함?
- Fragment들이 다른 경로로 갈 수도 있음
- 라우터에 부담 큼
- 다음 네트워크에서 또 쪼갤 수도 있는데 무의미함

### 예시
```
원본: Total length = 2500 bytes (header + 2480 byte data)
이 네트워크 MTU = 9000 bytes → OK 그대로 전달
다음 네트워크 MTU = 1500 bytes → 쪼개야 함

쪼갠 결과:
┌──────────────────────────────────┐
│ Fragment 1: data 1480 bytes      │  Offset = 0,    MF = 1
│ Fragment 2: data 1000 bytes      │  Offset = 185 (= 1480/8), MF = 0
└──────────────────────────────────┘
```
(첫 fragment는 8-byte 배수로 자르려고 1480, 두 번째는 나머지 1000)

### Fragmentation은 "나쁘다"
- 라우터/호스트 부담 큼
- 한 fragment 손실되면 **전체 datagram 손실** (TCP 입장에선 전부 재전송)
- → 가능하면 **처음부터 안 쪼개도록** 하자!

---

## 5.2 Path MTU Discovery (PMTU)

### 아이디어
Fragmentation 피하려고 **DF=1**로 보내면, 큰 패킷이 작은 MTU 네트워크에 가면 라우터가 폐기.
- 라우터는 폐기하면서 **ICMP "Fragmentation Needed"** 메시지를 출발지로 보냄
- 그 안에 "이 네트워크 MTU는 X야"라고 알려줌
- 송신자가 datagram 크기를 그에 맞춰 줄임

이 과정을 반복해서 **경로 전체에서 가장 작은 MTU**를 찾아냄. 현대 OS의 기본 동작.

### IPv6에서는?
**Fragmentation 자체가 금지** → PMTU 필수.

---

## 5.3 ICMP — Internet Control Message Protocol

### 역할
IP의 **에러 보고 / 진단** 도우미. IP 위에서 직접 동작 (TCP/UDP 안 씀).

### 자주 쓰이는 ICMP 메시지
| 타입 | 의미 | 사용처 |
|---|---|---|
| Echo Request / Reply | "살아있어?" "응" | **ping** |
| Destination Unreachable | 못 가 | 라우팅 실패 |
| Time Exceeded | TTL 0됨 | **traceroute** |
| Fragmentation Needed | 쪼개야 하는데 DF=1 | PMTU |
| Redirect | 더 좋은 경로 있어 | 라우팅 최적화 |

### ICMP 헤더 (8 byte)
```
┌─────────┬─────────┬───────────────┐
│ Type 1B │ Code 1B │ Checksum 2B   │
├─────────┴─────────┴───────────────┤
│   Rest of header (4 byte, 타입별) │
├───────────────────────────────────┤
│ Data (원본 IP 헤더 + payload 8B)  │
└───────────────────────────────────┘
```

---

## 5.4 Private IP & NAT (Network Address Translation)

### Private IP 주소 범위 (★ 외울 것)
| 범위 | 클래스 |
|---|---|
| `10.0.0.0/8` | A |
| `172.16.0.0/12` | B |
| `192.168.0.0/16` | C |

이 주소들은 **인터넷에 광고 안 됨**. 사설망(home/회사 내부)에서만 사용.

### NAT 작동 원리
사설망 호스트가 인터넷에 패킷 보낼 때, 라우터가:

```
[Host 10.0.0.1] → [Router + NAT 150.150.0.1] → [Internet → Server 200.100.10.1]

Source IP 변환:
보낼 때:  Source=10.0.0.1     → 변환 → Source=150.150.0.1
받을 때:  Dest=150.150.0.1    → 변환 → Dest=10.0.0.1
```

### NAT 매핑 추적
- 라우터가 **(내부 IP, 내부 포트) ↔ (외부 IP, 외부 포트)** 매핑 테이블 유지
- 응답이 돌아오면 원래 내부 호스트로 변환

### NAT의 장단점
**장점**:
- 1개의 공인 IPv4 주소로 여러 사설 호스트 공유 → IPv4 주소 부족 문제 완화
- IPv6 도입을 수십 년 늦춤

**단점**:
- 사설망 안에서 서버 운영 어려움 (port forwarding 필요)
- UDP 양방향 통신 어려움
- **CG-NAT(Carrier-Grade NAT)**: ISP가 NAT를 함 → 더 제한적, port forwarding 불가

---

## 5.5 DHCP — Dynamic Host Configuration Protocol

### 역할
새로 네트워크에 접속한 호스트에게 **IP 주소 + 네트워크 설정 자동 할당**.

자동으로 받는 정보:
- IP 주소
- Netmask
- Gateway 주소
- DNS 서버 주소 + search path/suffix

UDP 기반, 서버는 **포트 67**에서 listen.

### DHCP 4단계 (★ DORA — 외울 것)

```
Client                                  DHCP Server
  │                                       │
  │── ① DHCPDISCOVER (broadcast) ──────→ │   "DHCP 서버 어디?"
  │     src MAC: 자기, dst MAC: FF:FF:FF:FF:FF:FF
  │     src IP: 0.0.0.0,  dst IP: 255.255.255.255
  │     src port: 68,     dst port: 67
  │                                       │
  │ ←── ② DHCPOFFER (unicast) ─────────  │   "이 IP 줄게: YIAddr=X"
  │       (subnet mask, gateway, lease 시간 포함)
  │                                       │
  │── ③ DHCPREQUEST (broadcast) ───────→ │   "그 IP 받을게"
  │      (다른 서버한테도 거절 알림)
  │                                       │
  │ ←── ④ DHCPACK (unicast) ─────────── │   "OK 확정"
  │                                       │
  │ ⑤ ARP request: "혹시 이 IP 누가 쓰고 있어?"  → 응답 오면 DHCPDECLINE
```

### 왜 DISCOVER가 broadcast?
호스트가 아직 IP도 모르고 DHCP 서버 IP도 모름 → 모두에게 broadcast로 묻는 수밖에.

---

## 5.6 IPv6 (개념만)

### IPv4의 문제
- 32비트 = 약 43억 개 주소 → 부족
- NAT가 임시 해결책이지만 한계 있음

### IPv6 특징
- **128비트 주소** = 약 $3.4 \times 10^{38}$개 (사실상 무한)
- 내장된 보안 메커니즘
- 향상된 multicast 확장성
- QoS 기능 내장
- **Fragmentation 금지** → PMTU 필수

### IPv6 헤더 (40 byte 고정)
```
Bit:  0     4         12        16        24       31
      ┌────┬─────────┬──────────────────────────────┐
      │Vers│ Traffic │ Flow Label                   │
      │    │  Class  │                               │
      ├────┴─────────┼─────────┬─────────┬──────────┤
      │ Payload Len  │ NextHdr │ HopLimit│           │
      ├──────────────┴─────────┴─────────┴──────────┤
      │           Source Address (128 bit)            │
      ├───────────────────────────────────────────────┤
      │         Destination Address (128 bit)         │
      └───────────────────────────────────────────────┘
                     10 × 32 bit = 40 octets
```

### IPv6 도입 현황
- 1998년 12월 도입
- 호주 약 40%, 인도 약 80% 도입
- IPv4 + NAT가 너무 잘 동작해서 동기 부족 → 지지부진

---

## 5.7 Routing Protocols 개요

### Interior vs Exterior
| 종류 | 사용처 | 예시 |
|---|---|---|
| **Interior Gateway Protocol (IGP)** | AS 내부 (한 조직 안) | RIP, OSPF |
| **Exterior Gateway Protocol (EGP)** | AS 사이 (조직 간) | BGP |

### 두 가지 알고리즘
| 알고리즘 | 기반 | 비유 |
|---|---|---|
| **Distance Vector (DV)** | Bellman-Ford | "소문 듣고 거리 추정" |
| **Link State (LS)** | Dijkstra | "지도 보고 최단 경로 계산" |

---

## 5.8 Distance Vector Routing (DVR) — RIP 기반

### 작동 방식
1. 각 노드가 **자기로부터 모든 다른 노드까지의 최소 거리** 테이블 유지
2. 처음엔 직접 연결된 이웃만 알고, 나머지는 무한대 ($\infty$)
3. **주기적으로 (보통 30초)** 이웃에게만 자기 거리 벡터 전달
4. 이웃 정보 받으면, "이 이웃 거쳐서 가면 더 짧은가?" 비교
5. 더 짧으면 자기 테이블 업데이트

### 거리 비용 메트릭
- 보통 **hop count** (몇 개 라우터 거치는지)
- RIP의 최대 hop: **15** (16=무한대로 간주)

### Bellman-Ford 알고리즘 복잡도
- $O(E)$ ~ $O(VE)$ (V=노드 수, E=엣지 수)

### 단점
- **수렴이 느림** (소문이 퍼지듯) — 변화 전파에 많은 hop이 걸림
- Count-to-infinity 문제 발생 가능

---

## 5.9 RIP — Routing Information Protocol

### 특징
- DV 기반 IGP
- UDP 기반, 포트 520
- 최대 hop count 15
- Periodic timer: 30초마다 업데이트
- Expiration timer: **180초** (= 30 × 6) 동안 업데이트 없으면 라우터 죽었다고 판단
  - 6배 둔 이유: 가끔 메시지 손실 허용

### RIP 메시지 크기
- 단일 네트워크 광고: 24 bytes
- N개 네트워크 광고: $20N + 4$ bytes

---

## 5.10 Link State Routing (LSR) — OSPF 기반

### 작동 방식
1. 각 노드가 자기 **모든 링크 상태**를 **flooding**(범람)으로 전체에 전파
2. 모든 노드가 네트워크 전체 지도(map)를 가짐
3. 각 노드가 **Dijkstra 알고리즘**으로 자기로부터 모든 노드까지의 최단 경로 계산
4. 결과를 routing table의 next hop으로 사용

### 장점
- 수렴이 빠름 (변화 즉시 flood)
- 더 정확한 최단 경로

### Dijkstra 복잡도
- $O(V^2)$ 일반적, sparse network에선 $O((V+E)\log V)$

---

## 5.11 OSPF — Open Shortest Path First

### 특징
- **Link state routing** 기반
- **IP 위에서 직접** 동작 (TCP/UDP 안 씀, ICMP처럼)
- **Hello protocol**: 라우터들이 인접 라우터 발견
  - Hello 패킷을 multicast 주소 `224.0.0.5`로 10초마다 전송
  - 응답 오면 인접성(adjacency) 인식

### Designated Router (DR) / Backup DR (BDR)
- 라우터들이 **broadcast domain**(같은 스위치)에 있으면 DR/BDR 선출
- 모든 라우터가 서로 정보 공유하면 비효율 → DR/BDR한테만 보내면 됨
- Point-to-point 링크에선 DR 불필요

### Link State Advertisement (LSA)
- 링크 상태 변경 시 **즉시 flooding**으로 전파
- 변경 감지한 노드가 이웃에게 LSA 전송 → 이웃이 다른 이웃에게 중계
- 중복 LSA는 폐기
- 보통 수 초 내에 전체 네트워크에 전파

### OSPF Areas (계층 구조)
- 큰 네트워크는 **areas로 분할**
- **Area 0** = backbone (필수)
- **Area Border Router (ABR)**: 여러 area에 걸친 라우터
- **AS Border Router (ASBR)**: 외부 AS와 연결된 라우터

---

## 5.12 Bellman-Ford 알고리즘 (계산 출제 가능 — 공식만)

### 기본 아이디어
"내 이웃이 알려준 거리 + 내가 그 이웃까지 가는 거리"가 더 짧으면 update.

### 의사코드
```
초기화:
  D[s] = 0          (자기 자신까지 비용 = 0)
  D[n] = ∞          (다른 노드는 무한대)

반복 (수렴할 때까지):
  for each edge (u, v) with cost w(u, v):
      if D[u] + w(u, v) < D[v]:
          D[v] = D[u] + w(u, v)
          predecessor[v] = u
```

### 복잡도
- 일반: $O(V \cdot E)$
- 음의 가중치 있어도 동작 (단, 음의 사이클 없어야 함)

---

## 5.13 Dijkstra 알고리즘 (계산 출제 가능 — 공식만)

### 기본 아이디어
**가장 가까운 노드부터 순서대로** 처리해 나감. 모든 가중치는 양수여야 함.

### 의사코드
```
초기화:
  T = {s}              (처리한 노드 집합 — 처음엔 출발점만)
  L(s) = 0             (자기 자신은 0)
  L(n) = w(s, n) for n ≠ s   (직접 이웃이면 비용, 아니면 ∞)

반복:
  T 안에 없는 노드 중 L 값이 최소인 v 찾기
  v를 T에 추가
  
  모든 노드 n에 대해:
      L(n) = min(L(n), L(v) + w(v, n))
  
  모든 노드가 T에 들어갈 때까지 반복
```

### 복잡도
- 일반: $O(V^2)$
- Sparse network: $O((V+E)\log V)$

### 핵심 차이 (Bellman-Ford vs Dijkstra)
| 항목 | Bellman-Ford | Dijkstra |
|---|---|---|
| 사용 알고리즘 패러다임 | DV (지역 정보) | LS (전역 정보) |
| 음의 가중치 | 허용 | 불허 |
| 복잡도 | $O(VE)$ | $O(V^2)$ |
| 사용 프로토콜 | RIP | OSPF |

---

## 5.14 BGP — Border Gateway Protocol

### 특징
- **Inter-domain (AS 간) routing protocol** — 사실상의 표준
- 일종의 **path vector routing** (DV 변형)
- TCP 위에서 동작 (포트 179)

### 두 종류
| 종류 | 용도 |
|---|---|
| **eBGP** (external BGP) | 다른 AS와 통신 |
| **iBGP** (internal BGP) | 같은 AS 내 라우터들끼리 |

### BGP 메시지 4종류
| 메시지 | 의미 |
|---|---|
| **OPEN** | TCP 연결 열고 인증 |
| **UPDATE** | 새 경로 광고 / 옛 경로 철회 |
| **KEEPALIVE** | UPDATE 없을 때 살아있다 알림 + OPEN ACK |
| **NOTIFICATION** | 에러 보고 / 연결 종료 |

### BGP의 역할
- 이웃 AS로부터 subnet reachability 정보 받음 (eBGP)
- AS 내부 라우터들에게 전파 (iBGP)
- 정책 기반(policy-based) 좋은 경로 결정

---

# Module 6 — Data Link Layer

## 🎯 한 줄 요약
**같은 네트워크 안에서** 비트 스트림을 frame으로 묶어서 전달. **Ethernet, WiFi**가 대표.
**MAC 주소** 사용. **공유 매체에서 충돌 처리**가 핵심 문제.

---

## 6.1 Data Link Layer가 하는 일

비트 스트림에 **구조(structure)** 를 추가해서 의미 있는 frame을 만듦.

### Frame이 가져야 할 것들
- **Start sequence**: 데이터 시작 알림 (프리앰블)
- **Source/Destination address**: 누가 누구한테
- **Error detection code**: 손상 감지 (FCS/CRC)
- **Length 또는 end marker**: 어디서 끝나는지
- **Payload**: 실제 데이터
- (선택) Protocol version, packet type 등 메타데이터

---

## 6.2 Framing & Preamble

### 문제
- 비트 스트림에 에러 있을 수 있음 (비트 누락/뒤집힘)
- 송신기 안 보낼 때 노이즈도 비트로 보일 수 있음
- 어디서 진짜 메시지가 시작/끝나는지 어떻게 알지?

### 해결: Preamble + SFD
- **Preamble**: `1010...1010` 패턴 (수신기가 클럭 동기화)
- **SFD (Start Frame Delimiter)**: `10101011` (이 패턴 보면 헤더 시작)

수신기는 1010 패턴을 찾고, SFD 보면 그 뒤를 frame 헤더로 해석.

---

## 6.3 IEEE 802 Working Groups

데이터 링크 + 물리 계층 표준은 IEEE 802 위원회가 관리:

| 표준 | 내용 |
|---|---|
| **802.2** | LLC (Logical Link Control) — Ethernet II에선 안 씀 |
| **802.3** | **Ethernet** |
| **802.11** | **WiFi** |
| **802.15.1** | Bluetooth |
| **802.15.4** | Zigbee |

---

## 6.4 MAC 주소 (Media Access Control)

### 형식
- **6 bytes (48 bits)** = 16진수 6쌍
- 예: `00:0a:f7:c6:44:50`
- 앞 3 byte: **OUI (Organizationally Unique Identifier)** — 제조사 식별 (예: 00:0a:f7 = Broadcom)
- 뒤 3 byte: 제조사가 부여한 고유 번호

### 특수 주소
| 주소 | 의미 |
|---|---|
| `FF:FF:FF:FF:FF:FF` | **Broadcast** (네트워크 모두에게) |
| 첫 비트가 1 | **Multicast** (특정 그룹) |
| 첫 비트가 0 | **Unicast** (개별 호스트) |

### IP 주소와의 차이
| 항목 | MAC 주소 | IP 주소 |
|---|---|---|
| 계층 | Layer 2 | Layer 3 |
| 길이 | 48 bit | 32 bit (IPv4) |
| 부여 시점 | 제조 시 (HW에 박혀 있음) | OS가 부여 (DHCP 등) |
| 변하는가? | 보통 변경 안 됨 (소프트웨어로 변경 가능) | 네트워크 바뀌면 변경 |
| 비유 | 주민등록번호 | 집 주소 |

---

## 6.5 ARP — Address Resolution Protocol (★)

### 문제
호스트가 IP 주소(예: `192.168.1.5`)는 알지만, 그 컴퓨터의 **MAC 주소를 모름**. Layer 2 frame 만들려면 MAC 주소가 필요한데?

### 해결: ARP
1. **ARP Request (broadcast)**:
   - "IP 192.168.1.5의 주인 누구야?"
   - 출발지 MAC: 자기 MAC
   - 목적지 MAC: `FF:FF:FF:FF:FF:FF` (broadcast)

2. **ARP Reply (unicast)**:
   - 해당 IP의 주인만 응답: "나야! 내 MAC은 00:11:22:33:44:55"
   - 출발지 MAC: 자기
   - 목적지 MAC: 요청한 호스트

3. **ARP Cache**:
   - 양쪽 다 IP↔MAC 매핑을 일정 시간 캐싱 (매번 ARP 안 하려고)

### ARP는 Layer 2 위에서 직접 동작
- IP나 TCP 안 거침 (그래서 ARP 자체가 자주 별도로 다뤄짐)

### 실제 명령
- `arp -n` : ARP cache 보기

---

## 6.6 Frame Check Sequence (FCS) / CRC

### 역할
Frame 끝에 붙는 **체크섬**. 전송 중 비트 손상 감지.

### 작동 방식
1. 송신자: 전체 frame에 대해 CRC 계산해서 FCS 필드에 채움
2. 수신자: 받은 frame의 CRC 다시 계산
3. **계산값과 받은 값이 다르면 → frame 손상 → 폐기**

### 핵심 사실 (★ 시험 빈출)
- CRC가 다르면 NIC(Network Interface Card)는 **frame을 폐기** (discard)
- Layer 2는 보통 **재전송 안 함** (그건 위 계층의 일)
- 손실은 위 계층에서 처리 (TCP가 재전송)

---

## 6.7 Medium Access Control (MAC) — 매체 접근 제어

### 왜 문제?
**공유 매체(shared medium)** 에선 여러 호스트가 동시에 보내면 **충돌(collision)** 발생.

### 매체 종류
| 종류 | 충돌 발생? | 예시 |
|---|---|---|
| 비공유 (전용 채널) | ❌ | 현대 switched Ethernet (각 호스트가 스위치와 1:1) |
| 공유 (shared) | ⭕ | 옛날 coaxial Ethernet, **WiFi** |

→ 공유 매체에선 **충돌 처리 메커니즘 필요**

---

## 6.8 CSMA/CD — Ethernet의 충돌 처리 (★)

**Carrier Sense Multiple Access / Collision Detection**

### 작동 단계
1. **Carrier Sense (반송파 감지)**: 매체가 idle인지 listen
2. 점유 중이면 → 끝날 때까지 대기 + **inter-packet gap** 만큼 추가 대기 → 다시 시도
3. Idle이면 → 즉시 전송
4. 전송 중에도 매체 listen
5. **충돌 감지**되면:
   - **Jam signal** 보냄 (모두에게 충돌 알림)
   - 0과 N 사이 **랜덤 시간 대기** 후 재시도

### Binary Exponential Backoff
재전송 횟수 N에 따라 대기 시간 범위 결정:
- $1 \le N \le 10$: $0 \le k \le 2^N$ 에서 $k$ 랜덤 선택
- $11 \le N \le 15$: $0 \le k \le 2^{10} = 1024$ 로 고정
- $N = 15$ 이후도 충돌 → 네트워크에 심각한 문제

→ 충돌이 반복될수록 대기 시간 범위가 **지수적으로** 늘어남 → 자연스럽게 재충돌 확률 감소

### 최소 프레임 길이
- Ethernet 최소 프레임: 64 bytes
- 이보다 짧은 프레임은 **padding**으로 채움
- 이유: 충돌 감지가 끝나기 전에 전송 끝나면 충돌 못 감지

---

## 6.9 CSMA/CA — WiFi의 충돌 처리 (★)

**Carrier Sense Multiple Access / Collision Avoidance**

### 왜 CD 안 쓰고 CA?
무선에선 **충돌 감지가 어렵거나 불가능**:
- 송신 중에는 자기 신호가 너무 강해서 다른 신호 안 들림
- → 일단 충돌이 일어나도록 두지 말고 **회피(avoidance)** 하자

### 작동 방식 (DCF: Distributed Coordination Function)
1. 매체 listen
2. Idle이면 **임의의 시간(random backoff)** 대기 후 전송
3. 받은 쪽이 **ACK** 보냄 → 송신자가 ACK 받으면 성공
4. ACK 못 받으면 충돌이라 가정 → 재시도

---

## 6.10 Hidden Node 문제 & RTS/CTS (★)

### Hidden Node 문제
```
A ─────── AP ─────── C
  (서로 못 봄)
```
- A와 C가 서로 신호를 못 들음 (멀거나 장애물)
- 둘 다 AP는 들을 수 있음
- A와 C가 동시에 보내면 → AP에서 충돌 → 둘 다 통신 실패
- 그런데 A, C는 carrier sense에서 매체가 idle하다고 봄!

### 해결: RTS/CTS
1. **RTS (Request To Send)**: A가 AP에 "보낼게" 요청
2. **CTS (Clear To Send)**: AP가 "OK" 응답 — 이 CTS는 **C도 들음**
3. C는 CTS 보면 "AP가 누군가랑 통신 중이구나" 알고 잠시 대기
4. A가 데이터 전송, AP가 ACK

### Exposed Node 문제
```
A ─── B ─── C ─── D
```
- B가 A에게 보내는 중
- C는 B의 전송을 들음 → 매체 busy로 판단
- C가 D에게 보낼 수 있는데도 보내지 못함 (실제론 충돌 안 일어남)
- → 대역폭 낭비

---

## 6.11 WiFi 모드 (BSS / Ad-hoc)

### Infrastructure Mode (BSS — Basic Service Set)
- 중앙에 **Access Point (AP)** 가 있음
- 모든 통신이 AP를 거침
- 일반 가정/회사 WiFi가 이 모드

### Ad-hoc Mode (IBSS — Independent BSS)
- AP 없음, 호스트들끼리 직접 통신
- 임시 네트워크 (예: 노트북끼리 직접 파일 공유)

### Distribution System
- 여러 BSS를 연결해서 **ESS (Extended Service Set)** 만듦
- 호스트가 한 AP에서 다른 AP로 이동하며 연결 유지(roaming) 가능

---

## 6.12 Switched Ethernet — 스위치 동작

### 옛날 Ethernet (Hub)
- 모든 포트가 한 매체 공유 → CSMA/CD 필요
- 충돌 잦음, 비효율

### 현대 Switched Ethernet
- 각 포트가 **독립된 채널** → 충돌 없음
- 스위치가 **MAC 주소 → 포트 매핑 테이블** 유지
- Frame 받으면 목적지 MAC 보고 적절한 포트로만 전달

### 스위치 동작 방식
| 방식 | 동작 |
|---|---|
| **Cut-through** | 헤더만 보면 바로 전달 시작 (빠름, 에러 frame도 전달 가능) |
| **Store-and-forward** | 전체 frame 받고 CRC 검사 후 전달 (느리지만 안전) |

---

## 6.13 Ethernet Frame 형식

### Ethernet II Frame (★)
```
┌─────────┬─────┬───────────┬───────────┬────────┬─────────┬─────┐
│Preamble │ SFD │ Dest MAC  │ Src MAC   │ Type   │ Payload │ FCS │
│  7 B    │ 1 B │   6 B     │   6 B     │  2 B   │ 46-1500 │ 4 B │
└─────────┴─────┴───────────┴───────────┴────────┴─────────┴─────┘
```

- **Type** 필드: 위 계층 프로토콜 (IPv4=0x0800, IPv6=0x86DD, ARP=0x0806)
- **최소 payload 46 byte**: 부족하면 padding
- **최대 payload 1500 byte**: = MTU

### IEEE 802.3 Frame (Ethernet II와 약간 다름)
- **Length** 필드 (Type 대신) — 페이로드 길이
- 위에 LLC 헤더 추가 (802.2)
- 현재는 Ethernet II가 압도적으로 많이 쓰임

### 시험 포인트
- IEEE 802.3은 **Data link + Physical layer** 둘 다 규정
- 802.11도 마찬가지

---

# 📐 시험에 나올 수 있는 핵심 공식 모음

> 시험 공지: MCQ + **calculations** 혼합. 계산 문제 영역의 공식 정리.

---

## TCP 관련 공식

### MSS 계산
$$\text{MSS} = \text{MTU} - \text{IP header} - \text{TCP header}$$

기본 Ethernet 환경:
$$\text{MSS} = 1500 - 20 - 20 = 1460 \text{ bytes}$$

### Combined Window
$$\text{MaxWindow} = \min(\text{CongestionWindow}, \text{AdvertisedWindow})$$

송신자가 보낼 수 있는 양:
$$\text{보낼 양} = \min(\text{데이터}, \text{MaxWindow} - \text{미확인 데이터})$$

### Slow Start vs AIMD 전환
```
if cwnd < ssthresh:          → Slow Start (ACK당 +1, RTT당 ×2)
else:                        → AIMD (RTT당 +1)
```

### Timeout 발생 시 (TCP Tahoe & Reno)
$$\text{ssthresh}_{\text{new}} = \frac{\text{cwnd}}{2}, \quad \text{cwnd}_{\text{new}} = 1$$

### 3 Duplicate ACK 시
- **Tahoe**: 위와 동일 (cwnd=1)
- **Reno**: $\text{cwnd}_{\text{new}} = \frac{\text{cwnd}}{2}$ (Slow Start 안 하고 AIMD 계속)

### RTT 추정
$$\overline{RTT_n} = (1-a) \cdot \overline{RTT_{n-1}} + a \cdot RTT_{measured}$$

### Mean Deviation
$$Mdev_n = (1-b) \cdot Mdev_{n-1} + b \cdot |\overline{RTT_n} - RTT_{measured}|$$

### Retransmission Timeout (RTO)
$$RTO_n = \overline{RTT_n} + 4 \times Mdev_n$$

---

## Fragmentation 공식

### Fragment 개수
$$N_{fragments} = \left\lceil \frac{\text{Original payload}}{\text{Per-fragment payload size}} \right\rceil$$

### Per-fragment payload size 계산
- MTU에서 IP header(20 byte) 빼기
- **8의 배수로 내림** (마지막 fragment 제외)

$$\text{Fragment payload} = \left\lfloor \frac{\text{MTU} - 20}{8} \right\rfloor \times 8$$

### Fragment Offset
- 단위: **8 byte**
- $i$번째 fragment의 offset:
$$\text{Offset}_i = \frac{\text{앞선 fragment들의 페이로드 합}}{8}$$

### MF (More Fragments) flag
- 마지막 fragment: MF = 0
- 나머지: MF = 1

---

## UDP / Efficiency 계산

### Transmission Efficiency
$$\eta = \frac{\text{유용한 데이터 byte}}{\text{전체 전송 byte (헤더 모두 포함)}}$$

### 계층별 오버헤드
| 계층 | 오버헤드 |
|---|---|
| TCP | 20 byte (기본) |
| UDP | 8 byte |
| IPv4 | 20 byte (기본) |
| IPv6 | 40 byte (고정) |
| Ethernet II | 14 byte (header) + 4 byte (FCS) = 18 byte |
| Ethernet 최소 frame | 64 byte (padding 포함) |

### 예시 — UDP/IP/Ethernet 위에서 16 byte 데이터의 효율
- UDP level: $16 / (16 + 8) = 66.6\%$
- IP level: $16 / (16 + 8 + 20) = 36.4\%$
- Data Link level: $16 / 64 = 25\%$ (최소 프레임 크기 사용)

---

## Throughput / Latency 공식 (가능성)

### Transmission delay (= insertion time)
$$t_{ins} = \frac{\text{Frame size (bits)}}{\text{Link rate (bps)}}$$

### Propagation delay
$$t_{prop} = \frac{\text{Distance}}{\text{Signal speed}}$$

### Round Trip Time (1 hop)
$$RTT = 2 \times t_{prop} \text{ (왕복)}$$

### TCP Slow Start phase 시간 (간단화)
$$T_{phaseB} = N_{RTT} \times (t_{ins} + 2 \times t_{prop})$$
where $N_{RTT}$ = steady state까지 걸리는 RTT 수

---

## Routing 알고리즘 의사코드

### Bellman-Ford (간단판)
```
for all v: D[v] = ∞
D[source] = 0

for k = 1 to V-1:
    for each edge (u, v) with cost w:
        if D[u] + w < D[v]:
            D[v] = D[u] + w
            prev[v] = u
```

### Dijkstra (간단판)
```
T = {source}, L[source] = 0
L[n] = w(source, n) for all n ≠ source

while T ≠ all nodes:
    find v not in T with minimum L[v]
    T = T ∪ {v}
    for each n not in T:
        L[n] = min(L[n], L[v] + w(v, n))
```

---

## CSMA/CD Backoff
재전송 N번째 시도 시:
- $1 \le N \le 10$: 대기 슬롯 수 $k$를 $0 \le k \le 2^N$ 에서 랜덤 선택
- $11 \le N \le 15$: $0 \le k \le 1024$ 로 고정
- $N > 15$: 포기 (네트워크 문제)

---

# 🎯 시험 직전 핵심 체크리스트

## 반드시 알아야 할 헤더 필드

### TCP Header (20 byte 기본)
- Source/Destination Port (16 bit each)
- Sequence number, Ack number (32 bit each)
- HL, Flags (URG/ACK/PSH/RST/SYN/FIN)
- Advertised Window
- Checksum, Urgent Pointer

### IPv4 Header (20 byte 기본)
- Version, IHL, ToS, Total Length
- Identification, Flags (DF/MF), Fragment Offset
- TTL, Protocol, Header Checksum
- Source/Destination Address (32 bit each)

### IPv6 Header (40 byte 고정)
- Version, Traffic Class, Flow Label
- Payload Length, Next Header, Hop Limit
- Source/Destination Address (128 bit each)

### UDP Header (8 byte)
- Source/Destination Port, Length, Checksum

### Ethernet II Frame
- Preamble (7B) + SFD (1B) + Dst MAC (6B) + Src MAC (6B) + Type (2B) + Payload (46-1500B) + FCS (4B)

---

## 절대 헷갈리지 말아야 할 것들

### IP vs MAC
| 질문 | 답 |
|---|---|
| 라우터 거치면 변하는 건? | **MAC** (IP는 그대로) |
| 32비트 주소? | **IPv4** |
| 48비트 주소? | **MAC** |
| 128비트 주소? | **IPv6** |

### TCP vs UDP
| 질문 | TCP | UDP |
|---|---|---|
| Connection 설정? | ⭕ (3-way handshake) | ❌ |
| 신뢰성 보장? | ⭕ | ❌ |
| 순서 보장? | ⭕ | ❌ |
| Flow/Congestion control? | ⭕ | ❌ |
| Header 크기? | 20 byte | 8 byte |
| 사용 예? | 웹, 이메일, 파일전송 | DNS, VoIP, 게임 |

### 라우팅 프로토콜 비교
| 항목 | RIP | OSPF | BGP |
|---|---|---|---|
| 알고리즘 | Distance Vector | Link State | Path Vector |
| 기반 | Bellman-Ford | Dijkstra | DV 변형 |
| 사용처 | IGP (소규모) | IGP (대규모) | EGP (AS 간) |
| 메트릭 | hop count | 링크 비용 | 정책 |
| 전송 | UDP 520 | IP 직접 | TCP 179 |
| 최대 hop | 15 | 무제한 | 무제한 |

### CSMA/CD vs CSMA/CA
| 항목 | CSMA/CD | CSMA/CA |
|---|---|---|
| 사용처 | 옛 Ethernet | WiFi |
| 충돌 처리 | **Detection** (감지 후 jam) | **Avoidance** (회피) |
| ACK 사용? | ❌ | ⭕ |
| 무선/유선 | 유선 | 무선 |
| 추가 메커니즘 | Binary exponential backoff | RTS/CTS (옵션) |

### Slow Start vs AIMD
| 항목 | Slow Start | AIMD |
|---|---|---|
| 증가율 | 지수 (RTT당 ×2) | 선형 (RTT당 +1) |
| ACK당 cwnd 증가 | +1 | +1/cwnd |
| 사용 시점 | 시작/timeout 후 | threshold 도달 후 |

---

## 🔑 자주 출제되는 개념 질문 패턴

1. **"Layer X의 책임은?"** — Framing은 Layer 2, IP addressing은 Layer 3, 신뢰성은 Layer 4
2. **"이 PDU의 이름은?"** — Message/Segment/Datagram/Frame
3. **"이 주소는 어느 계층?"** — Port=L4, IP=L3, MAC=L2
4. **"라우터가 받은 datagram 어떻게 처리?"** — destination IP 확인 → routing table → longest match → next hop
5. **"3-way handshake 순서?"** — SYN → SYN+ACK → ACK
6. **"Fragment offset 계산?"** — 앞선 페이로드 합 ÷ 8
7. **"Slow start 시작은?"** — cwnd=1, ACK당 +1
8. **"CRC 다르면?"** — Frame 폐기 (재전송 안 함)
9. **"DNS는 TCP/UDP 뭐 씀?"** — 보통 UDP (간단/빠름)
10. **"OSPF 알고리즘?"** — Dijkstra (Link State)

---

## 📝 노트 정리 우선순위 (A4 2장에 압축)

### 1순위 (필수)
- TCP cwnd 변화 다이어그램 (slow start, timeout, 3 dup ACK)
- TCP state machine 다이어그램
- IPv4/TCP/UDP/Ethernet header 필드
- Fragmentation 공식 (offset, MF, length)
- Routing protocol 비교표 (RIP/OSPF/BGP)
- RTT/RTO 공식
- DHCP 4단계 (DORA)

### 2순위 (중요)
- 5-layer 모델표 (PDU, 주소)
- ARP 동작
- CSMA/CD vs CSMA/CA
- NAT 동작 원리
- Bellman-Ford / Dijkstra 의사코드
- Hidden node / RTS-CTS

### 3순위 (있으면 좋음)
- Private IP 범위
- Well-known ports (HTTP=80, DNS=53, etc.)
- IPv6 주소 크기, 헤더 구조
- OSPF area / DR/BDR 개념

---

## 🚫 시험에 나오지 않는 것 (공식적으로 제외됨)

- Subnetting 계산
- VLSM 계산
- CIDR 슈퍼넷 계산
- Route summarization 계산
- 클래스(A/B/C) 분류 후 비트 계산

이런 거 안 외워도 됨. 하지만 라우터가 **prefix 매칭**으로 forwarding 결정한다는 **개념**은 알아야 함.

---

**Good luck on your final! 🍀**
