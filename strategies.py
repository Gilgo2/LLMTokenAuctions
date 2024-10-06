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
        relevance = 0.001
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
        relevance = 0.001
    elif not company_mentioned_in_current_sentence and last_mentioned_company == bidder_company_name:
        relevance = 1
    elif not company_mentioned_in_current_sentence and last_mentioned_company != bidder_company_name:
        relevance = 0.25
    # should not reach this 'else'
    else:
        relevance = 0.5

    new_bid = bid * relevance

    return new_bid

def decreasing_based_on_position_strategy(bid, partial_ad, bidder_company_name, company_names):
    """
    This function decreases the original bid based on the length of the current ad (partial ad). 
    The longer the ad, the lower the bid.
    
    Parameters:
        bid (float): The original bid from the bidder company.
        partial_ad (str): The current partially generated ad text.
        bidder_company_name (str): The name of the company that is bidding.
        company_names (list): A list of company names participating in the bidding process.
    
    Returns:
        adjusted_bid (float): The adjusted bid after applying the decreasing strategy.
    """

    # Get the length of the partial ad (number of characters or words)
    partial_ad_length = len(partial_ad.split()) 
    
    # Define a rate or formula to decrease the bid based on the partial ad length
    # Decrease the bid by 3 percentage of the original bid for each character (or word)
    decrease_factor = 0.03
    
    # Calculate the adjusted bid
    adjusted_bid = bid - (partial_ad_length * decrease_factor * bid)
    
    # Ensure the bid doesn't go below a minimum (e.g., zero or some other value)
    adjusted_bid = max(0, adjusted_bid)
    
    return adjusted_bid











