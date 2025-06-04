# Python Cheat Sheet
# Dieses Cheat Sheet fasst die wichtigsten Konzepte aus den von Ihnen gelernten Python-Kursen zusammen. Es soll Ihnen als schnelle Referenz dienen, mit Erklärungen und Beispielen für jedes Thema.


# 1.Hallo Python & Grundlegende Syntax print() Funktion

# Die print()-Funktion wird verwendet, um Ausgaben auf der Konsole anzuzeigen.
# Beschreibung:
# Sie können Zeichenketten (Text), Zahlen oder Variablen ausgeben.
# Beispiel:

print("Hallo Welt!") # Ausgabe einer Zeichenkette
print(123)           # Ausgabe einer Zahl
nachricht = "Python ist toll!"
print(nachricht)     # Ausgabe einer Variablen


# Kommentare
# Kommentare sind Zeilen im Code, die vom Interpreter ignoriert werden. Sie dienen dazu, den Code für Menschen verständlicher zu machen.
# Beschreibung:
# Ein Kommentar beginnt mit einem #-Zeichen.
# Beispiel:

# Dies ist ein einzeiliger Kommentar
x = 10 # Hier wird der Variablen x der Wert 10 zugewiesen


# 2.Arithmetik und Variablen

# Arithmetische Operationen
# Python unterstützt Standard-Rechenoperationen.
# Beschreibung:
# +: Addition
# -: Subtraktion
# *: Multiplikation
# /: Division (ergibt immer eine Gleitkommazahl)
# //: Ganzzahlige Division (ergibt den ganzzahligen Teil des Quotienten)
# %: Modulo (ergibt den Rest einer Division)
# **: Potenzierung
# Beispiel:

ergebnis_add = 5 + 3   # 8
ergebnis_sub = 10 - 4  # 6
ergebnis_mult = 2 * 6  # 12
ergebnis_div = 15 / 4  # 3.75
ergebnis_int_div = 15 // 4 # 3
ergebnis_mod = 15 % 4  # 3 (Rest von 15 geteilt durch 4)
ergebnis_potenz = 2 ** 3 # 8 (2 hoch 3)

print(f"Addition: {ergebnis_add}")
print(f"Subtraktion: {ergebnis_sub}")
print(f"Multiplikation: {ergebnis_mult}")
print(f"Division: {ergebnis_div}")
print(f"Ganzzahlige Division: {ergebnis_int_div}")
print(f"Modulo: {ergebnis_mod}")
print(f"Potenzierung: {ergebnis_potenz}")


# Variablen
# Variablen sind benannte Speicherorte für Werte.
# Beschreibung:
# Sie können Zahlen, Text oder andere Datentypen in Variablen speichern und später darauf zugreifen oder sie ändern.
# Beispiel:

alter = 30
name = "Anna"
preis = 19.99

print(f"{name} ist {alter} Jahre alt und der Preis beträgt {preis} Euro.")

alter = alter + 1 # Wert der Variablen ändern
print(f"Nächstes Jahr ist {name} {alter} Jahre alt.")


# Dynamische Typisierung
# In Python müssen Sie Variablen nicht explizit einen Datentyp zuweisen. Der Typ wird automatisch zur Laufzeit basierend auf dem zugewiesenen Wert bestimmt und kann sich ändern.
# Beispiel:

x = 4      # x ist vom Typ int
x = "Vier" # Jetzt ist x vom Typ str
print(f"Wert von x: {x}, Typ von x: {type(x)}")


# 3.Funktionen

# Funktionen definieren
# Funktionen sind Blöcke von wiederverwendbarem Code, die eine bestimmte Aufgabe ausführen.
# Beschreibung:
# Eine Funktion wird mit dem Schlüsselwort def definiert, gefolgt vom Funktionsnamen, Klammern für Parameter und einem Doppelpunkt.
# Der Funktionskörper ist eingerückt.
# Beispiel:

def gruss(name):
    """
    Diese Funktion gibt einen personalisierten Gruß aus.
    """
    print(f"Hallo, {name}!")

def addiere(a, b):
    """
    Diese Funktion addiert zwei Zahlen und gibt das Ergebnis zurück.
    """
    return a + b


# Funktionen aufrufen
# Um eine Funktion auszuführen, rufen Sie sie mit ihrem Namen und den erforderlichen Argumenten auf.
# Beschreibung:
# Wenn eine Funktion einen Wert zurückgibt (mit return), können Sie diesen Wert in einer Variablen speichern.
# Beispiel:

gruss("Max") # Aufruf der Funktion gruss

summe = addiere(5, 7) # Aufruf der Funktion addiere und Speichern des Ergebnisses
print(f"Die Summe ist: {summe}")


# ```help()` Funktion
# Die `help()`-Funktion gibt die Dokumentation (Docstring) eines Objekts oder einer Funktion aus.
# Beschreibung:
# Nützlich, um zu verstehen, was eine Funktion tut und welche Parameter sie erwartet.
# Beispiel:

help(print)      # Zeigt die Hilfe für die print-Funktion an
help(addiere)    # Zeigt den Docstring der selbstdefinierten addiere-Funktion an


# Eingebaute Funktionen
# Python bietet viele nützliche, bereits integrierte Funktionen, die Sie direkt verwenden können.
# Beschreibung:
# Diese Funktionen sind global verfügbar und müssen nicht importiert werden.
# Beispiel:

print(f"Absoluter Wert von -5: {abs(-5)}")       # => 5
print(f"Gerundeter Wert von 3.1415 auf 2 Dezimalstellen: {round(3.1415, 2)}") # => 3.14
print(f"Länge des Strings 'Hallo': {len('Hallo')}") # => 5


# 4.Datentypen

# Integer (int)
# Ganzzahlen ohne Dezimalstellen.
# Beispiel:

zahl = 10
print(f"Typ von zahl: {type(zahl)}") # <class 'int'>


# Float (float)
# Gleitkommazahlen (Zahlen mit Dezimalstellen).
# Beispiel:

dezimalzahl = 3.14
print(f"Typ von dezimalzahl: {type(dezimalzahl)}") # <class 'float'>


# Boolean (bool)
# Wahrheitswerte: True oder False.
# Beispiel:

ist_wahr = True
ist_falsch = False
print(f"Typ von ist_wahr: {type(ist_wahr)}") # <class 'bool'>


# String (str)
# Zeichenketten (Text).
# Beschreibung:
# Strings werden in einfachen (') oder doppelten (") Anführungszeichen eingeschlossen.
# Beispiel:

text = "Dies ist ein String."
print(f"Typ von text: {type(text)}") # <class 'str'>


# Typüberprüfung
# Überprüfen Sie den Datentyp einer Variablen oder ob ein Objekt eine Instanz eines bestimmten Typs ist.
# Beschreibung:
# type() gibt den Typ eines Objekts zurück. isinstance(obj, typ) prüft, ob obj eine Instanz von typ ist.
# Beispiel:

wert = 3.5
print(f"Typ von 3.5: {type(wert)}") # => <class 'float'>
print(f"Ist 10 eine Instanz von int?: {isinstance(10, int)}") # => True


# Typkonvertierung
# Wandeln Sie Werte von einem Datentyp in einen anderen um.
# Beschreibung:
# Gängige Funktionen sind int(), float(), str(), bool().
# Beispiel:

string_zahl = "5"
ganze_zahl = int(string_zahl)
print(f"'{string_zahl}' als int: {ganze_zahl}, Typ: {type(ganze_zahl)}") # => 5, <class 'int'>

float_zahl = 3.14
string_float = str(float_zahl)
print(f"{float_zahl} als str: '{string_float}', Typ: {type(string_float)}") # => "3.14", <class 'str'>

wahrheitswert_aus_null = bool(0)
print(f"0 als bool: {wahrheitswert_aus_null}, Typ: {type(wahrheitswert_aus_null)}") # => False, <class 'bool'>


# 5.Bedingungen und Bedingte Anweisungen

# if, elif, else
# Steuern den Programmfluss basierend auf Bedingungen.
# Beschreibung:
# if: Führt einen Codeblock aus, wenn die Bedingung True ist.
# elif (else if): Führt einen Codeblock aus, wenn die vorherige if- oder elif-Bedingung False war und diese elif-Bedingung True ist.
# else: Führt einen Codeblock aus, wenn keine der vorherigen if- oder elif-Bedingungen True war.
# Beispiel:

punktzahl = 75

if punktzahl >= 90:
    print("Note: A")
elif punktzahl >= 80:
    print("Note: B")
elif punktzahl >= 70:
    print("Note: C")
else:
    print("Note: D")


