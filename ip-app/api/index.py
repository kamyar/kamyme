from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def plain_lol():
  return {
		"message": "Hello /lol/",
   }
