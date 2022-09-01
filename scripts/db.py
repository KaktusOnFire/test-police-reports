import csv
import time
import asyncpg
import asyncio
import sys

from threading import Thread
from datetime import datetime
import pytz


def bg_async(func):
    def wrapper():
        loop = asyncio.new_event_loop()
        loop.run_until_complete(func)
    
    Thread(target=wrapper).start()

async def async_insert(values, db_url, db_table):
    conn = await asyncpg.connect(db_url)

    await conn.executemany(f'''
        INSERT INTO {db_table} (
                    crime_id,crime_type,report_date, 
                    call_date,offense_date,call_time, 
                    call_datetime,disposition,address, 
                    city,state,agency_id,address_type,common_location) 
        VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14)''', values)

    await conn.close()

def main():
    row_count = None
    filename = input("Enter csv file name: ")
    db_url = input("Enter PostgreSQL database URL (like postgresql://user:pass@host/database): ")
    db_table = input("Enter target table name: ")
    
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        sys.stdout.write("Getting csv rows count... ")
        sys.stdout.flush()
        row_count = sum(1 for row in datareader) - 1
        sys.stdout.write("Done!\n")

    start = time.time()
    with open(filename, 'r') as csvfile:        
        datareader = csv.reader(csvfile)
        iteration_counter = 0
        total_counter = 0

        values = []
        next(datareader, None)
        for row in datareader:
            iteration_counter += 1
            total_counter += 1
            sys.stdout.write(f"\rProgress - {total_counter}/{row_count}. Time elapsed - {'{:.3f}'.format(time.time() - start)} seconds.")
            sys.stdout.flush()

            if iteration_counter > 25000:
                bg_async(async_insert(values, db_url, db_table))
                iteration_counter = 1
                values = []

            row[0] = int(row[0])
            row[2] = datetime.fromisoformat(row[2])
            row[3] = datetime.fromisoformat(row[3])
            row[4] = datetime.fromisoformat(row[4])
            row[5] = pytz.utc.localize(datetime.fromisoformat(row[6]))
            row[6] = pytz.utc.localize(datetime.fromisoformat(row[6]))
            row[11] = int(row[11])
            values.append(row)
        if len(values) != 0:
            bg_async(async_insert(values, db_url, db_table))

        sys.stdout.write(f"\r[COMPLETED] Progress - {total_counter}/{row_count}. Time elapsed - {'{:.3f}'.format(time.time() - start)} seconds.")

if __name__ == "__main__":
    main()