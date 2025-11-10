import os

# Login feature, if you want then True , if you dont want then False
LOGIN_SYSTEM = bool(os.environ.get('LOGIN_SYSTEM', True)) # True or False

if LOGIN_SYSTEM == False:
    # if login system is false then fill your tg account session below 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

# Bot token @Botfather
BOT_TOKEN = os.environ.get("8517968392:AAGZk9F1jPRxfV5WXLk9CbLrq78Zcg9qR94", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("22951848", ""))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("178201e3c0577efb4c1acba9863ed669", "")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5751472348"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("mongodb+srv://nehalsingh20242024_db_user:7CPP7raHTop05HR2@cluster0.zv4n0if.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("nehalsingh20242024", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
