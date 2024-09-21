from flask import Flask, jsonify, request

app=Flask(__name__)

books=[
	{"id":11,"title":"Ravi Raman","author":"Mr. Ravi"},
	{"id":12,"title":"Mera dost","author":"Mr. X"},
	{"id":13,"title":"Life is Zero","author":"Dr. Sangeeta"}
]

@app.route("/books',methods=['Get']")
def get_All():
	return books

@app.route("/books/<int:book_id>",methods=['Get'])
def getBook(book_id):
	for book in books:
		if book['id']==book_id:
			return book
		else:
			print("Enter correct")

if __name__=="__main__":
	app.run(debug=True)