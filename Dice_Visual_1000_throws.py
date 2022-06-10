from dice_class import Dice
from plotly.graph_objs import Bar, Layout
from plotly import offline

dice = Dice()

results = []

#We Roll A Die 1000 Times Using A Loop
for x in range(0,1000):
	result = dice.roll()
	results.append(result)

frequencies = []

#We Calculate The Frequency Using A Loop
for x in range(1,dice.nums_of_side+1):
	frequency = results.count(x)
	frequencies.append(frequency)

#X-Coordinate Values
x_values = list(range(1,dice.nums_of_side+ 1))

#We Genrate the Bar Graph 
data = [Bar(x=x_values,y=frequencies)]

#We set a title for the x and y axises.
x_axis_config = {'title':'Number On Die'}
y_axis_config = {'title':'Frequency Of Number'}

#Generate the graph 
my_layout = Layout(title = "Rolling A Dice 1000 times",xaxis = x_axis_config,yaxis = y_axis_config)
offline.plot({'data': data,'layout':my_layout},filename = "Dice_1000.html")

