import json
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

Window.size = (400, 700)

kv = """

MDScreenManager:
    HomeScreen:
    Main:
    PipScreen:
    PriceInfo:

<HomeScreen>:
    name:'menu'
    MDRectangleFlatIconButton:
        text: "WELCOME"
        icon: "distribute-horizontal-center"
        line_color: 0, 0, 0, 0
        pos_hint: {"center_x": .5, "center_y": .5}
        font_size: 55
        # font_name: "branda.ttf"

    MDIconButton:
        icon: "location-enter"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: 
            root.manager.current = 'tab'
            root.manager.transition.direction = "left"
    MDLabel:
        text: "REMEMBER TO ALWAYS BE HUMBLE!!"
        halign: "center"
        pos_hint: {'center_y': 0.1}
        font_size: 20


<Main>:
    name: 'tab'

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "TRADE-AI"
            anchor_title: 'center'
            right_action_items:
                [["distribute-horizontal-center", lambda x : app.set_screen('calc')]]
            left_action_items:
                [["information-outline", lambda x : app.priceinfo('marketpriceinfo')]]


        MDTabs:
            id: tabs
            tab_hint_x: True
            on_tab_switch: root.on_tab_switch(*args)
            
            # NAS100
            Tab:
                title: "NAS100"
                MDTextField:
                    id: op
                    hint_text: "OPEN"
                    mode: "rectangle"
                    pos_hint: {"center_x": .5, "center_y": .9}
                    size_hint_x: 0.8
                    # width: 60

                MDTextField:
                    id: vl
                    hint_text: "VOLUME"
                    mode: "rectangle"
                    pos_hint: {"center_x": .5, "center_y": .75}
                    size_hint_x: 0.8
                    # width: 150

                MDTextField:
                    id: lo
                    hint_text: "LOW"
                    mode: "rectangle"
                    pos_hint: {"center_x": .5, "center_y": .60}
                    size_hint_x: 0.8
                    # width: 60

                MDTextField:
                    id: hi
                    hint_text: "HIGH"
                    mode: "rectangle"
                    pos_hint: {"center_x": .5, "center_y": .45}
                    size_hint_x: 0.8
                    # width: 150

                MDRaisedButton:
                    text: "SUBMIT"
                    pos_hint: {"center_x": .5, "center_y": .30}
                    on_release:  
                        app.my_func()
                    
                MDCard:
                    size_hint: None, None
                    size: "325dp", "80dp"
                    pos_hint: {"center_x": .5, "center_y": .15}
                    radius: 5
                    styles: "filled"
                    MDLabel:
                        text: ""
                        id: put_txt_here
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .6}
                        
    

                MDIconButton:
                    icon: "home"
                    icon_size: "40"
                    pos_hint: {"center_x": .8, "center_y": .05}
                    on_press:
                        root.manager.current = 'menu'
                        root.manager.transition.direction = "right"
                        
          
            # US30
            Tab:
                title: "US30"
                MDTextField:
                    id: o
                    hint_text: "OPEN"
                    mode: "rectangle"
                    pos_hint: {"center_x": .5, "center_y": .9}
                    size_hint_x: 0.8
                    # width: 150

                MDTextField:
                    id: v
                    hint_text: "VOLUME"
                    mode: "rectangle"
                    pos_hint: {"center_x": .5, "center_y": .75}
                    size_hint_x: 0.8
                    # width: 150

                MDTextField:
                    id: l
                    hint_text: "LOW"
                    mode: "rectangle"
                    pos_hint: {"center_x": .5, "center_y": .60}
                    size_hint_x: 0.8
                    # width: 150

                MDTextField:
                    id: h
                    hint_text: "HIGH"
                    mode: "rectangle"
                    pos_hint: {"center_x": .5, "center_y": .45}
                    size_hint_x: 0.8
                    # width: 150
                    
                MDRaisedButton:
                    text: "SUBMIT"
                    pos_hint: {"center_x": .5, "center_y": .30}
                    on_release:  
                        app.my_us30()
                    
                MDCard:
                    size_hint: None, None
                    size: "325dp", "80dp"
                    pos_hint: {"center_x": .5, "center_y": .15}
                    radius: 5
                    MDLabel:
                        text: ""
                        id: put_us30
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .6}


                MDIconButton:
                    icon: "home"
                    icon_size: "40"
                    pos_hint: {"center_x": .8, "center_y": .05}
                    on_press:
                        root.manager.current = 'menu'
                        root.manager.transition.direction = "right"
           
            # GER30
            Tab:
                title: "GER30"
                MDTextField:
                    id: op_1
                    hint_text: "OPEN"
                    mode: "rectangle"
                    pos_hint: {"center_x": .5, "center_y": .9}
                    size_hint_x: 0.8
                    # width: 150

                MDTextField:
                    id: vol_1
                    hint_text: "VOLUME"
                    mode: "rectangle"
                    pos_hint: {"center_x": .5, "center_y": .75}
                    size_hint_x: 0.8
                    # width: 150

                MDTextField:
                    id: lo_1
                    hint_text: "LOW"
                    mode: "rectangle"
                    pos_hint: {"center_x": .5, "center_y": .60}
                    size_hint_x: 0.8 
                    # width: 150

                MDTextField:
                    id: hi_1
                    hint_text: "HIGH"
                    mode: "rectangle"
                    pos_hint: {"center_x": .5, "center_y": .45}
                    size_hint_x: 0.8
                    # width: 150
                MDRaisedButton:
                    text: "SUBMIT"
                    pos_hint: {"center_x": .5, "center_y": .30}
                    on_release:  
                        app.my_ger30()
                        
                MDCard:
                    size_hint: None, None
                    size: "325dp", "80dp"
                    pos_hint: {"center_x": .5, "center_y": .15}
                    radius: 5
                    MDLabel:
                        text: ""
                        id: put_ger30
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .6}
    
    
                MDIconButton:
                    icon: "home"
                    icon_size: "40"
                    pos_hint: {"center_x": .8, "center_y": .05}
                    on_press:
                        root.manager.current = 'menu'
                        root.manager.transition.direction = "right"

<PipScreen>:
    name: 'calc'
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "Pip Calc"
            pos_hint: {'top': 1}
        MDTextField:
            id: input_dt
            halign: "right"
            valign: "bottom"
            font_size: 32
            multiline: True
            mode: "fill"
            pos_hint: {"center_x": .5, "center_y": .70}
            size_hint: 0.9, 0.5
            background_color: app.theme_cls.bg_normal
        MDGridLayout:
            cols: 4
            rows: 5
            padding: 15
            size: root.width, root.height
            MDFlatButton:
                id: C
                text: "%"
                font_size: 30
                size: 500, 200
                # md_bg_color: 1, 0, 0, 1
                size_hint: 1, 1
                on_press:
                    root.signs('%')
                
            MDFlatButton:
                id: C
                text: "C"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.clear()
                
            MDFlatButton:
                id: C
                text: u"\u00AB"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                # md_bg_color: 214/255, 43/255, 43/255
                on_press:
                    root.remove_last()
            
            MDFlatButton:
                id: C
                text: "/"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                md_bg_color: 64/255, 119/255, 201/255
                on_press:
                    root.signs('/')
                md_bg_radius: 0
                
            MDFlatButton:
                id: C
                text: "7"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(7)
            
            MDFlatButton:
                id: C
                text: "8"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(8)
                
            MDFlatButton:
                id: C
                text: "9"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(9)
            
            MDFlatButton:
                id: C
                text: "x"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                md_bg_color: 64/255, 119/255, 201/255
                md_bg_radius: -1
                on_press:
                    root.signs('*')
                            
            MDFlatButton:
                id: C
                text: "4"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(4)
            
            MDFlatButton:
                id: C
                text: "5"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(5)
            MDFlatButton:
                text: "6"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(6)
            
            MDFlatButton:
                id: C
                text: "-"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                md_bg_color: 64/255, 119/255, 201/255
                md_bg_radius: 0
                on_press:
                    root.signs('-')
                
            MDFlatButton:
                text: "1"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(1)
            
            MDFlatButton:
                id: C
                text: "2"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(2)
            MDFlatButton:
                id: C
                text: "3"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(3)
            
            MDFlatButton:
                id: C
                text: "+"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                md_bg_color: 64/255, 119/255, 201/255
                on_press:
                    root.signs('+')
                
            MDFlatButton:
                id: C
                text: "+/-"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.pos_neg()
            
            MDFlatButton:
                id: C
                text: "0"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(0)
            MDFlatButton:
                id: C
                text: "."
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press:
                    root.dot()
            
            MDFlatButton:
                id: C
                text: "="
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                md_bg_color: 64/255, 119/255, 201/255
                on_press:
                    root.results()
                
                
            
        MDIconButton:
            icon: "keyboard-backspace"
            icon_size: "40"
            pos_hint: {"center_x": .1, "center_y": .1}
            on_press:
                root.manager.current = 'tab'
                root.manager.transition.direction = "right"

<PriceInfo>:
    name: "marketpriceinfo"
    MDBoxLayout:
        orientation: "vertical"
        MDIconButton:
            icon: "arrow-up-drop-circle"
            icon_size: "40"
            pos_hint: {"center_x": .1, "center_y": .9}
            on_press:
                root.manager.current = 'tab'
                root.manager.transition.direction = "up"
                
        MDBottomNavigation:
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'NAS100'
                icon: "hand-coin-outline"
    
                MDCard:
                    size_hint: None, None
                    size: "325dp", "380dp"
                    pos_hint: {"center_x": .5, "center_y": .65}
                    radius: 5
                    MDLabel:
                        text: ""
                        id: nas100_price_info
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .6}
                MDRaisedButton:
                    text: "SUBMIT"
                    pos_hint: {"center_x": .5, "center_y": .25}
                    on_release:  
                        root.nas100info()
    
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'US30'
                icon: "hand-coin-outline"

    
                MDCard:
                    size_hint: None, None
                    size: "325dp", "380dp"
                    pos_hint: {"center_x": .5, "center_y": .65}
                    radius: 5
                    MDLabel:
                        text: ""
                        id: us30_price_info
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .6}
                MDRaisedButton:
                    text: "SUBMIT"
                    pos_hint: {"center_x": .5, "center_y": .25}
                    on_release:  
                        root.us30info()
    
            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'GER30'
                icon: "hand-coin-outline"
                
    
                MDCard:
                    size_hint: None, None
                    size: "325dp", "380dp"
                    pos_hint: {"center_x": .5, "center_y": .65}
                    radius: 5
                    MDLabel:
                        text: ""
                        id: ger30_price_info
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .6}
                MDRaisedButton:
                    text: "SUBMIT"
                    pos_hint: {"center_x": .5, "center_y": .25}
                    on_release:  
                        root.ger30info()
        
        
<Tab>:
    MDLabel:
        id: label
        halign: "center"

"""


