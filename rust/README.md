# Rust 개발자 로드맵 - 아일랜드 취업 특화 (1년 과정)

## 🎯 목표
아일랜드 Tech 기업에서 Rust 경력 개발자로 채용 가능한 수준의 역량 확보

## 🇮🇪 아일랜드 Rust 채용 시장 분석
- **블록체인/Web3**: Ethereum, Polkadot 관련 기업들 (ConsenSys, Parity 등)
- **클라우드 네트워킹**: AWS, Microsoft, Google의 더블린 오피스
- **사이버 보안**: Symantec, McAfee, IBM Security 등 보안 기업

## 📚 Phase 1: 핵심 기본기 속성 (8주)

### Part A: 공식 문서 완주 (5주) https://doc.rust-kr.org/title-page.html
**The Rust Programming Language 완독**
- **1주차**: Ch 1-4 (시작하기, 추리 게임, 일반 개념, 소유권) 
  - ch1, ch2 complete(9/26)
- **2주차**: Ch 5-8 (구조체, 열거형, 패키지/크레이트, 컬렉션)
- **3주차**: Ch 9-12 (에러처리, 제네릭/트레이트, 테스팅, 미니프로젝트)
- **4주차**: Ch 13-16 (클로저/반복자, Cargo, 포인터, 동시성)
- **5주차**: Ch 17-20 (OOP, 패턴매칭, 고급기능, 웹서버 프로젝트)

### Part B: 실무 & 인터뷰 필수 (3주)
**아일랜드 기업이 반드시 묻는 핵심**

#### 6주차: 소유권과 라이프타임 심화
- **빌림 체커 완벽 이해** (실무 디버깅 필수)
- **라이프타임 어노테이션** 실전 패턴
- **Cow, Pin, PhantomData** 고급 타입
- 코딩 테스트: 소유권 관련 문제 10개

#### 7주차: 비동기와 성능
- **async/await 내부 동작** (Future, Pin)
- **Tokio vs async-std** 차이점
- **성능 프로파일링** (flamegraph, criterion)
- 코딩 테스트: 비동기 처리 문제 5개

#### 8주차: 실무 패턴과 베스트 프랙티스
- **에러 처리 전략** (anyhow vs thiserror)
- **Builder 패턴, Type State 패턴**
- **unsafe 코드** 언제 써야 하나
- **매크로 작성** 기초
- 모의 인터뷰: 주요 질문 20개 연습

## 🚀 Phase 2: 프로젝트 중심 학습 (44주)

### 프로젝트 1: 초급 - CLI 도구 모음 (8주)
**실무형 CLI 도구 3개 개발**
- **주차 1-3**: 파일 동기화 도구 (병렬 처리, 해시 비교)
- **주차 4-5**: 로그 분석기 (정규식, 통계)
- **주차 6-8**: 시스템 모니터 (CPU/메모리/네트워크)
- 학습 포인트: 에러 처리, 파일 I/O, 병렬 처리, clap 사용법

### 프로젝트 2: 중급 - 웹 API 서버 (10주)
**Production급 백엔드 서비스**
- **주차 9-11**: 기본 REST API (Axum, SQLx)
- **주차 12-14**: 인증/인가 시스템 (JWT, 세션)
- **주차 15-16**: WebSocket 실시간 기능
- **주차 17-18**: 캐싱과 성능 최적화 (Redis)
- 학습 포인트: 비동기 프로그래밍, DB 연동, 보안, 테스팅

### 프로젝트 3: 블록체인 - 간단한 DeFi 프로토콜 (8주)
**아일랜드 Web3 기업 대비**
- **주차 19-21**: 기본 블록체인 구조 (해시, 머클트리)
- **주차 22-24**: 트랜잭션과 지갑 시스템
- **주차 25-26**: 스마트 컨트랙트 기초 (WASM)
- 학습 포인트: 암호화, P2P 네트워킹, 컨센서스

