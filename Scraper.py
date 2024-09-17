from playwright.async_api import Playwright, async_playwright, expect, Page
import playwright
import json
import asyncio
import os
import sys
import time

game = input("Game Name: ")
sites_to_load= []
#expect.set_options(timeout = 10_000)


async def brower_loader(playwright: Playwright, url, target, title, price, site_url) -> None:
     async with async_playwright() as p:
    #p = await async_playwright().start()
        browser = await p.chromium.launch(headless=True) # launch new browser
        context = await browser.new_context()
        page = await context.new_page() # Open new page

        await page.goto(url+game)
        #print(url, target, title, price, site_url)
        await scraper(page, target, title, price, site_url)

        await context.close()
        await browser.close()
    #await async_playwright().stop()

async def scraper(page: Page, target: str, title_selector: str, price_selector: str, url_selector: str):
    scraped_elements = []


    items = await page.locator(target).element_handles()
    #print(items)
    for item in items:
        scraped_element = {}

        # Extract game title
        title_element = await item.query_selector(title_selector)
        #print(title_element)
        if title_element:
            game_title = await title_element.inner_text()
            scraped_element["title"] = game_title


        price_element = await item.query_selector(price_selector)
        #print(price_element)
        if price_element:
            game_price = await price_element.text_content()
            scraped_element["price"] = game_price

        url_element = await item.query_selector(url_selector)
        #print(url_element)
        if url_element:
            game_url = await price_element.text_content()
            scraped_element["url"] = game_url

        #scraped_elements.append(scraped_element)
        print(scraped_element)
    #await write_results(scraped_elements)
    #print(scraped_elements)
        #scraped_element.clear()
        #print(scraped_element)





async def load_data():
    #sites_to_load = []
    with open("sites.json") as json_file:
        data = json.load(json_file)
        data_length = len(data["site_to_compare"])
        for i in range(data_length):
            sites_to_load.append(data["site_to_compare"][i])
    #print(sites_to_load)
    #return sites_to_load

async def write_results(new_data, filename = "results.json"):

    seed = {"results" : []}

    if not os.path.isfile(filename):
        with open(filename, mode='w', encoding='utf-8') as file:
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["results"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(seed, file)
            json.dump(file_data, file, indent = 4)
    else:
        with open(filename,'a+') as file:
             # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["results"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

async def main():

    await load_data()
    data = len(sites_to_load)
    for i in range(data):
        await brower_loader(Playwright, sites_to_load[i]["site_search"], sites_to_load[i]["target"], sites_to_load[i]["title"], sites_to_load[i]["price"], sites_to_load[i]["url"] )


# Blocking call which returns when the hello_world() coroutine is done
asyncio.run(main())
