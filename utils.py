def find_index_of_ad_last_sentence_start(ad):
    return min(ad.rfind('.'), 0)


def find_last_mentioned_company(ad, company_names):
    last_company_name = ""
    last_company_name_index = -1
    for name in company_names:
        index = ad.find(name)
        if index > last_company_name_index:
            last_company_name = name
            last_company_name_index = index
    return last_company_name, last_company_name_index
