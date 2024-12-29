from selenium.webdriver import Chrome

driver=Chrome() #open the browser
driver.get('http://www.fb.com') #enter the url
print(driver.title) #print the title of the page
print(driver.current_url) #print the url present in the address bar
print(driver.page_source) #print html code of the page
driver.close() #close the browser
