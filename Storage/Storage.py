import time
import os
from FileObject import *
from Store import Store
import sys
'''

starting with object storage on a basic level

'''

class Storage():

    storage = {}
    bucketList = []

    def __init__(self):
        print "entered the class Storage, and initializing the values"
        print "[Storage.__init__()] initializing self.storage dictionary to blank dictionary"
        self.storage = {}
        self.currentBucket = ""
        print "[Storage.__init__()] printing blank dictionary to check if it has been initialized"
        self.storeObj = Store()
        print self.storage

    def createBucket(self, bucketName):
        print "[Storage.createBucket()] received bucket name and file name"
        createAttempt = self.createBucketHelper(bucketName)
        if createAttempt is "success":
            print "the bucket was created!"
            self.currentBucket = bucketName
        else:
            print "there was a problem in creating the bucket"

    def creator(self, afile, filePath):
        print "[Storage.creator()] calling the createObject() and createFileObject()"
        self.createObject(afile)
        self.createFileObject(afile, filePath)

    def setCurrentBucket(self, bname):
        self.currentBucket = bname

    def createObject(self, afile):

        print "[Storage.CreateObject()] populating the storage dictionary with the file that has been sent"

        '''
        the dictionary will contain the file as the value pointed to it by the timestamp that it came at
        this will help us to know if the file is the latest copy when retrieving

        The object for file will then be created into our own object for file, where we will enter the metadata
        This will be retrieved with the entry for the file in the storage array
        '''

        dt = time.strftime("%Y-%m-%d %H:%M")

        # adding into the list so that the access can search this.  This will later be put into a database
        self.storage[dt] = afile

    def createFileObject(self, afile, filePath):
        print "[Storage.createFileObject()] serializing the file object before it can be stored"

        '''
        The serialized object will then get stored in the backend
        The backend for now is a block storage based directory

        We will give the parameters required by the constructor of the fileobject class and create an object
        this will help the constructor of the fileobject class to enter the metadata
        '''

        # using a placeholder file till figuring out how to pass the file path and the file to this function
        fullname = os.path.basename(filePath)
        firstname = os.path.splitext(fullname)[0]
        dtToSend = time.strftime("%Y-%m-%d %H:%M")
        tempFile = FileObject(afile, firstname, dtToSend)
        print "[Storage.createFileObject()] printing a class variable from returned file object :: " + tempFile.filename
        print "[Storage.createFileObject()] trying to serialize and store the object into bucket: " + self.currentBucket
        insertionattempt = self.storeObj.insertIntoStoreList(self.currentBucket, tempFile)

        if insertionattempt is "success":
            print "[!Storage.createFileObject.insertionattempt!] the object has been stored!"
        else:
            print "[!Storage.createFileObject.insertionattempt!] there was an error, please check logs!"
            print "[!Storage.createFileObject.insertionattempt!] printing return message:: " + insertionattempt

        print "[Storage.createFileObject()] the object has been initialized.  Please check debug comments starting with FileObject"

    # TODO: awful name, change!
    def createBucketHelper(self, bucketName):
        print self.bucketList
        print "[Storage.createBucketHelper()] received request for bucket with bucket name " + bucketName

        '''
        create a bucket with the bucket name that was passed as a parameter
        The bucket name needs to be unique, and hence we have to check if the bucket already exists.
        This is checked in the bucketList and if the name already exists, we will return an error
        If the name does not exist, then the bucket will be created with the name as specified, at the path as specified
        '''

        '''
        for i in self.bucketList:
            if bucketName is i:
                print "[Storage.createBucketHelper()] ERROR: The bucket with the specified name already exists\n"
                print "The bucket names have to be unique."
                return "duplicate"
        '''

        bucketCreatorForStore = self.storeObj.createEmptyBucket(bucketName)
        if bucketCreatorForStore is "error":
            print "there was a problem in creating the bucket, please check the logs for Store"
        else:
            print "[Storage.createBucketHelper()] the name is not duplicate, inseriting name into bucketList[]"
            self.bucketList.append(bucketName)
            return "success"

    def listBuckets(self):

        """
        only lists the buckets in the current bucket list.
         This is just for the reference
         please query the backend list for the list of buckets that are actually created in the backend
        """

        print "[Storage.listBuckets()] listing the buckets"
        return self.bucketList

    def getMainContentsDirFromStore(self):
        mainContentsDir = self.storeObj.getMainContentsDirectory()
        return mainContentsDir

    def printOnlyBuckets(self):
        print "----------------------list of buckets-------------------"
        for i in self.bucketList:
            print "bucket name                |       " + i
        print "--------------------------------------------------------"

    def printMainContentsDirFromStore(self):
        mainContentsDir = self.storeObj.getMainContentsDirectory()

        for j in mainContentsDir.keys():
            print "bucket name:: " + j
            print "contents:: "
            tempArrayOfContents = mainContentsDir[j]
            for k in tempArrayOfContents:
                print k.filename

    def checkIfBucketExists(self, bname):
        print self.bucketList
        for i in self.bucketList:
            print "if " + bname + " is " + i
            if bname == i:
                print "returning true!"
                return True
        return False

    def startBackup(self):
        print "backup prior to cleaning"

    def cleanup(self):
        print "THIS IS THE CLEANUP FUNCTION!!! IT WILL DESTROY EVERYTHING AT THE BACKEND"
        userPass = raw_input("please enter the password for the server so that this function can proceed:: ")
        if userPass == "hastalavista":
            self.storeObj.destroyStore()
        else:
            print "wrong password, sober up and try again!"


def mainLoop():
    s = Storage()

    exit_flag = False

    while exit_flag is False:

        print "1. display list of buckets"
        print "2. display buckets and their contents"
        print "3. create a bucket"
        print "4. create a bucket and store a file"
        print "5. store a file in an existing bucket"
        print "6. exit"
        print "7. cleanup (requires password)"
        userIn = input("please enter an option :: ")

        if userIn == 1:
            print "displaying the list of buckets"
            s.printOnlyBuckets()

        if userIn == 2:
            print "displaying buckets and their contents"
            s.printMainContentsDirFromStore()

        if userIn == 3:
            print "creating a bucket"
            bname = raw_input("enter the bucket name")
            s.createBucket(bname)

        if userIn == 4:
            print "creating a bucket and storing a file"
            print "creating a bucket"
            bname = raw_input("enter the bucket name")
            s.createBucket(bname)

            # 2. create the object storage
            # TODO: to ensure that the bucket is created before even trying to create a storage for the object
            filePath = '/home/rohan/Documents/PythonLearning/Storage/test.txt'
            f = open(filePath)
            s.creator(f, filePath)

        if userIn == 5:
            print "storing a file in an existing bucket"
            s.printOnlyBuckets()
            userBucketInput = raw_input("please enter the bucket in which you want to store the file:: ")
            doesExist = s.checkIfBucketExists(userBucketInput)
            if doesExist is True:
                userFileIn = raw_input("please enter the path of the file with the name of the file:: ")
                f = open(userFileIn)
                s.setCurrentBucket(userBucketInput)
                s.creator(f, userFileIn)
            else:
                print doesExist
                print "the bucket that you entered does not exist, please try again!"

        if userIn == 6:
            print "starting backup before exiting"
            print "exiting..."
            sys.exit()
        if userIn == 7:
            confirmation = raw_input("starting cleanup, better be sober start? [yes/no]: ")
            if confirmation == "yes":
                print "godspeed!"
                s.cleanup()
            else:
                print "come back later!"
                sys.exit()


mainLoop()