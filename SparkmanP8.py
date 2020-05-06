#SparkmanP7
#Programmer: Bailey Sparkman
#Email: bsparkman@cnm.edu
#Purpose: Demonstrate how to define a class
import math
class GeoPoint:
    def _init_(self): #set two attributes
        self.lat = 0.0
        self.lon = 0.0
        self.description = ''
    def SetPoint(self,lat,lon): #set values
        self.lat = lat
        self.lon = lon
    def GetPoint(self): #return tuple or list with lat and lon
        return self.lat, self.lon
    def SetDescription(self, description):#location name (ex: Abq)
        self.description = description
    def GetDescription(self):#return objects self.description attribute
        return self.description
    def GetDistance(self, lat2, lon2): #borrowed from user rockacbruno on github
        lat1 = self.lat
        lon1 = self.lon
        radius = 6371 #km
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c
        return d
def Welcome():
    print '''Welcome! Please follow the prompts to find whether
you are closest to Albuqeruqe, New Mexico or Siox Falls, South Dakota!'''
    
#MAIN
Welcome()
print
#Instantiate two points
point1 = GeoPoint()
point1.SetPoint(35.0844,106.6504) #abq
point1.SetDescription('Albuqerque, New Mexico')

point2 = GeoPoint()
point2.SetPoint (43.5473, 96.7283) #Siox Falls
point2.SetDescription('Siox Falls, South Dakota')


doanother = 'yes' #start loop
while doanother == 'yes':
    try:
        raw_input('Please enter the name of your current physical location: ') #ask user for a loaction
        lat = float(raw_input('Please enter the latitude of the location (in decimal degrees): '))
        lon = float(raw_input('Please enter the longitude of the location (in decimal degrees): '))
        print
        dist1 = point1.GetDistance(lat, lon)
        dist2 = point2.GetDistance(lat, lon)
        if dist1 > dist2: #tell user which point they are closest to
            print "You are closest to ",point2.GetDescription()," which is located at", point2.GetPoint()
        elif dist2 > dist1:
            print "You are closest to", point1.GetDescription()," which is located at", point1.GetPoint()
            print
    except ValueError:
        print 'Please enter a valid number, no letters accepted here!'
        print
    except NameError:
        print 'Please enter your current PHYSICAL location!'
        print
    doanother = raw_input("Would you like to do another? [yes/no] ")
print 'Thank you for using my program'
