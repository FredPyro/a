from flask import Flask, request

app = Flask(__name__) #start aplikasi selalu flask

@app.route('/')
def form(): #tampilan utama website
    return '''
        <html>
        <head>
            <title>Express Yourself!</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    padding: 50px;
                    text-align: center;
                }
                h2 {
                    color: #333;
                }
                form {
                    background-color: cyan;
                    padding: 20px;
                    border-radius: 10px;
                    display: inline-block;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
                    text-align: left;
                }
                input[type=text], input[type=number] {
                    width: 100%;
                    padding: 8px;
                    margin: 8px 0;
                    box-sizing: border-box;
                }
                input[type=submit] {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type=submit]:hover {
                    background-color: #fff;
                }
            </style>
        </head>
        <body>
            <h2>Isi Biodata Kamu</h2>
            <form action="/biodata" method="post">
                Name: <input type="text" name="name"><br>
                Age: <input type="number" name="age"><br>
                Hobby: <input type="text" name="hobby"><br>
                Location: <input type="text" name="location"><br>
                Region: <input type="text" name="region"><br>
                <input type="submit" value="Kirim">
            </form>
        </body>
        </html>
    '''

@app.route('/biodata', methods=['POST'])
def biodata():
    name = request.form['name']
    age = request.form['age']
    hobby = request.form['hobby']
    location = request.form['location']
    region = request.form['region']

    return f'''
        <html>
        <head>
            <title>Hasil Biodata</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    padding: 50px;
                    text-align: center;
                }}
                h2 {{
                    color: #333;
                }}
                .card {{
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    display: inline-block;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
                    text-align: left;
                }}
                a {{
                    display: inline-block;
                    margin-top: 20px;
                    text-decoration: none;
                    color: #4CAF50;
                }}
            </style>
        </head>
        <body>
            <h2>Results</h2>
            <div class="card">
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Age:</strong> {age}</p>
                <p><strong>Hobby:</strong> {hobby}</p>
                <p><strong>Location:</strong> {location}</p>
                <p><strong>Region:</strong> {region}</p>
            </div>
            <br>
            <a href="/">← Repost Another?</a>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
