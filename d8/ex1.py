
def greet():
    print('xxx')
    print('xxx')
    print('xxx')


greet()


def greet_with_name(name): #parameter
    print(f'hello {name}')
    print(f'howdy {name}')

greet_with_name('Angela') #argument - value of the data

def greet_with(name, location):
    print(f'Hello {name}, what is it like in {location} ?')

greet_with("Jakub", "Gdansk")
greet_with(name="Hubert", location="London")