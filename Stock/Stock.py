from finvizfinance.screener.overview import Overview
import pandas as pd
import csv 
import os

filters_dict = {'Debt/Equity':'Under 1', 
                    'PEG':'Low (<1)', 
                    'Operating Margin':'Positive (>0%)', 
                    'P/B':'Low (<1)',
                    'P/E':'Low (<5)',
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

    df_overview = foverview.screener_view()

    if not os.path.exists("out"):
        os.makedirs("out")
    df_overview.to_csv('out/Overview.csv,index=False')
    tickets = df_overview['Ticke'].to_list()
    return tickets

    print(get_undervalued_stocks)
    


    