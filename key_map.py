
#Author: Michael Milicevich
#Class that maps the datastore key of a building's appliance to the appliance's actual name
#used for quick testing


class Key_map(object):


	def __init__(self, building = 1):
		self.map = {}
		self.load_map(building)


	def load_map(self, building):

		if building == 1:
			self.map['mains1'] ='/building1/elec/meter1' 
			self.map['mains2'] ='/building1/elec/meter2' 
			self.map['fridge'] ='/building1/elec/meter5' 
			self.map['dish washer'] ='/building1/elec/meter6' 
			self.map['sockets1'] ='/building1/elec/meter7' 
			self.map['sockets2'] ='/building1/elec/meter8' 
			self.map['light1'] ='/building1/elec/meter9' 
			self.map['microwave'] ='/building1/elec/meter11' 
			self.map['unknown1'] ='/building1/elec/meter12' 
			self.map['electric space heater'] ='/building1/elec/meter13' 
			self.map['electric stove'] ='/building1/elec/meter14' 
			self.map['sockets3'] ='/building1/elec/meter15' 
			self.map['sockets4'] ='/building1/elec/meter16' 
			self.map['light2'] ='/building1/elec/meter17' 
			self.map['light3'] ='/building1/elec/meter18' 
			self.map['unknown2'] ='/building1/elec/meter19'
			self.map['washer dryer'] ='/building1/elec/meter10_20'
			self.map['electric oven'] ='/building1/elec/meter3_4'
		else:
			print("Building application key map cannot be found")

	def list_appliances(self):
		for key in self.map:
			print(key)

	def get_key(self, apl):
		return self.map[apl]

