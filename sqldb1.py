from pymongo import MongoClient
from collections import Counter
import time
import Levenshtein
from collections import deque
# Establish connection with MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["licensePlatesDatabase"]
collection = db["LicensePlates"]

# Dictionary to store license plate occurrences in a time window
license_plate_counts = {}
time_window = 1  # Check every 1 second


def get_most_frequent_plate():
    """Return the most frequent license plate detected in the current time window."""
    if not license_plate_counts:
        return None
    
    # Find the most common license plate
    most_common_plate, _ = Counter(license_plate_counts).most_common(1)[0]
    
    return most_common_plate

def is_similar_plate(new_plate):
    """Check if the new license plate is a minor variation of an existing one."""
    existing_plates = collection.find({}, {"_id": 0, "license_plate": 1})
    
    for plate in existing_plates:
        if "license_plate" in plate:
          existing_plate = plate["license_plate"]
          similarity_ratio = Levenshtein.ratio(existing_plate, new_plate)
          edit_distance = Levenshtein.distance(existing_plate, new_plate)
        
        # If similarity is 80% or higher, consider it a duplicate
        if similarity_ratio >= 0.8 or edit_distance <= 2:
            return True

    return False


def insert_license_plate(start_time, end_time, license_plate, violation_type):
    """Insert license plate data into MongoDB, avoiding duplicates and OCR variations."""
    
    global license_plate_counts

    # Normalize the plate format (removing extra spaces, standardizing letters)
    license_plate = license_plate.strip().replace(" ", "").upper()

    if is_similar_plate(license_plate):
        return
    
    most_frequent_plate = get_most_frequent_plate()

    # Update frequency count
    if license_plate in license_plate_counts:
        license_plate_counts[license_plate] += 1
    else:
        license_plate_counts[license_plate] = 1

    # Wait for 1 second before finalizing the most frequent plate
    time.sleep(time_window)

    # Get the most frequently occurring plate
    most_frequent_plate = get_most_frequent_plate()

    if most_frequent_plate:
        # Check if it already exists in the database
        if license_plate_counts[most_frequent_plate] < 3:
            return
        existing_plate = collection.find_one({"license_plate": most_frequent_plate})

        if not existing_plate:
            collection.insert_one({
                "start_time": start_time,
                "end_time": end_time,
                "license_plate": most_frequent_plate,
                "violation_type": violation_type
            })
            print(f"✅ License plate '{most_frequent_plate}' inserted with violation: {violation_type}")
        else:
            pass

    # Clear the license plate counts after storing the most frequent one
    license_plate_counts.clear()

def get_stored_license_plates():
    """Fetch all unique stored license plates from the database."""
    plates = collection.find({}, {"_id": 0, "license_plate": 1, "violation_type":1})
    return [(plate["license_plate"], plate["violation_type"]) for plate in plates if "license_plate" in plate and "violation_type" in plate]



