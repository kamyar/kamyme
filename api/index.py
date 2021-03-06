from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/api/hello/")
async def plain_lol():
  return {
		"message": "Hello /lol/",
   }


@app.get("/{req_path:path}")
@app.get("/{req_path:path}/")
async def serve_my_app(request: Request, req_path: str):
    print(f"path: {req_path}")
    return {
		"message": f"Hello /{req_path}",
 	}



@app.get("/api/{req_path:path}")
@app.get("/api/{req_path:path}/")
async def laa(request: Request, req_path: str):
    print(f"path: {req_path}")
    return {
		"message": f"Hello /api/{req_path}",
 	}

