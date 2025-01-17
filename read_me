IoT Sensor Management and Simulation REST API
Description

This project implements a REST API for managing and simulating IoT sensor data. It consists of a server that provides endpoints for accessing and controlling sensor data and a client interface for interacting with the server. The system is designed to simulate three sensors—temperature, humidity, and light intensity—and allows users to retrieve data, adjust measurement periods, and update sensor values dynamically.
Features
Server-Side Features:

    List Sensors:
        Endpoint: /sensors
        Method: GET
        Returns a list of all available sensors.

    Retrieve Sensor Data:
        Endpoint: /data/<sensor_name>
        Method: GET
        Fetches the current data (value and tags) for a specific sensor.

    Update Measurement Period:
        Endpoint: /period/<sensor_name>
        Method: PUT
        Updates the frequency (in seconds) at which a specific sensor reports its data.

    Update Sensor Value and Tags:
        Endpoint: /sensors/<sensor_name>
        Method: PUT
        Updates the value and metadata (tags) of a sensor.

    Simulated Sensor Data:
        Sensors periodically generate random values within a defined range, simulating real-world operation.

Client-Side Features:

    List Sensors: Displays all available sensors.
    Get Sensor Data: Fetches and displays data for a selected sensor.
    Update Measurement Period: Updates the reporting frequency of a specific sensor.

How to Run
Server:

    Install the necessary dependencies:

pip install flask requests

Run the server script:

    python REST_Server_for_IoT_Sensor_Management_and_Simulation.py

    The server will start on http://127.0.0.1:5001.

Client:

    Run the client interface script:

    python IoT_Sensor_Client_Interface.py

    Use the menu-driven interface to interact with the REST API.

API Endpoints
Server
Endpoint	Method	Description
/sensors	GET	List all available sensors.
/data/<sensor_name>	GET	Retrieve data for a specific sensor.
/period/<sensor_name>	PUT	Update the measurement period of a sensor.
/sensors/<sensor_name>	PUT	Update the value and tags of a sensor.
Simulation Details

    Temperature Sensor:
        Range: -10 to 40°C
        Tags: { "greenhouse_id": "λαχανα", "field": "tyrnabos" }
        Default Period: 1 second

    Humidity Sensor:
        Range: 40% to 100%
        Tags: { "greenhouse_id": "μαρουλια", "field": "Agia" }
        Default Period: 2 seconds

    Light Intensity Sensor:
        Range: 500 to 1000 lux
        Tags: { "greenhouse_id": "ντοματες", "field": "belika" }
        Default Period: 3 seconds

Example Usage
Client Interface:

    List all sensors:

Menu:
1. List all sensors
> Enter your choice: 1

Get sensor data:

Menu:
2. Get sensor data
> Enter your choice: 2
> Enter sensor name: temperature

Update measurement period:

    Menu:
    3. Update measurement period
    > Enter your choice: 3
    > Enter sensor name: temperature
    > Enter new measurement period (seconds): 5

Notes

    Ensure both the server and client scripts are run on the same device or modify the base_url in the client script to match the server's IP and port.
