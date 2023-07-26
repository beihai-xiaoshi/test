import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# 创建一个浏览器对象
browser = webdriver.Chrome()
ac = ActionChains(browser)
try:
    # 开启一个浏览器并访问https://www.baidu.com
    req=browser.get('https://trendinsight.oceanengine.com/api/open/index/get_portrait?_signature=_02B4Z6wo00901anpivAAAIDAiQ.NNN5RycGp7I5AAAugsyAJM0mGwa3uSrhArmGOWet80WpWUFCHoUB-UeJ4MYrsejMq4kEFfg.zAcAlxQT7k6lMChzoV7CtEaoNFWLIRj0tnIrddGJqvzl866')
    # 在打开的网页响应中根据id查找元素   获取到查询框

    print(req)
    time.sleep(20)

    # 显示等待， 等待10秒
    #wait = WebDriverWait(browser, 10)
    # 显式等待指定某个条件，然后设置最长等待时间。如果在这个时间还没有找到元素，那么便会抛出异常
    #wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    # 输出当前的url


finally:
    pass
    # 关闭浏览器
    browser.close()