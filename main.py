from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {
        "message" : "Server is running"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    
