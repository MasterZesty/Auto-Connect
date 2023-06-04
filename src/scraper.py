from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import json

CHROME_DRIVER_PATH = 'C:/Users/kgn27/AppData/Local/pyppeteer/pyppeteer/local-chromium/588429/chrome-win32/'
GCP_PDE_URL = 'https://googlecloudcertified.credential.net/?groups=68191&location=Pune,%20Maharashtra,%20India&lat=18.5204303&lng=73.8567437'




def get_profile_links(page_url):
    ''''This function uses chromedriver in headless 
        mode to get url page content and extract linkedin
        profiles'''

    # Set the path to the ChromeDriver executable
    chrome_driver_path = CHROME_DRIVER_PATH

    # Set Chrome options to run the browser in headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode

    # Create a new ChromeDriver instance
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

    try:
        # Load the URL
        url = page_url
        driver.get(url)

        profile_links = []  # List to store the LinkedIn profile links
        c = 0

        while True:
            # Wait for the content to load (you may need to adjust the sleep time)
            time.sleep(5)

            # Extract and print the LinkedIn profile links from the current page
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            linkedin_links = soup.find_all('a', href=lambda href: href and 'linkedin.com/in/' in href)
            for link in linkedin_links:
                #c += 1
                #print(c,'--------',link['href'])
                profile_links.append(link['href'])

            # Find the "Next" button
            next_button = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Next results")]')

            # Check if the "Next" button is disabled
            if "disabled" in next_button.get_attribute("class"):
                break  # Exit the loop if the "Next" button is disabled

            # Click the "Next" button to load the next page
            next_button.click()

            # Print the progress 
            remaining_profiles = len(profile_links)  # Number of remaining profiles
            print(f"Processed {remaining_profiles} profiles....")


        # Save the profile links to a JSON file
        total_profiles = len(profile_links)
        print(f"Total {total_profiles} profiles.")
        with open('linkedin_profiles.json', 'w') as f:
            json.dump(profile_links, f)

    except Exception as e:
        # Handle any exceptions and print the error message
        print(f"An error occurred: {str(e)}")

    finally:
        # Quit the driver
        driver.quit()

    return None



if __name__ == "__main__":
    print("Starting Program....")
    get_profile_links(GCP_PDE_URL)