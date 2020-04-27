
# inicializo mi cubo semantico con valor de none o sea null
# sí no se encuentra un atributo en el diccionario le asigna el valor de none
semantic_cube = defaultdict(
    lambda: defaultdict(lambda: defaultdict(lambda: None)))

# lógica booleana 
# 0 = false
# 1 = true

# OPERACIONES ARITMÉTICAS

#INT 

# suma
semantic_cube['int']['+']['int'] = 'int'
semantic_cube['int']['+']['float'] = 'float'
# semantic_cube['int']['+']['char'] = ''

# resta
semantic_cube['int']['-']['int'] = 'int'
semantic_cube['int']['-']['float'] = 'float'
# semantic_cube['int']['-']['char'] = ''

# multiplicación
semantic_cube['int']['*']['int'] = 'int'
semantic_cube['int']['*']['float'] = 'float'
# semantic_cube['int']['*']['char'] = ''

# division 
semantic_cube['int']['/']['int'] = 'int'
semantic_cube['int']['/']['float'] = 'float'
# semantic_cube['int']['/']['char'] = ''

#FLOAT

# suma
semantic_cube['float']['+']['int'] = 'float'
semantic_cube['float']['+']['float'] = 'float'
# semantic_cube['float']['+']['char'] = ''

# resta
semantic_cube['float']['-']['int'] = 'float'
semantic_cube['float']['-']['float'] = 'float'
# semantic_cube['float']['-']['char'] = ''

# multiplicación
semantic_cube['float']['*']['int'] = 'float'
semantic_cube['float']['*']['float'] = 'float'
# semantic_cube['float']['*']['char'] = ''

# division 
semantic_cube['float']['/']['int'] = 'float'
semantic_cube['float']['/']['float'] = 'float'
# semantic_cube['float']['/']['char'] = ''

#CHAR

# suma
# semantic_cube['char']['+']['int'] = ''
# semantic_cube['char']['+']['float'] = ''
semantic_cube['char']['+']['char'] = 'char'

# resta
# semantic_cube['char']['-']['int'] = ''
# semantic_cube['char']['-']['float'] = ''
# semantic_cube['char']['-']['char'] = ''

# multiplicación
# semantic_cube['char']['*']['int'] = ''
# semantic_cube['char']['*']['float'] = ''
# semantic_cube['char']['*']['char'] = ''

# division 
# semantic_cube['char']['/']['int'] = ''
# semantic_cube['char']['/']['float'] = ''
# semantic_cube['char']['/']['char'] = ''


# OPERACIONES CONDICIONALES

# INT

# mayorque
semantic_cube['int']['>']['int'] = 'int'
semantic_cube['int']['>']['float'] = 'int'
# semantic_cube['int']['>']['char'] = ''

# menorque
semantic_cube['int']['<']['int'] = 'int'
semantic_cube['int']['<']['float'] = 'int'
# semantic_cube['int']['<']['char'] = ''

# mayorigual
semantic_cube['int']['>=']['int'] = 'int'
semantic_cube['int']['>=']['float'] = 'int'
# semantic_cube['int']['>=']['char'] = ''

# menorigual
semantic_cube['int']['<=']['int'] = 'int'
semantic_cube['int']['<=']['float'] = 'int'
# semantic_cube['int']['<=']['char'] = ''

# igualigual
semantic_cube['int']['==']['int'] = 'int'
semantic_cube['int']['==']['float'] = 'int'
# semantic_cube['int']['==']['char'] = ''

# diferente
semantic_cube['int']['!=']['int'] = 'int'
semantic_cube['int']['!=']['float'] = 'int'
# semantic_cube['int']['!=']['char'] = ''

# FLOAT

# mayorque
semantic_cube['float']['>']['int'] = 'int'
semantic_cube['float']['>']['float'] = 'int'
# semantic_cube['float']['>']['char'] = ''

# menorque
semantic_cube['float']['<']['int'] = 'int'
semantic_cube['float']['<']['float'] = 'int'
# semantic_cube['float']['<']['char'] = ''

# mayorigual
semantic_cube['float']['>=']['int'] = 'int'
semantic_cube['float']['>=']['float'] = 'int'
# semantic_cube['float']['>=']['char'] = ''

# menorigual
semantic_cube['float']['<=']['int'] = 'int'
semantic_cube['float']['<=']['float'] = 'int'
# semantic_cube['float']['<=']['char'] = ''

# igualigual
semantic_cube['float']['==']['int'] = 'int'
semantic_cube['float']['==']['float'] = 'int'
# semantic_cube['float']['==']['char'] = ''

# diferente
semantic_cube['float']['!=']['int'] = 'int'
semantic_cube['float']['!=']['float'] = 'int'
# semantic_cube['float']['!=']['char'] = ''

# CHAR
# mayorque
# semantic_cube['char']['>']['int'] = 'int'
# semantic_cube['char']['>']['float'] = 'int'
# semantic_cube['char']['>']['char'] = 'int'

# menorque
# semantic_cube['char']['<']['int'] = 'int'
# semantic_cube['char']['<']['float'] = 'int'
# semantic_cube['char']['<']['char'] = 'int'

# mayorigual
# semantic_cube['char']['>=']['int'] = 'int'
# semantic_cube['char']['>=']['float'] = 'int'
# semantic_cube['char']['>=']['char'] = 'int'

# menorigual
# semantic_cube['char']['<=']['int'] = 'int'
# semantic_cube['char']['<=']['float'] = 'int'
# semantic_cube['char']['<=']['char'] = 'int'

# igualigual
# semantic_cube['char']['==']['int'] = 'int'
# semantic_cube['char']['==']['float'] = 'int'
semantic_cube['char']['==']['char'] = 'int'

# diferente
# semantic_cube['char']['!=']['int'] = 'int'
# semantic_cube['char']['!=']['float'] = 'int'
semantic_cube['char']['!=']['char'] = 'int'