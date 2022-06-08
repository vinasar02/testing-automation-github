from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://fibersafe.tmrnd.com.my:86/")
driver.maximize_window()
print(driver.title)