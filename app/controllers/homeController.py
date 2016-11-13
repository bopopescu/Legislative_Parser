#Home Page Controleler

from app.models import *
from app.allImports import *

from app.logic.sentiment import callChain
from app.logic.parse_sections import get_sections
from app.logic.bill_scrapping import get_summaries
from app.logic.summarize import summarize


from flask import render_template

@app.route('/', methods=["GET"])
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
    bill = Bill.select().where(Bill.id == bid).get()
    sections = get_sections(bill.link_web + '/text')
    summaries = get_summaries(bill.link_web + '/summary')
    print bill.link_web
    return render_template('display.html', bill=bill, sections=sections, summaries=summaries)
