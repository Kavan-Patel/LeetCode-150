# 134.Gas Station
# https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # Here first we check sum of total gas and total cost 
        # if sum of gas is less then we can't complete entire round
        # Here we're returning -1
        if sum(gas) < sum(cost):
            return -1
        # If solution exist then we assign starting index at 0th position
        # and total_tank initially 0
        start_index = 0
        tank_capacity = 0
        for i in range(len(gas)):
            # Update the total tank at perticuler stop and calculate 
            # how much gas will use to reach next station
            tank_capacity += (gas[i] - cost[i])
            # if any point tank_capacity every dropped to -ve
            # We update the start index to next position
            # and reset the tank_capacity
            if tank_capacity < 0:
                start_index = i+1
                tank_capacity = 0
        
        return start_index