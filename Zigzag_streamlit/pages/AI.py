import streamlit as st 
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import plotly.express as px
import joblib
from mecab import MeCab
import time

path = 'artifact/'

def stream_data(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.05)
        
@st.cache_data
def get_artifacts(artifacts_path='artifact/', model_name=''):
    try:
        catboost_model = joblib.load(f'{artifacts_path}{model_name}/{model_name}_catboost_model.pkl')
        col = joblib.load(f'{artifacts_path}{model_name}/{model_name}_col.pkl')
        scaler = joblib.load(f'{artifacts_path}{model_name}/{model_name}_scaler.pkl')
        vectorizer = joblib.load(f'{artifacts_path}{model_name}/{model_name}_vectorizer.pkl')
        return catboost_model, col, scaler, vectorizer
    except Exception as e:
        st.error(f"Error loading artifacts for model '{model_name}': {e}")
        return None, None, None, None

color_model, color_col, color_scaler, color_vectorizer = get_artifacts(model_name='color')
outfit_model, outfit_col, outfit_scaler, outfit_vectorizer = get_artifacts(model_name='outfit')
price_model, price_col, price_scaler, price_vectorizer = get_artifacts(model_name='price')
quality_model, quality_col, quality_scaler, quality_vectorizer = get_artifacts(model_name='quality')
status_model, status_col, status_scaler, status_vectorizer = get_artifacts(model_name='status')
texture_model, texture_col, texture_scaler, texture_vectorizer = get_artifacts(model_name='texture')
thick_model, thick_col, thick_scaler, thick_vectorizer = get_artifacts(model_name='thick')

models_info = [
    (color_vectorizer, color_scaler, color_col, color_model),
    (outfit_vectorizer, outfit_scaler, outfit_col, outfit_model),
    (price_vectorizer, price_scaler, price_col, price_model),
    (quality_vectorizer, quality_scaler, quality_col, quality_model),
    (status_vectorizer, status_scaler, status_col, status_model),
    (texture_vectorizer, texture_scaler, texture_col, texture_model),
    (thick_vectorizer, thick_scaler, thick_col, thick_model)
    ]

def tokenizer(data):
    tokenizer = MeCab()
    token_list = []
    pos_filter = ['NNG','MAG','EC','VA','VA+EF','VV+ETM','NNB+JKB','VCP+EC','VCP','MAG+JX','VCN']
    for text in data['tokens']:
        prah = []  
        lst = tokenizer.pos(text)  
        for word, pos in lst:
            if pos in pos_filter:
                prah.append(word)  
        token_list.append(' '.join(prah))  
    
    return token_list


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

path = 'data/'

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
        <span>고민중인가요? 도움이 될만한 리뷰들을 뽑아 드리고, 왜 추천하는지 설명도 해드려요!</span>
    </div>
""", unsafe_allow_html=True)

text_input = st.text_input(label='',placeholder='예시)나는 165, 55정도이고 상품을 볼땐 색감을 중요시 여기는거 같아', value='')

if text_input:
    text_list = [text_input]  
    df_text = pd.DataFrame({'tokens': text_list})  # 데이터프레임으로 변환
    predictions = get_keyword(df_text, models_info)  # 예측 수행
    selected_features = [feature for i, feature in enumerate(main_features) if predictions[i] > 0]
    text = ','.join(selected_features)+'을 중요시 여기는군요! 잠시만 기달려주세여 모든 리뷰들을 분석해서 추천해 드릴게요!'
    st.write_stream(stream_data(text))

#오버핏이 딱 좋고 재질은 음..기모 그리고 색감도 중요한거 같아 키는 171/53 이정도야

previous_product_name = st.session_state.get("previous_product_name")

if selected_product != previous_product_name:
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

    # Display plot in Streamlit app
    st.plotly_chart(fig)
  
    # Update previous_product_name in session state
    st.session_state["previous_product_name"] = selected_product
else:
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

    # Display plot in Streamlit app
    st.plotly_chart(fig)
  
    # Update previous_product_name in session state
    st.session_state["previous_product_name"] = selected_product
    st.plotly_chart(fig)