import streamlit as st 
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from konlpy.tag import Okt
import nltk
import re

# 데이터 로드 함수를 정의합니다.
review_data = pd.read_csv('review_data.csv', index_col=False)

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

@st.cache_data(persist="disk")
def plot_review_trend_for_year(df, year, columns=None):
    # 원하는 년도에 해당하는 데이터 필터링
    df_year = df[df['년'] == year]
    
    # '월'로 그룹핑하기 위해 '월' 컬럼을 인덱스로 설정
    df_year = df_year.set_index('월')  # '월'을 인덱스로 설정

    # 긍정, 부정 개수 세기 준비
    positive_counts = pd.DataFrame()
    negative_counts = pd.DataFrame()

    # 선택한 컬럼이 없으면 모든 컬럼을 대상으로 함
    if columns is None:
        columns = ['색감긍부중', '핏긍부중', '재질긍부중', '퀄리티긍부중', '두께긍부중', '가격.1긍부중', '제품상태긍부중']
    elif isinstance(columns, str):
        columns = [columns]  # 문자열이면 리스트로 변환

    # 각 컬럼별 긍정, 부정 개수 계산
    for column in columns:
        if column in df_year.columns:
            positive_counts[column] = df_year.groupby('월')[column].apply(lambda x: (x == '긍정').sum())
            negative_counts[column] = df_year.groupby('월')[column].apply(lambda x: (x == '부정').sum())

    # 그래프 그리기
    if not positive_counts.empty:
        n_columns = len(positive_counts.columns)
        fig, axs = plt.subplots(n_columns, 1, figsize=(10, 6*n_columns), sharex=True)

        if n_columns == 1:
            axs = [axs]  # axs를 리스트로 만들어 단일 컬럼일 때의 에러 방지

        for i, column in enumerate(positive_counts.columns):
            axs[i].plot(positive_counts.index, positive_counts[column], label='긍정', marker='o', linestyle='-', color='blue')
            axs[i].plot(negative_counts.index, negative_counts[column], label='부정', marker='x', linestyle='--', color='red')
            axs[i].set_title(column)
            axs[i].legend()

        plt.xlabel('월')
        plt.xticks(range(1, 13))  # 1월부터 12월까지 x축에 표시
        plt.tight_layout()
        st.pyplot(plt)
    else:
        print("선택한 컬럼이 데이터에 존재하지 않습니다.")

@st.cache_data(persist="disk")              
def clean_and_preprocess_texts(texts):
    cleaned_texts = []

    for text in texts:
        cleaned_text = re.sub('[^가-힣0-9a-zA-Z]', ' ', text)
        cleaned_text = re.sub('\s+', ' ', cleaned_text)
        cleaned_text = re.sub('(가갹|가걱|가격대)', '가격', cleaned_text)
        cleaned_text = re.sub('(이쁘다|예쁘다)', '예쁘다', cleaned_text)
        cleaned_texts.append(cleaned_text)

    return cleaned_texts   
@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path, index_col=False)

