from flask import Flask, render_template 
app = Flask(__name__)  

@app.route('/')
def render_main():
    return render_template('index2.html')

@app.route('/<x>')
def render(x):
    return render_template('index.html', num_from_host=int(x))










if __name__=="__main__":   
    app.run(debug=True)  