# Velloria 랜딩페이지 — Cafe24 배포 가이드

## 핵심 요약

`index.html` **한 파일만 업로드하면 끝**입니다.  
폰트·이미지가 모두 이 파일 안에 내장되어 있어 외부 파일이 필요 없습니다.

---

## 배포 방법 (Cafe24 FTP)

### 방법 A — FTP 클라이언트 (FileZilla 등)

1. Cafe24 호스팅 FTP 정보 확인  
   → 관리자페이지 > 호스팅 관리 > FTP 접속정보
2. FTP 클라이언트로 접속
3. `/public_html/` 폴더에 `index.html` 업로드
4. 브라우저에서 `https://내도메인.com` 접속 확인

### 방법 B — Cafe24 파일 관리자 (FTP 없이)

1. Cafe24 관리자 > 호스팅 관리 > 파일 관리자
2. `/public_html/` 폴더 선택
3. 파일 업로드 > `index.html` 선택
4. 완료

---

## 폴더 구조 설명

```
velloria-landing/
├── index.html              ← ★ 이것만 업로드 (폰트+이미지 내장, 약 1.5MB)
│
├── assets/                 ← 원본 이미지 (이미지 교체 시 사용)
│   ├── IMG-01.jpg ~ IMG-09.jpg   ← 랜딩페이지에 쓰인 9개
│   └── (기타 추가 이미지들)
│
├── tools/                  ← 수정·재빌드 도구 (개발자용)
│   ├── index.template.html ← 본문 수정은 여기서
│   ├── subset_fonts.py     ← 폰트 서브셋 + 빌드 (1단계)
│   ├── inline_images.py    ← 이미지 인라인 + 빌드 (2단계)
│   └── fonts/              ← 원본 OTF 파일 보관 위치 (별도 보관 필요, 아래 참고)
│
├── docs/design/
│   └── velloria-image-guide.md  ← 사진 촬영/제작 가이드
│
└── README.md               ← 개발 참고 문서
```

---

## 내용 수정 후 재빌드 방법

텍스트나 카피를 바꾸거나 이미지를 교체할 경우:

### 폰트 OTF 파일 준비 (최초 1회)
`tools/fonts/` 폴더에 아래 파일들을 넣어주세요:
- `SUIT-Light.otf`, `SUIT-Medium.otf`, `SUIT-SemiBold.otf`, `SUIT-ExtraBold.otf`
  → [다운로드](https://github.com/sunn-us/SUIT/releases)
- `Pretendard-Regular.otf`, `Pretendard-Medium.otf`
  → [다운로드](https://github.com/orioncactus/pretendard/releases)
- `SCDream5.otf`
  → S-Core 공식 배포처

### 재빌드 명령
```powershell
# 1단계: 폰트 서브셋 + index.html 기본 생성
python tools/subset_fonts.py

# 2단계: 이미지 압축 + 인라인 삽입 → 최종 index.html 완성
python tools/inline_images.py
```

필요 패키지: `pip install "fonttools[woff]" brotli Pillow`

---

## 게시 전 반드시 교체할 항목

| 항목 | 현재 상태 | 교체 방법 |
|---|---|---|
| eBay 구매 링크 3곳 | `https://www.ebay.com` | `tools/index.template.html` 에서 검색·교체 후 재빌드 |
| Formspree 이메일폼 | `YOUR_FORM_ID` | formspree.io에서 발급 후 교체 |
| 후기 4개 | "예시" 표시 자리표시자 | 실제 구매자 후기로 교체 |
| 제품 정보 | FAQ 블록 비어있음 | 팔찌 길이·소재·배송 등 입력 |
| 사업자 정보 | 푸터 비어있음 | 상호·사업자번호·대표·주소 입력 |
| IMG-01, 03, 08, 09 | 가로(16:9/4:3) 이미지 | 세로(3:4) 이미지로 교체 후 재빌드 |

---

## 이미지 교체 방법

1. 새 이미지를 `assets/IMG-01.jpg` 등으로 저장 (파일명 유지)
2. 재빌드 실행:
   ```powershell
   python tools/subset_fonts.py && python tools/inline_images.py
   ```
3. 생성된 `index.html`을 Cafe24에 재업로드

---

## 주의 사항

- `index.html`은 약 **1.5MB**입니다. 첫 로딩 시 1~2초 소요될 수 있습니다.
- 이미지를 고해상도로 교체하면 파일이 더 커질 수 있으니, `tools/inline_images.py`의 압축 설정(`quality`, `max_w`)을 조절하세요.
- 콘텐츠 원칙: 허위·과장 표현 금지. 실제 후기와 확인된 제품 정보만 사용.

---

## 상품 상세페이지 — `detail.html`

랜딩(`index.html`)과 별개로, **카페24 상품 상세페이지**용 긴 에디토리얼 페이지를 함께 제공합니다.

- 파일: `detail.html` (폰트 + 사진 17장 내장, 약 2.7MB, 단일 파일)
- 구성: 표지 → 목차 → 12개 섹션(브랜드 → 제품 → 디테일 → 사양 → 착용 → 스타일링 → 일상 → 구성·가격 → 관리 → 구성품 → FAQ) → 클로징
- 시그니처: 섹션을 잇는 "한 줄의 빛" 스레드 + 스톤 노드 (테니스 팔찌의 이어진 한 줄을 페이지 구조로 표현)

### 카페24에 올리는 방법 (둘 중 택1)

1. **상품 상세 HTML 직접 붙여넣기** — 상품 관리 > 상세설명 > HTML 편집(`< >`) 모드에서
   `detail.html`의 `<body> … </body>` 안쪽 내용 + `<style> … </style>`를 붙여넣기.
2. **독립 페이지로 업로드** — `detail.html`을 그대로 `/public_html/`에 올려 별도 링크로 사용.

### 재빌드

본문/사진 수정 후:

```powershell
python tools/build_detail.py
```

> `build_detail.py` 한 번으로 폰트 서브셋 + 사진 압축·인라인을 모두 처리해 `detail.html`을 생성합니다.
> 사진은 `assets/` 파일명 일부(substring)로 매칭하므로, 교체 시 같은 키워드가 들어간 파일명을 유지하세요.

### 게시 전 교체 항목 (detail.html)

| 항목 | 현재 | 교체 |
|---|---|---|
| 구매 링크 2곳 | 팔찌 상품 페이지 URL | 그대로 사용 또는 최신 URL로 |
| 사이즈 | "옵션에서 선택" | 실제 체인 길이/사이즈 입력 |
| 구성품 3종 | 일반 표기(파우치/카드) | 실제 패키지 구성으로 |
| 사업자 정보 | 푸터 비어있음 | 상호·사업자번호 등 입력 |

> 사양은 확인된 값(CZ·실버 컬러 진공 도금·약 4mm·약 12g)만 표기했으며, 큐빅 지르코니아를 다이아몬드로 표기하지 않았습니다. 추가 사양은 확인 후에만 기재하세요.
