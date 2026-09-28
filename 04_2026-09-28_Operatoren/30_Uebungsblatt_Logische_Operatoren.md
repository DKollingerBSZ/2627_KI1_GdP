# Übungsblatt: Logische Operatoren `and` und `or` in Python

Mit `and` und `or` kannst du mehrere Bedingungen miteinander verknüpfen.

- `and`: Das Gesamtergebnis ist nur dann `True`, wenn **beide** Bedingungen `True` sind.
- `or`: Das Gesamtergebnis ist `True`, wenn **mindestens eine** Bedingung `True` ist.

**Arbeitsweise:** Sage vor jeder Aufgabe voraus, ob `True` oder `False` ausgegeben wird. Schreibe anschließend ein kleines Python-Programm, führe es aus und überprüfe deine Vermutung.

## 1. Optional: Einzelne Bedingungen verknüpfen

1. Erstelle zwei Variablen:
   ```python
   sonnig = True
   warm = True
   ```
   Prüfe mit `and`, ob es sonnig **und** warm ist.

2. Ändere `warm` auf `False`. Welche Ausgabe erwartest du? Teste das Programm erneut.

3. Erstelle die Variablen:
   ```python
   hungrig = False
   durstig = True
   ```
   Prüfe mit `or`, ob die Person hungrig **oder** durstig ist.

4. Setze beide Variablen auf `False`. Welche Ausgabe erzeugt `hungrig or durstig`?

## 2. Aufgaben mit Zahlen

Speichere die Ergebnisse jeweils in einer Variablen namens `ergebnis` und gib sie aus.

5. Prüfe, ob eine Zahl zwischen 10 und 20 liegt. Verwende dafür `and`.

6. Prüfe, ob eine Zahl kleiner als 0 **oder** größer als 100 ist. Verwende dafür `or`.

7. Prüfe, ob eine Person mindestens 16 Jahre alt ist und einen Ausweis besitzt. Verwende die Variablen:
    ```python
    alter = 17
    hat_ausweis = True
    ```

8. Prüfe, ob eine Person einen Rabatt bekommt, wenn sie unter 18 **oder** über 65 Jahre alt ist.

## 3. Aufgaben mit `input()`

Lies die benötigten Werte mit `input()` ein. Wandle Zahlen mit `int()` um und wandle die Eingaben `ja` und `nein` in passende Wahrheitswerte um.

9. **Einlass:** Frage nach dem Alter und danach, ob eine Eintrittskarte vorhanden ist. Der Einlass ist erlaubt, wenn die Person mindestens 16 Jahre alt **und** eine Eintrittskarte vorhanden ist.

10. **Freier Eintritt:** Frage nach dem Alter. Freien Eintritt erhalten Kinder unter 6 Jahren **oder** Personen ab 65 Jahren.

11. **Passwort prüfen:** Lies einen Benutzernamen und ein Passwort ein. Gib nur dann `True` aus, wenn der Benutzername `admin` **und** das Passwort `python123` lautet.

12. **Notfallkontakt:** Frage, ob jemand telefonisch **oder** per E-Mail erreichbar ist. Gib aus, ob mindestens eine Kontaktmöglichkeit vorhanden ist.

## 4. Kombinierte Bedingungen

13. Lies eine Punktzahl ein. Eine Prüfung ist bestanden, wenn die Punktzahl mindestens 50 beträgt und höchstens 100 beträgt.

14. Lies eine Temperatur ein. Gib aus, ob eine Warnung nötig ist, wenn die Temperatur unter 0 Grad **oder** über 35 Grad liegt.

15. Überlege zuerst, welche Bedingung zuerst ausgewertet wird. Bestimme anschließend die Ausgabe:
    ```python
    a = True
    b = False
    c = True

    print(a and b or c)
    print(a or b and c)
    ```

16. Setze in der vorherigen Aufgabe passende Klammern. Prüfe, ob diese Ausdrücke dasselbe Ergebnis liefern:
    ```python
    (a and b) or c
    a or (b and c)
    ```

##  Optional: Zusatzaufgabe

17. Schreibe ein kleines Programm für eine Tür. Die Tür öffnet sich, wenn eine gültige Karte **und** der richtige PIN eingegeben wurden. Zusätzlich soll sich die Tür im Notfall öffnen, wenn der Notfallknopf gedrückt wurde. Verwende dafür `and`, `or` und verständliche Ausgaben.
