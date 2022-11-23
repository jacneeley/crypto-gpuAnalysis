resale<-read.table(file="C:/Users/Jacne/Documents/python/visualization_and_datamining/data/dataminingProject/btc_gpu_mktData.csv",sep=',',header = TRUE)
attach(resale)
head(resale)
round(cor(resale[c(-1,-2)]),4)

#Linear Regression Model - Summarize Data
o1<-lm(GeForce.RTX.3090~btc_Price)
summary(o1)

#looking at things the other way
#o2<-lm(btc_Price~GeForce.RTX.3090)
#summary(o2)

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