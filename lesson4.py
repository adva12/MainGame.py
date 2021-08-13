from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/USER/Desktop/chromedriver.exe')
driver.get("https://google.com")

print(driver.current_url)
#print(driver.page_source)
#driver.quit()