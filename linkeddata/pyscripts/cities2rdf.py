from rdflib import Graph,URIRef, Literal
import json
import os
from shapely.geometry import shape

datans="http://atlantgis.squirrel.link/data/"
ontns="http://atlantgis.squirrel.link/ontology#"


def parseGeoJSONCities(folder,foldername,g):
    print("Parsing "+str(foldername))
    f = open (folder+"/"+foldername+" "+foldername+"_Buildings.GeoJSON", "r")
    # Reading from file
    buildings = json.loads(f.read())
    f = open (folder+"/"+foldername+" "+foldername+"_Buildings_LS.GeoJSON", "r")
    # Reading from file
    building_lines = json.loads(f.read())
    f = open (folder+"/"+foldername+" "+foldername+"_City_Area.GeoJSON", "r")
    # Reading from file
    city_area = json.loads(f.read())
    f = open (folder+"/"+foldername+" "+foldername+"_City_Map.GeoJSON", "r")
    # Reading from file
    city_map = json.loads(f.read())
    f = open (folder+"/"+foldername+" "+foldername+"_Greens.GeoJSON", "r")
    # Reading from file
    greens = json.loads(f.read())
    f = open (folder+"/"+foldername+" "+foldername+"_Squares.GeoJSON", "r")
    # Reading from file
    squares = json.loads(f.read())
    f = open (folder+"/"+foldername+" "+foldername+"_Streets.GeoJSON", "r")
    # Reading from file
    streets = json.loads(f.read())
    f = open (folder+"/"+foldername+" "+foldername+"_Walls.GeoJSON", "r")
    # Reading from file
    walls = json.loads(f.read())
    f = open (folder+"/"+foldername+" "+foldername+"_Walls_Area.GeoJSON", "r")
    # Reading from file
    walls_area = json.loads(f.read())
    g.add((URIRef(datans+foldername+"_city"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef(ontns+"City")))
    g.add((URIRef("http://www.opengis.net/ont/geosparql#hasGeometry"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.w3.org/2002/07/owl#ObjectProperty")))
    g.add((URIRef(ontns+"hasBuilding"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.w3.org/2002/07/owl#ObjectProperty")))
    g.add((URIRef("http://www.opengis.net/ont/geosparql#asWKT"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.w3.org/2002/07/owl#DatatypeProperty")))
    g.add((URIRef(datans+foldername+"_city"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal(foldername,lang="en")))
    featcounter=1
    for build in buildings["features"]:
        g.add((URIRef(datans+foldername+"_city"),URIRef(ontns+"hasBuilding"),URIRef(datans+foldername+"_city_building"+str(featcounter))))
        g.add((URIRef(datans+foldername+"_city_building"+str(featcounter)),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef(ontns+"Building")))
        g.add((URIRef(datans+foldername+"_city_building"+str(featcounter)),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Building "+str(featcounter)+" of AtlantGIS City "+str(foldername),lang="en")))
        g.add((URIRef(datans+foldername+"_city_building"+str(featcounter)),URIRef("http://www.opengis.net/ont/geosparql#hasGeometry"),URIRef(datans+foldername+"_city_building"+str(featcounter)+"_geom")))
        g.add((URIRef(datans+foldername+"_city_building"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.opengis.net/ont/sf#Polygon")))
        g.add((URIRef(datans+foldername+"_city_building"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Building footprint of building "+str(featcounter)+" of AtlantGIS City "+str(foldername),lang="en")))
        wktgeom = shape(build["geometry"])
        g.add((URIRef(datans+foldername+"_city_building"+str(featcounter)+"_geom"),URIRef("http://www.opengis.net/ont/geosparql#asWKT"),Literal("<http://www.opengis.net/def/crs/EPSG/0/4326> "+str(wktgeom),datatype="http://www.opengis.net/ont/geosparql#wktLiteral")))    
        featcounter+=1
    featcounter=1
    for sqa in squares:
        g.add((URIRef(datans+foldername+"_city"),URIRef(ontns+"hasSquare"),URIRef(datans+foldername+"_city_square"+str(featcounter))))
        g.add((URIRef(datans+foldername+"_city_square"+str(featcounter)),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef(ontns+"Square")))
        g.add((URIRef(datans+foldername+"_city_square"+str(featcounter)),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Square "+str(featcounter)+" of AtlantGIS City "+str(foldername),lang="en")))
        g.add((URIRef(datans+foldername+"_city_square"+str(featcounter)),URIRef("http://www.opengis.net/ont/geosparql#hasGeometry"), URIRef(datans+foldername+"_city_square"+str(featcounter)+"_geom")))
        wktgeom = shape(build["geometry"])
        g.add((URIRef(datans+foldername+"_city_square"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.opengis.net/ont/sf#Polygon")))
        g.add((URIRef(datans+foldername+"_city_square"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Area of square "+str(featcounter)+" of AtlantGIS City "+str(foldername),lang="en")))
        g.add((URIRef(datans+foldername+"_city_square"+str(featcounter)+"_geom"),URIRef("http://www.opengis.net/ont/geosparql#asWKT"),Literal(wktgeom,datatype="http://www.opengis.net/ont/geosparql#wktLiteral")))
        featcounter+=1
    featcounter=1
    for sqa in greens:
        g.add((URIRef(datans+foldername+"_city"),URIRef(ontns+"hasGreen"),URIRef(datans+foldername+"_city_green"+str(featcounter))))
        g.add((URIRef(datans+foldername+"_city_green"+str(featcounter)),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef(ontns+"Green")))
        g.add((URIRef(datans+foldername+"_city_green"+str(featcounter)),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Green "+str(featcounter)+" of AtlantGIS City "+str(foldername),lang="en")))
        g.add((URIRef(datans+foldername+"_city_green"+str(featcounter)),URIRef("http://www.opengis.net/ont/geosparql#hasGeometry"), URIRef(datans+foldername+"_city_green"+str(featcounter)+"_geom")))
        wktgeom = shape(build["geometry"])
        g.add((URIRef(datans+foldername+"_city_green"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.opengis.net/ont/sf#Polygon")))
        g.add((URIRef(datans+foldername+"_city_green"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Area of green "+str(featcounter)+" of AtlantGIS City "+str(foldername),lang="en")))
        g.add((URIRef(datans+foldername+"_city_green"+str(featcounter)+"_geom"),URIRef("http://www.opengis.net/ont/geosparql#asWKT"),Literal(wktgeom,datatype="http://www.opengis.net/ont/geosparql#wktLiteral")))
        featcounter+=1
    featcounter=1
    for sqa in greens:
        g.add((URIRef(datans+foldername+"_city"),URIRef(ontns+"hasGreen"),URIRef(datans+foldername+"_city_green"+str(featcounter))))
        g.add((URIRef(datans+foldername+"_city_green"+str(featcounter)),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef(ontns+"Green")))
        g.add((URIRef(datans+foldername+"_city_green"+str(featcounter)),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Green "+str(featcounter)+" of AtlantGIS City "+str(foldername),lang="en")))
        g.add((URIRef(datans+foldername+"_city_green"+str(featcounter)),URIRef("http://www.opengis.net/ont/geosparql#hasGeometry"), URIRef(datans+foldername+"_city_green"+str(featcounter)+"_geom")))
        wktgeom = shape(build["geometry"])
        g.add((URIRef(datans+foldername+"_city_green"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.opengis.net/ont/sf#Polygon")))
        g.add((URIRef(datans+foldername+"_city_green"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Area of green "+str(featcounter)+" of AtlantGIS City "+str(foldername),lang="en")))
        g.add((URIRef(datans+foldername+"_city_green"+str(featcounter)+"_geom"),URIRef("http://www.opengis.net/ont/geosparql#asWKT"),Literal(wktgeom,datatype="http://www.opengis.net/ont/geosparql#wktLiteral")))
        featcounter+=1
    g.add((URIRef(datans+foldername+"_city_wall"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef(ontns+"CityWall")))
    g.add((URIRef(datans+foldername+"_city_wall"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("City Wall of AtlantGIS City "+str(foldername),lang="en")))
    g.add((URIRef(datans+foldername+"_city_wall"),URIRef("http://www.opengis.net/ont/geosparql#hasGeometry"),URIRef(datans+foldername+"_city_wall_area")))
    g.add((URIRef(datans+foldername+"_city_wall_area"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("City Wall Area of AtlantGIS City "+str(foldername))))
    wktgeom = shape(walls_area["features"][0]["geometry"])
    g.add((URIRef(datans+foldername+"_city_wall_area"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.opengis.net/ont/sf#Polygon")))
    g.add((URIRef(datans+foldername+"_city_wall_area"),URIRef("http://www.opengis.net/ont/geosparql#asWKT"),Literal(wktgeom,datatype="http://www.opengis.net/ont/geosparql#wktLiteral")))
    g.add((URIRef(datans+foldername+"_city_wall"),URIRef("http://www.opengis.net/ont/geosparql#hasGeometry"),URIRef(datans+foldername+"_city_wall_border")))
    g.add((URIRef(datans+foldername+"_city_wall_border"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.opengis.net/ont/sf#LineString")))
    g.add((URIRef(datans+foldername+"_city_wall_border"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("City Wall Border of AtlantGIS City "+str(foldername))))
    wktgeom = shape(walls["features"][0]["geometry"])
    g.add((URIRef(datans+foldername+"_city_wall_border"),URIRef("http://www.opengis.net/ont/geosparql#asWKT"),Literal(wktgeom,datatype="http://www.opengis.net/ont/geosparql#wktLiteral")))
    
 
g=Graph()
subdirs=[x[0] for x in os.walk("../../atlantgis_cities/vector/geojson/")]
print(subdirs)
for subdir in subdirs:
    if subdir!="" and subdir!="../../atlantgis_cities/vector/geojson/":
        parseGeoJSONCities(subdir,subdir[subdir.rfind("/")+1:],g)
g.serialize("out.ttl")
    

