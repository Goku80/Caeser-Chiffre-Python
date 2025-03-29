# Caeser-Chiffre-Python
Dieses Skript implementiert Funktionen für die Verschlüsselung und Entschlüsselung von Texten mithilfe des Caesar-Chiffre.
Es erstellt Histogramme für gegebene Texte, berechnet die Häufigkeiten von Buchstaben und führt den Chi-Quadrat-Test durch,
um verschlüsselte Texte zu entschlüsseln. Die Hauptfunktion ermöglicht es, den verschlüsselten oder entschlüsselten Text auszugeben,
Histogramme zu erstellen und den Caesar-Chiffre zu knacken, indem es ein gegebenes Beispieltext verwendet.

## Verwendung

Um das Programm zu verwenden, führen Sie den folgenden Befehl in der Kommandozeile aus:

```bash
python caesar.py "Text zum Verschlüsseln" Schlüssel
```

Dabei ist:
- "Text zum Verschlüsseln" der Text, den Sie verschlüsseln oder entschlüsseln möchten (in Anführungszeichen)
- Schlüssel eine Ganzzahl, die den Verschlüsselungsschlüssel darstellt

### Beispiele:

1. Verschlüsseln mit Schlüssel 3:
```bash
python caesar.py "Hallo Welt" 3
```

2. Entschlüsseln mit Schlüssel -3:
```bash
python caesar.py "Kdoor Zhow" -3
```

**Wichtig:**
- Der Schlüssel muss eine Zahl sein und wird immer als letztes Argument angegeben
- Für die Entschlüsselung verwenden Sie einen negativen Schlüssel
- Wenn Ihr Text Leerzeichen enthält, setzen Sie ihn in Anführungszeichen
