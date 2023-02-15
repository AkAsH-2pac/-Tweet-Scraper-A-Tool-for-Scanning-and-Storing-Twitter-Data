import pymongo
def insert_to_mongo(tweets):
    def connect_to_mongo():
        client = pymongo.MongoClient(
            "mongodb+srv://akash:1234@twitterscrapetest.mu23tqj.mongodb.net/?retryWrites=true&w=majority")
        db = client["Tesla_Tweets_DB"]
        tweets_collection = db["Tesla_Tweets_"]
        return tweets_collection

