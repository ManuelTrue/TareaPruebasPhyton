import pytest
from numerosAmigos import numeros_amigos
esperado=" son amigos"


@pytest.mark.parametrize(
        "número1,número2,esperado",
[(220,284,esperado),
 (1184,1210,esperado),
 (6,6,esperado),
 (120,284,esperado),
 (1184,1210,esperado),
 (630,54,esperado),
 (90,56,esperado),
 (63,14,esperado),
 (262,2924,esperado),
 (2924,2620,esperado)
 ]

)
def test_numeroAmigos_param(número1,número2,esperado):
    assert numeros_amigos(número1,número2)==str(número1) +" y " +str(número2)+ esperado
