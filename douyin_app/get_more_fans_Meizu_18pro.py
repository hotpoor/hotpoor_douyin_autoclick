import sys
import os
import time
import random

# step1 已经打开了抖音
# step2 已经访问了兔子178（涨粉直播间）
# 开始跑同样的话术

device_id = "abc08d7d"
comment_x = 82
comment_y = 2273
send_x = 977
send_y = 2097

message_list = [
    "诚信交友，大家好，我十年Python工程师，现在自己重新起步，期待和大家共勉！",
    "诚信交友，诚信交友，诚信交友，诚信交友，诚信交友，诚信交友，诚信交友，我是夏力维",
    "诚信交友，遭遇裁员，只能自己出来干，已三十岁，人生期待新发展",
    "诚信交友，一起涨粉，我会持续关注大家，不太会用手机小屏幕，速度偏慢望谅解",
    "诚信交友，互关互关，相互扶持，777777777777",
    "诚信交友，互关互关，我是活粉，今日有票",
]

def adb_tap(x,y,sleep=0):
    cmd_str = "adb -s %s shell input tap %s %s"%(device_id,x,y)
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)
def adb_swipe(x,y,x1,y1,t=1000,sleep=0):
    cmd_str = "adb -s %s shell input swipe %s %s %s %s %s"%(device_id,x,y,x1,y1,t)
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)
def adb_send_message(message,sleep=0):
    cmd_str = "adb -s %s shell am broadcast -a ADB_INPUT_TEXT --es msg '%s'"%(device_id,message)
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)

send_times = 100
for i in range(0,send_times):
    print("第%s次发送"%i)
    adb_tap(comment_x,comment_y,1)
    current_message = int(random.random()*10%len(message_list))
    # current_message = int(i%len(message_list))
    adb_send_message(message_list[current_message],1)
    adb_tap(send_x,send_y,2)
