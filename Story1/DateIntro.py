
# Unix time
# datetime 操作
# http://tool.chinaz.com/Tools/unixtime.aspx
# http://www.ithome.com.tw/voice/106285
"""
我們取用時間
"""
# 預設為utc時間
import datetime
nowUtcUnixTime = datetime.datetime.utcnow().timestamp()
print(nowUtcUnixTime)

# 轉換成整數
print(int(nowUtcUnixTime))


nowLocalUnixTime = datetime.datetime.now().timestamp()
print(int(nowLocalUnixTime))


gmt8Second = int(nowLocalUnixTime)-int(nowUtcUnixTime)
print(gmt8Second)
print(gmt8Second/3600)

#import pytz

