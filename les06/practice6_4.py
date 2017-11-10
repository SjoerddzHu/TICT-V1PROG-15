studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]
def gemiddelde_per_student(studentencijfers):
    aantalrijen = len(studentencijfers)
    aantalkolommen = len(studentencijfers[0])
    antw = 0
    tijdelijk=0
    gem_lst=[]
    for rij in range(aantalrijen):
        for kolom in range(aantalkolommen):
            tijdelijk+=studentencijfers[rij][kolom]
        antw=tijdelijk/aantalkolommen
        gem_lst.append(antw)
        tijdelijk=0
        antw=0
    return gem_lst
def gemiddelde_van_alle_studenten(studentencijfers):
    aantalrijen = len(studentencijfers)
    aantalkolommen = len(studentencijfers[0])
    antw = 0
    tijdelijk=0
    for rij in range(aantalrijen):
        for kolom in range(aantalkolommen):
            tijdelijk=studentencijfers[rij][kolom]+tijdelijk
    antw=tijdelijk/(aantalrijen*aantalkolommen)
    return antw
print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
