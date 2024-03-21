import random
import sensor.generate as g
import time
import sensor.write_to_db as w




def main():
   records_num = random.randrange(100,300)
   while(records_num):
      record = g.generate_record()
      w.write_to_file(record)
      seconds_to_sleep = random.randrange(5,10)
      time.sleep(seconds_to_sleep)
      records_num -= 1


      
if __name__ == '__main__':
   main()