# Streamlit 앱을 정의합니다.
def app():
    st.title('상품의 긍부정 추이를 살펴봅시다')

    st.header('원하는 카테고리와 브랜드를 골라 주세요 ')
    option_cate = st.selectbox(
        '원하는 의류의 카테고리를 골라주세요',
        review_data['중분류'].unique().tolist(),index = None)

    category = review_data[review_data['중분류']==option_cate]
    df_grouped =category.groupby(['월', '리뷰전체긍부정중립']).size().unstack(fill_value=0)

    # 라인 그래프 시각화
    plt.figure(figsize=(10, 6))
    df_grouped.plot(kind='line', marker='o')
    plt.title(f'{option_cate} 카테고리의 월별 긍부정 개수 추이')
    plt.xlabel('월')
    plt.ylabel('개수')
    plt.legend(title='긍부정중립', bbox_to_anchor=(1, 1))
    st.pyplot(plt)
    
    category_review = category
    category_brands_lst = category_review['브랜드'].unique().tolist()

    # 원하는 브랜드 고르도록 지시
    option_brand = st.selectbox(
        '원하는 브랜드를 골라주세요',
        category_brands_lst, index =None)

    selected_brand_review = category_review[category_review['브랜드']==option_brand]

    df_grouped =selected_brand_review.groupby(['월', '리뷰전체긍부정중립']).size().unstack(fill_value=0)
    # 라인 그래프 시각화
    plt.figure(figsize=(10, 6))
    months = [f'{i}월' for i in range(1, 13)]  # 1월부터 12월까지 문자열 생성
    df_grouped.plot(kind='line', marker='o')
    plt.title(f'{option_brand}의 월별 긍부정 개수 추이')
    plt.xlabel('월')
    plt.ylabel('개수')
    plt.legend(title='긍부정중립', bbox_to_anchor=(1, 1))
    plt.xticks(range(1, 13), months)
    st.pyplot(plt)

    option_cate = st.selectbox(
        '확인하고 싶은 긍부정의 요소를 골라주세요',
        ['색감긍부중','핏긍부중', '재질긍부중', '퀄리티긍부중', '두께긍부중', '가격.1긍부중', '제품상태긍부중'])
    
    df = selected_brand_review[['색감긍부중','핏긍부중', '재질긍부중', '퀄리티긍부중', '두께긍부중', '가격.1긍부중', '제품상태긍부중','월','년']]
    
    plot_review_trend_for_year(df, 2023, columns=option_cate)

    review_data_neg_pos = pd.read_csv('review_data_neg_pos.csv', index_col=False)

    st.title('아래는 색감,핏,재질에 대한 긍부정 키워드드를 빈도순으로 시각화한 자료입니다')

    st.header('원하는 카테고리와 브랜드를 골라 주세요 ')
    #데이터 로드


    # 원하는 카테고리 고르도록 지시
    option_cate = st.selectbox(
        '원하는 의류의 카테고리를 골라주세요',
        review_data_neg_pos['중분류'].unique().tolist(),index = None,key='unique_key_for_category_selectbox')

    category = review_data_neg_pos[review_data_neg_pos['중분류']==option_cate]
    
    category_review = category
    category_brands_lst = category_review['브랜드'].unique().tolist()

    # 원하는 브랜드 고르도록 지시
    option_brand = st.selectbox(
        '원하는 브랜드를 골라주세요',
        category_brands_lst, index =None,key='unique_key_for_brand_selectbox')

    brand_review = category_review[category_review['브랜드']==option_brand][['상품명','리뷰']].reset_index().drop(columns = 'index')
    merchan_name_lst = brand_review['상품명'].unique().tolist()

    option_marchan = st.selectbox(
        '원하는 상품을 골라주세요',
        merchan_name_lst, index =None)



    merchan_reviews_dict = {}

    for merchan in merchan_name_lst:
        
        merchan_reviews_series = brand_review[brand_review['상품명'] == merchan]['리뷰']
        merchan_reviews_dict[merchan] =merchan_reviews_series
        
    selected_merchan_review = merchan_reviews_dict[option_marchan]   



    tm_list = clean_and_preprocess_texts(selected_merchan_review)

    okt = Okt()
    words_list =[]
    stop_words = ['셔츠','좋다','너무','그거','보기','가지','입다','하다','같다','있다','으로','자다','이다','사다','오오'
                ,'아니다','이다','이에요','에요','예요','그리고','인데','오다','기다','이나','이라','예쁘다','같아요','않다',
                '후드','따뜻하다','들다','구매','여름','기모','하고','부분','약간','투맨','생각','이렇다','그렇다','스럽다']

    for i in range(len(tm_list)):
        text  = tm_list[i]
        morp = okt.pos(text, stem = True, norm = True)
        for word, tag in morp:
            if ( tag=='Adjective' ) and len(word)>1 and (word not in stop_words):
                words_list.append(word)

    word_freq = nltk.FreqDist(words_list)
    word = word_freq.keys()
    freq = word_freq.values()
    word_count_df = pd.DataFrame([word,freq], index = ['word','freq']).T
    word_count_df.sort_values(by = ['freq'], ascending = False, inplace = True)
    
    top_n = word_count_df.head(20)

    # 시각화
    plt.figure(figsize=(10, 8))
    plt.bar(top_n['word'], top_n['freq'], color='skyblue')
    plt.xlabel('단어')
    plt.ylabel('빈도수')
    plt.title('긍부정 단어 빈도수 상위 20개')
    plt.xticks(rotation=45)
    st.pyplot(plt)
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
