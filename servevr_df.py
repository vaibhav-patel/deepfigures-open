import json
from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import request
import requests
app = Flask(__name__)
CORS(app)
from flask import request
import time
# test()

@app.route('/test')
def test():
    s1 = time.time()
    print('---full--time--', time.time() - s1)
    # with open('/Users/vaibhav/Rax/rax-gist-backend/api/summarizer/debugJSONObjects/test_results/tiny_overview/The Value of Zoo Experiences for Connecting People with Nature_TINY_OVERVIEW_SUMMARY.json', 'r') as f:
    # with open('/Users/vaibhav/Rax/rax-gist-backend/api/summarizer/debugJSONObjects/test_results/small_overview/NA_SMALL_OVERVIEW_SUMMARY.json', 'r') as f:
    # with open('/Users/vaibhav/Rax/rax-gist-backend/api/summarizer/debugJSONObjects/test_results/medium_overview/NA_MEDIUM_OVERVIEW_SUMMARY.json', 'r') as f:
    # with open('/Users/vaibhav/Rax/rax-gist-backend/api/summarizer/debugJSONObjects/test_results/key_insights/Why Zoos & Aquariums Matter: Assessing the Impact of a Visit to a Zoo or Aquarium_key_insights.json', 'r') as f:
    #     x = json.loads(f.read())
    return 'testdf'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3268)



