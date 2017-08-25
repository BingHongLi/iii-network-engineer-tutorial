# -*- coding: utf-8 -*-

import os

# 取得當前所在路徑
# Output String
os.getcwd()

# 創造資料夾
# Output Unit
os.mkdir('testDir')

# 新建檔案
# https://www.tutorialspoint.com/python/os_open.htm
#file1 = os.open('testDir/test.txt', os.O_CREAT )
file1= open('testDir/test.txt','w')
file1.write('dsad')

# 關閉檔案
# Output Unit
file1.close()

# 刪除資料夾與檔案
# 刪除裡面檔案之後，再刪除資料夾
