
from collections import defaultdict

# inicializo mi cubo semantico con valor de none o sea null
# sí no se encuentra un atributo en el diccionario le asigna el valor de none
semantic_cube = defaultdict(
    lambda: defaultdict(lambda: defaultdict(lambda: None)))

# 0 = false
# 1 = true

# OPERACIONES ARITMÉTICAS

#INT 

# semantic_cube['int']['&']['int'] = 'bool'
# semantic_cube['int']['|']['int'] = 'bool'
semantic_cube['int']['>']['int'] = 'bool'
semantic_cube['int']['<']['int'] = 'bool'
semantic_cube['int']['>=']['int'] = 'bool'
semantic_cube['int']['<=']['int'] = 'bool'
semantic_cube['int']['==']['int'] = 'bool'
semantic_cube['int']['!=']['int'] = 'bool'
semantic_cube['int']['+']['int'] = 'int'
semantic_cube['int']['-']['int'] = 'int'
semantic_cube['int']['*']['int'] = 'int'
semantic_cube['int']['/']['int'] = 'int'
semantic_cube['int']['=']['int'] = 'int'

# FLOAT

# semantic_cube['float']['&']['float'] = 'bool'
# semantic_cube['float']['|']['float'] = 'bool'
semantic_cube['float']['>']['float'] = 'bool'
semantic_cube['float']['<']['float'] = 'bool'
semantic_cube['float']['>=']['float'] = 'bool'
semantic_cube['float']['<=']['float'] = 'bool'
semantic_cube['float']['==']['float'] = 'bool'
semantic_cube['float']['!=']['float'] = 'bool'
semantic_cube['float']['+']['float'] = 'float'
semantic_cube['float']['-']['float'] = 'float'
semantic_cube['float']['*']['float'] = 'float'
semantic_cube['float']['/']['float'] = 'float'
semantic_cube['float']['=']['float'] = 'float'

# CHAR

# semantic_cube['char']['&']['char'] = 'bool'
# semantic_cube['char']['|']['char'] = 'bool'
semantic_cube['char']['>']['char'] = 'bool'
semantic_cube['char']['<']['char'] = 'bool'
semantic_cube['char']['>=']['char'] = 'bool'
semantic_cube['char']['<=']['char'] = 'bool'
semantic_cube['char']['==']['char'] = 'bool'
semantic_cube['char']['!=']['char'] = 'bool'
semantic_cube['char']['+']['char'] = 'char'
# semantic_cube['char']['-']['char'] = 'char'
# semantic_cube['char']['*']['char'] = 'char'
# semantic_cube['char']['/']['char'] = 'char'
semantic_cube['char']['=']['char'] = 'char'

# BOOL

semantic_cube['bool']['&']['bool'] = 'bool'
semantic_cube['bool']['|']['bool'] = 'bool'
# semantic_cube['bool']['>']['bool'] = 'bool'
# semantic_cube['bool']['<']['bool'] = 'bool'
# semantic_cube['bool']['>=']['bool'] = 'bool'
# semantic_cube['bool']['<=']['bool'] = 'bool'
semantic_cube['bool']['==']['bool'] = 'bool'
semantic_cube['bool']['!=']['bool'] = 'bool'
# semantic_cube['bool']['+'][boolt'] = 'bool'
# semantic_cube['bool']['-']['bool'] = 'bool'
# semantic_cube['bool']['*']['bool'] = 'bool'
# semantic_cube['bool']['/']['bool'] = 'bool'
# semantic_cube['bool']['=']['bool'] = 'bool'

# INT FLOAT

