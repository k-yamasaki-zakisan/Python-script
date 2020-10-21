from selenium import webdriver
from bs4 import BeautifulSoup

# Method to find the main website from the given URL
def main_website(url) -> str:
    parts = url.split('/')
    return parts[2]

# Method to check if the keywords of scrapped link matches with the main website
def present(url:str, web_main:str) -> bool:
     ok_flag = False
     for i in range(0, len(url)-len(web_main)+1):
         if url[i:i+len(web_main)]:
             ok_flag = True
             break
    return ok_flag

# Method to check all links in a webpage and categorise them as External or Internal Links
def links(url:str):
    # Running the driver in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # Change the driver_path to where your chrome driver is installed
    driver = webdriver.Chrome(options=options)

    links = ""
    try:
        # Requesting the desired webpage through selenium Chrome driver as some pages use javascripts
        driver.get(url)

        # Storing the entire webpage in html variable
        html = driver.page_source
        driver.quit()

        # Using beautiful soup to filter the scraped data
        soup = BeautifulSoup(html, "lxml")  # get element(fast than "html.parser")
        links = soup.find_all("a")
        web_main = main_website(url)
        internal_links = []
        external_links = []
        for link in links:
            try:
                final_url = ""
                # x is used to check the first character of the scrapped link
                x = link['href'][0:1]
                if x == '/':
                    final_url = url + link['href']
                    internal_links.append(final_url)
                elif x == '#':
                    final_url = url + '/' + link['href']