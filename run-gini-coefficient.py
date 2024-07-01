from money_model import MoneyModel

model = MoneyModel(100, 10, 10)
for i in range(100):
    model.step()

