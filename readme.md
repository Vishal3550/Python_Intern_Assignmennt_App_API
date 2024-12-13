# README.md

## Django API for Managing App Details

This project implements a Django-based API to manage app details. The API includes the following endpoints:
- **POST /api/add-app**: Add app details to the database.
- **GET /api/get-app/{id}**: Retrieve app details by ID.
- **DELETE /api/delete-app/{id}**: Remove an app by ID.

---

### **Setup Instructions**

#### **Prerequisites**
- Python 3.8 or above installed
- `pip` package manager installed

#### **Steps to Set Up**

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd app_management
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django
   ```

4. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the API**
   Open your browser or API testing tool (e.g., Postman) and access `http://127.0.0.1:8000/api/`.

---

### **API Endpoints**

#### **1. Add App Details**
- **Endpoint**: `POST /api/add-app`
- **Description**: Adds a new app to the database.
- **Request Body**:
  ```json
  {
      "app_name": "Example App",
      "version": "1.0",
      "description": "This is a sample app."
  }
  ```
- **Response**:
  ```json
  {
      "message": "App added successfully!",
      "id": 1
  }
  ```

#### **2. Get App Details by ID**
- **Endpoint**: `GET /api/get-app/{id}`
- **Description**: Retrieves the details of an app by its ID.
- **Response**:
  ```json
  {
      "app_name": "Example App",
      "version": "1.0",
      "description": "This is a sample app."
  }
  ```

#### **3. Delete App by ID**
- **Endpoint**: `DELETE /api/delete-app/{id}`
- **Description**: Deletes an app from the database by its ID.
- **Response**:
  ```json
  {
      "message": "App deleted successfully!"
  }
  ```

---

### **Folder Structure**
```
app_management/
|-- app_api/
|   |-- migrations/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- views.py
|   |-- urls.py
|-- app_management/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- db.sqlite3
|-- manage.py
|-- README.md
```

---

### **Testing the API**

1. **Using Postman**
   - Add app details via `POST /api/add-app`.
   - Retrieve app details via `GET /api/get-app/{id}`.
   - Delete app via `DELETE /api/delete-app/{id}`.

2. **Using cURL**
   - Add app details:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"app_name": "Example App", "version": "1.0", "description": "Sample description."}' http://127.0.0.1:8000/api/add-app
     ```
   - Retrieve app details:
     ```bash
     curl -X GET http://127.0.0.1:8000/api/get-app/1
     ```
   - Delete app:
     ```bash
     curl -X DELETE http://127.0.0.1:8000/api/delete-app/1
     ```

---

### **Notes**
- Ensure that the development server is running before testing the API.
- For production deployment, configure settings (e.g., `ALLOWED_HOSTS`, `DEBUG=False`, and database).


