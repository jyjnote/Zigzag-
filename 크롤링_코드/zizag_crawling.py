from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import pandas as pd

db_1 = list()   #예외처가 나도 데이터를 받을 수있는 리스트셋들
db_2 = list()

cols_1 = ['브랜드', '상품명', '가격', '리뷰수', '상품평점', '닉네임', '리뷰', '별점', '날짜', '맞춤정보','선택옵션', '한줄평']
cols_2=['스타일최고','구매욕상승','궁금증해소']

Zigzag_1 = pd.DataFrame(columns=cols_1)
Zigzag_1 = pd.DataFrame(columns=cols_2)

url='https://zigzag.kr/categories/-1?title=%EC%9D%98%EB%A5%98&category_id=-1&middle_category_id=474&sub_category_id=494&sort=201' #맨투맨/스웨터셔츠
driver = webdriver.Chrome()
driver.get(url)

#scrolls = 2 # 본인이 해당 변수가 들어간 부분 조정하면됨
for _ in range(2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

soup = BeautifulSoup(driver.page_source, "html.parser") # html객체를 가져옴
links = soup.select("#__next > div.zds-themes.light-theme > main > section.css-baq3dp.eabfyam0 > div a")  # 그안의 a태그를 싹다 가져오기

for link in links[:10]:
    product_url = link.get('href')
    full_url = f'https://zigzag.kr{product_url}' #접속
    driver.get(full_url)
    time.sleep(5)

    item_page = BeautifulSoup(driver.page_source, 'html.parser') #해당 상품 html 가져옴 // 아직 상품의 리뷰는 들어간거 아님

    brand_name = item_page.select_one('.css-1clkw4t').text #해당 태그 택스트가져옴 아래는 동일
    item_name = item_page.select_one('.css-jdi3f5').text
    price = item_page.select_one('.css-15ex2ru').text
    review_count = item_page.select_one('.css-1t4skuu').text
    item_score_avg = item_page.select_one('.e1cf25cj0').text
    
    #print(brand_name, item_name, price, review_count, item_score_avg)#확인용
    
    #리뷰 버튼 작동
    driver.find_element(By.CSS_SELECTOR, '#__next > div.zds-themes.light-theme > div > div.pdp__bottomFloating > div > div.css-qpt0u3.e1yh52zv2 > div > div').click()
    time.sleep(5)
    
    for _ in range(30):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(5)
    
    more_list = driver.find_elements(By.CSS_SELECTOR, ".css-1aa4nqt") # 더보기버튼들 담기
    
    for more in more_list:
        try:
            more.click() #더보기들 작동
            time.sleep(5)
            #print('더보기 작동') #아래 코드로 확인가능
        except:
            pass
    
    #time.sleep(5)    
    
    review_page = BeautifulSoup(driver.page_source, 'html.parser') #해당 상품의 리뷰 페이지 html 가져오기
    
    for ch in driver.find_elements(By.CSS_SELECTOR,'.css-1bpeccg'): #현재 창의 상품의 리뷰 페이지의 요소 세가지 컨테이너들을 모두 가져오기 ch는 캐릭터의 약자임 문자형으로 작업들을 할거니 ch 작명함
        #ch의 결과:<selenium.webdriver.remote.webelement.WebElement (session="d1f75d8107564e8c402f931a45874597", element="33145EAFE7948E8D821535A09D24995A_element_129")>
        
        #즉 현재 리뷰창이 스크롤이 되면 그 갯수만큼의 스타일최고, 구매욕상승, 궁금증해소 html을 가져온다
        
        filter=''.join(ch.text.split()) #결과 :'스타일최고0구매욕상승0궁금증해소0'
        
        #print(filter)

        #ch.text.split('\n')의 결과 예시 ['스타일최고', '0', '구매욕상승', '0', '궁금증해소', '0']

        if '스타일최고' in filter:
            style_score = int(ch.text.split('\n')[ch.text.split('\n').index('스타일최고')+1]) 
        else:style_score=0

        if '구매욕상승' in filter:
            purchase_score = int(ch.text.split('\n')[ch.text.split('\n').index('구매욕상승')+1])
        else:purchase_score=0

        if '궁금증해소' in filter:
            curiosity_score = int(ch.text.split('\n')[ch.text.split('\n').index('궁금증해소')+1])
        else:curiosity_score=0   

        db_2.append([style_score,purchase_score,curiosity_score])

    for review_element in review_page.select('.e1pdzmd01'): #리뷰페이지 닉네임,리뷰 등등이 담겨진 컨테이너 html 가져오기

        #초기화
        style_score=0
        purchase_score=0
        curiosity_score=0

        # 추출
        nickname = review_element.select_one('.css-utqis4').text
        review = review_element.select_one('.css-epr5m6').text
        star_container = review_element.select_one('div.css-c45d1y.e3ggphk2')
        rating = len(str(star_container).rsplit('#FFA93B')) - 1
        review_date = review_element.select_one('.css-1w6topb').text

        review_html = str(review_element.select_one('.css-q2mnm3')) #요소가 있는지 검사하기위해 html 자체를 문자화시킴

        custom_info = None
        selected_option = None
        summary_comment = None

        elements = review_element.select('.css-q2mnm3')

        #성공적으로 요소를 받았는지 검사
        if len(elements) > 0:
            text = elements[0].text

            # 모든 경우의 수 계산
            if '맞춤 정보' in text and '선택 옵션' in text and '한줄평' in text:
                custom_info = elements[0].select('.css-s53yvn.e170qtp21')[0].text
                selected_option = elements[0].select('.css-s53yvn.e170qtp21')[1].text
                summary_comment = elements[0].select('.css-s53yvn.e170qtp21')[2].text
            
            elif '맞춤 정보' in text and '선택 옵션' in text:
                custom_info = elements[0].select('.css-s53yvn.e170qtp21')[0].text
                selected_option = elements[0].select('.css-s53yvn.e170qtp21')[1].text
                summary_comment = None
            elif '맞춤 정보' in text and '한줄평' in text:
                custom_info = elements[0].select('.css-s53yvn.e170qtp21')[0].text
                selected_option = None
                summary_comment = elements[0].select('.css-s53yvn.e170qtp21')[1].text

            elif '선택 옵션' in text and '한줄평' in text:
                custom_info = None
                selected_option = elements[0].select('.css-s53yvn.e170qtp21')[0].text
                summary_comment = elements[0].select('.css-s53yvn.e170qtp21')[1].text

            elif '맞춤 정보' in text:
                custom_info = elements[0].select('.css-s53yvn.e170qtp21')[0].text

            elif '선택 옵션' in text:
                selected_option = elements[0].select('.css-s53yvn.e170qtp21')[0].text

            elif '한줄평' in text:
                summary_comment = elements[0].select('.css-s53yvn.e170qtp21')[0].text
 
        db_1.append([brand_name, item_name, price, review_count, item_score_avg, nickname, review, rating, review_date, custom_info,selected_option,summary_comment]) 
  

Zigzag_1 = pd.DataFrame(db_1, columns=cols_1)
Zigzag_2 = pd.DataFrame(db_2, columns=cols_2)
Zigzag = pd.concat([Zigzag_1, Zigzag_2], axis=1)
Zigzag.to_excel('Zigzag.xlsx', index=False)