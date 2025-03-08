# NFL Stats Scraper
This project is a Python-based scraper that collects NFL player statistics for specific categories (rushing, receiving, passing) across different seasons and saves them as CSV files. It uses the Selenium WebDriver to extract data from Pro Football Reference and saves the data locally in a structured directory.

## Features
Scrapes NFL player statistics for selected categories (rushing, receiving, passing).
Supports scraping data for a given year or range of years.
Saves the data as CSV files with proper directory structure.
Prerequisites
Make sure you have the following installed:

* Python 3.x
* pip for managing Python packages
* Selenium WebDriver
* WebDriver (e.g., ChromeDriver)
* Install the required Python packages:

`pip install selenium`

## How It Works
The script uses Selenium WebDriver to navigate the Pro Football Reference website.
It scrapes player statistics for the specified category (rushing, receiving, or passing) and year range.
The data is saved as a CSV file in the OUTPUT_FOLDER directory.

## Code Usage
Clone the repository or create a Python script with the following code:
Update the OUTPUT_FOLDER variable in the script to the desired directory where you want the CSV files to be saved.

Example Usage:

```
fetch_players_season_stats(PASSING, 2024, 2025)
```
This will scrape passing statistics for the 2024 and 2025 NFL seasons and save them as CSV files in the specified output folder.

## Notes:
Issue with the 'Share & Export' Button: There is an issue with the visibility of the "Get table as CSV" button. The script currently requires manual hovering over the "Share & Export" button on the page for the CSV download button to be clickable. This is a known issue in the code.
Folder Structure:
The scraper will create a folder structure as follows:
```
/path/to/your/output/folder
  ├── nfl
      ├── rushing
          └── 2024_stats.csv
          └── 2025_stats.csv
      ├── receiving
          └── 2024_stats.csv
      └── passing
          └── 2024_stats.csv
```

## License
This project is open source and available under the MIT License.

