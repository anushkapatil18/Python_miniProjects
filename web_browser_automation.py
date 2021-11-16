from selenium import webdriver

class Music:
    def __init__self(self):
        self.driver = webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32")

    def play(self):
        name = input('enter a youtuber name     ')
        self.driver.get("https://www.youtube.com/user/"+name+"videos")
        a = self.driver.find_element_by_xpath('//*[@id="thumbnail"]')
        a.click()

bot = Music()
bot.play()