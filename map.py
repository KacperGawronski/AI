import numpy as np
import matplotlib.pyplot as plt
menu = { 
"":0,
"kawa":20,
"pomidorowa":10,
"grochowa":10,
"pierogi":30,
"kopytka":25
}
int_to_menu=menu.keys()

directions={
	'H':np.array([0,0]),
	'N':np.array([-1,0]),
	'S':np.array([1,0]),
	'E':np.array([0,1]),
	'W':np.array([0,-1])
}

class Kelner:
	def clear_orders(self):
		self.orders=np.array([0 for x in range(len(int_to_menu))]
	def __init__(self,y,x):
		self.clear_orders()
		self.position=np.array([x,y])
		self.contain=np.array([0 for x in range(len(int_to_menu))]
	def move(self,direction):
		self.position+=directions[direction]
	def get_pos(self):
		return self.position

def decrease_second(x):
	return (x[0],x[1]-1)
	
class Environment:
	def __init__(self,width,height,x=None):
		self.maxx=width-1
		self.maxy=height-1
		if x is None:
			wh=width*(height-1)
			self.grid = np.hstack((np.random.permutation(np.hstack((np.ones(wh//10,dtype='byte'),np.zeros(wh-wh//10,dtype='byte')))),np.zeros(width,dtype='byte'))).reshape((height,width))
		self.kelner=Kelner(width-1,height-1)
		self.t=0
		self.todos = []
		self.waiting = np.array([0 for i in range(len(int_to_menu))])
	def get_grid(self):
		return self.grid
	def action(self,direction):
		self.todos=[map(decrease_second,self.todos)]
		self.waiting.extend([map(lambda x:x[0],filter(lambda x:x[1]<=0,self.todos))])
		self.todos=[filter(lambda x:x[1]>0,self.todos)]
		pos=tuple(self.kelner.get_pos()+directions[direction])
		if pos[0]>=0 and pos[1]>=0 and pos[0]<=self.maxy and pos[1]<=self.maxx then:
			self.kelner.move(direction)
			if direction=='H':
				if pos[0]==self.maxy:
					for k,v in enumerate(kelner.orders[1:]):
						self.todos.extend([(k,menu[int_to_menu[k]])]*v)
					kelner.clear_orders()
					
					
		else:
			return 'e'

e=Environment(20,20)
print(e.get_grid())
print(e.kelner.get_pos())
e.action('W')
print(e.kelner.get_pos())
