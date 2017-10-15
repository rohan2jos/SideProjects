from flask import Flask, render_template, request
from flask import send_file
from flask import send_from_directory
from werkzeug import secure_filename
import os


'''
LISTING THE EXPOSED URLS:

/server/upload
    this will upload a file that you choose on the local fs

/server/download
    this will (for now) download a test.txt on the local fs, please ensure that you
    delete this file on every run

/server/list
    a very unformatted and bad looking list of files in the current repo/local fs folder
    of the project
'''


app = Flask(__name__)

@app.route('/')
def index():
    return "[server.py] Please enter the correct url to use the API"

# route to upload a file
# for now, we will pass the name of the file that you want to upload
@app.route('/server/upload')
def upload_file():
    print "[server.py] hit the upload page"
    return send_file('upload.html')

# helper method that contains the code to secure filename and use uploader, and then store the fileS
@app.route('/server/uploader', methods=['POST'])
def uploader():
    print "[server.py] hit the uploader"
    print "[server.py] redirection: entered helper method to upload the file, method=POST"
    filetToUpload=request.files['file']
    filetToUpload.save(secure_filename(filetToUpload.filename))
    return 'success! is in development, please delete the local file, close the browser, close the server!'


@app.route('/server/download')
def file_download():
    print "[server.py] hit the downloader"
    print "[server.py] downloading file..."
    try:
        return send_file('/home/rohan/Documents/ProjectApps/test.txt', attachment_filename='test.txt', as_attachment=True)
    except Exception as e:
        return str(e)

@app.route('/server/list')
def ls_files():
    print "[server.py] listing the files in the current dir: this is specific to the computer for now, in development"
    listOfFiles = os.listdir('.')

    strList = ""
    for i in listOfFiles:
        strList = strList + "\n" + i
    return strList
# collect the methods and run the server
# debugger is turned on, turn off if there are a lot of debug lines
if __name__ == '__main__':
    app.run(debug=True)
