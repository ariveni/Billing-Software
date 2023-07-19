from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
df = pd.read_csv("payment.csv")



s=Service("D:\\selenium_scripts\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("provide website url")

driver.find_element("name","unme").send_keys("username")


driver.find_element("id","password").send_keys("password")


driver.find_element("id","logn_submt").click()

driver.find_element(By.XPATH,"//html/body/div[2]/aside/div/ul/li[3]/a/span[1]").click()

for i in df["Username"]:
    driver.find_element(By.XPATH,"//html/body/div[2]/aside/div/ul/li[3]/ul/li[1]/a").click()
    driver.find_element("name","id_b2929032").send_keys(i)
    driver.find_element(By.XPATH,"//html/body/div[2]/section/section/form/div/div/div/div[1]/div[3]/button").click()
    driver.find_element(By.XPATH,"//html/body/div[2]/section/section/div/div[2]/div/div[2]/table/tbody/tr/th/div/button").click()
    driver.find_element(By.XPATH,"//html/body/div[2]/section/section/div/div[2]/div/div[2]/table/tbody/tr/th/div/ul/li[2]/a").click()
    driver.find_element(By.XPATH,"//html/body/div[2]/section/section/div/div/div/div[3]/div/div[1]/div[1]/div[2]/div/div/form/table/tbody/tr[8]/td[2]/input").click()
    driver.find_element(By.XPATH,"//html/body/div[2]/section/section/div/div/div/div[3]/div/div[1]/div[1]/div[2]/div/div/form/table/tbody/tr[8]/td[2]/select").click()
    driver.find_element(By.XPATH,"//html/body/div[2]/section/section/div/div/div/div[3]/div/div[1]/div[1]/div[2]/div/div/form/table/tbody/tr[8]/td[2]/select/option[2]").click()
    driver.find_element(By.XPATH,"//html/body/div[2]/section/section/div/div/div/div[3]/div/div[1]/div[1]/div[2]/div/div/form/table/tbody/tr[17]/td[2]/input").click()
driver.quit()

