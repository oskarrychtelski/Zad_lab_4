#zad.1
# liczby=[i for i in range(50) if i%4==0]
# print(liczby)
# plik=open("dane.txt","w+")
# plik.writelines(str(liczby))
# plik.close()

#zad.2
# plik=open("dane.txt","r")
# print(plik.readlines())
# plik.close()

#zad.3
# with open("tekst.txt","w") as plik:
#         plik.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
# with open("tekst.txt","r") as plik:
#     for linia in plik:
#         print(linia,end="")

#zad.4
# class NaZakupy:
#     def __init__(self,nazwaproduktu,ilosc,jednostka_miary,cena_jed):
#         self.nazwaproduktu=nazwaproduktu
#         self.ilosc=ilosc
#         self.jednostka_miary=jednostka_miary
#         self.cena_jed=cena_jed
#     def wyświetl_produkt(self):
#         print (f"nazwa: ",self.nazwaproduktu,"\nilosc: ",self.ilosc,"\njednostka miary: ",self.jednostka_miary,"\ncena jednostkowa: ",self.cena_jed)
#     def ile_produktu(self):
#         print(self.ilosc,self.jednostka_miary)
#     def ile_kosztuje(self):
#         print(3*self.cena_jed)
# x=NaZakupy("Andrzej jestem", "30", "cm.", "odpowiednio")
# x.ile_kosztuje()
# x.ile_produktu()
# x.wyświetl_produkt()


#zad.5
class ciagi:
    a1=0
    r=0
    n=0
    def wyswietl_dane(self):
        print(f"pierwszy wyraz:", self.a1, "roznica: ", self.r, "ile wyrazow: ", self.ile)
    def pobierz_parametry(self,a1,r,n):
        self.a1=a1
        self.r=r
        self.n=n
    def pobierz_elementy(self):
        elementy=[element for element in input("Podaj dowolna ilosc elementow ciagu: ")]
        print(elementy)
    def policz_sume(self):
        suma=0
        for element in elementy:
            suma+=element
        print(suma)
    def policz_elementy(self):
        i=0
        if n>1:
            an = a1 + r
            while i==n:
                an+=r
                i+=1
            print(an)
        else:
            print(a1)



#Przepraszam że nie dokończyłem, ale w ten weekend się przeprowadzałem o 250km. Pochłonęlo mi to naprawdę mnóstwo czasu. Mam nadzieję, że to nie jest duży problem.