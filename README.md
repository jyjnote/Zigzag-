# 🌸ZigZag🌸 쇼핑몰 분석 & BI서비스

📌 데이터 출처: [ZigZag](https://zigzag.kr/)

📌 대회 주제 : 🌏 온라인 쇼핑몰 데이터를 활용하여 비즈니스적 가치 창출하기

📌 대회 기간 : 2024.01.30 ~ 2024.03.20

📌 개발스택

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-092E20?style=for-the-badge&logo=Beautiful%20Soup&logoColor=white)![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-0078D4?style=for-the-badge&logo=networkx&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

**DEMO**
![KakaoTalk_20240320_142716478](https://github.com/jyjnote/Zigzag-/assets/144209498/43720c67-dc7d-42e2-8c18-e9cdb7ab74ba)
![KakaoTalk_20240320_142720597](https://github.com/jyjnote/Zigzag-/assets/144209498/8ef058e9-dccf-488d-814e-cb2a1e6a2b83)


## member.

| 7️⃣👨 | 7️⃣👨 | 7️⃣👨 | 5️⃣👩 | 5️⃣👩 |
| :---: | :---: | :---: | :---: | :---: |
| [`이도훈`](https://github.com/LEEDOHOON427) | [`정재연`](https://github.com/jyjnote) | [`양태성`](https://github.com/TaeseongYang) | [`박주연`](https://github.com/Parkkjuyeon) | [`임나연`](https://github.com/limnayean) |

### **분석 포인트**

온라인 매장에 입점 하고 싶은 예비 셀러와 바이어를 위해 우리는 지그재그내에 다른 Seller들의 특성과 바이어들 대해 파악한 후 판매 품목을 선정하기 위한 가이드라인 및 구매의사 결정을 도움을 제시하고자 한다. 

`어떤?` `누구에게?` `어떻게?` 라는 3가지의 기준으로 수익성이 높은 상품군을 관리할 수 있도록 적절한 가이드라인을 제공하는 것, 바이어에겐 보다 적절한 구매결정을 제공하는 것으로 목표로 데이터를 분석하였다. 

먼저 소비 시장을 파악하기에 앞서, **ZigZag라는 쇼핑몰의 온라인 판매자로 등록하는 것이 적절한 지**를 파악해보았다.  

---
## 프로젝트 설명 

> ZigZag 온라인 쇼핑몰 입점을 원하는 예비 판매자 (SELLER)와 구매자(buyer) 를 위한 판매 물품 선정 가이드라인 👊

### 🤔타겟 및 상황 설정

📌 **Target :** ZigZag에 뛰어들려는 예비 *`Seller`* & *`buyer`*

<br/>

📝 **프로젝트 문제 상황(troubleshooting)**

```python
-Crawling-
    - 지개재그 해당 사이트의 리뷰의 순위 기준을 정확하게 파악하기 힘들었음.
    - 리뷰에서 몇몇 요소가 있거나 없는 형태임.

    -> 정확하게 크롤링 해올 부분을 정하고 어떤 상황에서도 크롤링을 해올 수 있도록 코드에 분기를 추가해서 해결

-Model-
    - 어떤식으로 리뷰 데이터를 처리할것인지 어려움이 있었음
    - 리뷰 데이터라는 특성 상 해당 피처(target)이 필연적으로 불균형을 이룸(ex: 핏:80% 퀄리티:5% 가격:5%)
    - 각 피처 내에서 또 긍정(1), 부정(-1), 중립(0)이 불균형함 (ex: 핏:80 구성에서 1:70% -1:25% 0:5%)

    -> 다양한 모델 기법을 시도 및 적절한 평가 지표를 설정하여 다음 문제를 해결

-BI-
    - 분석된 데이터를 정확하게 무엇을 어떻게 보여줄지 어려움을 겪음

    -> 팀원 전체 회의를 통해서 의견을 조율함
```


<br/>

---
## CONTENTS
### **❓ ZigZag 쇼핑몰 선택, 괜찮을까 ?**

# 프로젝트 주제 : 리뷰 데이터 기반 서비스 제공 및 상품 분석 

<기획의도>
- 여성 쇼핑몰 중에서 에이블리와 1,2위를 다투는 지그재그의 리뷰 데이터를 통해 20-30 여성의 구매 결정에 도움을 주고 입점 업체에게는 현재 업체 의류의 문제점에 대한 인사이트를 제공

<주요 분석 내용>

1) 소비자 입장

- 해당 카테고리 상품의 리뷰 데이터를 바탕으로 소비자들이 어떤 이유에서 긍 / 부정으로 느끼게 되었는지 긍 / 부정의 비율(시각화)과 구체적인 근거 요약 텍스트 생성 + 각 상품의 긍 / 부정 요인에 대한 키워(상위 3개씩)을 bar 그래프로 시각화 
- 소비자의 신체 사이즈 기입과 구매가 망설여 지는 이유기입을 통해 비슷한 고민이 있는 사람의 리뷰 데이터로부터 구매결정에 도움이 되도록 시각화
- 같은 카테고리 내의 다른 상품과 비교하여 해당 상품의 상대적인 위치를 보여줌. 이는 소비자가 다른 상품과의 차이를 이해하게 해줌

2) 기업 입장

리뷰 분석을 기반으로 소비자들이 어떤 부분에서 만족을 하는지 새로운 리뷰가 들어올 때마다 갱신되는 대시보드 생성 대시 보드의 내용은 다음과 같습니다. 

- 감성 점수 : 긍정적, 부정적 리뷰의 비율을 보여주는 지표. 이는 제품이나 서비스에 대한 전반적인 고객 만족도를 측정하는 데 도움이 됨. 
- 키워드 빈도 및 중요도 : 제품이나 서비스와 관련된 주요 키워드의 빈도와 중요도를 시각화. 예를 들어, '내구성',' 사용 편의성' 등과 긍정적 키워드와 '고장', '불편함' 등과 같은 부정적 키워드를 구분하여 표시 
- 트렌드 분석 : 시간에 따른 리뷰의 전반적인 변화를 추적하여, 특정 시점에서의 긍정적 또는 부정적 리뷰의 증가 추세를 보여줌. 
- 재구매 고객 피드백 요약 : 두 번 이상 구매한 고객에 대해 자주 언급되는 칭찬 사항을 요약하여 제시 
- 카테고리별 비교 : 같은 카테고리 내 다른 제품과의 비교 분석을 제공. 예를 들어, 경쟁 제품과 비교하여 귀사의 제품이 어떤 면에서 우수한지, 어떤 면에서 개선이 필요한지를 시각화.

<기대효과>

1) 소비자 입장에서의 가치 : 구매하는 데 많은 시간을 들이지 않고도 다른 소비자들이 쓴 신뢰 있는 리뷰들을 단시간에 분석해 구매 결정에 도움을 받을 수 있다. 이는 곧 소비 촉진으로 이어져 매출 증대에 기여
 
2) 기업 입장에서의 가치 : 리뷰 분석을 실시간으로 가능하게 하여 즉각적인 피드백이 가능하고 해당 카테고리 상품에 대한 전반적인 트렌드와 고객 만족에 영향을 끼치는 요인을 한눈에 파악할 수 있음

