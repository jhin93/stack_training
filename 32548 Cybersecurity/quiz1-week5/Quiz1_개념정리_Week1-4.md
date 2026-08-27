# Quiz 1 개념 총정리 (Week 1 ~ Week 4)

> **시험 정보**: Quiz-1, Week-5 Lab, Spring 2026 / 범위 = Week 1~4 강의·워크숍
> **문제 유형**: 객관식(1답) · 복수답(체크박스, 여러 개 정답) · True/False, 각 1점
> **팁**: 대부분 "용어 정의"를 물어봄. 아래 **굵은 영어 단어**를 보고 뜻이 바로 떠오르면 대부분 맞힘.

---

# PART 1. 보안의 기본 개념 (Week 1)

## 1-1. Cybersecurity(사이버보안)의 정의
- **정확한 정의**: 컴퓨터 **시스템(Hardware + Software)** 과 그 안의 **정보**를 보호하는 것.
- 즉 "네트워크만" 지키는 게 아니라 **하드웨어·소프트웨어·데이터 전체**를 지키는 것.
- 시험 포인트: "정확한 정의?" → **Securing Hardware and Software of Computer system** (네트워크만/물리보안만 고르면 틀림)

## 1-2. 보안 목표 (Security Goals) — 제일 많이 나옴 ⭐
암기법: **CIA + 3개 더**. 각 단어의 "한 줄 정의"를 외워.

| 영어 용어 | 한글 | 한 줄 정의 (이게 시험 답) |
|---|---|---|
| **Confidentiality** | 기밀성 | 인가된(허락된) 사람만 정보를 볼 수 있음 (비밀 유지) |
| ├ **Data confidentiality** | 데이터 기밀성 | 데이터가 비인가자에게 노출 안 됨 |
| └ **Privacy** | 프라이버시 | 개인이 자기 정보가 누구에게·어떻게 쓰이는지 통제 |
| **Integrity** | 무결성 | 인가 없이 **변경/조작되지 않음** |
| ├ **Data integrity** | 데이터 무결성 | 데이터가 함부로 바뀌지 않음 |
| └ **System integrity** | 시스템 무결성 | **시스템이 (허가 안 된 조작 없이) 원래 의도한 기능을 그대로 수행** |
| **Availability** | 가용성 | 필요할 때 시스템·데이터에 **접근 가능** |
| **Authenticity** | 진정성 | 진짜인지 검증 가능 (진짜 사용자/출처가 맞는지) |
| **Accountability** | 책임추적성 | **어떤 행위를 특정 주체(entity)로 유일하게 추적** 가능 |

**시험에서 이렇게 나옴 (연습문제 Q1·Q2 유형):**
- "행위를 **entity에게 유일하게 추적**하도록 요구하는 보안 목표?" → **Accountability**
- "시스템이 **비인가 조작 없이 의도한 기능을 손상 없이 수행**하도록 보장?" → **System Integrity**

> 헷갈림 주의: Integrity = "**바뀌지 않음**", Availability = "**쓸 수 있음**", Confidentiality = "**안 보임**", Accountability = "**누가 했는지 추적**".

## 1-3. 공격의 종류 — Passive vs Active ⭐
| 구분 | 뜻 | 특징 | 예시 |
|---|---|---|---|
| **Passive attack**(수동적) | **엿듣기만**, 시스템 변경 X | **탐지 어려움**, 예방(암호화)이 중요 | **Release of message content**(메시지 내용 훔쳐보기), **Traffic analysis**(트래픽 패턴 분석) |
| **Active attack**(능동적) | **시스템 자원을 변경/조작하거나 동작에 영향** | 탐지는 가능, 완전 예방은 어려움 | **Masquerade**(위장), **Replay**(재전송), **Modification**(변조), **Denial of Service(DoS)** |

**시험 유형 (Q3):** "시스템 자원을 **변경**하거나 동작에 **직접 영향**을 주는 공격?" → **Active**
(Passive / Release of message content / Traffic analysis 는 전부 "수동적"이라 오답)

## 1-4. 악성코드 & 위협
- **Malware(악성코드)**: **정상 기능에 해를 끼칠 수 있는 원치 않는(unwanted) 프로그램 코드.**
  - 시험 답: "malware is an unwanted programming code which **may cause harm** to the normal functions of a computer" (may **not** harm = 오답)
