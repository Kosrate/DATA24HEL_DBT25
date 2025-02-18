from database.mongo_connection import get_db_connection

def get_products_to_reorder():
    """Hämtar produkter där ReorderLevel > UnitsInStock + UnitsOnOrder."""
    db = get_db_connection()
    collection = db["products"]

    query = {"ReorderLevel": {"$gt": {"$sum": ["$UnitsInStock", "$UnitsOnOrder"]}}}
    products = list(collection.find(query, {"ProductName": 1, "CompanyName": 1, "ContactName": 1, "Phone": 1}))

    return products
