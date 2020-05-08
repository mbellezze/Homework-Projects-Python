def leer():
    with open("Myfile.txt", mode="r") as my_new_file:
        contents = my_new_file.read()
    return contents


def escribir():
    with open("Myfile.txt", mode="a") as my_new_file:
        my_new_file.write("\nHola Gime")

escribir()
print(leer())