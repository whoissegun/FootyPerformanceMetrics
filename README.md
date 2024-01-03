# Football Data Analysis and Visualization

## Project Overview

This project is designed to fetch, analyze, and visualize data on Manchester City F.C performance in 2022. It provides insights into the teams' performance across different metrics such as wins, draws, losses, goal distribution, card distribution, and match fixtures.

## Features

- Fetch football data using external APIs.
- Analyze team performance statistics.
- Visualize data in different formats (bar charts, pie charts, scatter plots, etc.).

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Pip (Python package manager)

### Installation

1. Clone the repository to your local machine:
git clone https://github.com/whoissegun/FootyPerformanceMetrics.git


2. Navigate to the cloned directory:
cd FootyPerformanceMetrics


3. Install required Python packages:
pip install -r requirements.txt

### Setting Up Environment Variables

1. Create a `.env` file in the project root directory and add the following variables:
RAPID_API_KEY=your_api_key_here
RAPID_API_HOST=your_api_host_here
RAPID_API_BASE_URL=your_api_base_url_here


### Run the main script to start the analysis:

python main.py

## Structure

- `fetch_data/`: Module for fetching data from APIs.
- `analyze_data.py`: Functions for analyzing and plotting data.
- `main.py`: Main script to run the analysis.
- `utils/`: Utility functions and constants.
- `requirements.txt`: Required Python libraries.
- `DATA_REPORT.md`: My interpretations of the data visualized
