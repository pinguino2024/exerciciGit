#Nova funcionalitat

llenguatge = ""
llenguatges_list = []
while llenguatge != "-1":
    llenguatge = input("LLenguatge de programació que coneixes? -1 per acabar: ")
    llenguatges_list.append(llenguatge)

print("Llenguatges")
for l in llenguatges_list:
    print(l)