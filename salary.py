import datetime
def calculate_salary():
    a = datetime.datetime.today().strftime("%d.%m.%Y")
    print(f' {a}  I like the salary!')


if __name__ == '__main__':
    calculate_salary()
