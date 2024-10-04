1. Clean Architecture
2. repository partner
3. fast api
4. sqlalchemy (postgres)




How to install 
1. git clone git@github.com:ducdang2bnk/ducdt-ml-api.git
2. create env
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
3. alembic init alembic
```bash
alembic init alembic
```
4. add "sqlalchemy.url = postgresql://user:password@localhost/dbname" vao alembic.ini
4. run by comand line: uvicorn app.main:app --reload
5. run project by pycharm
    name: uvicorn
    env
    module: uvicorn
    script: app.main:app --reload

    