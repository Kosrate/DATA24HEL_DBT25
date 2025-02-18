from database.mongo_connection import get_db_connection

def get_products_to_reorder():
    """Hämtar produkter där ReorderLevel > UnitsInStock + UnitsOnOrder."""
    db = get_db_connection()
    collection = db["products"]
    
    query = {"ReorderLevel": {"$gt": {"$add": ["$UnitsInStock", "$UnitsOnOrder"]}}}
    products = list(collection.find(query, {"ProductName": 1, "CompanyName": 1, "ContactName": 1, "Phone": 1}))
    
    return products

def get_all_products():
    """Hämtar alla produkter från databasen."""
    db = get_db_connection()
    collection = db["products"]
    
    products = list(collection.find({}, {"ProductName": 1, "CompanyName": 1, "ContactName": 1, "Phone": 1, "UnitsInStock": 1, "UnitsOnOrder": 1, "ReorderLevel": 1}))
    
    return products
