
# inicializo mi cubo semantico con valor de none o sea null
# sí no se encuentra un atributo en el diccionario le asigna el valor de none
semantic_cube = defaultdict(
    lambda: defaultdict(lambda: defaultdict(lambda: None)))

# lógica booleana 
# 0 = false
# 1 = true

# OPERACIONES ARITMÉTICAS

#INT 

semantic_cube['int']['&']['int'] = 'bool'
semantic_cube['int']['|']['int'] = 'bool'
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

semantic_cube['float']['&']['float'] = 'bool'
semantic_cube['float']['|']['float'] = 'bool'
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

semantic_cube['char']['&']['char'] = 'bool'
semantic_cube['char']['|']['char'] = 'bool'
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

# INT FLOAT

semantic_cube['int']['&']['float'] = semantic_cube['float']['&']['int'] = 'bool'
semantic_cube['int']['|']['float'] = semantic_cube['float']['|']['int'] = 'bool'
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
semantic_cube['int']['=']['float'] = 'int'
semantic_cube['float']['=']['int'] = 'float'

# INT CHAR

semantic_cube['int']['&']['char'] = semantic_cube['char']['&']['int'] = 'bool'
semantic_cube['int']['|']['char'] = semantic_cube['char']['|']['int'] = 'bool'
semantic_cube['int']['>']['char'] = semantic_cube['char']['>']['int'] = 'bool'
semantic_cube['int']['<']['char'] = semantic_cube['char']['<']['int'] = 'bool'
semantic_cube['int']['>=']['char'] = semantic_cube['char']['>=']['int'] = 'bool'
semantic_cube['int']['<=']['char'] = semantic_cube['char']['<=']['int'] = 'bool'
semantic_cube['int']['==']['char'] = semantic_cube['char']['==']['int'] = 'bool'
semantic_cube['int']['!=']['char'] = semantic_cube['char']['!=']['int'] = 'bool'
semantic_cube['int']['+']['char'] = semantic_cube['char']['+']['int'] = 'int'
semantic_cube['int']['-']['char'] = semantic_cube['char']['-']['int'] = 'int'
semantic_cube['int']['*']['char'] = semantic_cube['char']['*']['int'] = 'int'
semantic_cube['int']['/']['char'] = semantic_cube['char']['/']['int'] = 'int'
semantic_cube['int']['=']['char'] = 'int'
semantic_cube['char']['=']['int'] = 'char'

# FLOAT CHAR

semantic_cube['float']['&']['char'] = semantic_cube['char']['&']['float'] = 'bool'
semantic_cube['float']['|']['char'] = semantic_cube['char']['|']['float'] = 'bool'
semantic_cube['float']['>']['char'] = semantic_cube['char']['>']['float'] = 'bool'
semantic_cube['float']['<']['char'] = semantic_cube['char']['<']['float'] = 'bool'
semantic_cube['float']['>=']['char'] = semantic_cube['char']['>=']['float'] = 'bool'
semantic_cube['float']['<=']['char'] = semantic_cube['char']['<=']['float'] = 'bool'
semantic_cube['float']['==']['char'] = semantic_cube['char']['==']['float'] = 'bool'
semantic_cube['float']['!=']['char'] = semantic_cube['char']['!=']['float'] = 'bool'
semantic_cube['float']['+']['char'] = semantic_cube['char']['+']['float'] = 'float'
semantic_cube['float']['-']['char'] = semantic_cube['char']['-']['float'] = 'float'
semantic_cube['float']['*']['char'] = semantic_cube['char']['*']['float'] = 'float'
semantic_cube['float']['/']['char'] = semantic_cube['char']['/']['float'] = 'float'
semantic_cube['float']['=']['char'] = 'float'
semantic_cube['char']['=']['float'] = 'char'
