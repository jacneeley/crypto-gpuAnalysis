# crypto-gpuAnalysis

## purpose:
- mine data
- analyze data
- construct a forward built Linear Regression Model
- build a model using training and test sets to predict After Market Graphics Cards Prices
- Test for Linear Regression violations.

## Overview
The following was a Academic group research assignment. The final report was completed in Fall of 2022.<br>
For the project, we were to pretend we were data analysts for a company that sold computer parts. <br>
We wanted to see if there was any correlation with Bitcoin prices and After Market GPU prices as GPU's are crucial for crypto currency mining.<br>

Sources for Data:
- [Tom’s Hardware, GPU Prices: Tracking Graphics Cards Sold on eBay](https://www.tomshardware.com/news/lowest-gpu-prices)
- [BlockChain.com | Charts – Bitcoin MKT Price (USD), Last 3 years](https://www.blockchain.com/explorer/charts/market-price) *as of 2022*

## Abstract
It is essential to note that several factors can influence Graphics Cards' after-market prices. These
factors include, but are not limited to, the following:
- Inflation
- 2020-Present global supply chain crisis.
  - Global Chip Shortage
- Potential trend relating to BTC Prices

The focus of this study was to investigate the correlation between Bitcoin valuations and
various price points that GPU models sold for on the popular eBay marketspace. After our
analysis, we reject our null hypothesis that the valuation of Bitcoin does not affect after-market
GPU prices.
Crypto experienced an all-time high back in November 2021, now 1 year later Bitcoin
has fallen to about $16K from its all-time high of $67,572 (back in Nov. 08, 2021). During the
global pandemic, GPU’s have been well above MSRP. Now that crypto currencies like Bitcoin
have fallen, GPU prices have begun to fall. Correlation does not equal causation, but it was
interesting to see since powerful GPUs are needed to mine cryptocurrency effectively.
Assume we are a company that sells new and secondhand GPUs. With our observations,
we built a model using bit coin prices from the last 3 years and the average GPU prices from the
last 25 months (about 2 years). Unfortunately, we found that our model would not be a great
predictor for after-market GPU prices. In the context of our data, the model violated several
linear regression assumptions. We found that the correlation between the eBay Prices and
BTC_Prices that we observed was only .4929. When adding QTY sold and factoring for each
GPU in our model, we increased the quality of our model (Adj. R-Squared increased) and found
that we could explain 86.43% of the variations. We were able to conclude that Bitcoin price does
in fact influence after-market (ebay) GPU prices, but as mentioned earlier, our model is not a
great predictor. Our model’s predictions severally underpredict values when compared to what
we observed. In some cases, we greatly overpredict values in comparison to what we observed.
Based on these findings, we believe that our model is not currently capable of correctly
predicting eBay Prices when controlling for the independent variable BTC_Price and outside
factors. An effective model could help us maximize our profits as efficiently as possible by
giving us insights into what prices we should be selling our products at, especially high
performing GPU

## Conclusions
With our observations, we constructed a forward-Built MLR. Using bitcoin prices from
the last 3 years, and average GPU prices from the last 25 months (about 2 years). Our model
violated 2 linear assumption tests. It is reasonable to believe that the statistically insignificant
GPUs present in our data caused our model to suffer, and that our model does not predict values
better than the dependent variables intercept, even though our complex model was a better
predictor than our simple model. The only thing we were able to conclude in this study is that we
can reject the Null Hypothesis that states that btc_Price has no effect on GPU eBay Prices;
however, given our observations we were not able to adequately create predictions based on
btc_Prices that would provide business value for the company at this time.

[Full Report>>](https://github.com/jacneeley/crypto-gpuAnalysis/blob/main/Crypto%20GPU%20Analysis.pdf)
