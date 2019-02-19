# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import logging
import json
## REFERENCE: https://developers.google.com/api-client-library/python/apis/cloudfunctions/v1
from googleapiclient import discovery
##from google.oauth2 import service_account

from flask import Flask


app = Flask(__name__)

@app.route('/')
def menu():
    """Return a friendly HTTP greeting."""
    msg=hello()
    msg=msg+'Current menu'
    msg=msg+'[0] / (root) Hello+ this menu '
    msg=msg+'[1] /helloHello World '
    msg=msg+'[2] /extfun private : hw external fun'
    msg=msg+'[3] /testsec Hello+ sec end point '
    msg=msg+'[4] /testpatch Hello+ sec end point '    
    return msg,200,{'Content-Type': 'text/plain; charset=utf-8'}

def extfun():
    """Return a friendly HTTP greeting."""
    return 'Hello World external function!'

@app.route('/hello')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World geantino timeout33sec updateMask!'

@app.route('/testsec')
def testsec():
    """Return a friendly HTTP greeting."""
    return extfun()+ '\n'+hello() + '\n\n' + 'Hello World testSEC endpoint!'

@app.route('/testpatch')
def testpatchfun():
    message=hello()+"========================================"
    ##request_json = request.get_json()
    ##info = request_json["credentials"]
    ##credentials = service_account.Credentials.from_service_account_info(info)
    ##function_service = discovery.build('cloudfunctions', 'v1', credentials=credentials)
    function_service = discovery.build('cloudfunctions', 'v1') 
    ##name = request_json["name"]
    ##tags = request_json["tags"]    
    name="projects/drogon-flex/locations/us-central1/functions/funfun-python37-flex"
    get_request = function_service.projects().locations().functions().get(name=name)
    gbody = get_request.execute()
    message=message+"=================GET00======================="
    message=message+json.dumps(gbody,indent=4)
    
    ##for tag in tags:
    ##    body["labels"][tag["key"]] = tag["value"]
    gbody["labels"]["deployment-tool"] = "kraken-mania"
    #gbody["labels"]["Company"] = "GoogLe"
    gbody["timeout"] = "33s"
    request = function_service.projects().locations().functions().patch(name=name, body=gbody, updateMask="labels,timeout")
    pbody=request.execute()
    message=message+"=================PATCH00======================="
    message=message+json.dumps(pbody,indent=4)

    get_request2 = function_service.projects().locations().functions().get(name=name)
    cbody = get_request2.execute()
    message=message+"=================GET01======================="
    message=message+json.dumps(cbody,indent=4)
    
    message=message+"=================END======================="
    return 'Hello World testpatch!'+message


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
