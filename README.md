# Velloria — 데일리 팔찌 랜딩페이지 (velloriacopy1)

> **"손목 위 조용한 우아함"** · 비싼 척하지 않아도 충분히 고급스러운 데일리 팔찌 브랜드의 단일 페이지 랜딩.
> 구매는 **eBay 리스팅에서 완료**됩니다 — 이 페이지는 제품을 보여주고 구매처로 연결하는 역할을 합니다.

- **라이브:** https://velloriacopy1.vercel.app (Vercel 배포 후)
- **언어:** 한국어
- **구성:** 정적 HTML **단일 파일** — 빌드 단계 없음, 외부 의존성 없음 (폰트가 base64로 내장됨)
- **디자인:** 화이트·블랙 모노톤(레퍼런스 팔레트 기반). 스크롤 등장·마퀴·가격 카운트업·자가 드로잉 아크 등 **모션 다수**. `prefers-reduced-motion`이거나 JS가 막혀도 콘텐츠·가격이 정상 표시되도록 **점진적 향상** 적용.

---

## 파일 구조

```
velloriacopy1/
├── index.html                 # 랜딩페이지 전체 (스타일·폰트 모두 이 한 파일에 포함) ← 배포 대상
├── vercel.json                # Vercel 정적 호스팅 설정 (보안 헤더 등)
├── .gitignore / .gitattributes
├── README.md
└── tools/                     # 빌드 도구 (배포에는 불필요, 재서브셋용)
    ├── index.template.html    # 폰트 토큰(__SUIT_LIGHT__ 등)이 들어간 원본 템플릿
    ├── subset_fonts.py        # 폰트 서브셋 + base64 임베드 → index.html 생성
    └── fonts/                 # 원본 OTF 6종 (git 미포함, 로컬 보관)
```

> **수정 흐름:** 본문/카피는 `tools/index.template.html`에서 고치고 → `python tools/subset_fonts.py`를 실행하면 → `index.html`이 새로 생성됩니다. `index.html`을 직접 손대도 되지만, 한국어 글자를 새로 추가하면 폰트를 다시 서브셋해야 합니다(아래 폰트 항목 참고).

---

## ★ 게시 전 반드시 교체할 항목

이 페이지는 **콘텐츠 원칙(허위·과장 금지)** 을 지키도록, 확인되지 않은 정보는 비워두거나 “예시”로 표시해 두었습니다. 라이브 트래픽을 보내기 전에 아래를 채워주세요.

1. **구매 CTA 링크 (eBay 임시 placeholder · 4곳)**
   현재 모든 구매 버튼이 `https://www.ebay.com` 으로 연결되어 있습니다. 실제 리스팅 URL로 바꿔주세요.
   위치: 히어로 / 가격 섹션 / 한정수량 섹션 / 마지막 CTA — `index.html`(또는 템플릿)의 `https://www.ebay.com` **4곳**.

2. **이메일 폼 (Formspree)**
   `무료 코디 이미지팩` 폼은 [Formspree](https://formspree.io) 무료 폼으로 동작합니다.
   - Formspree에서 폼 1개 생성 → 발급된 엔드포인트(`https://formspree.io/f/XXXXXXX`)를 복사
   - `index.html`의 `https://formspree.io/f/YOUR_FORM_ID` 를 그 주소로 교체
   - 연결 전에는 버튼을 눌러도 “폼이 아직 연결되지 않았습니다” 안내만 표시됩니다(에러 없음).

3. **후기 섹션 (예시 → 실제 후기)**
   `증거/신뢰` 섹션의 4개 후기는 **“예시”로 표시된 자리표시자**입니다. 콘텐츠 원칙상 **실제 구매자/착용자 후기로만** 교체해 주세요(임의로 만든 후기 사용 금지). 실제 후기를 넣은 뒤 `예시` 배지와 `※ 예시…` 안내를 제거하면 됩니다.

4. **제품 정보 / 사업자 정보**
   - FAQ 하단 “제품 정보 — 게시 전 입력” 블록: 팔찌 길이·소재·도금 여부·착용 주의·배송·교환/반품 기준을 **확인된 사실로** 채워주세요.
   - 푸터 `상호 · 사업자등록번호 · 통신판매업 신고번호 · 대표 · 주소 · 고객센터` 를 입력해주세요(전자상거래법 표시 의무).

5. **이미지 (IMG-01 ~ IMG-09)**
   제품/착용 사진 자리는 **점선 슬롯**으로 비워 두었고, 각 슬롯에 `IMG-01`처럼 번호와 **촬영 가이드 문구**가 적혀 있습니다(레퍼런스와 동일한 방식). 해당 컷을 촬영해 슬롯을 실제 이미지로 교체하면 됩니다. 목록: 01 히어로 제품컷 · 02 데일리 착용컷 · 03 매크로 디테일 · 04~07 니트/셔츠/데이트/데님 룩 · 08 소량 패키지 · 09 마지막 클로즈업.

---

## 콘텐츠 원칙 (중요)

근거 없는 과장·허위 표현은 넣지 않습니다. **실제 검증된 후기와 확인된 제품 사실만** 사용합니다.
금지 예시: 가짜 후기·별점·구매수, 거짓 한정수량/마감 타이머, 확인되지 않은 소재·도금·보증 표기.
한정수량 섹션은 숫자 카운터 없이 “소량 제작” 이라는 **브랜드 방침**만 서술합니다 — 실제로 소량일 때만 의미가 있습니다.

---

## 로컬 미리보기

```powershell
python -m http.server 4178 --directory .
```

→ 브라우저에서 http://localhost:4178 접속.

---

## 폰트

- 본문·FAQ — **Pretendard** (Regular 400 / Medium 500)
- 헤드라인·워드마크·CTA·가격 — **SUIT** (Light 300 / Medium 500 / SemiBold 600)
- eyebrow·라벨 — **S-Core Dream** (5)

세 폰트(모두 SIL OFL)는 **페이지에 실제로 쓰는 글자만 서브셋**해 woff2로 base64 임베드되어 있습니다(현재 443자, 약 200KB).
한국어 문구를 바꿔 **새로운 글자가 생기면 다시 서브셋**해야 합니다(안 하면 그 글자가 시스템 폰트로 대체됨).

```powershell
# tools/fonts/ 에 원본 6종이 있는 상태에서:
python tools/subset_fonts.py
```

원본 OTF가 없으면 공식 배포처에서 받아 `tools/fonts/`에 아래 이름으로 넣어주세요:
`SUIT-Light.otf, SUIT-Medium.otf, SUIT-SemiBold.otf, Pretendard-Regular.otf, Pretendard-Medium.otf, SCDream5.otf`
(Pretendard·SUIT: github.com/orioncactus, github.com/sunn-us · S-Core Dream: S-Core 공식 배포)

---

## 배포 (Vercel)

GitHub `growandrun/velloriacopy1` 저장소를 Vercel에 **import(git 연동)** 하면, 이후 `git push` 시 **자동 재배포**됩니다. 프레임워크 프리셋은 **Other(정적)**, 빌드 명령 없음, 출력 디렉터리 루트(`.`).
