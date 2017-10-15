from flask import Flask, render_template

from SearchAndSort.MainFile import generateReport

print "running test suite, this will generate a new results file"
generateReport()
print "test suite complete!"

# *** VERY IMPORTANT: This will fail, please change path
app = Flask(__name__, template_folder='C:\Users\erohajo\Documents\Github\PythonLearning\PythonLearning')

@app.route("/")
def index():
    print "user has entered the results server"
    return render_template('results.html')

@app.route("/results")
def results():
    print "user has entered the results page"
    return render_template('results.html')

if __name__ == "__main__":
    app.run()