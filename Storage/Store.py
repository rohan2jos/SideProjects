import time
from FileObject import *
import pickle
import os
import shutil
import time

class Store():

    # contains the objects of all the files in the Store :: for debugging, to remove
    storageList = []

    # contains the names of all the files in the Store :: used for quick search
    storageNameList = []

    # contains the names of the buckets in the store
    MainBucketList = []

    # holds the pointer to the current bucket for allowing storage
    currentBucket = ""

    # dictionary that contains key: value pairs, where key is bucket name and the value is a list of the names
    # of the objects
    mainContentsDirectory = {}

    def __init__(self):
        print "[Store.__init__()] creating object for Store"
        print "[Store.__init__()] initializing directory for buckets on system"
        os.mkdir('/home/rohan/Documents/buckets/')

    def insertIntoStoreList(self, bucketname, fileObj):
        print "[Store.insertIntoStoreList()] received tempfile :: " + fileObj.filename + " with bucketname:: " + bucketname

        checkBucketList = self.checkMainBucketList(bucketname)

        if checkBucketList is "error":
            return "there is already a bucket with the name requested, resulting in a duplicate attempt.  Aborting creation of the bucket"

        self.MainBucketList.append(bucketname)

        print "[Store.insertIntoStoreList()] inserting the object into a storage list"
        self.storageList.append(fileObj)
        self.storageNameList.append(fileObj.filename)
        print "[Store.insertIntoStoreList()] printing the current list"
        print self.storageNameList
        self.serializeAndStore(bucketname, fileObj)
        return "success"

    def serializeAndStore(self, bucketname, fileObj):
        print "[Store.serializeAndStore()] serializing and storing the object in the bucket"
        tempList = []


        # creation of bucket, and serializing

        bucketPath = '/home/rohan/Documents/buckets/' + bucketname
        #os.mkdir(bucketPath)
        self.createEmptyBucket(bucketname)


        tempFileName = fileObj.filename
        print "creating serialized file with name " + tempFileName
        tempFileNameWithPath = bucketPath + "/" + tempFileName
        fl = open(tempFileNameWithPath, 'w')
        pickle.dump(fileObj, fl)
        fl.close()


        # important: this code is only for new buckets
        # TODO: to modify this code to see if the bucket exists, and if it does, pick out the list
        tempList.append(fileObj)
        self.mainContentsDirectory[bucketname] = tempList

        f2 = open(tempFileNameWithPath, 'r')
        tempObj = pickle.load(f2)
        f2.close()

        # checks to see if the object has been serialized and de-serialized
        print "unserialized object filename:::: " + tempObj.filename
        print "unserialized object timestamp:::: " + tempObj.timestamp


    def createEmptyBucket(self, bname):

        attemptToCreateBucket = self.checkMainBucketList(bname)
        if attemptToCreateBucket is "error":
            print "problem in creating the bucket"
            return "error"
        else:
            print "[Store.createEmptyBucket] trying to create an empty bucket with bucket name as " + bname
            bucketPath = '/home/rohan/Documents/buckets/' + bname
            os.mkdir(bucketPath)
            return "success"


    def checkMainBucketList(self, bucketname):
        for i in self.MainBucketList:
            if bucketname is i:
                print "the name is duplicate!"
                return "error"
        print "[Storage.checkMainBucketList()] the main bucket list does not contain bucket name, proceed..."
        return "clean"

    def getMainBucketList(self):
        return self.MainBucketList

    def getMainContentsDirectory(self):
        return self.mainContentsDirectory

    def retrieveFileObject(self, filename):
        print "[Store.retrieveFileObject] searching for file object with filename as " + filename

        # inefficient search
        for i in self.storageList:
            # need a better way to retrieve, for now this is a working placeholder
            if filename is i.filename:
                return i

        print "[Store.retrieveFileObject()] cannot find the filename with the requested object, please raise error"

    def destroyStore(self):
        print "HOPE YOU KNOW WHAT YOU ARE DOING"
        print "cleaning the data structures in the store"
        time.sleep(1)
        print "...cleaning MainBucketList..."
        self.MainBucketList = []
        time.sleep(1)
        print "...cleaning mainContentsDirectory..."
        self.mainContentsDirectory = {}
        time.sleep(1)
        print "...cleaning storageList..."
        self.storageList = []
        time.sleep(1)
        print "...cleaning storageNameList..."
        self.storageNameList = []
        time.sleep(1)

        print "cleaning up the directory on the system"
        shutil.rmtree('/home/rohan/Documents/buckets/')


