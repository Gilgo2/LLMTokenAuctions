from typing import Optional


class Bidder:
    def __init__(self, bid, strategy_func, bidder_company, budget, company_names: Optional[list] = None):
        self.bid = bid
        self.strategy_func = strategy_func
        self.bidder_company = bidder_company
        self.company_names = ['Alpha Airlines', 'Beta Resort'] if company_names is None else company_names
        self.budget = budget

    def get_bid(self, partial_ad):
        return self.strategy_func(self.bid, partial_ad, self.bidder_company, self.company_names)