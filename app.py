from flask import Flask, request
import math

app = Flask(__name__)

def gcd(a, b):
    """Calculate Greatest Common Divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def lcm(x, y):
    """Calculate Lowest Common Multiple using GCD"""
    return abs(x * y) // gcd(x, y)

def is_natural_number(value):
    """Check if value is a natural number (positive integer > 0)"""
    try:
        num = int(value)
        return num > 0 and str(num) == str(value).strip()
    except (ValueError, TypeError):
        return False

@app.route('/official_siddik_gmail_com')
def calculate_lcm():
    """Calculate LCM of two natural numbers x and y"""
    x_param = request.args.get('x')
    y_param = request.args.get('y')
    
    # Check if both parameters are provided and are natural numbers
    if (x_param is None or y_param is None or 
        not is_natural_number(x_param) or not is_natural_number(y_param)):
        return "NaN"
    
    x = int(x_param)
    y = int(y_param)
    
    # Calculate and return LCM
    result = lcm(x, y)
    return str(result)

@app.route('/')
def home():
    """Basic health check endpoint"""
    return "LCM Calculator API is running. Use /official_siddik_gmail_com?x={}&y={}"

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)