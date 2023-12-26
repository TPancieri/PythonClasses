def greet_pythons(items: list) -> None:
    greeting = 'Hello'
    print(f'ID of `greeting` in `greet_pythons` is {id(greeting)}')

    def make_greeting(item: str) -> str:
        greeting = 'Hi'
        print(f'ID of `greeting` in `make_greeting` is {id(greeting)}')
        return f'{greeting} {item}'

    for item in items:
        print(make_greeting(item))
    print(f'Inside greet_pythons, `greeting` is {greeting}')
    print(f'ID of `greeting` in `greet_pythons` is {id(greeting)}')


names = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)
