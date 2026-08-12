# Assignment 1 — 문항별 강의자료 매핑표

마감: **2026-08-28 (금) 17:00** · 비중 20% · 8문항 100점
채점 원칙: **justification 요구 문항은 배점의 최소 절반이 justification에 배정**

자료 약칭
- **W1** = `week1/UTS Cloud Lecture 1-3.pdf` (25p)
- **W2** = `week2/Week2_CloudLecture-5.pdf` (27p)
- **W3** = `week3/Week3_CloudLecture-3.pdf` (30p)

페이지 번호는 PDF 페이지 기준(표지 = p.1)

---

## Q1 (5점) — 클라우드 정의 / 클라우드 컴퓨팅 정의 / 비용 모델

| 하위 질문 | 배점 | 자료 위치 | 내용 |
|---|---|---|---|
| What is cloud? | 2 | **W1 p.3** | "A Cloud is a pool of virtualized computer resources" + 워크로드 호스팅 + on-demand 프로비저닝. 그림 있음 |
| What is cloud computing? | 1 | **W2 p.4** ⭐ | **NIST 정의 전문** + Thomas Erl 정의. 각주에 출처 URL까지 있음 → 그대로 인용 가능 |
| | | W2 p.5 | NIST 도표: Deployment/Service Models + Essential Characteristics 5개 (On-Demand Self-Service, Broad Network Access, Resource Pooling, Rapid Elasticity, Measured Service) |
| Explain the cloud cost model | 2 | **W1 p.6** ⭐ | **비용 모델 그래프** — 전통 IT(고정 자본비 + 변동 운영비) vs 클라우드(변동 운영비만). 다이어그램으로 답하기 최적 |
| | | W1 p.5 | Computing Paradigms 표 — Buy and own vs Subscribe, "80-95% 총비용 절감", pay-as-you-go |

**작성 팁**: 정의 2개(NIST + Erl)를 대조하면 5점 만점 잡기 쉬움. 비용 모델은 W1 p.6 그래프를 직접 그려 넣을 것.

---

## Q2 (15점) — 서비스 모델 / IaaS·PaaS·SaaS와 상호관계

| 하위 질문 | 배점 | 자료 위치 | 내용 |
|---|---|---|---|
| What are the cloud service models? | 3 | **W1 p.7** | IaaS/PaaS/SaaS 삼각 관계도 + 각 한 줄 정의 |
| Describe IaaS, PaaS, SaaS **and the relationships among them** | 12 | **W1 p.8** ⭐⭐ | **Service Layers Definition** — People / Client Device / Hosted App SW / Infrastructure SW / OS / **Virtualisation Layer** / Physical Servers / Networking & Firewalling / Data Centre M&E 계층 + 각 aaS가 어디까지 포함하는지 화살표. **"relationships" 답의 핵심 그림** |
| | | W1 p.9 | Layered Cloud Architectural Development — IaaS→PaaS→SaaS 위로 쌓이는 구조 |
| | | **W2 p.7** | IaaS 다이어그램 + SLA 계약 예시 (Virtual Server 32GB RAM, 가용성 99.5%, $0.95/hour) |
| | | **W2 p.8** | PaaS 다이어그램 — ready-made environment, "?"는 구현 상세가 의도적으로 은닉됨을 표시 |
| | | **W2 p.9** | SaaS 다이어그램 — 계약만 접근 가능, 하위 IT 자원 접근 불가 |

**주의**: Deployment Models(Public/Private/Community/Hybrid, W1 p.10 · W2 p.5)는 **Service Model이 아님.** 섞어 쓰면 감점.

**작성 팁**: 12점짜리라 각 모델당 약 3점 + 관계 설명 3점 배분. "누가 무엇을 관리하는가(책임 경계)"로 관계를 설명하면 강함.

---

## Q3 (15점) — 클라우드 구성요소 / 구성요소 기반 아키텍처

