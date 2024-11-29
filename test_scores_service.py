import chromedriver_autoinstaller
from selenium.webdriver.support.ui import Select


from selenium import webdriver
from selenium.webdriver.common.by import By
import re

def test_scores_service(url):
    # Initialize the browser
    driver = webdriver.Chrome()

    try:
        # Open the URL
        driver.get(url)

        # Find the score element
        score_element = driver.find_element(By.ID, 'score')

        # Get the score value
        score_value = score_element.text

        # Check if the score is a number between 1 and 1000
        if re.match(r'^\d+$', score_value):
            score = int(score_value)
            return 1 <= score <= 1000
        else:
            return False
    finally:
        # Close the browser
        driver.quit()

def main_function():
    url = 'http://localhost:8777'
    if test_scores_service(url):
        print("Test passed")
        exit(0)
    else:
        print("Test failed")
        exit(-1)


if __name__ == '__main__':
    chromedriver_autoinstaller.install()
    main_function()
