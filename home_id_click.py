from appium import webdriver
import time

# server 启动参数
from selenium.webdriver.common.by import By

desired_caps = {}

# 设备信息
# desired_caps["platformName"] = "Android"
# desired_caps["platformVersion"] = "8.0.0"
# desired_caps["deviceName"] = "SHARP FS8010"

desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "7.0"
desired_caps["deviceName"] = "QMKNW17513007051"

# {"platformName":"Android","platformVersion":"7.0","deviceName":"QMKNW17513007051","appPackage":"com.zsl.dream.fruit","appActivity":".main.StartActivity"},"platformName":"Android","platformVersion":"7.0","deviceName":"QMKNW17513007051","appPackage":"com.zsl.dream.fruit","appActivity":".main.StartActivity","deviceUDID":"QMKNW17513007051","deviceScreenSize":"1080x1920","deviceModel":"PRA-TL10","deviceManufacturer":"HUAWEI"}

# app信息
desired_caps["appPackage"] = "com.zsl.dream.fruit"
desired_caps["appActivity"] = ".main.StartActivity"

# 声明手机驱动对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

#等待20秒
time.sleep(10)

driver.find_element_by_id("com.zsl.dream.fruit:id/ly_fourth").click()

time.sleep(10)

# if driver.find_element_by_id()

# driver.quit()