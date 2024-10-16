from typing import Optional


class Bidder:
    def __init__(self, bid, strategy_func, bidder_company, budget, company_names: Optional[list] = None, messages_alpha: Optional[list] = None, messages_beta: Optional[list] = None):
        self.bid = bid
        self.strategy_func = strategy_func
        self.bidder_company = bidder_company
        self.company_names = ['Alpha Airlines', 'Beta Resort'] if company_names is None else company_names
        self.budget = budget
        self.messages_alpha = [
                {"role": "user", "content": "You are an expert of writing texts that naturally combines two ads together. Your choice of words and sentences is full of artistic flair. Do not include an intro, only write an ad."}, {"role":"user", "content":"Write a two-sentence ad for a flight to Hawaii using Alpha Airlines. Ensure Alpha Airlines is at the beginning of each sentence."}
            ] if messages_alpha is None else messages_alpha
        self.messages_beta = [
                {"role": "user", "content": "You are an expert of writing texts that naturally combines two ads together. Your choice of words and sentences is full of artistic flair, Do not include an intro, only write an ad."}, {"role":"user", "content":"Write a two-sentence ad for a vacation in Hawaii at the Beta Resort. Ensure Beta Resort is at the beginning of each sentence."}
            ] if messages_beta is None else messages_beta

    def get_bid(self, partial_ad):
        return self.strategy_func(self.bid, partial_ad, self.bidder_company, self.company_names)