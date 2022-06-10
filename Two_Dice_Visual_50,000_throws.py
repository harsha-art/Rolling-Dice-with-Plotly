from plotly.graph_objs import Bar,Layout
from plotly import offline
from dice_class import Dice 

#Objects Of The Dice Class 
die1 = Dice()
die2 = Dice()

#We Generate Random Values for the throws 50,000 times 
results=[die1.roll()+die2.roll() for x in range(50000)] 

#Max Value Of The Dice 
max_value = die1.nums_of_side + die2.nums_of_side

#We calculate The frequency of each throw
frequencies = [results.count(f) for f in range(2,max_value+1)]

#X-Coordinate Values
xvalues = [x for x in range(2,max_value+1)]

#We Make A Bar Graph Here 
data = [Bar(x = xvalues , y = frequencies )]

#We set a title for the x and y axises.
x_layout_attributes = {'title':'Number on Two D6 Dice','dtick':1}
y_layout_attributes = {'title':'Frequency Of Number'}

#Generate the graph 
mylayout = Layout(title = 'Rolling Two Dice 50,000 times',xaxis = x_layout_attributes ,yaxis = y_layout_attributes)
offline.plot({'data':data,'layout':mylayout},filename = "Two D2 50,000 times.html" )
