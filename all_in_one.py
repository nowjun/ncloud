from flask import Flask, request

import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    gcd = None
    lcm = None
    
    if request.method == "POST":
        try:
            num1 = int(request.form.get("a"))
            num2 = int(request.form.get("b"))
            
            gcd = math.gcd(num1, num2)
            lcm = abs(num1 * num2) // gcd
        except ValueError:
            return "숫자를 입력하세요."
    
    html = '''
    <html>
    <head>
        <title>GCD and LCM Calculator</title>
    </head>
    <body>
        <h1>GCD and LCM Calculator</h1>
        <form method="post">
            <label for="a">Enter the first number (a):</label>
            <input type="number" id="a" name="a" required><br>
            <label for="b">Enter the second number (b):</label>
            <input type="number" id="b" name="b" required><br>
            <input type="submit" value="Calculate">
        </form>
        '''
    
    if gcd is not None and lcm is not None:
        html += f"<p>최대 공약수: {gcd}, 최소 공배수: {lcm}</p>"
    
    html += '''
    </body>
    </html>
    '''
    
    return html

if __name__ == "__main__":
    app.run(debug=True)