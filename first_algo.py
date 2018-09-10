# CODE PYTHON

def initialize(context):
    # context.techies = [sid(24), sid(1900), sid(16841)]
                       
     context.aapl = sid(24)
    # context.csco = sid(1900)
    # context.amzn = sid(16841)
    
# def handle_data(context, data):
#     price_history = data.history(context.techies, fields = 'price', bar_count = 5, frequency = '1d')
#     print(price_history)
    
    # tech_close = data.current(context.techies, 'close')               print(tech_close)
    # print("\n")
    # print(type(tech_close))
                       
    # order_target_percent(context.aapl, .27)
    # order_target_percent(context.csco, .20)
    # order_target_percent(context.amzn, .53)

schedule_function(open_positions, date_rules.week_start(), time_rules.market_open())
        
schedule_function(close_positions, date_rules.week_end(), time_rules.market_close(minutes = 30
    

def open_positions(context, data):
    order_target_percent(context.aapl, 0.10)
    
def close_positions(context, data):
    order_target_percent(context.aapl, 0)