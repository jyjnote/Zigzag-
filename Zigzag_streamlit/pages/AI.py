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


artifact_path = 'artifact/'
image_path = "image/"
path = 'data/'

def stream_data(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.05)
        
# @st.cache_data
# def get_artifacts(artifacts_path='artifact/', model_name=''):
#     try:
#         catboost_model = joblib.load(f'{artifacts_path}{model_name}/{model_name}_catboost_model.pkl')
#         col = joblib.load(f'{artifacts_path}{model_name}/{model_name}_col.pkl')
#         scaler = joblib.load(f'{artifacts_path}{model_name}/{model_name}_scaler.pkl')
#         vectorizer = joblib.load(f'{artifacts_path}{model_name}/{model_name}_vectorizer.pkl')
#         return catboost_model, col, scaler, vectorizer
#     except Exception as e:
#         st.error(f"Error loading artifacts for model '{model_name}': {e}")
#         return None, None, None, None

# color_model, color_col, color_scaler, color_vectorizer = get_artifacts(model_name='color')
# outfit_model, outfit_col, outfit_scaler, outfit_vectorizer = get_artifacts(model_name='outfit')
# price_model, price_col, price_scaler, price_vectorizer = get_artifacts(model_name='price')
# quality_model, quality_col, quality_scaler, quality_vectorizer = get_artifacts(model_name='quality')
# status_model, status_col, status_scaler, status_vectorizer = get_artifacts(model_name='status')
# texture_model, texture_col, texture_scaler, texture_vectorizer = get_artifacts(model_name='texture')
# thick_model, thick_col, thick_scaler, thick_vectorizer = get_artifacts(model_name='thick')

# models_info = [
#     (color_vectorizer, color_scaler, color_col, color_model),
#     (outfit_vectorizer, outfit_scaler, outfit_col, outfit_model),
#     (price_vectorizer, price_scaler, price_col, price_model),
#     (quality_vectorizer, quality_scaler, quality_col, quality_model),
#     (status_vectorizer, status_scaler, status_col, status_model),
#     (texture_vectorizer, texture_scaler, texture_col, texture_model),
#     (thick_vectorizer, thick_scaler, thick_col, thick_model)
#     ]

# def tokenizer(data):
#     tokenizer = MeCab()
#     token_list = []
#     pos_filter = ['NNG','MAG','EC','VA','VA+EF','VV+ETM','NNB+JKB','VCP+EC','VCP','MAG+JX','VCN']
#     for text in data['tokens']:
#         prah = []  
#         lst = tokenizer.pos(text)  
#         for word, pos in lst:
#             if pos in pos_filter:
#                 prah.append(word)  
#         token_list.append(' '.join(prah))  
    
#     return token_list


def get_predict(data,_scaler, col, model, vectorizer):
    x = vectorizer.transform(data).toarray()
    x = _scaler.transform(x)    
    x = x[:, col]  # Accessing the appropriate index of the tuple
    return model.predict(x)

def get_keyword(data, models_info):
    predictions = []
    for model_info in models_info:
        vectorizer, scaler, col, model = model_info
        predictions.append(get_predict(tokenizer(data), scaler, col, model, vectorizer))
    return predictions


@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path, index_col=False)

db = load_data(f'{path}DB.xlsx')

main_features=['색감','핏','재질','퀄리티','제품상태','가격','두께']
keyword_dict = {0: '색감', 1: '핏', 2: '재질', 3: '퀄리티', 4: '제품상태', 5: '가격', 6: '두께'}

#st.image(f'image\로고.png')

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
        checked_color=st.checkbox('색감')
    with check_outfit:
        checked_outfit=st.checkbox('핏')
    with check_price:
        checked_price=st.checkbox('가격')
    with check_quality:
        checked_quality=st.checkbox('퀄리티')
    with check_status:
        checked_status=st.checkbox('상태')
    with check_texture:
        check_texture=st.checkbox('재질')
    with check_thick:
        checked_thick=st.checkbox('두께')
    get_selected_col=[checked_color,checked_outfit,checked_price,checked_quality,checked_status,check_texture,checked_thick]
    
    
#search_item=st.text_input(label='',placeholder='예시)[1+1수량할인💗/5만장돌파/컬러추가] 단독)살결 인생슬리브리스 - 5color')

get_analsys=False



# if st.button('분석 보기'):
#     if not search_item:
#         st.warning('상품명을 입력해주세요!', icon="⚠️")
#     else:
#         selected_product=search_item
#         get_analsys=True
    
  
# text_input = st.text_input(label='',placeholder='예시)나는 165, 55정도이고 상품을 볼땐 색감을 중요시 여기는거 같아', value='')

# if text_input:
#     text_list = [text_input]  
#     df_text = pd.DataFrame({'tokens': text_list})  # 데이터프레임으로 변환
#     predictions = get_keyword(df_text, models_info)  # 예측 수행
#     selected_features = [feature for i, feature in enumerate(main_features) if predictions[i] > 0]
#     text = ','.join(selected_features)+'을 중요시 여기는군요! 잠시만 기달려주세여 모든 리뷰들을 분석해서 추천해 드릴게요!'
#     st.write_stream(stream_data(text))

#오버핏이 딱 좋고 재질은 음..기모 그리고 색감도 중요한거 같아 키는 171/53 이정도야
item = db[db['상품명'] == selected_product]
item_reviews = len(item)
no_reviews_features = np.array((item[main_features].eq(0).sum() == item_reviews).to_list())

main_features_filtered = np.array(main_features)[~no_reviews_features]

review_counts = item[main_features_filtered]

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
    low_error = random.randint(-5, 0)  # 키에 대한 오차 범위 (-5cm ~ 0cm)
    high_error = random.randint(0, 5)  # 몸무게에 대한 오차 범위 (0kg ~ 5kg)
    
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
    


#if get_analsys:
    # anal_db = db[db['상품명'] == selected_product]
    # selected_col = [main_features[i] for i, pick in enumerate(get_selected_col) if pick]
    # anal_db = anal_db[selected_col]

    # combined_values = anal_db.values.flatten()
    
    # positive_count = np.sum(combined_values == 1)
    # negative_count = np.sum(combined_values == -1)
    # neutral_count = np.sum(combined_values == 0)
    
    # total_count = len(combined_values)
    
    # positive_percentage = (positive_count / total_count) * 100
    # negative_percentage = (negative_count / total_count) * 100
    # neutral_percentage = (neutral_count / total_count) * 100

    # positive_text = f"<span style='color:skyblue'>긍정{positive_percentage:.2f}%</span>"
    # negative_text = f"<span style='color:pink'>부정{negative_percentage:.2f}%</span>"
    # neutral_text = f"<span style='color:yellow'>중립{neutral_percentage:.2f}%</span>"

    # text = f"{','.join(selected_col)}을 중요시 여기는 군요! 저희 데이터에 의하면 {selected_product}의 리뷰 분포는 {positive_text}, {negative_text}, {neutral_text} 입니다!"

    # st.markdown(f"""
    #     <div style='display: flex; align-items: center;'>
    #         <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    #         <i class="fas fa-robot" style='margin-right: 10px;'></i>
    #         <span>{text}</span>
    #     </div>
    # """, unsafe_allow_html=True)
    # #st.write_stream(stream_data(text))

