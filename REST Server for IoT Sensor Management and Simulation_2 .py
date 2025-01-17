from flask import Flask, jsonify, request
import threading
import random
import time
import requests

# Flask app setup
app = Flask(__name__)

# Default sensor data and measurement periods
sensor_data = {
    "temperature": {"value": 25.0, "tags": {"greenhouse_id": "λαχανα", "field": "tyrnabos"}},
    "humidity": {"value": 50.0, "tags": {"greenhouse_id": "μαρουλια", "field": "Agia"}},
    "light_intensity": {"value": 700, "tags": {"greenhouse_id": "ντοματες", "field": "belika"}},
}

measurement_periods = {
    "temperature": 1,
    "humidity": 2,
    "light_intensity": 3,
}

# Thread control
stop_threads = False

# Maximum allowed period before halting updates
MAX_PERIOD = 900  # Adjust as needed (e.g., 1000 seconds)

# Root route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Sensor REST API",
        "endpoints": {
            "/sensors": "List available sensors (GET)",
            "/data/<sensor_name>": "Get specific sensor data (GET)",
            "/period/<sensor_name>": "Update sensor measurement period (PUT)",
            "/sensors/<sensor_name>": "Update sensor value and tags (PUT)"
        }
    })

# List all available sensors
@app.route('/sensors', methods=['GET'])

#------ list method -------------------------------------

def list_sensors():
    return jsonify({"sensors": list(sensor_data.keys())})

# Get data from a specific sensor
@app.route('/data/<sensor_name>', methods=['GET'])

#---------Data Method  --------------------------
def get_data(sensor_name):
    if sensor_name in sensor_data:
        return jsonify({
            "sensor": sensor_name,
            "value": sensor_data[sensor_name]["value"],
            "tags": sensor_data[sensor_name]["tags"]
        })
    else:
        return jsonify({"error": "Sensor not found"}), 404

# Update the measurement period for a specific sensor
@app.route('/period/<sensor_name>', methods=['PUT'])


#---------Period Method  ----------------------


def update_period(sensor_name):
    if sensor_name in measurement_periods:
        try:
            new_period = request.json.get("period")
            if new_period and new_period > 0:
                measurement_periods[sensor_name] = new_period
                return jsonify({"message": f"Updated {sensor_name} period to {new_period} seconds"})
            else:
                return jsonify({"error": "Invalid period"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"error": "Sensor not found"}), 404

# Update sensor value and tags
@app.route('/sensors/<sensor_name>', methods=['PUT'])
def update_sensor(sensor_name):
    if sensor_name in sensor_data:
        try:
            value = request.json.get("value")
            tags = request.json.get("tags", {})
            if value is not None:
                sensor_data[sensor_name]["value"] = value
                if tags:
                    sensor_data[sensor_name]["tags"] = tags
                return jsonify({
                    "message": f"Updated {sensor_name}",
                    "value": value,
                    "tags": sensor_data[sensor_name]["tags"]
                })
            else:
                return jsonify({"error": "No value provided"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"error": "Sensor not found"}), 404

# Sensor simulation and communication with server
def send_to_server(sensor_name, value, tags):
    try:
        payload = {"value": value, "tags": tags}
        response = requests.put(f"http://127.0.0.1:5001/sensors/{sensor_name}", json=payload)
        if response.status_code == 200:
            print(f"Server Updated: {sensor_name} - {value:.2f}, Tags: {tags}")
        else:
            print(f"Error updating {sensor_name}: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")

def simulate_sensor(sensor_name, min_val, max_val, is_int=False, tags={}):
    while not stop_threads:
        # Dynamically fetch the current period
        current_period = measurement_periods[sensor_name]

        # Halt updates if the period exceeds the maximum allowed
        if current_period > MAX_PERIOD:
            print(f"Sensor {sensor_name} updates halted due to long period: {current_period} seconds")
            time.sleep(1)  # Sleep briefly before rechecking the period
            continue

        # Generate a random value for the sensor
        value = random.randint(min_val, max_val) if is_int else random.uniform(min_val, max_val)

        # Send the simulated value to the server
        send_to_server(sensor_name, value, tags)

        # Sleep for the updated period
        time.sleep(current_period)

# Start the server and simulation threads
if __name__ == '__main__':
    # Simulation threads
    simulation_threads = [
        threading.Thread(target=simulate_sensor, args=("temperature", -10, 40, False, {"greenhouse_id": "λαχανα", "field": "tyrnabos"})),
        threading.Thread(target=simulate_sensor, args=("humidity", 40, 100, False, {"greenhouse_id": "μαρουλια", "field": "Agia"})),
        threading.Thread(target=simulate_sensor, args=("light_intensity", 500, 1000, True, {"greenhouse_id": "ντοματες", "field": "belika"})),
    ]

    # Start simulation threads
    for thread in simulation_threads:
        thread.start()

    # Run Flask server
    try:
        app.run(host='127.0.0.1', port=5001)
    finally:
        # Stop simulation threads
        stop_threads = True
        for thread in simulation_threads:
            thread.join()

