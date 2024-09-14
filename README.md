# Selenium-project
# eBay Automation with Selenium
This project automates the process of logging into eBay, searching for specific items, adding them to the cart, and logging out. It uses Python with Selenium for web interaction and allows you to automate multiple searches from a list of items stored in a text file.

# Features
Automates login to eBay.
Searches for items from a list.
Adds the first search result to the cart.
Logs out after processing.

# Prerequisites
Before running the script, ensure you have the following installed:
Python 3.x
Selenium
Chrome WebDriver (automatically managed using webdriver-manager)

# You can install the necessary Python packages using:
pip install selenium webdriver-manager

# How to Use
Clone the Repository:
git clone https://github.com/varshasathyaprakash/Selenium-project.git
cd Selenium-project

# Prepare the List of Items:
Create a file named items_to_search.txt in the project directory.
Add one item per line to search on eBay.
Example:
laptop
smartphone
headphones
# Modify Login Details:
Open the merged.py file and update the email and password in the run_ebay_login_and_search_test function:
email.send_keys("your-ebay-email")  # Replace with your eBay email
password.send_keys("your-ebay-password")  # Replace with your eBay password

# Run the Script:
Run the script from your terminal:
python merged.py

The script will:
Open eBay in Chrome.
Log in with your credentials.
Search for each item listed in items_to_search.txt.
Add the first search result to the cart.
Log out after completing the searches.

# Notes
Ensure you have Google Chrome installed, as the script uses Chrome WebDriver.

