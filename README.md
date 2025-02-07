# internship-takehome
Takehome project for the internship

## Task
Implement a web application!
Use this base code to build your application, submissions will be accepted via a pull request.

some ideas:
- Todo list
- kanban board
- note taking app
- url shortener service
- Some charts
- Some AI service
[more ideas](https://roadmap.sh/backend/projects?difficulty=beginner)


## Running the Application

1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app
   ```

The application will be available at `http://localhost:8000`


## Development
### Development Tips

**Auto-reload during development**
   - FastAPI with uvicorn supports auto-reloading when code changes
   - Use the `--reload` flag: `uvicorn app.main:app --reload`

**Interactive API Documentation**
   - FastAPI automatically generates interactive API docs
   - Access Swagger UI at `/docs` (http://localhost:8000/docs)
   - Access ReDoc at `/redoc` (http://localhost:8000/redoc)


### Project Structure
project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── templates/
│       └── index.html
├── Dockerfile
├── docker-compose.yml
└── requirements.txt

