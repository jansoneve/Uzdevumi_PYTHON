import math

def hipotenuza(a, b):
    hipotenuza=math.sqrt(pow(a,2)+pow(b,2))
    return hipotenuza
if (b<=0) or (a<=0):
    print(0)
    break

print(hipotenuza(3, 4))
"""
    Funkcija akceptē divus argumentus - katešu garumus un atgriež 
    hipotenūzas garumu, vai 0, ja kaut vienas katetes garums ir <= 0
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem.

    Argumenti:
        a {int vai float} -- katetes a garums
        b {int vai float} -- katetes b garums
    Atgriež:
        int vai float -- hipotenūzas garums
    Piemēri:
        hipotenuza(3, 4) == 5.0
        hipotenuza(3, 0) == 0
    """
