""" 5. Algorisme que llegeix 3 nombres i diu quin és el major. """
A = input("Entra el primer numero: ")
A = int(A)
B = input("Entra el segon numero: ")
B = int(B)
C = input("Entra el tercer numero: ")
C = int(C)
if A > B:
    if A > C:
        print("El major es: ", A)
if A < B:
    if B > C:
        print("El major es: ", B)
    else:
        print("El major es: ", C)
if A == B:
    if B == C:
        print("Tots son iguals")
    if B > C:
        print("El major es: ", B)
    if C > B:
        print("El major es: ", C)
