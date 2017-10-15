import time

class FileObject():

    timestamp = ""
    filename = ""

    def __init__(self, afile, filename, timestamp):
        print "[FileObject.__init__] creating the object for file"
        self.createMetadata(afile, filename, timestamp)

    def createMetadata(self, afile, filename, timestamp):
        print "[FileObject.createMetadata()] entering the metadata for the file object"
        self.timestamp = timestamp
        print "[FileObject.createMetadata()] printing the created metadata"
        print self.timestamp
        self.filename = filename
        print self.filename
        self.returnSelf()

    def returnSelf(self):
        print "[FileObject.returnSelf()] the file object has been created, now returning so it can be stored"
        return self
