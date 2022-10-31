''''
Spacy tutorial 01: Hello world
'''
import spacy

# https://www.cnbc.com/2022/10/30/stock-market-news-futures-open-to-close.html
text = "Stocks slipped Monday as the final trading day of October kicked off, but the major averages were on pace to snap a two-month losing streak.\
The S&P 500 last traded 0.8% lower, while the Nasdaq Composite tumbled 1.2%. The Dow Jones Industrial Average futures shed 130 points, or 0.4%.\
Markets made a huge comeback in October, guided by the Dow. The 30-stock index was last up 13.9% for the month and on pace for its best month since 1976 as investors have bet on more traditional companies, like banks, to lead the next bull. The S&P 500 and Nasdaq Composite are also up about 8% and 4%, respectively, this month.\
October’s gains have come despite a mixed third-quarter earnings season, which has shown slowing growth and a few major disappointments from large tech companies such as Meta Platforms and Amazon. Those names led Monday’s tech sector losses as investors continued their rotation out of the growth sector.\
Traders are preparing week this for the latest Federal Reserve meeting beginning Tuesday. The central bank is expected to hike rates by three quarters of a percentage again on Wednesday, but many on Wall Street are looking for a signal from the FOMC statement or Chairman Jerome Powell’s press conference that the Fed could pause its hikes in the near future, or curb their size.\
This, and economic data due out later this week, such as October’s nonfarm payrolls on Friday, could threaten the recent market rally.\
""“We primarily attribute the S&P 500′s sharp +9% rebound over the past 10 trading days to seemingly never-ending hopes for a ‘Fed pivot,’ which [the] market is apparently defining as a +75bps hike this week followed by a +50bps move in December,” said Wolfe Research’s Chris Senyek in a note to clients Monday. “Our sense is that investors are more likely than not to be disappointed on Wednesday afternoon.""”\
Earnings season continues this week with reports from Uber, Pfizer and Advanced Micro Devices."

# load spacy package
nlp = spacy.load('en_core_web_sm')

doc = nlp(text)

print("====================")
for sentence in doc.sents:
    print(sentence)
print("====================")
