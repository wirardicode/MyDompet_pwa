from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from sqlBridge import sub, debitUpdate, showDataTunai, infoUang, infoDebit
from fastapi.middleware.cors import CORSMiddleware
#
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()
app = FastAPI()

# Token tetap yang akan kamu verifikasi
VALID_TOKEN = "Z3T4WA1FUKU"

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != VALID_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
    return credentials.credentials

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class tunai(BaseModel):
    Pemasukan:int
    Pengeluaran:int
    Keterangan:str

class Update(BaseModel):
    UpdateDebit:int

@app.get('/')
def root():
    return{200, "hello word"}

@app.post('/send')
def inputTunai(tunai:tunai):
    try:
        sub(tunai.Pemasukan, tunai.Pengeluaran, tunai.Keterangan)
        return{"status": 200, "message": "saved"}
    except:
        return{"status": 500, "message": "Error"}
    
@app.post('/debit')
def update(Update:Update):
    try:
        debitUpdate(Update.UpdateDebit)
        return{"status": 200, "message": "saved"}
    except:
        return {"status": 500, "message": "Error"}

@app.get('/tunai')
def getTunai():
    try:
        data = showDataTunai()
        return {'status': 200, 'message': "Success fecthing", 'data': data}
    except:
        return {'status': 500, 'message': "Failed fecthing"}

#contoh untuk eksekusi token  
#@app.get("/secure-data")
#def secure_data(token: str = Depends(verify_token)):
#    return {"data": "Ini data rahasia yang butuh token"}

@app.get("/geting-total")
def secure_data(token: str = Depends(verify_token)):
    try:
        totalin=infoUang()
        return {'status': 200, 'data': totalin}
    except:
        return {'satus':500, 'message': 'error'}

@app.get('/get-debit')
def secureDebit(token: str = Depends(verify_token)):
    try:
        debit = infoDebit()
        return {'status': 200, 'message': debit}
    except:
        return {'status': 500, 'message': 'error'}