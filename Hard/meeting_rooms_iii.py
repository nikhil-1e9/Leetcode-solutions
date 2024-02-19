class Solution:
  """
  You are given an integer n. There are n rooms numbered from 0 to n - 1.

  You are given a 2D integer array meetings where meetings[i] = [starti, endi] 
  means that a meeting will be held during the half-closed time interval [starti, endi). 
  All the values of starti are unique.
  
  Meetings are allocated to rooms in the following manner:
  
  - Each meeting will take place in the unused room with the lowest number.
  - If there are no available rooms, the meeting will be delayed until a room becomes free. 
    The delayed meeting should have the same duration as the original meeting.
  - When a room becomes unused, meetings that have an earlier original start time should be given the room.
  - Return the number of the room that held the most meetings. 
    If there are multiple rooms, return the room with the lowest number.
  
  A half-closed interval [a, b) is the interval between a and b including a and not including b.
  """
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()
        # Create 2 min heaps one for knowing meeting end times and one for knowing which rooms are currently empty
        heap = []
        empty = [x for x in range(n)]
        heapify(empty)
        # hash map to store the frequency of the rooms 
        rooms = defaultdict(int)
        
        for start, end in meetings:
            # Choose the lowest room number that has completed the last meeting
            while heap and start >= heap[0][0]:
                _, room = heappop(heap)
                heappush(empty, room)
            # If there is an empty room keep that for current meeting
            if empty:
                emptyRoom = heappop(empty)
                heappush(heap, (end, emptyRoom))
                rooms[emptyRoom] += 1
            # If no rooms are empty wait for the meeting which will end earliest and then use that room
            else:
                prevEnd, room = heappop(heap)
                start, end = prevEnd, prevEnd - start + end
                heappush(heap, (end, room))
                rooms[room] += 1

        # Find which room was used most number of times
        mostMeets = 0
        for room, meets in rooms.items():
            if meets > mostMeets:
                mostMeets = meets
                roomNum = room
        
        return roomNum
            
