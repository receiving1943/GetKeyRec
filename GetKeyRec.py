import sys
import os
import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_login(driver):
    """
    Waits for an element containing 'Welcome' to appear, indicating successful login.
    """
    wait = WebDriverWait(driver, 20)
    try:
        welcome_xpath = "//*[contains(text(), 'Welcome')]"
        wait.until(EC.presence_of_element_located((By.XPATH, welcome_xpath)))
        print("Login confirmed.")
    except:
        print("Login not confirmed within timeout.")
        sys.exit("Exiting due to login failure.")

def select_order_type(driver):
    """
    Select 'Order' from the dropdown menu once at the beginning.
    """
    wait = WebDriverWait(driver, 10)
    try:
        dropdown_xpath = '/html/body/div[1]/div[1]/div[1]/div/header/div/div[2]/div[5]/div/div/div/form/div[1]/select'
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
        dropdown.click()

        order_option_xpath = '/html/body/div[1]/div[1]/div[1]/div/header/div/div[2]/div[5]/div/div/div/form/div[1]/select/option[2]'
        order_option = wait.until(EC.element_to_be_clickable((By.XPATH, order_option_xpath)))
        order_option.click()
        # print("Selected 'Order' from dropdown once.")
    except Exception as e:
        print(f"Error selecting 'Order' from dropdown: {e}")

def get_keyrec_for_po(driver, po_number, count=2):
    """
    Inputs PO number, clicks search, waits, and extracts key rec number.
    Uses explicit wait for the key rec element.
    """
    wait = WebDriverWait(driver, 10)
    try:
        # Input PO number
        input_xpath = '/html/body/div[1]/div[1]/div[1]/div/header/div/div[2]/div[5]/div/div/div/form/div[3]/div/input'
        input_box = wait.until(EC.element_to_be_clickable((By.XPATH, input_xpath)))
        input_box.clear()
        input_box.send_keys(po_number)

        # Click search button
        button_xpath = '/html/body/div[1]/div[1]/div[1]/div/header/div/div[2]/div[5]/div/div/div/form/div[3]/button'
        search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        search_btn.click()

        # Fixed delay for page to load
        t.sleep(3)

        # XPath for key rec number
        keyrec_xpath = f'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div[{count}]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]'
        # print(f"Waiting for key rec element with XPath: {keyrec_xpath}")
        # Explicit wait for the key rec element
        keyrec_element = wait.until(EC.visibility_of_element_located((By.XPATH, keyrec_xpath)))
        keyrec_text = keyrec_element.text.strip()
        print(f"Found key rec for PO {po_number}: {keyrec_text}")
        return keyrec_text
    except Exception as e:
        print(f"Error retrieving key rec for PO {po_number}: {e}")
        return None

if __name__ == "__main__":
    # Suppress logs
    sys.stderr = open(os.devnull, 'w')

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--log-level=3')  # Show only errors
    options.add_argument('--incognito')
    options.add_argument('--disable-logging')
    options.add_argument('--disable-background-networking')
    options.add_argument("--start-maximized")  # Start maximized

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)

    # Maximize window (redundant but good)
    driver.maximize_window()

    # Restore stderr
    sys.stderr.close()
    sys.stderr = sys.__stderr__

    # Open URL once and wait for manual sign-in
    driver.get('https://webapps.homedepot.com/MyFreight/')
    input("Please sign in manually, then press Enter to continue...")

    # Wait for login confirmation
    wait_for_login(driver)

    # Select 'Order' from dropdown once
    select_order_type(driver)

    # Enter PO list
    po_input_string = input("Enter PO numbers separated by commas: ")
    po_list = [po.strip() for po in po_input_string.split(',')]

    key_rec_pairs = []
    count = 2  # starting count for XPath

    for po in po_list:
        print(f"\nProcessing PO: {po}")
        key_rec = get_keyrec_for_po(driver, po, count)
        if key_rec:
            # print(f"Successfully retrieved: {key_rec}")
            key_rec_pairs.append((po, key_rec))
        else:
            print("Failed to retrieve key rec.")
            key_rec_pairs.append((po, 'Failed to retrieve key rec'))
        count += 1
        # print("Waiting 5 seconds before next PO...\n")
        t.sleep(5)

    driver.quit()

    # Save to file
    filename = "po_keyrec_output.txt"
    with open(filename, "w") as f:
        for po, kr in key_rec_pairs:
            f.write(f"{po}:{kr}\n")
    print(f"\nDone! Saved {len(key_rec_pairs)} PO key rec pairs to {filename}.")