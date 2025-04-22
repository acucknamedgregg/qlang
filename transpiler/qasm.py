"""
QLang Radical-Aware Transpiler  
- Optimizes quantum circuits using Chinese character radicals  
- Context-aware gate selection  
"""

def transpile(ast: dict) -> str:
    """Converts QLang AST to optimized QASM."""
    # Step 1: Radical-based optimizations (e.g., 氵 → decoupling)
    gates = apply_radical_optimizations(ast['characters'])
    
    # Step 2: Context-aware gate selection (e.g., 化学 → excitation-preserving)
    gates += apply_context_rules(ast.get('context', 'default'))
    
    return to_qasm(gates)

def apply_radical_optimizations(characters: list) -> list:
    """Adds noise mitigation based on radicals."""
    gates = []
    for char in characters:
        if '氵' in char:  # Water radical = amplitude damping
            gates.extend(['Delay(100, dt)', f'measure {char}'])
        elif '火' in char:  # Fire radical = thermal relaxation
            gates.extend(['T2Swap', f'measure {char}'])
    return gates

def apply_context_rules(context: str) -> list:
    """Selects gate sets for chemistry/finance/etc."""
    if context == '化学':
        return ['rz', 'ry', 'cx']  # Hardware-efficient
    elif context == '金融':
        return ['h', 'cx', 'swap']  # QAOA-friendly
    return ['h', 'cx']  # Default

def to_qasm(gates: list) -> str:
    """Formats as QASM."""
    return '\n'.join(gates)

# Example usage  
if _name_ == '_main_':
    example_ast = {
        'characters': ['测', '量'],
        'context': '化学'
    }
    print(transpile(example_ast))
