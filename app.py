from fastapi import FastAPI 


app = FastAPI()

@app.get('/') #this is the path/route
def index():
    return "This is the front page"

    
 @main.get('about')
 def about():
    return "About page"