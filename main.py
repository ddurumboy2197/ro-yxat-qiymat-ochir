class Ro'yhat:
    def __init__(self):
        self.ro'yhat = []

    def qo'sh(self, qiymat):
        self.ro'yhat.append(qiymat)

    def o'chir(self, qiymat):
        if qiymat in self.ro'yhat:
            self.ro'yhat.remove(qiymat)
        else:
            print("Ro'yxatda bunday qiymat yo'q.")

    def ko'r(self):
        return self.ro'yhat

ro'yhat = Ro'yhat()
ro'yhat.qo'sh(1)
ro'yhat.qo'sh(2)
ro'yhat.qo'sh(3)
print(ro'yhat.ko'r())  # [1, 2, 3]
ro'yhat.o'chir(2)
print(ro'yhat.ko'r())  # [1, 3]
ro'yhat.o'chir(4)
print(ro'yhat.ko'r())  # [1, 3]
