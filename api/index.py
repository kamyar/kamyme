from fastapi import FastAPI

app = FastAPI()


@app.get("/{path}")
def read_root(path: str):
    return {"path": path}


@app.get("/api/{path}")
def read_item(path: str, q: Optional[str] = None):
    return {"path": path}
