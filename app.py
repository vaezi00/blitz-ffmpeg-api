from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok", "service": "blitz-ffmpeg-api"}


@app.get("/health")
def health():
    return {"status": "healthy"}
