from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def home():
    return {"message":"come to home"}


@app.get("/users")
def users_list():
    return {"name":"ram","age":23,"role":"backend"}



@app.get("/get_product")
def get_product():
    return {"id":1,"name":"laptop","price":100000}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0",port="8000")
    