---
title: Velloria Landing Image Guide (IMG-01 ~ IMG-09)
type_artifact: image-prompt-fallback
mode: business-campaign
subject: 9 product & lifestyle images for the Velloria daily-bracelet landing page (velloriacopy1)
source_brief: tools/index.template.html (labelled IMG-01~IMG-09 dashed slots)
brand_identity:
  logo_path: none
  palette: ["#FFFFFF", "#F5F4F2", "#1A1A1A", "#6E6E6E", "#141414"]
  typography: SUIT / Pretendard / S-Core Dream
  style_adjectives: [quiet-luxury, monochrome, understated, editorial, daily]
format: mixed (banner-hero / social-vertical / square)
aspect_ratio: per-image (16:9, 3:4, 4:3)
gen_mode: fallback-prompt
model: manual
created: 2026-06-15
last_updated: 2026-06-15
---

# Velloria — 랜딩 이미지 제작 가이드 (IMG-01 ~ IMG-09)

제품: **실버 큐빅 지르코니아(CZ) 데일리 팔찌** · 브랜드 톤: **quiet luxury, 화이트·블랙 모노크롬**.

## 0. 공통 원칙 (전부 적용)

1. **색은 흑백/뉴트럴로.** 페이지가 순백·먹색 모노톤이라, 사진도 **흑백(그레이스케일)에 가깝거나 채도를 크게 낮춘 뉴트럴**(화이트·아이보리 `#F5F4F2`·웜그레이·차콜·블랙 `#141414`)로 통일. **골드/유색 보석/컬러 의상 금지.** 실버 팔찌는 무채색이라 흑백과 잘 맞습니다.
2. **제품컷·매크로·마지막 클로즈업(IMG-01, 03, 09)은 "실제 제품"으로 촬영 권장.** AI 생성은 원석 개수·연결 구조를 지어내 **허위 표현**이 될 수 있습니다. (브랜드 규칙: 실제와 다른 원석/구조 묘사 금지)
3. **라이프스타일컷(IMG-02, 04~07, 08)도 실제 팔찌를 손목/소품에 올려 촬영**하는 것이 가장 안전. AI는 배경/무드 레퍼런스 용도로만.
4. **과한 반짝임 금지.** 빛 받을 때만 은은하게. 데일리 주얼리 인상 유지.
5. **여백 많이, 미니멀.** 배경 단순하게. 텍스트/로고/워터마크 넣지 않기(웹에서 얹음).
6. **손 모델**: 네일은 누드/투명·짧게, 손 깨끗하게. 시계·다른 반지로 시선 분산 금지(레이어드 컷 제외).
7. **내보내기**: WebP, 2x 해상도, sRGB. 슬롯 비율에 맞춰 크롭.

### 파일 목록 요약

| 슬롯 | 위치 | 비율 | 권장 크기(2x) | 제작 방식 |
|---|---|---|---|---|
| IMG-01 | 히어로 아래 제품컷 | 16:9 | 2000×1125 | **실제 촬영** |
| IMG-02 | ③ 결과 — 데일리 착용 | 3:4 | 1200×1600 | 실제 촬영 |
| IMG-03 | ④ 제품가치 — 매크로 | 4:3 | 1600×1200 | **실제 촬영(필수 권장)** |
| IMG-04 | ⑤ 스타일링 — Knit | 3:4 | 1200×1600 | 실제 촬영 |
| IMG-05 | ⑤ 스타일링 — Shirt | 3:4 | 1200×1600 | 실제 촬영 |
| IMG-06 | ⑤ 스타일링 — Date | 3:4 | 1200×1600 | 실제 촬영 |
| IMG-07 | ⑤ 스타일링 — Denim | 3:4 | 1200×1600 | 실제 촬영 |
| IMG-08 | ⑩ 한정수량 — 패키지 | 4:3 | 1600×1200 | 실제 촬영 |
| IMG-09 | ⑪ 마지막 클로즈업 | 16:9 | 1400×788 | **실제 촬영** |

