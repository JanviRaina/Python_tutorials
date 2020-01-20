class Dad:
    basketball=1
class Son(Dad):
    basketball=7
    dance=1
    def isDance(self):
        return f"I can dance {self.dance} no. of times"
class Grandson(Son):
    dance=6
    # def isDance(self):
    #     return f"Jackson YEAH!" \
    #     f"I can dance {self.dance} no. of times"

darry=Dad()
larry=Son()
Harry=Grandson()

print(Harry.isDance())
print(Harry.basketball)