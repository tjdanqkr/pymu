from selenium import webdriver

chedr = r'C:\Users\BIT\Desktop\chromedriver.exe'
driver = webdriver.Chrome(chedr)

#browser = webdriver.PhantomJS()
driver.implicitly_wait(3)

driver.get('https://naver.com')

r = driver.execute_script("return 100 +50")
print(r)

