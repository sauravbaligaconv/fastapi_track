import fastapi
from fastapi import Request,status,FastAPI

app = FastAPI()

@app.get('/myip')
def my_endpoint(request: Request):
    ip = request.client.host
    print(ip)
    return {'status': 1,'message': 'ok','ip':ip}
