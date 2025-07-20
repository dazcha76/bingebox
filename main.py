from fastapi import FastAPI

app = FastAPI()

@app.get("/shows")
def get_shows():
  return {"message": "Hello World!"}