class Tab(MDFloatLayout, MDTabsBase):
    pass


class HomeScreen(Screen):
    pass


class PriceInfo(Screen):

    def nas100info(self):
        div_classes = {'open': "js-symbol-open",
                       'volume': "js-symbol-volume",
                       'daily low': "js-symbol-header__range-price-l",
                       'daily high': "js-symbol-header__range-price-r"}

        base_url = 'https://www.tradingview.com/symbols/OANDA-NAS100USD/'
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        data = {}
        try:
            driver.get(base_url)
            WebDriverWait(driver, 30)

            header_container = driver.find_element(By.CLASS_NAME, 'js-header-fundamentals')
            for key, val in div_classes.items():
                element = header_container.find_element(By.CLASS_NAME, val)
                data[key] = element.text
                print("Great!!!!!")
            result = "Open: {}\nVolume: {}\nDaily low: {}\nDaily high: {}".format(
                data.get("open", ""),
                data.get("volume", ""),
                data.get("daily low", ""),
                data.get("daily high", ""))

            self.ids.nas100_price_info.text = result
        except Exception as e:
            print(e)
        finally:
            driver.close()

    def us30info(self):
        div_classes = {'open': "js-symbol-open",
                       'volume': "js-symbol-volume",
                       'daily low': "js-symbol-header__range-price-l",
                       'daily high': "js-symbol-header__range-price-r"}

        base_url = 'https://www.tradingview.com/symbols/OANDA-US30USD/'
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        data = {}
        try:
            driver.get(base_url)
            WebDriverWait(driver, 30)

            header_container = driver.find_element(By.CLASS_NAME, 'js-header-fundamentals')
            for key, val in div_classes.items():
                element = header_container.find_element(By.CLASS_NAME, val)
                data[key] = element.text
                print("Great!!!!!")
            result = "Open: {}\nVolume: {}\nDaily low: {}\nDaily high: {}".format(
                data.get("open", ""),
                data.get("volume", ""),
                data.get("daily low", ""),
                data.get("daily high", ""))

            self.ids.us30_price_info.text = result
        except Exception as e:
            print(e)
        finally:
            driver.close()

    def ger30info(self):
        div_classes = {'open': "js-symbol-open",
                       'volume': "js-symbol-volume",
                       'daily low': "js-symbol-header__range-price-l",
                       'daily high': "js-symbol-header__range-price-r"}

        base_url = 'https://www.tradingview.com/symbols/GLOBALPRIME-GER30/'
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        data = {}
        try:
            driver.get(base_url)
            WebDriverWait(driver, 30)

            header_container = driver.find_element(By.CLASS_NAME, 'js-header-fundamentals')
            for key, val in div_classes.items():
                element = header_container.find_element(By.CLASS_NAME, val)
                data[key] = element.text
                print("Great!!!!!")
            result = "Open: {}\nVolume: {}\nDaily low: {}\nDaily high: {}".format(
                data.get("open", ""),
                data.get("volume", ""),
                data.get("daily low", ""),
                data.get("daily high", ""))
            self.ids.ger30_price_info.text = result
        except Exception as e:
            print(e)
        finally:
            driver.close()


