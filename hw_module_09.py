from functools import wraps

dict_of_contacts = {}


def input_error(func):
    @wraps(func)
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return print("Give me name and phone please")
        except ValueError:
            return print("Enter user name")
        except KeyError:
            return print("Try again. Not correct key")
    return inner


def hello(*args):
    return print("How can I help You?")


@input_error
def add(*args):
    list_of_param = args[0].split()
    global dict_of_contacts
    name = str(list_of_param[0])
    number = list_of_param[1:]
    if not number:
        raise IndexError()
    dict_of_contacts.update({name.capitalize(): list_of_param[1:]})

    return dict_of_contacts


@input_error
def change(*args):
    list_of_param = args[0].split()
    global dict_of_contacts
    name = str(list_of_param[0])
    for keys in dict_of_contacts.keys():
        if name.capitalize() == keys:
            dict_of_contacts.update({keys: list_of_param[1:]})
    number = list_of_param[1:]
    if not number:
        raise IndexError()
    return f"{dict_of_contacts}"


@input_error
def phone(*args):
    global dict_of_contacts
    name = str(args[0])
    for keys in dict_of_contacts.keys():
        if name.capitalize() == keys:
            return print('\n'.join(dict_of_contacts.get(keys)))
    if not name:
        raise ValueError()


def show_all(*args):
    return print('\n'.join([f'{k}: {", ".join(v)}' for k, v in dict_of_contacts.items()]))


def exit(*args):
    return print("Good bye!")


def no_command(*args):
    return print("Unknown command, try again")


COMMANDS = {hello: "hello", add: "add", change: "change", phone: "phone",
            show_all: "show all", exit: ["good bye", "close", "exit"]}


def handler(text):
    for command, kword in COMMANDS.items():
        if text in kword:
            if type(kword) is str:
                return command, text.replace(kword, "").strip()
            else:
                return command, None
    return no_command, None


def main():
    while True:
        user_input = input(">>>")
        command, data = handler(user_input.lower())
        command(data)
        if command == exit:
            break


if __name__ == "__main__":
    main()
