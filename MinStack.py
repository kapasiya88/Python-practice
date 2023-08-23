# https://leetcode.com/problems/min-stack/description/

# MinStack() initializes the stack object
class MinStack:

    def __init__(self):
        self.st=[] #stack
        self.min=None #min element

#  pushes the element val onto the stack.
    def push(self, val: int) -> None:
         self.st.append(val)
                
#  removes the element on the top of the stack.
    def pop(self) -> None:
        x=self.st.pop()
    
#  gets the top element of the stack.
    def top(self) -> int:
        x=self.st[-1]
        return x

#  retrieves the minimum element in the stack.
    def getMin(self) -> int:
        x=min(self.st)
        return x


# Example:
# Input:
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# param_4 = obj.getMin()
# print(param_4)
# obj.pop()
# param_3 = obj.top()
# print(param_3)
# param_4 = obj.getMin()
# print(param_4)

# Output:[null,null,null,null,-3,null,0,-2]