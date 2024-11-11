import pandas as pd

opening_range_minutes = 15
target_percentage = 0.10
stop_percentage = 0.2

def calculate_pnl(entry_price, exit_price, quantity):
    return (exit_price - entry_price) * quantity

def strategy(data):
    data = data.copy()  # Make a copy of the data to avoid SettingWithCopyWarning
    data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S')
    data.sort_values(by='Time', inplace=True)
    opening_range = data.head(opening_range_minutes)
    opening_range_high = opening_range['High'].max()
    opening_range_low = opening_range['Low'].min()
    entry_price = None
    position = 0
    trade_log = []
    for index, row in data.iterrows():
        current_time = row['Time']
        current_high = row['High']
        current_low = row['Low']
        if current_time > opening_range['Time'].max():
            if entry_price is None:
                if current_high > opening_range_high:
                    entry_price = current_high
                    position = 1  # LONG position
                elif current_low < opening_range_low:
                    entry_price = current_low
                    position = -1  # Short position
            else:
                if position == 1 and current_high >= entry_price * (1 + target_percentage):
                    exit_price = current_high
                    pnl = calculate_pnl(entry_price, exit_price, 1)
                    trade_log.append([current_time, entry_price, current_time, exit_price, pnl, row['Ticker']])
                    entry_price = None
                elif position == -1 and current_low <= entry_price * (1 - target_percentage):
                    exit_price = current_low
                    pnl = calculate_pnl(entry_price, exit_price, -1)
                    trade_log.append([current_time, entry_price, current_time, exit_price, pnl, row['Ticker']])
                    entry_price = None

    trade_df = pd.DataFrame(trade_log, columns=["Entry Time", "Entry Price", "Exit Time", "Exit Price", "PnL",'Instrument'])
    return trade_df

file_path = "/Users/eswar/Desktop/TASK2/data/GFDLNFO_BACKADJUSTED_01032023.csv"
data = pd.read_csv(file_path)
Ticker='BANKNIFTY'
data1=data[data['ticker'].apply(lambda x: x[:len(Ticker)==Ticker])]
trades = strategy(data1)
output_file ="ans.csv"
trades.to_csv(output_file, index=False)
data_file = "/Users/eswar/Desktop/pythonProject/ans.csv"
output_file = "/Users/eswar/Desktop/pythonProject/trade_logs.csv"
df = pd.read_csv(data_file)
df['Entry Time'] = df['Entry Time'].str.split(' ').str[1]
df['Exit Time'] = df['Exit Time'].str.split(' ').str[1]
df.to_csv(output_file, index=False)