import Location
import distance

def main(a, b, c, d):
    values = Location.locate(a, b, c, d)
    first = distance.haversine(values[a], values[c])
    second = distance.haversine(values[b], values[d])
    print "The distance from", a, "to", c, "is", first, "miles"
    print "The distance from", b, "to", d, "is", second, "miles"
    