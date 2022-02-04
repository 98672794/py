



'''
winpy3

webdriver Chrome 動作
ATWSteChrome
ATW202202042022
mokaki
https://98672794.github.io/
'''
# -*- coding: UTF-8 -*-









from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent
import random


# 截圖
from PIL import Image

from PIL import ImageGrab


import time
import os
import logging
import requests
import json
import zipfile
from win32com import client as wincom_client


import ATWFolder












###################################################################################
############################################################# ATWSteChrome 說明
def README(): 
    print ("\n*** README ***\n")
    t = [
        'mokaki',
        'https://98672794.github.io/',
        '202202 ',
        ' ==== 恭賀新禧 ==== ',
        'ATWSteChrome.',
        '打開chrome,冇去下 =\n    _SteChrome(chromedriverURL,ChromeSel)',
        '自动下載最新 chromedriver =\n    _InputChromeAutoUpData(chromedriverURL)',
        '_SeleniumHighlight =\n    _SeleniumHighlight(element, effect_time, color, border)',
        ' =\n    _',
        ' =\n    _',
        'Loop 數 停 202111272338 =\n    _Loop數停(chrome號,點位,動作,入字)',
        '登入whatsapp 202110230158 =\n    _LoginWhatsapp(ChromeSel,t1,sel)'
    ]
    for txt in t:
        print ("\n   ",txt,"\n")
    print ("\n*** /README ***\n")
    os.system("pause")

















###################################################################################
####################################################### AutoWeb selenium chrome set
def _SteChrome(chromedriverURL,ChromeSel):     #   (保存chromedriver的路徑)
    
    global chrome

    #selenium chrome 配置
    options = Options()
    #if ChromeSel == 'chrome1':
    #    options.add_argument('--headless')  # 配置无界面

    options.add_argument("--incognito")  # 配置隐私模式 https://blog.csdn.net/weixin_35757704/article/details/112975153
    options.add_argument("--disable-notifications")

    # 取消log
    options.use_chromium = True
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    

    #random window_siz
    #        K        k    k
    W = [280,540,375,414,375,320,411,411,360]
    H = [653,720,812,736,667,568,823,731,640]

    N = int(random.uniform(0, 8))


    # chromedriver有否
    while True:
        try:
            chromedriverURL0 = chromedriverURL + '/chromedriver'
    
            # Chrome ADMIN
            if ChromeSel == 'chrome':
                chrome = webdriver.Chrome(chromedriverURL0, chrome_options=options)
                chrome.set_window_size(W[N],H[N])
    

            # User Chrome1,2,3,4...
            else:
                # python 批量 global
                names = globals()
                aa=ChromeSel[6:]
                # 动态变量名赋值 https://www.runoob.com/w3cnote/python-dynamic-var.html
                names['chrome' + str(aa) ] = webdriver.Chrome(chromedriverURL0, chrome_options=options)

                #options.add_argument("--incognito")# 配置隐私模式
                #options.add_argument('--headless') # 配置无界面

            ua = UserAgent()
            userAgent = ua.random
            options.add_argument(f'user-agent={userAgent}')


            break
        except:
            # 自动下載最新chromedrive
            _InputChromeAutoUpData(chromedriverURL)    #   (保存chromedriver的路徑)
            continue
    


















































###################################################################################
################################################## AutoWeb 自动下載最新 chromedriver
# https://medium.com/drunk-wis/python-selenium-chrome-browser-%E8%88%87-driver-%E6%83%B1%E4%BA%BA%E7%9A%84%E7%89%88%E6%9C%AC%E7%AE%A1%E7%90%86-cbaf1d1861ce

ii0 = 0
ChmExUrl0 = 0
# chrome_helper.py
CHROME_DRIVER_BASE_URL = "https://chromedriver.storage.googleapis.com"
#CHROME_DRIVER_FOLDER = ii0    # chromedriver 存放路徑
CHROME_DRIVER_MAPPING_FILE = r"{}\mapping.json".format(ii0)
CHROME_DRIVER_EXE = r"{}\chromedriver.exe".format(ii0)
CHROME_DRIVER_ZIP = r"{}\chromedriver_win32.zip".format(ii0)
def _InputChromeAutoUpData(chromedriverURL):    #   (保存chromedriver的路徑)
    global ii0
    global ChmExUrl0
    #print ('_SetFolder\n'+ str(v1) +'\n')

    # chromedriver 存放路徑
    #tt2 = '*****您好\n***請填寫下載 chromedriver 後存放的路徑，如:\n.\AutoWeb\n'
    #ii0 = input(tt2)
    ii0 = chromedriverURL
    
    # _SetFolder
    ATWFolder._SetFolder(ii0,'MakeFolder')   #   (文件夾名,動作)

    tt2 = '***請填寫您的 chrome.exe 路徑，如:'
    tt9 = '***您的chrome.exe不存在***'
    # 驗查 chrome.exe 位置
    ChmExUrl1 = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    ChmExUrl2 = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    if os.path.isfile(ChmExUrl1):
        #print ('ChmExUrl1\n'+ str(ChmExUrl1) +'\n')
        ChmExUrl0 = ChmExUrl1
    else:
        if os.path.isfile(ChmExUrl2):
            #print ('ChmExUrl2\n'+ str(ChmExUrl2) +'\n')
            ChmExUrl0 = ChmExUrl2
        else:
            # 都沒 = input loop 至有
            while True:
                print (tt9)
                ii1 = input(tt2+ChmExUrl1+ChmExUrl2)
                try:
                    print ('\n'+ str(ii1) +'\n')
                    if os.path.isfile(ii1):
                        ChmExUrl0 = ii1
                except:
                    continue
                else:
                    break
    # Run
    check_browser_driver_available()

