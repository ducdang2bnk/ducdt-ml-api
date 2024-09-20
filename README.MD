git clone git@github.com:ducdang2bnk/ducdt-ml-api.git
create env
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt



run by comand line: uvicorn app.main:app --reload

run project by pycharm
    name: uvicorn
    env
    module: uvicorn
    script: app.main:app --reload
    working directory: /media/bnk/data/data/ducdt-ml-api