# semantic_cube['int']['&']['float'] = semantic_cube['float']['&']['int'] = 'bool'
# semantic_cube['int']['|']['float'] = semantic_cube['float']['|']['int'] = 'bool'
semantic_cube['int']['>']['float'] = semantic_cube['float']['>']['int'] = 'bool'
semantic_cube['int']['<']['float'] = semantic_cube['float']['<']['int'] = 'bool'
semantic_cube['int']['>=']['float'] = semantic_cube['float']['>=']['int'] = 'bool'
semantic_cube['int']['<=']['float'] = semantic_cube['float']['<=']['int'] = 'bool'
semantic_cube['int']['==']['float'] = semantic_cube['float']['==']['int'] = 'bool'
semantic_cube['int']['!=']['float'] = semantic_cube['float']['!=']['int'] = 'bool'
semantic_cube['int']['+']['float'] = semantic_cube['float']['+']['int'] = 'float'
semantic_cube['int']['-']['float'] = semantic_cube['float']['-']['int'] = 'float'
semantic_cube['int']['*']['float'] = semantic_cube['float']['*']['int'] = 'float'
semantic_cube['int']['/']['float'] = semantic_cube['float']['/']['int'] = 'float'
# semantic_cube['int']['=']['float'] = 'int'
# semantic_cube['float']['=']['int'] = 'float'

# INT CHAR

# semantic_cube['int']['&']['char'] = semantic_cube['char']['&']['int'] = 'bool'
# semantic_cube['int']['|']['char'] = semantic_cube['char']['|']['int'] = 'bool'
# semantic_cube['int']['>']['char'] = semantic_cube['char']['>']['int'] = 'bool'
# semantic_cube['int']['<']['char'] = semantic_cube['char']['<']['int'] = 'bool'
# semantic_cube['int']['>=']['char'] = semantic_cube['char']['>=']['int'] = 'bool'
# semantic_cube['int']['<=']['char'] = semantic_cube['char']['<=']['int'] = 'bool'
semantic_cube['int']['==']['char'] = semantic_cube['char']['==']['int'] = 'bool'
semantic_cube['int']['!=']['char'] = semantic_cube['char']['!=']['int'] = 'bool'
# semantic_cube['int']['+']['char'] = semantic_cube['char']['+']['int'] = 'int'
# semantic_cube['int']['-']['char'] = semantic_cube['char']['-']['int'] = 'int'
# semantic_cube['int']['*']['char'] = semantic_cube['char']['*']['int'] = 'int'
# semantic_cube['int']['/']['char'] = semantic_cube['char']['/']['int'] = 'int'
# semantic_cube['int']['=']['char'] = 'int'
# semantic_cube['char']['=']['int'] = 'char'

# INT BOOL

# semantic_cube['int']['&']['bool'] = semantic_cube['bool']['&']['int'] = 'bool'
# semantic_cube['int']['|']['bool'] = semantic_cube['bool']['|']['int'] = 'bool'
# semantic_cube['int']['>']['bool'] = semantic_cube['bool']['>']['int'] = 'bool'
# semantic_cube['int']['<']['bool'] = semantic_cube['bool']['<']['int'] = 'bool'
# semantic_cube['int']['>=']['bool'] = semantic_cube['bool']['>=']['int'] = 'bool'
# semantic_cube['int']['<=']['bool'] = semantic_cube['bool']['<=']['int'] = 'bool'
semantic_cube['int']['==']['bool'] = semantic_cube['bool']['==']['int'] = 'bool'
semantic_cube['int']['!=']['bool'] = semantic_cube['bool']['!=']['int'] = 'bool'
# semantic_cube['int']['+']['bool'] = semantic_cube['bool']['+']['int'] = 'int'
# semantic_cube['int']['-']['bool'] = semantic_cube['bool']['-']['int'] = 'int'
# semantic_cube['int']['*']['bool'] = semantic_cube['bool']['*']['int'] = 'int'
# semantic_cube['int']['/']['bool'] = semantic_cube['bool']['/']['int'] = 'int'
# semantic_cube['int']['=']['bool'] = 'int'
# semantic_cube['bool']['=']['int'] = 'char'

# FLOAT CHAR

