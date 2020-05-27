# TODO : complete check operators function
from stack import Stack
# checker class check on balanced brackets and math operations
class Checker:
    def __init__(self, target):
        self.leftBracket = ['(','{','[']
        self.rightBracket = [')','}',']']
        self.operators = ['+','-','*','/']
        self.target = target

    # check on palanced brackets
    def checkBrackets(self):
        stack = Stack()
        for i in list(self.target):
            if i in self.leftBracket:
                stack.push(i)
            elif i in self.rightBracket:
                if stack.isEmpty() or not self.isPairBracket(stack.getTop(), i):
                    return False
                else:
                    stack.pop()
        return stack.isEmpty()

    # check if left in leftBracket is equal to right in rightBracket
    def isPairBracket(self, left, right):
        for j,i in enumerate(self.leftBracket):
            if left == self.leftBracket[j] and right == self.rightBracket[j]:
                return True
        return False

    # check on math operations
    def checkOperators(self):
        # pass
        return True

    def checkExpression(self):
        return self.checkBrackets() and self.checkOperators()
