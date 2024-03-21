#read the records
#remove record from file
import json
import msvcrt



def check_10_records(total_records,data):
    total_alive = 0
    index = 0
    for record in data:
        if index >= total_records:
            deaths = record['deaths']
            births = record['births']
            if total_records < deaths:
                return index
            total_alive = births - deaths

            
            if index == total_records + 10:
                break
        index += 1




# load the data 
def load_data():
    # Open the JSON file in read/write mode
    with open('db/records.json', 'r+') as file:
        # Acquire an exclusive lock for both reading and writing
        msvcrt.locking(file.fileno(), msvcrt.LK_LOCK)

        # Read the JSON data
        file.seek(0)  # Move the file pointer to the beginning
        json_data = json.load(file)

        # Modify the JSON data (example)
        json_data['new_key'] = 'new_value'

        # Write the modified JSON data back to the file
        file.seek(0)  # Move the file pointer to the beginning
        json.dump(json_data, file, indent=4)
        file.truncate()

        # Release the lock on the file
        msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK)
    
# Example usage:
filename = 'data.json'
load_data(filename)
 



