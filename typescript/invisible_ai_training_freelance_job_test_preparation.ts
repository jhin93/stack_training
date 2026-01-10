
//  제네릭
// 제네릭 없이 - 중복 코드
function getFirstNumber(arr: number[]): number {
  return arr[0];
}
function getFirstString(arr: string[]): string {
  return arr[0];
}
// 제네릭 사용 - 하나로
function getFirst<T>(arr: T[]): T {
    return arr[0]
};

const num = getFirst([1, 2, 3]);
const str = getFirst(['a', 'b', 'c']);

// AI 데이터 처리 예제
function processDataBatch<T>(data: T[], transform: (item: T) => T): T[] {
  return data.map(transform);
}

interface TrainingData {
  text: string;
  label: number;
}

const results = processDataBatch<TrainingData>(
  [{text: "hello", label: 1}],
  (item) => ({...item, text: item.text.toLowerCase()})
);

// 객체와 인터페이스
// 기본 인터페이스
interface User {
  id: number;
  name: string;
  email?: string;          // optional - 있어도 되고 없어도 됨
  readonly createdAt: Date; // readonly - 수정 불가
}

// Index signature - 동적 속성
interface DataLabels {
    [key: string]: number;
}

const labels: DataLabels = {
    "positive": 1,
    "negative": 0,
    "neutral": 2
}

// AI 학습 데이터 예제
interface TrainingExample {
  id: string;
  input: string;
  output: string;
  metadata?: {
    [key: string]: any;  // 유연한 메타데이터
  };
}

const example: TrainingExample = {
  id: "ex1",
  input: "What is AI?",
  output: "Artificial Intelligence is...",
  metadata: {
    difficulty: "easy",
    category: "definition"
  }
};

// 유틸리티 타입
// 설명: TypeScript가 제공하는 타입 변환 도구들입니다. 기존 타입을 변형해서 새 타입을 만듭니다.
interface User22 {
    id: number;
    name: string;
    address: string;
    password: string;
}

// Partial<T> - 모든 속성을 optional로
type UserUpdate = Partial<User22>;
const update: UserUpdate = {
    name: "New Name"
}

// Pick<T, K> - 특정 속성만 선택
type UserPreview = Pick<User22, 'id' | 'name'>;
const preview: UserPreview = {
    id: 1,
    name: "John"
}

// Omit<T, K> - 특정 속성 제외
type UserPublic = Omit<User22, 'password'>;
const publicUser: UserPublic = {
    id: 1,
    name: "John",
    address: "test22"
};

// Record<K, V> - 키-값 매핑
type UserRoles = Record<string, string[]>;
const roles: UserRoles = {
    "admin": ["read", "write", "delete"],
    "user": ["read"],
    "guest": []
};