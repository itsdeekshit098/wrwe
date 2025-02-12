from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Replace these values with your actual MySQL database information
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "sql@hansi123mgp",
    "database": "TripDetails",
}

def create_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('indexc.html')

@app.route('/submit', methods=['GET'])
def submit():
    if request.method == 'GET':
        name_of_driver = request.args.get('nameofdriver')
        vehicle_number = request.args.get('vehicle_number')
        date_and_time = datetime.strptime(request.args.get('date'), '%Y-%m-%dT%H:%M')
        starting_km = request.args.get('s_km')
        ending_km = request.args.get('e_km')

        connection = create_connection()
        cursor = connection.cursor()

        # Insert data into MySQL
        sql = "INSERT INTO TripDetails (DriverName, VehicleNumber, DateTime, StartingKilometer, EndingKilometer) VALUES (%s, %s, %s, %s, %s)"
        values = (name_of_driver, vehicle_number, date_and_time, starting_km, ending_km)

        try:
            cursor.execute(sql, values)
            connection.commit()
        except Exception as e:
            print("Error:", e)
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    return redirect(url_for('display'))
@app.route('/display')
def display():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    # Retrieve data from MySQL
    sql = "SELECT * FROM TripDetails"
    cursor.execute(sql)
    trips = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('display1.html', trips=trips)
    
@app.route('/delete/<int:trip_id>', methods=['POST'])
def delete(trip_id):
    connection = create_connection()
    cursor = connection.cursor()

    # Delete the record with the specified TripID
    sql = "DELETE FROM TripDetails WHERE TripID = %s"
    values = (trip_id,)

    try:
        cursor.execute(sql, values)
        connection.commit()
    except Exception as e:
        print("Error:", e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

    # Redirect back to the display page after deletion
    return redirect(url_for('display'))

if __name__ == '__main__':
    app.run(debug=True)
