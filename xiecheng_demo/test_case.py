
from pyse import Pyse, TestCase, TestRunner
from parameterized import parameterized
import os


class Test(TestCase):
    """Baidu serach test case"""

    @classmethod
    def setUpClass(cls):
        """ Setting browser driver, Using chrome by default."""
        cls.driver = Pyse("chrome")
        cls.timeout = 15  # You can customize timeout time


    def login(self):
        self.open("https://www.ctrip.com/")
        self.max_window()
        self.sleep(5)
        self.click("xpath=> //*[@id='nav-bar-set-login']/a/span/span")
        self.type("id=>nloginname","15726626806")
        self.type("id=>npwd","13148023l")
        self.sleep(5)
        self.click("id=>nsubmit")
    #火车票
    def test_AssetManagement(self):
        Test.login(self)
        self.click("id=>nav_trains")
#        self.click("link_text=>资产管理")
 #       self.click("link_text=
        self.clear("id=>notice01")
        self.type("id=>notice01","北京")
        self.sleep(2)
        self.clear("id=>notice02")
        self.type("id=>notice02","邯郸")
        self.sleep(2)
        js = "document.getElementById('dateObj').removeAttribute('readonly')"#去掉readonly
        self.datainpt(js)
        self.clear("id=>dateObj")
        self.sleep(5)
        js2 = "document.getElementById('dateObj').value='2019-12-25'"
        self.datainpt(js2)
        self.sleep(2)
        self.click("id=>searchbtn")
        self.sleep(5)
if __name__ == '__min__':
    runner = TestRunner('./', '携程网站', '测试环境：Chrome')
    runner.run()

'''
说明：
'./' ： 指定测试目录。
'百度测试用例' ： 指定测试项目标题。
'测试环境：Chrome' ： 指定测试环境描述。

debug() # debug模式不生成测试报告
run()   # run模式生成测试报告
'''

