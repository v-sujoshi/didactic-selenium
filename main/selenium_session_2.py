from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver(r"C:\\Users\\v-sujoshi.FAREAST\\Workspace\\playground\\driver\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
