class MyStack:

    stack = []

    def __init__(self):
        print "[MyStack.__init__] entered the stack class"

    '''
    get_stack()
    args: none
    returns: the list stack
    '''
    def get_stack(self):
        print "[MyStack.get_stack] returning stack from class"
        return self.stack

    '''
    push()
    args: a value that has to be inserted in the front of the list
    returns: the list stack with the given value inserted at the front of the list
    '''
    def push(self, val):
        print "[MyStack.push] pushing ", val
        self.stack.insert(0, val)

    '''
    pop()
    args: none
    returns: the value that has been popped from the head of the stack
    ***: we create a temporary list and enter all elements from the stack to that list
        minus the first element of the stack.  We then put back all elements from that list
        into the stack
    '''
    def pop(self):
        print "[MyStack.pop] popping ", self.stack[0]
        poppedVal = self.stack[0]

        anotherStack = []
        for i in range(1, len(self.stack)):
            anotherStack.append(self.stack[i])

        self.stack = anotherStack
        return poppedVal

    '''
    get_last()
    args: none
    returns: The last element of the stack (the first element that was entered into the stack)
    '''
    def get_last(self):
        print "[MyStack.get_last] getting the last item"
        if len(self.stack) == 0:
            return
        else:
            return self.stack[len(self.stack) - 1]

    '''
    args: none
    returns: The first element of the stack (the element that was entered last)
    '''
    def get_first(self):
        print "[MyStack.get_first] getting the first item"
        if len(self.stack) == 0:
            return
        else:
            return self.stack[0]

    '''
    peek()
    args: none
    returns: Calls the get_first() and returns the head of the stack without popping it
    '''
    def peek(self):
        print "[MyStack.peek] peeking, returning the first element without popping"
        return self.get_first()


anInstance = MyStack()
anInstance.push(5)
anInstance.push(4)
anInstance.push(3)
lastItem = anInstance.get_last()
firstItem = anInstance.peek()
print "first item is ", firstItem
print "last item is ", lastItem
popper = anInstance.pop()
print "popped value returned to main is ", popper
returnedStack = anInstance.get_stack()
print returnedStack