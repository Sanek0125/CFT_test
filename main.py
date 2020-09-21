import os, view
from app import app

if __name__ == '__main__':
    
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.run(debug=False, host="0.0.0.0")

