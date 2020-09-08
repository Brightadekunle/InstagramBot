import time
from bs4 import BeautifulSoup as b
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        website = 'https://www.instagram.com/'
        driver.get(website)
        driver.maximize_window() 
        driver.implicitly_wait(5)

        username =  driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

        driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()


    def LikeandComment(self, hashtag, comment):
        driver = self.driver
        self.login()
        site = 'https://www.instagram.com/explore/tags/' + hashtag + '/'
        driver.get(site)

        for i in range(1, 2):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(2)
            
        hrefs = driver.find_elements_by_tag_name('a')
        pictureHrefs = [elem.get_attribute('href') for elem in hrefs]


        for picture_link in pictureHrefs:
            driver.get(picture_link)

            driver.find_element_by_xpath('//*[contains(@aria-label,"Like")]').click()

            # To enable Comment box
            driver.find_element_by_xpath('//*[contains(@aria-label, "Add a comment…")]').click()
            commentSpace = driver.find_element_by_xpath('//*[contains(@aria-label, "Add a comment…")]')



            commentSpace.send_keys(comment)
            commentSpace.send_keys(Keys.ENTER)

    
    def follow(self, user):
        driver=self.driver
        self.login()
        users_page = 'https://www.instagram.com/' + user + '/'
        driver.get(users_page)

        follow_button = driver.find_element_by_xpath('//button[contains(text(), "Follow")]')
        follow_button.click()


    def unfollow(self, user):
        driver=self.driver
        self.login()
        users_page = 'https://www.instagram.com/' + user + '/'
        driver.get(users_page)

        to_unfollow_button = driver.find_element_by_xpath('//*[contains(@aria-label, "Following")]')
        to_unfollow_button.click()

        unfollow_button = driver.find_element_by_xpath('//button[contains(text(), "Unfollow")]')
        unfollow_button.click()

    
    def CloseBrowser(self):
        time.sleep(5)
        self.driver.close()

  

username = input('Enter username: ')
password = input('Enter password: ')

if __name__ == '__main__':
    get = InstagramBot(username, password)
    # get.follow(user)
    # get.unfollow(user)
    # get.LikeandComment('iloveJesus', 'I Love Jesus!')
    # get.CloseBrowser()
    