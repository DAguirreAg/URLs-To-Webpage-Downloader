from fastapi import FastAPI
from starlette.responses import RedirectResponse
import webpage_downloader

app = FastAPI()

@app.get("/")
def main():
    response = RedirectResponse(url='/docs')
    return response

@app.get("/download_webpages")
def download_webpages(frequency: str):

    if frequency not in Config.FREQUENCIES:
        return None

    webpage_downloader.main(frequency)

    return None
