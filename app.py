from flask import Flask, render_template, jsonify
import yaml

app = Flask(__name__)

info = yaml.load(open('info.yml', 'r'))


@app.route('/info')
def hello_world():
    return jsonify(info)


@app.route('/')
def index():
    #return render_template('index.html')
    return render_template("index.html", info=info['info'])
    

@app.route('/about', methods=['GET', 'POST'])
def about():
    
    return redirect("http://localhost:5000/#about")
    #return render_template("about.html", info=info['info'])


@app.route('/academic', methods=['GET', 'POST'])
def aca():

    return redirect("http://localhost:5000/#academic")


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
