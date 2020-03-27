# Discord Webhook That Sends a Message Every Time the MCD Stock Changes
from selenium import webdriver
import requests
import time

# Setup Selenium / ChromeDriver
discord_url = 'https://discordapp.com/api/webhooks/692607316725334127/5I12ORQsLsP7yzKBvoc1jABnDwjE7XksjVAXmFXLd2X8kk9B-NRS-mKcfxC1D1DgJD1x'
driver = webdriver.Chrome()
driver.get("https://www.tradingview.com/symbols/NYSE-MCD/")
chromedriver_path = r"C:\Users\suhpe\PycharmProjects\MCDStockPriceBot\chromedriver.exe"

# Wait for the page to open
time.sleep(2)
# Get current price of MCD stock
stock = driver.find_element_by_xpath(
    """/html/body/div[2]/div[4]/div/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]""")

# Setup for comparing prices
original = stock.text
new = original
newer = 0

# Save content for the bot to type
originalData = {
    "content": "Current McDonald's Stock is: $" + original + " USD"
}
# Make bot post message to discord
requests.post(discord_url, data=originalData)

# Main loop
while True:
    # Compare original to new, will always be true first time
    if original == new:
        # Get new stock price
        stock = driver.find_element_by_xpath(
            """/html/body/div[2]/div[4]/div/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]""")
        new = stock.text
        # Save content for the bot to type
        data = {
            "content": "Current McDonald's Stock is: $" + new + " USD"
        }
        # Refresh the page
        driver.refresh()
        time.sleep(2)
    if original != new:
        # Get new stock price
        stock = driver.find_element_by_xpath(
            """/html/body/div[2]/div[4]/div/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]""")
        # Force into last if statement (if newer == new)
        newer = stock.text
        new = stock.text
        # Save content for the bot to type
        data = {
            "content": "Current McDonald's Stock is: $" + newer + " USD"
        }
        # Post new stock price to discord
        requests.post(discord_url, data=data)
        time.sleep(2)
    if new == newer:
        # Force back into first if statement (if original == new)
        original = new