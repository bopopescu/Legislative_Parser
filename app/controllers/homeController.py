#Home Page Controleler

from app.models import Bill
from app.allImports import *

from app.logic.sentiment import callChain

from flask import render_template

@app.route('/home/', methods=["GET"])
def home(): 
    shittyData = callChain()
    return render_template('homeView.html', shittyData = shittyData)
