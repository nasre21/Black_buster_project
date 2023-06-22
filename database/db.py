import mysql.connector

def connectdb():
    try:
        conn = mysql.connector.connect(
            host='containers-us-west-69.railway.app',
            port=7127,
            user='root',
            password='npt4hAheAG9gcLJ9TpGy',
            database='Blockbuster'
    )
        print('Connecting to Blockbuster')

    except Exception as e:
        print(f'Error connecting to Blockbuster: {e}')

    return conn

connectdb()