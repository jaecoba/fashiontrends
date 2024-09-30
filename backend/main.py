from flask import Flask, jsonify, request
from pytrends.request import TrendReq
import pandas as pd

app = Flask(__name__)

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

fashion = ['baggy jeans', 'skinny jeans', 'straight jeans', 'high waisted jeans', 'bootcut jeans']

@app.route('/', methods=['GET'])
def get_popular_trends():

    # Build the payload for the trends request
    pytrends.build_payload(fashion, geo='US', timeframe='today 12-m')
    trends_data = pytrends.interest_over_time()

    # If no data is found, return a 404 error
    if trends_data.empty:
        return jsonify({"error": "No data available for the given query"}), 404

    # Drop 'isPartial' column (if necessary)
    trends_data['most_popular'] = trends_data.idxmax(axis=1)

    # Convert data to JSON and return
    trends_json = trends_data.reset_index().to_dict(orient='records')
    return jsonify(trends_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
