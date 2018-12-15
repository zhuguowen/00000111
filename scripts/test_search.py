import os
import sys
sys.path.append(os.getcwd())


import pytest
from base.get_driver import get_driver
from page.page_search import PageSearch


class TestSearch():


    def setup_class(self):
        self.serach=PageSearch(get_driver())
    def teardown_class(self):
        self.serach.driver.quit()

    @pytest.mark.parametrize("text", ["123"])
    def test_search(self,text):
        search = self.serach
        search.page_click_search_btn()
        search.page_input_text(text)
        search.page_click_back_btn()
