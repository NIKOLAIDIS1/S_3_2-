import requests
import json

# Server base URL (Update if running on another device)
base_url = "http://127.0.0.1:5001"

def list_sensors():
    """List all available sensors."""
    try:
        response = requests.get(f"{base_url}/sensors")
        if response.status_code == 200:
            sensors = response.json().get("sensors", [])
            print(json.dumps({"sensors": sensors}, indent=4))
        else:
            print(json.dumps({"error": response.text}, indent=4))
    except Exception as e:
        print(json.dumps({"error": str(e)}, indent=4))

def get_sensor_data(sensor_name):
    """Get data from a specific sensor."""
    try:
        response = requests.get(f"{base_url}/data/{sensor_name}")
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4))
        else:
            print(json.dumps({"error": response.text}, indent=4))
    except Exception as e:
        print(json.dumps({"error": str(e)}, indent=4))

def update_measurement_period(sensor_name, period):
    """Update the measurement period of a specific sensor."""
    try:
        response = requests.put(f"{base_url}/period/{sensor_name}", json={"period": period})
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4))
        else:
            print(json.dumps({"error": response.text}, indent=4))
    except Exception as e:
        print(json.dumps({"error": str(e)}, indent=4))

def main():
    print("Welcome to the Sensor Client Interface")
    while True:
        print("\nMenu:")
        print("1. List all sensors")
        print("2. Get sensor data")
        print("3. Update measurement period")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            list_sensors()
        elif choice == "2":
            sensor_name = input("Enter sensor name: ")
            get_sensor_data(sensor_name)
        elif choice == "3":
            sensor_name = input("Enter sensor name: ")
            try:
                period = int(input("Enter new measurement period (seconds): "))
                update_measurement_period(sensor_name, period)
            except ValueError:
                print(json.dumps({"error": "Invalid period. Please enter an integer."}, indent=4))
        elif choice == "4":
            print(json.dumps({"message": "Exiting the client interface."}, indent=4))
            break
        else:
            print(json.dumps({"error": "Invalid choice. Please try again."}, indent=4))

if __name__ == "__main__":
    main()

