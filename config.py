import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = 7108671

API_HASH = "51aaf9384a31af3e7068118883614867"

BOT_TOKEN = "5487546429:AAHZYxHGu2BCOJB-w5ZmxRq1Ni8cMOtP0AA"

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = "M4u_video"     

DB_URL = "mongodb+srv://enrich:enrich@cluster0.mhghl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
 
FLOOD = "10"

START_PIC = "https://telegra.ph/file/3678dcf40bc9bfed7b79e.jpg"

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1121140181').split()]

