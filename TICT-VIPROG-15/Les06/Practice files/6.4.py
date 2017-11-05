studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    antw=[]
    for student in studentencijfers:
        antw.append(sum(student)/3)
    return antw

print(gemiddelde_per_student(studentencijfers))

def gemiddelde_van_alle_studenten(studentencijfers):
    antw = sum(gemiddelde_per_student(studentencijfers))/4
    return antw
print(gemiddelde_van_alle_studenten(studentencijfers))
