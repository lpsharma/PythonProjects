from finvizfinance.screener.overview import Overview
import pandas as pd
import csv 
import os

from transformers import pipeline
import yfinance as yf
from goose3 import Goose
from requests import get 

filters_dict = {'Debt/Equity':'Under 1', 
                    'PEG':'Low (<1)', 
                    'Operating Margin':'Positive (>0%)', 
                    'P/B':'Low (<1)',
                    'P/E':'Under 15',
                    'InstitutionalTransactions':'Positive (>0%)',
                    'InsiderTransactions':'Positive (>0%)'}
    
parameters = ['Exchange', 'Index', 'Sector', 'Industry', 'Country', 'Market Cap.',
        'P/E', 'Forward P/E', 'PEG', 'P/S', 'P/B', 'Price/Cash', 'Price/Free Cash Flow',
        'EPS growththis year', 'EPS growthnext year', 'EPS growthpast 5 years', 'EPS growthnext 5 years',
        'Sales growthpast 5 years', 'EPS growthqtr over qtr', 'Sales growthqtr over qtr',
        'Dividend Yield', 'Return on Assets', 'Return on Equity', 'Return on Investment',
        'Current Ratio', 'Quick Ratio', 'LT Debt/Equity', 'Debt/Equity', 'Gross Margin',
        'Operating Margin', 'Net Profit Margin', 'Payout Ratio', 'InsiderOwnership', 'InsiderTransactions',
        'InstitutionalOwnership', 'InstitutionalTransactions', 'Float Short', 'Analyst Recom.',
        'Option/Short', 'Earnings Date', 'Performance', 'Performance 2', 'Volatility', 'RSI (14)',
        'Gap', '20-Day Simple Moving Average', '50-Day Simple Moving Average',
        '200-Day Simple Moving Average', 'Change', 'Change from Open', '20-Day High/Low',
        '50-Day High/Low', '52-Week High/Low', 'Pattern', 'Candlestick', 'Beta',
        'Average True Range', 'Average Volume', 'Relative Volume', 'Current Volume',
        'Price', 'Target Price', 'IPO Date', 'Shares Outstanding', 'Float']

#tickers = ['AMPY', 'BOOM', 'BWB', 'CAAS', 'CNX', 'HAFC', 'HTLF', 'SASR', 'SPNT', 'TCBX']


def get_undervalued_stocks():
    """
    Returns a list of tickers with:
    
    - Positive Operating Margin
    - Debt-to-Equity ratio under 1
    - Low P/B (under 1)
    - Low P/E ratio (under 15)
    - Low PEG ratio (under 1)
    - Positive Insider Transactions
    """
    foverview = Overview()
    foverview.set_filter(filters_dict=filters_dict)

    # out file 
    if not os.path.exists("out"):
        os.makedirs("out")

    df_overview = foverview.screener_view()
    df_overview.to_csv('./Stock/FinViz/out/Overview.csv',index=False)
    tickets = df_overview['Ticker'].to_list()
    return tickets


def get_ticker_news_sentiment(ticker):
    """
    Returns a Pandas dataframe of the given ticker's most recent news article headlines,
    with the overal sentiment of each article.

    Args:
        ticker (string)

    Returns:
        pd.DataFrame: {'Date', 'Article title', Article sentiment'}
    """
    ticker_news = yf.Ticker(ticker)
    news_list = ticker_news.get_news()
    extractor = Goose()
    pipe = pipeline("text-classification", model="ProsusAI/finbert")
    
    data = []
    for dic in news_list:
        title = dic['title']
        response = get(dic['link'])
        article = extractor.extract(raw_html=response.content)
        text = article.cleaned_text
        date = article.publish_date

        if (date != None):
            results = pipe(text[0:512])
            data.append({'Date':f'{date}','Article title':f'{title}','Article sentiment':results[0]['label']})

        """
        
        if len(text) > 1024:
            data.append({'Date':f'{date}',
                         'Article title':f'{title}',
                         'Article sentiment':'NaN too long'})
        else:
            results = pipe(text)
            #print(results)
            data.append({'Date':f'{date}',
                         'Article title':f'{title}',
                         'Article sentiment':results[0]['label']})
        """
    
    df = pd.DataFrame(data)
    return df


def generate_csv(ticker):
    df = get_ticker_news_sentiment(ticker)
    if (len(df)>0):
        df.to_csv(f'./Stock/FinViz/out/{ticker}.csv', index=False)

    


# Main Program 

# Extract list of stock tickers which  are undervalued
undervalued = get_undervalued_stocks()

# Loop through each ticker to get sentiment data
for ticker in undervalued:
    generate_csv(ticker)
    


    