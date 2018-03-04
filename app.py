#!/usr/bin/env python
import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)


    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "getMEK":
        return {}
    result = req.get("result")

    query = result.get("resolvedQuery")
    if 'email' in query.lower():
        zone = "ehsanul.karim@northsouth.edu"
    elif 'office' in query.lower():
        zone = "Office: SAC 946"
    elif 'phone' in query.lower():
        zone = "880255668200 7"
    else:
        zone = "Mohammad Ehsanul Karim\nLecturer\nOffice: SAC 946\nPhone: +88 02 55668200\nEmail: ehsanul.karim@northsouth.edu"       



    speech=zone

    return {
        "speech": speech,
        "displayText": speech,

        "source": "Mohammad Ehsanul Karim"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