<역할 분담>

- 박주연 : ppt, 발표
- 양태성 : 크롤링, 전체적인 모델링 
- 이도훈 : 홈페이지 구성, 시각화
- 정재연 : 크롤링, 홈페이지 구성, 시각화
- 임나연 : ppt, 발표

---
# 프로젝트 진행 상황 

<리뷰에 따른 키워드별 긍 / 부정 예측 모델링 구현 완료 : 양태성>

1. 첫 번째 모델, 리뷰에 따른 키워드 존재 여부 판별 (키워드는 '색감', '핏', '재질', '퀄리티' ,'제품 상태', '가격', '두께'를 의미)
- **왜 f1_score을 통해 모델의 성능을 평가?**
 - f1_score의 경우에는 기본적으로 pos( = 1)를 잘 맞추는 평가 모델이다. 
 - 우리의 모델 또한 존재하는 키워드를 바탕으로 긍 / 부정 평가 작업이 행해지기 때문에 pos를 잘 맞추는 것이 필요
 - 그렇기 때문에 f1_score를 사용했고 각 키워드가 pos를 잘 맞추는 것을 고려해야 하기 때문에 f1_score값에 mean()을 통해 키워드 별 평균적인 성능을 평가. 

|모델이름|점수|
|------|---|
|BM-K/KoDiffCSE-RoBERTa|73|
|kykim/bert-kor-base|76|
|team-lucid/deberta-v3-base-korean|72|
|smilegate-ai/kor_unsmile|74|
|BM-K/KoSimCSE-roberta|75|

2. 두 번째 모델, 각 키워드별 긍/ 부정 예측 모델링 구현 완료 : 양태성>
 - **왜 f1_macro를 통해 모델의 성능을 평가?**
 - pos, neg의 비율이 불균형한 상태
 - 이 모델의 pos와 neg 모두 잘 맞추는 것이 중요! 그러므로 pos 잘 맞출 확률, neg 잘 맞출 확률을 모두 고려
 - 사전학습 모델은 키워드별로 공통적으로 **'kykim/bert-kor-base'**를 사용

|키워드|점수|
|------|---|
|색감|88|
|핏|91|
|재질|93|
|퀄리티|87|
|제품상태|94|
|가격|92|
|두께|83|

<대시보드를 통한 시각화 거의 구현 완료 : 정재연>

![대시보드_1](https://github.com/TaeseongYang/Zigzag_project/assets/156265617/21ecabef-446a-40c7-99a3-c56921d46d36)

![제목_2](https://github.com/TaeseongYang/Zigzag_project/assets/156265617/9f2b82dc-7bc9-4862-a6da-5607a2786078)



---

## Reference 

 아시아 경제 / MZ세대 의류 구매 시 온라인 쇼핑몰 먼저 찾는다
 한국소비자원
