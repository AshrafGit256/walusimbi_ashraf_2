from multipledispatch import dispatch

@dispatch(int, int, int)
def calculate_total(math, science, english):
    total = math + science + english
    print('Total score:', total)

@dispatch(float, float, float)
def calculate_total(gpa1, gpa2, gpa3):
    average = (gpa1 + gpa2 + gpa3) / 3
    print('Average GPA:', round(average, 2))

calculate_total(78, 85, 90)          
calculate_total(3.5, 3.8, 4.0)       
