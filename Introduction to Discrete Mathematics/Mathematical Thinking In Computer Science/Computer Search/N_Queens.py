# import itertools as it

# class Coordinate:
#     """Represent the coordinate on a board"""

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def getX(self):
#         """Return the x coordinate."""
#         return self.x
    
#     def getY(self):
#         """Return the y coordinate."""
#         return self.y

#     def setX(self, x):
#         """Set the x coordinate."""
#         self.x = x

#     def setY(self, y):
#         """Set the y coordinate."""
#         self.y = y

#     def __str__(self) -> str:
#         return '<' + str(self.getX()) + ', ' +\
#                 str(self.getY()) + '>'

#     def __repr__(self) -> str:
#         return self.__str__()


# class Board:

#     def __init__(self, length, width) -> None:
#         self.length = length
#         self.width = width
#         pass

    
        


# ##### BRUTE-FORCE #####
# def is_solution(perm):
#     for (i1, i2) in it.combinations(range(len(perm)), 2):
#         if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
#             return False

#     return True

# for perm in it.permutations(range(8)):
#     if is_solution(perm):
#         print(perm)
#         exit()



# ##### BACK-TRACKING #####
# def can_be_extended_to_solution(perm):
#     i = len(perm) - 1
#     for j in range(i):
#         if i - j == abs(perm[i] - perm[j]):
#             return False
#     return True

# def extend(perm, n):
#     if len(perm) == n:
#         print(perm)
#         exit()

#     for k in range(n):
#         if k not in perm:
#             perm.append(k)

#             if can_be_extended_to_solution(perm):
#                 extend(perm, n)

#             perm.pop()

# extend(perm = [], n = 8)