- **Ransomware(랜섬웨어)**: 파일을 **암호화(잠금)** 하고 **몸값(ransom)** 을 요구하는 악성코드.
- **WannaCry**: 대표적 랜섬웨어. **crypto worm(암호화 웜)** 이고 **Bitcoin(비트코인)으로 몸값** 요구 + 컴퓨터를 잠그고 지불 요구. (복수답: "crypto worm demanding ransom in Bitcoin" + "malware locks computer demanding payment" 둘 다 맞음)
- **Worm(웜)**: 스스로 복제·전파되는 악성코드 (사용자 실행 없이도 퍼짐).
- **Virus(바이러스)**: 다른 파일에 붙어서 퍼지는 악성코드.

## 1-5. 공격자 (Cyber Attacker)
- **동기(motives)**: **금전적 이득(Monetary gain)**, 경쟁사 **브랜드 가치 훼손**, **사이버 테러(cyberterrorism)**, 정부·기업 **기밀 탈취**, **사이버 전쟁(cyber warfare)** 등.
- 시험에서 "공격자의 동기?" → 대부분 **All of the above**(위 전부).

## 1-6. 취약점 & 사고 대응
- **Vulnerability(취약점)**: 공격에 이용될 수 있는 **약점/허점**.
- **CVE (Common Vulnerabilities and Exposures)**: 알려진 취약점에 붙이는 **고유 번호/목록**.
- **CVSS (Common Vulnerability Scoring System)**: 취약점의 **위험도를 점수로 매기는 시스템** (0~10점). ⭐
  - 시험 답: **Common Vulnerability Scoring System** (Secured/Compromised 는 함정 오답)
- **Incident Response(사고 대응)**: 보안 사고를 조사·대응하는 **과정에서 수집된 통찰/정보**를 다루는 활동.
  - 시험 답: "Insights collected from **investigations and response activities** in incident management and forensics"
- **Threat Intelligence(위협 인텔리전스)**: 위협에 대한 기술 정보 DB.
- **Dark Web marketplace**: 훔친 데이터·크리덴셜·익스플로잇을 사고파는 곳.

## 1-7. 데이터 프라이버시 (Data Privacy)
- **정의**: 어떤 데이터가 **중요하고 누구와 공유되어야 하는지**를 다루는 것. (누구에게 공유되는가가 핵심)
- **GDPR (General Data Protection Regulation)**: **EU(유럽연합)가 만든 개인정보보호 법/프레임워크**. ⭐
  - 시험 답: EU가 제안한 프라이버시 프레임워크 → **GDPR** (TDPR/DPGR = 철자 바꾼 함정 오답)

---

# PART 2. 웹 보안 (Week 2)

## 2-1. HTTP 기본
- **HTTP**: 웹 브라우저↔서버 통신 규약. **평문(암호화 안 됨)** → 그래서 HTTPS(=HTTP+TLS) 필요.
- **HTTP 메시지 구조**: **헤더(header)** + **본문(body)**.
  - 헤더의 각 줄은 **CRLF(줄바꿈, \r\n)** 로 끝남.
  - **헤더와 본문은 "빈 줄(blank line)" 로 구분** = CRLF가 **두 번**(CRLF CRLF).
  - 시험 함정(Q24): "header와 body는 **one CR LF** 로 구분된다" → **False** (한 개가 아니라 빈 줄 = 두 개의 CRLF)

### HTTP 응답 상태 코드 (Response Codes) ⭐
| 코드 | 뜻 |
|---|---|
| **200** | **성공 (OK)** ← "웹 요청 성공 시 반환 코드?" 답 |
| 301 | 영구 이동 (Redirect) |
| 403 | 접근 금지 (Forbidden) |
| 404 | 없음 (Not Found) |
| 500 | 서버 내부 오류 |

**시험 유형(Q22):** "웹 요청이 **성공**하면 서버가 반환하는 코드?" → **200**

## 2-2. 웹 공격 종류 ⭐⭐
### SQL Injection (SQLi)
- 입력창에 **SQL 구문을 삽입**해서 인증 우회·데이터 탈취.
- 원인: **특수문자를 걸러내지 않음(failure to sanitise special characters)**.

### XSS (Cross-Site Scripting)
- 웹페이지에 **악성 스크립트를 삽입**해서 다른 사용자 브라우저에서 실행.
- **Reflected XSS(반사형)**: 악성 스크립트가 **요청에 실려 즉시 반사**됨 (서버에 저장 X). 링크 클릭 유도.
- **Persistent/Stored XSS(저장형)**: 악성 데이터가 **서버에 저장**됨 → 방문자마다 실행. ⭐
  - 시험 유형(Q26): "공격자가 데이터를 **타깃 서버에 직접 저장**하는 경우?" → **Persistent XSS attack**

