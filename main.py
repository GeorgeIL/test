# import streamlit as st
# import pymongo

# # # Initialize connection.
# # # Uses st.cache_resource to only run once.
# # @st.cache_resource
# # def init_connection():
# #     return pymongo.MongoClient(**st.secrets["mongo"])

# # client = init_connection()

# # # Pull data from the collection.
# # # Uses st.cache_data to only rerun when the query changes or after 10 min.
# # @st.cache_data(ttl=600)
# # def get_data():
# #     db = client.mydb
# #     items = db.mycollection.find()
# #     items = list(items)  # make hashable for st.cache_data
# #     return items

# # items = get_data()

# # # Print results.
# # for item in items:
# #     st.write(f"{item['name']} has a :{item['pet']}:")
# # st.title("Main Page")

# st.header("Transactions")
# col1, col2 = st.columns(2)
# with col1:
#     st.button("Remove Transaction", help="", use_container_width=True, icon="➖")
# with col2:
#     st.button("Add Transaction", help="Goes to transaction page", use_container_width=True, icon="➕", )
    

import pymongo as mg

from dotenv import load_dotenv
import os

load_dotenv()  # reads .env

connection_string = os.getenv("DB_CS")
db_name = "FinTrack"
collection_transactions = "Transactions"

# Configure DB connection and information
client = mg.MongoClient(connection_string)
db = client[db_name]
collection = db[collection_transactions]

# ... perform operations ...
res = collection.find().to_list()

# Close the client
client.close()