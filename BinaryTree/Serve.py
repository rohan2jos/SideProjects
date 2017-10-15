from flask import Flask
import HeapNode
from BinTree import  *

app = Flask(__name__)

instance.level_wise()

'''
create an instance for the BinTree and then we can use that
when the api calls come in
'''

anotherInstance = BinTree("anotherInstance")

'''
index()
args: Integer data
returns: the string that is generated from the level_wise() with the tree
in level wise order
'''
@app.route('/index/<int:data>')
def index(data):
    print "[Serve.py] we are at ", data
    instance.insert(data)
    return "Data has been inserted!"

@app.route('/index/show')
def show():
    print "[Serve.py] showing the tree"
    tree = instance.level_wise()
    return tree

@app.route('/add/<int:data>', methods = ['PUT'])
def add_data(data):
    print "[Serve.add_data()] user adding data ", data
    instance.insert(data)
    tree = instance.level_wise()
    return tree

@app.route('/index/preorder')
def pre_order():
    print "[Serve.py] calling preorder"
    nodes = instance.traversal("preorder")
    finalStr = ""
    print "[Serve.py] trying to print the nodes array"
    print nodes
    print "[Serve.py] length of nodes " + str(len(nodes))

    for i in nodes:
        finalStr = finalStr + " " + str(i)

    return "preorder traversal is " + finalStr

@app.route('/index/postorder')
def post_order():
    print "[Serve.py] calling postorder"
    nodes = instance.traversal("postorder")
    finalStr = ""
    for i in nodes:
        finalStr = finalStr + " " + i
    return "postorder traversal is " + finalStr

@app.route('/index/inorder')
def in_order():
    print "[Serve.py] calling inorder"
    nodes = instance.traversal("inorder")
    finalStr = ""
    for i in nodes:
        finalStr = finalStr + " " + i
    return "inorder traversal is " + finalStr

'''
collect the methods, and run the server
*** Please run via Terminal and end with ctrl + c, else might keep port open
(running through an IDE - results in this)
Don't do this and you have to do some boring shit where you have to search the
port and kill it.  In case you don't listen/read:
Commands are -

ps -aef | grep 5000
kill <pid>

'''
if __name__ == '__main__':
    app.run()