# Vergleichsoperatoren
# Werden verwendet, um Werte zu vergleichen.
# Beschreibung:
# ==: Gleich
# !=: Ungleich
# <: Kleiner als
# >: Größer als
# <=: Kleiner oder gleich
# >=: Größer oder gleich
# Beispiel:

x = 10
y = 5

print(f"x == y: {x == y}")   # False
print(f"x != y: {x != y}")   # True
print(f"x > y: {x > y}")     # True
print(f"x <= y: {x <= y}")   # False


# Logische Operatoren
# Werden verwendet, um mehrere Bedingungen zu kombinieren.
# Beschreibung:
# and: True, wenn beide Bedingungen True sind.
# or: True, wenn mindestens eine Bedingung True ist.
# not: Kehrt den Wahrheitswert einer Bedingung um.
# Beispiel:

alter = 25
hat_fuehrerschein = True

if alter >= 18 and hat_fuehrerschein:
    print("Darf Auto fahren.")

if alter < 18 or not hat_fuehrerschein:
    print("Darf kein Auto fahren.")

ist_regen = True
if not ist_regen:
    print("Gehe spazieren.")


# 6.Listen

# Listen erstellen
# Listen sind geordnete, veränderliche Sammlungen von Elementen.
# Beschreibung: Elemente werden in eckigen Klammern [] durch Kommas getrennt.
# Eine Liste kann verschiedene Datentypen enthalten.
# Beispiel:

meine_liste = [1, 2, "drei", True, 4.5]
leere_liste = []


# Indizierung und Slicing
# Zugriff auf einzelne Elemente oder Teilmengen einer Liste.
# Beschreibung:
# Indizierung: Elemente werden über ihren Index (Position) abgerufen, beginnend bei 0 für das erste Element. Negative Indizes zählen vom Ende der Liste (-1 ist das letzte Element).
# Slicing: Erstellt eine neue Liste, die einen Teil der ursprünglichen Liste enthält. Syntax: [start:ende:schritt]. ende ist exklusiv.
# Beispiel:

fruechte = ["Apfel", "Banane", "Kirsche", "Dattel", "Erdbeere"]

print(f"Erstes Element: {fruechte[0]}")     # Apfel
print(f"Letztes Element: {fruechte[-1]}")   # Erdbeere
print(f"Element von Index 1 bis 3 (exkl.): {fruechte[1:4]}") # ['Banane', 'Kirsche', 'Dattel']
print(f"Alle Elemente ab Index 2: {fruechte[2:]}") # ['Kirsche', 'Dattel', 'Erdbeere']
print(f"Alle Elemente bis Index 3 (exkl.): {fruechte[:3]}") # ['Apfel', 'Banane', 'Kirsche']
print(f"Alle Elemente mit Schritt 2: {fruechte[::2]}") # ['Apfel', 'Kirsche', 'Erdbeere']


# Listenmethoden
# Funktionen, die auf Listen angewendet werden können.
# Beschreibung:
# append(element): Fügt ein Element am Ende der Liste hinzu.
# pop(index): Entfernt das Element am angegebenen Index (oder das letzte, wenn kein Index angegeben ist) und gibt es zurück.
# len(liste): Gibt die Anzahl der Elemente in der Liste zurück (keine Methode, sondern eine eingebaute Funktion).
# remove(wert): Entfernt das erste Vorkommen des angegebenen Werts.
# insert(index, element): Fügt ein Element an einem bestimmten Index ein.
# sort(): Sortiert die Liste an Ort und Stelle.
# reverse(): Kehrt die Reihenfolge der Elemente an Ort und Stelle um.
# Beispiel:

zahlen = [1, 5, 2, 8, 3]

zahlen.append(10)      # [1, 5, 2, 8, 3, 10]
print(f"Nach append: {zahlen}")

entferntes_element = zahlen.pop(2) # Entfernt 2, gibt 2 zurück
print(f"Entferntes Element: {entferntes_element}")
print(f"Nach pop: {zahlen}") # [1, 5, 8, 3, 10]

zahlen.remove(8)       # Entfernt das erste Vorkommen von 8
print(f"Nach remove: {zahlen}") # [1, 5, 3, 10]

zahlen.insert(1, 99)   # Fügt 99 an Index 1 ein
print(f"Nach insert: {zahlen}") # [1, 99, 5, 3, 10]

print(f"Länge der Liste: {len(zahlen)}") # 5

