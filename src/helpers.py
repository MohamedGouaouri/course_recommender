
import json


def model_df_to_json(recommendation_df):
    return json.loads(
        recommendation_df.to_json(orient='records')
    )
