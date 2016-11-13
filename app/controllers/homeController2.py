#Home Page Controleler

from app.models import *
from app.allImports import *

from app.logic.sentiment import callChain
from app.parse_sections import get_sections

from flask import render_template

@app.route('/home/', methods=["GET"])
def home():
    master = Bill.select().join(Salient, on=(Bill.ID == Salient.ID_id))
    ##Kye left off here after making the join statement 
    for i in master:
        print i  
    bills = Bill.select().where(Bill.is_alive == "True")
    return render_template('homeView.html', numbills = len(bills), master = master)

@app.route('/list/', methods=["GET"])
def list_bills():
    bills = Bill.select().where(Bill.is_alive == "True")
    return render_template('list.html', bills=bills)

@app.route('/view/<bid>/', methods=["GET"])
def view_bill(bid):

    bills = Bill.select().where(Bill.is_alive == "True").where(Bill.bID == bid).get()
    salient = Salient.select().where(Salient.ID_id == bills.ID)
    sections = get_sections(bill.link_web + "/text")
    count = salient.group_by(Salient.section).count()
    colors = dict();

    for section in range(count):
        summaries = salient.select(Salient.name).where((Salient.section == section) & (Salient.summary == True))
        sections_s = salient.select().where((Salient.section == section) & (Salient.summary == False))
        names = list()

        for section in summaries:
            if section.name not in names:
                section.name.append(section.name)

        for section in sections_s:
            if section.name in names:
                colors[section] = "alert alert-success"
                break
        else:
            colors[section] = "alert alert-warning"

    return render_template('display.html', sections = sections, colors = colors)