zahlen.sort()          # Sortiert die Liste
print(f"Nach sort: {zahlen}") # [1, 3, 5, 10, 99]

zahlen.reverse()       # Kehrt die Liste um
print(f"Nach reverse: {zahlen}") # [99, 10, 5, 3, 1]


# 7.Schleifen und List Comprehensions

# for Schleifen
# Iterieren über Elemente einer Sequenz (z.B. Listen, Strings, Tupel).
# Beschreibung:
# Der Codeblock innerhalb der Schleife wird für jedes Element einmal ausgeführt.
# Beispiel:

zahlen = [1, 2, 3, 4, 5]

print("For-Schleife über eine Liste:")
for zahl in zahlen:
    print(zahl * 2)

print("\nFor-Schleife mit range():")
# range(start, stop, step) erzeugt eine Sequenz von Zahlen
for i in range(3): # 0, 1, 2
    print(i)

for i in range(1, 6, 2): # 1, 3, 5
    print(i)


# ```while` Schleifen
# Führen einen Codeblock aus, solange eine Bedingung `True` ist.
# Beschreibung:
# Es ist wichtig, dass die Bedingung irgendwann `False` wird, um eine Endlosschleife zu vermeiden.
# Beispiel:

zaehler = 0
print("\nWhile-Schleife:")
while zaehler < 5:
    print(zaehler)
    zaehler += 1 # zaehler = zaehler + 1


# List Comprehensions
# Eine prägnante Möglichkeit, neue Listen aus bestehenden Listen zu erstellen.
# Beschreibung:
# Syntax: [ausdruck for element in sequenz if bedingung]
# Die if-Bedingung ist optional.
# Beispiel:

original_zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Quadrate aller Zahlen
quadrate = [zahl**2 for zahl in original_zahlen]
print(f"Quadrate: {quadrate}") # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Nur gerade Zahlen
gerade_zahlen = [zahl for zahl in original_zahlen if zahl % 2 == 0]
print(f"Gerade Zahlen: {gerade_zahlen}") # [2, 4, 6, 8, 10]

# Quadrate nur der geraden Zahlen
quadrate_gerade = [zahl**2 for zahl in original_zahlen if zahl % 2 == 0]
print(f"Quadrate der geraden Zahlen: {quadrate_gerade}") # [4, 16, 36, 64, 100]


# 8.Strings und Dictionaries

# String-Methoden
# Funktionen, die auf Zeichenketten angewendet werden können.
# Beschreibung:
# Strings sind unveränderlich, d.h. String-Methoden geben einen neuen String zurück, anstatt den ursprünglichen zu ändern.
# Beispiel:

text = "  Hallo Welt!  "

print(f"Original: '{text}'")
print(f"Großbuchstaben: '{text.upper()}'") # HALLO WELT!
print(f"Kleinbuchstaben: '{text.lower()}'") #   hallo welt!
print(f"Erster Buchstabe groß: '{text.capitalize()}'") #   hallo welt!
print(f"Leerzeichen entfernen: '{text.strip()}'") # Hallo Welt!
print(f"Ersetzen: '{text.replace('Welt', 'Python')}'") #   Hallo Python!
print(f"Split (nach Leerzeichen): {text.strip().split(' ')}") # ['Hallo', 'Welt!']
print(f"Startet mit 'Hallo': {text.strip().startswith('Hallo')}") # True
print(f"Endet mit '!': {text.strip().endswith('!')}") # True
print(f"Länge: {len(text)}") # 15 (inkl. Leerzeichen)


# f-Strings (Formatted String Literals)
# Eine einfache Möglichkeit, Variablen und Ausdrücke in Strings einzubetten.
# Beschreibung:
# Beginnen Sie den String mit f oder F vor dem öffnenden Anführungszeichen. Variablen und Ausdrücke werden in geschweifte Klammern {} gesetzt.
# Beispiel:

name = "Lisa"
alter = 28
nachricht = f"Mein Name ist {name} und ich bin {alter} Jahre alt."
print(nachricht)

produkt = "Laptop"
preis = 1200.50
mehrwertsteuer = 0.19
gesamtpreis = preis * (1 + mehrwertsteuer)
print(f"Der {produkt} kostet {preis:.2f} Euro. Inklusive Mehrwertsteuer: {gesamtpreis:.2f} Euro.")


