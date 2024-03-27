import time
from playwright.sync_api import sync_playwright


def run_this(url):
    def scroll_me():
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                with open("links.txt", 'a') as file:
                    page.on("response", lambda response: file.write(response.url + "\n") if 'images.scrolller.com' in response.url else print('nah'))
                    page.goto(url)
                    time.sleep(5)
                    page.click('//*[@id="root"]/div/div[2]/div[2]/div[5]/div[2]/button[1]')
                    for x in range(5):
                        page.keyboard.press("End")
                        print(f"End pressed {x+1} times")
                        time.sleep(2)
                    try:
                        page.click('//*[@id="root"]/div/div[1]/div[2]/div/div[3]/button')
                    finally:
                        pass
                    for x in range(15):
                        page.keyboard.press("End")
                        print(f"End pressed {x+1} times")
                        time.sleep(2)
                browser.close()
        except:
            print("error handled")

    for i in range(20):
        scroll_me()