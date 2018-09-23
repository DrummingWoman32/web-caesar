from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }

            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <!-- create your form here-->

        <!-- POST method to be used -->

        Rotate by: <input type="text" name="rot" value="0">
        <br>
        <br>
        <textarea name="text"></textarea> 
        <br>
        <input type="submit" value="Submit Query">
        <br>
        <br>
 
    </body>
</html>

"""
@app.route("/", methods=['POST'])
def encrypt(rot, text):

    #encrypt_form = request.form['rot']
    form += ("<h1>" + str(rotate_string(text, rot)) + "</h1>")
    return form




@app.route("/")
def index():
    return form

app.run()

