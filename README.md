<h1 align="center"> SearchEngine-PredictionEndpoint</h1>

<hr>

## <img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="25"> <b> API</b>

1. Landing page of application

![Screenshot](snippets/snip1.png)

2. User uploads an image
![Screenshot](snippets/snip2.png)

3. If at this stage user want to upload another image then click on RELOAD
![Screenshot](snippets/snip1.png)

4. If user clicks on Search images then Galler API will get hit
![Screenshot](snippets/snip3.png)

`Note : In visual matches I kept static image files, which can be made dynamic based on search engine results`

💻 How to setup:

Creating conda environment
```
conda create -p venv python==3.8 -y
```

activate conda environment
```
conda activate ./venv
```

Install requirements
```
pip install -r requirements.txt
```
Run the live server using flask
```
python app.py
```
To launch flask UI
```
http://localhost:5000/
```
