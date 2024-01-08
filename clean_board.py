""""get all the elements and delete them. NOW IS NOT WORKING PROPERLY   """
from utils import delete_element,get_all_elements
from config import PATH_SAVE_MAP
import json
from tqdm import tqdm

elemets=get_all_elements().json()["data"]

#cycle all elements and delete
for element in tqdm(elemets):
    delete_element(element["id"])