import ply.lex as lex
import ply.yacc as yacc
from math import pi
from math import pow
import networkx as nx
import matplotlib.pyplot as plt
from library import *
from math import pi
from math import pow
from networkx.drawing.nx_pydot import graphviz_layout

parseGraph = None
NODE_COUNTER = 0

def add_node(attr):
   global parseGraph
   global NODE_COUNTER
   print(parseGraph)
   attr["counter"] = NODE_COUNTER
   parseGraph.add_node(NODE_COUNTER, **attr)
   NODE_COUNTER += 1


   return parseGraph.nodes[NODE_COUNTER - 1]


symbol_table = dict()


symbol_table["PI"] = pi
symbol_table["E"] = 2.718281828459045


def myPrint(v1,v2,v3,v4):
   print("Printing: ", v1,v2,v3,v4)


def do_nothing():
   print("We are nothing...")


def sumAB(a,b):
   return a+b


symbol_table["myPrint"] = myPrint
symbol_table["nothing"] = do_nothing
symbol_table["sumAB"] = sumAB
symbol_table["load"] = load_image
symbol_table["show"] = show_image
symbol_table["tuple"] = gen_vector
symbol_table["showi"] = show_histograma


# These will be our terminal characters
tokens = (
   'NUMBER',
   'VARIABLE',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIV',
   'EQUAL',
   'EXP',
   'LPAREN',
   'RPAREN',
   'COMMA',
   'CONNECT',
   'STRING'
   )

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_EQUAL = r'='
t_EXP = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_CONNECT = r'->'


def t_STRING(t):
   r'\"(.)*\"'
   t.value = t.value[1:-1]
   return t


def t_NUMBER(t):
   r'\d+\.?\d*'


   if (t.value.find(".") > -1):
       t.value = float(t.value)
   else:
       t.value = int(t.value)
   return t


'''
def t_FUNCTION(t):
   r'[a-zA-Z_][a-zA-Z0-9_]*\(   (\d+\.?\d*  |    [a-zA-Z_][a-zA-Z0-9_]*   )     \)'
   print("****" , t.value)
   s = t.value[0:-1].split("(")
   t.value = s
   return t
'''


def t_VARIABLE(t):
   r'[a-zA-Z_][a-zA-Z0-9_]*'
   return t


def t_error(t):
   print("Error on  ", t.value)
   t.lexer.skip(1)


print("Translator v1.0")


lexer = lex.lex()


def p_assignment_assign(p):
   '''
   assignment : VARIABLE EQUAL expression
   '''
   node = add_node({'type':'ASSIGN', 'label':f'=', 'value':''})
   node_var = add_node({'type':'VARIABLE_ASSIGN', 'label':f'VAR_{p[1]}', 'value':p[1]})


   parseGraph.add_edge(node["counter"], node_var["counter"])
   parseGraph.add_edge(node["counter"], p[3]["counter"])
  
   p[0] = node


def p_assignment_flow(p):
   '''
   assignment : VARIABLE EQUAL flow
   '''
   node = add_node({'type':'ASSIGN', 'label':f'=', 'value':''})
   node_var = add_node({'type':'VARIABLE_ASSIGN', 'label':f'VAR_{p[1]}', 'value':p[1]})


   parseGraph.add_edge(node["counter"], node_var["counter"])
   parseGraph.add_edge(node["counter"], p[3]["counter"])
  
   p[0] = node


def p_flow(p):
   '''
   flow : VARIABLE CONNECT flow_functions
   '''
   # Nos regresa el ID de las conexiones
   connections = parseGraph.neighbors(p[3][0]["counter"])


   # Convertir las conexiones a sus nodos correspondientes
   for c in connections:
       c = parseGraph.nodes[c]
       if(c["type"] == "PENDING_NODE"):
           c["type"] = "VARIABLE"
           c["label"] = f"VAR_{p[1]}"
           c["value"] = p[1]
           break


   p[0] = p[3][-1]


def p_flow_functions(p):
   '''
   flow_functions : flow_function_call CONNECT flow_functions
   '''
   # Nos regresa el ID de las conexiones
   connections = parseGraph.neighbors(p[3][0]["counter"])


   # Convertir las conexiones a sus nodos correspondientes
   for c in connections:
       c = parseGraph.nodes[c]
       if(c["type"] == "PENDING_NODE"):
           parseGraph.add_edge(c["counter"], p[1]["counter"])
           break


   p[0] = [p[1]] + p[3]


