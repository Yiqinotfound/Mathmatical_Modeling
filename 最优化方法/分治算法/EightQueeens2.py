
# This function calculates the number of conflicts between queens in a given status
# status: a list representing the position of queens on the chessboard
# returns: the number of conflicts between queens in the given status
def num_of_conflict(status):
    num_of_conflict = 0
    for col1 in range(0, 7):
        for col2 in range(col1+1, 8):
            # Check if two queens are attacking each other
            if (status[col1] == status[col2]) \
            or ((col2 - col1) == abs(status[col1] - status[col2])):
                num_of_conflict += 1
    return num_of_conflict
 
 
 
# This function returns a new status based on the decreasing T and the current status
# status: a list representing the position of queens on the chessboard
# T: the current temperature
# returns: a new status based on the decreasing T and the current status
def get_next_num_of_conflict_status(status, T):
    next_status = [] # Store the 56 neighbors of the current status
    
    for col in range(0,8):
        for row in range(0, 8):
            new_status = status.copy()
            if status[col] != row:
                new_status[col] = row
                next_status.append(new_status)
    choose_status = random.randint(0, 55) # Choose one from the 56 neighbors
    if num_of_conflict(next_status[choose_status]) <= num_of_conflict(status): # If the new status is better than the original
        return next_status[choose_status]
    else: # If the original status is better than the new status
        E = num_of_conflict(status) - num_of_conflict(next_status[choose_status])
        probability = math.e**(E/T) # Probability calculation formula
        choose = random.random()
        if choose <= probability: # With a certain probability, the new status replaces the original status
            return next_status[choose_status]
    return status  # Return the original status without moving
 
 
 
 
 
 
 
# This code uses the simulated annealing algorithm to solve the eight queens problem
import random
import math

status = [0, 0, 0, 0, 0, 0, 0, 0]
for col in range(0, 8):
    row = random.randint(0, 7)
    status[col] = row
print("the initial status: ")
print(status)
print("the num of conflict: ")
print(num_of_conflict(status))
T = 5.0 # Initial temperature
while num_of_conflict(status) > 0: # While the optimal solution is not found
    new_status = get_next_num_of_conflict_status(status, T) # Get a new status
    if new_status == status: # If no move is made
        print("E < 0, but no move") # 
    else: 
        status = new_status
        print("the new status: ")
        print(status)
        print("the num of conflict: ")
        print(num_of_conflict(status))
        if num_of_conflict(status) == 0:
            print("find a answer!")
            break
    T = T * 0.99  # Decrease T and probability
    if T < 0.0001:  # After 1077 iterations, T is considered to be close to 0
        print("T = 0, can't find a answer")
