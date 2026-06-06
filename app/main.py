from fastapi import FastAPI

app = FastAPI(title="XSOLA API")

@app.get("/")
def home():
    return {"message": "XSOLA backend running"}