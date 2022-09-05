import sys
import os
import time
import random

# step1 已经打开了抖音
# step2 已经访问了兔子178（涨粉直播间）
# 开始跑同样的话术

message_list = [
    "诚信交友，大家好，我夏力维，十年Python工程师，现在自己重新抖音起步，期待和大家共勉！",
    "诚信交友，诚信交友，诚信交友，诚信交友，诚信交友，诚信交友，诚信交友，我是夏力维。",
    "诚信交友，遭遇裁员，只能自己出来干，已三十岁，人生期待新征程。",
    "诚信交友，一起涨粉，我会持续关注大家，不太会用手机小屏幕，速度偏慢望谅解！",
]

def adb_tap(x,y,sleep=0):
    cmd_str = "adb shell input tap %s %s"%(x,y)
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)
def adb_swipe(x,y,x1,y1,t=1000,sleep=0):
    cmd_str = "adb shell input swipe %s %s %s %s %s"%(x,y,x1,y1,t)
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)
def adb_send_message(message,sleep=0):
    cmd_str = "adb shell am broadcast -a ADB_INPUT_TEXT --es msg '%s'"%message
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)

send_times = 100
for i in range(0,send_times):
    print("第%s次发送"%i)
    adb_tap(317,2270,1)
    current_message = int(random.random()*10%4)
    adb_send_message(message_list[current_message],1)
    adb_tap(1005,2238,1)
