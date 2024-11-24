#Nova funcionalitat

print("Introdueix els llenguatges de programació que domines:")
print("Per acabar introdueix un 0.")
llenguatge = input()
llenguatges_list = []
while llenguatge != "0":
    llenguatges_list.append(llenguatge)
    llenguatge = input()
print("Llenguatges:", llenguatges_list)