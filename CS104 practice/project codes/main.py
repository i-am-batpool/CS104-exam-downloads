from flask import Flask, render_template, request, send_file
from myfunctions import maketable

data=[]

app = Flask(__name__)    
@app.route('/', methods=['GET', 'POST'])
def login():
    global data
    if request.method == 'POST':
        todo = request.form.get('submit')
        if (todo=="Upload"):
            logfile=request.files['inputfile']
            if (logfile.filename==""):
                return render_template('index.html', message="Please upload a file", color="red")
            logfile.save("uploads/input.log")
            data=maketable("uploads/input.log")
            if (data==[]):
                return render_template('index.html', message="Please upload a valid log file", color="red")
            else:
                return render_template('index.html', message="Uploaded Succesfully!! Go to view pages to see appropriate visualisations.", color="green")
        elif (todo=="View"):
            return render_template('posted.html', tabledata=data)
    else:
        if request.args.get('submit')=="Download":
            return send_file("output.csv", as_attachment=True)
        return render_template('index.html', message="")
