import streamlit as st 
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import plotly.express as px

path = 'data/'
st.set_page_config(
    page_title='bi',
)

db = pd.read_excel(f'{path}DB.xlsx', index_col=False)

db.fillna(0, inplace=True)
db['리뷰'] = db['리뷰'].str.replace('\n', ' ')

main_features = ['색감', '핏', '재질', '퀄리티', '제품상태', '가격', '두께']

count_positive = db[main_features].eq(1).sum()[db[main_features].eq(1).sum() > 0]
count_negative = db[main_features].eq(-1).sum()[db[main_features].eq(-1).sum() > 0]

st.title('전체 상품의 긍정과 부정 리뷰의 분포')

# 그래프 생성
fig = go.Figure()

# 긍정의 바 차트 추가
fig.add_trace(go.Bar(
    x=count_positive.index,
    y=count_positive.values,
    name='긍정',
    marker_color='rgb(55, 83, 109)'
))

# 부정의 바 차트 추가
fig.add_trace(go.Bar(
    x=count_negative.index,
    y=count_negative.values,
    name='부정',
    marker_color='rgb(219, 64, 82)'
))

# 그래프 레이아웃 설정
fig.update_layout(
    bargap=0.1,  # 막대 사이의 간격 조정
    plot_bgcolor='rgba(0, 0, 0, 0.7)',  # 그래프 배경색 어둡게 설정
    paper_bgcolor='rgba(0, 0, 0, 0.7)',  # 전체 배경색 어둡게 설정
    font=dict(color='white'),  # 글자 색상을 흰색으로 설정
    width=800,  # 그래프 너비 설정
    height=600  # 그래프 높이 설정
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)

# TOP 8 상품의 부정 리뷰 분포
unique_products = list(db.drop_duplicates(subset=['상품명']).sort_values(by='리뷰수', ascending=False)[:8]['상품명'])

positive_ratio = [0.2, 0.4, 0.6, 0.5, 0.8, 0.7, 0.3, 0.9]
negative_ratio = [0.8, 0.6, 0.4, 0.5, 0.2, 0.3, 0.7, 0.1]  # 상품별 부정 비율

st.title('TOP.8 부정 리뷰의 분포')

product_names = unique_products

# Creating one subplot
fig = make_subplots(rows=1, cols=1, specs=[[{}]], shared_xaxes=True,
                    shared_yaxes=False, vertical_spacing=0.001)

fig.add_trace(go.Bar(x=np.arange(len(product_names)), y=positive_ratio, name='Positive',
                     marker=dict(color='rgba(50, 171, 96, 0.6)'),
                     hoverinfo='text',
                     hovertext=product_names),
)
# 부정 그래프 생성
fig.add_trace(go.Bar(x=np.arange(len(product_names)), y=negative_ratio, name='Negative',
                     marker=dict(color='rgba(219, 64, 82, 0.6)'),
                     hoverinfo='text',
                     hovertext=product_names),
              )

# 그래프 레이아웃 설정
fig.update_layout(
    yaxis_title='비율',
    xaxis=dict(tickvals=np.arange(len(product_names)), ticktext=['' for _ in product_names]),  # x축 눈금 레이블 제거
    barmode='stack',  # 스택으로 쌓음
    plot_bgcolor='rgba(0, 0, 0, 0.7)',  # 그래프 배경색 어둡게 설정
    paper_bgcolor='rgba(0, 0, 0, 0.7)',  # 전체 배경색 어둡게 설정
    font=dict(color='white'),  # 글자 색상을 흰색으로 설정
    width=800,  # 그래프 너비 설정
    height=600
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)
