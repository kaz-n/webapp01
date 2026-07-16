# webapp01

Sample FastAPI app that returns the current datetime at GET /now.

Run the app locally:

    python -m uvicorn app.main:app --reload

Run tests:

    pip install -r requirements.txt
    pytest