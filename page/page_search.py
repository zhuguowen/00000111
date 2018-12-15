from base.base1 import Base


class PageSearch(Base):
    def page_input_username(self,username):
        self.base_input(,username)

    def page_input_pwd(self,pasword):
        self.base_input(loc_pwd,pasword)

    def page_click_login_btn(self):
        self.base_click(loc).click