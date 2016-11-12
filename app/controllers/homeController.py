#Home Page Controleler

from app.models import Bill
from app.allImports import *

from flask import render_template

@app.route('/home/', methods=["GET"])
def home(): 
    return render_template('homeView.html')
