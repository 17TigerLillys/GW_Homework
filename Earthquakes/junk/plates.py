from flask import Flask, render_template, jsonify, redirect #flash, request

import os


app = Flask(__name__)


#created a mongo database on mlab called mars. Use this for the Heroku app
#dice, angel list, the cia


@app.route("/")
def index():
    print("getting dashboard homepage")

    return render_template("index.html")
       #, data=data)


@app.route("/plates")
def plates():
	plates = pd.read_csv("plates.csv", encoding = "utf-8")
	plate_names_not_clean = plates["PlateBoundIdentifer"].unique()
	plate_names = list(plate_names_not_clean)
	plates_lat_longs = plates[["PlateBoundIdentifer", "StartLat", "StartLong"]]

	plate_dict = {}
	for plate in plate_names:
	    lat_long_list = []
	    for index, row in plates_lat_longs.iterrows():
	        plate_name = row["PlateBoundIdentifer"]
	        if plate_name == plate:
	            lat_long_list.append([row["StartLat"], row["StartLong"]])
	    plate_dict[plate] = lat_long_list
	return jsonify(plate_dict)



if __name__ == "__main__":
    app.run(debug=True)




