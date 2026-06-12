from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pickle

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Load model and vectorizer
with open("app/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("app/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(
        request: Request,
        message: str = Form(...)
):

    transformed = vectorizer.transform([message])

    probabilities = model.predict_proba(transformed)[0]

    ham_prob = round(probabilities[0] * 100, 2)
    spam_prob = round(probabilities[1] * 100, 2)

    if spam_prob > ham_prob:
        result = "SPAM EMAIL"
        score = spam_prob
    else:
        result = "SAFE EMAIL"
        score = ham_prob

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "request": request,
            "result": result,
            "score": score,
            "spam_prob": spam_prob,
            "ham_prob": ham_prob
        }
    )