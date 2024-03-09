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


# def get_predict(data,_scaler, col, model, vectorizer):
#     x = vectorizer.transform(data).toarray()
#     x = _scaler.transform(x)    
#     x = x[:, col]  # Accessing the appropriate index of the tuple
#     return model.predict(x)

# def get_keyword(data, models_info):
#     predictions = []
#     for model_info in models_info:
#         vectorizer, scaler, col, model = model_info
#         predictions.append(get_predict(tokenizer(data), scaler, col, model, vectorizer))
#     return predictions



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
