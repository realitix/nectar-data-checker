#!/usr/bin/env python3
from os import listdir
from os.path import join
import json

PATH = "../nectar-data"


def main():
    entities = {
        "measures": {},
        "states": {},
        "utensils": {},
        "tags": {},
        "aliments": {},
        "receipes": {},
        "meals": {}
    }

    # Load all json
    for a in entities.keys():
        for uuid in listdir(join(PATH, a)):
            with open(join(PATH, a, uuid)) as json_file:
                try:
                    entities[a][uuid] = json.load(json_file)
                except:
                    print("Error in file " + join(PATH, a, uuid))
                    raise
    
    # Check aliment foreign keys
    for k, v in entities['aliments'].items():
        # tags
        for tag_uuid in v['tags']:
            if tag_uuid not in entities['tags']:
                print(f"Tag {tag_uuid} not existent. Error in aliment: {k}")
        
        # states
        for state_uuid, state_value in v['states'].items():
            if state_uuid not in entities['states']:
                print(f"State {state_uuid} not existent. Error in aliment: {k}")
                for measure_uuid in state_value['measures']:
                    print(f"Measure {measure_uuid} not existent. Error in aliment: {k}")


    # Check receipe foreign keys
    for k, v in entities['receipes'].items():
        # tags
        for tag_uuid in v['tags']:
            if tag_uuid not in entities['tags']:
                print(f"Tag {tag_uuid} not existent. Error in receipe: {k}")
        
        # utensils
        for utensil_uuid in v['utensils']:
            if utensil_uuid not in entities['utensils']:
                print(f"Utensils {utensils_uuid} not existent. Error in receipe: {k}")

        # steps
        for step in v['steps']:
            for aliment_uuid in step['aliments']:
                print(f"Aliment {aliment_uuid} not existent. Error in receipe: {k}")
            
            for receipe_uuid in step['receipes']:
                print(f"Receipe {receipe_uuid} not existent. Error in receipe: {k}")




if __name__ == "__main__":
    main()
