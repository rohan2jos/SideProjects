class ContextManagerDemo:
    def __init__(self):
        print "inside the init"

    def __enter__(self):
        print "inside the enter for the context manager"
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print "exiting"


with ContextManagerDemo() as cmObj:
    print cmObj