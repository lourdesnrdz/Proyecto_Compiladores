
# inicializo mi cubo semanticso con valor de none o sea null
# sí no se encuentra un atributo en el diccionario le asigna el valor de none
semantics_cube = defaultdict(
    lambda: defaultdict(lambda: defaultdict(lambda: None)))

# 0 = false
# 1 = true

# OPERACIONES ARITMÉTICAS

#INT 

semantics_cube['int']['&']['int'] = 'bool'
semantics_cube['int']['|']['int'] = 'bool'
semantics_cube['int']['>']['int'] = 'bool'
semantics_cube['int']['<']['int'] = 'bool'
semantics_cube['int']['>=']['int'] = 'bool'
semantics_cube['int']['<=']['int'] = 'bool'
semantics_cube['int']['==']['int'] = 'bool'
semantics_cube['int']['!=']['int'] = 'bool'
semantics_cube['int']['+']['int'] = 'int'
semantics_cube['int']['-']['int'] = 'int'
semantics_cube['int']['*']['int'] = 'int'
semantics_cube['int']['/']['int'] = 'int'
semantics_cube['int']['=']['int'] = 'int'

# FLOAT

semantics_cube['float']['&']['float'] = 'bool'
semantics_cube['float']['|']['float'] = 'bool'
semantics_cube['float']['>']['float'] = 'bool'
semantics_cube['float']['<']['float'] = 'bool'
semantics_cube['float']['>=']['float'] = 'bool'
semantics_cube['float']['<=']['float'] = 'bool'
semantics_cube['float']['==']['float'] = 'bool'
semantics_cube['float']['!=']['float'] = 'bool'
semantics_cube['float']['+']['float'] = 'float'
semantics_cube['float']['-']['float'] = 'float'
semantics_cube['float']['*']['float'] = 'float'
semantics_cube['float']['/']['float'] = 'float'
semantics_cube['float']['=']['float'] = 'float'

# CHAR

semantics_cube['char']['&']['char'] = 'bool'
semantics_cube['char']['|']['char'] = 'bool'
semantics_cube['char']['>']['char'] = 'bool'
semantics_cube['char']['<']['char'] = 'bool'
semantics_cube['char']['>=']['char'] = 'bool'
semantics_cube['char']['<=']['char'] = 'bool'
semantics_cube['char']['==']['char'] = 'bool'
semantics_cube['char']['!=']['char'] = 'bool'
semantics_cube['char']['+']['char'] = 'char'
# semantics_cube['char']['-']['char'] = 'char'
# semantics_cube['char']['*']['char'] = 'char'
# semantics_cube['char']['/']['char'] = 'char'
semantics_cube['char']['=']['char'] = 'char'

# INT FLOAT

semantics_cube['int']['&']['float'] = semantics_cube['float']['&']['int'] = 'bool'
semantics_cube['int']['|']['float'] = semantics_cube['float']['|']['int'] = 'bool'
semantics_cube['int']['>']['float'] = semantics_cube['float']['>']['int'] = 'bool'
semantics_cube['int']['<']['float'] = semantics_cube['float']['<']['int'] = 'bool'
semantics_cube['int']['>=']['float'] = semantics_cube['float']['>=']['int'] = 'bool'
semantics_cube['int']['<=']['float'] = semantics_cube['float']['<=']['int'] = 'bool'
semantics_cube['int']['==']['float'] = semantics_cube['float']['==']['int'] = 'bool'
semantics_cube['int']['!=']['float'] = semantics_cube['float']['!=']['int'] = 'bool'
semantics_cube['int']['+']['float'] = semantics_cube['float']['+']['int'] = 'float'
semantics_cube['int']['-']['float'] = semantics_cube['float']['-']['int'] = 'float'
semantics_cube['int']['*']['float'] = semantics_cube['float']['*']['int'] = 'float'
semantics_cube['int']['/']['float'] = semantics_cube['float']['/']['int'] = 'float'
semantics_cube['int']['=']['float'] = 'int'
semantics_cube['float']['=']['int'] = 'float'

# INT CHAR

semantics_cube['int']['&']['char'] = semantics_cube['char']['&']['int'] = 'bool'
semantics_cube['int']['|']['char'] = semantics_cube['char']['|']['int'] = 'bool'
semantics_cube['int']['>']['char'] = semantics_cube['char']['>']['int'] = 'bool'
semantics_cube['int']['<']['char'] = semantics_cube['char']['<']['int'] = 'bool'
semantics_cube['int']['>=']['char'] = semantics_cube['char']['>=']['int'] = 'bool'
semantics_cube['int']['<=']['char'] = semantics_cube['char']['<=']['int'] = 'bool'
semantics_cube['int']['==']['char'] = semantics_cube['char']['==']['int'] = 'bool'
semantics_cube['int']['!=']['char'] = semantics_cube['char']['!=']['int'] = 'bool'
semantics_cube['int']['+']['char'] = semantics_cube['char']['+']['int'] = 'int'
semantics_cube['int']['-']['char'] = semantics_cube['char']['-']['int'] = 'int'
semantics_cube['int']['*']['char'] = semantics_cube['char']['*']['int'] = 'int'
semantics_cube['int']['/']['char'] = semantics_cube['char']['/']['int'] = 'int'
semantics_cube['int']['=']['char'] = 'int'
semantics_cube['char']['=']['int'] = 'char'

# FLOAT CHAR

semantics_cube['float']['&']['char'] = semantics_cube['char']['&']['float'] = 'bool'
semantics_cube['float']['|']['char'] = semantics_cube['char']['|']['float'] = 'bool'
semantics_cube['float']['>']['char'] = semantics_cube['char']['>']['float'] = 'bool'
semantics_cube['float']['<']['char'] = semantics_cube['char']['<']['float'] = 'bool'
semantics_cube['float']['>=']['char'] = semantics_cube['char']['>=']['float'] = 'bool'
semantics_cube['float']['<=']['char'] = semantics_cube['char']['<=']['float'] = 'bool'
semantics_cube['float']['==']['char'] = semantics_cube['char']['==']['float'] = 'bool'
semantics_cube['float']['!=']['char'] = semantics_cube['char']['!=']['float'] = 'bool'
semantics_cube['float']['+']['char'] = semantics_cube['char']['+']['float'] = 'float'
semantics_cube['float']['-']['char'] = semantics_cube['char']['-']['float'] = 'float'
semantics_cube['float']['*']['char'] = semantics_cube['char']['*']['float'] = 'float'
semantics_cube['float']['/']['char'] = semantics_cube['char']['/']['float'] = 'float'
semantics_cube['float']['=']['char'] = 'float'
semantics_cube['char']['=']['float'] = 'char'


print(semantics_cube)