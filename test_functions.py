
from functions import salary, hello_who
def test_hello_who_max():
    assert hello_who("Max") == "Hello, Max"


def test_hello_who_other():
    assert hello_who("Lto") == "Hello, Lto"
    assert hello_who("Other") == "Hello, Other"
    assert hello_who("Kate") == "Hello, Kate"

def test_salaty():
    assert salary(2,2) == 8
    assert salary(3,1)== 6
