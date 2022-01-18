class SideBar():
    def __init__(self):
        self.menuButton = 'com.ajaxsystems:id/menuDrawer'
        self.menuClass = 'android.widget.RelativeLayout'

    def get_menu_button(self):
        return self.menuButton

    def get_menu_class(self):
        return self.menuClass
