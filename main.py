from fastapi import FastAPI, Query, status, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles from swagger_i_bundle import swagger_i_path

app = FastAPI(docs_url=None)

app.mount(path: "/swagger-ui", staticFiles(directory=swagger_ui_path), name="swagger-ui")

@app.get(path:"/docs" ,include_in_schema=False)
def custom_swagger_ui():
  return get_swagger_ui_html(
    openapi_ur1="/openapi.json",
    titLe="FastAPI docs",
    swagger_js_url=r"swagger-ui/swagger-ui-bundle.js",
    swagger_css_url=r"swagger-ui/swagger-ui.css"
    )

my_costs ={
  1:{
    "desc": "scarf",
    "amount": 400_000
  },
  2:{
    "desc": "t_shirt",
    "amount: 500_000
  }
  3:{
  "desc": "potato",
  "amount": 600_000
}

@app get ("/home")
def start:
  return my_costs


@app.get("/home/{input_id}")
def start_new(input_id: int | None = None):
  if input_id is None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="you must enter a value")
  else:
    if input_id in my_costs:
      return my_costs[input_id]
    else:
      raise HTTPException(status_code= status. HTTP_404_NOT_FOUND, detail="Not found")


@app.post("/home/{input_id}")
def create_new_costs(input_id:int, thing:str | None = Query(default="test"), cost:int | None= Query(default= 0)):
  if input_id not in my_costs:
    my_costs.update({input_id: {"desc": thing, "amount": cost}})
    return my_costs
  else:
    raise HTTPException(status_codes= status.HTTP_406_NOT_ACCEPTABLE, detail="Not acceptable")


@app.delete("/home")
def delete_new_costs(input_id:int | None = Query(default= None)) :
  if input_id is None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="you must enter a value*)
  if input_id not in my_costs:
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Not found id to delete!")
  eLse:
    del my_costs[input_id]
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/home")
def update_costs(input_id:int | None = Querydefault= None), thing:str | None = Query(default="test_update"), cost:int | None= Query(default= 1)) :
  if input_id is None:
    raise HTTException(status_code= status.HTTP_400_BAD_REQUEST, detai1= "you must enter a value")
  if input_id not in my_costs:
    raise HTTPException(status_codes= status.HTTP_404_NOT_FOUND, detail= "Not found id to update!")
  eLse:
    my_costs[input_id]"desc"] = thing
    my_costs[input_id]["amount"] = cost
    return my_costs[input_id]

@app.post("/home")
def create_new_costs(thing:str| None =Query(defaulte"test"), cost:int | None= Query (default= 0)) :
  max_id = max(my_costs) + 1
  my_costs.update({max_id: {"desc: thing, "amount": cost}})
  return my_costs
