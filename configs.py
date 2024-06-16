from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "29554659"))
    API_HASH = getenv("API_HASH", "7257d3b3192355ae71ada27cfdc3837c")
    BOT_TOKEN = getenv("BOT_TOKEN", "7150586146:AAGRVQq7GnAzdknNmUl2loEgy-ubaMOKm0k")
    FSUB = getenv("FSUB", "TechMon_UPSC")
    CHID = int(getenv("CHID", "-1002128064285"))
    SUDO = list(map(int, getenv("SUDO", "6815027331").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://techmonofficial:techmon123@cluster0.wo0hzaa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

cfg = Config()
