
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightIGUALleftORleftANDnonassocMENORQUEMAYORQUEIGUALIGUALDIFERENTEMENORIGUALMAYORIGUALleftMASMENOSleftPORDIVAND CHAR COMA CORCHETE_A CORCHETE_C CTE_CH CTE_F CTE_I CTE_STR DESDE DIFERENTE DIV ENTONCES ESCRIBIR FLOAT FUNCION HACER HASTA HAZ ID IGUAL IGUALIGUAL INT LEER LLAVE_A LLAVE_C MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MIENTRAS OR PARENT_A PARENT_C POR PRINCIPAL PROGRAMA PUNTOCOMA REGRESA SI SINO VAR VOIDprograma : PROGRAMA ID PUNTOCOMA progprog : main\n\t| dec_vars dec_funciones main\n\t| dec_vars main\n\t| dec_funciones main\n\tmain : PRINCIPAL actualiza_func_name PARENT_A PARENT_C dec_estactualiza_func_name : dec_vars : VAR vars save_varsvars : tipo_simple ids_simple PUNTOCOMA\n\t| tipo_simple ids_simple PUNTOCOMA vars\n\tsave_vars : tipo_simple : INT\n\t| FLOAT\n\t| CHAR\n\tids_simple : ID save_vars_name\n\t| ID save_vars_name dimension\n\t| ID save_vars_name COMA ids_simple\n\t| ID save_vars_name dimension COMA ids_simple\n\tsave_vars_name : dimension : CORCHETE_A CTE_I CORCHETE_Cvariable : ID r_push_id\n\t| ID r_push_id dim\n\tr_push_id : variables : variable r_generate_quad_leer\n\t| variable r_generate_quad_leer COMA variables \n\tdim : CORCHETE_A expresion CORCHETE_C\n\tdec_funciones : funcion r_generate_endfunc\n\t| funcion r_generate_endfunc dec_funciones\n\tr_generate_endfunc : funcion : FUNCION tipo_simple ID create_func_table func_dos\n\t| FUNCION VOID func_type_void ID create_func_table func_dos\n\tfunc_type_void : create_func_table : func_dos : PARENT_A PARENT_C var_funcs\n\t| PARENT_A parametros PARENT_C save_params var_funcs\n\tsave_params : var_funcs : dec_est\n\t| dec_vars dec_est\n\tparametros : tipo_simple ID save_params_list\n\t| tipo_simple ID save_params_list COMA parametros\n\tsave_params_list : dec_est : LLAVE_A LLAVE_C\n\t| LLAVE_A estatutos_dos LLAVE_C\n\testatutos : asignacion PUNTOCOMA \n\t| llamada PUNTOCOMA \n\t| retorno PUNTOCOMA \n\t| lectura PUNTOCOMA \n\t| escritura PUNTOCOMA \n\t| decision \n\t| ciclo_for \n\t| ciclo_while \n\testatutos_dos : estatutos\n\t| estatutos estatutos_dos\n\tasignacion : variable IGUAL r_push_oper expresion r_generate_quad_asigr_generate_quad_asig : llamada : ID r_check_func_exists PARENT_A r_generate_ERA PARENT_C r_generate_gosub\n\t| ID r_check_func_exists PARENT_A r_generate_ERA expresiones PARENT_C r_generate_gosub\n\tr_check_func_exists : r_generate_ERA : r_generate_gosub : expresiones : expresion r_generate_parameter\n\t| expresion r_generate_parameter COMA r_act_param_count expresion\n\tr_generate_parameter : r_act_param_count : expresion : t_expresion r_generate_quad_or\n\t| t_expresion r_generate_quad_or OR r_push_oper expresion\n\tr_generate_quad_or : t_expresion : g_expresion r_generate_quad_and\n\t| g_expresion r_generate_quad_and AND r_push_oper t_expresion\n\tr_generate_quad_and : g_expresion : m_expresion r_generate_quad_logicos\n\t| m_expresion op_logicos m_expresion r_generate_quad_logicos\n\tr_generate_quad_logicos : op_logicos : MAYORQUE r_push_oper\n\t| MENORQUE r_push_oper\n\t| MAYORIGUAL r_push_oper\n\t| MENORIGUAL r_push_oper\n\t| IGUALIGUAL r_push_oper\n\t| DIFERENTE r_push_oper\n\tm_expresion : termino r_generate_quad_masmen\n\t| termino r_generate_quad_masmen MAS r_push_oper m_expresion\n\t| termino r_generate_quad_masmen MENOS r_push_oper m_expresion\n\ttermino : factor r_generate_quad_muldiv\n\t| factor r_generate_quad_muldiv POR r_push_oper termino\n\t| factor r_generate_quad_muldiv DIV r_push_oper termino\n\tr_push_oper : r_generate_quad_masmen : r_generate_quad_muldiv :  factor : PARENT_A r_push_ff expresion PARENT_C r_pop_ff\n\t| CTE_I r_push_cte_i\n\t| CTE_F r_push_cte_f\n\t| CTE_CH r_push_cte_c\n\t| variable\n\t| act_flag_llamada llamada\n\tact_flag_llamada : r_push_cte_i : r_push_cte_f : r_push_cte_c : r_push_ff : r_pop_ff : retorno : REGRESA PARENT_A expresion PARENT_C r_generate_quad_retornor_generate_quad_retorno : lectura : LEER PARENT_A variables PARENT_Cr_generate_quad_leer : escritura : ESCRIBIR PARENT_A escr PARENT_Cescritura_dos : CTE_STR r_push_cte_str\n\t| expresion\n\tr_push_cte_str : r_generate_quad_escr : escr : escritura_dos r_generate_quad_escr\n\t| escritura_dos r_generate_quad_escr COMA escr\n\tdecision : if r_end_if \n\t| if r_goto_ifelse else r_end_ifif : SI PARENT_A expresion PARENT_C r_check_exp_type ENTONCES LLAVE_A estatutos_dos LLAVE_Cr_check_exp_type : r_end_if : r_goto_ifelse : else : SINO LLAVE_A estatutos_dos LLAVE_Cciclo_while : MIENTRAS r_save_jump PARENT_A expresion PARENT_C r_check_exp_type HAZ LLAVE_A estatutos_dos LLAVE_C r_goto_whiler_goto_while : r_save_jump : ciclo_for : DESDE ID r_save_var_for IGUAL expresion r_generate_quad_asig_for HASTA r_save_jump r_expresion_for expresion r_check_exp_for HACER LLAVE_A estatutos_dos LLAVE_C r_goto_forr_expresion_for : r_save_var_for : r_generate_quad_asig_for : r_check_exp_for : r_goto_for : '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,5,6,14,15,25,38,47,74,],[0,-1,-2,-4,-5,-3,-6,-42,-43,]),'ID':([2,18,19,20,21,23,24,32,39,42,49,55,56,57,63,64,67,72,76,77,78,79,80,81,84,85,86,87,91,99,100,102,103,114,122,125,131,133,138,139,140,141,142,143,144,157,158,159,171,172,174,175,176,177,178,179,180,181,182,183,184,185,195,196,198,199,200,201,204,209,217,219,220,221,222,225,227,229,231,233,235,236,],[3,29,-12,-13,-14,31,-32,37,59,29,59,-49,-50,-51,-116,89,29,98,-44,-45,-46,-47,-48,-86,115,115,115,-112,115,115,-59,115,-99,151,-116,115,115,115,115,-86,-86,-86,-86,-86,-86,-113,59,115,-86,-86,-74,-75,-76,-77,-78,-79,-86,-86,-86,-86,115,115,115,115,115,115,115,115,-118,-64,-121,59,115,-123,59,115,-114,-120,-119,59,-127,-122,]),'PUNTOCOMA':([3,28,29,35,41,50,51,52,53,54,68,83,92,93,101,105,106,107,108,109,110,111,112,113,115,130,134,135,136,137,145,146,147,148,149,150,152,154,164,165,168,170,173,191,192,194,197,208,210,211,212,213,214,215,216,],[4,34,-19,-15,-16,76,77,78,79,80,-17,-21,-18,-20,-22,-67,-70,-73,-87,-88,-96,-97,-98,-93,-23,-55,-102,-65,-68,-71,-80,-83,-90,-91,-92,-94,-103,-105,-54,-60,-26,-101,-73,-56,-60,-100,-72,-57,-89,-66,-69,-81,-82,-84,-85,]),'PRINCIPAL':([4,7,8,11,13,17,22,27,30,34,40,44,47,73,74,94,95,127,162,],[9,9,9,-29,9,-11,-27,-8,-28,-9,-10,-30,-42,-31,-43,-34,-37,-38,-35,]),'VAR':([4,70,97,128,],[10,10,-36,10,]),'FUNCION':([4,7,11,17,22,27,34,40,44,47,73,74,94,95,127,162,],[12,12,-29,-11,12,-8,-9,-10,-30,-42,-31,-43,-34,-37,-38,-35,]),'PARENT_A':([9,16,31,36,37,46,59,60,61,62,65,66,81,82,84,86,90,91,99,100,102,103,125,131,133,138,139,140,141,142,143,144,151,159,171,172,174,175,176,177,178,179,180,181,182,183,185,195,196,198,199,200,201,209,217,220,221,225,],[-7,26,-33,45,-33,45,-58,84,85,86,-121,91,-86,100,103,103,125,103,103,-59,103,-99,103,103,103,103,-86,-86,-86,-86,-86,-86,-58,103,-86,-86,-74,-75,-76,-77,-78,-79,-86,-86,-86,-86,103,103,103,103,103,103,103,-64,-121,103,-123,103,]),'INT':([10,12,34,45,163,],[19,19,19,19,19,]),'FLOAT':([10,12,34,45,163,],[20,20,20,20,20,]),'CHAR':([10,12,34,45,163,],[21,21,21,21,21,]),'VOID':([12,],[24,]),'LLAVE_A':([17,27,33,34,40,70,96,97,123,128,207,218,232,],[-11,-8,39,-9,-10,39,39,-36,158,39,219,222,233,]),'PARENT_C':([26,45,71,83,98,100,101,104,105,106,107,108,109,110,111,112,113,115,116,117,118,119,120,121,126,129,131,135,136,137,145,146,147,148,149,150,153,155,156,160,165,166,167,168,169,173,190,191,192,193,194,197,202,203,208,210,211,212,213,214,215,216,224,],[33,70,97,-21,-41,-59,-22,134,-67,-70,-73,-87,-88,-96,-97,-98,-93,-23,152,-104,154,-109,-108,-107,161,-39,165,-65,-68,-71,-80,-83,-90,-91,-92,-94,-24,-110,-106,188,-60,192,-63,-26,194,-73,-40,-56,-60,-61,-100,-72,-25,-111,-57,-89,-66,-69,-81,-82,-84,-85,-62,]),'COMA':([29,35,41,83,93,98,101,105,106,107,108,109,110,111,112,113,115,117,119,120,121,129,135,136,137,145,146,147,148,149,150,153,155,156,165,167,168,173,191,192,193,194,197,208,210,211,212,213,214,215,216,],[-19,42,67,-21,-20,-41,-22,-67,-70,-73,-87,-88,-96,-97,-98,-93,-23,-104,-109,-108,-107,163,-65,-68,-71,-80,-83,-90,-91,-92,-94,184,185,-106,-60,-63,-26,-73,-56,-60,209,-100,-72,-57,-89,-66,-69,-81,-82,-84,-85,]),'CORCHETE_A':([29,35,59,83,115,],[-19,43,-23,102,-23,]),'LLAVE_C':([39,48,49,55,56,57,63,75,76,77,78,79,80,87,122,157,186,204,223,226,227,229,231,234,235,236,],[47,74,-52,-49,-50,-51,-116,-53,-44,-45,-46,-47,-48,-112,-116,-113,204,-118,227,229,-114,-120,-119,235,-127,-122,]),'REGRESA':([39,49,55,56,57,63,76,77,78,79,80,87,122,157,158,204,219,222,227,229,231,233,235,236,],[60,60,-49,-50,-51,-116,-44,-45,-46,-47,-48,-112,-116,-113,60,-118,60,60,-114,-120,-119,60,-127,-122,]),'LEER':([39,49,55,56,57,63,76,77,78,79,80,87,122,157,158,204,219,222,227,229,231,233,235,236,],[61,61,-49,-50,-51,-116,-44,-45,-46,-47,-48,-112,-116,-113,61,-118,61,61,-114,-120,-119,61,-127,-122,]),'ESCRIBIR':([39,49,55,56,57,63,76,77,78,79,80,87,122,157,158,204,219,222,227,229,231,233,235,236,],[62,62,-49,-50,-51,-116,-44,-45,-46,-47,-48,-112,-116,-113,62,-118,62,62,-114,-120,-119,62,-127,-122,]),'DESDE':([39,49,55,56,57,63,76,77,78,79,80,87,122,157,158,204,219,222,227,229,231,233,235,236,],[64,64,-49,-50,-51,-116,-44,-45,-46,-47,-48,-112,-116,-113,64,-118,64,64,-114,-120,-119,64,-127,-122,]),'MIENTRAS':([39,49,55,56,57,63,76,77,78,79,80,87,122,157,158,204,219,222,227,229,231,233,235,236,],[65,65,-49,-50,-51,-116,-44,-45,-46,-47,-48,-112,-116,-113,65,-118,65,65,-114,-120,-119,65,-127,-122,]),'SI':([39,49,55,56,57,63,76,77,78,79,80,87,122,157,158,204,219,222,227,229,231,233,235,236,],[66,66,-49,-50,-51,-116,-44,-45,-46,-47,-48,-112,-116,-113,66,-118,66,66,-114,-120,-119,66,-127,-122,]),'CTE_I':([43,81,84,86,91,99,100,102,103,125,131,133,138,139,140,141,142,143,144,159,171,172,174,175,176,177,178,179,180,181,182,183,185,195,196,198,199,200,201,209,217,220,221,225,],[69,-86,110,110,110,110,-59,110,-99,110,110,110,110,-86,-86,-86,-86,-86,-86,110,-86,-86,-74,-75,-76,-77,-78,-79,-86,-86,-86,-86,110,110,110,110,110,110,110,-64,-121,110,-123,110,]),'IGUAL':([58,59,83,89,101,124,168,],[81,-23,-21,-124,-22,159,-26,]),'SINO':([63,88,227,],[-117,123,-114,]),'CORCHETE_C':([69,83,101,105,106,107,108,109,110,111,112,113,115,132,135,136,137,145,146,147,148,149,150,165,168,173,191,192,194,197,208,210,211,212,213,214,215,216,],[93,-21,-22,-67,-70,-73,-87,-88,-96,-97,-98,-93,-23,168,-65,-68,-71,-80,-83,-90,-91,-92,-94,-60,-26,-73,-56,-60,-100,-72,-57,-89,-66,-69,-81,-82,-84,-85,]),'CTE_F':([81,84,86,91,99,100,102,103,125,131,133,138,139,140,141,142,143,144,159,171,172,174,175,176,177,178,179,180,181,182,183,185,195,196,198,199,200,201,209,217,220,221,225,],[-86,111,111,111,111,-59,111,-99,111,111,111,111,-86,-86,-86,-86,-86,-86,111,-86,-86,-74,-75,-76,-77,-78,-79,-86,-86,-86,-86,111,111,111,111,111,111,111,-64,-121,111,-123,111,]),'CTE_CH':([81,84,86,91,99,100,102,103,125,131,133,138,139,140,141,142,143,144,159,171,172,174,175,176,177,178,179,180,181,182,183,185,195,196,198,199,200,201,209,217,220,221,225,],[-86,112,112,112,112,-59,112,-99,112,112,112,112,-86,-86,-86,-86,-86,-86,112,-86,-86,-74,-75,-76,-77,-78,-79,-86,-86,-86,-86,112,112,112,112,112,112,112,-64,-121,112,-123,112,]),'POR':([83,101,109,110,111,112,113,115,146,147,148,149,150,165,168,191,192,194,208,210,],[-21,-22,-88,-96,-97,-98,-93,-23,182,-90,-91,-92,-94,-60,-26,-56,-60,-100,-57,-89,]),'DIV':([83,101,109,110,111,112,113,115,146,147,148,149,150,165,168,191,192,194,208,210,],[-21,-22,-88,-96,-97,-98,-93,-23,183,-90,-91,-92,-94,-60,-26,-56,-60,-100,-57,-89,]),'MAS':([83,101,108,109,110,111,112,113,115,145,146,147,148,149,150,165,168,191,192,194,208,210,215,216,],[-21,-22,-87,-88,-96,-97,-98,-93,-23,180,-83,-90,-91,-92,-94,-60,-26,-56,-60,-100,-57,-89,-84,-85,]),'MENOS':([83,101,108,109,110,111,112,113,115,145,146,147,148,149,150,165,168,191,192,194,208,210,215,216,],[-21,-22,-87,-88,-96,-97,-98,-93,-23,181,-83,-90,-91,-92,-94,-60,-26,-56,-60,-100,-57,-89,-84,-85,]),'MAYORQUE':([83,101,107,108,109,110,111,112,113,115,145,146,147,148,149,150,165,168,191,192,194,208,210,213,214,215,216,],[-21,-22,139,-87,-88,-96,-97,-98,-93,-23,-80,-83,-90,-91,-92,-94,-60,-26,-56,-60,-100,-57,-89,-81,-82,-84,-85,]),'MENORQUE':([83,101,107,108,109,110,111,112,113,115,145,146,147,148,149,150,165,168,191,192,194,208,210,213,214,215,216,],[-21,-22,140,-87,-88,-96,-97,-98,-93,-23,-80,-83,-90,-91,-92,-94,-60,-26,-56,-60,-100,-57,-89,-81,-82,-84,-85,]),'MAYORIGUAL':([83,101,107,108,109,110,111,112,113,115,145,146,147,148,149,150,165,168,191,192,194,208,210,213,214,215,216,],[-21,-22,141,-87,-88,-96,-97,-98,-93,-23,-80,-83,-90,-91,-92,-94,-60,-26,-56,-60,-100,-57,-89,-81,-82,-84,-85,]),'MENORIGUAL':([83,101,107,108,109,110,111,112,113,115,145,146,147,148,149,150,165,168,191,192,194,208,210,213,214,215,216,],[-21,-22,142,-87,-88,-96,-97,-98,-93,-23,-80,-83,-90,-91,-92,-94,-60,-26,-56,-60,-100,-57,-89,-81,-82,-84,-85,]),'IGUALIGUAL':([83,101,107,108,109,110,111,112,113,115,145,146,147,148,149,150,165,168,191,192,194,208,210,213,214,215,216,],[-21,-22,143,-87,-88,-96,-97,-98,-93,-23,-80,-83,-90,-91,-92,-94,-60,-26,-56,-60,-100,-57,-89,-81,-82,-84,-85,]),'DIFERENTE':([83,101,107,108,109,110,111,112,113,115,145,146,147,148,149,150,165,168,191,192,194,208,210,213,214,215,216,],[-21,-22,144,-87,-88,-96,-97,-98,-93,-23,-80,-83,-90,-91,-92,-94,-60,-26,-56,-60,-100,-57,-89,-81,-82,-84,-85,]),'AND':([83,101,106,107,108,109,110,111,112,113,115,136,137,145,146,147,148,149,150,165,168,173,191,192,194,197,208,210,213,214,215,216,],[-21,-22,-70,-73,-87,-88,-96,-97,-98,-93,-23,172,-71,-80,-83,-90,-91,-92,-94,-60,-26,-73,-56,-60,-100,-72,-57,-89,-81,-82,-84,-85,]),'OR':([83,101,105,106,107,108,109,110,111,112,113,115,135,136,137,145,146,147,148,149,150,165,168,173,191,192,194,197,208,210,212,213,214,215,216,],[-21,-22,-67,-70,-73,-87,-88,-96,-97,-98,-93,-23,171,-68,-71,-80,-83,-90,-91,-92,-94,-60,-26,-73,-56,-60,-100,-72,-57,-89,-69,-81,-82,-84,-85,]),'HASTA':([83,101,105,106,107,108,109,110,111,112,113,115,135,136,137,145,146,147,148,149,150,165,168,173,187,191,192,194,197,205,208,210,211,212,213,214,215,216,],[-21,-22,-67,-70,-73,-87,-88,-96,-97,-98,-93,-23,-65,-68,-71,-80,-83,-90,-91,-92,-94,-60,-26,-73,-125,-56,-60,-100,-72,217,-57,-89,-66,-69,-81,-82,-84,-85,]),'HACER':([83,101,105,106,107,108,109,110,111,112,113,115,135,136,137,145,146,147,148,149,150,165,168,173,191,192,194,197,208,210,211,212,213,214,215,216,228,230,],[-21,-22,-67,-70,-73,-87,-88,-96,-97,-98,-93,-23,-65,-68,-71,-80,-83,-90,-91,-92,-94,-60,-26,-73,-56,-60,-100,-72,-57,-89,-66,-69,-81,-82,-84,-85,-126,232,]),'CTE_STR':([86,185,],[120,120,]),'ENTONCES':([161,189,],[-115,207,]),'HAZ':([188,206,],[-115,218,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'prog':([4,],[5,]),'main':([4,7,8,13,],[6,14,15,25,]),'dec_vars':([4,70,128,],[7,96,96,]),'dec_funciones':([4,7,22,],[8,13,30,]),'funcion':([4,7,22,],[11,11,11,]),'actualiza_func_name':([9,],[16,]),'vars':([10,34,],[17,40,]),'tipo_simple':([10,12,34,45,163,],[18,23,18,72,72,]),'r_generate_endfunc':([11,],[22,]),'save_vars':([17,],[27,]),'ids_simple':([18,42,67,],[28,68,92,]),'func_type_void':([24,],[32,]),'save_vars_name':([29,],[35,]),'create_func_table':([31,37,],[36,46,]),'dec_est':([33,70,96,128,],[38,95,127,95,]),'dimension':([35,],[41,]),'func_dos':([36,46,],[44,73,]),'estatutos_dos':([39,49,158,219,222,233,],[48,75,186,223,226,234,]),'estatutos':([39,49,158,219,222,233,],[49,49,49,49,49,49,]),'asignacion':([39,49,158,219,222,233,],[50,50,50,50,50,50,]),'llamada':([39,49,114,158,219,222,233,],[51,51,150,51,51,51,51,]),'retorno':([39,49,158,219,222,233,],[52,52,52,52,52,52,]),'lectura':([39,49,158,219,222,233,],[53,53,53,53,53,53,]),'escritura':([39,49,158,219,222,233,],[54,54,54,54,54,54,]),'decision':([39,49,158,219,222,233,],[55,55,55,55,55,55,]),'ciclo_for':([39,49,158,219,222,233,],[56,56,56,56,56,56,]),'ciclo_while':([39,49,158,219,222,233,],[57,57,57,57,57,57,]),'variable':([39,49,84,85,86,91,99,102,125,131,133,138,158,159,184,185,195,196,198,199,200,201,219,220,222,225,233,],[58,58,113,117,113,113,113,113,113,113,113,113,58,113,117,113,113,113,113,113,113,113,58,113,58,113,58,]),'if':([39,49,158,219,222,233,],[63,63,63,63,63,63,]),'parametros':([45,163,],[71,190,]),'r_check_func_exists':([59,151,],[82,82,]),'r_push_id':([59,115,],[83,83,]),'r_end_if':([63,122,],[87,157,]),'r_goto_ifelse':([63,],[88,]),'r_save_jump':([65,217,],[90,221,]),'var_funcs':([70,128,],[94,162,]),'r_push_oper':([81,139,140,141,142,143,144,171,172,180,181,182,183,],[99,174,175,176,177,178,179,195,196,198,199,200,201,]),'dim':([83,],[101,]),'expresion':([84,86,91,99,102,125,131,133,159,185,195,220,225,],[104,121,126,130,132,160,167,169,187,121,211,224,228,]),'t_expresion':([84,86,91,99,102,125,131,133,159,185,195,196,220,225,],[105,105,105,105,105,105,105,105,105,105,105,212,105,105,]),'g_expresion':([84,86,91,99,102,125,131,133,159,185,195,196,220,225,],[106,106,106,106,106,106,106,106,106,106,106,106,106,106,]),'m_expresion':([84,86,91,99,102,125,131,133,138,159,185,195,196,198,199,220,225,],[107,107,107,107,107,107,107,107,173,107,107,107,107,213,214,107,107,]),'termino':([84,86,91,99,102,125,131,133,138,159,185,195,196,198,199,200,201,220,225,],[108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,215,216,108,108,]),'factor':([84,86,91,99,102,125,131,133,138,159,185,195,196,198,199,200,201,220,225,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'act_flag_llamada':([84,86,91,99,102,125,131,133,138,159,185,195,196,198,199,200,201,220,225,],[114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,]),'variables':([85,184,],[116,202,]),'escr':([86,185,],[118,203,]),'escritura_dos':([86,185,],[119,119,]),'else':([88,],[122,]),'r_save_var_for':([89,],[124,]),'save_params':([97,],[128,]),'save_params_list':([98,],[129,]),'r_generate_ERA':([100,],[131,]),'r_push_ff':([103,],[133,]),'r_generate_quad_or':([105,],[135,]),'r_generate_quad_and':([106,],[136,]),'r_generate_quad_logicos':([107,173,],[137,197,]),'op_logicos':([107,],[138,]),'r_generate_quad_masmen':([108,],[145,]),'r_generate_quad_muldiv':([109,],[146,]),'r_push_cte_i':([110,],[147,]),'r_push_cte_f':([111,],[148,]),'r_push_cte_c':([112,],[149,]),'r_generate_quad_leer':([117,],[153,]),'r_generate_quad_escr':([119,],[155,]),'r_push_cte_str':([120,],[156,]),'r_generate_quad_asig':([130,],[164,]),'expresiones':([131,],[166,]),'r_generate_quad_retorno':([134,],[170,]),'r_check_exp_type':([161,188,],[189,206,]),'r_generate_gosub':([165,192,],[191,208,]),'r_generate_parameter':([167,],[193,]),'r_generate_quad_asig_for':([187,],[205,]),'r_pop_ff':([194,],[210,]),'r_act_param_count':([209,],[220,]),'r_expresion_for':([221,],[225,]),'r_check_exp_for':([228,],[230,]),'r_goto_while':([229,],[231,]),'r_goto_for':([235,],[236,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAMA ID PUNTOCOMA prog','programa',4,'p_programa','parser2.py',126),
  ('prog -> main','prog',1,'p_prog','parser2.py',140),
  ('prog -> dec_vars dec_funciones main','prog',3,'p_prog','parser2.py',141),
  ('prog -> dec_vars main','prog',2,'p_prog','parser2.py',142),
  ('prog -> dec_funciones main','prog',2,'p_prog','parser2.py',143),
  ('main -> PRINCIPAL actualiza_func_name PARENT_A PARENT_C dec_est','main',5,'p_main','parser2.py',150),
  ('actualiza_func_name -> <empty>','actualiza_func_name',0,'p_actualiza_func_name','parser2.py',153),
  ('dec_vars -> VAR vars save_vars','dec_vars',3,'p_dec_vars','parser2.py',173),
  ('vars -> tipo_simple ids_simple PUNTOCOMA','vars',3,'p_vars','parser2.py',190),
  ('vars -> tipo_simple ids_simple PUNTOCOMA vars','vars',4,'p_vars','parser2.py',191),
  ('save_vars -> <empty>','save_vars',0,'p_save_vars','parser2.py',197),
  ('tipo_simple -> INT','tipo_simple',1,'p_tipo_simple','parser2.py',214),
  ('tipo_simple -> FLOAT','tipo_simple',1,'p_tipo_simple','parser2.py',215),
  ('tipo_simple -> CHAR','tipo_simple',1,'p_tipo_simple','parser2.py',216),
  ('ids_simple -> ID save_vars_name','ids_simple',2,'p_ids_simple','parser2.py',225),
  ('ids_simple -> ID save_vars_name dimension','ids_simple',3,'p_ids_simple','parser2.py',226),
  ('ids_simple -> ID save_vars_name COMA ids_simple','ids_simple',4,'p_ids_simple','parser2.py',227),
  ('ids_simple -> ID save_vars_name dimension COMA ids_simple','ids_simple',5,'p_ids_simple','parser2.py',228),
  ('save_vars_name -> <empty>','save_vars_name',0,'p_save_vars_name','parser2.py',233),
  ('dimension -> CORCHETE_A CTE_I CORCHETE_C','dimension',3,'p_dimension','parser2.py',252),
  ('variable -> ID r_push_id','variable',2,'p_variable','parser2.py',268),
  ('variable -> ID r_push_id dim','variable',3,'p_variable','parser2.py',269),
  ('r_push_id -> <empty>','r_push_id',0,'p_r_push_id','parser2.py',274),
  ('variables -> variable r_generate_quad_leer','variables',2,'p_variables','parser2.py',303),
  ('variables -> variable r_generate_quad_leer COMA variables','variables',4,'p_variables','parser2.py',304),
  ('dim -> CORCHETE_A expresion CORCHETE_C','dim',3,'p_dim','parser2.py',309),
  ('dec_funciones -> funcion r_generate_endfunc','dec_funciones',2,'p_dec_funciones','parser2.py',314),
  ('dec_funciones -> funcion r_generate_endfunc dec_funciones','dec_funciones',3,'p_dec_funciones','parser2.py',315),
  ('r_generate_endfunc -> <empty>','r_generate_endfunc',0,'p_r_generate_endfunc','parser2.py',319),
  ('funcion -> FUNCION tipo_simple ID create_func_table func_dos','funcion',5,'p_funcion','parser2.py',346),
  ('funcion -> FUNCION VOID func_type_void ID create_func_table func_dos','funcion',6,'p_funcion','parser2.py',347),
  ('func_type_void -> <empty>','func_type_void',0,'p_func_type_void','parser2.py',351),
  ('create_func_table -> <empty>','create_func_table',0,'p_create_func_table','parser2.py',358),
  ('func_dos -> PARENT_A PARENT_C var_funcs','func_dos',3,'p_func_dos','parser2.py',401),
  ('func_dos -> PARENT_A parametros PARENT_C save_params var_funcs','func_dos',5,'p_func_dos','parser2.py',402),
  ('save_params -> <empty>','save_params',0,'p_save_params','parser2.py',408),
  ('var_funcs -> dec_est','var_funcs',1,'p_var_funcs','parser2.py',423),
  ('var_funcs -> dec_vars dec_est','var_funcs',2,'p_var_funcs','parser2.py',424),
  ('parametros -> tipo_simple ID save_params_list','parametros',3,'p_parametros','parser2.py',429),
  ('parametros -> tipo_simple ID save_params_list COMA parametros','parametros',5,'p_parametros','parser2.py',430),
  ('save_params_list -> <empty>','save_params_list',0,'p_save_params_list','parser2.py',435),
  ('dec_est -> LLAVE_A LLAVE_C','dec_est',2,'p_dec_est','parser2.py',455),
  ('dec_est -> LLAVE_A estatutos_dos LLAVE_C','dec_est',3,'p_dec_est','parser2.py',456),
  ('estatutos -> asignacion PUNTOCOMA','estatutos',2,'p_estatutos','parser2.py',461),
  ('estatutos -> llamada PUNTOCOMA','estatutos',2,'p_estatutos','parser2.py',462),
  ('estatutos -> retorno PUNTOCOMA','estatutos',2,'p_estatutos','parser2.py',463),
  ('estatutos -> lectura PUNTOCOMA','estatutos',2,'p_estatutos','parser2.py',464),
  ('estatutos -> escritura PUNTOCOMA','estatutos',2,'p_estatutos','parser2.py',465),
  ('estatutos -> decision','estatutos',1,'p_estatutos','parser2.py',466),
  ('estatutos -> ciclo_for','estatutos',1,'p_estatutos','parser2.py',467),
  ('estatutos -> ciclo_while','estatutos',1,'p_estatutos','parser2.py',468),
  ('estatutos_dos -> estatutos','estatutos_dos',1,'p_estatutos_dos','parser2.py',473),
  ('estatutos_dos -> estatutos estatutos_dos','estatutos_dos',2,'p_estatutos_dos','parser2.py',474),
  ('asignacion -> variable IGUAL r_push_oper expresion r_generate_quad_asig','asignacion',5,'p_asignacion','parser2.py',479),
  ('r_generate_quad_asig -> <empty>','r_generate_quad_asig',0,'p_r_generate_quad_asig','parser2.py',483),
  ('llamada -> ID r_check_func_exists PARENT_A r_generate_ERA PARENT_C r_generate_gosub','llamada',6,'p_llamada','parser2.py',530),
  ('llamada -> ID r_check_func_exists PARENT_A r_generate_ERA expresiones PARENT_C r_generate_gosub','llamada',7,'p_llamada','parser2.py',531),
  ('r_check_func_exists -> <empty>','r_check_func_exists',0,'p_r_check_func_exists','parser2.py',535),
  ('r_generate_ERA -> <empty>','r_generate_ERA',0,'p_r_generate_ERA','parser2.py',546),
  ('r_generate_gosub -> <empty>','r_generate_gosub',0,'p_r_generate_gosub','parser2.py',575),
  ('expresiones -> expresion r_generate_parameter','expresiones',2,'p_expresiones','parser2.py',607),
  ('expresiones -> expresion r_generate_parameter COMA r_act_param_count expresion','expresiones',5,'p_expresiones','parser2.py',608),
  ('r_generate_parameter -> <empty>','r_generate_parameter',0,'p_r_generate_parameter','parser2.py',613),
  ('r_act_param_count -> <empty>','r_act_param_count',0,'p_r_act_param_count','parser2.py',648),
  ('expresion -> t_expresion r_generate_quad_or','expresion',2,'p_expresion','parser2.py',655),
  ('expresion -> t_expresion r_generate_quad_or OR r_push_oper expresion','expresion',5,'p_expresion','parser2.py',656),
  ('r_generate_quad_or -> <empty>','r_generate_quad_or',0,'p_r_generate_quad_or','parser2.py',661),
  ('t_expresion -> g_expresion r_generate_quad_and','t_expresion',2,'p_t_expresion','parser2.py',667),
  ('t_expresion -> g_expresion r_generate_quad_and AND r_push_oper t_expresion','t_expresion',5,'p_t_expresion','parser2.py',668),
  ('r_generate_quad_and -> <empty>','r_generate_quad_and',0,'p_r_generate_quad_and','parser2.py',673),
  ('g_expresion -> m_expresion r_generate_quad_logicos','g_expresion',2,'p_g_expresion','parser2.py',678),
  ('g_expresion -> m_expresion op_logicos m_expresion r_generate_quad_logicos','g_expresion',4,'p_g_expresion','parser2.py',679),
  ('r_generate_quad_logicos -> <empty>','r_generate_quad_logicos',0,'p_r_generate_quad_logicos','parser2.py',684),
  ('op_logicos -> MAYORQUE r_push_oper','op_logicos',2,'p_op_logicos','parser2.py',689),
  ('op_logicos -> MENORQUE r_push_oper','op_logicos',2,'p_op_logicos','parser2.py',690),
  ('op_logicos -> MAYORIGUAL r_push_oper','op_logicos',2,'p_op_logicos','parser2.py',691),
  ('op_logicos -> MENORIGUAL r_push_oper','op_logicos',2,'p_op_logicos','parser2.py',692),
  ('op_logicos -> IGUALIGUAL r_push_oper','op_logicos',2,'p_op_logicos','parser2.py',693),
  ('op_logicos -> DIFERENTE r_push_oper','op_logicos',2,'p_op_logicos','parser2.py',694),
  ('m_expresion -> termino r_generate_quad_masmen','m_expresion',2,'p_m_expresion','parser2.py',699),
  ('m_expresion -> termino r_generate_quad_masmen MAS r_push_oper m_expresion','m_expresion',5,'p_m_expresion','parser2.py',700),
  ('m_expresion -> termino r_generate_quad_masmen MENOS r_push_oper m_expresion','m_expresion',5,'p_m_expresion','parser2.py',701),
  ('termino -> factor r_generate_quad_muldiv','termino',2,'p_termino','parser2.py',706),
  ('termino -> factor r_generate_quad_muldiv POR r_push_oper termino','termino',5,'p_termino','parser2.py',707),
  ('termino -> factor r_generate_quad_muldiv DIV r_push_oper termino','termino',5,'p_termino','parser2.py',708),
  ('r_push_oper -> <empty>','r_push_oper',0,'p_r_push_oper','parser2.py',711),
  ('r_generate_quad_masmen -> <empty>','r_generate_quad_masmen',0,'p_r_generate_quad_masmen','parser2.py',718),
  ('r_generate_quad_muldiv -> <empty>','r_generate_quad_muldiv',0,'p_r_generate_quad_muldiv','parser2.py',723),
  ('factor -> PARENT_A r_push_ff expresion PARENT_C r_pop_ff','factor',5,'p_factor','parser2.py',797),
  ('factor -> CTE_I r_push_cte_i','factor',2,'p_factor','parser2.py',798),
  ('factor -> CTE_F r_push_cte_f','factor',2,'p_factor','parser2.py',799),
  ('factor -> CTE_CH r_push_cte_c','factor',2,'p_factor','parser2.py',800),
  ('factor -> variable','factor',1,'p_factor','parser2.py',801),
  ('factor -> act_flag_llamada llamada','factor',2,'p_factor','parser2.py',802),
  ('act_flag_llamada -> <empty>','act_flag_llamada',0,'p_act_flag_llamada','parser2.py',807),
  ('r_push_cte_i -> <empty>','r_push_cte_i',0,'p_r_push_cte_i','parser2.py',819),
  ('r_push_cte_f -> <empty>','r_push_cte_f',0,'p_r_push_cte_f','parser2.py',832),
  ('r_push_cte_c -> <empty>','r_push_cte_c',0,'p_r_push_cte_c','parser2.py',845),
  ('r_push_ff -> <empty>','r_push_ff',0,'p_r_push_ff','parser2.py',856),
  ('r_pop_ff -> <empty>','r_pop_ff',0,'p_r_pop_ff','parser2.py',863),
  ('retorno -> REGRESA PARENT_A expresion PARENT_C r_generate_quad_retorno','retorno',5,'p_retorno','parser2.py',879),
  ('r_generate_quad_retorno -> <empty>','r_generate_quad_retorno',0,'p_r_generate_quad_retorno','parser2.py',883),
  ('lectura -> LEER PARENT_A variables PARENT_C','lectura',4,'p_lectura','parser2.py',912),
  ('r_generate_quad_leer -> <empty>','r_generate_quad_leer',0,'p_r_generate_quad_leer','parser2.py',916),
  ('escritura -> ESCRIBIR PARENT_A escr PARENT_C','escritura',4,'p_escritura','parser2.py',929),
  ('escritura_dos -> CTE_STR r_push_cte_str','escritura_dos',2,'p_escritura_dos','parser2.py',934),
  ('escritura_dos -> expresion','escritura_dos',1,'p_escritura_dos','parser2.py',935),
  ('r_push_cte_str -> <empty>','r_push_cte_str',0,'p_r_push_cte_str','parser2.py',942),
  ('r_generate_quad_escr -> <empty>','r_generate_quad_escr',0,'p_r_generate_quad_escr','parser2.py',954),
  ('escr -> escritura_dos r_generate_quad_escr','escr',2,'p_escr','parser2.py',971),
  ('escr -> escritura_dos r_generate_quad_escr COMA escr','escr',4,'p_escr','parser2.py',972),
  ('decision -> if r_end_if','decision',2,'p_decision','parser2.py',977),
  ('decision -> if r_goto_ifelse else r_end_if','decision',4,'p_decision','parser2.py',978),
  ('if -> SI PARENT_A expresion PARENT_C r_check_exp_type ENTONCES LLAVE_A estatutos_dos LLAVE_C','if',9,'p_if','parser2.py',982),
  ('r_check_exp_type -> <empty>','r_check_exp_type',0,'p_r_check_exp_type','parser2.py',985),
  ('r_end_if -> <empty>','r_end_if',0,'p_r_end_if','parser2.py',1008),
  ('r_goto_ifelse -> <empty>','r_goto_ifelse',0,'p_r_goto_ifelse','parser2.py',1021),
  ('else -> SINO LLAVE_A estatutos_dos LLAVE_C','else',4,'p_else','parser2.py',1055),
  ('ciclo_while -> MIENTRAS r_save_jump PARENT_A expresion PARENT_C r_check_exp_type HAZ LLAVE_A estatutos_dos LLAVE_C r_goto_while','ciclo_while',11,'p_ciclo_while','parser2.py',1059),
  ('r_goto_while -> <empty>','r_goto_while',0,'p_r_goto_while','parser2.py',1063),
  ('r_save_jump -> <empty>','r_save_jump',0,'p_r_save_jump','parser2.py',1082),
  ('ciclo_for -> DESDE ID r_save_var_for IGUAL expresion r_generate_quad_asig_for HASTA r_save_jump r_expresion_for expresion r_check_exp_for HACER LLAVE_A estatutos_dos LLAVE_C r_goto_for','ciclo_for',16,'p_ciclo_for','parser2.py',1091),
  ('r_expresion_for -> <empty>','r_expresion_for',0,'p_r_expresion_for','parser2.py',1095),
  ('r_save_var_for -> <empty>','r_save_var_for',0,'p_r_save_var_for','parser2.py',1117),
  ('r_generate_quad_asig_for -> <empty>','r_generate_quad_asig_for',0,'p_r_generate_quad_asig_for','parser2.py',1151),
  ('r_check_exp_for -> <empty>','r_check_exp_for',0,'p_r_check_exp_for','parser2.py',1203),
  ('r_goto_for -> <empty>','r_goto_for',0,'p_r_goto_for','parser2.py',1226),
]
