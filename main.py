from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import string, random

app = FastAPI(debug=True)
templates = Jinja2Templates(directory="templates")

# In-memory store: short_code -> original_url
url_store = {}

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/shorten", response_class=HTMLResponse)
async def shorten_url(request: Request, long_url: str = Form(...)):
    short_code = generate_short_code()
    url_store[short_code] = long_url
    short_url = f"https://fastapi-url-shortener-1.onrender.com/{short_code}"
    return templates.TemplateResponse("index.html", {
        "request": request,
        "short_url": short_url,
        "long_url": long_url
    })

@app.get("/{short_code}")
async def redirect_to_url(short_code: str):
    long_url = url_store.get(short_code)
    if long_url:
        return RedirectResponse(url=long_url)
    return {"error": "Invalid short URL"}