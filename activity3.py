class india:
    def language(self):
        print("Hindi is the national language of India")

    def capital(self):
        print("New Delhi is the capital of India")

    def development(self):
        print("India is a developing country")

class usa:
    def language(self):
        print("English is the national language of USA")

    def capital(self):
        print("Washington DC is the capital of USA")

    def development(self):
        print("USA is a developed country")

obj_ind=india()
obj_usa=usa()

for country in(obj_ind,obj_usa):
    country.language()
    country.capital()
    country.development()