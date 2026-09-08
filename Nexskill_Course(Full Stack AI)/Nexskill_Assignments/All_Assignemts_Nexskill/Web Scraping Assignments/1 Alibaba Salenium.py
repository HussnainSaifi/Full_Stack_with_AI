from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import os

driver = webdriver.Chrome()
driver.get("https://www.alibaba.com/trade/search?SearchText=mobile")

time.sleep(10)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

data = []

items = driver.find_elements(By.CSS_SELECTOR, "div[data-spm]")

print("Found items:", len(items))

for item in items:
    try:
        lines = item.text.split("\n")

        # Name
        name = lines[0] if len(lines) > 0 else "N/A"

        # Price
        price = "N/A"
        for line in lines:
            if "$" in line or "USD" in line:
                price = line
                break

        # Links
        try:
            link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        except:
            link = "N/A"

        # clean condition
        if name != "N/A" and len(name) > 3:
            data.append({
                "name": name,
                "price": price,
                "link": link
            })

    except:
        continue

driver.quit()

# save
folder = r"C:/Users/Hussnain Saifi/Documents/GitHub/CLass-3/All_Assignemts/Web Scraping Assignments/alibaba.csv"

with open(folder, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, ["name", "price", "link"])
    writer.writeheader()
    writer.writerows(data)

print("Total products:", len(data))