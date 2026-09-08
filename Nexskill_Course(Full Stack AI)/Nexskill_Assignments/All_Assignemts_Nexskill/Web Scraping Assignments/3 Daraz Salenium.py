from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import re

url = "https://www.daraz.pk/catalog/?q=mobile"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(6)

data = []

items = driver.find_elements(By.CSS_SELECTOR, "div[data-qa-locator='product-item']")

for item in items:
    try:
        # Name
        try:
            name = item.find_element(By.TAG_NAME, "img").get_attribute("alt").strip()
            if name == "":
                raise Exception
        except:
            name = item.find_element(By.TAG_NAME, "a").text.strip()

        name = name[:50]

        # Price
        try:
            price = item.find_element(By.CLASS_NAME, "ooOxS").text.strip()
        except:
            price = "0"

        # Sold
        text = item.text.lower()
        match = re.search(r'([\d\.]+k?)\s*sold', text)

        if match:
            sold = match.group(1)
        else:
            sold = "0"

        # Clean
        if name != "" and price != "":
            data.append({
                "name": name,
                "price": price,
                "sold": sold
            })

    except:
        continue

driver.quit()

# CSV
filename = r"All_Assignemts/Web Scraping Assignments/Darazpk.csv"

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, ["name", "price", "sold"])
    writer.writeheader()
    writer.writerows(data)
