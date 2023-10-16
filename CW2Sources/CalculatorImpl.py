import json
import sys

def evaluate_expr(parsed_expr):

    if isinstance(parsed_expr,dict):
        for key,value in parsed_expr.items():
            if key == 'plus':
                x1 = evaluate_expr(value)
                return sum(x1)
            elif key =='minus':
                x1 = evaluate_expr(value)
                return(x1[0]-x1[1])
            
            elif key =='times':
                x1= evaluate_expr(value)
                return(x1[0]*x1[1])
            
            elif key =='int':
                return value
            
            elif key == 'root':
                return evaluate_expr(value)
            
    elif isinstance(parsed_expr,list):
        oprs=[]
        for arg in parsed_expr:
            oprs.append(evaluate_expr(arg))
        return oprs
    
    elif isinstance(parsed_expr, int):
        return parsed_expr
              

    """This function takes an expression parsed from the JSON
       arithmetic expression format and returns the full evaluation.
       That is, if the JSON expresses '1+1', this function returns '2'."""
    return None

def load_json_expr(json_path):

    with open(json_path, 'r') as file:
        parsed_json = json.load(file)
    """This function takes a file path to a JSON file  represened
       as a string and returns a parsed form. You can presume that
       the JSON file is valid wrt the arithmetic expression format."""
    return parsed_json
    
    pass
    

if __name__=='__main__':
    expr_file_path = sys.argv[1]
    print(evaluate_expr(load_json_expr(expr_file_path)))
