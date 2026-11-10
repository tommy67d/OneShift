[← Contributors](README.md)

# Nisar Ouhammouch , Matrikelnr.: 77206712688

## Meta-Goals

### Target grade

2,0

### Personal goals

In diesem Projekt möchte ich lernen, ein relationales Datenmodell zu entwerfen und eine REST-API mit JSON bereitzustellen. Ich will verstehen, wie Tabellen wie Nutzer, Schichten und Buchungen sinnvoll miteinander verknüpft werden und wie die App diese Daten über eine saubere Schnittstelle ausliefert.
Außerdem möchte ich sicher mit Git im Team arbeiten können, also mit Branches, Pull Requests und dem Lösen von Merge-Konflikten. Dieses Wissen will ich später im Praktikum und im Beruf nutzen, um mich schnell in bestehende Projekte und Teams einzuarbeiten.

### Eidesstattliche Erklärung
## [Nisar Ouhammouch, Matrikelnr.: 77206712688]

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

KI-Systeme (z.B. LLM-basierte Werkzeuge) habe ich ausschließlich als Hilfsmittel gemäß der Vorgaben im Modul eingesetzt. Insbesondere habe ich zu keiner Zeit und in keiner Weise agentische Systeme ("Agentic AI") genutzt. Jegliche Nutzung habe ich vollständig und gemäß der geltenden Regeln und Vorgaben an HWR Berlin und Fachbereich 1 dokumentiert.

Mir ist bewusst, dass folgendes als Täuschungsversuch gewertet wird und zu einer Beurteilung der Modulleistung mit "nicht ausreichend" führt:

Die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe; Die nicht vollständige Offenlegung genutzter KI-Systeme; Jegliche Nutzung von Agentic AI. Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

### Vertical features

#### Schichten anfragen und Buchungen verwalten (Studierende & Unternehmen)

Datenmodell für Buchungen: Verknüpfung von Studierenden und Schichten mit Status (angefragt, bestätigt, abgelehnt)
Studierende fragen eine offene Schicht an und sehen ihre Anfragen mit Status in einer Übersicht
Unternehmen sehen eingegangene Anfragen zu ihren Schichten und bestätigen oder lehnen ab, bestätigte Schicht wird als „besetzt“ markiert
Validierung: keine doppelte Anfrage für dieselbe Schicht, keine Anfrage auf bereits besetzte Schichten
REST-API mit JSON: offene Schichten und eigene Buchungen abrufen (z. B. GET /api/shifts, GET /api/bookings)
