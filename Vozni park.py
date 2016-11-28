class Avto(object):
    def __init__(self, znamka, model, km_num, serv_year):
        self.znamka = znamka
        self.model = model
        self.km_num = km_num
        self.serv_year = serv_year

def full_spec(self):
    return self.znamka + " " + self.model + " " + self.km_num + " " + serv_year

vozilo_1 = Avto(znamka="bmw", model="320i", km_num="100000", serv_year="2000")
vozilo_2 = Avto(znamka="zastava", model="yugo", km_num="150000", serv_year="1985")
vozilo_3 = Avto(znamka="reanult", model="clio", km_num="75000", serv_year="2005")
vozilo_4 = Avto(znamka="fiat", model="tipo", km_num="123000", serv_year="2011")

vozila = [vozilo_1, vozilo_2, vozilo_3, vozilo_4]


for vehicle in vozila:
    print vehicle.full_spec()