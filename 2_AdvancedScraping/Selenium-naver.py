from selenium import webdriver

id = ""
pw = ""

#   PhantomJS 드라이버 추출,
#   phantomjs.exe 파일의 경로 설정
browser = webdriver.PhantomJS(executable_path="D:\\python\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")

browser.implicitly_wait(3)

#   로그인 페이지 접근
url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지 접근")

#   id, pw 입력
e = browser.find_element_by_id("id")
e.clear()
e.send_keys(id)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(pw)

#   form 입력 및 로그인 요청
form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼 클릭")

#   네이버 쇼핑몰페이지 요청
browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")


#   출력
#products = browser.find_elements_by_css_selector(".p_info span")
products = browser.find_elements_by_css_selector("div.p_inr > div.p_info > a > span")
print("products : " , products)

for product in products :
    print("-", product.text)

