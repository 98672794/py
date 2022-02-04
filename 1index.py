

'''
winpy3

1index
執行Github中的.py
ATW20220204
mokaki
https://98672794.github.io/




'''

# -*- coding: UTF-8 -*-
##########################################################################import
from copy import Error
import re


import ATWSteChrome
import ATWFolder











###################################################################################
############################################################# 1index 說明
def README(): 
    print ("\n*** README ***\n")
    t = [
        'mokaki',
        'https://98672794.github.io/',
        '202202042044',
        ' ==== 恭賀新禧 ==== ',
        '1index.',
        '000 =\n    0000',
        '000 =\n    0000',
        '000 =\n    0000',
        '000 =\n    0000'
    ]
    for txt in t:
        print ("\n   ",txt,"\n")
    print ("\n*** /README ***\n")
    ATWFolder.os.system("pause")











#######################################################################
##################################################### Start = 開始 分頁0
def Start():

    #### 在當前文件夾创工作目錄 if not ####
    NowJobFolder = ATWFolder._MakeJobFolder('_atw')

    #### selenium chrome 配置 ####
    #                                             冇下載
    ATWSteChrome._SteChrome(NowJobFolder,'chrome')
    #                                             admin login whatsapp
    ATWSteChrome.chrome.get('https://98672794.github.io/')
























###################################################################################### 发生异常
def _Error(e):
    print(e)
    print(e.__traceback__.tb_frame.f_globals["__file__"])   # 发生异常所在的文件
    print(e.__traceback__.tb_lineno)                        # 发生异常所在的行数










if __name__ == "__main__":
    Start()
    #README()






