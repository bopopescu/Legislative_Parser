from app.logic.sentiment import callChain
from app.logic.bill_scrapping import *
from app.logic.parse_sections import *
from app.models import *
import time
"""
for bill in Bill.select():
    summary = get_summaries(bill.link_web + "/summary")
    if summary == "N/A":
        pass
    else:
        for key in summary:
            time.sleep(.05)
            temp = callChain(summary[key])
            for ndx in range(len(temp['entities'])):
                for lst_key in temp['entities'][ndx]:
                    if lst_key == "salience":
                        score = float(temp['entities'][ndx][lst_key]) 
                    elif lst_key == "type":
                        tyype = str(temp['entities'][ndx][lst_key]) 
                    elif lst_key == "name":
                        name = str(temp['entities'][ndx][lst_key])
                Salient(ID = bill.ID,
                        summary = True,
                        name = name,
                        score = score,
                        obj_type = tyype,
                        section = key 
                        ).save()
"""
for bill in Bill.select():    
    try:
        summary = get_sections(bill.link_web + "/text")
        for key in summary:
            temp = callChain(summary[key])
            time.sleep(.05)
            for ndx in range(len(temp['entities'])):
                for lst_key in temp['entities'][ndx]:
                    if lst_key == "salience":
                        score = float(temp['entities'][ndx][lst_key]) 
                    elif lst_key == "type":
                        tyype = str(temp['entities'][ndx][lst_key]) 
                    elif lst_key == "name":
                        name = str(temp['entities'][ndx][lst_key])
                Salient(ID = bill.ID,
                        summary = False,
                        name = name,
                        score = score,
                        obj_type = tyype,
                        section = key 
                        ).save()      
    except:
        pass   
