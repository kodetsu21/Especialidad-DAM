""" 3. Algorisme que llegeix dos nombres i mostra com a resultat quin és el més gran. """
A = input("Entra el primer numero: ")
A = int(A)
B = input("Entra el segon numero: ")
B = int(B)
if A < B:
    print(A, " < ", B)
if A == B:
    print(A, " = ", B)
if A > B:
    print(A, " > ", B)
