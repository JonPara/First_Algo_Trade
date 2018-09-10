# CODE PYTHON

def initialize(context):
    context.aapl = sid(24)
    context.csco = sid(1900)
    context.amzn = sid(16841)

def handle_data(context, data):
    order_target_percent(context.aapl, .27)
    order_target_percent(context.csco, .20)
    order_target_percent(context.amzn, .53)
    