class PipScreen(Screen):
    def clear(self):
        self.ids.input_dt.text = '0'

    def bt_values(self, number):
        prev_number = self.ids.input_dt.text
        if 'Input Error Buddy' in prev_number:
            prev_number = ''
        if prev_number == '0':
            self.ids.input_dt.text = ''
            self.ids.input_dt.text = f'{number}'
        else:
            self.ids.input_dt.text = f'{prev_number}{number}'

    def signs(self, sing):
        prev_number = self.ids.input_dt.text
        self.ids.input_dt.text = f'{prev_number}{sing}'

    def remove_last(self):
        prev_number = self.ids.input_dt.text
        prev_number = prev_number[:-1]
        self.ids.input_dt.text = prev_number

    def results(self):
        prev_number = self.ids.input_dt.text
        try:
            result = eval(prev_number)
            self.ids.input_dt.text = str(result)
        except:
            self.ids.input_dt.text = 'Input Error Buddy'

    def pos_neg(self):
        prev_number = self.ids.input_dt.text
        if '-' in prev_number:
            self.ids.input_dt.text = f'{prev_number.replace("-", "")}'
        else:
            self.ids.input_dt.text = f'-{prev_number}'

    def dot(self):
        prev_number = self.ids.input_dt.text
        num_list = re.split("[+/*%-]", prev_number)
        if (
                "+" in prev_number or "-" in prev_number or "/" in prev_number or "*" in prev_number or "%" in prev_number) and "." not in \
                num_list[-1]:
            prev_number = f"{prev_number}."
            self.ids.input_dt.text = prev_number

        elif "." in prev_number:
            pass
        else:
            prev_number = f"{prev_number}."
            self.ids.input_dt.text = prev_number


