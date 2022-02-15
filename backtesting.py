import backtrader as bt
import matplotlib as mtp
from numpy import busday_count
from pandas import Period
from constants import *
from alpaca_trade_api.rest import TimeFrame,REST
from alpaca_trade_api.stream import Stream
rest_api = REST(API_KEY,SECRET_KEY,'https://paper-api.alpaca.markets')

def run_backtest(symbols,start,end,strategy,timeframe=TimeFrame.Day, cash=5000):
    '''
    1.symbols= list or string for symbol to search
    2.start -> Start date to run the backtest
    3.end -> end date to run the backtest
    4.strategy -> Strategy to test
    5.timeframe -> time range 
    6.cash -> to run with notional
    
    '''
    #initialization of broker
    bak = bt.Cerebro(stdstats=True)
    bak.broker.setcash(cash)
    
    #add the strategy
    bak.addstrategy(strategy)
    
    #Check the symbol list
    if type(symbols) == str:
        symbol = symbols
        alp_data = rest_api.get_bars(symbol,timeframe,start,end,adjustment='all').df
        data = bt.feeds.PandasData(dataname=alp_data,name=symbol)
        bak.adddata(data)
    elif type(symbols) == list or type(symbols) == set:
        for symbol in symbols:
            alp_data = rest_api.get_bars(symbol,timeframe,start,end,adjustment='all').df
            data = bt.feeds.PandasData(dataname=alp_data,name=symbol)
            bak.adddata(data)
    
    
    # runing the test
    initial_portfolio_value = bak.broker.getvalue()
    print (f'Initial value of the portfolio -->{initial_portfolio_value}')
    results = bak.run()
    final_portfolio_value = bak.broker.getvalue()
    print (f'Final value of the portfolio  -->{final_portfolio_value} and Return is --> {(final_portfolio_value/initial_portfolio_value -1)*100}%')
    
class smaCross(bt.Strategy):
    params = dict(
        pfast = 13,
        pslow = 30
    )
    def __init__(self):
        smaf = bt.ind.SMA(period=self.params.pfast)
        smas = bt.ind.SMA(period=self.params.pslow)
        self.cross_over = bt.ind.CrossOver(smaf,smas)
    def next(self):
        if not self.position and self.cross_over > 0:
            self.buy()
        elif self.position and self.cross_over < 0:
            self.close()

run_backtest('GE','2021-01-01','2021-11-01',smaCross,TimeFrame.Day,10000)
            
      

    
