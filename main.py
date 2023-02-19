from flask import Flask, render_template, jsonify

app = Flask(__name__)

GALLERY = [
  {
    'id': 1,
    'title' : '1 designs',
    'imgurl' : '#'
  },
  {
    'id': 2,
    'title' : '2 designs',
    'imgurl' : '#'
  },
  {
    'id': 3,
    'title' : '3 designs',
    'imgurl' : '#'
  },
  {
    'id': 4,
    'title' : '4 designs',
    'imgurl' : '#'
  },
  {
    'id': 5,
    'title' : '5 designs',
    'imgurl' : '#'
  },
  
]




@app.route("/")
def hello_world():
  return render_template('home.html')


@app.route("/api/gallery")
def listgallery():
  return jsonify(GALLERY)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)