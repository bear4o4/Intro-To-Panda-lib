# Pandas Housing Analysis

This project explores the relationship between housing prices and various factors such as location, population, and income using the `pandas` library in Python. The dataset used for this analysis is `housing.csv`.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd pandas-housing-analysis
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the `housing.csv` file in the project directory.
2. Run the `main.py` script:
    ```sh
    python main.py
    ```

## Project Structure

- `main.py`: The main script that performs the data analysis tasks.
- `housing.csv`: The dataset used for analysis.
- `requirements.txt`: The list of required Python packages.

## Tasks

The project performs the following tasks:

1. Load the dataset using `pandas`.
2. Display the first and last few rows of the DataFrame.
3. Provide a concise summary of the DataFrame, including null values.
4. Select specific columns and rows using `loc` and `iloc`.
5. Filter rows based on conditions.
6. Plot histograms and scatter plots to visualize the data.
7. Create new columns based on existing data.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
