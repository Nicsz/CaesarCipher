from flask import Flask, request
from Caesar import rotate

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Шифр Цезаря</title>
        
        <style>
        
            body {{
                background-color: #fff;
            }}

            .wrapper {{
                top: 40%;
                left: 50%;
                width: 600px;
                height: 600px;
                margin: 0 auto;
                position: fixed;
                transform: translate(-50%, -50%)
            }}

            .inner-wrapper {{
                width: 475px;
                margin: 0 auto;
                padding-top: 50px;
            }}

            form {{
                width: 100%;
                display: block;
                margin: 0 auto;
                font-size: 16px;
                border-radius: 10px;
                font-family: 'Roboto', sans-serif;
            }}

            textarea {{
                width: 100%;
                height: 150px;
                margin: 8px 0;
                font-size: 14px;
                border-radius: 4px;
                padding: 12px 20px;
                border: 1px solid #ccc;
                box-sizing: border-box;
            }}

            h1 {{
                color: #2A3132;
                font-weight: 100;
                text-align: center;
                font-family: 'Roboto', sans-serif;
            }}

            p {{
                color: #000;
                display: block;
                margin: 0 auto;
                font-size: 16px;
                text-align: left;
                font-weight: 200;
                padding-bottom: 20px;
                font-family: 'Roboto', 'Helvetica', sans-serif;
            }}

            hr {{
                border: 0;
                padding: 0 0 15px 0;
                width: 100%;
                height: 1px;
                opacity: 0.5;
                display: block;
                margin: 0 auto;
                border-top: 1px solid #aeaeae;
            }}

            label {{
                color: #aeaeae;
                margin-top: 20px;
                font-size: 14px;
                font-weight: 300;
                float: left;
            }}

            input[type=text], select {{
                width: 60%;
                margin: 8px 0;
                padding: 12px 20px;
                border-radius: 4px;
                display: inline-block;
                border: 1px solid #ccc;
                box-sizing: border-box;
                float: right;
            }}

            input[type=submit] {{
                width: 45%;
                color: white;
                border: none;
                margin: 8px 0;
                cursor: pointer;
                padding: 14px 20px;
                border-radius: 4px;
                background-color: #000 ;//#2A3132
            }}
            
            input[value=Зашифровать] {{
                float: right;
            }}
            
            input[type=submit]:hover {{
                background-color: #aeaeae;
                transition: 0.25s;
            }}

        </style>
    </head>
    <body>
        <div class="wrapper">
            <div class="inner-wrapper">
                <h1>Шифр Цезаря</h1>
                <p>Приложение Шифр Цезаря! Введите Ваше сообщение и ключ для поворота, чтобы зашифровать!</p>

                <hr>

                <form class="cipher-form" action ="/" method="POST">
                    <textarea name="input" placeholder="Введите Ваше сообщение:"></textarea>
                    <label for "rot">Введите ключ для поворота:</label>
                    <input type="text" id="rot" name="rot" value="0" onclick="this.value=''">
                    <input type="submit" name="e" value="Расшифровать">
                    <input type="submit" name="d" value="Зашифровать">
                    <textarea name="output" onclick="this.value=''" placeholder="Результат:">{0}</textarea>
                </form>
            </div>
        </div>
    </body>
</html>"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['input'])
    enc_dec_text = rotate(text, rot)
    return form.format(enc_dec_text)
app.run()