# Dictionaries
# Ungeordnete, veränderliche Sammlungen von Schlüssel-Wert-Paaren.
# Beschreibung:
# Jeder Schlüssel muss eindeutig sein. Schlüssel können Strings, Zahlen oder Tupel sein. Werte können beliebige Datentypen sein.
# Beispiel:

person = {
    "name": "Tom",
    "alter": 40,
    "stadt": "Berlin",
    "beruf": "Ingenieur"
}

leeres_dict = {}

print(f"Name der Person: {person['name']}") # Zugriff auf einen Wert

person["alter"] = 41 # Wert ändern
print(f"Neues Alter: {person['alter']}")

person["email"] = "tom@example.com" # Neues Schlüssel-Wert-Paar hinzufügen
print(f"Person mit E-Mail: {person}")

del person["beruf"] # Schlüssel-Wert-Paar entfernen
print(f"Person ohne Beruf: {person}")

print(f"Alle Schlüssel: {person.keys()}")     # dict_keys(['name', 'alter', 'stadt', 'email'])
print(f"Alle Werte: {person.values()}")    # dict_values(['Tom', 41, 'Berlin', 'tom@example.com'])
print(f"Alle Paare: {person.items()}")     # dict_items([('name', 'Tom'), ('alter', 41), ('stadt', 'Berlin'), ('email', 'tom@example.com')])

# Über Dictionaries iterieren
print("\nIterieren über Schlüssel-Wert-Paare:")
for schluessel, wert in person.items():
    print(f"{schluessel}: {wert}")


# Dictionary-Methoden und Operatoren
# Zusätzliche nützliche Methoden und Operatoren für Dictionaries.
# Beschreibung:
# get(key, default): Gibt den Wert für den angegebenen Schlüssel zurück. Wenn der Schlüssel nicht gefunden wird, wird default zurückgegeben (standardmäßig None).
# key in dict: Prüft, ob ein Schlüssel im Dictionary vorhanden ist. Gibt True oder False zurück.
# Beispiel:

person = {"name": "Marvin", "age": 25}

# get() Methode
print(f"Alter der Person (mit get()): {person.get('age')}")       # => 25
print(f"Beruf der Person (nicht vorhanden, mit get()): {person.get('beruf', 'Unbekannt')}") # => Unbekannt

# 'in' Operator
print(f"Ist 'age' in person?: {'age' in person}")          # => True
print(f"Ist 'email' in person?: {'email' in person}")        # => False


# Sets
# Ungeordnete Sammlungen von einzigartigen Elementen.
# Beschreibung:
# Sets sind nützlich, um Duplikate zu entfernen und mathematische Mengenoperationen durchzuführen. Elemente werden in geschweiften Klammern {} oder mit der set()-Funktion erstellt.
# Beispiel:

einzigartig = set([1, 2, 2, 3, 4, 4, 5])
print(f"Set mit einzigartigen Werten: {einzigartig}") # => {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Vereinigung von Set1 und Set2: {set1.union(set2)}")        # => {1, 2, 3, 4, 5}
print(f"Schnittmenge von Set1 und Set2: {set1.intersection(set2)}") # => {3}


# Arbeiten mit externen Bibliotheken

# Bibliotheken importieren
# Um Funktionen aus externen Bibliotheken zu nutzen, müssen diese importiert werden.
# Beschreibung:
# import modulname: Importiert das gesamte Modul. Sie greifen auf Funktionen mit modulname.funktion() zu.
# import modulname as alias: Importiert das Modul und gibt ihm einen kürzeren Alias.
# from modulname import funktion: Importiert eine spezifische Funktion direkt, sodass Sie sie ohne Präfix aufrufen können.
# from modulname import *: Importiert alle Funktionen aus einem Modul. Dies wird im Allgemeinen nicht empfohlen, da es zu Namenskonflikten führen kann.
# Beispiel:

# Beispiel mit dem 'math'-Modul (für mathematische Funktionen)

import math
print(f"Quadratwurzel von 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")

import math as m
print(f"Sinus von 0: {m.sin(0)}")

from math import factorial
print(f"Fakultät von 5: {factorial(5)}") # 5 * 4 * 3 * 2 * 1 = 120

# Beispiel mit dem 'random'-Modul (für Zufallszahlen)
import random
print(f"Zufallszahl zwischen 1 und 10: {random.randint(1, 10)}")
print(f"Zufällige Auswahl aus einer Liste: {random.choice(['Rot', 'Grün', 'Blau'])}")


