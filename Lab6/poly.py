# CPE 101-01
# LAB 6: Polynomial Functions
# Name: Raheel Rehmatullah
# Section: 7

#Purpose : This function takes two polynomials of degree two (lists of length three) as arguments and adds them
#list list -> list
def poly_add2(poly1, poly2):
    newPoly = []
    newPoly.append(poly1[0] + poly2[0])
    newPoly.append(poly1[1] + poly2[1])
    newPoly.append(poly1[2] + poly2[2])
    return newPoly

#print(poly_add2([0, 0, 0], [1, 1, 1]))

#Purpose : This function takes two polynomials of degree two (lists of length three) as arguments and multiplies them
#list list -> list
def poly_multiply2(poly1, poly2):
    newPoly = []
    newPoly.append(poly1[0] * poly2[0])
    newPoly.append(poly1[1] * poly2[0] + poly1[0] * poly2[1])
    newPoly.append(poly1[0] * poly2[2] + poly1[1] * poly2[1] + poly1[2] * poly2[0])
    newPoly.append(poly1[1] * poly2[2] + poly1[2] * poly2[1])
    newPoly.append(poly1[2] * poly2[2])
    return newPoly
