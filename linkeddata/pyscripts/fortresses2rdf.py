from rdflib import Graph,URIRef, Literal
import csv
import os
from shapely.geometry import shape

datans="http://atlantgis.squirrel.link/data/"
ontns="http://atlantgis.squirrel.link/ontology#"
 
g=Graph()
f = open ("../../tables/atlantgis_fortresses.csv", "r")
roads = reader = csv.DictReader(f)
featcounter=0
for rd in roads:
    g.add((URIRef(datans+"fortress"+str(featcounter)),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef(ontns+"Fortress")))
    g.add((URIRef(datans+"fortress"+str(featcounter)),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Fortress "+str(featcounter),lang="en")))
    g.add((URIRef(datans+"fortress"+str(featcounter)),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Fortress "+str(featcounter),lang="de")))
    g.add((URIRef(datans+"fortress"+str(featcounter)),URIRef("http://www.w3.org/2006/time#hasTime"),URIRef(datans+"period/"+str(rd["period"]))))
    g.add((URIRef(datans+"periods/"+str(rd["period"])),URIRef("http://www.w3.org/2006/time#after"),URIRef(datans+"period/17")))
    g.add((URIRef(datans+"fortress"+str(rd["period"])),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Time Period "+str(rd["period"]),lang="en")))
    g.add((URIRef(datans+"fortress"+str(rd["period"])),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Fortress "+str(rd["period"]),lang="de")))
    g.add((URIRef(datans+"periods/"+str(rd["period"])),URIRef("http://www.w3.org/2006/time#before"),URIRef(datans+"period/25")))
    g.add((URIRef(datans+"fortress"+str(featcounter)),URIRef("http://www.opengis.net/ont/geosparql#hasGeometry"),URIRef(datans+"fortress"+str(featcounter)+"_geom"))) 
    g.add((URIRef(datans+"fortress"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.opengis.net/ont/sf#Point")))
    g.add((URIRef(datans+"fortress"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Fortress "+str(featcounter)+" Geometry",lang="en")))
    g.add((URIRef(datans+"fortress"+str(featcounter)+"_geom"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"),Literal("Fortress "+str(featcounter)+" Geometrie",lang="de")))
    g.add((URIRef(datans+"fortress"+str(featcounter)+"_geom"),URIRef("http://www.opengis.net/ont/geosparql#asWKT"),Literal("<http://www.opengis.net/def/crs/EPSG/0/32628> "+str(rd["WKT"]),datatype="http://www.opengis.net/ont/geosparql#wktLiteral")))  
    featcounter+=1
g.add((URIRef("http://www.opengis.net/ont/sf#Point"),URIRef("http://www.w3.org/2000/01/rdf-schema#subClassOf"),URIRef("http://www.opengis.net/ont/geosparql#Geometry")))
g.add((URIRef(ontns+"Fortress"),URIRef("http://www.w3.org/2000/01/rdf-schema#subClassOf"),URIRef("http://www.opengis.net/ont/geosparql#Feature")))
g.serialize("fortresses.ttl")
    

