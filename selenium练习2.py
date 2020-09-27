import unittest  # unittest提供框架去组织测试用例
from selenium import webdriver  # 提供WebDriver实现
from selenium.webdriver.common.keys import Keys  # 提供键盘操作


class PythonOrgSearch(unittest.TestCase):  # 继承TestCase模块告诉unittest该类是测试用例
    def setUp(self):  # 初始化
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):  # 测试用例
        driver = self.driver
        driver = webdriver.Chrome()  # 打开网站
        self.assertIn("Python", driver.title)  # assert方法判断页面标题中是否包含"Python"
        elem = driver.find_element_by_name("q")  # 找到属性name='p'的标签（测试id属性）
        elem.send_keys("pycon")  # 输入"pycon"
        elem.send_keys(Keys.RETURN)  # 点击进入
        assert "No results found." not in driver.page_source

        def tearDown(self):  # 关闭浏览器
            self.driver.close()


if __name__ == '__main__':
    unittest.main()



