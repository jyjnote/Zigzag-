import streamlit as st 
import pandas as pd
import numpy as np
import plotly.graph_objs as go

# 데이터 로드 함수를 정의합니다.
@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path, index_col=False)

# Streamlit 앱을 정의합니다.
def app():
    # 데이터를 로드합니다.
    db = load_data('review_46086.xlsx')

    # 그래프를 그릴 중분류 선택 상자를 만듭니다.
    category = db['중분류'].unique().tolist()
    selected_category = st.selectbox('**중분류 선택**', category)

    # 선택된 중분류에 해당하는 상위 20개의 제품을 찾습니다.
    top_products = db[db['중분류'] == selected_category]['상품명'].value_counts().nlargest(20).index.tolist()

    # 중분류 및 선택된 상위 20개 제품에 해당하는 데이터를 추출합니다.
    selected_data = db[(db['중분류'] == selected_category) & (db['상품명'].isin(top_products))]

    # 각 7가지 특성의 긍정과 부정 비율을 계산합니다.
    features = ['색감', '핏', '재질', '퀄리티', '제품상태', '가격', '두께']
    positive_ratios = []
    negative_ratios = []

    for feature in features:
        feature_data = selected_data.groupby('상품명')[feature].mean()
        total_reviews = len(selected_data[selected_data[feature] != 0])
        
        positive_count = selected_data[selected_data[feature] == 1].groupby('상품명')[feature].count()
        negative_count = selected_data[selected_data[feature] == -1].groupby('상품명')[feature].count()

        positive_ratio = (positive_count / total_reviews).reindex(top_products, fill_value=0)
        negative_ratio = (negative_count / total_reviews).reindex(top_products, fill_value=0)

        positive_ratios.append(positive_ratio)
        negative_ratios.append(negative_ratio)

    # 스택 바 그래프를 그리기 위한 데이터를 생성합니다.
    layout = go.Layout(
        barmode='stack',
        xaxis=dict(title='특성'),
        yaxis=dict(title='비율')
    )

    # 사용자가 긍정 또는 부정을 선택할 수 있는 체크박스를 추가합니다.
    show_positive = st.checkbox('긍정 보기', value=True)
    show_negative = st.checkbox('부정 보기', value=True)

    # 긍정과 부정 비율을 나타내는 스택 바 그래프를 생성합니다.
    traces = []
    colors = ['green', 'red']
    if show_positive:
        for i, feature_ratio in enumerate(positive_ratios):
            trace = go.Bar(
                x=features,
                y=feature_ratio,
                name=f'{features[i]} 긍정',
                marker=dict(color='green'),
                visible=True
            )
            traces.append(trace)
    if show_negative:
        for i, feature_ratio in enumerate(negative_ratios):
            trace = go.Bar(
                x=features,
                y=feature_ratio,
                name=f'{features[i]} 부정',
                marker=dict(color='red'),
                visible=True
            )
            traces.append(trace)

    fig = go.Figure(data=traces, layout=layout)

    # 그래프를 표시합니다.
    st.write('### 각 7가지 특성에 대한 긍정과 부정 비율')
    st.plotly_chart(fig)

    # 상위 20개 제품의 이름을 칼럼으로 나열합니다.
    col1, col2 = st.columns(2)
    with col1:
        st.write('**상위 20개 제품 리스트 (1-10)**:')
        for i, product in enumerate(top_products[:10], start=1):
            st.write(f'{i}. {product}')
    with col2:
        st.write('**상위 20개 제품 리스트 (11-20)**:')
        for i, product in enumerate(top_products[10:], start=11):
            st.write(f'{i}. {product}')

# Streamlit 애플리케이션을 실행합니다.
if __name__ == '__main__':
    app()
