{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "57697548",
   "metadata": {},
   "outputs": [
    {
     "ename": "TimeoutException",
     "evalue": "Message: timeout: Timed out receiving message from renderer: 300.000\n  (Session info: chrome=121.0.6167.140)\nStacktrace:\n\tGetHandleVerifier [0x00007FF7BDC55E42+3538674]\n\t(No symbol) [0x00007FF7BD874C02]\n\t(No symbol) [0x00007FF7BD725AEB]\n\t(No symbol) [0x00007FF7BD712FE8]\n\t(No symbol) [0x00007FF7BD712E9F]\n\t(No symbol) [0x00007FF7BD7113A5]\n\t(No symbol) [0x00007FF7BD711E5F]\n\t(No symbol) [0x00007FF7BD71F32E]\n\t(No symbol) [0x00007FF7BD731D83]\n\t(No symbol) [0x00007FF7BD7361DA]\n\t(No symbol) [0x00007FF7BD712420]\n\t(No symbol) [0x00007FF7BD731B9A]\n\t(No symbol) [0x00007FF7BD7ABCBA]\n\t(No symbol) [0x00007FF7BD78EE53]\n\t(No symbol) [0x00007FF7BD75F514]\n\t(No symbol) [0x00007FF7BD760631]\n\tGetHandleVerifier [0x00007FF7BDC86CAD+3738973]\n\tGetHandleVerifier [0x00007FF7BDCDC506+4089270]\n\tGetHandleVerifier [0x00007FF7BDCD4823+4057299]\n\tGetHandleVerifier [0x00007FF7BD9A5C49+720121]\n\t(No symbol) [0x00007FF7BD88126F]\n\t(No symbol) [0x00007FF7BD87C304]\n\t(No symbol) [0x00007FF7BD87C432]\n\t(No symbol) [0x00007FF7BD86BD04]\n\tBaseThreadInitThunk [0x00007FFD8EB0257D+29]\n\tRtlUserThreadStart [0x00007FFD9080AA58+40]\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTimeoutException\u001b[0m                          Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[138], line 71\u001b[0m\n\u001b[0;32m     68\u001b[0m \u001b[38;5;66;03m#print(filter)\u001b[39;00m\n\u001b[0;32m     70\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m스타일최고\u001b[39m\u001b[38;5;124m'\u001b[39m \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mfilter\u001b[39m:\n\u001b[1;32m---> 71\u001b[0m     style_score \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mint\u001b[39m(ch\u001b[38;5;241m.\u001b[39mtext\u001b[38;5;241m.\u001b[39msplit(\u001b[38;5;124m'\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m'\u001b[39m)[\u001b[43mch\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mtext\u001b[49m\u001b[38;5;241m.\u001b[39msplit(\u001b[38;5;124m'\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m'\u001b[39m)\u001b[38;5;241m.\u001b[39mindex(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m스타일최고\u001b[39m\u001b[38;5;124m'\u001b[39m)\u001b[38;5;241m+\u001b[39m\u001b[38;5;241m1\u001b[39m])\n\u001b[0;32m     72\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:style_score\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0\u001b[39m\n\u001b[0;32m     74\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m구매욕상승\u001b[39m\u001b[38;5;124m'\u001b[39m \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mfilter\u001b[39m:\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\selenium\\webdriver\\remote\\webelement.py:90\u001b[0m, in \u001b[0;36mWebElement.text\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     87\u001b[0m \u001b[38;5;129m@property\u001b[39m\n\u001b[0;32m     88\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mtext\u001b[39m(\u001b[38;5;28mself\u001b[39m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28mstr\u001b[39m:\n\u001b[0;32m     89\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"The text of the element.\"\"\"\u001b[39;00m\n\u001b[1;32m---> 90\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_execute\u001b[49m\u001b[43m(\u001b[49m\u001b[43mCommand\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mGET_ELEMENT_TEXT\u001b[49m\u001b[43m)\u001b[49m[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\selenium\\webdriver\\remote\\webelement.py:395\u001b[0m, in \u001b[0;36mWebElement._execute\u001b[1;34m(self, command, params)\u001b[0m\n\u001b[0;32m    393\u001b[0m     params \u001b[38;5;241m=\u001b[39m {}\n\u001b[0;32m    394\u001b[0m params[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_id\n\u001b[1;32m--> 395\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_parent\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mexecute\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcommand\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mparams\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\selenium\\webdriver\\remote\\webdriver.py:347\u001b[0m, in \u001b[0;36mWebDriver.execute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    345\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mcommand_executor\u001b[38;5;241m.\u001b[39mexecute(driver_command, params)\n\u001b[0;32m    346\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m response:\n\u001b[1;32m--> 347\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43merror_handler\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcheck_response\u001b[49m\u001b[43m(\u001b[49m\u001b[43mresponse\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    348\u001b[0m     response[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_unwrap_value(response\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    349\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m response\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py:229\u001b[0m, in \u001b[0;36mErrorHandler.check_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    227\u001b[0m         alert_text \u001b[38;5;241m=\u001b[39m value[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124malert\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    228\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m exception_class(message, screen, stacktrace, alert_text)  \u001b[38;5;66;03m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[39;00m\n\u001b[1;32m--> 229\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m exception_class(message, screen, stacktrace)\n",
      "\u001b[1;31mTimeoutException\u001b[0m: Message: timeout: Timed out receiving message from renderer: 300.000\n  (Session info: chrome=121.0.6167.140)\nStacktrace:\n\tGetHandleVerifier [0x00007FF7BDC55E42+3538674]\n\t(No symbol) [0x00007FF7BD874C02]\n\t(No symbol) [0x00007FF7BD725AEB]\n\t(No symbol) [0x00007FF7BD712FE8]\n\t(No symbol) [0x00007FF7BD712E9F]\n\t(No symbol) [0x00007FF7BD7113A5]\n\t(No symbol) [0x00007FF7BD711E5F]\n\t(No symbol) [0x00007FF7BD71F32E]\n\t(No symbol) [0x00007FF7BD731D83]\n\t(No symbol) [0x00007FF7BD7361DA]\n\t(No symbol) [0x00007FF7BD712420]\n\t(No symbol) [0x00007FF7BD731B9A]\n\t(No symbol) [0x00007FF7BD7ABCBA]\n\t(No symbol) [0x00007FF7BD78EE53]\n\t(No symbol) [0x00007FF7BD75F514]\n\t(No symbol) [0x00007FF7BD760631]\n\tGetHandleVerifier [0x00007FF7BDC86CAD+3738973]\n\tGetHandleVerifier [0x00007FF7BDCDC506+4089270]\n\tGetHandleVerifier [0x00007FF7BDCD4823+4057299]\n\tGetHandleVerifier [0x00007FF7BD9A5C49+720121]\n\t(No symbol) [0x00007FF7BD88126F]\n\t(No symbol) [0x00007FF7BD87C304]\n\t(No symbol) [0x00007FF7BD87C432]\n\t(No symbol) [0x00007FF7BD86BD04]\n\tBaseThreadInitThunk [0x00007FFD8EB0257D+29]\n\tRtlUserThreadStart [0x00007FFD9080AA58+40]\n"
     ]
    }
   ],
   "source": [
    "from selenium import webdriver\n",
    "from bs4 import BeautifulSoup\n",
    "from selenium.webdriver.common.by import By\n",
    "import time\n",
    "import pandas as pd\n",
    "\n",
    "db_1 = list()\n",
    "db_2 = list()\n",
    "\n",
    "cols_1 = ['브랜드', '상품명', '가격', '리뷰수', '상품평점', '닉네임', '리뷰', '별점', '날짜', '맞춤정보','선택옵션', '한줄평']\n",
    "cols_2=['스타일최고','구매욕상승','궁금증해소']\n",
    "\n",
    "Zigzag_1 = pd.DataFrame(columns=cols_1)\n",
    "Zigzag_1 = pd.DataFrame(columns=cols_2)\n",
    "\n",
    "#url = 'https://zigzag.kr/categories/-1?title=%EC%9D%98%EB%A5%98&category_id=-1&middle_category_id=560&sub_category_id=561&sort=201' # 미니스커트\n",
    "url='https://zigzag.kr/categories/-1?title=%EC%9D%98%EB%A5%98&category_id=-1&middle_category_id=507&sort=201'#원피스\n",
    "\n",
    "driver = webdriver.Chrome()\n",
    "driver.get(url)\n",
    "\n",
    "scrolls = 3\n",
    "for _ in range(scrolls):\n",
    "    driver.execute_script(\"window.scrollTo(0, document.body.scrollHeight);\")\n",
    "    time.sleep(2)\n",
    "\n",
    "soup = BeautifulSoup(driver.page_source, \"html.parser\")\n",
    "links = soup.select(\"#__next > div.zds-themes.light-theme > main > section.css-baq3dp.eabfyam0 > div a\")\n",
    "\n",
    "for link in links:\n",
    "    product_url = link.get('href')\n",
    "    full_url = f'https://zigzag.kr{product_url}'\n",
    "    driver.get(full_url)\n",
    "    time.sleep(5)\n",
    "\n",
    "    item_page = BeautifulSoup(driver.page_source, 'html.parser')\n",
    "\n",
    "    brand_name = item_page.select_one('.css-1clkw4t').text\n",
    "    item_name = item_page.select_one('.css-jdi3f5').text\n",
    "    price = item_page.select_one('.css-15ex2ru').text\n",
    "    review_count = item_page.select_one('.css-1t4skuu').text\n",
    "    item_score_avg = item_page.select_one('.e1cf25cj0').text\n",
    "    \n",
    "    #print(brand_name, item_name, price, review_count, item_score_avg)\n",
    "    \n",
    "    driver.find_element(By.CSS_SELECTOR, '#__next > div.zds-themes.light-theme > div > div.pdp__bottomFloating > div > div.css-qpt0u3.e1yh52zv2 > div > div').click()\n",
    "    time.sleep(4)\n",
    "    \n",
    "    for _ in range(scrolls):\n",
    "        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')\n",
    "        time.sleep(4)\n",
    "    \n",
    "    more_list = driver.find_elements(By.CSS_SELECTOR, \".css-1aa4nqt\")\n",
    "    \n",
    "    for more in more_list:\n",
    "        try:\n",
    "            more.click()\n",
    "        except:\n",
    "            pass\n",
    "    \n",
    "    time.sleep(10)    \n",
    "    \n",
    "    review_page = BeautifulSoup(driver.page_source, 'html.parser')\n",
    "    \n",
    "    for ch in driver.find_elements(By.CSS_SELECTOR,'.css-1bpeccg'):\n",
    "        filter=''.join(ch.text.split())\n",
    "        \n",
    "        #print(filter)\n",
    "\n",
    "        if '스타일최고' in filter:\n",
    "            style_score = int(ch.text.split('\\n')[ch.text.split('\\n').index('스타일최고')+1])\n",
    "        else:style_score=0\n",
    "\n",
    "        if '구매욕상승' in filter:\n",
    "            purchase_score = int(ch.text.split('\\n')[ch.text.split('\\n').index('구매욕상승')+1])\n",
    "        else:purchase_score=0\n",
    "\n",
    "        if '궁금증해소' in filter:\n",
    "            curiosity_score = int(ch.text.split('\\n')[ch.text.split('\\n').index('궁금증해소')+1])\n",
    "        else:curiosity_score=0   \n",
    "\n",
    "        db_2.append([style_score,purchase_score,curiosity_score])\n",
    "\n",
    "    for review_element in review_page.select('.e1pdzmd01'):\n",
    "\n",
    "        style_score=0\n",
    "        purchase_score=0\n",
    "        curiosity_score=0\n",
    "\n",
    "        nickname = review_element.select_one('.css-utqis4').text\n",
    "        review = review_element.select_one('.css-epr5m6').text\n",
    "        star_container = review_element.select_one('div.css-c45d1y.e3ggphk2')\n",
    "        rating = len(str(star_container).rsplit('#FFA93B')) - 1\n",
    "        review_date = review_element.select_one('.css-1w6topb').text\n",
    "\n",
    "        review_html = str(review_element.select_one('.css-q2mnm3')) \n",
    "        recommend_html = str(review_page.select('.css-1bpeccg')) \n",
    "\n",
    "        if '맞춤 정보' in review_html:\n",
    "            custom_info=review_element.select_one('.css-q2mnm3').select_one('.css-s53yvn').text\n",
    "        else:\n",
    "            custom_info = None\n",
    "\n",
    "        if '선택 옵션' in review_html:\n",
    "            try:\n",
    "                custom_info_element = review_element.select_one('.css-q2mnm3')\n",
    "                selected_option=custom_info_element.select_one('.css-1ccr5bn').text+custom_info_element.select('.css-1ccr5bn')[1].text\n",
    "            except IndexError :\n",
    "                selected_option=custom_info_element.select_one('.css-1ccr5bn').text\n",
    "        else:\n",
    "            selected_option = None\n",
    "\n",
    "        if '한줄평' in review_html:\n",
    "            #try:\n",
    "                summary_comment=review_page.select('.css-s53yvn')[2].text\n",
    "            #except IndexError :\n",
    "            #   summary_comment=review_page.select('.css-s53yvn')[0].text\n",
    "        else:\n",
    "            summary_comment = None\n",
    " \n",
    "\n",
    "        db_1.append([brand_name, item_name, price, review_count, item_score_avg, nickname, review, rating, review_date, custom_info,selected_option,summary_comment])\n",
    "\n",
    "    \n",
    "\n",
    "Zigzag_1 = pd.DataFrame(db_1, columns=cols_1)\n",
    "Zigzag_2 = pd.DataFrame(db_2, columns=cols_2)\n",
    "Zigzag = pd.concat([Zigzag_1, Zigzag_2], axis=1)\n",
    "Zigzag\n",
    "\n",
    "Zigzag.to_csv('zigzag_data.csv', index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "518107ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "Zigzag.to_excel('zigzag_data.xlsx', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "59365c09",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'스타일최고0구매욕상승1궁금증해소0'"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "filter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "a379f7cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<selenium.webdriver.remote.webelement.WebElement (session=\"27abb4f447969e49ba65425cb10df3a7\", element=\"56A06EC11AFDE1824E63989FD19120B4_element_8057\")>"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ch"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "241a6fd7",
   "metadata": {},
   "outputs": [
    {
     "ename": "StaleElementReferenceException",
     "evalue": "Message: stale element reference: stale element not found\n  (Session info: chrome=121.0.6167.140); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#stale-element-reference-exception\nStacktrace:\n\tGetHandleVerifier [0x00007FF7BDC55E42+3538674]\n\t(No symbol) [0x00007FF7BD874C02]\n\t(No symbol) [0x00007FF7BD725AEB]\n\t(No symbol) [0x00007FF7BD73514B]\n\t(No symbol) [0x00007FF7BD72B92A]\n\t(No symbol) [0x00007FF7BD729D10]\n\t(No symbol) [0x00007FF7BD72D150]\n\t(No symbol) [0x00007FF7BD72D210]\n\t(No symbol) [0x00007FF7BD76723B]\n\t(No symbol) [0x00007FF7BD78F0AA]\n\t(No symbol) [0x00007FF7BD76124A]\n\t(No symbol) [0x00007FF7BD78F2C0]\n\t(No symbol) [0x00007FF7BD7ABDE3]\n\t(No symbol) [0x00007FF7BD78EE53]\n\t(No symbol) [0x00007FF7BD75F514]\n\t(No symbol) [0x00007FF7BD760631]\n\tGetHandleVerifier [0x00007FF7BDC86CAD+3738973]\n\tGetHandleVerifier [0x00007FF7BDCDC506+4089270]\n\tGetHandleVerifier [0x00007FF7BDCD4823+4057299]\n\tGetHandleVerifier [0x00007FF7BD9A5C49+720121]\n\t(No symbol) [0x00007FF7BD88126F]\n\t(No symbol) [0x00007FF7BD87C304]\n\t(No symbol) [0x00007FF7BD87C432]\n\t(No symbol) [0x00007FF7BD86BD04]\n\tBaseThreadInitThunk [0x00007FFD8EB0257D+29]\n\tRtlUserThreadStart [0x00007FFD9080AA58+40]\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mStaleElementReferenceException\u001b[0m            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[142], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mch\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mtext\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\selenium\\webdriver\\remote\\webelement.py:90\u001b[0m, in \u001b[0;36mWebElement.text\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     87\u001b[0m \u001b[38;5;129m@property\u001b[39m\n\u001b[0;32m     88\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mtext\u001b[39m(\u001b[38;5;28mself\u001b[39m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28mstr\u001b[39m:\n\u001b[0;32m     89\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"The text of the element.\"\"\"\u001b[39;00m\n\u001b[1;32m---> 90\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_execute\u001b[49m\u001b[43m(\u001b[49m\u001b[43mCommand\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mGET_ELEMENT_TEXT\u001b[49m\u001b[43m)\u001b[49m[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\selenium\\webdriver\\remote\\webelement.py:395\u001b[0m, in \u001b[0;36mWebElement._execute\u001b[1;34m(self, command, params)\u001b[0m\n\u001b[0;32m    393\u001b[0m     params \u001b[38;5;241m=\u001b[39m {}\n\u001b[0;32m    394\u001b[0m params[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_id\n\u001b[1;32m--> 395\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_parent\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mexecute\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcommand\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mparams\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\selenium\\webdriver\\remote\\webdriver.py:347\u001b[0m, in \u001b[0;36mWebDriver.execute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    345\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mcommand_executor\u001b[38;5;241m.\u001b[39mexecute(driver_command, params)\n\u001b[0;32m    346\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m response:\n\u001b[1;32m--> 347\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43merror_handler\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcheck_response\u001b[49m\u001b[43m(\u001b[49m\u001b[43mresponse\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    348\u001b[0m     response[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_unwrap_value(response\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    349\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m response\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py:229\u001b[0m, in \u001b[0;36mErrorHandler.check_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    227\u001b[0m         alert_text \u001b[38;5;241m=\u001b[39m value[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124malert\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    228\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m exception_class(message, screen, stacktrace, alert_text)  \u001b[38;5;66;03m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[39;00m\n\u001b[1;32m--> 229\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m exception_class(message, screen, stacktrace)\n",
      "\u001b[1;31mStaleElementReferenceException\u001b[0m: Message: stale element reference: stale element not found\n  (Session info: chrome=121.0.6167.140); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#stale-element-reference-exception\nStacktrace:\n\tGetHandleVerifier [0x00007FF7BDC55E42+3538674]\n\t(No symbol) [0x00007FF7BD874C02]\n\t(No symbol) [0x00007FF7BD725AEB]\n\t(No symbol) [0x00007FF7BD73514B]\n\t(No symbol) [0x00007FF7BD72B92A]\n\t(No symbol) [0x00007FF7BD729D10]\n\t(No symbol) [0x00007FF7BD72D150]\n\t(No symbol) [0x00007FF7BD72D210]\n\t(No symbol) [0x00007FF7BD76723B]\n\t(No symbol) [0x00007FF7BD78F0AA]\n\t(No symbol) [0x00007FF7BD76124A]\n\t(No symbol) [0x00007FF7BD78F2C0]\n\t(No symbol) [0x00007FF7BD7ABDE3]\n\t(No symbol) [0x00007FF7BD78EE53]\n\t(No symbol) [0x00007FF7BD75F514]\n\t(No symbol) [0x00007FF7BD760631]\n\tGetHandleVerifier [0x00007FF7BDC86CAD+3738973]\n\tGetHandleVerifier [0x00007FF7BDCDC506+4089270]\n\tGetHandleVerifier [0x00007FF7BDCD4823+4057299]\n\tGetHandleVerifier [0x00007FF7BD9A5C49+720121]\n\t(No symbol) [0x00007FF7BD88126F]\n\t(No symbol) [0x00007FF7BD87C304]\n\t(No symbol) [0x00007FF7BD87C432]\n\t(No symbol) [0x00007FF7BD86BD04]\n\tBaseThreadInitThunk [0x00007FFD8EB0257D+29]\n\tRtlUserThreadStart [0x00007FFD9080AA58+40]\n"
     ]
    }
   ],
   "source": [
    "ch.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "id": "50005ba3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method WebElement.find_element of <selenium.webdriver.remote.webelement.WebElement (session=\"27abb4f447969e49ba65425cb10df3a7\", element=\"56A06EC11AFDE1824E63989FD19120B4_element_8057\")>>"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ch.find_element"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36ccb340",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
