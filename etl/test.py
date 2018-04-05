from os import walk
import csv
import psycopg2

conn = psycopg2.connect("dbname=dc_data user=dc_data password=password host=localhost")
cur = conn.cursor()

parking_insert_query = "INSERT INTO parking_violation \
    (\
        x,\
        y,\
        day_of_week,\
        holiday,\
        week_of_year,\
        month_of_year,\
        issue_time,\
        violation_code,\
        violation_description,\
        location,\
        rp_plate_state,\
        body_style,\
        address_id,\
        streetseg_id,\
        xcoord,\
        ycoord,\
        ticket_issue_date\
    )\
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"


def importFile(filename):
    print 'Loading %s' % filename
    with open('../data/'+filename,'rb') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            cur.execute(parking_insert_query, (
                row[0] or None,
                row[1] or None,
                row[4] or None,
                row[5] or None,
                row[6] or None,
                row[7] or None,
                row[8] or None,
                row[9] or None,
                row[10] or None,
                row[11] or None,
                row[12] or None,
                row[13] or None,
                row[14] or None,
                row[15] or None,
                row[16] or None,
                row[17] or None,
                row[18] or None
            ))
        conn.commit()

def importFiles(dir):
    print 'Starting import for files in %s' % dir
    for (dirpath, dirnames, filenames) in walk(dir):
        for filename in filenames:
            if filename.endswith('.csv'):
                importFile(filename)
    cur.close()
    conn.close()
    print 'Import complete!'

importFiles('../data')
