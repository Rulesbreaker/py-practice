import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    keyword = 'iphone'
    option = Options()
    option.add_argument('--headless')
    if len(sys.argv) > 1:
        keyword = sys.argv[1]
    chrome_driver = r"D:\ProgramData\Anaconda3\envs\py37\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
    driver = webdriver.Chrome(chrome_options=option, executable_path=chrome_driver)
    driver.get('https://www.jd.com/')
    # save screenshot to check bug
    # driver.save_screenshot('1.png')
    button = 'id,key'
    kw = driver.find_element(By.ID, 'key')

    kw.send_keys(keyword)
    kw.send_keys(Keys.ENTER)
    # sleep是为了让页面加载完，否则会取不到后面的button
    time.sleep(3)
    # 点击按销量排序
    sort_btn = driver.find_element(By.XPATH, './/div[@class="f-sort"]/a[2]')
    sort_btn.click()

    has_next = True
    while has_next:
        # sleep是为了让页面加载完，否则会取不到元素
        time.sleep(3)

        cur_page = driver.find_element(By.XPATH, '//div[@id="J_bottomPage"]//a[@class="curr"]').text
        print('--------Current page is %s--------' % cur_page)
        # 获取整个商品区域的尺寸
        goods_list = driver.find_element(By.ID, 'J_goodsList')
        # 根据区域大小决定往下滑动多少
        y = goods_list.rect['y'] + goods_list.rect['height']
        driver.execute_script('window.scrollTo(0, %s)' % y)
        # 获取所有商品节点
        products = driver.find_elements(By.CLASS_NAME, 'gl-item')
        for p in products:
            row = {}
            sku = p.get_attribute('data-sku')
            row['price'] = p.find_element(By.CSS_SELECTOR, 'strong.J_%s' % sku).text
            row['name'] = p.find_element(By.CSS_SELECTOR, 'div.p-name>a>em').text
            row['comments'] = p.find_element(By.ID, 'J_comment_%s' % sku).text
            try:
                row['shop'] = p.find_element(By.CSS_SELECTOR, 'div.p-shop>span>a').text
            except Exception:
                row['shop'] = '无'
            print(row)

        next_page = driver.find_element(By.CSS_SELECTOR, 'a.pn-next')
        if 'disabled' in next_page.get_attribute('class'):
            has_next = False
        else:
            next_page.click()

    driver.quit()