class Main(Screen):
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <main.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

    # instance_tab.ids.label.text = tab_text

    # 'Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green',
    # 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray'


class TM(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.primary_palette = "Blue"
        self.icon = "logo.png"
        Builder.load_string(kv)

        sm = MDScreenManager()
        sm.add_widget(HomeScreen(name='menu'))
        sm.add_widget(Main(name='tab'))
        sm.add_widget(PipScreen(name='calc'))
        sm.add_widget(PriceInfo(name="marketpriceinfo"))
        return sm

    def set_screen(self, calc):
        self.root.current = calc

    def price_screen(self, price):
        self.root.current = price

    def priceinfo(self, markepriceinfo):
        self.root.current = markepriceinfo

        # For NAS100

    def my_func(self):
        open = self.root.get_screen("tab").ids.op.text
        volume = self.root.get_screen("tab").ids.vl.text
        high = self.root.get_screen("tab").ids.hi.text
        low = self.root.get_screen("tab").ids.lo.text
        link = f'https://trademavericks-api.herokuapp.com/nas100'
        data = {"open": open, "volume": volume, "low": low, "high": high}
        headers = {'Content-Type': 'application/json'}
        self.request = UrlRequest(url=link, req_headers=headers, on_success=self.func, method='POST',
                                  req_body=json.dumps(data))

    def func(self, *args):
        self.data = self.request.result
        ans = self.data
        print("Horray")
        self.root.get_screen('tab').ids.put_txt_here.text = ans["prediction"]

    # For US30

    def my_us30(self):
        open = self.root.get_screen("tab").ids.o.text
        volume = self.root.get_screen("tab").ids.v.text
        high = self.root.get_screen("tab").ids.h.text
        low = self.root.get_screen("tab").ids.l.text
        link = f'https://trademavericks-api.herokuapp.com/us30'
        data = {"open": open, "volume": volume, "low": low, "high": high}
        headers = {'Content-Type': 'application/json'}
        self.request = UrlRequest(url=link, req_headers=headers, on_success=self.us30, method='POST',
                                  req_body=json.dumps(data))

    def us30(self, *args):
        self.data = self.request.result
        ans = self.data
        print("Horray")
        self.root.get_screen('tab').ids.put_us30.text = ans["prediction"]

    #  For GER30

    def my_ger30(self):
        open = self.root.get_screen("tab").ids.op_1.text
        volume = self.root.get_screen("tab").ids.vol_1.text
        high = self.root.get_screen("tab").ids.hi_1.text
        low = self.root.get_screen("tab").ids.lo_1.text
        link = f'https://trademavericks-api.herokuapp.com/ger30'
        data = {"open": open, "volume": volume, "low": low, "high": high}
        headers = {'Content-Type': 'application/json'}
        self.request = UrlRequest(url=link, req_headers=headers, on_success=self.ger30, method='POST',
                                  req_body=json.dumps(data))

    def ger30(self, *args):
        self.data = self.request.result
        ans = self.data
        print("Workline")
        self.root.get_screen('tab').ids.put_ger30.text = ans["prediction"]


TM().run()
