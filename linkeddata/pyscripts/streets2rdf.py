from rdflib import Graph,URIRef, Literal
import json
import os
from shapely.geometry import shape

datans="http://atlantgis.squirrel.link/data/"
ontns="http://atlantgis.squirrel.link/ontology#"
 
g=Graph()
f = open ("../../atlantgis_cities/vector/geojson/intercityroads.geojson", "r")
roads = json.loads(f.read())
featcounter=0
for rd in roads["features"]:
    g.add((URIRef(datans+"intercity_road"+str(featcounter)),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef(ontns+"Road")))
    g.add((URIRef(datans+"intercity_road"+str(featcounter)),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Intercity Road "+str(featcounter)+": "+rd["properties"]["layer"],lang="en")))
    g.add((URIRef(datans+"intercity_road"+str(featcounter)),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Überlandstraße "+str(featcounter)+": "+rd["properties"]["layer"],lang="en")))
    g.add((URIRef(datans+"intercity_road"+str(featcounter)),URIRef("http://www.opengis.net/ont/geosparql#hasGeometry"),URIRef(datans+"intercity_road"+str(featcounter)+"_geom"))) 
    wktgeom = shape(rd["geometry"])
    g.add((URIRef(datans+"intercity_road"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.opengis.net/ont/sf#LineString")))
    g.add((URIRef(datans+"intercity_road"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Intercity Road "+str(featcounter)+": "+rd["properties"]["layer"]+" Geometry",lang="en")))
    g.add((URIRef(datans+"intercity_road"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Intercity Road "+str(featcounter)+": "+rd["properties"]["layer"]+" Geometrie",lang="de")))
    g.add((URIRef(datans+"intercity_road"+str(featcounter)+"_geom"),URIRef("http://www.opengis.net/ont/geosparql#asWKT"),Literal(wktgeom,datatype="http://www.opengis.net/ont/geosparql#wktLiteral")))  
    featcounter+=1
g.add((URIRef("http://www.opengis.net/ont/sf#LineString"),URIRef("http://www.w3.org/2000/01/rdf-schema#subClassOf"),URIRef("http://www.opengis.net/ont/geosparql#Geometry")))
g.add((URIRef(ontns+"Road"),URIRef("http://www.w3.org/2000/01/rdf-schema#subClassOf"),URIRef("http://www.opengis.net/ont/geosparql#Feature")))
g.serialize("streets.ttl")
    

