from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.lambdatest.com")
pageTitle = driver.title # retrieve the title of the current web page
print(pageTitle)
pageSource = driver.page_source # retrieve the source code of the last loaded page
print(pageSource)
driver.quit()
