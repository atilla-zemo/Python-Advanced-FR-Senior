# Exceptions erheben
# raise
# Wir können selbst einen Fehler erstellen
def checker(text):
    if type(text) != str:
        raise TypeError(
            f"Sorry, wir können nicht mit {type(text)} arbeiten"
            f", wir brauchen nämlich die Klasse str!")
    else:
        return text

checker(123)

