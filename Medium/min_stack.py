class MinStack:
  """
  Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

  Implement the MinStack class:
  
  MinStack() initializes the stack object.
  void push(int val) pushes the element val onto the stack.
  void pop() removes the element on the top of the stack.
  int top() gets the top element of the stack.
  int getMin() retrieves the minimum element in the stack.
  You must implement a solution with O(1) time complexity for each function.
  """

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        if not self.arr:
            self.arr.append((val, val))
        else:
            if val < self.arr[-1][1]:
                self.arr.append((val, val))
            else: 
                self.arr.append((val, self.arr[-1][1]))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
