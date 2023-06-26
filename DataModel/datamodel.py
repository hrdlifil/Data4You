from enum import Enum

class Adresa:
    mesto:str
    ulice:str
    psc:str
    cislo_popisne:str

    def __init__(self, mesto:str, ulice:str, psc:str, cislo_popisne:str) -> None:
        self.mesto = mesto
        self.ulice = ulice
        self.psc = psc
        self.cislo_popisne = cislo_popisne

class Jmeno:
    krestni_jmeno:str
    prostredni_jmeno:str
    prijmeni:str

    def __init__(self, krestni_jmeno:str, prostredni_jmeno:str, prijmeni:str) -> None:
        self.krestni_jmeno = krestni_jmeno
        self.prostredni_jmeno = prostredni_jmeno
        self.prijmeni = prijmeni

class CisloUctu:
    kod_banky:str
    swift:str
    iban:str
    predcisli:str
    cislo:str

    def __init__(self, kod_banky:str, swift:str, iban:str, predcisli:str, cislo:str) -> None:
        self.kod_banky = kod_banky
        self.swift = swift
        self.iban = iban
        self.predcisli = predcisli
        self.cislo = cislo

class FormaSpoluprace(Enum):
    EXTERNI = 1
    INTERNI = 2

class Pohlavi(Enum):
    ZENA = 1
    MUZ = 2
    JINE = 3

class Zamestnanec:
    jmeno:Jmeno
    cislo_uctu:CisloUctu
    email:str
    identifikacni_cislo:str
    adresa:Adresa
    is_active:bool
    forma_spoluprace:FormaSpoluprace
    pozice:str
    datum_nastupu:str

x = Pohlavi.MUZ
print(x.value)


#Komentar
#Komentar po vymazani suboru 
