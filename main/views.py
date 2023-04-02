from django.shortcuts import render
from access_points import get_scanner
from whereami.predict import *


from sqlalchemy import create_engine, text
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

# Create your views here.
def index(request):
    return render(request, 'landing.html')

def home(request):
    li_ssid=[]
    li_security=[]
    li_quality=[]
    a=access()
    for x in range(len(a)):
        li_ssid.append(a[x].ssid)
        li_security.append(a[x].security)
        li_quality.append(a[x].quality)  
    zipped=zip(li_ssid,li_quality,li_security)
    return render(request, 'home.html',{'li':li_ssid,'li_security':li_security,'li_quality':li_quality,'zipped':zipped})    
def access():
    wifi_scanner = get_scanner()
    return(wifi_scanner.get_access_points())


def execute_query(query_string):
	with engine.connect() as conn:
            result = conn.execute(text(query_string))
            print(result)
            return(result.all())
def track(request):
    city=str(request.POST.get('Devicename'))
    print(city)
    query_string = """ SELECT * FROM Localhive where Device='Ranjit' """
    a=execute_query(query_string)
    list_access=a[0][2]
    # a1=predict_proba(eval(list_access))
    # print(a1)
    print(list_access)

    import subprocess
    subprocess.Popen(['python', 'main/imp.py'])
    return render(request, 'tracking.html') 


    


