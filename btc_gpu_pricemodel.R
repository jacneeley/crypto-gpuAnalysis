resale<-read.table(file="C:/Users/Jacne/Documents/python/visualization_and_datamining/data/dataminingProject/btc_gpu_mktData.csv",sep=',',header = TRUE)
attach(resale)
head(resale)
round(cor(resale[c(-1,-2)]),4)
summary(resale)

#Linear Regression Model - Summarize Data

#Most popular mining gpus
o1<-lm(btc_Price~GeForce.RTX.3090)
summary(o1)
o2<-lm(btc_Price~Radeon.RX.6700.XT)
summary(o2)


#btc relative to gpu
plot(btc_Price~GeForce.RTX.3090)
plot(o1)

plot(btc_Price~Radeon.RX.6700.XT)
plot(o2)

plot(btc_Price~GeForce.RTX.3090)

o3<-lm(btc_Price~GeForce.RTX.3090+Radeon.RX.6700.XT)


#is btc_price a good predictor for a given gpu price?
p1<-predict(o1)
p2<-predict(o2)

#residuals
r1<-residuals(o1)
r2<-residuals(o2)

#increasing or decreasing variance?
plot(r1~p1,xlab="predicted",ylab="Residuals")
plot(r2~p1,xlab="predicted",ylab="Residuals")
