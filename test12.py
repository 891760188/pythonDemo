# -*- coding: UTF-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support import ui

# browser = webdriver.PhantomJs()
browser = webdriver.Chrome()
url = 'https://www.kaistart.com/project/more.html'
try:
    browser.get(url)
    wait = ui.WebDriverWait(browser, 20)
    wait.until(lambda dr: dr.find_element_by_class_name('project-detail').is_displayed())

    # 一直滚动到最底部
    js1 = 'return document.body.scrollHeight'
    js2 = 'window.scrollTo(0, document.body.scrollHeight)'
    old_scroll_height = 0
    i = 0
    while i < 2 and browser.execute_script(js1) >= old_scroll_height:
        old_scroll_height = browser.execute_script(js1)
        browser.execute_script(js2)
        time.sleep(1)
        i+=1

    # sel = Selector(text=browser.page_source)
    # proj_list = sel.xpath('//li[@class="project-li"]')

    ul = browser.find_element_by_css_selector('ul.screen-list')
    lis = ul.find_elements_by_tag_name('li'); # element和elements的区别
    for li in lis:
        print  li.text

except:
    print 'err'
finally:
    print 'finally'