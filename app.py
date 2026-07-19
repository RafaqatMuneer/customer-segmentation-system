from flask import Flask, request, jsonify
import pandas as pd
import joblib
from sklearn.cluster import KMeans

# ---------------------------------------
# Flask App
# ---------------------------------------

app = Flask(__name__)

# ---------------------------------------
# Load Trained Pipeline
# ---------------------------------------

with open("models/customer_segmentation.joblib", "rb") as f:
    model = joblib.load(f)

# ---------------------------------------
# Cluster Information
# ---------------------------------------

segment_map = {
    0: "Regular Customer",
    1: "Premium Customer",
    2: "Young Enthusiastic Shopper",
    3: "High Income Saver",
    4: "Budget Customer"
}

segment_description = {
    0: "Customers with moderate income and average spending behavior.",
    1: "High-income customers who spend frequently and are ideal for premium offers.",
    2: "Young customers with lower income but high spending habits, making them responsive to promotions and new products.",
    3: "Customers with high income but relatively low spending, representing an opportunity for targeted marketing.",
    4: "Customers with lower income and conservative spending patterns who may respond well to discounts and value-based offers."
}

marketing_action = {
    0: "Recommend standard products and loyalty rewards.",
    1: "Offer premium memberships and exclusive promotions.",
    2: "Target with seasonal offers and trending products.",
    3: "Encourage spending through personalized incentives.",
    4: "Promote discounts and value-for-money bundles."
}

# ---------------------------------------
# Home Route
# ---------------------------------------

@app.route("/")
def home():
    return jsonify({
        "message": "Customer Segmentation API is Running Successfully!"
    })

# ---------------------------------------
# Prediction Route
# ---------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.json

        # Create DataFrame (column names must match training data)
        input_df = pd.DataFrame([{
            "Gender": str(data["Gender"]),
            "Age": int(data["Age"]),
            "Annual Income (k$)": float(data["Annual Income (k$)"]),
            "Spending Score (1-100)": int(data["Spending Score (1-100)"])
        }])

        # Predict Cluster
        cluster = int(model.predict(input_df)[0]) 

        # Return Result
        return jsonify({

            "cluster": cluster + 1, # set index to 1 instead of 0

            "segment": segment_map[cluster],

            "description": segment_description[cluster],

            "marketing_action": marketing_action[cluster]

        })

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 400


# ---------------------------------------
# Run Flask App
# ---------------------------------------

if __name__ == "__main__":
    app.run(debug=True)