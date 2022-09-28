from fastapi import FastAPI, Request
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import File, UploadFile

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
TEMPLATES = Jinja2Templates(directory='templates')


@app.get("/", status_code=200)
@app.post("/")
async def index(request: Request):
    return TEMPLATES.TemplateResponse(name='index.html', context={"request": request})


@app.post('/image')
def upload_file(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