def p_flow_functions_alone(p):
   '''
   flow_functions : flow_function_call
   '''
   p[0] = [p[1]]


def p_flow_function_call(p):
   '''
   flow_function_call : VARIABLE LPAREN params RPAREN
   '''
   node = add_node({"type":"FLOW_FUNCTION_CALL", "label":f"ff_{p[1]}", "value":p[1]})
   pending_node = add_node({"type":"PENDING_NODE", "label":f"pending", "value":""})
   parseGraph.add_edge(node["counter"], pending_node["counter"])


   for n in p[3]:
       parseGraph.add_edge(node["counter"], n["counter"])


   p[0] = node


def p_assignment_expression(p):
   '''
   assignment : expression
   '''
   p[0] = p[1]


def p_expression_term(p):
   '''
   expression : term
               | string_def
   '''
   p[0] = p[1]


def p_string_def(p):
   '''
   string_def : STRING
   '''
   p[0] = add_node({"type":"STRING", "label":p[1], "value":p[1]})


def p_expression_plus(p):
   '''
   expression : expression PLUS term
   '''
   node = add_node({'type':'PLUS', 'label':f'+', 'value':''})
   parseGraph.add_edge(node["counter"], p[1]["counter"])
   parseGraph.add_edge(node["counter"], p[3]["counter"])


   p[0] = node


def p_expression_minus(p):
   '''
   expression : expression MINUS term
   '''
   node = add_node({'type':'MINUS', 'label':f'-', 'value':''})
   parseGraph.add_edge(node["counter"], p[1]["counter"])
   parseGraph.add_edge(node["counter"], p[3]["counter"])


   p[0] = node


def p_term_exponent(p):
   '''
   term : exponent
   '''
   p[0] = p[1]


def p_term_times(p):
   '''
   term : term TIMES exponent
   '''
   node = add_node({'type':'TIMES', 'label':f'*', 'value':''})
   parseGraph.add_edge(node["counter"], p[1]["counter"])
   parseGraph.add_edge(node["counter"], p[3]["counter"])


   p[0] = node


def p_term_divides(p):
   '''
   term : term DIV exponent
   '''
   node = add_node({'type':'DIV', 'label':f'/', 'value':''})
   parseGraph.add_edge(node["counter"], p[1]["counter"])
   parseGraph.add_edge(node["counter"], p[3]["counter"])


   p[0] = node


def p_exponent_factor(p):
   '''
   exponent : factor
   '''
   p[0] = p[1]


def p_exponent_exp(p):
   '''
   exponent : factor EXP factor
   '''
   node = add_node({'type':'POWER', 'label':f'POW', 'value':''})
   parseGraph.add_edge(node["counter"], p[1]["counter"])
   parseGraph.add_edge(node["counter"], p[3]["counter"])


   p[0] = node


# p: Expresion que acabamos de parsear
def p_factor_num(p):
   '''
   factor : NUMBER
   '''
   # p[0] tiene factor
   # p[1] tiene NUMBER
   # Entonces se cambia el factor -> NUMBER
   n = add_node({'type':'NUMBER', 'label':f'NUM_{p[1]}', 'value':p[1]})
  
   p[0] = n


def p_factor_variable(p):
   '''
   factor : VARIABLE
   '''
   p[0] = add_node({'type':'VARIABLE', 'label':f'VAR_{p[1]}', 'value':p[1]})


def p_factor_expr(p):
   '''
   factor : LPAREN expression RPAREN
   '''
   node = add_node({'type':'GROUP', 'label':f'( )', 'value':''})
   parseGraph.add_edge(node["counter"], p[2]["counter"])


   p[0] = node


def p_factor_function_call(p):
   '''
   factor : function_call
   '''
   p[0] = p[1]


def p_function_call_no_params(p):
   '''
   function_call : VARIABLE LPAREN RPAREN
   '''
   p[0] = add_node({'type':'FUNCTION_CALL', 'label':f'FUN_{p[1]}', 'value':p[1]})


