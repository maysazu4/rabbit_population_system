class last_read:
    def __init__(self):
        self.total_records = 0
        self.alive = 100

def analyze_data():
    #check if there are 10 new records in the database
    #if so read them
    #while reading check if the deaths number is not bigger than the alive number
    #if so stop the reading and delete the record from the database and try to read again
    #else continue and update the total_records and the alive number
    #print the data