def get_chrome_driver_major_version():
    chrome_browser_path = ChmExUrl0     #chrome.exe 位置
    chrome_ver = get_file_version(chrome_browser_path)
    chrome_major_ver = chrome_ver.split(".")[0]
    return chrome_major_ver

def get_latest_driver_version(browser_ver):
    latest_api = "{}/LATEST_RELEASE_{}".format(
        CHROME_DRIVER_BASE_URL, browser_ver)
    resp = requests.get(latest_api)
    lastest_driver_version = resp.text.strip()
    return lastest_driver_version

def download_driver(driver_ver, dest_folder):
    download_api = "{}/{}/chromedriver_win32.zip".format(
        CHROME_DRIVER_BASE_URL, driver_ver)
    dest_path = os.path.join(dest_folder, os.path.basename(download_api))
    resp = requests.get(download_api, stream=True, timeout=300)

    if resp.status_code == 200:
        with open(dest_path, "wb") as f:
            f.write(resp.content)
        logging.info("Download driver completed")
    else:
        raise Exception("Download chrome driver failed")

def unzip_driver_to_target_path(src_file, dest_path):
    with zipfile.ZipFile(src_file, 'r') as zip_ref:
        zip_ref.extractall(dest_path)
    logging.info("Unzip [{}] -> [{}]".format(src_file, dest_path))

def read_driver_mapping_file():
    driver_mapping_dict = {}
    if os.path.exists(CHROME_DRIVER_MAPPING_FILE):
        driver_mapping_dict = read_json(CHROME_DRIVER_MAPPING_FILE)
    return driver_mapping_dict

def check_browser_driver_available():
    chrome_major_ver = get_chrome_driver_major_version()
    mapping_dict = read_driver_mapping_file()
    driver_ver = get_latest_driver_version(chrome_major_ver)

    if chrome_major_ver not in mapping_dict:
        download_driver(driver_ver, ii0)
        unzip_driver_to_target_path(r'{}/chromedriver_win32.zip'.format(ii0), ii0)

        mapping_dict = {
            chrome_major_ver: {
                "driver_path": CHROME_DRIVER_EXE,
                "driver_version": driver_ver
            }
        }
        
        # 下載完 Del zip
        os.remove(r'{}/chromedriver_win32.zip'.format(ii0))


        print ("\n***!!chromedriver 已經下載到",ii0," 文件夾中!!!!!*****\n")

        mapping_dict.update(mapping_dict)
        #write_json(CHROME_DRIVER_MAPPING_FILE, mapping_dict)

# file_util.py
def get_file_version(file_path):
    logging.info('Get file version of [%s]', file_path)
    if not os.path.isfile(file_path):
        raise FileNotFoundError("{!r} is not found.".format(file_path))

    wincom_obj = wincom_client.Dispatch('Scripting.FileSystemObject')
    version = wincom_obj.GetFileVersion(file_path)
    logging.info('The file version of [%s] is %s', file_path, version)
    return version.strip()

def read_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

























































################################################################ _SeleniumHighlight
# https://stackoverflow.com/questions/52207164/python-selenium-highlight-element-doesnt-do-anything
#   _SeleniumHighlight(Txt1, 3, "blue", 5)
def _SeleniumHighlight(element, effect_time, color, border):
    """Highlights (blinks) a Selenium Webdriver element"""
    chrome = element._parent
    def apply_style(s):
        chrome.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)







































################################################## Loop and Check
#   C   = CheckPoint
#   T   = Talk
def _LoopAndCheck(c1,c2,c3,c4,c5,t1,t2,t3,t4,t5,sel):  

    #print('\n   *4** ',c1,' ***\n') 

    if sel == 'WAR1':
        while True:
            print('\n   *** ',t1,' ***\n') 
            try:
                #   WAR1 = 點個人檔案
                c1 = eval(c1)
                c1
                break
            except:
                time.sleep(2)
                continue

        try:
            #   WAR1 = 您的名字
            c2 = eval(c2)
            say = c2.find_element_by_xpath(c3).get_attribute('textContent')
            print('\n   *** ',say,t2,' ***\n') 
        except:
            print('\n   *** 找不到 您的名字 ***\n') 




'''
    c1 = eval(c1)
    c2 = eval(c2)
    c3 = eval(c3)
    c4 = eval(c4)
    c5 = eval(c5)


'''











################################################## Loop 數 停
# 202111272338
def _Loop數停(chrome號,點位,動作,入字):
    Error數 = 0
    while True:
        try:
            全 = eval(chrome號 + '.find_element_by_xpath(' + 點位 + ').' + 動作 + '()')
            全
            
            況 = '可'
            break

        except:
            Error數+=1
            print('Error數=',Error數)
            if Error數 == 3:
                況 = '沒'
                break

            time.sleep(2)
            continue

    return 況















################################################## whatsapp
# 登入whatsapp

#   C   = CheckPoint
#   T   = Talk
def _LoginWhatsapp(ChromeSel,t1,sel):  
    #print('\n   *4** ',c1,' ***\n') 

    NN202110230158 = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]'  

    if sel == 'WAR1':
        while True:
            print('\n   *** ',t1,' ***\n') 
            try:
                #   WAR1 = 點個人檔案
                c1 = eval(ChromeSel)
                c1.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/header/div[1]/div/img').click()
                break
            except:
                time.sleep(2)
                continue





























# K ##################################################################################################
####################################################################################### Login Facebook













































































#
#
#
# cd C:/Users/mokaki/AppData/Local/Programs/Python/Python39/python setup.py install

if __name__ == "__main__":
    README()

