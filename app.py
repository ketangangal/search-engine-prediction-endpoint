from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import File, UploadFile
from estimator.components.predict import Prediction
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
TEMPLATES = Jinja2Templates(directory='templates')
searchedImages = []

predict_pipe = Prediction()


@app.get("/", status_code=200)
@app.post("/")
async def index(request: Request):
    """
    Description : This Route loads the index.html
    """
    return TEMPLATES.TemplateResponse(name='index.html', context={"request": request})


@app.post('/image')
async def upload_file(file: UploadFile = File(...)):
    """
    Description : This Route loads the predictions in a list which will be listed on webpage.
    """
    global searchedImages, predict_pipe
    try:
        if predict_pipe:
            contents = file.file.read()
            searchedImages = predict_pipe.run_predictions(contents)
            return {"message": "Prediction Completed"}
        else:
            return {"message": "First Load Model in Production using reload_prod_model route"}
    except Exception as e:
        return {"message": f"There was an error uploading the file {e}"}


@app.post('/reload')
def reload():
    """
    Description : This Route resets the predictions in a list for reload.
    """
    global searchedImages
    searchedImages = []
    return


@app.get('/reload_prod_model')
def reload():
    """
    Description : This Route is Event Triggered or owner controlled to update
                  the model in prod with minimal downtime.
    """
    global predict_pipe
    try:
        del predict_pipe
        predict_pipe = Prediction()
        return {"Response": "Successfully Reloaded"}
    except Exception as e:
        return {"Response": e}


@app.get('/gallery')
async def gallery(request: Request):
    """
    Description : This Route lists all the predicted images on the gallery.html listing depends on prediction.
    """
    global searchedImages
    return TEMPLATES.TemplateResponse('gallery.html', context={"request": request, "length": len(searchedImages),
                                                               "searchedImages": searchedImages})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

