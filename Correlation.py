import numpy as np
import csv
import plotly.express as px
def plotFigure(dataPath):
    with open(dataPath) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x='Temperature',y='Ice-cream Sales( ₹ )')
        fig.show()

def getDataSource(dataPath):
    iceCreamSales=[]
    coldDrinkSales=[]
    with open(dataPath) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            iceCreamSales.append(float(row['Temperature']))
            coldDrinkSales.append(float(row['Ice-cream Sales( ₹ )']))
    return{'x':iceCreamSales,'y':coldDrinkSales}
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between Temperature and Ice Cream sales:/n',correlation[0,1])
def setup():
    dataPath='./Temperature.csv'
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)
setup()