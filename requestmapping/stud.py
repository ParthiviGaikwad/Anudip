from flask import Flask, jsonify, request

app=Flask(__name__)

stu=[
	{"id":1,"name":"Parthivi" ,"address":"Kalamboli"},
	{"id":2, "name":"Aleena","address":"Kamothe"},
	{"id":3,"name":"Meenakshi","address":"Panve;"}
]

@app.route("/student",methods=['GET'])
def get_All():
	return stu

@app.route("/id/<int:stu_id>",methods=['GET'])
def getStud(stu_id):
	for x in stu:
		if x["id"]==stu_id:
			return x
	print("Enter correct")

if __name__ == "__main__" :
	app.run(debug=True)