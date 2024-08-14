# ScrappingProject

## Web Scraping Project for Retrieving Project Details

This project is a web scraping tool designed to retrieve project details such as **GSTIN No**, **PAN No**, **Name**, and **Permanent Address** from the [Himachal Pradesh RERA Public Dashboard](https://hprera.nic.in/PublicDashboard) using Selenium and Python. The scraped data is saved into a CSV file.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
- [Running the Script](#running-the-script)
- [Output](#output)
- [Requirements](#requirements)
- [License](#license)

## Project Overview

The script automates the process of extracting specific project information from the RERA Public Dashboard. The key data points retrieved are:

- **Rera No**: The unique RERA registration number of the project.
- **Name**: The name of the project owner.
- **GSTIN No**: The GST Identification Number associated with the project.
- **PAN No**: The PAN Number associated with the project.
- **Permanent Address**: The permanent address of the project.

## Setup Instructions

### Prerequisites

1. **Python 3.x**: Ensure that Python 3.x is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
2. **Edge WebDriver**: Download the appropriate version of Edge WebDriver for your version of Edge browser from [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
3. **Chrome WebDriver**: Download the appropriate version of Chrome WebDriver for your version of Chrome browser from [Chrome WebDriver](https://developer.chrome.com/docs/chromedriver/downloads).

### Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows:
.\env\Scripts\activate

# On macOS/Linux:
source env/bin/activate
```

### Install Required Python Packages

All required Python packages are listed in the `requirements.txt` file. Install them using following command:

```bash
pip install -r requirements.txt
```

## Running the Script

1. Ensure that the Edge WebDriver path in the script is correctly set to the location where you downloaded the WebDriver (`path = "C:\msedgedriver.exe"`).
2. Run the Python script:

```bash
python Scrapper.py
```

The script will open the Edge browser, navigate to the RERA Public Dashboard, extract the required information, and save it to a CSV file. (Please don't click anywhere on the running edge browser as it would interept with the program and not give desired output.)

## Output

The output of the script is a CSV file named `scraped_data.csv`, which is saved in the specified directory. The file contains the following columns:

- `Rera No`
- `Name`
- `GSTIN No`
- `PAN No`
- `Permanent Address`

## Requirements

The following Python libraries are used in this project:

- `selenium`
- `pandas`
- `requests`

These are included in the `requirements.txt` file and can be installed using the command mentioned in the [Setup Instructions](#setup-instructions) section.