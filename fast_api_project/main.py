from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def root():
    return {"sushant":"9763"}

@app.get("/posts")
def get_posts():
    return {"data":"this is you post "}


@app.delete("/posts/{id}")
def ok():
    return {"sushant":"9763280178" }


@app.get("/about")
def about():
    return {"data":"this is about page"}




@app.get("/contact")
def contact():
    return {"data":"this is contact page"}


@app.get("/home")
def home():
    return {"data":"this is home page"}


@app.get("/help")
def help():
    return {"data":"this is help page"}