> **공통 프롬프트 머리말(모든 AI 프롬프트 앞에 붙이세요):**
> `Editorial photography for "Velloria", a quiet-luxury daily jewelry brand. Strict monochrome / black-and-white-leaning palette: pure white, ivory #F5F4F2, soft warm grey, charcoal, near-black #141414. A delicate thin silver (white-metal / rhodium) tennis-style bracelet set with small clear cubic-zirconia stones — understated, NOT flashy, true to a real product. Soft diffused light, gentle highlights, fine film grain, minimal high-end aesthetic, lots of negative space, no gold tone, no color.`
>
> **공통 네거티브:** `gold tone, colored/rainbow gemstones, oversized chunky jewelry, gaudy sparkle, plastic look, busy/cluttered background, text, watermark, logo, distorted hand, extra fingers, fake unrealistic diamond clusters`
>
> 플랫폼별: **MidJourney** 끝에 `--ar 16:9`(또는 3:4 / 4:3) `--style raw --q 2` · **DALL·E 3 / Imagen / Firefly**는 위 문장 그대로 + "vertical 3:4"처럼 비율을 문장에 명시.

---

## IMG-01 — 히어로 제품컷 (16:9) · 실제 촬영

**한 줄:** 검정~차콜(또는 순백) 배경 위, 실제 Velloria 팔찌 하나가 자연스러운 곡선으로 놓인 고급 제품컷. 첫 화면이라 **전체 형태가 한눈에**.

- **구도:** 팔찌 단독, 화면 중앙. 부드러운 S-곡선으로 살짝 휘어 놓기. 위아래 여백 충분히(16:9 가로 프레임).
- **라이팅:** 소프트박스 키라이트 1개 + 반사판. 빛이 스톤을 스치며 작은 글린트가 점점이. 하이라이트 날아가지 않게, 그라데이션 falloff.
- **배경:** 무광 차콜→블랙 그라데이션 또는 클린 화이트(seamless).
- **정직성:** 실제 제품 그대로(원석 개수·구조 동일). 과장 보정 금지.
- **AI 프롬프트:** `[공통 머리말] A single bracelet laid in a soft natural curve, floating on a seamless charcoal-to-near-black (#141414) background. One soft directional studio light grazes the piece so each tiny stone catches a faint glint; smooth gradient falloff, subtle specular highlights. Centered, generous negative space, realistic macro product photography, 16:9 horizontal. [공통 네거티브] --ar 16:9 --style raw`

## IMG-02 — 데일리 착용 손목컷 (3:4) · 실제 촬영

**한 줄:** 밝은 자연광 카페/실내, 테이블 위에 팔찌 착용한 여성의 손목. 커피잔·다이어리·유리컵 중 하나를 자연스럽게.

- **구도:** 얼굴은 프레임 밖(또는 턱 아래). 손목+팔찌에 집중. 세로 3:4.
- **라이팅:** 큰 창의 부드러운 주광, 에어리하고 그림자 옅게.
- **소품/의상:** 흰/그레이 테이블, 오트밀·그레이 니트나 셔츠. **컬러 의상 금지**(뉴트럴).
- **AI 프롬프트:** `[공통 머리말] Close-up of a woman's wrist resting on a pale stone or white table in a bright minimal cafe, soft window daylight, wearing the delicate silver CZ bracelet; she loosely holds a white ceramic coffee cup. Face out of frame, shallow depth of field, desaturated neutral monochrome, airy editorial mood. Vertical 3:4. [공통 네거티브] --ar 3:4 --style raw`

## IMG-03 — 매크로 디테일 (4:3) · 실제 촬영(필수 권장)

**한 줄:** 팔찌 일부를 크게 확대 — **원석 컷팅면·금속 이음새·연결(잠금) 구조가 선명하게**. "실물이 허술하지 않다"는 신뢰용.

- **구도:** 익스트림 클로즈업, 체인 링크와 클래스프가 보이도록. 4:3.
- **라이팅:** 매크로 라이팅, 금속 반사 컨트롤(검은/흰 반사판), 스톤 패싯 또렷하게.
- **배경:** **블랙 벨벳 / 화이트 벨벳 / 그레이 대리석**(웜 아이보리는 모노톤에서 제외).
- **정직성:** ⚠️ **반드시 실제 제품**. AI는 스톤 수·구조를 지어내므로 사용 금지. 실측 그대로.
- **AI(무드 참고용만):** `[공통 머리말] Extreme macro of the silver CZ bracelet showing faceted stones, metal links and the clasp, on black velvet, crisp reflections. 4:3. [공통 네거티브] --ar 4:3` ← *게시용 아님, 실제 컷으로 교체*

## IMG-04 — Soft Knit Look (3:4) · 실제 촬영

**한 줄:** 오트밀/그레이 니트 소매 사이로 팔찌가 살짝 보이는 손목 클로즈업.

