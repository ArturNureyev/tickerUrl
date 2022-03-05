import pandas as pd


def get_ticker_url():
    data = pd.read_csv(r'https://raw.githubusercontent.com/alvarobartt/investpy/master/investpy/resources/stocks.csv',
                       usecols=['tag', 'symbol', 'country'])
    american_companies = data[data['country'] == 'united states']
    data_output: dict[str, str] = {}

    for index, row in american_companies.iterrows():
        data_output[str(row["symbol"])] = f"https://www.investing.com/equities/{row['tag']}"

    return data_output


get_ticker_url()