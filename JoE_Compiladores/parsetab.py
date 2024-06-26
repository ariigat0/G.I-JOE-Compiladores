
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA CONNECT DIV EQUAL EXP LPAREN MINUS NUMBER PLUS RPAREN STRING TIMES VARIABLE\n   assignment : VARIABLE EQUAL expression\n   \n   assignment : VARIABLE EQUAL flow\n   \n   flow : VARIABLE CONNECT flow_functions\n   \n   flow_functions : flow_function_call CONNECT flow_functions\n   \n   flow_functions : flow_function_call\n   \n   flow_function_call : VARIABLE LPAREN params RPAREN\n   \n   assignment : expression\n   \n   expression : term\n               | string_def\n   \n   string_def : STRING\n   \n   expression : expression PLUS term\n   \n   expression : expression MINUS term\n   \n   term : exponent\n   \n   term : term TIMES exponent\n   \n   term : term DIV exponent\n   \n   exponent : factor\n   \n   exponent : factor EXP factor\n   \n   factor : NUMBER\n   \n   factor : VARIABLE\n   \n   factor : LPAREN expression RPAREN\n   \n   factor : function_call\n   \n   function_call : VARIABLE LPAREN RPAREN\n   \n   function_call : VARIABLE LPAREN params RPAREN\n   \n   params : params COMMA expression\n           | expression\n   '
    
_lr_action_items = {'VARIABLE':([0,10,12,13,14,15,16,17,18,33,35,40,41,],[2,20,21,20,20,20,20,20,20,36,20,20,36,]),'STRING':([0,10,12,13,35,40,],[7,7,7,7,7,7,]),'NUMBER':([0,10,12,13,14,15,16,17,18,35,40,],[9,9,9,9,9,9,9,9,9,9,9,]),'LPAREN':([0,2,10,12,13,14,15,16,17,18,20,21,35,36,40,],[10,13,10,10,10,10,10,10,10,10,13,13,10,40,10,]),'$end':([1,2,3,4,5,6,7,8,9,11,20,21,22,23,24,27,28,29,30,31,32,34,37,38,43,44,],[0,-19,-7,-8,-9,-13,-10,-16,-18,-21,-19,-19,-1,-2,-22,-11,-12,-14,-15,-17,-20,-23,-3,-5,-4,-6,]),'EQUAL':([2,],[12,]),'EXP':([2,8,9,11,20,21,24,32,34,],[-19,18,-18,-21,-19,-19,-22,-20,-23,]),'TIMES':([2,4,6,8,9,11,20,21,24,27,28,29,30,31,32,34,],[-19,16,-13,-16,-18,-21,-19,-19,-22,16,16,-14,-15,-17,-20,-23,]),'DIV':([2,4,6,8,9,11,20,21,24,27,28,29,30,31,32,34,],[-19,17,-13,-16,-18,-21,-19,-19,-22,17,17,-14,-15,-17,-20,-23,]),'PLUS':([2,3,4,5,6,7,8,9,11,19,20,21,22,24,26,27,28,29,30,31,32,34,39,],[-19,14,-8,-9,-13,-10,-16,-18,-21,14,-19,-19,14,-22,14,-11,-12,-14,-15,-17,-20,-23,14,]),'MINUS':([2,3,4,5,6,7,8,9,11,19,20,21,22,24,26,27,28,29,30,31,32,34,39,],[-19,15,-8,-9,-13,-10,-16,-18,-21,15,-19,-19,15,-22,15,-11,-12,-14,-15,-17,-20,-23,15,]),'RPAREN':([4,5,6,7,8,9,11,13,19,20,24,25,26,27,28,29,30,31,32,34,39,42,],[-8,-9,-13,-10,-16,-18,-21,24,32,-19,-22,34,-25,-11,-12,-14,-15,-17,-20,-23,-24,44,]),'COMMA':([4,5,6,7,8,9,11,20,24,25,26,27,28,29,30,31,32,34,39,42,],[-8,-9,-13,-10,-16,-18,-21,-19,-22,35,-25,-11,-12,-14,-15,-17,-20,-23,-24,35,]),'CONNECT':([21,38,44,],[33,41,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignment':([0,],[1,]),'expression':([0,10,12,13,35,40,],[3,19,22,26,39,26,]),'term':([0,10,12,13,14,15,35,40,],[4,4,4,4,27,28,4,4,]),'string_def':([0,10,12,13,35,40,],[5,5,5,5,5,5,]),'exponent':([0,10,12,13,14,15,16,17,35,40,],[6,6,6,6,6,6,29,30,6,6,]),'factor':([0,10,12,13,14,15,16,17,18,35,40,],[8,8,8,8,8,8,8,8,31,8,8,]),'function_call':([0,10,12,13,14,15,16,17,18,35,40,],[11,11,11,11,11,11,11,11,11,11,11,]),'flow':([12,],[23,]),'params':([13,40,],[25,42,]),'flow_functions':([33,41,],[37,43,]),'flow_function_call':([33,41,],[38,38,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assignment","S'",1,None,None,None),
  ('assignment -> VARIABLE EQUAL expression','assignment',3,'p_assignment_assign','translator.py',133),
  ('assignment -> VARIABLE EQUAL flow','assignment',3,'p_assignment_flow','translator.py',147),
  ('flow -> VARIABLE CONNECT flow_functions','flow',3,'p_flow','translator.py',161),
  ('flow_functions -> flow_function_call CONNECT flow_functions','flow_functions',3,'p_flow_functions','translator.py',182),
  ('flow_functions -> flow_function_call','flow_functions',1,'p_flow_functions_alone','translator.py',201),
  ('flow_function_call -> VARIABLE LPAREN params RPAREN','flow_function_call',4,'p_flow_function_call','translator.py',208),
  ('assignment -> expression','assignment',1,'p_assignment_expression','translator.py',224),
  ('expression -> term','expression',1,'p_expression_term','translator.py',231),
  ('expression -> string_def','expression',1,'p_expression_term','translator.py',232),
  ('string_def -> STRING','string_def',1,'p_string_def','translator.py',239),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','translator.py',246),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','translator.py',258),
  ('term -> exponent','term',1,'p_term_exponent','translator.py',270),
  ('term -> term TIMES exponent','term',3,'p_term_times','translator.py',277),
  ('term -> term DIV exponent','term',3,'p_term_divides','translator.py',289),
  ('exponent -> factor','exponent',1,'p_exponent_factor','translator.py',301),
  ('exponent -> factor EXP factor','exponent',3,'p_exponent_exp','translator.py',308),
  ('factor -> NUMBER','factor',1,'p_factor_num','translator.py',321),
  ('factor -> VARIABLE','factor',1,'p_factor_variable','translator.py',333),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','translator.py',340),
  ('factor -> function_call','factor',1,'p_factor_function_call','translator.py',351),
  ('function_call -> VARIABLE LPAREN RPAREN','function_call',3,'p_function_call_no_params','translator.py',358),
  ('function_call -> VARIABLE LPAREN params RPAREN','function_call',4,'p_function_call_params','translator.py',365),
  ('params -> params COMMA expression','params',3,'p_params','translator.py',380),
  ('params -> expression','params',1,'p_params','translator.py',381),
]
