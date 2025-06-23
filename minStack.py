class minStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val):
        self.stack.append(val)
        print(self.stack)
        
        val = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    def top(self):
        print(self.stack[-1])
    def getMin(self):
        print(self.minStack[-1])
