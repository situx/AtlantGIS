var tree={
  "plugins": [
    "defaults",
    "search",
    "sort",
    "state",
    "types",
    "contextmenu"
  ],
  "search": {
    "show_only_matches": true
  },
  "types": {
    "class": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/class.png"
    },
    "geoclass": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/geoclass.png"
    },
    "halfgeoclass": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/halfgeoclass.png"
    },
    "collectionclass": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/collectionclass.png"
    },
    "geocollection": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/geometrycollection.png"
    },
    "featurecollection": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/featurecollection.png"
    },
    "instance": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/instance.png"
    },
    "geoinstance": {
      "icon": "https://cdn.jsdelivr.net/gh/i3mainz/geopubby@master/public/icons/geoinstance.png"
    }
  },
  "core": {
    "themes": {
      "responsive": true
    },
    "check_callback": true,
    "data": [
      {
        "id": "http://atlantgis.squirrel.link/ontology#ArchaeologicalSite",
        "parent": "http://atlantgis.squirrel.link/ontology#Site",
        "type": "instance",
        "text": "ArchaeologicalSite (:ArchaeologicalSite)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Site",
        "parent": "http://www.opengis.net/ont/geosparql#Feature",
        "type": "instance",
        "text": "Site (:Site)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/geosparql#Feature",
        "parent": "http://www.opengis.net/ont/geosparql#SpatialObject",
        "type": "instance",
        "text": "Feature (gsp:Feature)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Archont",
        "parent": "http://atlantgis.squirrel.link/ontology#HumanEntity",
        "type": "instance",
        "text": "Archont (:Archont)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#HumanEntity",
        "parent": "http://atlantgis.squirrel.link/ontology#AtlantGIS_Classes",
        "type": "instance",
        "text": "HumanEntity (:HumanEntity)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#AtlantGIS_Classes",
        "parent": "#",
        "type": "class",
        "text": "AtlantGIS_Classes (:AtlantGIS_Classes) [2]",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#CoastLine",
        "parent": "http://www.opengis.net/ont/geosparql#Feature",
        "type": "instance",
        "text": "CoastLine (:CoastLine)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#LandType",
        "parent": "http://www.opengis.net/ont/geosparql#Feature",
        "type": "instance",
        "text": "LandType (:LandType)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Resource",
        "parent": "http://www.opengis.net/ont/geosparql#Feature",
        "type": "instance",
        "text": "Resource (:Resource)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Site_suniv1_",
        "parent": "http://www.opengis.net/ont/geosparql#Feature",
        "type": "instance",
        "text": "Site (:Site)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Stream",
        "parent": "http://www.opengis.net/ont/geosparql#Feature",
        "type": "instance",
        "text": "Stream (:Stream)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Voronoi",
        "parent": "http://www.opengis.net/ont/geosparql#Feature",
        "type": "instance",
        "text": "Voronoi (:Voronoi)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/geosparql#SpatialObject",
        "parent": "#",
        "type": "instance",
        "text": "SpatialObject (gsp:SpatialObject)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Find",
        "parent": "http://atlantgis.squirrel.link/ontology#FindingsEntity",
        "type": "instance",
        "text": "Find (:Find)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#FindingsEntity",
        "parent": "http://atlantgis.squirrel.link/ontology#AtlantGIS_Classes",
        "type": "instance",
        "text": "FindingsEntity (:FindingsEntity)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#FindingsEntity_suniv1_",
        "parent": "http://atlantgis.squirrel.link/ontology#AtlantGIS_Classes",
        "type": "instance",
        "text": "FindingsEntity (:FindingsEntity)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#HumanEntity_suniv1_",
        "parent": "http://atlantgis.squirrel.link/ontology#AtlantGIS_Classes",
        "type": "instance",
        "text": "HumanEntity (:HumanEntity)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#TemporalEntity",
        "parent": "http://atlantgis.squirrel.link/ontology#AtlantGIS_Classes",
        "type": "instance",
        "text": "TemporalEntity (:TemporalEntity)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/geosparql#SpatialObject_suniv1_",
        "parent": "http://atlantgis.squirrel.link/ontology#AtlantGIS_Classes",
        "type": "instance",
        "text": "SpatialObject (gsp:SpatialObject)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Goldkupfererz",
        "parent": "http://atlantgis.squirrel.link/ontology#Resource",
        "type": "instance",
        "text": "Goldkupfererz (:Goldkupfererz)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Silber",
        "parent": "http://atlantgis.squirrel.link/ontology#Resource",
        "type": "instance",
        "text": "Silber (:Silber)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Zinn",
        "parent": "http://atlantgis.squirrel.link/ontology#Resource",
        "type": "instance",
        "text": "Zinn (:Zinn)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Period",
        "parent": "http://atlantgis.squirrel.link/ontology#TemporalEntity",
        "type": "instance",
        "text": "Period (:Period)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#VesselType",
        "parent": "http://atlantgis.squirrel.link/ontology#Find",
        "type": "instance",
        "text": "VesselType (:VesselType)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/geosparql#Feature_suniv1_",
        "parent": "http://www.opengis.net/ont/geosparql#SpatialObject",
        "type": "instance",
        "text": "Feature (gsp:Feature)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/geosparql#Geometry",
        "parent": "http://www.opengis.net/ont/geosparql#SpatialObject",
        "type": "instance",
        "text": "Geometry (gsp:Geometry)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/sf#MultiLineString",
        "parent": "http://www.opengis.net/ont/geosparql#Geometry",
        "type": "instance",
        "text": "MultiLineString (sf:MultiLineString)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/sf#MultiPoint",
        "parent": "http://www.opengis.net/ont/geosparql#Geometry",
        "type": "instance",
        "text": "MultiPoint (sf:MultiPoint)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/sf#MultiPolygon",
        "parent": "http://www.opengis.net/ont/geosparql#Geometry",
        "type": "instance",
        "text": "MultiPolygon (sf:MultiPolygon)",
        "data": {}
      },
      {
        "id": "http://www.opengis.net/ont/sf#Point",
        "parent": "http://www.opengis.net/ont/geosparql#Geometry",
        "type": "instance",
        "text": "Point (sf:Point)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q1554231",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "instance",
        "text": "Q1554231 (wde:Q1554231)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q1701967",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "instance",
        "text": "Q1701967 (wde:Q1701967)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q17334923",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "instance",
        "text": "Q17334923 (wde:Q17334923)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q193379",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "instance",
        "text": "Q193379 (wde:Q193379)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q3001793",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "instance",
        "text": "Q3001793 (wde:Q3001793)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q355304",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "instance",
        "text": "Q355304 (wde:Q355304)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q6428674",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "instance",
        "text": "Q6428674 (wde:Q6428674)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q757267",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "instance",
        "text": "Q757267 (wde:Q757267)",
        "data": {}
      },
      {
        "id": "http://www.wikidata.org/entity/Q839954",
        "parent": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "type": "instance",
        "text": "Q839954 (wde:Q839954)",
        "data": {}
      },
      {
        "id": "http://atlantgis.squirrel.link/ontology#Wikidata_Classes",
        "parent": "#",
        "type": "class",
        "text": "Wikidata_Classes (:Wikidata_Classes) [9]",
        "data": {}
      }
    ]
  },
  "@context": {
    "@version": 1.1,
    "foaf": "http://xmlns.com/foaf/0.1/",
    "ct": "http://purl.org/vocab/classtree#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "icon": "foaf:image",
    "id": "@id",
    "parent": "rdfs:subClassOf",
    "halfgeoclass": "ct:HalfGeoClass",
    "geoclass": {
      "@type": "ct:icontype",
      "@id": "ct:GeoClass"
    },
    "collectionclass": {
      "@type": "ct:icontype",
      "@id": "ct:CollectionClass"
    },
    "featurecollectionclass": {
      "@type": "ct:icontype",
      "@id": "ct:FeatureCollectionClass"
    },
    "class": "owl:Class",
    "instance": "owl:NamedIndividual",
    "geoinstance": {
      "@type": "ct:Icontype",
      "@id": "ct:GeoNamedIndividual"
    },
    "text": "rdfs:label",
    "type": "ct:icontype",
    "types": "ct:icontypes",
    "core": {
      "@type": "ct:TreeConfig",
      "@id": "@nest"
    },
    "data": {
      "@id": "ct:treeitem",
      "@type": "ct:TreeItem"
    }
  }
}