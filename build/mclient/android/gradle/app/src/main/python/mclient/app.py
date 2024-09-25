import sys
import os
import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from mclient.pages.settings import SettingsPage

# 确保可以找到 pages 模块
sys.path.insert(0, os.path.dirname(__file__))
from . import Config

class MainApp(toga.App):
    def startup(self) :
        self.main_window=toga.MainWindow(title=self.formal_name)
        self.main_box=toga.Box(style=Pack(direction=COLUMN))
        
        self.page1_button=toga.Button("Go to Page 1",on_press=self.open_page1)
        self.settings_button=toga.Button("Settings",on_press=self.open_settings)
        
        self.main_box.add(self.page1_button)
        self.main_box.add(self.settings_button)
        
        self.main_window.content=self.main_box
        self.main_window.show()
    
    def open_page1(self,widget):
        self.main_window.content=toga.Label("This is Page 1", style=Pack(padding=(10, 0)))
        
    def open_settings(self,widget):
        self.main_window.content=SettingsPage(self).get_content()
    
    def show_main(self):
        self.main_window.content=self.main_box
    







class HelloM(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.label2=Label(Config().version)
        self.label=Label("Check for updates...")
        self.check_for_updates('1.0.0')
        self.main_box.add(self.label2)
        self.main_box.add(self.label)
        self.main_window.content = self.main_box
        self.main_window.show()

    
    def check_for_updates(self,current_version):
        try:
            response=requests.get("https://mpi.cpolar.top/latest-version")
            latest_version=response.json()['version']
            
            if latest_version>current_version:
                self.label.text=f"New version {latest_version} available!"
                self.prompt_update(latest_version)
            else:
                self.label.text="You are using the lastest version."
        except Exception as e:
            self.label.text='Failed to check for updates'
            print(f"Error:{e}")
        
    
    def prompt_update(self,lastest_version):
        self.label.text+=f"\nWould you like to update to version {lastest_version}?"
        #alert = Alert('Update Available', f'New version {latest_version} is available. Would you like to update?')
        #alert.show()
        

def main():
    #return HelloM()
    return MainApp()
