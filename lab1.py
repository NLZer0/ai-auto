from experta import *

Questions = {
    1: "Для чего приобретается автомобиль?\n",
    2: "Каков ваш бюджет?\n",
    3: "Какой тип кузова вам нужен?\n",
    4: "«Механика» или «автомат»?\n",
}

Answers = {
    1:  "1 - для поездок по городу\n"
        "2 - для поездок за город\n"
        "3 - для частых путешествий\n",
    
    2:  "1 - Большой\n"
        "2 - Средний\n"
        "3 - Низкий\n",
        
    3:  "1 - Седан\n"
        "2 - Хэтчбек\n"
        "3 - Универсал\n"
        "4 - Минивен\n",
    
    4:  "1 - Механика\n"
        "2 - Автомат\n",
}


class KnowledgeBase(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        #Меры доверия
        self.MD_Hyundai_Solaris = [0]
        self.MD_Volkswagen_Polo  = [0]
        self.MD_Lada_Largus_VP  = [0]
        self.MD_Renault_Logan  = [0]
        self.MD_Lada_Granta  = [0]
        self.MD_Skoda_Octavia = [0]
        self.MD_Kia_Ceed = [0]
        self.MD_Kia_Cerato = [0]
        self.MD_Ford_Focus = [0]
        self.MD_Hyundai_Elantra = [0]
        self.MD_Toyota_Corolla = [0]
        self.MD_MercedesBenz_CLA = [0]
        self.MD_Audi_A3 = [0]
        self.MD_MercedesBenz_A = [0]
        self.MD_Toyota_Camry = [0]
        self.MD_Hyundai_Sonata = [0]
        self.MD_Mazda6 = [0]
        self.MD_Volkswagen_Passat = [0]
        self.MD_BMW_3 = [0]
        self.MD_MercedesBenz_C = [0]
        self.MD_Audi_A4 = [0]
        self.MD_Genesis_G70 = [0]
        self.MD_BMW_5 = [0]
        self.MD_MercedesBenz_E = [0]
        self.MD_BMW_7 = [0]
        self.MD_MercedesMaybach = [0]
        self.MD_Volkswagen_Multivan = [0]
        self.MD_Hyundai_H1 = [0]
        self.MD_MercedesBenz_V = [0]

        #Массивы мер доверия
        self.MD_11 = [
            self.MD_Hyundai_Solaris,
            self.MD_Volkswagen_Polo,
            self.MD_Renault_Logan,
            self.MD_Lada_Granta,
            self.MD_Kia_Cerato,
            self.MD_Toyota_Corolla,
            self.MD_MercedesBenz_CLA,
            self.MD_Toyota_Camry,
            self.MD_Hyundai_Sonata,
            self.MD_Mazda6,
            self.MD_Volkswagen_Passat,
            self.MD_BMW_3,
            self.MD_MercedesBenz_C,
            self.MD_Audi_A4,
            self.MD_Genesis_G70,
            self.MD_BMW_5,
            self.MD_MercedesBenz_E,
            self.MD_BMW_7,
            self.MD_MercedesMaybach
        ]
        self.MD_12 = [
            self.MD_Skoda_Octavia,
            self.MD_Lada_Largus_VP,
            self.MD_Kia_Ceed,
            self.MD_Ford_Focus,
            self.MD_Hyundai_Elantra,
            self.MD_Audi_A3
        ]
        self.MD_13 = [
            self.MD_Volkswagen_Multivan,
            self.MD_Hyundai_H1,
            self.MD_MercedesBenz_V,
        ]
        self.MD_21 = [
            self.MD_MercedesBenz_CLA,
            self.MD_MercedesBenz_A,
            self.MD_Genesis_G70,
            self.MD_MercedesBenz_E,
            self.MD_BMW_7,
            self.MD_MercedesMaybach,
            self.MD_MercedesBenz_V
        ]
        self.MD_22 = [
            self.MD_Skoda_Octavia,
            self.MD_Kia_Ceed,
            self.MD_Kia_Cerato,
            self.MD_Ford_Focus,
            self.MD_Toyota_Corolla,
            self.MD_Audi_A3,
            self.MD_Toyota_Camry,
            self.MD_Hyundai_Sonata,
            self.MD_Mazda6,
            self.MD_BMW_3,
            self.MD_MercedesBenz_C,
            self.MD_Audi_A4,
            self.MD_BMW_5,
            self.MD_Hyundai_H1,
        ]
        self.MD_23 = [
            self.MD_Hyundai_Solaris,
            self.MD_Volkswagen_Polo,
            self.MD_Lada_Largus_VP,
            self.MD_Renault_Logan,
            self.MD_Lada_Granta,
            self.MD_Hyundai_Elantra,
            self.MD_Volkswagen_Passat,
            self.MD_Volkswagen_Multivan
        ]
        self.MD_31 = [
            self.MD_Hyundai_Solaris,
            self.MD_Volkswagen_Polo,
            self.MD_Lada_Granta,
            self.MD_Kia_Cerato,
            self.MD_Hyundai_Elantra,
            self.MD_Toyota_Corolla,
            self.MD_MercedesBenz_CLA,
            self.MD_Audi_A3,
            self.MD_MercedesBenz_A,
            self.MD_Toyota_Camry,
            self.MD_Hyundai_Sonata,
            self.MD_Mazda6,
            self.MD_BMW_3,
            self.MD_MercedesBenz_C,
            self.MD_Audi_A4,
            self.MD_Genesis_G70,
            self.MD_BMW_5,
            self.MD_MercedesBenz_E,
            self.MD_BMW_7,
            self.MD_MercedesMaybach,
        ]
        self.MD_32 = [
            self.MD_Hyundai_Elantra,
            self.MD_Toyota_Corolla,
            self.MD_Mazda6,
            self.MD_Volkswagen_Passat,
        ]
        self.MD_33 = [
            self.MD_Lada_Largus_VP,
            self.MD_Renault_Logan,
            self.MD_Skoda_Octavia,
            self.MD_Kia_Ceed,
            self.MD_Hyundai_Elantra,
            self.MD_Toyota_Corolla,
            self.MD_Mazda6,
            self.MD_Volkswagen_Passat,
            self.MD_Audi_A4,
            self.MD_BMW_5,
        ]
        self.MD_34 = [
            self.MD_Volkswagen_Multivan,
            self.MD_Hyundai_H1,
            self.MD_MercedesBenz_V,
        ]
        self.MD_41 = [
            self.MD_Lada_Largus_VP ,
            self.MD_Lada_Granta,
        ]
        self.MD_42 = [
            self.MD_Hyundai_Solaris,
            self.MD_Volkswagen_Polo ,
            self.MD_Renault_Logan ,
            self.MD_Skoda_Octavia,
            self.MD_Kia_Ceed,
            self.MD_Kia_Cerato,
            self.MD_Ford_Focus,
            self.MD_Hyundai_Elantra,
            self.MD_Toyota_Corolla,
            self.MD_MercedesBenz_CLA,
            self.MD_Audi_A3,
            self.MD_MercedesBenz_A,
            self.MD_Toyota_Camry,
            self.MD_Hyundai_Sonata,
            self.MD_Mazda6,
            self.MD_Volkswagen_Passat,
            self.MD_BMW_3,
            self.MD_MercedesBenz_C,
            self.MD_Audi_A4,
            self.MD_Genesis_G70,
            self.MD_BMW_5,
            self.MD_MercedesBenz_E,
            self.MD_BMW_7,
            self.MD_MercedesMaybach,
            self.MD_Volkswagen_Multivan,
            self.MD_Hyundai_H1,
            self.MD_MercedesBenz_V,
        ]


        #Меры недоверия
        self.MDN_Hyundai_Solaris = [0]
        self.MDN_Volkswagen_Polo  = [0]
        self.MDN_Lada_Largus_VP  = [0]
        self.MDN_Renault_Logan  = [0]
        self.MDN_Lada_Granta  = [0]
        self.MDN_Skoda_Octavia = [0]
        self.MDN_Kia_Ceed = [0]
        self.MDN_Kia_Cerato = [0]
        self.MDN_Ford_Focus = [0]
        self.MDN_Hyundai_Elantra = [0]
        self.MDN_Toyota_Corolla = [0]
        self.MDN_MercedesBenz_CLA = [0]
        self.MDN_Audi_A3 = [0]
        self.MDN_MercedesBenz_A = [0]
        self.MDN_Toyota_Camry = [0]
        self.MDN_Hyundai_Sonata = [0]
        self.MDN_Mazda6 = [0]
        self.MDN_Volkswagen_Passat = [0]
        self.MDN_BMW_3 = [0]
        self.MDN_MercedesBenz_C = [0]
        self.MDN_Audi_A4 = [0]
        self.MDN_Genesis_G70 = [0]
        self.MDN_BMW_5 = [0]
        self.MDN_MercedesBenz_E = [0]
        self.MDN_BMW_7 = [0]
        self.MDN_MercedesMaybach = [0]
        self.MDN_Volkswagen_Multivan = [0]
        self.MDN_Hyundai_H1 = [0]
        self.MDN_MercedesBenz_V = [0]


        #Массивы мер недоверия
        self.MDN_11 = [
            self.MDN_Lada_Largus_VP,
            self.MDN_Kia_Ceed,
            self.MDN_Ford_Focus,
            self.MDN_Hyundai_Elantra,
            self.MDN_Audi_A3,
            self.MDN_Volkswagen_Multivan,
            self.MDN_Hyundai_H1,
            self.MDN_MercedesBenz_V,
            self.MDN_Skoda_Octavia,
        ]
        self.MDN_12 = [
            self.MDN_Hyundai_Solaris,
            self.MDN_Volkswagen_Polo,
            self.MDN_Renault_Logan,
            self.MDN_Lada_Granta,
            self.MDN_Kia_Cerato,
            self.MDN_Toyota_Corolla,
            self.MDN_MercedesBenz_CLA,
            self.MDN_Toyota_Camry,
            self.MDN_Hyundai_Sonata,
            self.MDN_Mazda6,
            self.MDN_Volkswagen_Passat,
            self.MDN_BMW_3,
            self.MDN_MercedesBenz_C,
            self.MDN_Audi_A4,
            self.MDN_Genesis_G70,
            self.MDN_BMW_5,
            self.MDN_MercedesBenz_E,
            self.MDN_BMW_7,
            self.MDN_MercedesMaybach,
            self.MDN_Volkswagen_Multivan,
            self.MDN_Hyundai_H1,
            self.MDN_MercedesBenz_V
        ]
        self.MDN_13 = [
            self.MDN_Skoda_Octavia,
            self.MDN_Hyundai_Solaris,
            self.MDN_Volkswagen_Polo,
            self.MDN_Renault_Logan,
            self.MDN_Lada_Granta,
            self.MDN_Skoda_Octavia,
            self.MDN_Kia_Cerato,
            self.MDN_Toyota_Corolla,
            self.MDN_MercedesBenz_CLA,
            self.MDN_Toyota_Camry,
            self.MDN_Hyundai_Sonata,
            self.MDN_Mazda6,
            self.MDN_Volkswagen_Passat,
            self.MDN_BMW_3,
            self.MDN_MercedesBenz_C,
            self.MDN_Audi_A4,
            self.MDN_Genesis_G70,
            self.MDN_BMW_5,
            self.MDN_MercedesBenz_E,
            self.MDN_BMW_7,
            self.MDN_MercedesMaybach,
            self.MDN_Lada_Largus_VP,
            self.MDN_Kia_Ceed,
            self.MDN_Ford_Focus,
            self.MDN_Hyundai_Elantra,
            self.MDN_Audi_A3
        ]
        self.MDN_23 = [
            self.MDN_Skoda_Octavia,
            self.MDN_Kia_Ceed,
            self.MDN_Kia_Cerato,
            self.MDN_Ford_Focus,
            self.MDN_Toyota_Corolla,
            self.MDN_Audi_A3,
            self.MDN_Toyota_Camry,
            self.MDN_Hyundai_Sonata,
            self.MDN_Mazda6,
            self.MDN_BMW_3,
            self.MDN_MercedesBenz_C,
            self.MDN_Audi_A4,
            self.MDN_BMW_5,
            self.MDN_MercedesBenz_CLA,
            self.MDN_Hyundai_H1,
            self.MDN_MercedesBenz_A,
            self.MDN_Genesis_G70,
            self.MDN_MercedesBenz_E,
            self.MDN_BMW_7,
            self.MDN_MercedesMaybach,
            self.MDN_MercedesBenz_V
        ]
        self.MDN_22 = [
            self.MDN_Hyundai_Solaris,
            self.MDN_Volkswagen_Polo,
            self.MDN_Lada_Largus_VP,
            self.MDN_Renault_Logan,
            self.MDN_Lada_Granta,
            self.MDN_Hyundai_Elantra,
            self.MDN_Volkswagen_Passat,
            self.MDN_Volkswagen_Multivan,
            self.MDN_MercedesBenz_CLA,
            self.MDN_MercedesBenz_A,
            self.MDN_Genesis_G70,
            self.MDN_MercedesBenz_E,
            self.MDN_BMW_7,
            self.MDN_MercedesMaybach,
            self.MDN_MercedesBenz_V
        ]
        self.MDN_21 = [
            self.MDN_Hyundai_Solaris,
            self.MDN_Volkswagen_Polo,
            self.MDN_Lada_Largus_VP,
            self.MDN_Renault_Logan,
            self.MDN_Lada_Granta,
            self.MDN_Hyundai_Elantra,
            self.MDN_Volkswagen_Passat,
            self.MDN_Volkswagen_Multivan,
            self.MDN_Skoda_Octavia,
            self.MDN_Kia_Ceed,
            self.MDN_Kia_Cerato,
            self.MDN_Ford_Focus,
            self.MDN_Toyota_Corolla,
            self.MDN_Audi_A3,
            self.MDN_Toyota_Camry,
            self.MDN_Hyundai_Sonata,
            self.MDN_Mazda6,
            self.MDN_BMW_3,
            self.MDN_MercedesBenz_C,
            self.MDN_Audi_A4,
            self.MDN_BMW_5,
            self.MDN_Hyundai_H1,
        ]    
        self.MDN_31 = [
            self.MDN_Lada_Largus_VP,
            self.MDN_Skoda_Octavia,
            self.MDN_Kia_Ceed,
            self.MDN_Ford_Focus,
            self.MDN_Volkswagen_Multivan,
            self.MDN_Hyundai_H1,
            self.MDN_MercedesBenz_V,
        ]
        self.MDN_32 = [
            self.MDN_Hyundai_Solaris,
            self.MDN_Volkswagen_Polo ,
            self.MDN_Lada_Largus_VP ,
            self.MDN_Renault_Logan ,
            self.MDN_Lada_Granta ,
            self.MDN_Skoda_Octavia,
            self.MDN_Kia_Ceed,
            self.MDN_Kia_Cerato,
            self.MDN_Ford_Focus,
            self.MDN_MercedesBenz_CLA,
            self.MDN_Audi_A3,
            self.MDN_MercedesBenz_A,
            self.MDN_Toyota_Camry,
            self.MDN_Hyundai_Sonata,
            self.MDN_BMW_3,
            self.MDN_MercedesBenz_C,
            self.MDN_Audi_A4,
            self.MDN_Genesis_G70,
            self.MDN_BMW_5,
            self.MDN_MercedesBenz_E,
            self.MDN_BMW_7,
            self.MDN_MercedesMaybach,
            self.MDN_Volkswagen_Multivan,
            self.MDN_Hyundai_H1,
            self.MDN_MercedesBenz_V,
        ]
        self.MDN_33 = [
            self.MDN_Hyundai_Solaris,
            self.MDN_Volkswagen_Polo ,
            self.MDN_Lada_Granta ,
            self.MDN_Kia_Cerato,
            self.MDN_Ford_Focus,
            self.MDN_MercedesBenz_CLA,
            self.MDN_Audi_A3,
            self.MDN_MercedesBenz_A,
            self.MDN_Toyota_Camry,
            self.MDN_Hyundai_Sonata,
            self.MDN_BMW_3,
            self.MDN_MercedesBenz_C,
            self.MDN_Genesis_G70,
            self.MDN_MercedesBenz_E,
            self.MDN_BMW_7,
            self.MDN_MercedesMaybach,
            self.MDN_Volkswagen_Multivan,
            self.MDN_Hyundai_H1,
            self.MDN_MercedesBenz_V,
        ]
        self.MDN_34 = [
            self.MDN_Hyundai_Solaris,
            self.MDN_Volkswagen_Polo ,
            self.MDN_Lada_Largus_VP ,
            self.MDN_Renault_Logan ,
            self.MDN_Lada_Granta ,
            self.MDN_Skoda_Octavia,
            self.MDN_Kia_Ceed,
            self.MDN_Kia_Cerato,
            self.MDN_Ford_Focus,
            self.MDN_Hyundai_Elantra,
            self.MDN_Toyota_Corolla,
            self.MDN_MercedesBenz_CLA,
            self.MDN_Audi_A3,
            self.MDN_MercedesBenz_A,
            self.MDN_Toyota_Camry,
            self.MDN_Hyundai_Sonata,
            self.MDN_Mazda6,
            self.MDN_Volkswagen_Passat,
            self.MDN_BMW_3,
            self.MDN_MercedesBenz_C,
            self.MDN_Audi_A4,
            self.MDN_Genesis_G70,
            self.MDN_BMW_5,
            self.MDN_MercedesBenz_E,
            self.MDN_BMW_7,
            self.MDN_MercedesMaybach,
        ]
        self.MDN_41 = [
            self.MDN_Hyundai_Solaris,
            self.MDN_Volkswagen_Polo ,
            self.MDN_Renault_Logan ,
            self.MDN_Skoda_Octavia,
            self.MDN_Kia_Ceed,
            self.MDN_Kia_Cerato,
            self.MDN_Ford_Focus,
            self.MDN_Hyundai_Elantra,
            self.MDN_Toyota_Corolla,
            self.MDN_MercedesBenz_CLA,
            self.MDN_Audi_A3,
            self.MDN_MercedesBenz_A,
            self.MDN_Toyota_Camry,
            self.MDN_Hyundai_Sonata,
            self.MDN_Mazda6,
            self.MDN_Volkswagen_Passat,
            self.MDN_BMW_3,
            self.MDN_MercedesBenz_C,
            self.MDN_Audi_A4,
            self.MDN_Genesis_G70,
            self.MDN_BMW_5,
            self.MDN_MercedesBenz_E,
            self.MDN_BMW_7,
            self.MDN_MercedesMaybach,
            self.MDN_Volkswagen_Multivan,
            self.MDN_Hyundai_H1,
            self.MDN_MercedesBenz_V,
        ]
        self.MDN_42 = [
            self.MDN_Lada_Largus_VP ,
            self.MDN_Lada_Granta,
        ]
        
    @Rule(
        Fact(answ="1-1"))
    def _11(self):
        for it in self.MD_11:
            it[0] = it[0] + 0.2*(1-it[0])
        for it in self.MDN_12:
            it[0] = it[0] + 0.2*(1-it[0])
        for it in self.MDN_13:
            it[0] = it[0] + 0.2*(1-it[0])
    @Rule(
        Fact(answ="1-2"))
    def _12(self):
        for it in self.MDN_11:
            it[0] = it[0] + 0.2*(1-it[0])
        for it in self.MD_12:
            it[0] = it[0] + 0.2*(1-it[0])
        for it in self.MDN_13:
            it[0] = it[0] + 0.2*(1-it[0])
    @Rule(
        Fact(answ="1-3"))
    def _13(self):
        for it in self.MDN_11:
            it[0] = it[0] + 0.2*(1-it[0])
        for it in self.MDN_12:
            it[0] = it[0] + 0.2*(1-it[0])
        for it in self.MD_13:
            it[0] = it[0] + 0.2*(1-it[0])


    @Rule(
        Fact(answ="2-1"))
    def _21(self):
        for it in self.MD_21:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_22:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_23:
            it[0] = it[0] + 0.5*(1-it[0])
    @Rule(
        Fact(answ="2-2"))
    def _22(self):
        for it in self.MDN_21:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MD_22:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_23:
            it[0] = it[0] + 0.5*(1-it[0])       
    @Rule(
        Fact(answ="2-3"))
    def _23(self):
        for it in self.MDN_21:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_22:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MD_23:
            it[0] = it[0] + 0.5*(1-it[0])   
    


    @Rule(
        Fact(answ="3-1"))
    def _31(self):
        for it in self.MD_31:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_32:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_33:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_34:
            it[0] = it[0] + 0.5*(1-it[0])  
    @Rule(
        Fact(answ="3-2"))
    def _32(self):
        for it in self.MDN_31:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MD_32:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_33:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_34:
            it[0] = it[0] + 0.5*(1-it[0])  
    @Rule(
        Fact(answ="3-3"))
    def _33(self):
        for it in self.MDN_31:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_32:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MD_33:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_34:
            it[0] = it[0] + 0.5*(1-it[0])  
    @Rule(
        Fact(answ="3-4"))
    def _34(self):
        for it in self.MDN_31:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_32:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MDN_33:
            it[0] = it[0] + 0.5*(1-it[0])
        for it in self.MD_34:
            it[0] = it[0] + 0.5*(1-it[0])  
        

    @Rule(
        Fact(answ="4-1"))
    def _41(self):
        for it in self.MD_41:
            it[0] = it[0] + 0.2*(1-it[0])
        for it in self.MDN_42:
            it[0] = it[0] + 0.2*(1-it[0])
    @Rule(
        Fact(answ="4-2"))
    def _42(self):
        for it in self.MDN_41:
            it[0] = it[0] + 0.2*(1-it[0])
        for it in self.MD_42:
            it[0] = it[0] + 0.2*(1-it[0])


    #Вспомогательные методы
    def getKU(self):
        tmp_list = {
            "Hyundai Solari" : self.MD_Hyundai_Solaris[0] - self.MDN_Hyundai_Solaris[0] ,
            "Volkswagen Polo" : self.MD_Volkswagen_Polo [0] - self.MDN_Volkswagen_Polo[0]  ,
            "Lada Largus VP" : self.MD_Lada_Largus_VP [0] - self.MDN_Lada_Largus_VP[0]  ,
            "Renault Logan" : self.MD_Renault_Logan [0] - self.MDN_Renault_Logan[0]  ,
            "Lada Granta" : self.MD_Lada_Granta [0] - self.MDN_Lada_Granta[0]  ,
            "Skoda Octavia" : self.MD_Skoda_Octavia[0] - self.MDN_Skoda_Octavia[0] ,
            "Kia Ceed" : self.MD_Kia_Ceed[0] - self.MDN_Kia_Ceed[0] ,
            "Kia Cerato" : self.MD_Kia_Cerato[0] - self.MDN_Kia_Cerato[0] ,
            "Ford Focus" : self.MD_Ford_Focus[0] - self.MDN_Ford_Focus[0] ,
            "Hyundai Elantra" : self.MD_Hyundai_Elantra[0] - self.MDN_Hyundai_Elantra[0] ,
            "Toyota Corolla" : self.MD_Toyota_Corolla[0] - self.MDN_Toyota_Corolla[0] ,
            "MercedesBenz CLA" : self.MD_MercedesBenz_CLA[0] - self.MDN_MercedesBenz_CLA[0] ,
            "Audi A3" : self.MD_Audi_A3[0] - self.MDN_Audi_A3[0],
            "MercedesBenz A" : self.MD_MercedesBenz_A[0] - self.MDN_MercedesBenz_A[0] ,
            "Toyota Camry" : self.MD_Toyota_Camry[0] - self.MDN_Toyota_Camry[0] ,
            "Hyundai Sonata" : self.MD_Hyundai_Sonata[0] - self.MDN_Hyundai_Sonata[0] ,
            "Mazda 6" : self.MD_Mazda6[0] - self.MDN_Mazda6[0] ,
            "Volkswagen Passat" : self.MD_Volkswagen_Passat[0] - self.MDN_Volkswagen_Passat[0] ,
            "BMW 3" : self.MD_BMW_3[0] - self.MDN_BMW_3[0] ,
            "MercedesBenz C" : self.MD_MercedesBenz_C[0] - self.MDN_MercedesBenz_C[0] ,
            "Audi A4" : self.MD_Audi_A4[0] - self.MDN_Audi_A4[0] ,
            "Genesis G70" : self.MD_Genesis_G70[0] - self.MDN_Genesis_G70[0] ,
            "BMW 5" : self.MD_BMW_5[0] - self.MDN_BMW_5[0] ,
            "MercedesBenz E" : self.MD_MercedesBenz_E[0] - self.MDN_MercedesBenz_E[0] ,
            "BMW 7" : self.MD_BMW_7[0] - self.MDN_BMW_7[0] ,
            "Mercedes Maybach" : self.MD_MercedesMaybach[0] - self.MDN_MercedesMaybach[0] ,
            "Volkswagen Multivan" : self.MD_Volkswagen_Multivan[0] - self.MDN_Volkswagen_Multivan[0] ,
            "Hyundai H1" : self.MD_Hyundai_H1[0] - self.MDN_Hyundai_H1[0] ,
            "MercedesBenz V" : self.MD_MercedesBenz_V[0] - self.MDN_MercedesBenz_V[0] ,
        }
        return tmp_list
                    
    def check_auto(self):
        ku = self.getKU()
        max = -1
        key = ""
        for res in ku:
            if ku[res] > max:
                max = ku[res]
                key = res

        return key, max


KBase = KnowledgeBase()
KBase.reset() # Prepare the engine for the execution.

for ThisKey in Questions:
    print(Questions[ThisKey])
    x = str(input(Answers[ThisKey]))
    ans = str(ThisKey) + "-" + x
    KBase.declare(Fact(answ=ans))
    KBase.run()

check = KBase.check_auto()

print("Вам подходит : " + check[0])