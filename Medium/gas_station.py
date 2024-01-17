class Solution:
  """
  There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
  You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
  You begin the journey with an empty tank at one of the gas stations.
  Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
  otherwise return -1. If there exists a solution, it is guaranteed to be unique
  """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ## Double pass solution O(2n)
        n = len(cost)
        Gas = gas+gas
        Cost = cost+cost
        i,j = 0,0
        balance = 0

        while j-i < n:
            balance += Gas[j]-Cost[j]
            if balance < 0:
                balance = 0
                i = j+1
            j += 1
            if i >= n:
                return -1
        return i

        ## Single pass solution
        start = 0
        balance = 0
        deficit = 0
        n = len(gas)
      
        for i in range(n):
            balance += gas[i]-cost[i]
            if balance < 0:
                start = i+1
                deficit += balance
                balance = 0
        if deficit+balance >= 0:
            return start
        else: return -1
