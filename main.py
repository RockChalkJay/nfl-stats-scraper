import traceback
from typing import Optional

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

OUTPUT_FOLDER: str = "/path/to/your/output/folder"
# Categories
RUSHING: str = "rushing"
RECEIVING: str = "receiving"
PASSING: str = "passing"

def fetch_players_season_stats(category, start_year, end_year: Optional[int] = None):
    try:
        # Set up the WebDriver
        driver = webdriver.Chrome()

        # Verify valid year range
        if end_year is None or end_year < start_year:
            end_year = start_year

        while start_year <= end_year:

            # Navigate to the target webpage
            url = f"https://www.pro-football-reference.com/years/{start_year}/{category}.htm"
            driver.get(url)

            print("Wait for the 'Share & Export' menu to load")
            hover_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//li[@class='hasmore']/span[text()='Share & Export']"))
            )

            # Perform a mouse-over action on the "Share & Export" menu
            print("Performing mouse over on the 'Share & Export' menu")
            action = ActionChains(driver)
            action.move_to_element(hover_element).perform()

            print("Wait for the \"Get table as CSV\" button to become visible")
            # This doesn't work for some reason. I have to manually hover over the
            # Share & Export button in order for the button to be found and the
            # rest of the code to execute.
            csv_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[text()='Get table as CSV (for Excel)']"))
            )

            # Click the "Get table as CSV" button
            csv_button.click()

            # Wait for the CSV content to appear in the generated text area
            csv_content_element = driver.find_element(By.ID, f"csv_{category}")

            # Extract the CSV content
            csv_content = csv_content_element.text
            print("CSV content successfully extracted!")

            # Remove the first four lines
            lines = csv_content.splitlines()[5:]
            csv_content = "\n".join(lines)

            # Verify the output folder exists and create one if not
            output_folder = Path(f"{OUTPUT_FOLDER}/nfl/{category}")
            output_folder.mkdir(parents=True, exist_ok=True)

            with open(f"{output_folder.as_posix()}/{start_year}_stats.csv", "w") as file:
                file.write(csv_content)
            print(f"CSV content saved to {category}_data.csv")

            start_year += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    fetch_players_season_stats(PASSING, 2024)