#Nova funcionalitat

llenguatge = ""
llenguatges_list = []
while llenguatge != "0":
    llenguatge = input("LLenguatge de programació que coneixes? 0 per acabar: ")
    llenguatges_list.append(llenguatge)

print("Segons")
for l in llenguatges_list:
    print(l)