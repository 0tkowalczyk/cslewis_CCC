from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

formatting = """
<MyScreenManager>:
    <ButtonScreen>:
        BoxLayout: 
            orientation: 'vertical'
            Button:
                text: 'Read a Book'
                on_press: root.read_a_book()
                on_press: root.add_time(20)   
            Button:
                text: 'Workout'
                on_press: root.workout() 
                on_press: root.add_time(15)     
class PlayerStatistics:

    def __init__(self, strength=0, wisdom=0, time=0):
        self.time: int = time
        self.strength: int = strength
        self.wisdom: int = wisdom
        self.attributeDict = {"STR": self.strength, "WIS": self.wisdom}


    def increment_Strength(self, amount=1):
        self.strength = self.strength + amount

    def increment(self, parameter, amount=1):
        if self.attributeDict.__contains__(parameter):
            self.attributeDict[parameter] = self.attributeDict[parameter] + amount
        else:
            print("That Parameter does not exist")

    def increment_Wisdom(self, amount=1):
        self.wisdom = self.wisdom + amount
        pass

    def __str__(self):
        return str(
            "Name: " + self.name + "|" + "time: " + str(self.time)
            + "\n" + "Strength: " + str(self.strength)
            + "\n" + "Wisdom: " + str(self.wisdom)
        )

    def increment_Time(self, amount=1):
        self.time = self.time + amount
        pass


class MyScreenManager(ScreenManager, Widget):
    data = ObjectProperty(PlayerStatistics)

class ButtonScreen(Screen):

    def get_data(self) -> PlayerStatistics:
        return self.manager.get_screen('character').data_stats

    display = StringProperty("IF THIS IS SHOWING SOMETHING WENT WRONG")

    # StringProperty("Strength: " + str(Strength))

    def workout(self):
        stats: PlayerStatistics = self.get_data()
        stats.increment_Strength(1)
        self.display = str(stats)

    def read_a_book(self):
        stats: PlayerStatistics = self.get_data()
        stats.increment_Wisdom(1)
        self.display = str(stats)

    def add_time(self, amount):
        stats: PlayerStatistics = self.get_data()
        stats.increment_Time(amount)
        self.display = str(stats)


class GUIApp(App):

    def build(self):
        return MyScreenManager()


# Entry point into the game
if __name__ == '__main__':
    GUIApp().run()
