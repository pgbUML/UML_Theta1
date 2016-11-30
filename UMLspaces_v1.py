# We're parsing the UML space inventory to build a user interface where we can
# choose: Campus, Building, Floor, Room
# each element filters down the list of all rooms
import csv
from pprint import pprint

def initUMLspaces(campuses, campBldgs,bFlrs, rooms):
    # list of our 4 campuses
    #campuses = []
    # Dictionary of all buildings, with campus keys
    #campBldgs = {}
    # Dictionary of floors; buildings are the keys
    #bFlrs = {}
    # Dictionary of roooms, 'BLDGID'-'FLOOR' is the key
    #rooms = {}
     
    with open("UMLspaces.csv",'rb') as csvfile:
        UMLsp = csv.DictReader(csvfile, delimiter=',')
        for row in UMLsp:
            # Simple: build list of campuses
            if row['BUILDING_CAMPUS'] not in campuses:
                campuses.append(row['BUILDING_CAMPUS'])
                
            # Build dictionary of buildings, campus keys
            if row['BUILDING_CAMPUS'] not in campBldgs.keys():
                campBldgs[row['BUILDING_CAMPUS']] = []
                campBldgs[row['BUILDING_CAMPUS']].append(row['BUILDING_UML_ID'])
            elif row['BUILDING_UML_ID'] not in campBldgs[row['BUILDING_CAMPUS']]:
                campBldgs[row['BUILDING_CAMPUS']].append(row['BUILDING_UML_ID'])

            # Build dictionary of floors, buildings as keys
            if row['BUILDING_UML_ID'] not in bFlrs.keys():
                bFlrs[row['BUILDING_UML_ID']] = []
                bFlrs[row['BUILDING_UML_ID']].append(row[str('FLOOR')])
            elif row[str('FLOOR')] not in bFlrs[row['BUILDING_UML_ID']]:
               bFlrs[row['BUILDING_UML_ID']].append(row[str('FLOOR')])
               
            #BUILDING_FLOOR
            if row['BUILDING_FLOOR'] not in rooms.keys():
                rooms[row['BUILDING_FLOOR']] = []
                rooms[row['BUILDING_FLOOR']].append(row[str('ROOM')])
            elif row[str('ROOM')] not in rooms[row['BUILDING_FLOOR']]:
               rooms[row['BUILDING_FLOOR']].append(row[str('ROOM')])
           

    #print campuses
    #print campBldgs
    #for f in bFlrs.keys():
    #    print ">>>:",f,bFlrs[f]
    #for r in rooms.keys():
     #   print ">>>:",r,rooms[r]
