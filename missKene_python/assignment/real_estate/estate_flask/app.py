from flask import Flask
import mysql.connector

app = Flask(__name__)

db_host = 'localhost'
db_user = 'root'
db_password = ''
db_database = 'real_estate'


def get_properties():
    mysqldb = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_database)
    mycursor = mysqldb.cursor()
    mycursor.execute('SELECT Property_id,Name,Description,Address,Size,Country,State,Price FROM estate_info')
    rows = mycursor.fetchall()
    mysqldb.close()
    return rows


@app.route('/')
def home():
    return '''<h1 style="color: blue; font-family: sans-serif">Welcome to Real Estate Marketting!!!</h1>
<a href="/properties"><button style="border: none; padding: 15px; border-radius: 10px; font-weight: bold; background-color: skyue;">Properties</button></a>'''


@app.route('/properties')
def preview():
    rows = get_properties()

    table_rows = ''
    for property_id, name, description, address, size, country, state, price in rows:
        table_rows += f'''
        <tr>
            <td>{property_id}</td>
            <td>{name}</td>
            <td>{description}</td>
            <td>{address}</td>
            <td>{size}</td>
            <td>{country}</td>
            <td>{state}</td>
            <td>{price}</td>
        </tr>'''

    return f'''
    <html>
    <head>
        <title>Real Estate Marketing</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
            th {{ background: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>Real Estate Marketing</h1>
        <table>
            <tr>
                <th>Property ID</th><th>Name</th><th>Description</th><th>Address</th>
                <th>Size</th><th>Country</th><th>State</th><th>Price</th>
            </tr>
            {table_rows}
        </table>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)