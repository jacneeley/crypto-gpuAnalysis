resale<-read.table(file="C:/Users/Jacne/Documents/python/visualization_and_datamining/data/dataminingProject/btc_gpu_mktData.csv",sep=',',header = TRUE)
attach(resale)

cor(resale[c(-1,-2)])
