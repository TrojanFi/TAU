class NewClass:
    def __init__(self, zmienna):
        self.zmienna = zmienna

    def kotlet(self,a):
        a = a+1
        return a

    def drugi_kotlet(self):
        return self.kotlet(self.zmienna)

a = NewClass(1)
print(a.drugi_kotlet())

class TestNewClass:
    def test_kotlet(self):
        assert kotlet(1) == 2

{
    'komenda': {
        'parametr': 'explain par'
    }
}


# def test_kotlet():
#     assert kotlet(1) == 2
