**FastAPI MongoDB CRUD Application**

This project is a FastAPI application that performs CRUD operations with MongoDB. It includes item management, filtering, and aggregation using FastAPI's routing mechanism.

----Table of Contents----
->Project Setup
->Running the Project
->API Endpoints
   Create an Item
   Get an Item by ID
   Filter Items
   Update an Item
   Delete an Item
   Aggregate Items
->Dependencies

**Project Setup**
1. Clone the Repository

git clone https://github.com/your-username/your-repo-name.git
cd 

2. Create a Virtual Environment
#Create a virtual environment and activate it.

python -m venv env
env\Scripts\activate


3. Install Dependencies
#Install the required dependencies from the requirements.txt file.

pip install -r requirements.txt

4. Set Up MongoDB
#MongoDB is installed and running on your local machine 
#I setup the MongoDb details in database.py module
MONGO_URI="mongodb://localhost:27017"

5. Run the Application
Run the FastAPI app using Uvicorn:
uvicorn main:app --reload

The application will now be running at: http://127.0.0.1:8000

You can also access the automatically generated API documentation at: http://127.0.0.1:8000/docs

**Running the Project**
-->Start MongoDB
Ensure you have installed the required dependencies using pip install -r requirements.txt.
Run the application using uvicorn main:app --reload.

-->API Endpoints
**About items details**

1. Create an Item
Endpoint: /items

Method: POST

Description: Adds a new item to the MongoDB database.

Request Body Example:

{
  "name": "Item1",
  "email": "shopping@example.com",
  "item_name": jeans
  "quantity": 10,
}
Response Example:

{
  "id": "64ac7c5e123456789abcdef0"
}

2. Get an Item by ID
Endpoint: /items/{id}

Method: GET

Description: Retrieves an item by its MongoDB ObjectId.

Response Example:
{
  "_id": "64ac7c5e123456789abcdef0",
  "name": "Item 1",
  "email": "user@example.com",
  "quantity": 10,
  "expiry_date": "2024-12-31",
  "insert_date": "2023-07-15T12:34:56"
}

3. Filter Items
Endpoint: /items/filter_by

Method: GET

Description: Filters items based on various parameters such as email, expiry_date, insert_date, and quantity.

Query Parameters:

email: Filter by email address.
expiry_date: Filter by expiry date (greater than).
insert_date: Filter by insert date (greater than).
quantity: Filter by quantity (greater than or equal).
Example Request:

GET /items/filter_by?email=user@example.com&quantity=5


4. Update an Item
Endpoint: /items/{id}

Method: PUT

Description: Updates an existing item in the database by its ObjectId.

Request Body Example:

{
  "name": "Updated Item",
  "quantity": 15
}
Response Example:

{
  "msg": "Item updated"
}

5. Delete an Item
Endpoint: /items/{id}

Method: DELETE

Description: Deletes an item from the database by its ObjectId.

Response Example:

{
  "msg": "Item deleted"
}


6. Aggregate Items
Endpoint: /items/aggregate

Method: GET

Description: Aggregates items by grouping them by email and returning the total count of items per email.

Response Example:

[
  {
    "_id": "user@example.com",
    "total_items": 5
  }
]

**About clock-in details**

1. Create an clock-in
Endpoint: /clock-in

Method: POST

Description: Adds a new details to the MongoDB database.

Request Body Example:

{
  "email": "email@example.com"
  "location": "hyderabad'

}
Response Example:

{
  "id": "64ac7c5e123456789abcedf3"
}

2. Get an details by ID
Endpoint: /clock-in/{id}

Method: GET

Description: Retrieves an details by its MongoDB ObjectId.

Response Example:
{
  "_id": "64ac7c5e123456789abcedf3"
  "email": "email@example.com",
  "location": "hyderabad"
  "insert_date": "2023-07-15T12:34:56"
}

3. Filter details
Endpoint: /clock-in/filter

Method: GET

Description: Filters details based on various parameters such as email, location, insert_date.

Query Parameters:

email: Filter by email address.
insert_date: Filter by insert date (greater than).
location: Filter by location
Example Request:

GET /items/filter_by?email=email@example.com&location=hyderabad


4. Update an details
Endpoint: /clock-in/{id}

Method: PUT

Description: Updates an existing details in the database by its ObjectId.

Request Body Example:

{
  "location": "Hyderabad",
  
}
Response Example:

{
  "msg": "Clock-in record updated"
}

5. Delete an details
Endpoint: /clock-in/{id}

Method: DELETE

Description: Deletes an details from the database by its ObjectId.

Response Example:

{
  "msg": "Clock-in record deleted"
}




