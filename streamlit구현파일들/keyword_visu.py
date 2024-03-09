import streamlit as st
import pandas as pd
import numpy as np
import re
from konlpy.tag import Okt,Komoran, Kkma
import nltk
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import networkx as nx
import re
import random
from io import BytesIO
from PIL import Image 
    

def get_node_size(node_values):
    nsize = np.array([v for v in node_values])  
    nsize = 10000 * (nsize - min(nsize)) / (max(nsize) - min(nsize))
    
    return nsize

@st.cache_data(persist="disk")  
def ego_network(g_edge,keyword):
    fig, ax = plt.subplots(figsize=(18, 13))
    g_ego  = nx.ego_graph(g_edge, keyword)
    ax.set_title('ego_network Graph', fontsize =16)
    dc1 = nx.degree_centrality(g_ego).values()
    nx.draw_networkx(g_ego,
                    pos = nx.kamada_kawai_layout(g_ego),
                    font_family = 'Malgun Gothic',
                    font_color = 'black',
                    with_labels = True,
                    font_size =10,
                    cmap = plt.cm.RdPu,
                    font_weight='bold',
                    edge_color='lightgray',
                    node_size = get_node_size(dc1),
                    node_color = list(dc1),
                    alpha = 0.7,
                    ax =ax)
    return st.pyplot(fig)
    
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

@st.cache_data(persist="disk")
def ttm_df(num,tm_list):
    cv1 =CountVectorizer(ngram_range=(1,num),
                        tokenizer= okt_token)
    dtm_counts1 = cv1.fit_transform(tm_list)
    # dtm_df1 = pd.DataFrame(dtm_counts1.todense().tolist(),
    #                         columns =cv1.get_feature_names_out())
    ttm_counts1 = (dtm_counts1.T * dtm_counts1)
    ttm_counts1.setdiag(0)
    ttm_df1 = pd.DataFrame(ttm_counts1.todense().tolist(),
                          columns = cv1.get_feature_names_out(),
                          index = cv1.get_feature_names_out())
    return ttm_df1



@st.cache_data(persist="disk")
def okt_token(text):
    okt = Okt()
    words_list =[]
    stop_words = ['좋다','너무','그거','보기','가지','입다','하다','같다','있다','으로','자다','이다','사다'
              ,'아니다','이다','이에요','에요','예요','그리고','인데','오다','기다','이나','이라','예쁘다','같아요',
            '후드','따뜻하다','들다','구매','여름','기모','사려','마음','지는','투맨','이고','코랄','에서','이랑',\
                  '여서','처럼','셔츠','하고','이즈','버핏']
    morp = okt.pos(text,stem = True, norm = True)
    
    for word, tag in morp:
        if (tag =='Noun' or tag =='Adjective'  ) and len(word)>1 and (word not in stop_words):
            words_list.append(word)
            
    return words_list

review_data = pd.read_excel('review_46086.xlsx',header =0)

def app():
    st.title('상품의 대략적인 평가를 키워드로 살펴봅시다')

    st.header('원하는 카테고리와 브랜드를 골라 주세요 ')
    #데이터 로드


    # 원하는 카테고리 고르도록 지시
    option_cate = st.selectbox(
        '원하는 의류의 카테고리를 골라주세요',
        review_data['중분류'].unique().tolist(),index = None)

    category = review_data[review_data['중분류']==option_cate]
    category_review = category[['중분류','브랜드','상품명','리뷰']].reset_index().drop(columns = 'index')
    category_brands_lst = category_review['브랜드'].unique().tolist()

    # 원하는 브랜드 고르도록 지시
    option_brand = st.selectbox(
        '원하는 브랜드를 골라주세요',
        category_brands_lst, index =None)

    brand_review = category_review[category_review['브랜드']==option_brand][['상품명','리뷰']].reset_index().drop(columns = 'index')
    merchan_name_lst = brand_review['상품명'].unique().tolist()

    option_marchan = st.selectbox(
        '원하는 상품을 골라주세요',
        merchan_name_lst, index =None)

    merchan_review = category_review[category_review['상품명'] == option_marchan]['리뷰']

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
                '후드','따뜻하다','들다','구매','여름','기모','하고','부분','약간','투맨','생각']

    for i in range(len(tm_list)):
        text  = tm_list[i]
        morp = okt.pos(text, stem = True, norm = True)
        for word, tag in morp:
            if (tag =='Noun' or tag=='Adjective' ) and len(word)>1 and (word not in stop_words):
                words_list.append(word)

    @st.cache_data(persist="disk")
    def word_cloud(words_list):
        plt.rcParams['font.family'] ='Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] =False
        from PIL import Image            
        icon =  np.array(Image.open('alice_mask.png'))   # 마스크가 될 이미지 불러오기 
        word_counts = Counter(words_list)
        word_counts = word_counts.most_common(70)
        pink_color_func = lambda *args, **kwargs: "rgb(238,130,238)"
        WC = WordCloud(font_path='C:\Windows\Fonts\HMKMRHD.ttf',
                    max_font_size =100,mask= icon, background_color='black', stopwords = stop_words,collocations=False, color_func=pink_color_func)
        cloud =WC.generate_from_frequencies(dict(word_counts))
        fig, ax = plt.subplots(figsize=(16, 18))

        ax.imshow(cloud)
        plt.axis('off')  # 축을 표시하지 않음
        ax.set_frame_on(False)
        buf = BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
        buf.seek(0)

        # Streamlit으로 워드 클라우드 이미지 표시
        st.image(buf)

    word_cloud(words_list)

    
    words_list = []
    stop_words = ['셔츠','좋다','너무','그거','보기','가지','입다','하다','같다','있다','으로','자다','이다','사다','오오'
                ,'아니다','이다','이에요','에요','예요','그리고','인데','오다','기다','이나','이라','예쁘다','같아요','않다',
                '후드','따뜻하다','들다','구매','여름','기모','하고','부분','약간','투맨','분도']

