from flask import Flask, jsonify, request
from pytrends.request import TrendReq
import pandas as pd

app = Flask(__name__)

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

@app.route('/api/trends', methods=['GET'])
def get_trends():
    # Get keyword, region, and timeframe from request parameters
    keyword = request.args.get('keyword', 'fashion')
    region = request.args.get('region', 'US')
    start_date = request.args.get('start_date', 'today 12-m')
    end_date = request.args.get('end_date', None)

    # Build timeframe
    if end_date:
        timeframe = f'{start_date} {end_date}'
    else:
        timeframe = start_date

    # Build the payload for the trends request
    pytrends.build_payload([keyword], geo=region, timeframe=timeframe)
    trends_data = pytrends.interest_over_time()

    # If no data is found, return a 404 error
    if trends_data.empty:
        return jsonify({"error": "No data available for the given query"}), 404

    # Drop 'isPartial' column (if necessary)
    trends_data = trends_data.drop(columns=['isPartial'], errors='ignore')

    # Convert data to JSON and return
    trends_json = trends_data.reset_index().to_dict(orient='records')
    return jsonify(trends_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
