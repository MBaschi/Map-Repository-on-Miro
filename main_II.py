""""The scoper of the project is to automaticly draw in Miro a board with the Map of another project, 
This second version also draw classes inside a python folder"""
import math
import requests
import os
from utils import create_widget_in_miro_board, get_top_level_class_names_from_file
import json
from config import BOARD_ID, BOARD_URL, API_TOKEN, PATH_FOLDER_TO_MAP, PATH_SAVE_MAP
import inspect
import sys


INITIAL_CORNER_POSITION = [0,0] #position of the bottom left corner of a rectangle: will be modified for each rectangle tha have to bhe drawn
INITIAL_SIZES = 1000000 #size of the rectangle: will be modified for each rectangle tha have to bhe drawn
BORDER_PERCENTAGE=0.05 #percentage of the border of the rectangle

map={ #map of the board: it will be saved in a json file
    "type": [],
    "name": [],
    "position": [],
    "size": [],
    "parent_widget_id": [],
    "id": []
} 


def draw_map(path,corner_position,size, parent_widget_id=None,type="folder"):
    elements_name=[]
    if type=="folder": 
        elements_name=os.listdir(path)
    if type=="file" and path.endswith(".py"): 
        elements_name = get_top_level_class_names_from_file(path)
    
    elements_name = sorted(elements_name)    #order elemets by name
    num_elements = len(elements_name)

    #Geometry of the object
    if num_elements==0: return #if the folder is empty we don't draw anything
    num_col = math.ceil(math.sqrt(num_elements)) 
    distance_from_element = size*BORDER_PERCENTAGE#distance that element keep from the border
    size_element = size/(num_col)-2*distance_from_element  # size of each sub element
    
    if size_element<100: #if the size of the element is too small we draw an error message in red on the board          
        widget = create_widget_in_miro_board(
                    element_type="error", 
                    position=[corner_position[0]+distance_from_element,corner_position[1]+distance_from_element], 
                    size=size*0.8,
                    name=f"Can't draw {num_elements} elements -> the resulting size is too small if needed insert manually",
                    parent_widget_id=parent_widget_id
                    ) #if the size of the element is too small we don't draw anything
        return 
    
    #Positions of the elements
    positions=[] #list of the positions of the elements corner
    col_position=0 #keep track of the column we are drwaing 
    row_number=0 #keep track of the row we are drwaing
    for i in range(num_elements): #create a list of the positions of the elements corner
        positions.append([
            corner_position[0]+distance_from_element+col_position*(distance_from_element+size_element), #x coordinates
            corner_position[1]-distance_from_element-row_number*(distance_from_element+size_element) #y coordinates
             ]) #it start to daw from the top left and go to the rigth: i know that it's a mess to imagine with a bit of patience paper and pecil you can understand it
        
        col_position+=1
        if col_position==num_col: #if we are at the end of the row
            col_position=0 #we go to the next row
            row_number+=1
 
    #Drawing of the elements
    i=0
    for element in elements_name: #for each element in the folder 
        print(f"Drawing {element}")  
        if type=="folder": #if we are watchuing inside a folder we divide into files and folders
            element_path = os.path.join(path, element) #create the path of the element
            element_type = "folder" if os.path.isdir(element_path) else "file" #check if the element is a folder or a file
        if type=="file": element_type = "class" #if we are watching inside a file we draw the classes inside it
       
        widget = create_widget_in_miro_board(
                    element_type=element_type, 
                    position=positions[i], 
                    size=size_element,
                    name=element, 
                    parent_widget_id=parent_widget_id
                    ) #create the widget in miro
        

        #save the data of the element in the map
        map["type"].append(element_type)
        map["name"].append(element)
        map["position"].append(positions[i])
        map["size"].append(size_element)
        map["parent_widget_id"].append(parent_widget_id)
        map["id"].append(widget["id"])
        
        if element_type != "class": #if elemet is not a class we draw the map of it
            draw_map(path=element_path,corner_position=positions[i],size=size_element,parent_widget_id=widget["id"],type=element_type) #draw the map of the folder 

        i+=1

draw_map(path=PATH_FOLDER_TO_MAP,corner_position=INITIAL_CORNER_POSITION,size=INITIAL_SIZES,type="folder")

#save the map in a json file
with open(PATH_SAVE_MAP, "w") as f:
    json.dump(map, f, indent=4)

print("done")
