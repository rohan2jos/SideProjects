import sys

def GetError(value, name):
    print "entered the function"
    MainAns = 0
    try:
        if value == 0:
            print "value is 0, cannot be divided and hence raising exception"
            raise ArithmeticError()
        ans = 100/value
        MainAns = ans
        print name[10]
    except ArithmeticError as msg:
        print "exception has been caught when trying to divide by ", value
        print msg
    except IndexError as msg:
        print "exception has been caught when trying to index"
        print msg
    finally:
        print "code coming here nevertheless!"
        print MainAns



GetError(100, "rohan")
GetError(0, "rohan")