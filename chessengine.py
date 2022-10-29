
from sys import stdin
input = lambda: stdin.readline().strip()

################################################################
####                                                        ####
####                     RULES AND SETUP                    ####
####                                                        ####
################################################################

#### PIECES

# white

K0 = ('king',0)
Q0 = ('queen',0)
R1 = ('rook',0)
R2 = ('rook',0)
B1 = ('bishop',0) # black squares
B2 = ('bishop',0) # white squares
N1 = ('kinght',0)
N2 = ('kinght',0)

Pa = ('pawn',0)
Pb = ('pawn',0)
Pc = ('pawn',0)
Pd = ('pawn',0)
Pe = ('pawn',0)
Pf = ('pawn',0)
Pg = ('pawn',0)
Ph = ('pawn',0)

# black

k0 = ('king',1)
q0 = ('queen',1)
r1 = ('rook',1)
r2 = ('rook',1)
b1 = ('bishop',1) # white squares
b2 = ('bishop',1) # black squares
n1 = ('kinght',1)
n2 = ('kinght',1)

pa = ('pawn',1)
pb = ('pawn',1)
pc = ('pawn',1)
pd = ('pawn',1)
pe = ('pawn',1)
pf = ('pawn',1)
pg = ('pawn',1)
ph = ('pawn',1)

# more pieces are to be declared if pawns are promoted, shown below

'''

    # white

    Q1 = ('queen',0)
    Q2 = ('queen',0)
    Q3 = ('queen',0)
    Q4 = ('queen',0)
    Q5 = ('queen',0)
    Q6 = ('queen',0)
    Q7 = ('queen',0)
    Q8 = ('queen',0)

    R3 = ('rook',0)
    R4 = ('rook',0)
    R5 = ('rook',0)
    R6 = ('rook',0)
    R7 = ('rook',0)
    R8 = ('rook',0)
    R9 = ('rook',0)
    R0 = ('rook',0)

    B3 = ('bishop',0)
    B4 = ('bishop',0)
    B5 = ('bishop',0)
    B6 = ('bishop',0)
    B7 = ('bishop',0)
    B8 = ('bishop',0)
    B9 = ('bishop',0)
    B0 = ('bishop',0)

    N3 = ('kinght',0)
    N4 = ('kinght',0)
    N5 = ('kinght',0)
    N6 = ('kinght',0)
    N7 = ('kinght',0)
    N8 = ('kinght',0)
    N9 = ('kinght',0)
    N0 = ('kinght',0)

    # black

    q1 = ('queen',1)
    q2 = ('queen',1)
    q3 = ('queen',1)
    q4 = ('queen',1)
    q5 = ('queen',1)
    q6 = ('queen',1)
    q7 = ('queen',1)
    q8 = ('queen',1)

    r3 = ('rook',1)
    r4 = ('rook',1)
    r5 = ('rook',1)
    r6 = ('rook',1)
    r7 = ('rook',1)
    r8 = ('rook',1)
    r9 = ('rook',1)
    r0 = ('rook',1)

    b3 = ('bishop',1)
    b4 = ('bishop',1)
    b5 = ('bishop',1)
    b6 = ('bishop',1)
    b7 = ('bishop',1)
    b8 = ('bishop',1)
    b9 = ('bishop',1)
    b0 = ('bishop',1)

    n3 = ('kinght',1)
    n4 = ('kinght',1)
    n5 = ('kinght',1)
    n6 = ('kinght',1)
    n7 = ('kinght',1)
    n8 = ('kinght',1)
    n9 = ('kinght',1)
    n0 = ('kinght',1)

'''

# below is not a piece, just a placeholder

e_ = ('',-1)

#### BORAD

currentboard = [
    [r1,n1,b1,q0,k0,b2,n2,r2], # rank 8
    [pa,pb,pc,pd,pe,pf,pg,ph], # rank 7
    [e_,e_,e_,e_,e_,e_,e_,e_], # rank 6
    [e_,e_,e_,e_,e_,e_,e_,e_], # rank 5
    [e_,e_,e_,e_,e_,e_,e_,e_], # rank 4
    [e_,e_,e_,e_,e_,e_,e_,e_], # rank 3
    [Pa,Pb,Pc,Pd,Pe,Pf,Pg,Ph], # rank 2
    [R1,N1,B1,Q0,K0,B2,N2,R2]  # rank 1
]

# FEN - board convesrion function???

castle = [
    [2,2], # white long, short
    [2,2]  # black long, short
]
# 1 if immediately possible,
# 2 if impossible because there are pieces between r and k, or check conditions, (mutable)
# 0 if impossible and immutable, or already done.

enpassant = [ # indicates if pawn from file is capturable by EP.
    [0,0,0,0,0,0,0,0], # white a to h
    [0,0,0,0,0,0,0,0]  # black a to h
]
# 1 if pawn just moved two ranks and therefore being captured by EP is possible,
# 0 if already moved or never moved.

# IMPORTANT NOTE: In the context of threefold repetition, two positions are considered different if the opportunity to {castle, perform a given en passant capture} exists in one position but not the other.

################################################################

def Solve(a):
    1

'''

################################################################

def Turn():
    
    # whoseturn = white or black
    sol = Solve(WhoseTurn)
    
    print(sol)

################################################################

if __name__ == "__main__":
    
    Turn()

'''
