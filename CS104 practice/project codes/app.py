from flask import Flask, render_template, request, send_file
from myfunctions import maketable, levelstate, eventcode, eventtime
import os

data=[]

app = Flask(__name__)    
@app.route('/', methods=['GET', 'POST'])
def login():
    global data
    if request.method == 'POST':
        todo = request.form.get('submit')
        if (todo=="Upload"):
            logfile=request.files['inputfile']
            start_time="1970-01-01T00:00:00"
            end_time="2050-12-31T23:59:59"
            if (logfile.filename==""):
                return render_template('index.html', message1="Please upload a file", msgcolor="red")
            logfile.save("uploads/input.log")
            data=maketable("uploads/input.log", start_time, end_time)
            if (data==[]):
                return render_template('index.html', message1="Please upload a valid log file", msgcolor="red")
            elif (len(data)==1):
                return render_template('index.html', message1="File does not contain data", msgcolor="crimson")
            else:
                return render_template('index.html', message1="Uploaded Succesfully!! Select time range on which to analyse below. Go to view pages to see appropriate visualisations.", msgcolor="greenyellow")
        elif (todo=="Select"):
            start_time=request.form.get('starttime')
            end_time=request.form.get('endtime')
            if (not os.path.exists("uploads/input.log")):
                return render_template('index.html', message2="Pls upload file before selecting time range", msgcolor="red")
            data=maketable("uploads/input.log", start_time, end_time)
            return render_template('index.html', message2="Applied selected time range!! Go to view pages to see appropriate visualisations.", msgcolor="greenyellow")
    else:
        return render_template('index.html', message1="Please upload a file")

@app.route('/viewcsv', methods=['GET', 'POST'])
def viewcsv():
    global data
    if (data==[]):
        return render_template('plsupload.html', message="Please upload a file on the upload page to view!")
    else:
        if request.args.get('submit')=="Download":
            return send_file("output.csv", as_attachment=True)
        return render_template('rendertable.html', tabledata=data)
    
@app.route('/viewplot', methods=['GET', 'POST'])
def viweplot():
    global data
    if (data==[]):
        return render_template('plsupload.html', message="Please upload a file on the upload page to view!")
    elif (len(data)==1):
        return render_template('plsupload.html', message="No data in selected time range! Please select a different time range to view plots.")
    else:
        levelstate(data)
        eventcode(data)
        eventtime()
        if request.args.get('submit')=="levelstatepdf":
            return send_file("static/plots/levelstate.pdf", as_attachment=True)
        elif request.args.get('submit')=="levelstatepng":
            return send_file("static/plots/levelstate.png", as_attachment=True)
        elif request.args.get('submit')=="eventcodepdf":
            return send_file("static/plots/eventcode.pdf", as_attachment=True)
        elif request.args.get('submit')=="eventcodepng":
            return send_file("static/plots/eventcode.png", as_attachment=True)
        elif request.args.get('submit')=="eventtimepdf":
            return send_file("static/plots/eventtime.pdf", as_attachment=True)
        elif request.args.get('submit')=="eventtimepng":
            return send_file('static/plots/eventtime.png', as_attachment=True)
        return render_template('renderplots.html')
                                 