# semantic_cube['float']['&']['char'] = semantic_cube['char']['&']['float'] = 'bool'
# semantic_cube['float']['|']['char'] = semantic_cube['char']['|']['float'] = 'bool'
# semantic_cube['float']['>']['char'] = semantic_cube['char']['>']['float'] = 'bool'
# semantic_cube['float']['<']['char'] = semantic_cube['char']['<']['float'] = 'bool'
# semantic_cube['float']['>=']['char'] = semantic_cube['char']['>=']['float'] = 'bool'
# semantic_cube['float']['<=']['char'] = semantic_cube['char']['<=']['float'] = 'bool'
semantic_cube['float']['==']['char'] = semantic_cube['char']['==']['float'] = 'bool'
semantic_cube['float']['!=']['char'] = semantic_cube['char']['!=']['float'] = 'bool'
# semantic_cube['float']['+']['char'] = semantic_cube['char']['+']['float'] = 'float'
# semantic_cube['float']['-']['char'] = semantic_cube['char']['-']['float'] = 'float'
# semantic_cube['float']['*']['char'] = semantic_cube['char']['*']['float'] = 'float'
# semantic_cube['float']['/']['char'] = semantic_cube['char']['/']['float'] = 'float'
# semantic_cube['float']['=']['char'] = 'float'
# semantic_cube['char']['=']['float'] = 'char'

# FLOAT BOOL

# semantic_cube['float']['&']['bool'] = semantic_cube['bool']['&']['float'] = 'bool'
# semantic_cube['float']['|']['bool'] = semantic_cube['bool']['|']['float'] = 'bool'
# semantic_cube['float']['>']['bool'] = semantic_cube['bool']['>']['float'] = 'bool'
# semantic_cube['float']['<']['bool'] = semantic_cube['bool']['<']['float'] = 'bool'
# semantic_cube['float']['>=']['bool'] = semantic_cube['bool']['>=']['float'] = 'bool'
# semantic_cube['float']['<=']['bool'] = semantic_cube['bool']['<=']['float'] = 'bool'
semantic_cube['float']['==']['bool'] = semantic_cube['bool']['==']['float'] = 'bool'
semantic_cube['float']['!=']['bool'] = semantic_cube['bool']['!=']['float'] = 'bool'
# semantic_cube['float']['+']['bool'] = semantic_cube['bool']['+']['float'] = 'float'
# semantic_cube['float']['-']['bool'] = semantic_cube['bool']['-']['float'] = 'float'
# semantic_cube['float']['*']['bool'] = semantic_cube['bool']['*']['float'] = 'float'
# semantic_cube['float']['/']['bool'] = semantic_cube['bool']['/']['float'] = 'float'
# semantic_cube['float']['=']['bool'] = 'float'
# semantic_cube['bool']['=']['float'] = 'char'

# CHAR BOOL

# semantic_cube['char']['&']['bool'] = semantic_cube['bool']['&']['char'] = 'bool'
# semantic_cube['char']['|']['bool'] = semantic_cube['bool']['|']['char'] = 'bool'
# semantic_cube['char']['>']['bool'] = semantic_cube['bool']['>']['char'] = 'bool'
# semantic_cube['char']['<']['bool'] = semantic_cube['bool']['<']['char'] = 'bool'
# semantic_cube['char']['>=']['bool'] = semantic_cube['bool']['>=']['char'] = 'bool'
# semantic_cube['char']['<=']['bool'] = semantic_cube['bool']['<=']['char'] = 'bool'
semantic_cube['char']['==']['bool'] = semantic_cube['bool']['==']['char'] = 'bool'
semantic_cube['char']['!=']['bool'] = semantic_cube['bool']['!=']['char'] = 'bool'
# semantic_cube['char']['+']['bool'] = semantic_cube['bool']['+']['char'] = 'char'
# semantic_cube['char']['-']['bool'] = semantic_cube['bool']['-']['char'] = 'char'
# semantic_cube['char']['*']['bool'] = semantic_cube['bool']['*']['char'] = 'char'
# semantic_cube['char']['/']['bool'] = semantic_cube['bool']['/']['char'] = 'char'
# semantic_cube['char']['=']['bool'] = 'char'
# semantic_cube['bool']['=']['char'] = 'char'


# print(semantic_cube)
