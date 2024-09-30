from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360)

#keywords to look for, maybe scrape clothing websites for more keywords
fashion_keywords = ["denim jacket", "high-waisted jeans", "minimalist fashion"]

#
pytrends.build_payload(fashion_keywords, timeframe='today 12-m', geo='US')

trends_data = pytrends.interest_over_time()

trends_data.to_csv('fashion_trends.csv')

print(trends_data)