from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
      <!DOCTYPE html>
        <html>

        <head>
            <title>Zinpage</title>
        </head>

        <body>
            <h2>Welcome To Zinpage</h2>
            <p>
                Generate your digital menu in just 5 mins!
            </p>
            <a href="mailto:hellochaitanyavaddi@gmail.com">The work is inprogess</a>
        </body>

        </html>
    """