import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from mclient.database import Database

class SettingsPage:
    def __init__(self,app) -> None:
        self.app=app
        self.db=Database()
        self.load_settings()
    
    def get_content(self):
        box=toga.Box(style=Pack(direction=COLUMN))
        box.add(toga.Label('Settings',style=Pack(padding=(10,0))))
        
        self.option1=toga.Switch("Option 1",on_change=self.option_changed)
        self.option1.value=self.current_option1
        box.add(self.option1)
        
        back_button=toga.Button("Back to Main",on_press=self.go_back)
        box.add(back_button)
        
        return box
    
    def load_settings(self):
        settings=self.db.fetch_settings()
        if settings:
            self.current_option1=settings[0][1]
        else:
            self.current_option1=False # default
            
    def option_changed(self,widget):
        self.db.insert_setting(widget.value)  # 改为使用 widget.value
        print(f"Option 1 is now: {widget.value}")
    
    
    def go_back(self,widget):
        self.app.show_main()
    def __del__(self):
        self.db.close()