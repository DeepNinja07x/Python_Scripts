# pip install matplotlib
import matplotlib.pyplot as graph

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul"]
scores = [100,130,125,90,20,50,70]

graph.plot(months,scores,color=(0/255,0/255,255/255),marker = "+",markersize = 10,markeredgewidth = 2,
linewidth = 2,linestyle = "dotted", markeredgecolor = (255/255,0,0)) 
# The colour code is in RGB. Make sure you divide it by 255 (values have to be between 0 and 1)
graph.title("Monthly Analysis")
graph.xlabel("Months")
graph.ylabel("Stocks Sold")
graph.show()