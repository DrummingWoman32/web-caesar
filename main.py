
from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <!-- create your form here-->

        <form action="/" method="post">
            <label for="to_encrypt">Rotate by: </label>
            <input type="text" name="rot" value="0" id="to_encrypt">
            <br>
            <br>
            <textarea name="text">{0}</textarea> 
            <br>
            <input type="submit" value="Submit Query">
            <br>
            <br>
        </form>
 
    </body>
</html>

"""

#action="/hello" method="post">

#{0} above is placeholder for encrypted text
#so here I encrypt the text and return it
@app.route("/", methods=['POST'])
def encrypt():

    rot = int(request.form['rot'])
    #rot must be typecast into integer it actually is
    text = request.form['text']
    encrypted_text = rotate_string(text, rot)
    return form.format(encrypted_text)
    

@app.route("/")
def index():

    return form.format("")

app.run()

