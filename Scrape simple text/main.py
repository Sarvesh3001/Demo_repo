from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\sarveshwar\\Downloads\\chromedriver_win32\\chromedriver.exe")

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(service = service, options=options)
    driver.get("https://www.selenium.dev/documentation/webdriver")

    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by = "xpath", value = "/html/body/div/div[1]/div/main/div/div[1]")
    return element.text

print(main())
