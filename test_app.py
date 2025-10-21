from app import suma

def test_suma():
    assert suma(2, 3) == 5

# mas ejemplos
#   1- otra forma 
def test_suma_es_correcta():
    a, b = 2, 3
    resultado = suma(a, b)
    assert resultado == 5  # caso base
#   2- Forma logica
def test_suma_mayor_que_operandos():
    for a, b in [(0,1), (2,3), (10,5), (-1,4)]:
        assert suma(a,b) >= a
        assert suma(a,b) >= b