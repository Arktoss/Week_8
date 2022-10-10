from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
import threading
def BIGvote():
    def bigvote():
        web = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # opens google.
        web.get("https://forms.gle/vA1pUXvkb7MS1F8J9")
        wait = WebDriverWait(web, 2)
        # email path:
        # /html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input
        # name path:
        # /html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input
        # vote
        # /html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label
        # sub
        # /html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span
        def VOTING():
            wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")))
            emq = web.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
            nameq = web.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            VOTE = web.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label")
            submit = web.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

            emq.send_keys("brdek_adam@student.mahoningctc.com")
            nameq.send_keys("Brdek, Adam")
            VOTE.click()
            submit.click()
            web.refresh()
            VOTING()

        while(True):
            VOTING()
    t1 = threading.Thread(target = bigvote)
    t2 = threading.Thread(target = bigvote)
    t3 = threading.Thread(target = bigvote)
    t4 = threading.Thread(target = bigvote)
    t5 = threading.Thread(target = bigvote)
    t6 = threading.Thread(target = bigvote)
    t7 = threading.Thread(target = bigvote)
    t8 = threading.Thread(target = bigvote)
    t9 = threading.Thread(target = bigvote)
    t10 = threading.Thread(target = bigvote)


    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()

bt1 = threading.Thread(target = BIGvote)
bt2 = threading.Thread(target = BIGvote)
bt3 = threading.Thread(target = BIGvote)
bt4 = threading.Thread(target = BIGvote)

bt1.start()
bt2.start()
bt3.start()
bt4.start()