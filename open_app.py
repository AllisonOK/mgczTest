from appium import webdriver

# server 启动参数
desired_caps = {}

# 设备信息
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "8.0.0"
desired_caps["deviceName"] = "SHARP FS8010"
# app信息
desired_caps["appPackage"] = "com.zsl.dream.fruit"
desired_caps["appActivity"] = ".main.StartActivity"

# 声明手机驱动对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#<?xml version="1.0" encoding="UTF-8"?>
# <hierarchy rotation="0">
# <android.widget.FrameLayout index="0" text="" class="android.widget.FrameLayout" package="com.zsl.dream.fruit" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,121][1080,1920]" resource-id="" instance="0"><android.widget.LinearLayout index="0" text="" class="android.widget.LinearLayout" package="com.zsl.dream.fruit" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,121][1080,1920]" resource-id="" instance="0"><android.widget.FrameLayout index="0" text="" class="android.widget.FrameLayout" package="com.zsl.dream.fruit" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,121][1080,1920]" resource-id="android:id/content" instance="1"><android.widget.RelativeLayout index="0" text="" class="android.widget.RelativeLayout" package="com.zsl.dream.fruit" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,121][1080,1920]" resource-id="" instance="0"><android.widget.ImageView index="0" text="" class="android.widget.ImageView" package="com.zsl.dream.fruit" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,121][1080,1920]" resource-id="com.zsl.dream.fruit:id/image" instance="0"/></android.widget.RelativeLayout></android.widget.FrameLayout></android.widget.LinearLayout><android.widget.FrameLayout index="1" text="" class="android.widget.FrameLayout" package="com.zsl.dream.fruit" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,1920][1080,2040]" resource-id="android:id/navigationBarBackground" instance="2"/></android.widget.FrameLayout></hierarchy>

print(driver.page_source)

# 退出驱动对象
# driver.quit()