- **무드:** 따뜻하지만 채도 낮춘 뉴트럴, 부드럽고 깨끗. 베이지-그레이 톤.
- **AI 프롬프트:** `[공통 머리말] A wrist peeking from an oatmeal-grey chunky knit sweater sleeve, the silver CZ bracelet just visible, soft warm-but-desaturated daylight, cozy minimal mood, close-up, vertical 3:4. [공통 네거티브] --ar 3:4 --style raw`

## IMG-05 — Clean Shirt Look (3:4) · 실제 촬영

**한 줄:** 흰 셔츠 소매를 살짝 걷은 손목에 팔찌. 책상·다이어리·노트북 있는 깔끔한 배경(출근/공부 무드).

- **AI 프롬프트:** `[공통 머리말] A wrist with the silver CZ bracelet, white shirt sleeve lightly rolled, resting near a tidy desk with a notebook and laptop, clean bright neutral office mood, vertical 3:4. [공통 네거티브] --ar 3:4 --style raw`

## IMG-06 — Elegant Date Look (3:4) · 실제 촬영

**한 줄:** 검은 블라우스/원피스, 따뜻한 조명 아래 저녁 무드. 팔찌가 은은하게 빛나는 장면.

- **무드:** 드라마틱한 블랙 + 부드러운 하이라이트. 채도는 낮게(거의 흑백), 특별한 날 느낌.
- **AI 프롬프트:** `[공통 머리말] A wrist with the silver CZ bracelet against a black blouse, soft warm low key evening light, the bracelet glowing subtly, elegant intimate date-night mood, near black-and-white, vertical 3:4. [공통 네거티브] --ar 3:4 --style raw`

## IMG-07 — Casual Denim Look (3:4) · 실제 촬영

**한 줄:** 데님룩 + 팔찌 포인트, 가볍지만 세련된 캐주얼.

- **⚠️ 모노톤 주의:** 데님은 파랑이라 페이지 톤과 충돌. **흑백 변환** 또는 **그레이/블랙 워시 데님**으로 촬영해 무채색 유지.
- **AI 프롬프트:** `[공통 머리말] A wrist with the silver CZ bracelet over grey/black-washed denim, relaxed casual styling, converted to black-and-white, soft daylight, vertical 3:4. [공통 네거티브] blue color cast, [공통 네거티브] --ar 3:4 --style raw`

## IMG-08 — 소량 패키지 (4:3) · 실제 촬영

**한 줄:** 작은 주얼리 박스/파우치 3~5개를 정갈하게 정렬, 옆에 팔찌 하나 살짝. "소량 제작" 느낌.

- **배경/소품:** 화이트·그레이·블랙 중 브랜드 톤으로 통일. 깔끔, 미니멀.
- **AI 프롬프트:** `[공통 머리말] Three to five small minimal jewelry boxes/pouches neatly arranged on a white or grey surface, one silver CZ bracelet partly visible beside them, top-down or 3/4 angle, "small batch" curated feel, 4:3. [공통 네거티브] --ar 4:3 --style raw`

## IMG-09 — 마지막 클로즈업 (16:9, 검은 배경) · 실제 촬영

**한 줄:** 검은 배경 위 팔찌가 은은하게 빛나는 클로즈업. 원석·금속 광택 선명. 히어로보다 **조금 더 가까이** — "갖고 싶다"는 감정.

- **배경:** 블랙(웹의 어두운 섹션에 자연스럽게 녹아듦).
- **라이팅:** 한 줄기 부드러운 빛, 금속 글로스와 스톤 광택 또렷.
- **AI 프롬프트:** `[공통 머리말] Intimate close-up of the silver CZ bracelet glowing softly on a pure black background, one soft beam of light, crisp metal gloss and gentle stone sparkle, slightly closer than the hero shot, desire-evoking, 16:9. [공통 네거티브] --ar 16:9 --style raw`

---

## 교체 방법 (웹 적용)

각 슬롯은 현재 점선 자리표시자입니다. 촬영본을 준비하면 해당 `<div class="slot ...">...</div>` 를 아래처럼 `<img>`로 바꾸면 됩니다(비율 클래스는 유지 권장):

```html
<img class="slot wide" src="assets/img-01-hero.webp" alt="Velloria 실버 CZ 데일리 팔찌 제품컷" loading="lazy">
```

또는 `.slot`의 `background-image`로 채워도 됩니다. 이미지 저장 위치 예: `assets/` 폴더(신규). 교체 후 `index.html`만 갱신하면 되고, 폰트 재서브셋은 불필요합니다.