### 프로젝트 4: 네트워킹 - 로드 밸런서 (9주)
**클라우드 인프라 대비**
- **주차 27-29**: TCP/HTTP 프록시 기초
- **주차 30-32**: 헬스체크와 라우팅 알고리즘
- **주차 33-35**: 메트릭과 모니터링 (Prometheus)
- 학습 포인트: 소켓 프로그래밍, 성능 최적화, 관찰성

### 프로젝트 5: 보안 - 네트워크 스캐너 (9주)
**보안 기업 대비**
- **주차 36-38**: 포트 스캔과 서비스 탐지
- **주차 39-41**: 취약점 스캔 기초
- **주차 42-44**: 보고서 생성과 알림
- 학습 포인트: 네트워크 프로토콜, 병렬 스캔, 보안 패턴

### 마무리 - 포트폴리오 정리와 오픈소스 (주차 45-52, 8주)
- **주차 45-47**: 프로젝트 리팩토링과 문서화
- **주차 48-50**: Rust 오픈소스 기여 (이슈 해결)
- **주차 51-52**: 이력서와 GitHub 포트폴리오 완성

## 🛠 필수 도구와 크레이트

### 개발 도구
- **rustup** - Rust 버전 관리
- **cargo** - 빌드 시스템
- **rustfmt** - 코드 포맷터
- **clippy** - 린터
- **rust-analyzer** - LSP

### 핵심 크레이트
- **serde** - 직렬화/역직렬화
- **tokio** - 비동기 런타임
- **reqwest** - HTTP 클라이언트
- **clap** - CLI 파싱
- **tracing** - 로깅/트레이싱
- **thiserror/anyhow** - 에러 처리

## 📖 추천 학습 자료

### 필독서
1. **The Rust Programming Language** (공식 문서)
2. **Rust by Example**
3. **Async Programming in Rust**
4. **The Rustonomicon** (unsafe 코드)

