from selenium import webdriver

print("Hello Mathu")

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

print("Hello Mathu")
assert 'Django' in browser.title 
assert 'Mathu' in browser.title 