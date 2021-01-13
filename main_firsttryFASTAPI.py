# Goals:
#1) Connect FastAPI to the static websites
#2) Connect FastAPI to the MySQL databse
#3) Create a security and login functionality and interface
#4) Make it all run queries for tables --> SQLALCHEMY?


import aiofiles as aiofiles

import fastapi as fastapi
import uvicorn


from fastapi import FastAPI, Form
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="")


@app.post("/user/")
async def files(
                    request:           Request,
                    username: str    = Form(...),
                    password: str    = Form(...),
                ):
    print('username', username)
    print('password', password)
    return templates.TemplateResponse(
        'exploring_page.html',
        {
            'request':  request,
            'username': username,
        }
                                        )


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('initial_page.html', {'request': request})

from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("static")



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)