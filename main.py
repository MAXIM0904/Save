import os


def file_output(location_file_print):
    file_contents = open(location_file_print, "r")
    print(f"Содержимое файла:\n{file_contents.read()}")
    file_contents.close()


def record_file(text_1, location_file, massage_user="Файл успешно сохранен!"):
    write_file = open(location_file, "w")
    write_file.write(text_1)
    write_file.close()
    print(massage_user)
    file_output(location_file)


def file_director(location_save, text_user):
    name_file = input("Введите имя файла: ")
    location_save = os.path.join(location_save, f"{name_file}.txt")
    if os.path.isfile(location_save):
        user_answer = input("Вы действительно хотите перезаписать файл? ").lower()
        if user_answer == "да":
            record_file(text_user, location_save, "Файл успешно перезаписан!")
        else:
            print("Перезапись отменена")
            file_output(location_save)
    else:
        record_file(text, location_save)


def control_direct():
    while True:
        control_location_save = input("Куда хотите сохранить документ? Введите последовательность "
                                      "папок (через пробел): ").split()
        control_location_save = os.path.abspath(os.path.join(os.path.sep, *control_location_save))
        if os.path.isdir(control_location_save):
            return control_location_save
        else:
            print("Указанного места не существует!")


while True:
    text = input("Введите строку: ")
    if text == "все":
        break
    location_save_user = os.path.join(control_direct())  # Users А PycharmProjects python_basic Module14
    file_director(location_save_user, text)

# зачёт!
