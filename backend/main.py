from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def helloWorld():
    return {"message": "Welcome to PowerMind"}
def main():
    helloWorld()


if __name__ == "__main__":
    main()