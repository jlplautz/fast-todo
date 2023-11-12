from fastapi import FastAPI

app = FastAPI(
    title='Todo List Manager',
    version='0.1.0',
    description='A simple **Todo List** manager API.',
)


@app.get('/')
def hello():
    """texto"""
    return {'message': 'Hello, World!!!'}
