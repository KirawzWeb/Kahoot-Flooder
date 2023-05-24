from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import random
import threading
from colorama import Fore, init

os.system("cls")
os.system('title Disckid ^| by KirawzWeb')

code = input("Enter Code: ")
usr = input("Enter Username: ")
bot_count = int(input("Enter Bot Count: "))


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

def join_game(username, game_code):
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        os.system("cls")
        driver.get("https://kahoot.it/")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div[3]/div[2]/main/div/form/input").send_keys(game_code)
        time.sleep(0.7)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div[3]/div[2]/main/div/form/button").click()
        time.sleep(0.7)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[3]/div[2]/main/div/form/input").send_keys(username)
        time.sleep(0.7)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div[3]/div[2]/main/div/form/button").click()
        time.sleep(0.1)
        print(Fore.GREEN + f'    [+] {username} joined !')
        time.sleep(9999)
    except Exception as e:
        print(Fore.RED + f'    [-] {username} failed !')

threads = []

for i in range(bot_count):
    username = usr+'-'+str(random.randint(0, 9999999))
    thread = threading.Thread(target=join_game, args=(username, code))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
