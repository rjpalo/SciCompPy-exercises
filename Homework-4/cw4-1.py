#cw 4-1

point_list = [(1,1), (0,1), (-1,0), (2,3), (-0.5,-8), (-0.6,-0.8), (0,-1)]
print('Points checked: {}'.format(point_list))

#(a) a test if p is in unit circle,

in_circle = list(filter((lambda p: p[0]*p[0] + p[1]*p[1] == 1), point_list))
#tylko pkty na okręgu
print('List of points in unit circle: {}'.format(in_circle))


#(b) a test if the coordinates of p are positive,

positive = list(filter((lambda p: p[0] > 0 and p[1] > 0), point_list))
#strictly positive, i.e. zeros don't count
print('List of points with two positive coordinates: {}'.format(positive))

    
#(c) a sorting key (y decreasing, x increasing),

point_list.sort(key=lambda p: (-p[1], p[0]))
#y decr., for same y incr. x
print('Points sorted by decreasing y coord.: {}'.format(point_list))


#(d) a sorting key (the sum |x|+|y|).

point_list.sort(key=lambda p: (abs(p[0] + abs(p[1]))))
print('Points sorted by incr. (|x| + |y|) value: {}'.format(point_list))

#eof
