from fastapi import FastAPI


app = FastAPI(
    title=" Tradebulls Automated Video VIPV testing System",
    description="AI-assisted Video In-Person Verification prototype",
    version="1.0.0"
)


@app.get("/")
def root():

    return {
        "message": "Selfie Video VIPV System is running",
        "status": "success"
    }
