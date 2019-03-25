# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2019/03/25 QTAF自动生成

from hq2lib.testcase import Hq2TestCase

class HelloTest(Hq2TestCase):
    '''示例测试用例
    '''
    owner = "root"
    timeout = 5
    priority = Hq2TestCase.EnumPriority.High
    status = Hq2TestCase.EnumStatus.Design
    
    def run_test(self):
        self.log_info("hello testcase")
        self.assert_equal(True, True)
    
if __name__ == '__main__':
    HelloTest().debug_run()

