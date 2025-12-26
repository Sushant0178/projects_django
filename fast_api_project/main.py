from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"sushant":"9763280178"}

