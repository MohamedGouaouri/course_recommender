from model import recommend_course
from helpers import model_df_to_json
from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/recommend")
def recommend():
    title = 'Ultimate Investment Banking Course'
    rec_df = recommend_course(title)
    return jsonify(model_df_to_json(rec_df))


app.run(port=3001)
