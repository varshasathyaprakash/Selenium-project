import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def read_items_from_file(file_path):
    with open(file_path, 'r') as file:
        items = file.read().splitlines()
    return items


def handle_additional_auth(driver):
    try:
        fingerprint_prompt = driver.find_element(By.XPATH, "//button[text()='No thanks']")
        fingerprint_prompt.click()
        time.sleep(10)
    except:
        pass


def run_ebay_login_and_search_test(items_to_search):
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.ebay.com/")
        driver.maximize_window()
        time.sleep(10)
        print("Opened eBay and maximized window")

        sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
        sign_in_button.click()
        time.sleep(10)
        print("Clicked Sign in button")

        email = driver.find_element(By.ID, "userid")
        email.send_keys("abc@gmail.com")  # Replace with your eBay email
        time.sleep(10)
        print("Entered email")

        continue_button = driver.find_element(By.ID, "signin-continue-btn")
        continue_button.click()
        time.sleep(10)
        print("Clicked Continue button")

        password = driver.find_element(By.ID, "pass")
        password.send_keys("xyz")  # Replace with your eBay password
        time.sleep(10)
        print("Entered password")

        login_button = driver.find_element(By.ID, "sgnBt")
        login_button.click()
        time.sleep(10)
        print("Clicked login button")

        print("User has logged in")

        # Handle additional authentication if prompted
        try:
            passkeys_cancel_button = driver.find_element(By.ID, "passkeys-cancel-btn")
            passkeys_cancel_button.click()
            time.sleep(10)
            print("Handled passkeys cancel button")
        except:
            print("No passkeys cancel button")

        handle_additional_auth(driver)

        for item in items_to_search:
            search_box = driver.find_element(By.NAME, "_nkw")
            search_box.clear()
            search_box.send_keys(item)
            search_box.send_keys(Keys.RETURN)
            time.sleep(10)
            print(f"Searched for item: {item}")

            search_results = driver.find_elements(By.XPATH,
                                                  "//ul[contains(@class, 'srp-results')]/li[contains(@class, 's-item')]")
            if len(search_results) > 0:
                print(f"Search for '{item}' returned {len(search_results)} results.")

                # Navigate to the first result
                first_result = search_results[0].find_element(By.CLASS_NAME, "s-item__link").get_attribute('href')
                driver.get(first_result)
                time.sleep(2)
                print("Navigated to the first search result")

                try:
                    # Improved selector for "Add to cart" button
                    add_to_cart_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.ID, "atcBtn_btn_1"))
                    )
                    add_to_cart_button.click()
                    time.sleep(2)
                    print("Clicked on 'Add to cart' button successfully!")
                except Exception as e:
                    print(f"Error: 'Add to cart' button not found or could not be clicked. Exception: {e}")
            else:
                print(f"Search for '{item}' did not return any results.")

            time.sleep(5)  # Pause between searches

        # Logout functionality
        account_menu = driver.find_element(By.ID, "gh-ug")
        account_menu.click()
        time.sleep(2)

        logout_button = driver.find_element(By.LINK_TEXT, "Sign out")
        logout_button.click()
        time.sleep(10)
        print("Logged out successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


# Read items from the text file
file_path = 'items_to_search.txt'
items_to_search = read_items_from_file(file_path)

# Run the eBay login and search test cases
run_ebay_login_and_search_test(items_to_search)
