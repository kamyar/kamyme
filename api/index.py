from fastapi import FastAPI

app = FastAPI(root_path="/api")

@app.get("/", tags=["Root"])
async def plain_api():
  return {
    "message": "Hello /"
   }


@app.get("/api/", tags=["Root"])
async def plain_api():
  return {
    "message": "Hello /api/"
   }


@app.get("/{req_path:path}")
async def serve_my_app(request: Request, req_path: str):
    print(f"path: {req_path}")
    return {
      "message": "Hello /{path}"
 	}



@app.get("/api/{req_path:path}")
async def serve_my_app(request: Request, req_path: str):
    print(f"path: {req_path}")
    return {
      "message": "Hello /api/{path}"
 	}