### CSRF (Cross-Site Request Forgery) ⭐
- 뜻: **Cross-Site Request Forgery** (사이트 간 요청 위조). 로그인된 사용자를 속여 **원치 않는 요청을 대신 보내게** 함.
- 시험 함정(Q25): "CSRF = Central Security Resource Framework" → **False** (진짜는 Cross-Site Request Forgery)

### HTTP Response Splitting (HTTP 응답 분할)
- 응답에 **CRLF를 주입**해 응답을 쪼개 조작.
- 결과: **Web cache poisoning(웹 캐시 오염)**, **Browser hijacking(브라우저 하이재킹/XSS)** 등. (Q23 복수답)

## 2-3. 네트워크 공격 & 도구 (Lab)
- **Port scanning(포트 스캔)**: 열린 포트/서비스 탐색 (예: **nmap**, Zenmap). 정보수집(reconnaissance) 단계.
- **John the Ripper(JtR)**: **패스워드 크래킹** 도구 (약한 비번을 사전/무차별로 알아냄).
- **SYN flooding(SYN 플러딩)**: TCP 연결요청(SYN)을 폭주시켜 **서버 자원 고갈** → **DoS**. ⭐
  - 시험 유형(Q30): SYN flooding 결과 → **Exhausting server capacity(서버 용량 고갈)** + **Launching DoS attack** (복수답)
- **DoS / DDoS**: 서비스 거부 공격. DoS=1대, **DDoS**=여러 대(봇넷)로 분산 공격 → **가용성(Availability)** 을 침해.

---

# PART 3. 인증·키·PKI (Week 3)

## 3-1. Nonce (넌스) ⭐
- 뜻: **"Number used ONCE"** — **한 번만 쓰는 랜덤 값**.
- 목적: 응답이 **신선(fresh)** 한지 보장 → **재전송 공격(Replay attack) 방지**.
  - 시험 유형(Q11): "응답이 fresh하고 재전송되지 않았음을 보장하는 랜덤 값?" → **nonce**

## 3-2. PKI (Public Key Infrastructure, 공개키 기반구조)
공개키·인증서를 발급·관리하는 전체 체계.

- **X.509** ⭐: **공개키 인증서(public-key certificate)의 표준 포맷.** 네트워크 보안에서 거의 표준으로 쓰임.
  - 시험 유형(Q12): "공개키 인증서 포맷의 보편 표준?" → **X.509** (X.905는 함정 오답)
- **CA (Certificate Authority, 인증기관)**: 인증서를 **서명·발급**하는 신뢰기관.
- **RA (Registration Authority, 등록기관)**: 인증서 신청자의 **신원을 확인**해주는 보조 기관 (CA를 돕는 역할).
- **Identity Management(신원 관리)** ⭐: **조직 전체에 걸쳐 중앙집중·자동화된 방식**으로, 각 사용자의 **정체성(identity)을 정의**하고 속성을 연결하며 신원 검증 수단을 강제하는 접근법.
  - 시험 유형(Q13): 위 정의 → **Identity management** (Registration authority 아님!)

### PKCS 표준 (Public-Key Cryptography Standards)
번호별로 용도가 다름. 시험에 번호 매칭이 나옴 ⭐
| 표준 | 용도 |
|---|---|
| PKCS#1 | RSA 암호화 표준 |
| PKCS#3 | Diffie-Hellman 키 교환 |
| PKCS#5 | 패스워드 기반 암호화 |
| PKCS#7 | 메시지 서명/암호화 (CMS) |
| **PKCS#13** | **타원곡선 암호 (Elliptic Curve Cryptography)** ← 시험 답 |
| PKCS#15 | 토큰 정보 포맷 |

- 시험 유형(Q27): "**타원곡선(elliptic curves)** 을 정의하는 PKI 표준?" → **PKCS#13**

## 3-3. Kerberos & KDC ⭐
- **Kerberos(케르베로스)**: 네트워크 **인증 프로토콜** (티켓 기반).
- **KDC (Key Distribution Center, 키 분배 센터)**: 세션 키를 나눠주는 중앙 서버.
- **Kerberos는 KDC이다** → 시험(Q28) 답: **True**.

---

# PART 4. 암호학 & SSL/TLS (Week 4)

## 4-1. 대칭키 vs 비대칭키 ⭐
| 구분 | 키 | 특징 | 알고리즘 |
|---|---|---|---|
| **Symmetric(대칭키)** | **하나의 공유 키**로 암·복호화 | 빠름, 키 공유가 문제 | **AES, DES, 3DES, RC4**, Blowfish |
| **Asymmetric(비대칭키/공개키)** | **공개키(잠금)+개인키(해제)** 쌍 | 느림, 키 배포 쉬움 | **RSA, ECC(타원곡선), Diffie-Hellman** |

