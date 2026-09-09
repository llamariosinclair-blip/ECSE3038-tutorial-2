readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def list_devices(devices):
    """Prints the device name and temperature."""
    for d in devices:
        print(f"{d['name']} {d['temp']}")

def average_temp(devices):
    """Return the average temperature of all devices."""
    total = sum(d["temp"] for d in devices)
    return total / len(devices)

def hottest_device(devices):
    """Return the dictionary of the device with the highest temperature."""
    return max(devices, key=lambda d: d["temp"])

def to_status(device):
    """Return a dictionary indicating a single device's status."""
    status = "online" if device["online"] else "offline"
    
    device_status = {
        "device": device["name"],
        "status": status,
        "celsius": device["temp"], 
    }
    return device_status

def by_room(devices):
    """Return a dictionary grouping device names by their room."""
    rooms = {}
    for d in devices:
        room = d["room"]
        if room not in rooms:
            rooms[room] = []
        rooms[room].append(d["name"]) 
    return rooms

# --- Execute and Print ---
list_devices(readings)                
print(average_temp(readings))         
print(hottest_device(readings))             
print(to_status(readings[3]))                 
print(by_room(readings))                       