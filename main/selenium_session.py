from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = WebDriver(r"C:\\Users\\v-sujoshi.FAREAST\\Workspace\\playground\\driver\\chromedriver.exe")

driver.get("https://teams.microsoft.com")
driver.maximize_window()
print(driver.title)  # Login page
print(driver.current_url)

# How to find out Relative X-path
"""
Xpath construct:
Xpath="//tagname[@attribute='value']"
Xpath="//tagname[contains(@attribute, 'foo-')]"  id = "foo-<username>"
Xpath="//*[contains(text(),'underlying text to search')]"
Xpath="//*[@attribute1='value1' <or/and> @attribute2='value2']"
Xpath="//tagname[starts-with(@attribute,'value')]" "valueabcd"
Xpath="//td[text()='underlying text to search']"

https://www.guru99.com/xpath-selenium.html#:~:text=The%20XPath%20text%20%28%29%20function%20is%20a%20built-in,to%20be%20located%20should%20be%20in%20string%20form.
"""

# Send some email id for login screen using relative xpath
element = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//input[@type='email']")))
# element = driver.find_element_by_xpath("//input[@type='email']")

# Focus
if element == driver.switch_to.active_element:
    print("Email input is focussed")
else:
    print("Email input is not in focus")

email_id = "v-sujoshi@microsoft.com"
element.send_keys(email_id)

# Usage of indexes in Xpath

# Scroll Bar
driver.find_element_by_id("moreOptions").click()
scroll_element = driver.find_element_by_xpath("//div[contains(text(), 'If you plan on getting help for this problem')]")

# Javascript Executor
# driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
# driver.execute_script("scrollBy();")

# ActionChains
act = ActionChains(driver)
act.move_to_element(scroll_element).perform()
# act.send_keys(Keys.PAGE_DOWN).perform()

# Hover
hover_element = driver.find_element_by_xpath("//div[@aria-label='Sign-in options']")
act.move_to_element(hover_element).perform()


# highlighted text
act.move_to_element(element).click()
act.send_keys(Keys.HOME)
act.key_down(Keys.LEFT_SHIFT)
for _ in range(2):
    act.send_keys(Keys.ARROW_RIGHT)
act.key_up(Keys.LEFT_SHIFT).perform()
selection = driver.execute_script("return window.getSelection().toString();")
print(selection)

# act.move_by_offset(10, 0)

# drag functionalities
# https://www.geeksforgeeks.org/drag_and_drop-action-chains-in-selenium-python/#:~:text=Action%20chain%20methods%20are%20used%20by%20advanced%20scripts,the%20target%20element%20and%20releases%20the%20mouse%20button.
# act.drag_and_drop()
