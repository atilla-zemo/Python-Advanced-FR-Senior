# Exceptions kommen bei Fehlern vor
# z.B.:
# - Falscher Variablenname
# - Division durch 0
# - Man greift auf etwas zu, dass es nicht gibt
# - Falscher Datentyp
# Sorgt dafür, dass das Programm angehalten wird / "abstürzt"

# Fehler abfangen mit try & except - Schema
try:
    pass
    # Code, in dem ein Fehler passieren könnte
except:
    pass
    # Coder, der bei einem Fehler ausgeführt werden soll

# Beispiel
try:
    print("Start code...")
    print(error)
    print("No errors!")
except:
    print("We have an error!")

print("Code after try/except")

# Nur bestimmte Fehler abfangen
# Besser, nicht jeden Fehler blind abzufangen, sondern gezielt
try:
    number = int("Hallo")
except ValueError:
    print("Kann nicht String in Integer umwandeln!")

# Mehrere except-Blöcke
try:
    value = int("Hallo!")
    result = 10 / 0
except ValueError:
    print("Fehler beim Umwandeln!")
except ZeroDivisionError:
    print("Darf nicht durch 0 dividieren")
# except ZeroDivisionError wird nicht durchgeführt, weil beim
# try-block beim ersten Fehler angehalten / abgebrochen wird.

# Mehrere Fehler in einem except
try:
    value = int(input("Gebe eine Zahl ein! "))
except (ValueError, TypeError):
    print("Es gab einen Eingabefehler!")

# Verschachtelte Fehlerbehandlung
# Ein try-Block kann auch in einem anderen try-Block liegen

# Der else-Block
# Struktur
# try:
#   gefährlicher Code
# except:
#   bei Fehler
# else:
#   wenn kein Fehler passiert ist

try:
    number = int(input("Gebe eine Zahl ein! "))
except ValueError:
    print("Fehler bei der Nutzereingabe!")
else:
    print(f"Das Zweifache von {number} ist {number * 2}")

# Der finally-Block
# finally wird immer ausgeführt
try:
    print("Start")
    x = 1 / 0
except ZeroDivisionError:
    print("Fehler wurde abgefangen!")
finally:
    print("Dieser Block läuft immer!")

# Komplettes Beispiel mit allen Blöcken
print("\n\n\nKomplettes Beispiel mit allen Blöcken")
try:
    text = input("Gebe eine Zahl ein: ")
    number = int(text)
except ValueError:
    print("Das war keine Zahl!")
else:
    print("Umwandlung erfolgreich!")
finally:
    print("Einführung in Try/Except beendet!")
