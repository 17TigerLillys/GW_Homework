from flask import Flask, render_template, jsonify, redirect #flash, request

import os

from bb_functions import get_sample_names, get_sample_metadata, get_OTU_desc, get_sample_values

app = Flask(__name__)

sample_names, samples_df = get_sample_names()
#print(sample_names)
otu_data = get_OTU_desc()
meta_data = get_sample_metadata()



#created a mongo database on mlab called mars. Use this for the Heroku app
#dice, angel list, the cia


@app.route("/")
def index():
    print("getting dashboard homepage")

    return render_template("index.html")
       #, data=data)


@app.route("/names")
def names():
    #get list of sample names
    print("getting list of sample names")
    names_data = get_sample_names()
    return (jsonify(sample_names))
    #return redirect("http://localhost:5000/", code=302)


@app.route("/otu")
def otu():
    #get list of OTU descriptions
    print("getting list of OTU descriptions")
    otu_data = get_OTU_desc()
    return (jsonify(otu_data))
    #return redirect("http://localhost:5000/", code=302)

@app.route("/metadata/<sample>")
def metadata(sample):
    #get json dictionary of sample metadata
    print("getting json dict of sample metadata")
    meta_data = get_sample_metadata()
    return (jsonify(meta_data[int(sample)]))
    #return redirect("http://localhost:5000/", code=302)

#def wfreq():
    #get Weekly Washing Frequency as a number.
    print("getting washing frequency")
    wfreq_data = get_washing_freq()
    return (jsonify(wfreq_data))
    #return redirect("http://localhost:5000/", code=302)

@app.route("/samples/<sample>")
def samples(sample):
    #get OTU IDs and Sample Values for a given sample
    print("getting list of sample names")
    sample_data = get_sample_values(sample)
    return jsonify(sample_data)
    #return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