| 하위 질문 | 배점 | 자료 위치 | 내용 |
|---|---|---|---|
| What are the cloud components? | 5 | **W2 p.18** ⭐ | **Typical Cloud Architecture — Components: Virtual machines / Hypervisor / Physical Servers / Networks / SAN Storage.** 5점짜리 직답 |
| | | W3 p.3 | 다른 관점: Broadband Networks, Data Center, Virtualization, Web, Multitenant, Service Technology (6종) |
| Describe the cloud architecture based on these components | 10 | **W1 p.12** ⭐⭐ | **IaaS Cloud Architecture / Cloud OS 전체 구성도** — Tools층 / Core층 / Drivers층 / Physical infrastructure. **10점짜리 뼈대** |

### Cloud OS 컴포넌트별 역할 (W1 p.13~23) — 아키텍처 서술 재료

| 컴포넌트 | 페이지 | 역할 |
|---|---|---|
| VM manager | W1 p.13 | VM 전 생명주기 관리 (deploy, migrate, suspend, resume, shut down) |
| Network manager | W1 p.14 | 사설망 관리, 공인 IP 풀 관리, 프론트엔드↔인터넷 연결 |
| Storage manager | W1 p.15 | 스토리지 서비스·가상 스토리지를 commodity로 제공 |
| Federation manager | W1 p.16 | 원격 클라우드 인프라 접근 |
| Image manager | W1 p.17 | 다양한 OS/설정의 VM 이미지 대량 관리 |
| Auth & authorization | W1 p.18 | 인증 및 인가된 자원만 접근 허용 |
| Accounting & auditing | W1 p.19 | 배포 서비스의 자원 사용량 기록 |
| Information manager | W1 p.20 | VM·물리서버·네트워크·스토리지 상태 모니터링 |
| Administrator tools | W1 p.21 | 사용자 관리 도구, 물리 인프라 관리 도구 |
| Service manager / Cloud interfaces | W1 p.22 | 가상화된 multitier 서비스 관리 / 벤더별 API 제공 |
| Scheduler | W1 p.23 | 호스트 레벨(하이퍼바이저 스케줄러: 언제 자원 획득, 어느 물리 CPU 할당) / 클라우드 레벨(어느 물리 서버에 배치) / 페더레이션(로컬 자원 부족 시 원격 클라우드 배치) |

### 추가 메커니즘 (아키텍처 서술 깊이용)

| 그룹 | 페이지 | 항목 |
|---|---|---|
| Cloud **Infrastructure** Mechanisms | W3 p.9~15 | Logical Network Perimeter / Virtual Server / Cloud Storage Device / Cloud Usage Monitor(Monitoring·Polling·Resource Agent) / Resource Replication / Ready-made Environment |
| Cloud **Management** Mechanisms | W3 p.16~20 | Remote Administration System / Resource Management System / SLA Management System / Billing Management System |
| Cloud **Security** Mechanisms | W3 p.21 | Encryption, Hashing, Digital Signatures, PKI, IAM, SSO, Cloud-Based Security Groups, Hardened Virtual Server Images |
| Fundamental Cloud **Architectures** | W3 p.22~26 | Workload Distribution / Resource Pooling / Dynamic Scalability / Service Load Balancing |
| VIM (Virtual Infrastructure Manager) | W2 p.19 | 여러 하이퍼바이저를 한 VIM이 통합 제어 |
| vCenter 구조 | W3 p.28 | User Access Control, Core Services, Distributed Services(DRS·HA·vMotion·FT), Plug-ins, Interfaces |

**작성 팁**: W1 p.12 구성도를 다시 그리고 층별로 설명하는 방식이 가장 안전. Cloud OS = "클라우드의 운영체제"라는 비유(W1 p.24: 일반 OS와의 유사점)를 쓰면 서술이 매끄러움.

---

## Q4 (20점) ⭐ 최대 배점 — 가상화 / 가상화 계층 / 하이퍼바이저

