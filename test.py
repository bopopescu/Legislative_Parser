from app.logic.sentiment import callChain
from app.logic.bill_scrapping import *
from app.logic.parse_sections import *
from app.models import Bill


summary = get_summaries("https://www.govtrack.us/congress/bills/114/s1331/summary")
for key in summary:
    print callChain(summary[key])
