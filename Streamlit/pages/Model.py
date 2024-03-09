import streamlit as st 
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import plotly.express as px
import joblib
from mecab import MeCab
import time
import random

import google.generativeai as genai

genai.configure(api_key='AIzaSyBw71Pp8yMi6mSRYCGWxGRxZCrXtUqGz60')
model = genai.GenerativeModel('models/gemini-pro')


artifact_path = 'artifact/'
image_path = "image/"
path = 'data/'

def stream_data(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.05)
        

@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path, index_col=False)

db = load_data(f'{path}DB.xlsx')

main_features=['색감','핏','재질','퀄리티','제품상태','가격','두께']
keyword_dict = {0: '색감', 1: '핏', 2: '재질', 3: '퀄리티', 4: '제품상태', 5: '가격', 6: '두께'}


category = db['중분류'].unique().tolist()
selected_category = st.selectbox('**중분류**', category)

brands_in_category = db[db['중분류'] == str(selected_category)]['브랜드'].unique().tolist()
selected_brand = st.selectbox('**브랜드**', brands_in_category)

products_in_category_and_brand = db[(db['중분류'] == str(selected_category)) & (db['브랜드'] == str(selected_brand))]['상품명'].unique().tolist()
selected_product = st.selectbox('**상품명**', products_in_category_and_brand)

height = st.slider("키를 입력하세요 (단위: cm)", min_value=140, max_value=190, value=165)
weight = st.slider("몸무게를 입력하세요 (단위: kg)", min_value=30, max_value=100, value=55)

st.markdown("""
    <div style='display: flex; align-items: center;'>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
        <i class="fas fa-robot" style='margin-right: 10px;'></i>
        <span>해당 옷 구매시 중점적으로 보는 항목을 체크해주세요!(**중복가능**)</span>
    </div>
""", unsafe_allow_html=True)



with st.container():
    check_color,check_outfit,check_price,check_quality,check_status,check_texture,check_thick = st.columns(len(main_features))
    with check_color:
        checked_color=st.checkbox('색감' ,value=True)
    with check_outfit:
        checked_outfit=st.checkbox('핏',value=True)
    with check_price:
        checked_price=st.checkbox('가격',value=True)
    with check_quality:
        checked_quality=st.checkbox('퀄리티',value=True)
    with check_status:
        checked_status=st.checkbox('상태',value=True)
    with check_texture:
        check_texture=st.checkbox('재질',value=True)
    with check_thick:
        checked_thick=st.checkbox('두께',value=True)
    get_selected_col=[checked_color,checked_outfit,checked_price,checked_quality,checked_status,check_texture,checked_thick]
    



#search_item=st.text_input(label='',placeholder='예시)[1+1수량할인💗/5만장돌파/컬러추가] 단독)살결 인생슬리브리스 - 5color')

get_analsys=False

item = db[db['상품명'] == selected_product]
item_reviews = len(item)
no_reviews_features = np.array((item[main_features].eq(0).sum() == item_reviews).to_list())

main_features_filtered = np.array(main_features)[~no_reviews_features]

#review_counts = item[main_features_filtered]
selected_col = [main_features[i] for i, pick in enumerate(get_selected_col) if pick]
review_counts = item[selected_col]

sentiment_counts = review_counts.apply(lambda x: pd.Series(x.value_counts()), axis=0).fillna(0)

fig = make_subplots(rows=1, cols=len(main_features_filtered), specs=[[{'type': 'domain'}] * len(main_features_filtered)],
                        subplot_titles=review_counts.columns)

colors = ['rgb(255, 99, 71)', 'rgb(255, 255, 100)', 'rgb(135, 206, 250)']  # 파란색, 빨간색, 노란색

for i, col in enumerate(sentiment_counts.columns, start=1):
    fig.add_trace(go.Pie(labels=['부정','중립','긍정'], values=sentiment_counts[col].values, name=col,
                             marker=dict(colors=colors)), 1, i)

fig.update_traces(hole=.4, hoverinfo="label+percent+name")

fig.update_layout(
        title_text=selected_product + ' 리뷰 트랜드',
    )
fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=True)

st.plotly_chart(fig)


prompt = st.chat_input('예시)[1+1수량할인💗/5만장돌파/컬러추가] 단독)살결 인생슬리브리스 - 5color')
if prompt:
    selected_product=prompt


if prompt:
    # 랜덤한 오차 생성
    low_error = random.randint(-2, 0)  # 키에 대한 오차 범위 (-5cm ~ 0cm)
    high_error = random.randint(0, 2)  # 몸무게에 대한 오차 범위 (0kg ~ 5kg)
    
    # 오차를 키와 몸무게에 적용
    min_height = height + low_error
    max_height = height + high_error
    min_weight = weight + low_error
    max_weight = weight + high_error
    
    anal_db = db[(db['상품명'] == selected_product) &
                 (min_height <= db['키']) & (db['키'] <= max_height) &
                 (min_weight <= db['몸무게']) & (db['몸무게'] <= max_weight)]
    
    selected_col = [main_features[i] for i, pick in enumerate(get_selected_col) if pick]
    anal_db = anal_db[selected_col].fillna(0)  # NaN 값을 0으로 처리

    combined_values = anal_db.values.flatten()
    
    positive_count = np.sum(combined_values == 1)
    negative_count = np.sum(combined_values == -1)
    neutral_count = np.sum(combined_values == 0)
    
    total_count = len(combined_values)
    
    positive_percentage = (positive_count / total_count) * 100 if total_count != 0 else 0
    negative_percentage = (negative_count / total_count) * 100 if total_count != 0 else 0
    neutral_percentage = (neutral_count / total_count) * 100 if total_count != 0 else 0
    
    # 긍정, 부정, 중립에 대한 백분율에 따라 색상 지정
    positive_color = "skyblue" 
    negative_color = "pink" 
    neutral_color = "yellow" 

    text=f"{','.join(selected_col)}을 중요시 여기는 군요! 고객님의 신체정보 {height}/{weight}를 기준으로 저희 데이터에 의하면 " \
         f"<span style='color:{positive_color}'>긍정 {positive_percentage:.2f}%</span>, " \
         f"<span style='color:{negative_color}'>부정 {negative_percentage:.2f}%</span>, " \
         f"<span style='color:{neutral_color}'>중립 {neutral_percentage:.2f}%</span> 입니다!"
    
    st.markdown(f"""
        <div style='display: flex; align-items: center;'>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
            <i class="fas fa-robot" style='margin-right: 10px;'></i>
            <span>{text}</span>
        </div>
    """, unsafe_allow_html=True)
    with st.spinner('데이터 뽑는 중 띠리띠리..'):
        result = model.generate_content(f'{text} 분석 및 요약해서 이게 구매할만 할까?')
        st.write(result.text)
    