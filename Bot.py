import BotConfig
import time

driver = BotConfig.driver
driver.get('https://www.directmusicservice.com/login')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="index"]/div/ul/li[1]/a').click()
time.sleep(2)
driver.get('https://www.directmusicservice.com/login')
inputs = driver.find_elements_by_tag_name("input")
inputs[0].send_keys('iamdjmas')
inputs[1].send_keys('V3rd3r0s@DMS')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login"]/fieldset[4]/input').click()
time.sleep(1)
page = 76
count = 1
def download():
    global page
    global count
    driver.get('https://www.directmusicservice.com/browse/genres/hip-hop/' + str(page) + '/year/asc')
    print('Running on page', page)
    time.sleep(1)
    buttons = driver.find_elements_by_tag_name("a[class='download']")
    for button in buttons:
         driver.execute_script("arguments[0].click();", button)
         time.sleep(4)
    if page == 95:
        print('Hip hop downloads completed')
        time.sleep(10)
        driver.close()
        driver.quit()
    else:
        page += 1
    download()
download()