| 하위 질문 | 배점 | 자료 위치 | 내용 |
|---|---|---|---|
| What is virtualisation? | 5 | **W2 p.11** | "Abstraction of computer resources" + 목표: IT 자원 최대 활용 및 비용 절감 |
| | | W2 p.13 | **Without VMs vs With VMs 그림** — VMM이라는 새 소프트웨어 계층 삽입 |
| Describe different **layers** of virtualisation | 5 | **W2 p.12** ⭐ | **Types of Virtualization: Processor / Memory / Network / Storage** — 각각 한 줄 정의 포함 |
| | | **W3 p.7** | 보강: Servers / Storage / Network / **Power(virtual UPS)**. 출처가 Erl 교재로 명시돼 인용에 유리 |
| What is hypervisor? | 5 | **W2 p.15** ⭐ | 하이퍼바이저(VMM) 정의 — 게스트 OS와 시스템 자원 관리, 격리 지원, VM에 Logical CPU/memory/storage blocks/network 제공 |
| | | **W2 p.17** ⭐ | **Type 1 (bare-metal) vs Type 2 (hosted) 다이어그램** |
| What does a hypervisor do? | 5 | **W2 p.16** ⭐ | **Functions of Hypervisors 4가지**: ① VM 생성·관리 ② 가상화된 하드웨어 자원 풀에서 VM에 자원 할당 ③ VM 상태 모니터링 ④ VM의 시스템 간 이동에 관여 |
| | | W2 p.14 | Virtual Machine 정의 — 격리된 인스턴스, 가상 HW·가상 디스크·메타데이터 캡슐화 |

### 🔥 랩 경험을 justification으로 (여기가 점수)

| 쓸 내용 | 근거 |
|---|---|
| ESXi = Type 1 하이퍼바이저 | Week2 랩에서 OS 없이 베어메탈에 직접 설치 (18GB 디스크에 직접 설치) |
| Type 1을 Type 2 위에 중첩하려면 하드웨어 가상화 확장 필요 | Workstation에서 `Virtualize Intel VT-x/EPT` 를 켜야 ESXi 안의 VM이 동작 → Type 1이 CPU 가상화 확장에 직접 의존한다는 실증 |
| 하이퍼바이저의 "VM 이동 관여" 기능 | Week4 랩 vMotion — 전원 켠 채 호스트 간 이동 |
| 자원 할당·격리 기능 | Week6 랩 Resource Pool의 shares/limit로 CPU 배분 차등 |

---

## Q5 (15점) — 스토리지 가상화 / SAN

| 하위 질문 | 배점 | 자료 위치 | 내용 |
|---|---|---|---|
| What is storage virtualisation? | 2 | **W2 p.22** ⭐ | **정의 인용문**: "the process of presenting a logical view of the physical storage resources to a host computer system, treating all storage media (hard disk, optical disk, tape, etc.) in the enterprise as a single pool of storage" |
| What does storage virtualisation do? | 5 | **W2 p.22** ⭐ | **Block-level / File-level** 두 유형 + **Network-based / Host-based / Array-based** 세 방식 |
| | | W2 p.24 | 물리 스토리지 서브시스템의 복잡성·차이를 숨기는 추상화 계층. VM 내부에는 가상 HBA에 연결된 SCSI 디스크로 제시 |
| | | W3 p.12 | Cloud Storage Device — file/block/object/dataset 접근 방식별 프로토콜 (iSCSI·FC·FCoE LUN / POSIX NFS·CIFS / HTTP CRUD / DBMS API) |
| **When should it be used?** | 3 | ⚠️ **강의에 없음** | **외부 조사 필수.** 여기가 justification 배점 |
| What is SAN? | 2 | **W2 p.21** ⭐ | **NAS vs SAN 다이어그램** — SAN Switch, 파이버 옵틱, SAN Storage pools |
| What does SAN do? | 3 | W2 p.21 / W3 p.6 | 블록 수준 스토리지 네트워크. DB 서버·메일 서버·하이퍼바이저가 공유 |
| | | W2 p.20 | 대조군: DAS(Direct Attached Storage) + HBA |
| | | **W2 p.23** ⭐ | VMware Storage Architecture — datastore1/datastore2, **VMFS volume**, NFS, 하단에 DAS SCSI / FC SAN / iSCSI / NAS |

### 🔥 랩 경험을 justification으로

