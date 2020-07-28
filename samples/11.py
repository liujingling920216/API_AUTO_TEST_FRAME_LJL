import selenium
import time
from appium import webdriver

des = {
    'platformName': 'Android',
    'platformVersion': '8.0',  #填写android虚拟机的系统版本
    'deviceName': 'Samsung Galaxy S8',   #填写安卓虚拟机的设备名称
    'appPackage': 'com.android.gallery3d',   #填写被测试包名
    'appActivity': 'com.android.gallery3d.app.GalleryActivity',    #填写被测试app入口
    'udid': '192.168.56.103:5555',  # 填写通过命令行 adb devices 查看到的 uuid（指定已连接在MAC上的虚拟机）
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', des)