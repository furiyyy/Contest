from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
kwargsAcceptFun(name="Furi")


result = typeBasedTransformer(
    number=4,
    text="Salom",
    flag=True,
    numbers_list=[1, 2, 3],
    info={"a": 1, "b": 2}
)

print(result)

