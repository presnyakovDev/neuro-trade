import numpy as np

class Dataset:
    def __init__(self, json):
        self.close = []
        self.date = []
        self.changePercent = []
        self.averagePrice = []
        self.dataX = []
        self.volume = []
        self.dataY = []
        for i in range(len(json)):
            self.dataY.append([0])
        for i in range(len(json)):
            self.close.append(json[i]['close'])
            self.changePercent.append(json[i]['changePercent'])
            self.date.append(json[i]['date'])
            self.volume.append(json[i]['volume'])
            if i > 0 :
                self.averagePrice.append(sum(self.close)/len(self.close))
            else :
                self.averagePrice.append(self.close[i])
            if json[i]['date'] == '2018-07-20':
                self.dataY[i] = [1];
            if json[i]['date'] == '2018-07-03':
                self.dataY[i] = [1];
            if json[i]['date'] == '2018-05-30':
                self.dataY[i] = [1];
            self.dataX.append([self.close[i], self.changePercent[i], self.averagePrice[i]])
            self.X = np.array(self.dataX)
            self.y = np.array(self.dataY)

    def printState(self):
        print(self.X)
        #print(len(self.dataX))
        #print(self.y)
        #print(self.date)
        #print(self.changePercent)
        #print(self.averagePrice)
