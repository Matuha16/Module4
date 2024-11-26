def test_function():
    def inner_finction():
        print('Я в области видимости функции test_function')
    inner_finction()


test_function()