def parameter_recovery(p, x1, y1, x2, y2):
    """
    Recovers the a and b parameters from an elliptic curve when two points are known.
    :param p: the prime of the curve base ring
    :param x1: the x coordinate of the first point
    :param y1: the y coordinate of the first point
    :param x2: the x coordinate of the second point
    :param y2: the y coordinate of the second point
    :return: a tuple containing the a and b parameters of the elliptic curve
    """
    a = pow(x1 - x2, -1, p) * (pow(y1, 2, p) - pow(y2, 2, p) - (pow(x1, 3, p) - pow(x2, 3, p))) % p
    b = (pow(y1, 2, p) - pow(x1, 3, p) - a * x1) % p
    return int(a), int(b)


p = 4368590184733545720227961182704359358435747188309319510520316493183539079703

gx = 8742397231329873984594235438374590234800923467289367269837473862487362482
gy = 225987949353410341392975247044711665782695329311463646299187580326445253608
G = (gx, gy)
nG = (2582928974243465355371953056699793745022552378548418288211138499777818633265, 2421683573446497972507172385881793260176370025964652384676141384239699096612)

a,b = parameter_recovery(p,gx,gy,nG[0],nG[1])
print(a)
print(b)

