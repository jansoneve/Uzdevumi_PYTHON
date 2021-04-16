def summa(a, b):
    summa=a+b
    return summa
print("rezultātam 12: ", summa(-4, -5))
rez=summa(1,1)
print(rez)
print("pozitīvs + neg tests",summa(5,-5)==0.0)

"""
    Funkcija akceptē divus argumentus - skaiļus a un b,
    aprēķina to summu un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem.

    Argumenti:
        a {int vai float} -- pirmais skaitlis
        b {int vai float} -- otrais skaitlis
    Atgriež:
        int vai float -- argumentu summa
    Piemēri:
        summa(1, 1) == 2
        summa(1.0, -1) == 0.0
        summa(2.5, 1.2) == 3.7
    """
