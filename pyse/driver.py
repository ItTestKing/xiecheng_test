from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def Pyse(browser):
    """
    Run class initialization method, the default is proper
    to drive the Firefox browser. Of course, you can also
    pass parameter for other browser, Chrome browser for the "Chrome",
    the Internet Explorer browser for "internet explorer" or "ie".
    option = webdriver.ChromeOptions()
    """
    option = webdriver.ChromeOptions() #隐藏谷歌提示：“浏览器正受自动化软件控制”
    option.add_argument('disable-infobars')
    if browser == "firefox" or browser == "ff":
        return webdriver.Firefox()
    elif browser == "chrome":
        return webdriver.Chrome(chrome_options = option,desired_capabilities = None)
    elif browser == "internet explorer" or browser == "ie":
        return webdriver.Ie()
    elif browser == "opera":
        return webdriver.Opera()
    elif browser == "chrome_headless":
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        return webdriver.Chrome(chrome_options=chrome_options)
    elif browser == 'edge':
        return webdriver.Edge()
    else:
        raise NameError(
                "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'edge', 'chrome' or 'chrome_headless'." % browser)
