def transpile(ast):
         if ast.get("context") == "化学":
             return """
             qreg q[2];
             h q[0]; 
             cx q[0],q[1];
             measure q -> c;
             """
         raise ValueError("Unknown context")
