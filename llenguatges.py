#Nova funcionalitat

llenguatge = ""
llenguatges_list = []
while llenguatge != "stop":
    llenguatge = input("LLenguatge de programació que coneixes? 'stop' per acabar: ")
    llenguatges_list.append(llenguatge)

print("Segons")
for l in llenguatges_list:
    print(l)