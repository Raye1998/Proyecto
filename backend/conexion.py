import pyodbc

def connection_db():
    server = "darkgrepher"
    database = "Hospital"
    username = "usr_darkgrepher"
    password = "pokemon1"
    
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    
    try:
        conn = pyodbc.connect(conn_str)
        print("Conexión establecida con éxito.")
        return conn
    
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
