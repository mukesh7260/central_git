


def boundry(A,B, C,D):
    x0,y0 = A[0],A[0]
    x1,y1 = B[0],B[1]
    x2,y2 = C[1],C[0] 
    x3,y3 = D[1],D[1]
    
    dsum = (x0*y0+ x1*y1+ x2*y2 + x3*y3)
    dsum = abs(dsum + 0.5)
    return dsum 
boundry(1,2,3,4)
