# hotpoor_douyin_autoclick
hotpoor_douyin_autoclick

## 安卓手机准备
1、ADB Keyboard：[ADBKeyBoard](https://github.com/senzhk/ADBKeyBoard)

2、APK下载地址：[ADB Keyoard.apk](https://github.com/senzhk/ADBKeyBoard/blob/master/ADBKeyboard.apk)

3、手机设置-开发者模式-USB调试-显示屏幕位置（能看到坐标）

## 电脑准备
1、编程语言：[Python](https://www.python.org/)

2、命令行自动化工具：[ADB Platform](https://developer.android.com/tools/releases/platform-tools)

3、屏幕同步工具：[scrcpy](https://github.com/Genymobile/scrcpy)

4、设置全局变量确保 adb 和 scrcpy 两个命令式全局的

## 操作步骤
1、安卓手机插上数据线连电脑

2、电脑端打开命令行工具
```
# 获取设备ID
adb devices

# 获取屏幕投屏 -s 是用来加设备编号 -m是用来指定屏幕高度 不加参数 全尺寸画面太大 影响传输速度
scrcpy -s 设备ID -m 1024
```
3、打开抖音，搜索【助力新人直播间】

4、手机输入法设置【ADB Keyboard】

5、重新进入抖音页面直播间

6、配置屏幕坐标位置进入代码

7、运行代码
```
python XXX.py
```


