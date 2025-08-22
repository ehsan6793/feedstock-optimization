from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def test_endpoint():
    return {"message": "سلام! بک‌اند FastAPI کار می‌کند!"}