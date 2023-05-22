import time
from selenium import webdriver
import urllib.request

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

search_box = driver.find_element("name", "q")
search_box.send_keys('letter A')
search_box.submit()
time.sleep(3)

SCROLL_PAUSE_TIME = 1

# scroll part
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


images = driver.find_elements('css selector', '.rg_i.Q4LuWd')
count = 1

for image in images:
    image.click()
    time.sleep(3)
    imgUrl = driver.find_element('css selector', '.n3VNCb.KAlRDb').get_attribute("src")
    urllib.request.urlretrieve(imgUrl, str(count) + '.jpg')
    count = count + 1

driver.quit()