import datetime
def get_employees():
    a = datetime.datetime.today().strftime("%d.%m.%Y")
    print(F' {a}  Hello, peoples!')


if __name__ == '__main__':
    get_employees()
