from fastapi import FastAPI, Request
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import File, UploadFile
from estimator.components.predict import Prediction

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
TEMPLATES = Jinja2Templates(directory='templates')
searchedImages = []
predict_pipe = Prediction()


@app.get("/", status_code=200)
@app.post("/")
async def index(request: Request):
    return TEMPLATES.TemplateResponse(name='index.html', context={"request": request})


@app.post('/image')
async def upload_file(file: UploadFile = File(...)):
    global searchedImages, predict_pipe
    try:
        contents = file.file.read()
        searchedImages = predict_pipe.run_predictions(contents)
        return {"message": "Prediction Completed"}
    except Exception as e:
        return {"message": f"There was an error uploading the file {e}"}


@app.post('/reload')
def reload():
    global searchedImages
    searchedImages = []
    return


@app.post('/reload_prod_model')
def reload():
    global predict_pipe
    try:
        predict_pipe = Prediction()
        return {"Response": "Successfully Reloaded"}
    except Exception as e:
        return {"Response": e}


@app.get('/gallery')
async def gallery(request: Request):
    global searchedImages
    return TEMPLATES.TemplateResponse('gallery.html', context={"request": request, "length": len(searchedImages),
                                                               "searchedImages": searchedImages})


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8080, reload=True)
