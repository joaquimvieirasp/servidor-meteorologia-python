from flask import Flask, jsonify

app = Flask(__name__)

# Dados de exemplo
weather_data = {
    "city": "São Paulo",
    "temperatura": "25.0",
    "humidity": "60.0",
    "pressure": "1013.0",
    "wind_speed": 10.0,
    "wind_direction": "N"
}

@app.route("/")
def get_weather():
    return jsonify(weather_data)

if __name__== "__main__":
    app.run()
