import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def start_download():
    # Set up Firefox options
    firefox_options = FirefoxOptions()
    firefox_options.binary_location = (
        "/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox"
    )
    firefox_options.add_argument("--connect-existing")
    firefox_options.add_argument("--profile")
    firefox_options.add_argument(
        "/Users/nick/Library/Caches/Firefox/Profiles/7fpj7ejc.dev-edition-default"
    )
    firefox_options.set_preference("marionette", True)
    driver = webdriver.Remote(
        command_executor="http://localhost:4444", options=firefox_options
    )

    try:
        # Navigate to the page
        driver.get(
            "https://www.amazon.com/hz/mycd/digital-console/contentlist/booksPurchases/dateDsc?pageNumber=1"
        )
        time.sleep(10)
        assert "Amazon.com" in driver.title

        # Wait until the menu is clickable and click it
        menu_button = WebDriverWait(
            driver, 5
        ).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "[class^='Dropdown-module_container']",  # Select elements with class starting with 'Dropdown-module_dropdown_container'
                )
            )
        )
        menu_button.click()
        print("Clicked the menu button")

        # Wait until the download button is clickable and click it
        download_button = WebDriverWait(
            driver, 5
        ).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "[class^='Dropdown-module_dropdown_container'] div:nth-child(2)",  # Adjust the selector as needed
                )
            )
        )
        download_button.click()
        print("Clicked the download button")

        # Wait for the download to complete
        WebDriverWait(driver, 20).until(
            lambda x: os.path.exists(
                "/path/to/download/directory/filename.ext"
            )  # Replace with the actual filename
        )

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    start_download()
