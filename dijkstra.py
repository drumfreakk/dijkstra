#!/usr/bin/env python3

# distance to each city from A = infinity
# (distance to A = 0)
# iterate through cities, if distance < previous smallest distance thereto replace it
# repeat for city with shortest distance from there
# get distance by adding current distance to distance from current city to next
# once checked all options for one city mark it as visited, if visited dont repeat
# next city to go to is one with smallest distance from original city
# and like if you decide going via one city is best then you later get the route from doing pathfinding (or remembering what you did previously) to get to that better second-to-last city

# table:
#	city (int)	visited (bool)	distance (int)	via (int)

class Network:
	def __init__(self):
		self.roads = []
		self.cities = []

		self.road_order = []

	def create_city(self, name):
		self.cities.append({"name":name, "visited":False, "tentative":-1, "via": -1})

	def create_cities(self, names):
		for name in names:
			self.create_city(name)

	def create_road(self, city_a, city_b, distance):
		self.roads.append({"connects":[city_a, city_b], "distance":distance})

	def create_roads(self, roads):
		for road in roads:
			self.create_road(road[0], road[1], road[2])

	def get_index(self, city):
		for i in range(0, len(self.cities)):
			if self.cities[i]["name"] == city:
				return i

	def set_starting_city(self, city):
		self.cities[self.get_index(city)]["tentative"] = 0

	def set_options_for_city(self, city):
		self.road_order = []
		for i in range(0, len(self.roads)):
			if self.roads[i]["connects"][0] == city or self.roads[i]["connects"][1] == city:
				self.road_order.append(self.roads[i])
		self.road_order.sort(key=lambda road: road["distance"])	

	def check(self, city):
		if self.cities[self.get_index(city)]["visited"] == True:
			return

		self.set_options_for_city(city)
#		print(city)
		for road in self.road_order:
			current = self.cities[self.get_index(city)]["tentative"]
			for dest in road["connects"]:		# Get the destination city (ie. the one on the road that isnt the current one)
				if dest != city:
					destination_city = dest

#			print(road)

			dest_index = self.get_index(destination_city)
#			print(dest_index)
			tentative = self.cities[dest_index]["tentative"]
			
			if tentative == -1 or current + road["distance"] < tentative:
				self.cities[dest_index]["tentative"] = current + road["distance"]
				self.cities[dest_index]["via"] = city
		
		self.cities[self.get_index(city)]["visited"] = True
	
#		if city == 1:
#			print(self.road_order)
#			exit()

		check_order = self.road_order
		for unvis in check_order:
			for dest in unvis["connects"]:
				if dest != city:
					new = dest
			self.check(new)


	def __repr__(self):
		roads = ""
		cities = ""
		for road in self.roads:
			roads = "%s\n%s" % (roads, road)
		for city in self.cities:
			cities = "%s\n%s" % (cities, city)
		return "Network:\nroads: %s\n\ncities: %s" % (roads, cities)

#TODO add check to end

n = Network()
for i in range(0, 14):
	n.create_city(i)
#roads = [[0,1,1],[0,2,6],[0,3,7],[1,2,5],[1,3,2],[2,3,1]]
roads = [[0,1,20],
		 [0,2,60],
		 [0,3,47],
		 [0,8,57],
		 [0,11,136],
		 [1,2,56],
		 [1,3,56],
		 [1,11,152],
		 [2,3,61],
		 [2,4,120],
		 [2,5,105],
		 [2,13,155],
		 [3,6,66],
		 [3,8,76],
		 [3,13,86],
		 [4,5,146],
		 [5,6,70],
		 [5,7,122],
		 [5,13,51],
		 [6,8,89],
		 [6,9,67],
		 [6,13,19],
		 [7,13,138],
		 [8,9,53],
		 [8,11,104],
		 [9,10,81],
		 [9,11,98],
		 [10,11,86],
		 [10,12,27],
		 [11,12,63]]

n.create_roads(roads)


# Starting city is 0
n.set_starting_city(2)
n.check(2)
print(n)



