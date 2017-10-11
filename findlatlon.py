import numpy as np
import math

lat = 2.927132
lng = 101.656194
E_RADIUS = 6356
ang = 0

def new_location(theta, heading, alt):

    if theta > 0:
        ang = heading + 90

    elif theta < 0:
        ang = heading + 270

    elif theta == 0:
        ang = heading

    if ang >= 360:
        ang -= 360

    dist = math.tan(abs(theta)) * alt
    
    print dist

    return displace(ang, dist)

def displace(theta, distance):
    
    theta = np.float32(theta)

    delta = np.divide(np.float32(distance), np.float32(E_RADIUS))

    theta = math.radians(theta)
    lat1 = math.radians(lat)
    lng1 = math.radians(lng)
    
    lat2 = np.arcsin( np.sin(lat1) * np.cos(delta) + np.cos(lat1) * np.sin(delta) * np.cos(theta))
    

    lng2 = lng1 + (np.arctan2( np.sin(theta) * np.sin(delta) * np.cos(lat1), np.cos(delta) - np.sin(lat1) * np.sin(lat2)))
    
    lng2 = (lng2 + 3 * np.pi) % (2 * np.pi) - np.pi

    return  math.degrees(lat2), math.degrees(lng2)

