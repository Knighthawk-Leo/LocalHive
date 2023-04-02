import json
from sqlalchemy import create_engine, text

from access_points import get_scanner
db_str = "mysql+pymysql://ym0a12i67m4ls4f9z9xo:pscale_pw_nm9rVx8r09dPPkqdA2WBkStXkDGfazsZcJeHfyTE4c0@aws.connect.psdb.cloud/localhive?charset=utf8mb4"
db_connection_string = db_str
engine = create_engine(
	db_connection_string,
	connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)


def access():
    wifi_scanner = get_scanner()
    return(wifi_scanner.get_access_points())
# query_string = """
# CREATE TABLE Localhive (
# 	id INT AUTO_INCREMENT PRIMARY KEY,
#  	Device VARCHAR(230),
#     Data TEXT
# );
# """
a=access()
a_str = str(a).replace("'","\\'")

query_string = f"""
INSERT INTO `localhive`.`Localhive` (`Device`, `Data`) VALUES ('Yash', '{a_str}');
"""

#query_string = """SHOW TABLES"""
# query_string = """SELECT * FROM Localhive"""
def execute_query():
	with engine.connect() as conn:
		result = conn.execute(text(query_string))
		print(result.all())
execute_query()