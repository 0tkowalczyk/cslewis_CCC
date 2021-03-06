#!/usr/bin/kivy

# all necessary imports
import random 
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

kivy.require('1.7.2')

# creating screen manager
formatting = """
<MyScreenManager>:
    IntroScreen:
    SaveScreen:
    MainScreen:

# creating first screen   
<IntroScreen>:
    name: 'intro'    
    BoxLayout:
        orientation: 'horizontal'        
        Label:
            text: root.directions
            font_size: 25            
        TextInput:
            id: potential_save
            font_size: 25            
        Button:
            text: 'Start'
            on_press: root.load_or_start_new(potential_save.text)
 
# creating second screen             
<SaveScreen>:
    name: 'save'
    BoxLayout:
        orientation: 'horizontal'
        Label:
            id: instr
            size: self.texture_size
            text: root.MainText
        TextInput:
            id: name
            font_size: 25
        Button:
            text: 'Enter your name'
            on_press: root.createInfo

# creating third screen              
<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'horizontal'
        BoxLayout:
            orientation: 'vertical'
            Label:
                id: display
                text: root.display
            Button:
                text: 'Upgrade your pickaxe (up to 10 times)'
                on_press: root.upgradePick(1)
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: 'Mine Stone'
                on_press: root.addMoney(1,1)
            Button:
                text: 'Mine Coal'
                on_press: root.addMoney(3,3)
            Button:
                text: 'Mine Iron'
                on_press: root.addMoney(5,5)
            Button:
                text: 'Mine Gold'
                on_press: root.addMoney(10,10)
            Button:
                text: 'Mine Diamonds'
                on_press: root.addMoney(20,20)

"""
Builder.load_string(formatting)


# creating stats and functions
class CharacterInfo:

    def __init__(self, money=0, tier=1, multiplier=1, pickCounter=0, pickCost = 10):
        self.money: int = money
        self.name: str = ""
        self.tier = tier
#storing values to keep track of current pickaxe multiplier, how many have already been bought, and the cost of the next one
        self.multiplier = multiplier
        self.pickCounter = pickCounter
        self.pickCost = pickCost

    def create_from_save(self):
        pass

    def importSaveData(self):
        pass

    def setName(self, name=""):
        self.name = name

    def incrementMoney(self, amount=1, odds=1):
# allows money to only be incremented on certain random occasions
        if random.randint(1,odds) =1:
            self.money = self.money + amount * self.multiplier
        pass
    
    def changeMultiplier(self, amount):
#checks if they have the money and if they have upgrades left, if so, changes the multiplier
        if self.money > pickCost:
            if self.pickCounter < 10:
                self.multiplier = self.multiplier + amount
                self.pickCounter = self.pickCounter +1
                self.pickCost = self.pickCost * self.multiplier
        pass

    def __str__(self):
        return str(
            "\n" + "Money: $" + str(self.money)
        )


class MyScreenManager(ScreenManager, Widget):
    data = ObjectProperty(CharacterInfo)


# first screen’s functions
class IntroScreen(Screen):
    directions = StringProperty(str('''
    Welcome, this is the unlicensed Minecraft clicker!
    Click the buttons to mine. Each button has a different success rate, the higher the rate, the lower the payout. Upgrade your pickaxe to increase your payout. That’s all there is to it, good luck!
    '''))

    def load_or_start_new(self, savedata=''):
        if savedata != '':
            self.loadOld(savedata)
        else:
            self.createNew()
        pass

    def loadOld(self, data):
        self.manager.current = 'save'
        pass

    def createNew(self):
        self.manager.current = 'save'
        pass

    pass


# second screen’s functions
class SaveScreen(Screen):
    MainText = StringProperty(str('''
    What is your name?
    '''))

    secondText = StringProperty(str('''
    You need a name to play, what is yours?
    '''))

    data_stats: CharacterInfo = ObjectProperty(CharacterInfo)

    def createInfo(self, username):
        if username != '':
            self.data_stats = CharacterInfo()
            self.data_stats.setName(username)
            self.manager.get_screen('main').display = str(self.data_stats)
            self.manager.current = 'main'
        else:
            self.MainText = self.secondText
        pass
    pass


# third screen’s functions
class MainScreen(Screen):

    def get_data(self) -> CharacterInfo:
        return self.manager.get_screen('save').data_stats

    display = StringProperty("IF THIS IS SHOWING SOMETHING WENT WRONG")

    def addMoney(self, amount, odds):
        stats: CharacterInfo = self.get_data()
        stats.incrementMoney(amount, odds)
        self.display = str(stats)

    def upgradePick(self, amount):
        stats: CharacterInfo = self.get_data()
        stats.changeMultiplier(amount)

class OurApp(App):

    def build(self):
        return MyScreenManager()


# This should start the app
if __name__ == '__main__':
    OurApp().run()
