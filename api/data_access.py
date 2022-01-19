from pymongo import MongoClient

import config

connection_string = (f"mongodb+srv://{config.user}:{config.password}"
                     f"@{config.cluster}/{config.db_name}?"
                     f"retryWrites=true&w=majority&ssl=true"
                     f"&ssl_cert_reqs=CERT_NONE")

client = MongoClient(connection_string, serverSelectionTimeoutMS=2000)
db = client[config.db_name]
collection = db[config.collection_name]