# Objektorientierte Programmierung (OOP)

# Klassen und Objekte
# OOP ermöglicht die Modellierung von realen Entitäten als Objekte, die Eigenschaften (Attribute) und Verhaltensweisen (Methoden) haben.
# Beschreibung:
# Eine class ist ein Bauplan für Objekte. Ein object ist eine Instanz einer Klasse.
# __init__ ist der Konstruktor, der aufgerufen wird, wenn ein neues Objekt erstellt wird. self bezieht sich auf die aktuelle Instanz des Objekts.
# Beispiel:
class Person:
    def __init__(self, name, alter):
        """
        Konstruktor für die Person-Klasse.
        Initialisiert ein neues Person-Objekt mit einem Namen und Alter.
        """
        self.name = name
        self.alter = alter

    def vorstellen(self):
        """
        Methode, um die Person vorzustellen.
        """
        print(f"Hi, ich bin {self.name} und {self.alter} Jahre alt.")

# Erstellen von Objekten (Instanzen der Klasse Person)
p1 = Person("Marvin", 25)
p2 = Person("Anna", 30)

# Aufrufen von Methoden auf den Objekten
p1.vorstellen() # Hi, ich bin Marvin und 25 Jahre alt.
p2.vorstellen() # Hi, ich bin Anna und 30 Jahre alt.


# Fehlerbehandlung
# try, except
# Fehlerbehandlung ermöglicht es Ihnen, auf Laufzeitfehler (Exceptions) zu reagieren, ohne dass das Programm abstürzt.
# Beschreibung:
# Der Code im try-Block wird ausgeführt. Wenn ein Fehler auftritt, wird die Ausführung unterbrochen und der Code im entsprechenden except-Block ausgeführt.
# Sie können spezifische Fehlertypen abfangen (z.B. ValueError, TypeError).
# Beispiel:
try:
    zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))
    ergebnis = 10 / zahl
    print(f"Das Ergebnis ist: {ergebnis}")
except ValueError:
    print("Fehler: Das war keine gültige Zahl. Bitte geben Sie eine ganze Zahl ein.")
except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt.")
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
finally:
    print("Dieser Block wird immer ausgeführt, unabhängig davon, ob ein Fehler auftrat oder nicht.")


# Dateien Lesen & Schreiben

# Arbeiten mit Dateien
# Python bietet Funktionen zum Lesen und Schreiben von Daten in Dateien.
# Beschreibung:
# open() wird verwendet, um eine Datei zu öffnen. Der erste Parameter ist der Dateiname, der zweite der Modus:
# "w" (write): Zum Schreiben. Erstellt die Datei, wenn sie nicht existiert, oder überschreibt sie, wenn sie existiert.
# "r" (read): Zum Lesen. Die Datei muss existieren.
# "a" (append): Zum Anhängen. Fügt Daten am Ende der Datei hinzu.
# Das with-Statement stellt sicher, dass die Datei nach Gebrauch automatisch geschlossen wird, auch wenn Fehler auftreten.
# Beispiel:
# Schreiben in eine Datei
dateiname = "meine_datei.txt"
inhalt_zum_schreiben = "Hallo Welt!\nDies ist ein Test."

with open(dateiname, "w", encoding="utf-8") as f:
    f.write(inhalt_zum_schreiben)
print(f"'{dateiname}' wurde erfolgreich beschrieben.")

# Lesen aus einer Datei
with open(dateiname, "r", encoding="utf-8") as f:
    gelesener_inhalt = f.read()
print(f"\nInhalt von '{dateiname}':")
print(gelesener_inhalt)

# An eine Datei anhängen
inhalt_zum_anhaengen = "\nEine neue Zeile wurde hinzugefügt."
with open(dateiname, "a", encoding="utf-8") as f:
    f.write(inhalt_zum_anhaengen)
print(f"\n'{dateiname}' wurde erfolgreich aktualisiert (angehängt).")

# Erneut lesen, um den angehängten Inhalt zu sehen
with open(dateiname, "r", encoding="utf-8") as f:
    aktualisierter_inhalt = f.read()
print(f"\nAktualisierter Inhalt von '{dateiname}':")
print(aktualisierter_inhalt)
# Ich hoffe, dieses Cheat Sheet ist nützlich für Sie!