Week3 랩에서 iSCSI 타겟(172.20.20.50)을 ESXi01·ESXi02 **양쪽**에 dynamic target으로 붙이자, 두 호스트에서 **동일한 VMFS 데이터스토어**가 보였음 → 물리 디스크의 위치·종류와 무관하게 블록 스토리지를 단일 풀로 추상화한 실제 사례. Week4에서 이 공유 스토리지가 있었기에 **Storage vMotion / vMotion이 가능**했음 → "언제 스토리지 가상화를 써야 하는가(3점)"의 강력한 근거.

---

## Q6 (10점) — IaaS 구축의 도전과제 5가지 이상 + 대응

⚠️ **강의에 목록이 통째로 있지는 않음. 외부 조사 중심 + 아래 단서 활용.**

| 도전과제 후보 | 강의 단서 | 대응책 단서 |
|---|---|---|
| 보안·멀티테넌시 격리 | W3 p.21 (보안 메커니즘 8종) | 암호화, IAM, SSO, Cloud-Based Security Groups, Hardened VM Images |
| 자원 스케줄링·과다구독 | W1 p.23 (Scheduler 3계층) | 호스트/클라우드/페더레이션 레벨 스케줄링 |
| 확장성·부하 급증 | W3 p.24~26 | Dynamic Scalability, Service Load Balancing, Resource Replication |
| 가용성·장애 대응 | W3 p.28 (vCenter Distributed Services: HA·FT) | HA 클러스터, 이중화 |
| SLA 보장·과금 정확도 | W3 p.18~20 | SLA Management System, Billing Management System |
| 모니터링·가시성 | W3 p.13 (Cloud Usage Monitor) | Monitoring/Polling/Resource Agent |
| 네트워크 격리·복잡도 | W3 p.10 (Logical Network Perimeter) | VLAN, 포트그룹, 가상 방화벽 |
| 벤더 종속 / 상호운용성 | W1 p.22 (벤더별 자체 API) | 표준 API, 페더레이션 |

**🔥 랩 경험**: vmnet 설정 오류로 호스트-ESXi 통신 실패, 라이선스 만료 경고, 중첩 가상화 미설정, HA isolation address 도달 실패(Week7 랩 워크어라운드) — 전부 "실제 IaaS 구축 시 겪는 난제"의 1인칭 사례로 쓸 수 있음.

---

## Q7 (10점) — NaaS / 클라우드 생태계