### 온라인 리소스
- [Rust 공식 문서](https://doc.rust-lang.org)
- [Rust Cookbook](https://rust-lang-nursery.github.io/rust-cookbook/)
- [Awesome Rust](https://github.com/rust-unofficial/awesome-rust)
- [This Week in Rust](https://this-week-in-rust.org/)

## ✅ 아일랜드 취업 준비 체크리스트

### 필수 역량
- [ ] 소유권과 라이프타임 완벽 이해
- [ ] Result/Option 자연스러운 사용
- [ ] 비동기 프로그래밍 숙달
- [ ] 테스트 작성 습관화
- [ ] 에러 처리 베스트 프랙티스

### 아일랜드 시장 특화 경험
- [ ] 블록체인/Web3 프로젝트 경험
- [ ] 고성능 네트워킹 시스템 구축
- [ ] 보안 도구 개발 경험
- [ ] 클라우드 네이티브 애플리케이션
- [ ] 분산 시스템 이해

### 실무 경험
- [ ] gRPC/Protocol Buffers 사용
- [ ] 메트릭 모니터링 (Prometheus/Grafana)
- [ ] 컨테이너화 (Docker/Kubernetes)
- [ ] CI/CD 파이프라인 구축
- [ ] 성능 최적화와 프로파일링

### 소프트 스킬
- [ ] 영어 기술 문서 작성
- [ ] 오픈소스 기여 (특히 Rust 생태계)
- [ ] 코드 리뷰 문화 이해
- [ ] 애자일/스크럼 경험

## 📅 주간 학습 계획

### 일일 루틴 (1.5시간)
- **30분**: 이론 학습 및 문서 읽기
- **45분**: 코딩 실습
- **15분**: 복습 및 노트 정리

### 주간 목표 (10.5시간)
- **월-수**: 새로운 개념 학습 (4.5시간)
- **목-금**: 실습 프로젝트 (3시간)
- **주말**: 심화 학습 또는 코드 챌린지 (3시간)

## 🎯 마일스톤

### 2개월 차 (기본기 완료)
- Rust 핵심 문법 이해
- 소유권 시스템 기본 습득
- 간단한 프로그램 작성 가능

### 4개월 차 (첫 프로젝트)
- CLI 도구 3개 완성
- 에러 처리와 테스팅 숙달
- GitHub에 코드 공개

### 7개월 차 (웹 개발)
- Full-stack 웹 서비스 구현
- 비동기 프로그래밍 숙달
- DB와 캐싱 이해

### 10개월 차 (전문 분야)
- 블록체인/네트워킹/보안 중 2개 완성
- 실무급 프로젝트 보유
- 오픈소스 기여 시작

### 12개월 차 (취업 준비)
- 5개 실무 프로젝트 완성
- 아일랜드 기업 지원 가능
- 주니어 개발자 역량 확보

---

Rust Concept
```rust
// ⏺ Rust의 prelude는 모든 Rust 프로그램에 자동으로 import되는 표준 라이브러리의 기본 타입과
//   트레이트 모음입니다.
// 
//   주요 특징
// 
//   자동 import: std::prelude::v1::*이 모든 모듈에 암시적으로 포함됩니다.
// 
//   포함된 주요 항목들:
//   - 기본 타입: Option<T>, Result<T, E>
//   - 트레이트: Copy, Clone, Eq, PartialEq, Ord, PartialOrd, Debug, Display
//   - 반복자: Iterator, IntoIterator, DoubleEndedIterator, ExactSizeIterator
//   - 변환: From, Into, AsRef, AsMut
//   - 메모리: Drop, Sized, Send, Sync
//   - 문자열: ToString, &str, String
//   - 벡터: Vec
//   - 매크로: println!, eprintln!, format!, vec!

  // prelude 덕분에 별도 import 없이 사용 가능
  fn example() -> Option<String> {
      let v = vec![1, 2, 3];  // vec! 매크로
      Some("hello".to_string())  // Option, ToString
  }

  // 커스텀 prelude를 만들어 프로젝트 전체에서 공통으로 사용하는 타입들을 관리할 수도 있습니다.


// MUT, Shadowing
fn main() {
    // mut
    let mut y = 5;
    println!("mut y result : {y}");
    y = 6;
    println!("mut y result : {y}");

    // shadowing
    let x = 5;

    let x = x + 1;

    let x = x + 4;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}"); // 20
    }

    println!("The value of x is: {x}"); // 10


}


// Underscore
// ⏺ Rust에서 언더스코어(_)를 변수명 앞에 붙이는 이유는 "이 변수를 의도적으로 사용하지 않을 
//   것"이라고 컴파일러에게 명시적으로 알려주기 위함입니다.
// 
// 이유:
// 1. 경고 제거: _가 붙은 변수는 컴파일러가 "unused variable" 경고를 내지 않음
// 2. 코드 의도 명확화: 다른 개발자가 볼 때 "실수로 안 쓴 게 아니라 의도적으로 안 쓴다"는
// 것을 알 수 있음
// 3. 패턴 매칭 시 유용: 튜플이나 구조체에서 특정 값만 필요할 때, 나머지는 _로 무시
// 
// 예시:
fn main() {
    let (x, _y, z) = (1, 2, 3);  // y는 필요없지만 구조분해는 필요
    let _unused = 42;             // 나중에 쓸 수도 있지만 지금은 안 씀
    let _ = function();           // 반환값 완전 무시
}

// Tuple
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x, y, z) = tup;
    println!("The value of y is: {}", y);

    // Accessing Tuple Elements
    let x: (i32, f64, u8) = (500, 6.4, 1);
    let five_hundred = x.0;
    let six_point_four = x.1;
    let one = x.2;

    println!("The value of five_hundred is: {}", five_hundred);
}
// Array
fn main() {
    let a: [i32; 5] = [1, 2, 3, 4, 5];
    let b = [3; 5]; // let b = [3, 3, 3, 3, 3];
}
```