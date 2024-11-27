import uvicorn
from fastapi import FastAPI

app = FastAPI()

daten_g = {}

file = open("PLZO_CSV_LV95.csv", encoding="iso-8859-1")
next(file)

for line in file:
    data = line.strip().split(";")
    ortschaftsname = data[0]
    plz = data[1]
    Zusatzziffer = data[2]
    Gemeindename = data[3]
    BFSNr = data[4]
    Kantonskuerzel = data[5]
    E = data[6]
    N = data[7]
    Sprache = data[8]
    daten_g[ortschaftsname] = {
        "Ortschaftsname": ortschaftsname,
        "PLZ": plz,
        'Zusatzziffer': Zusatzziffer,
        'Gemeindename': Gemeindename,
        'BFS-Nr': BFSNr,
        "Kantonskuerzel": Kantonskuerzel,
        'E': E,
        'N': N,
        'Sprache': Sprache
    }
file.close()

@app.get("/")
async def basisverzeichnis():
    return {"status": "alles gut, es funktioniert"}

@app.get("/search")
async def search(ort: str):
    if ort in daten_g:
        return daten_g[ort]
    else:
        return {"error": "not found"}
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)