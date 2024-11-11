# 📈 Bank Nifty ORB Strategy

This project implements an **Opening Range Breakout (ORB) strategy** specifically tailored for **Bank Nifty**, a popular index in the Indian stock market. Using the first 15 minutes of market data, this strategy identifies breakout opportunities based on high and low price levels within this range. The system is customizable and logs each trade to a CSV file.

---

## 📝 Overview

The **Opening Range Breakout (ORB) strategy** is widely used for intraday trading. This project:
- Analyzes the first 15 minutes to define high and low ranges.
- Identifies breakout entry points and manages exits with target and stop-loss conditions.
- Logs trade details (entry/exit price and time, PnL) for further analysis.

This project is ideal for anyone interested in **quantitative finance, algorithmic trading,** and **data analysis**.

## ✨ Features

- **🔧 Customizable Parameters**: Adjustable time range, target, and stop-loss percentages.
- **📊 Automated Trade Logging**: Records entry/exit times, prices, PnL, and instrument.
- **🧹 Data Cleaning and Preparation**: Formats trade logs for reporting.
- **💾 CSV Export**: Logs trades in a CSV file for easy performance tracking.

---

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/ORB-BankNifty-Strategy.git
    cd ORB-BankNifty-Strategy
    ```

2. **Install Dependencies**:
    Ensure Python 3.7+ is installed, then run:
    ```bash
    pip install pandas
    ```

3. **Prepare Data**:
    Place your input CSV file with the relevant data (`ticker`, `High`, `Low`, `Time`) in the project directory.

4. **Run the Strategy**:
    Execute the `main.py` script:
    ```bash
    python main.py
    ```

## Usage

### Parameters

- `opening_range_minutes`: Number of minutes for the opening range (default: 15).
- `target_percentage`: Profit target percentage for trades (default: 0.10).
- `stop_percentage`: Stop-loss percentage to exit the trade if it moves against the position (default: 0.20).

### Running the Script

The strategy script reads a CSV file with intraday data, applies the ORB trading logic, and generates an output CSV with the trade log.

1. Update `file_path` in the script to point to your input CSV file.
2. Set `Ticker` to your target instrument (e.g., 'BANKNIFTY').
3. Run `main.py`.

The output, saved as `trade_logs.csv`, will contain:
- Entry and exit times
- Entry and exit prices
- PnL (Profit and Loss) for each trade

## Example Output

| Entry Time | Entry Price | Exit Time | Exit Price | PnL  | Instrument |
|------------|-------------|-----------|------------|------|------------|
| 09:30:00   | 35000       | 09:45:00  | 35100      | 1000 | BANKNIFTY  |
| 10:00:00   | 34800       | 10:30:00  | 34750      | -50  | BANKNIFTY  |




## Skills Demonstrated

- **Python Programming**: Implemented trading strategy logic using pandas for data processing.
- **Data Analysis**: Set up a structured trading log for analyzing ORB strategy performance.
- **Financial Acumen**: Applied quantitative techniques in algorithmic trading.
- **Automation and Reporting**: Scripted automated logging and reporting features with CSV export for further analysis.

