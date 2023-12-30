def get_age_group(age):
 
    """
    Devuelve el grupo de edad basado en la edad en años dentro del intervalo 0..150
    de lo contrario, devuelve 'desconocido'.
    """
    
    if 0 <= age <= 14:
        return 'infancia'

    if 15 <= age <= 24:
        return 'juventud' #young

    if 25 <= age <= 64:
        return 'adulto'

    if 65 <= age <= 100:
        return 'vejez'

    if (age < 0 or age > 100):
        return 'desconocido'
 
def test_get_age_group():
 
    """prueba unitaria para get_age_group"""
 
    assert get_age_group(-1) == 'desconocido'
    assert get_age_group(0) == 'infancia'
    assert get_age_group(14) == 'infancia'
    assert get_age_group(15) == 'juventud'
    assert get_age_group(24) == 'juventud'
    assert get_age_group(25) == 'adulto'
    assert get_age_group(64) == 'adulto'
    assert get_age_group(65) == 'vejez'
    assert get_age_group(80) == 'vejez'
    assert get_age_group(150) == 'desconocido'
