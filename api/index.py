from fastapi import FastAPI, Request

app = FastAPI()



@app.get("/api/", tags=["Root"])
async def plain_api():
  return {
		"message": "Hello /api/",
   }


@app.get("/{req_path:path}")
@app.get("/{req_path:path}/")
async def serve_my_app(request: Request, req_path: str):
    print(f"path: {req_path}")
    return {
		"message": "Hello /{path}",
 	}



@app.get("/api/{req_path:path}")
@app.get("/api/{req_path:path}/")
async def serve_my_app(request: Request, req_path: str):
    print(f"path: {req_path}")
    return {
		"message": "Hello /api/{path}",
 	}
