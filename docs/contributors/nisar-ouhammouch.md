[← Contributors](README.md)

# Nisar Ouhammouch , Matrikelnr.: 

## Meta-Goals

### Target grade

2,0

### Personal goals

In diesem Projekt möchte ich lernen, ein relationales Datenmodell zu entwerfen und eine REST-API mit JSON bereitzustellen. Ich will verstehen, wie Tabellen wie Nutzer, Schichten und Buchungen sinnvoll miteinander verknüpft werden und wie die App diese Daten über eine saubere Schnittstelle ausliefert.
Außerdem möchte ich sicher mit Git im Team arbeiten können, also mit Branches, Pull Requests und dem Lösen von Merge-Konflikten. Dieses Wissen will ich später im Praktikum und im Beruf nutzen, um mich schnell in bestehende Projekte und Teams einzuarbeiten.

### Vertical features

#### Schichten anfragen und Buchungen verwalten (Studierende & Unternehmen)

Datenmodell für Buchungen: Verknüpfung von Studierenden und Schichten mit Status (angefragt, bestätigt, abgelehnt)
Studierende fragen eine offene Schicht an und sehen ihre Anfragen mit Status in einer Übersicht
Unternehmen sehen eingegangene Anfragen zu ihren Schichten und bestätigen oder lehnen ab, bestätigte Schicht wird als „besetzt“ markiert
Validierung: keine doppelte Anfrage für dieselbe Schicht, keine Anfrage auf bereits besetzte Schichten
REST-API mit JSON: offene Schichten und eigene Buchungen abrufen (z. B. GET /api/shifts, GET /api/bookings)
