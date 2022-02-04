




'''
winpy3

文件夾動作
ATWFolder
ATW202202042022
mokaki
https://98672794.github.io/
'''
# -*- coding: UTF-8 -*-


import os





###################################################################################
############################################################# ATWFolder說明
def README(): 
    print ("\n*** README ***\n")
    t = [
        'mokaki',
        'https://98672794.github.io/',
        '202202042044',
        ' ==== 恭賀新禧 ==== ',
        'ATWFolder.',
        '生成文件夾 =\n    _SetFolder(v1,sel)',
        '獲取檔案路徑和當前工作目錄 =\n    _GetFolder()',
        '在當前文件夾创工作目錄 =\n    _MakeJobFolder(FolderName)'
    ]
    for txt in t:
        print ("\n   ",txt,"\n")
    print ("\n*** /README ***\n")
    os.system("pause")






###################################################################################
################################################################ AutoWeb 生成文件夾
def _SetFolder(v1,sel):     #   (文件夾名,動作)
    #print ('_SetFolder\n'+ str(v1) +'\n')
    
    # MakeFolder = MakeFolder
    if sel == 'MakeFolder':
        # 查 文件夾 在否       ./NOW
        folder = os.path.exists(v1)
        if not folder:
            os.makedirs(v1)    # makedirs　文件夾不在创，在ＥＲＲＯＲ
            print ("\n*** 成功创建文件夾 ",v1," ***\n")

            #_AutoWebLanguageSetting("\n***!!成功创建文件夾!!!!!*****\n")
            #print (Talk0,LanguageText,v1)








###################################################################################
######################################################### 獲取檔案路徑和當前工作目錄
# https://www.delftstack.com/zh-tw/howto/python/python-get-path/

def _GetFolder():
    # print ('_GetFolder')
    NowFolder = (os.path.dirname(os.path.abspath(__file__)))

    #print ('_GetFolder,',NowFolder)
    return NowFolder










###################################################################################
############################################################# 在當前文件夾创工作目錄
def _MakeJobFolder(FolderName): 
    # 要創的文件夾名 = FolderName

    # 獲取當前工作目錄
    NowFolder = _GetFolder()

    # 文件夾 全名
    NowJobFolder = NowFolder + '\\' + FolderName

    # 创文件夾 if 冇
    _SetFolder(NowJobFolder,'MakeFolder')

    return NowJobFolder




if __name__ == "__main__":
    README()
    
    