# tm_list는 분석할 텍스트의 리스트입니다.
    for text in tm_list:
        morp = okt.pos(text, stem=True, norm=True)
        # 형태소 분석 결과를 저장할 임시 리스트
        filtered_morp = [word for word, tag in morp if tag in ['Noun', 'Adjective', 'Josa'] and len(word) > 1 and word not in stop_words]
        
        # 3-gram 생성
        for i in range(len(filtered_morp) - 2):
            trigram = ' '.join(filtered_morp[i:i+3])
            words_list.append(trigram)

    @st.cache_data(persist="disk")        
    def word_cloud1(words_list):
        words_count = Counter(words_list)
        word_counts = words_count.most_common(20)
        icon =  np.array(Image.open('alice_mask.png'))
        pink_color_func = lambda *args, **kwargs: "rgb(238,130,238)"
        WC1 = WordCloud(font_path='C:\Windows\Fonts\HMKMRHD.ttf',
                    max_font_size =100,mask= icon, background_color='black', stopwords = stop_words,collocations=False, color_func=pink_color_func)
        cloud1 =WC1.generate_from_frequencies(dict(word_counts))
        fig, ax = plt.subplots(figsize=(13, 14))

        ax.imshow(cloud1)
        plt.axis('off')  # 축을 표시하지 않음
        ax.set_frame_on(False)
        buf1 = BytesIO()
        plt.savefig(buf1, format='png', bbox_inches='tight', pad_inches=0)
        buf1.seek(0)

        # Streamlit으로 워드 클라우드 이미지 표시
        st.image(buf1)

    word_cloud1(words_list)
    #------------------------------------------------------------#

    st.title('키워드 간의 네트워크 관계로 보기')

    # 버블 형태로 키워드 자세히 살펴보기
    ttm_df1 = ttm_df(int(st.number_input('버전1로 보시려면 "1"을, 버전2로 보시려면\
    "2"를 누른 후 엔터를 눌러주세요',value=None)),tm_list)


    is_continue = True
    edge_weight = 2

    while is_continue:
        g = nx.from_pandas_adjacency(ttm_df1)
        g_edge = nx.Graph()
        g_edge.add_nodes_from(g.nodes(data=True))
        
        edges = filter(lambda e: e[2]['weight'] >= edge_weight, g.edges(data=True))
        g_edge.add_edges_from(edges)

        for n in g.nodes():
            if len(list(nx.all_neighbors(g_edge, n))) == 0:
                g_edge.remove_node(n)
                
        keyword_count = g_edge.number_of_nodes()
        
        if 20 <= keyword_count <= 40:
            dc = nx.degree_centrality(g_edge).values()
            is_continue = False
        else:
            # 자동으로 edge_weight 값을 조절
            edge_weight += -1 if keyword_count < 20 else 3
        
    st.title("Network Graph Visualization")

    fig, ax = plt.subplots(figsize=(15, 11))
    ax.set_title('Network Graph', fontsize=16)
    pos = nx.kamada_kawai_layout(g_edge)
    nx.draw_networkx(g_edge, pos,  
                    font_family = 'Malgun Gothic',
                    font_color = 'black',
                    with_labels = True,
                    font_size =13,
                    cmap = plt.cm.RdPu,
                    font_weight='bold',
                    edge_color='lightgray',
                    node_size = get_node_size(dc) ,
                    node_color = list(dc),
                    alpha = 0.9,
                    ax =ax)

    st.pyplot(fig)

    # keyword = st.text_input('상단의 키워드 중 더 자세히 보고 싶은 키워드를 검색해보세요')
    # # ego 
    # fig, ax = plt.subplots(figsize=(18, 13))
    # g_ego  = nx.ego_graph(g_edge, keyword)
    # ax.set_title('ego_network Graph', fontsize =16)
    # dc1 = nx.degree_centrality(g_ego).values()
    # nx.draw_networkx(g_ego,
    #                 pos = nx.kamada_kawai_layout(g_ego),
    #                 font_family = 'Malgun Gothic',
    #                 font_color = 'black',
    #                 with_labels = True,
    #                 font_size =13,
    #                 cmap = plt.cm.RdPu,
    #                 font_weight='bold',
    #                 edge_color='lightgray',
    #                 node_size = get_node_size(dc1),
    #                 node_color = list(dc1),
    #                 alpha = 0.9,
    #                 ax =ax)

    # st.pyplot(fig)