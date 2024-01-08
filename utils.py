""""
In this file are saved the functions that create the objects in the boards:
the argument needed is the object typer, the postion and the shape. then the function return the request details
in the main will be called something like:
url, headers, data = new_object(folder, position, size)
requests.post(url, headers, data)
"""

import requests
from config import BOARD_URL, API_TOKEN
import ast

headers = {
    "accept": "application/json",
    "authorization": f"Bearer {API_TOKEN}",
    "content-type": "application/json"
}

def create_widget_in_miro_board(element_type, position, size, name, parent_widget_id=None):
    #url_frame,data_frame = frame_data(position, size, parent_widget_id=parent_widget_id)
    url_frame,data_frame = frame_data(position, size, parent_widget_id=None)
    response_frame = requests.post(url_frame, headers=headers, json=data_frame)

    url_title,data_title = title_data(element_type, position, size, name, parent_widget_id=response_frame.json()["id"])
    response_title = requests.post(url_title, headers=headers, json=data_title)
    a=response_title.json()["id"]
    return response_frame.json()

def frame_data(position, size, parent_widget_id=None):
    url=BOARD_URL+"/frames"
    data = {
              "data": {
                "title": None
              },
              "position": {
                "x": float(position[0]+size/2),
                "y": float(position[1]-size/2)
              },
              "geometry": {
                "height": float(size),
                "width": float(size)
              },
              #"parent": {
              #    "id": parent_widget_id
              #  }
            }
    return url, data

def title_data(element_type, position, size, name, parent_widget_id=None):
    url=BOARD_URL+"/texts"

    #depending on the type of the element the color of the title will change
    if element_type=="folder":color="#FAC710"
    if element_type=="file":color="#E6E6E6"
    if element_type=="class":color="#0CA789"
    if element_type=="error":color="#F24726"
    
    data = {
              "data": {
                "content": name,               
              },
              "style": {
                "fillColor": color,
                "fontSize": int(size/30)
              },
              "position": {
                "x": float(position[0]+size/2+size*0.001,),
                "y": float(position[1]-size*0.97)
              },
              "geometry": {
                "width": float(size-size*0.1)
              },
           # "parent": {
            #     "id": parent_widget_id
            #  }
            }
    return url, data

def get_all_elements():
    url=BOARD_URL+"/items"
    response = requests.get(url, headers=headers)
    return response

def delete_element(id):
    url=BOARD_URL+"/items"+"/"+id
    response = requests.delete(url, headers=headers)
    return response

def get_top_level_class_names_from_file(file_path):
    with open(file_path, "r") as source_code:
        tree = ast.parse(source_code.read())
    class_names = [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
    return class_names