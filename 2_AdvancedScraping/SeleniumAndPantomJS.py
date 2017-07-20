from selenium import webdriver

url = "http://www.naver.com"

#   PhantomJS 드라이버 추출,
#   phantomjs.exe 파일의 경로 설정
browser = webdriver.PhantomJS(executable_path="D:\\python\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")

browser.implicitly_wait(3)

#   url 읽기
browser.get(url)

#
browser.save_screenshot("website.png")

browser.quit()