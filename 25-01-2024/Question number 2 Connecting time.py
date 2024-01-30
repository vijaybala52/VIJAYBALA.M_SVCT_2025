# Cities on a map are connected by a number of roads. The number of roads between each city is in an array and city  is the starting location. The number of roads from city  to city  is the first value in the array, from city  to city  is the second, and so on. 

# How many paths are there from city  to the last city in the list, modulo ? 

# Example 


# There are  roads to city ,  roads to city  and  roads to city . The total number of roads is . 

# Note 
# Pass all the towns Ti for i=1 to n-1 in numerical order to reach Tn. 

# Function Description 

# Complete the connectingTowns function in the editor below. 

# int n: the number of towns 
# int routes[n-1]: the number of routes between towns 
# Returns 

# int: the total number of routes, modulo 1234567. 
# Input Format 
# The first line contains an integer T, T test-cases follow. 

# The first line contains an integer N (the number of towns). 
# The second line contains N - 1 space separated integers where the ith integer denotes the number of routes, Ni, from the town Ti to Ti+1 

# Constraints 
# 1 <= T<=1000 
# 2< N <=100 
# 1 <= routes[i] <=1000 

# Sample Input 

# 2 
# 3 
# 1 3 
# Sample Output 

# 3 
# 8 



def connectingTowns(n, routes): 
    total_routes = 1 
    for route in routes: 
        total_routes = (total_routes * route) % 1234567 
    return total_routes 
t = int(input()) 
for _ in range(t): 
    n = int(input()) 
    routes = list(map(int, input().split())) 
    result = connectingTowns(n, routes) 
    print(result)