def p_function_call_params(p):
   '''
   function_call : VARIABLE LPAREN params RPAREN
   '''
   node = add_node({'type':'FUNCTION_CALL', 'label':f'FUN_{p[1]}', 'value':p[1]})


   # For every parameter, generate an edge to connect it to the function
   for n in p[3]:
       parseGraph.add_edge(node["counter"], n["counter"])


   p[0] = node


def p_params(p):
   '''
   params : params COMMA expression
           | expression
   '''
   if(len(p) > 2):
       # Se concatena al resto de los parametros
       p[0] = p[1] + [p[3]]
   else:
       p[0] = [p[1]]


'''
def p_exponent_expr(p):
   ''
   exponent : LPAREN expression RPAREN
   ''
   node = add_node({'type':'GROUP', 'label':f'( )', 'value':''})
   parseGraph.add_edge(node["counter"], p[2]["counter"])


   p[0] = node
'''


def p_error(p):
   print("Syntax error in input: ", p)


def execute_parse_tree(tree):
   root = tree.nodes[0]
   root_id = 0
   res = visit_node(tree, root_id, -1)


   return res


def visit_node(tree, node_id, from_id):
   children = tree.neighbors(node_id)
   res = []
   for c in children:
       if(c != from_id):
           res.append(visit_node(tree, c, node_id))
           # print(res[-1])
   current_node = tree.nodes[node_id]


   if(current_node["type"] == "INITIAL"):
       return res[0]
  
   if(current_node["type"] == "ASSIGN"):
       symbol_table[res[0]] = res[1]
       # print(symbol_table)
       return res[1]
  
   if(current_node["type"] == "NUMBER"):
       return current_node["value"]
  
   if(current_node["type"] == "STRING"):
       return current_node["value"]
  
   if(current_node["type"] == "PENDING_NODE"):
       return res[0]
  
   if(current_node["type"] == "VARIABLE_ASSIGN"):
       return current_node["value"]
  
   if(current_node["type"] == "VARIABLE"):
       if current_node["value"] in symbol_table:
           return symbol_table[current_node["value"]]
       print("ERROR! Variable not found, returning 0")
       return 0
  
   if(current_node["type"] == "FUNCTION_CALL" or current_node["type"] == "FLOW_FUNCTION_CALL"):
       if current_node["value"] in symbol_table:
           if (len(res) > 0):
               return symbol_table[current_node["value"]](*res)
           else:
               return symbol_table[current_node["value"]]()
       else:
           fn = search_cv2(current_node["value"])
           if fn is not None:
               return fn(*res)
       print("ERROR! Function not found, returning 0")
       return 0
  
   if current_node["type"] == "POWER":
       return pow(res[0], res[1])
  
   if current_node["type"] == "PLUS":
       return res[0] + res[1]
  
   if current_node["type"] == "MINUS":
       return res[0] - res[1]
  
   if current_node["type"] == "TIMES":
       return res[0] * res[1]


   if current_node["type"] == "DIV":
       return res[0] / res[1]
  
   if current_node["type"] == "GROUP":
       return res[0]


parser = yacc.yacc()


while True:
   data = input(">")


   if(data == 'exit'):
       break


   if(data == 'st'):
       print(symbol_table)
       continue


   parseGraph = nx.Graph()
   NODE_COUNTER = 0


   root = add_node({"type":"INITIAL", "label":"INIT"})


   # Obtener el resultado del parsing de data
   result = parser.parse(data)


   parseGraph.add_edge(root["counter"], result["counter"])


   labels = nx.get_node_attributes(parseGraph, "label")
  
   # Visualizacion del arbol de ejecucion
   #nx.draw(parseGraph, labels=labels, with_labels=True)
   #plt.show()


   result = execute_parse_tree(parseGraph)
   print("Result", result)
   '''
   La ventaja de hacerlo como un grafo es que el codigo como grafo
   representa la ejecucion, efectivamente ya compilado. Entonces es
   transferible a cualquier computadora.
   '''

# Image Segmentation with Watershed Algorithm
img = cv2.imread('coins.jpeg')
assert img is not None, "file could not be read, check with os.path.exists()"
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
 
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
 
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
 
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
 
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
 
# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

print("\nended")

# from networkx.drawing.nx_pydot import graphviz_layout
