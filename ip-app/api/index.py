from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/")
async def return_ip(request: Request):
    # Response so that there is no quotation wrapping
    return Response(content=request.client.host)
