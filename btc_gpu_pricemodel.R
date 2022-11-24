resale<-read.table(file="C:/Users/Jacne/Documents/python/visualization_and_datamining/data/dataminingProject/btc_gpu_mktData.csv",sep=',',header = TRUE)
attach(resale)
head(resale)
round(cor(resale[c(-1,-2)]),4)
summary(resale)

#Linear Regression Model - Summarize Data

#Most popular mining gpus
o1<-lm(GeForce.RTX.3090~btc_Price)
summary(o1)
o7<-lm(Radeon.RX.6700.XT~btc_Price)
summary(o7)

#looking at things the other way
#o2<-lm(btc_Price~GeForce.RTX.3090)
#summary(o2)

#powerful cards
o2<-lm(GeForce.RTX.3080.T~btc_Price)
summary(o2)

o3<-lm(GeForce.RTX.3080~btc_Price)
summary(o3)

o4<-lm(Radeon.RX.6900.XT~btc_Price)
summary(o4)

o5<-lm(Radeon.RX.6800.XT~btc_Price)
summary(o5)

o6<-lm(Radeon.RX.6800~btc_Price)
summary(o6)

#don't think this one is useful, just wanted to see what it would look like.
o8<-lm(btc_Price~GeForce.RTX.3090)
summary(o8)

o9<-lm(btc_Price~GeForce.RTX.3090+Radeon.RX.6700.XT)
summary(o9)


#btc relative to gpu
plot(GeForce.RTX.3090~btc_Price)
plot(o1)

plot(Radeon.RX.6700.XT~btc_Price)
plot(o7)


plot(btc_Price~GeForce.RTX.3090)


#is btc_price a good predictor for a given gpu price?
p1<-predict(o1)
p2<-predict(o7)

#residuals
r1<-residuals(o1)
r2<-residuals(o7)

#increasing or decreasing variance?
plot(r1~p1,xlab="predicted",ylab="Residuals")
plot(r2~p1,xlab="predicted",ylab="Residuals")