- **암호화 모드**: **ECB**(패턴 노출, 약함) vs **CBC**(IV로 체이닝, 안전). ← Adobe 유출이 ECB 때문.
- **Key length(키 길이)** ⭐: 길수록 안전. **현대 알고리즘에서 가장 흔한 키 길이 = 128 bits.** (그 외 192, 256도 있음)
  - 시험 유형(Q9): "현대 알고리즘에서 가장 흔한 키 길이?" → **128 bits**

## 4-2. 해시 (Hash) & 무결성
- **Hash(해시)**: 데이터를 **고정 길이 지문**으로 변환 (단방향, 되돌릴 수 없음).
- 용도: **무결성(Integrity)** 검증, 비밀번호 저장, 서명.
- 대표 해시: **SHA(SHA-1, SHA-256), MD5**.

## 4-3. SSL / TLS ⭐
- **SSL (Secure Sockets Layer)**: 옛날 암호화 통신 프로토콜.
- **TLS (Transport Layer Security)**: **SSL의 표준화된(후속) 버전.** 지금 HTTPS는 사실상 TLS.
  - 시험 유형(Q6): "SSL의 인터넷 표준 버전은?" → **TLS** (SSH/HTTP/SLP는 오답)

### Cipher Suite(암호 스위트) 읽는 법 ⭐⭐
형식: `SSL_[키교환]_WITH_[대칭암호]_[해시]`

예시: **`SSL_RSA_WITH_RC4_128_SHA`**
| 부분 | 의미 |
|---|---|
| **RSA** | 키 교환/인증 알고리즘 |
| **RC4_128** | 대칭 암호 = RC4, 키 128비트 |
| **SHA** | **해시(MAC) 알고리즘** |

- 시험 유형(Q29): "이 cipher suite의 **해시 알고리즘**은?" → **SHA** (RSA=키교환, RC4=암호라 오답)

## 4-4. 인증서 & CA 신뢰 (Week 4 Lab 복습)
- 자기서명 CA를 만들고 → 서버 인증서를 서명 발급 → 브라우저가 CA를 신뢰해야 HTTPS 경고가 사라짐.
- 실제 사고: **DigiNotar**(CA 침해), **Heartbleed**(개인키 유출), **Lenovo Superfish**(악성 루트CA), **Adobe**(ECB 모드).

---

# PART 5. ⚡ 시험 직전 30초 암기 카드

| 질문 키워드 | 정답 |
|---|---|
| 행위를 entity로 유일 추적 | **Accountability** |
| 의도한 기능을 조작 없이 수행 | **System Integrity** |
| 시스템 자원을 변경하는 공격 | **Active** |
| 엿듣기만/트래픽 분석 | **Passive** |
| 사이버보안 정확한 정의 | **HW+SW 보호** |
| malware 정의 | **해를 끼칠 수 있는 원치 않는 코드** |
| WannaCry | **비트코인 요구 crypto worm/랜섬웨어** |
| 흔한 키 길이 | **128 bits** |
| 재전송 방지 랜덤값 | **nonce** |
| 공개키 인증서 표준 | **X.509** |
| 중앙집중 신원 접근 | **Identity management** |
| EU 프라이버시 | **GDPR** |
| CVSS | **Common Vulnerability Scoring System** |
| 웹 성공 코드 | **200** |
| CSRF | **Cross-Site Request Forgery** (T/F 함정 주의) |
| 서버에 저장하는 XSS | **Persistent XSS** |
| 타원곡선 PKI 표준 | **PKCS#13** |
| Kerberos = KDC | **True** |
| SSL 표준 버전 | **TLS** |
| cipher suite의 해시 | 맨 끝 = **SHA** |
| SYN flooding 결과 | **서버 자원 고갈 + DoS** |
| Incident Response | **조사·대응서 얻은 통찰** |
| header/body 구분 | **빈 줄(2×CRLF)** — "1 CRLF"는 False |

---

## 공부 순서 추천
1. **PART 5 암기카드**를 먼저 훑어 감 잡기
2. **PART 1의 보안목표(CIA+3)** 와 **PART 4 cipher suite 읽기** 는 확실히 (제일 자주 나옴)
3. 그다음 연습문제 풀면서 틀린 개념만 위로 돌아와 확인

화이팅! 🔥 개념 다 본 뒤 연습문제 풀다가 헷갈리는 거 있으면 물어봐.
