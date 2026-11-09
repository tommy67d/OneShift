[← Contributors](README.md)

# Hosam Khalili , Matrikelnr.: 77201177515

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

KI-Systeme (z.B. LLM-basierte Werkzeuge) habe ich ausschließlich als Hilfsmittel gemäß der Vorgaben im Modul eingesetzt. Insbesondere habe ich zu keiner Zeit und in keiner Weise agentische Systeme ("Agentic AI") genutzt. Jegliche Nutzung habe ich vollständig und gemäß der geltenden Regeln und Vorgaben an HWR Berlin und Fachbereich 1 dokumentiert.

Mir ist bewusst, dass folgendes als Täuschungsversuch gewertet wird und zu einer Beurteilung der Modulleistung mit "nicht ausreichend" führt:

Die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe;
Die nicht vollständige Offenlegung genutzter KI-Systeme;
Jegliche Nutzung von Agentic AI.
Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

## Meta-Goals

### Target grade

1,0 - 1,7

### Personal goals

Ich möchte lernen, wie man eine vollständige Webanwendung mit Flask entwickelt, von der Datenbank bis zur Benutzeroberfläche. Außerdem möchte ich sicher im Umgang mit Git und GitHub im Team werden, besonders mit Branches und Pull Requests. Im Team möchte ich die Verantwortung für ein zentrales Feature unserer Plattform übernehmen und dafür sorgen, dass es zuverlässig funktioniert.

---
### Vertical features

### Schicht-Feed

- Schicht-Feed: Liste aller offenen Schichten mit Titel, Betrieb, Tätigkeit, Datum, Uhrzeit, Bezirk,Stundenlohn
- Filter nach Datum, Bezirk, Tätigkeit, Mindest-Stundenlohn und benötigter Sprache
- Schicht-Detailseite: alle Infos zur Schicht und zum Betrieb, Button „Schicht anfragen“
- Schicht buchen (Buchungsanfrage senden) und eigene Anfrage stornieren
- „Meine Schichten“: Übersicht nach Status angefragt / bestätigt / abgeschlossen
- Validierung: nur offene Schichten in der Zukunft anfragbar, keine doppelte Anfrage, keine zeitlich überschneidenden Schichten, Stornieren nur bis 24 h vor Schichtbeginn
