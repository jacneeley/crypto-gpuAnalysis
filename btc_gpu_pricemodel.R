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

#increasing or decreasing variance?
plot(r1~p1,xlab="predicted",ylab="Residuals")
plot(r2~p1,xlab="predicted",ylab="Residuals")
