import urllib2
import json
import distance

LOC_URL = "http://maps.googleapis.com/maps/api/geocode/json?address="

def locate(begin1, begin2, end1, end2):
        begina = LOC_URL + begin1 + "&sensor=true"
        beginb = LOC_URL + begin2 + "&sensor=true"
        enda = LOC_URL + end1 + "&sensor=true"
        endb = LOC_URL + end2 + "&sensor=true"
        
        begina = begina.replace(" ", "+")
        beginb = beginb.replace(" ", "+")
        enda = enda.replace(" ", "+")
        endb = endb.replace(" ", "+")
        
        begina = urllib2.urlopen(begina)
        beginb = urllib2.urlopen(beginb)
        enda = urllib2.urlopen(enda)
        endb = urllib2.urlopen(endb) 
        
        begina = json.loads(str(begina.read()))
        beginb = json.loads(str(beginb.read()))
        enda = json.loads(str(enda.read()))
        endb = json.loads(str(endb.read()))
           
           
        try:
                begina_lat = begina['results'][0]['geometry']['bounds']['northeast']['lat']
                begina_lng = begina['results'][0]['geometry']['bounds']['northeast']['lng']
                
                beginb_lat = beginb['results'][0]['geometry']['bounds']['northeast']['lat']
                beginb_lng = beginb['results'][0]['geometry']['bounds']['northeast']['lng']
                
                enda_lat = enda['results'][0]['geometry']['bounds']['northeast']['lat']
                enda_lng = enda['results'][0]['geometry']['bounds']['northeast']['lng']
                
                endb_lat = endb['results'][0]['geometry']['bounds']['northeast']['lat']
                endb_lng = endb['results'][0]['geometry']['bounds']['northeast']['lng']
                
        except KeyError:
            
                begina_lat = begina['results'][0]['geometry']['viewport']['northeast']['lat']
                begina_lng = begina['results'][0]['geometry']['viewport']['northeast']['lng']
                
                beginb_lat = beginb['results'][0]['geometry']['viewport']['northeast']['lat']
                beginb_lng = beginb['results'][0]['geometry']['viewport']['northeast']['lng']
                
                enda_lat = enda['results'][0]['geometry']['viewport']['northeast']['lat']
                enda_lng = enda['results'][0]['geometry']['viewport']['northeast']['lng']
                
                endb_lat = endb['results'][0]['geometry']['viewport']['northeast']['lat']
                endb_lng = endb['results'][0]['geometry']['viewport']['northeast']['lng']
           
           
        begina_lat, begina_lng, beginb_lat, beginb_lng, enda_lat, enda_lng, endb_lat, endb_lng
    
        starta = begina_lat, begina_lng
        startb = beginb_lat, beginb_lng
        enda = enda_lat, enda_lng
        endb = endb_lat, endb_lng
        
        values = {begin1: starta,
                  begin2: startb,
                  end1: enda,
                  end2: endb}
        
        return values
        
        #print "Beginning Latitude Person A:", begina_lat, "Beginning Longitude Person A:", begina_lng
        #print "Beginning Latitude Person B:", beginb_lat, "Beginning Longitude Person B:", beginb_lng
        #print "Ending Latitude Person A:", enda_lat, "Ending Longitude Person A:", enda_lng
        #print "Ending Latitude Person B:", endb_lat, "Ending Longitude Person B:", endb_lng
        
   
    
