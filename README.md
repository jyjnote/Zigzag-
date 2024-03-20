# 지그재그 쇼핑몰 분석 & BI서비스

📌 데이터 출처: [지그재그](https://zigzag.kr/)

📌 대회 주제 : 🌏 온라인 쇼핑몰 데이터를 활용하여 비즈니스적 가치 창출하기

📌 대회 기간 : 2024.01.30 ~ 2024.03.20

📌 개발스택

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-092E20?style=for-the-badge&logo=Beautiful%20Soup&logoColor=white)![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-0078D4?style=for-the-badge&logo=networkx&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

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

- ZigZag 에 입점하게 된다면 수익에 대한 안정성이 보장되는가?
- 물품 배송은 안정적으로 이루어지는가 ?

<br/>

> 📝 **시장을 먼저 파악해보기 ————————————————————-——————✔️**
> 

🤔 **어떤 상품이 잘 팔릴까 ?**

- **❓ 어떤 물건이 제일 많이 팔릴까 ?**


    - 매출의 비중 크게 차지하는 품목은 어떤 것이 있는가?
        - 상품 품목 구매 순위 리스트 업
    - 브라질 소비 트렌드와 연관이 있는가?
    - 꾸준히 구매되는 상품들은 월 매출이 안정적일까?

🤔 **어디에서 더 잘 팔릴까 ?**

- ❓ **핫한 품목의 주문은 대체로 어디서 일어나는가 ?**
    - 생산 지역과 소비 지역이 서로 다른가 ?
        - 소비자-판매자 간 거리가 배송 기간에 미치는 영향이 있는가?


- ❓ **각 상품에 따라 지역 간 매출액 차이가 발생하는가 ??**
    - 지역 별로 어떤 품목이 가장 큰 판매 비중을 차지하는가 ?

<br/>

> 🚻 **다른 판매자들은 어떻게 수익을 얻고 있는지 파악해보기**  **————————————✔️**
> 

🤔 **어떻게 팔아야 더 잘 팔릴까 ?**

- ❓ **시장규모가 클수록 특히 잘 팔리는 물건이 있을까 ?**

- ❓ **ZigZag의 상, 하위 판매자 두 그룹의 매출액 차이는 얼마나 큰가 ?**


- ❓ **판매자가 안정적인 수익을 얻기 위해서는 여러 종류의 상품을 판매하는 것이 더 효과적인가 ?**
    - 한 셀러가 여러 개의 품목을 판매하고 있는지 ?
    - 연관성이 있는 상품을 함께 팔고 있는지 ?

<br/>



---

## Reference 

[브라질 소비 트렌드[전문가오피니언] 소비자 구성을 통해 본 브라질 소비시장](https://www.emerics.org:446/issueDetail.es?brdctsNo=253385&mid=a10200000000&&search_option=&search_keyword=&search_year=&search_month=&search_tagkeyword=&systemcode=06&search_region=&search_area=1&currentPage=7&pageCnt=10)

[브라질 지역 조사](https://namu.wiki/w/%EB%B8%8C%EB%9D%BC%EC%A7%88)

[브라질 인구 통계 - 주상파울루 대한민국 총영사관](https://overseas.mofa.go.kr/br-saopaulo-ko/brd/m_6167/view.do?seq=1096092&srchFr=&amp;srchTo=&amp;srchWord=&amp;srchTp=&amp;multi_itm_seq=0&amp;itm_seq_1=0&amp;itm_seq_2=0&amp;company_cd=&amp;company_nm=)
