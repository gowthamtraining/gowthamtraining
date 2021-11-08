from selenium import webdriver
a = input('enter any thing')
driver = webdriver.Chrome()
driver.get('https://www.google.com/search?q='+a+'&rlz')
