import math
'''
Inputs:
  first_city(list) : the coordinates of first city where the salesman will start his journey
  list_of_cities(list of lists) : the cities that are schecduled to be visited , list of tuples , each tuple has two elements: xi,yi

output:
  total_distance(float): the shortest route that passes by all cities

Note: i/p with lists is availabe , I tried list of tuples but I had difficulities with the python language interpreter

Algorithm:
  using greedy algorithm , in an inner loop we calculate the city with the shortest distance with the first city ,
  I save this distance in variable total_distance , when I find it , I remove this city from the list and caculate
  again the distance between the removed city and the remaining cities in the list untl the list of cities has no
  elemnts left , and the tatal_distance is incremented
'''

def calc_distance(first_city, next_city):
    distance =  math.sqrt((next_city[0] - first_city[0])**2 + (next_city[1] -first_city[1])**2)
    return distance

def tsm( first_city ,list_of_cities):
    total_distance = 0 
    temp_distance = 10000000  #variable to calculate distancw between two cities , start with very large number
    

    while(len(list_of_cities)>0):
        for i in list_of_cities:
            if calc_distance(first_city ,i) < temp_distance:
                temp_distance = calc_distance(first_city ,i)
                next_city = i
                print(i , temp_distance  , total_distance)
        total_distance += temp_distance 
        list_of_cities.remove(i)
    return total_distance

