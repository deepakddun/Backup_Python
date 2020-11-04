from flask import Flask, render_template
import os
app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/create")
def create():
    file_name = '/data/sample_file.txt'
    with open(file_name, 'w') as file_write:
        for i in range(1, 11):
            file_write.write(f'{i} \n')

    return "Created a file"


@app.route("/read")
def read():
    #file_name = '/data/sample_file.txt'
    lines = None
    with os.scandir('/data/') as entries:
        for entry in entries:
            with open(entry) as file_read:
                lines = file_read.readlines()
    return render_template("index.html", lines=lines)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port="8000")
    #app.run(debug=True)
