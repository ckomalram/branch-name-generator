from fastapi import FastAPI
from generate_branches import generate_branch_name

app = FastAPI()


def generate_branches_name(ticket: int, description: str):
    result = generate_branch_name(ticket, description)
    return map_response(result)

def map_response(result: dict):
    response=[]
    for key, value in result.items():
        response.append({ "name": key,
               "value": value
              })
    return response

@app.get('/branches/', tags=['branches'])
def get_branch_name_with_query(ticket: int, description: str):
    response = []
    response = generate_branches_name(ticket, description)
    return response

if __name__ == "__main__":
    generate_branches_name()

