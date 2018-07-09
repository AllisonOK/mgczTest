from appium import webdriver

desired_caps = {}

desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "8.0.0"
desired_caps["deviceName"] = "SHARP FS8010"

desired_caps["appPackage"] = "com.zsl.dream.fruit"
desired_caps["appActivity"] = ".main.StartActivity"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
