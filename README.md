# Home Depot PO KeyRec Retrieval Automation

## Overview
The **Home Depot PO KeyRec Retrieval** script automates logging into the Home Depot Freight Management portal, selecting "Order" mode, and retrieving KeyRec numbers for a list of Purchase Orders (POs). Built with **Python** and **Selenium**, it streamlines the process by automating browser interactions, including login verification, dropdown selection, PO input, and result extraction. The script uses explicit waits to ensure elements are loaded before interaction, making it robust against dynamic page loads. The retrieved PO and KeyRec pairs are saved in a text file for easy reference.

This automation allows users to process multiple POs efficiently, reducing manual effort and minimizing errors.

---

## Features
- Automated login verification by waiting for a "Welcome" message.
- Launches Chrome in full-screen (maximized) mode for better visibility.
- Selects "Order" mode from dropdown once at the start.
- Processes multiple PO numbers entered by the user.
- Uses explicit waits to handle dynamic content loading.
- Retrieves KeyRec numbers for each PO.
- Saves PO numbers and their KeyRec numbers into `po_keyrec_output.txt`.
- Combines fixed delays with dynamic waits for stability.

---

## Requirements
Ensure you have the following installed:

- **Python 3.x**
- **Selenium** (`pip install selenium`)
- **Chrome WebDriver**, compatible with your installed Chrome browser version.
- Optional: Adjust XPath selectors if the website layout changes.

---

## Installation
1. Download or clone this script.
2. Install the necessary Python packages:

```bash
pip install selenium
```
3. Download ChromeDriver from here matching your Chrome version.
4. Place the chromedriver executable in a directory accessible by your system or specify its path in the script.
5. Save the script as GetKeyRec.py or your preferred filename.
---	
## Usage
Run the script:
```bash
python GetKeyRec.py
```
Follow these steps:

- When prompted, sign in manually on the web portal. The script will wait until it detects a "Welcome" message confirming login success.
- Enter the list of PO numbers separated by commas (e.g., 123456, 789012, 345678).
The script will process each PO, retrieve the KeyRec number, and save the results in po_keyrec_output.txt.
---

## Notes

- The script employs explicit waits to handle dynamic content, increasing reliability.
- Be sure the XPath selectors match the current webpage layout; updates may be necessary if the site updates.
- The Chrome window opens in maximized mode for better visibility.
- The output file lists each PO and its corresponding KeyRec number, separated by a colon.
---
## License

This script is intended for personal use and automation purposes. Feel free to modify or adapt it, respecting the website’s terms of service.

---
## Contact
For questions or feedback, please contact Pressley at receiving_1943@homedepot.com.