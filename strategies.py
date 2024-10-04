from utils import find_last_mentioned_company, find_index_of_ad_last_sentence_start
from math import exp
def naive_strategy(bid, partial_ad, bidder_company_name, company_names):
    return bid

def name_contest_strategy(bid, partial_ad, bidder_company_name, company_names):
    """
    In this strategy the bidder incentive is to bet more when there is no company name in the sentence so their
    company name will show.
    """
    last_mentioned_company, last_mentioned_company_index = find_last_mentioned_company(partial_ad, company_names)
    last_sentence_start = find_index_of_ad_last_sentence_start(partial_ad)

    company_mentioned_in_current_sentence = last_sentence_start > last_mentioned_company_index
    if company_mentioned_in_current_sentence and last_mentioned_company == bidder_company_name:
        relevance = 1
    elif last_mentioned_company == "":
        relevance = 1.5
    elif company_mentioned_in_current_sentence:
        relevance = 0
    elif not company_mentioned_in_current_sentence and last_mentioned_company == bidder_company_name:
        relevance = 1
    elif not company_mentioned_in_current_sentence and last_mentioned_company != bidder_company_name:
        relevance = 1.5
    # should not reach this 'else'
    else:
        relevance = 0.5

    new_bid = bid * relevance

    return new_bid

def name_first_strategy(bid, partial_ad, bidder_company_name, company_names):
    """
    In this strategy, the bidder does not commit to large bets unless their company name is showing
    """
    last_mentioned_company, last_mentioned_company_index = find_last_mentioned_company(partial_ad, company_names)
    last_sentence_start = find_index_of_ad_last_sentence_start(partial_ad)

    company_mentioned_in_current_sentence = last_sentence_start > last_mentioned_company_index
    if company_mentioned_in_current_sentence and last_mentioned_company == bidder_company_name:
        relevance = 1.5
    elif last_mentioned_company == "":
        relevance = 0.5
    elif company_mentioned_in_current_sentence:
        relevance = 0
    elif not company_mentioned_in_current_sentence and last_mentioned_company == bidder_company_name:
        relevance = 1
    elif not company_mentioned_in_current_sentence and last_mentioned_company != bidder_company_name:
        relevance = 0.25
    # should not reach this 'else'
    else:
        relevance = 0.5

    new_bid = bid * relevance

    return new_bid










