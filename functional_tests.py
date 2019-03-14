from selenium import webdriver

firefoxprofile = webdriver.FirefoxProfile()
browser = webdriver.Firefox(firefoxprofile)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
