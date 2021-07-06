from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    print("hello ")
    return "I AM HERE _ >"
