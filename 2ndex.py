print("Введите первый коэффициент уравнения")
aCoef = int(input())
print("Введите второй коэффициент уравнения")
bCoef = int(input())
print("Введите третий коэффициент уравнения")
cCoef = int(input())
print(aCoef, bCoef, cCoef)
disc = (bCoef**2) - (4 * aCoef * cCoef)

if disc < 0:
 print("Корней нет")
else:
 if disc == 0:
  print("Найден единственный корень, его значение:", (-bCoef/(2*aCoef)))
 else:
  if disc > 0:
   ans1 = (-bCoef + disc**0.5) / (2*aCoef)
   ans2 = (-bCoef - disc**0.5) / (2*aCoef)
   print("Найдено два корня:", ans1, ",", ans2)