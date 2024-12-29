from selenium.webdriver import Chrome

driver=Chrome() #open the browser
driver.get('http://www.google.com') #enter the url
print(driver.title) #print the title of the page
driver.close() #close the browser
