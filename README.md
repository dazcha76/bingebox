### 🚀 Project Setup Instructions
Follow these steps to get your environment up and running after cloning this repository.

### ✅ Prerequisites
Python 3.10+  
PostgreSQL instance (local or remote)  
virtualenv or your preferred environment manager

### 📦 1. Clone the Repository
HTTPS: `git clone https://github.com/your-username/your-repo-name.git`  
SSH: `git@github.com:dazcha76/bingebox.git`  
`cd your-repo-name`

### 📁 2. Create and Activate a Virtual Environment
`python3 -m venv venv`  
`source venv/bin/activate` # On Windows: venv\Scripts\activate

### 📚 3. Install Dependencies
`pip install -r requirements.txt`

### 🔐 4. Create a .env File
In the root directory, create a .env file to store your database credentials:  

POSTGRES_SERVER=localhost  
POSTGRES_PORT=5432  
POSTGRES_USER=your_user  
POSTGRES_PASSWORD=your_password  
POSTGRES_DATABASE=your_db  

⚠️ Ensure the database exists and the credentials are correct.

### 🛠️ 5. Initialize the Database Tables
Run the following to create the required tables:  

`uvicorn main:app --reload`  

Once the app runs for the first time, SQLAlchemy will create the tables automatically via:  
`models.Base.metadata.create_all(bind=engine)`  

You can stop the server once the tables are created.  

### 🌱 6. (Optional) Seed the Database with Fake Data
`python3 seed.py`  

This uses Faker to populate your shows table with dummy data.  

### 🚀 7. Run the Application
`uvicorn main:app --reload`  

Visit the FastAPI interactive docs at:  
📍 http://127.0.0.1:8000/docs  

### 📬 API Endpoints Preview

GET /shows - List shows with filters and pagination  
GET /shows/{id} - Retrieve a single show  
POST /shows - Add a new show  
PATCH /shows/{id} - Toggle a show's "favorite" status  
GET /shows/{show_id}/episodes - List episodes by show  
GET /shows/{show_id}/actors - List actors by show  
GET /shows/{actor_id}/shows - List shows by actor 

### 🧹 Troubleshooting
Missing Tables? Make sure your .env is configured and the DB exists.  
Database connection error? Check PostgreSQL is running and accessible.  
Modules not found? Ensure you're in the virtual environment and dependencies are installed.  
