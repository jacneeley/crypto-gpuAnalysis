resale<-read.table(file="C:/Users/Jacne/Documents/python/visualization_and_datamining/data/dataminingProject/btc_gpu_mktData.csv",sep=',',header = TRUE)
attach(resale)
head(resale)
round(cor(resale[c(-1,-2)]),4) #positive correlation between btc_Price and given gpu Price
summary(resale)


#Linear Regression Model - Summarize Data

#Most popular mining gpus - based on google search
#gpu_Price as a predictor for btc_Price
o1<-lm(btc_Price~GeForce.RTX.3090)#powerhouse,work-horse
s1<-summary(o1)
o2<-lm(btc_Price~Radeon.RX.6700.XT)#durability, and efficient, all at a good price
s2<-summary(o2)

#Best Radeon on the mkt
o3<-lm(btc_Price~Radeon.RX.6900.XT)


o6<-lm(btc_Price~Radeon.RX.6700.XT+GeForce.RTX.3090)
o7<-lm(btc_Price~GeForce.RTX.3090+Radeon.RX.6900.XT)


#alternatively, btc_price as a predictor for gpu price
o4<-lm(GeForce.RTX.3090~btc_Price)
o5<-lm(Radeon.RX.6700.XT~btc_Price)

#btc relative to gpu
plot(btc_Price~GeForce.RTX.3090)
plot(o1)

plot(btc_Price~Radeon.RX.6700.XT)
plot(o2)

plot(btc_Price~GeForce.RTX.3090)




#is btc_price a good predictor for a given gpu price?
p1<-predict(o1)
p2<-predict(o2)

#residuals
r1<-residuals(o1)
r2<-residuals(o2)

#increasing or decreasing variance? - Increasing/Decreasing , significantly. -> bad b/c non-constant.
plot(r1~p1,xlab="predicted",ylab="Residuals")
plot(r2~p1,xlab="predicted",ylab="Residuals")
plot(o1)
#estimates for this models coefficients are not reliable
###########################################################################################

#samples model - bit coin prices and GPU ebay prices were taken over the last 1.5 -> 2 years.
mktsamples<-read.table(file="C:/Users/Jacne/Documents/python/visualization_and_datamining/data/dataminingProject/btc_gpu_mktSamples.csv",sep=',',header = TRUE)
attach(mktsamples)
head(mktsamples)
round(cor(mktsamples[c(-1)]),4)
summary(mktsamples)


#GPU eBAY Price relative to bitcoin Price
plot(eBay.Price~btc_Prices)
abline(a=mean(eBay.Price),b=0,col="green")


#Assumptions - Does our model violate any of the Linear Regression assumptions?
#predict and residual equations
p1<-predict(lm(eBay.Price~btc_Prices))
ro2<-residuals(lm(eBay.Price~btc_Prices))

#residuals vs predicted, are the residuals' variance increasing/decreasing or constant?
plot(ro2~p1,xlab="predicted",ylab="Residuals")
abline(a=mean(ro2),b=0,col='green')
#most data is constant, scattered randomly, constant variance.
#create residuals vs fitted
f1<-lm(eBay.Price~btc_Prices+factor(GPU))
plot(f1)

#does the model violate normality of residuals?
require(nortest)
library(nortest)
#Null hypothesis is that the residuals are normally distributed
lillie.test(ro2)

#are the residuals autocorrelated?
acf(ro2) #passes assumption? residuals are independent? I think? Need help interpreting this...


plot(eBay.Price~btc_Prices)
#regression line that will help us predict values we have not observed
abline(a=lm(eBay.Price~btc_Prices),b=0,col='red')

#Linear Regression Model - Summarize data
o1<-lm(eBay.Price~btc_Prices)
#Let's say alpha = .05. H_null: bit coin prices have no affect on gpu ebay prices
summary(o1)
#p-value = 2.2e-16; smaller than any reasonable alpha. Reject Null hypothesis.
#we can only explain about 30-32% of our eBay prices currently...
#Adjusted R-squared:  0.3059

#what about our expected eBay prices if btc was 0?
#b0 = 4.684e+02 = 468.40

#add 1000 units
#468.40* 1000 = 468400

#can using factor(GPU) improve the model?
summary(f1)
#Multiple R-squared:  .8825,	Adjusted R-squared:  .8742!!!

#################################################################################
#forward building our model. Do we include QTY Sold?
#let's look at correlation again.
round(cor(mktsamples[c(-1)]),4)
#QTY sold is not as strongly correlated as btc_price

#Will creating a more complex model, a model that includes QTY sold, be a better predictor than our previous model?
o2<-lm(eBay.Price~btc_Prices+QTY.Sold)
summary(o2)
#Multiple R-squared:  .3148,	Adjusted R-squared:  0.3109 ; good in-comparison to o1

f2<-lm(eBay.Price~btc_Prices+QTY.Sold+factor(GPU))
summary(f2)
#Multiple R-squared:  .886,	Adjusted R-squared:  .8775; when we factor gpu, we should include QTY sold.

###################################################################################
#create training and test sets
K=50
MAE = array(dim=c(K))
MSE = array(dim=c(K))
out = array(dim=c(K))
for (i in 1:K){
  randrows<- sample(1:nrow(mktsamples),nrow(mktsamples)*(0.7))
  
  #randrows go into training, rest goes into test
  training<-mktsamples[randrows,] #70% of the data to represent training
  test<-mktsamples[-randrows,] #30% of the data to represent test 
  
  
  attach(training)
  o=lm(eBay.Price~btc_Prices+QTY.Sold+factor(GPU)) #O does not contain any of the predictions, only the data we want to predict
  predict(o,newdata = test)
  
  #get eBay.Prices of test
  attach(test)
  
  #assuming we have a valid model, MAE will tell you how many errors on average
  MAE[i]<-mean(abs(eBay.Price-predict(o,newdata = test))) 
  MSE[i]<-mean(abs(eBay.Price-predict(o,newdata = test))^2)
  out[i]<-sum((eBay.Price<pred[,2])|(eBay.Price>pred[,3]))/length(eBay.Price)
}

predict(o,newdata = test, interval = "prediction")
pred<- predict(o,newdata = test, interval = "prediction")