| 하위 질문 | 배점 | 자료 위치 | 내용 |
|---|---|---|---|
| What is Network as a Service? | 5 | **W2 p.27** ⭐ | **Network Virtualization** — Server Virtualization(2001, x86)과 Network Virtualization(2012, Packet Forwarding) 대조. Logical Switch / Logical Router / Logical Load Balancer / Logical Firewall. **DECOUPLE → REPRODUCE → AUTOMATE**. 출처: VMware NSX 백서 |
| | | W2 p.25 | VMware Network Architecture — vSphere Standard Switch, **port groups**, 물리 NIC 매핑 |
| | | W2 p.26 | 가상 NIC, port group이 라벨 네트워크의 안정적 앵커 역할 |
| | | W3 p.10 | Logical Network Perimeter — 통신망에서의 네트워크 격리 |
| | | W3 p.4~5 | Broadband Networks, ISP, Connectionless Packet Switching, Router-Based Interconnectivity |
| Explain the cloud ecosystems | 5 | ⚠️ **강의에 없음** | **외부 조사 필수.** 단서: W2 p.6 Terminology(cloud provider/consumer/service owner/resource administrator/**carrier**) → 생태계 참여자 프레임으로 활용 가능 |

⚠️ **NaaS 용어 자체는 Week 4 강의(8/17~) 주제.** 강의를 기다리면 늦으므로 W2 p.27 + 외부 자료로 먼저 작성하고, 강의 후 용어만 맞출 것.

---

## Q8 (10점) — 데이터센터 정의 / 기본 구성요소

| 하위 질문 | 배점 | 자료 위치 | 내용 |
|---|---|---|---|
| What is a data center? | 5 | ⚠️ 정의는 부족 | **외부 조사 필요.** Week 5 강의가 마감 주간이라 기다리면 위험 |
| **List some basic components** | 5 | **W3 p.6** ⭐⭐ | **통째로 답이 있음**: |

### W3 p.6 — Data Center Technology (그대로 구성요소 답안)

| 분류 | 세부 |
|---|---|
| **Facilities** | Housing, racks, cabling, power supplies, environmental control station (heating, ventilation, air conditioning, fire protection 등) |
| **Computing Hardware** | Server, blade servers 등 |
| **Storage Hardware** | Hard Disk Arrays, Storage Area Network (SAN), Network-Attached Storage (NAS) |
| **Network Hardware** | Carrier and External Network Interconnection, Web-Tier Load Balancing and Acceleration, LAN Fabric, SAN Fabric, NAS Gateways |

**보조 자료**
- **W2 p.10** — Physical topology of VMware Infrastructure Data Center 다이어그램 (vCenter Server, vSphere Client, server groups, ESX/ESXi, fibre channel switch fabric, FC/iSCSI/NAS storage array) ← 다이어그램으로 답할 때 최적
- W3 p.27 — Hosts, Clusters and Resource Pools (물리 x86 서버 3대 → Cluster 12GHz/48GB → 부서별 resource pool)

---

## 📚 강의자료에 이미 명시된 인용 가능 출처

Harvard 인용에 바로 쓸 수 있는 것들. 강사가 직접 인용한 자료라 안전합니다.

| 출처 | 어디에 | 활용 문항 |
|---|---|---|
| **NIST** 클라우드 정의 (2011) — nist.gov | W2 p.4 각주 | **Q1, Q2** (필수급) |
| **Erl, T., Puttini, R. & Mahmood, Z.** (2013) *Cloud Computing: Concepts, Technology & Architecture*, Pearson | W2 p.4, W3 p.7 | Q1~Q6 전반 |
| cloudpatterns.org/mechanisms/overview | W3 p.9, 16, 21 | Q3, Q6 |
| VMware NSX Network Virtualization 백서 | W2 p.27 각주 | **Q7** |
| VMware vMotion Datasheet | W3 p.30 각주 | Q4, Q6 |
| pubs.vmware.com — Storage / Network Architecture | W2 p.24, p.26 | Q5, Q7 |
| whatiscloud.com — technology innovations | W3 p.3 | Q3 |
| informit.com article 2093407 | W3 p.22 | Q3 |
| techrepublic — NIST cloud standard | W2 p.5 | Q1 |

---

## ⚠️ 강의자료로 커버 안 되는 부분 (외부 조사 필수)

| 문항 | 빠진 부분 | 배점 |
|---|---|---|
| Q5 | 스토리지 가상화를 **언제** 써야 하는가 | 3 |
| Q6 | IaaS 도전과제 5가지 **목록과 대응책** | 10 |
| Q7 | **cloud ecosystems** 설명 | 5 |
| Q8 | 데이터센터 **정의** | 5 |
| | **합계** | **23점** |

→ 100점 중 **23점은 외부 자료 없이는 못 채웁니다.** 과제문에 "강의노트만으로는 불충분"이라 명시된 이유.

---

## 작성 순서 권장 (배점 큰 순서)

```
1. Q4 (20) — W2 p.11~17 만으로 거의 완결. 랩 경험 추가 → 만점 노려볼 것
2. Q2 (15) — W1 p.8 계층도가 핵심
3. Q3 (15) — W2 p.18(components) + W1 p.12(architecture)
4. Q5 (15) — W2 p.20~24. "언제 쓰나" 3점만 외부 조사
5. Q6 (10) — 외부 조사 중심. 랩 경험 활용도 최고
6. Q1 (5)  — W2 p.4 + W1 p.6. 가장 빠르게 끝남
7. Q7 (10) — W2 p.27 + 외부 (Week4 강의 후 보완)
8. Q8 (10) — W3 p.6 + 외부 정의 (Week5 강의 기다리지 말 것)
```

**강의자료만으로 커버되는 배점: 약 77점.** 나머지 23점이 외부 조사 몫입니다.
