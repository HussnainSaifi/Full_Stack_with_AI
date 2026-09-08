from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

url = "https://www.amazon.com/s?k=mobile"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(8)

data = []

items = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

print("Found items:", len(items))

for item in items:
    try:
        # Name
        try:
            name = item.find_element(By.XPATH, ".//h2").text
        except:
            name = "N/A"

        # Price
        try:
            price = item.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
        except:
            price = "N/A"

        # Rating
        try:
            rating = item.find_element(By.XPATH, ".//span[contains(@class,'a-icon-alt')]").text
        except:
            rating = "N/A"

        # Link
        try:
            link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        except:
            link = "N/A"

        # save
        if name != "N/A":
            data.append({
                "name": name[:60],
                "price": price,
                "rating": rating,
                "link": link
            })

    except:
        continue

driver.quit()

# csv
filename = r"All_Assignemts/Web Scraping Assignments/amazon.csv"

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, ["name", "price", "rating", "link"])
    writer.writeheader()
    writer.writerows(data)

print("Total products:", len(data))