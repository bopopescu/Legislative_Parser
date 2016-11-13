#Home Page Controleler

from app.models import *
from app.allImports import *

from app.logic.sentiment import callChain
from app.logic.parse_sections import get_sections
from app.logic.bill_scrapping import get_summaries
from app.logic.summarize import summarize
from app.logic.prognosis import get_prognosis



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
    bill = Bill.select().where(Bill.is_alive == "True").where(Bill.bID == bid).get()
    sections = get_sections(bill.link_web + '/text')
    summaries = get_summaries(bill.link_web + '/summary')
    salient = Salient.select().where(Salient.ID_id == bill.ID)
    count = salient.group_by(Salient.section).count()

    colors = dict();

    for section_count in range(count):
        summaries_s = salient.select(Salient.name).where((Salient.section == section_count) & (Salient.summary == True))
        sections_s = salient.select().where((Salient.section == section_count) & (Salient.summary == False))
        names = list()

        for section in summaries_s:
            if section.name not in names:
                names.append(section.name)

        color_set = False
        for section in sections_s:
            if section.name in names:
                colors[section_count] = "alert alert-success"
                color_set = True

        if not color_set:
            colors[section_count] = "alert alert-warning"
    for section_count in range(section_count):
        if section_count not in colors:
            colors = "alert alert-info"
    return render_template(
        'display.html',
        bill=bill,
        sections=sections,
        summaries=summaries,
        colors=colors,
        prognosis=get_prognosis(bill.link_web)
    )
