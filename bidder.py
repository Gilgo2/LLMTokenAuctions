class Bidder:
    def __init__(self, bid, strategy_func, bidder_company, budget):
        self.bid = bid
        self.strategy_func = strategy_func
        self.bidder_company = bidder_company
        self.company_names = ['Alpha Airlines', 'Beta Resort']
        self.budget = budget

    def get_bid(self, partial_ad):
        return self.strategy_func(self.bid, partial_ad, self.bidder_company, self.company_names)