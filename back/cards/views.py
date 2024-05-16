from django.shortcuts import render


# 카드 고릴라 셀레니움 크롤링
def card_gorilla_selenium(request):
    # 1. 브라우저 인스턴스를 생성하고 제어
    # 2. Chrome 브라우저의 실행 옵션을 설정하는 데 사용
    # 3. Selenium에서 웹 요소를 찾는 데 사용되는 위치 전략을 정의 (웹 요소 지정)
    # 4. 지정한 윈도우나 탭을 찾을 수 없을 때 발생하는 예외 처리
    from selenium import webdriver  # 1
    from selenium.webdriver.chrome.options import Options  # 2
    from selenium.webdriver.common.by import By  # 3
    from selenium.common.exceptions import NoSuchWindowException, NoSuchElementException  # 4
    import csv

    # 크롬 옵션에 관한 인스턴스
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 불필요한 에러 메세지 없애기
    chrome_options.add_argument('--start-maximized')  # 브라우저가 최대화된 상태로 실행
    chrome_options.add_argument("disable-infobars")

    # 크롬 드라이버 인스턴스
    driver = webdriver.Chrome(options=chrome_options)

    # CSV 파일 생성 (저장 경로, 쓰기 모드, 인코딩, 줄바꿈 없음으로 조정)
    static_dir = "C:\\Users\\limkt\\Desktop\\SSAFY\\Test-SSAFY\\final_project\\static"
    csv_data1 = open(f"{static_dir}\\card_data.csv", 'w', encoding='CP949', newline='')
    card_data = csv.writer(csv_data1)
    csv_data2 = open(f"{static_dir}\\benefit_data.csv", 'w', encoding='CP949', newline='')
    benefit_data = csv.writer(csv_data2)

    cards = [] # 2498
    benefits = [] # 2498
    card_data.writerow(['pk', 'name', 'brand', 'image', 'annual_fee1', 'annual_fee2', 'record', 'type'])
    benefit_data.writerow(['card', 'title', 'content'])
    

    CARD_URL = "#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div"
    BENEFIT_URL = "#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.bene_area > dl"
    for pk in range(1, 2498):
        try:
            driver.get(f"https://www.card-gorilla.com/card/detail/{pk}")
            driver.execute_script('document.querySelector("#q-app > header").style.visibility="hidden";')

            # 이름
            card_name = driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.data_area > div.tit > strong").text
            # 브랜드
            card_brand = driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.data_area > div.tit > p").text
            # 이미지
            card_image = driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.plate_area > div.card_img > img").get_attribute("src")
            # 연회비 1
            card_annual_fee1 = driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.bnf2 > dl:nth-child(1) > dd.in_out > span:nth-child(1) > b").text.replace(',', '')
            # 전월 실적
            card_record = driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.bnf2 > dl:nth-child(2) > dd > b").text.replace(',', '')
            # 연회비 2
            try:
                card_annual_fee2 = driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.bnf2 > dl:nth-child(1) > dd.in_out > span:nth-child(2) > b").text.replace(',', '')
            except NoSuchElementException:
                card_annual_fee2 = None
            # 타입
            try:
                card_type = driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.bnf2 > dl:nth-child(3) > dd > span").text
            except NoSuchWindowException:
                card_type = None
            card_data.writerow([pk, card_name, card_brand, card_image, card_annual_fee1, card_annual_fee2, card_record, card_type])
            # cards.append([pk, card_name, card_brand, card_image, card_annual_fee1, card_annual_fee2, card_record, card_type])

            # 혜택
            benefit_name = driver.find_elements(By.CSS_SELECTOR, f"{BENEFIT_URL} > dt > p")
            # 혜택 내용
            benefit_content = driver.find_elements(By.CSS_SELECTOR, f"{BENEFIT_URL} > dt > i")
            # 혜택 상세 버튼
            # benefit_click = driver.find_elements(By.CSS_SELECTOR, BENEFIT_URL)

            for i in range(len(benefit_name)):
                bnf_name = benefit_name[i].text
                bnf_content = benefit_content[i].text
                # benefit_click[i].click()
                # bnf_detail = driver.find_elements(By.CSS_SELECTOR, f"{BENEFIT_URL} > dd > div > p")
                # detail = bnf_detail[i].text
                benefit_data.writerow([pk, bnf_name, bnf_content])

        except:
            continue
    
    driver.quit()
    context = {
        'cards': cards,
        'benefits': benefits,
    }
    return render(request, 'card_gorilla.html', context)