# News Dashboard Projekt
## Einführung
Das News Dashboard Projekt ist eine Streamlit Web-App, die Nachrichtendaten visualisiert. Es ermöglicht eine umfassende Analyse verschiedener Aspekte wie Themenanalyse, Sentimentanalyse, Subjektivität und ein Relation Chord Diagramm.
Datenquelle

Die Daten für dieses Projekt stammen aus der Swissdox@LiRI-Datenbank, die etwa 23 Millionen veröffentlichte Medienartikel aus einer Vielzahl von Schweizer Medienquellen enthält. Die Quellen umfassen sowohl Print- als auch Digitalmedien und decken viele Jahrzehnte ab. Täglich werden etwa 5000 bis 6000 neue Artikel hinzugefügt. Die Daten werden von unseren Partnern CH Media, NZZ Mediengruppe, Ringier, Ringier Axel Springer Schweiz und TX Group (Tamedia), SRF/SRG und Wochenzeitung bereitgestellt, insgesamt 250 Quellen mit geplanter weiterer Expansion.

Die Datenbeschaffung erfolgt durch eine Kooperation zwischen LiRI und SMD (Schweizer Mediendatenbank AG). Die Initiative wurde von Prof. Dr. Noah Bubenhofer, Prof. Dr. Fabrizio Gilardi (UZH) und Roberto Nespeca (SMD) ins Leben gerufen und wird von der Universität Zürich UZH (Technologieplattform-Kommission) und den folgenden Unterstützern finanziert: Zürcher Hochschule für Angewandte Wissenschaften (Abteilung für Angewandte Linguistik), Universität Basel/Universitätsbibliothek Basel, ETHZ Bibliothek, Universitätsbibliothek Bern.

## Nutzungsbedingungen
Die Nutzung der Daten ist strikt auf Forschungs- und akademische Zwecke beschränkt. Eine kommerzielle Nutzung der Daten sowie jegliche Derivate sind nicht erlaubt. Zudem dürfen die Daten nur für das angegebene Forschungsprojekt verwendet und nicht mit Dritten geteilt werden. Die Daten dürfen nur lokal auf Geräten der Forscher und Studierenden oder auf der Infrastruktur des Vertragspartners (akademische Institution) gespeichert werden. Insbesondere ist die Speicherung auf Cloud-Plattformen Dritter nicht gestattet.
Datenverarbeitung

Der erste Schritt bestand darin, die Daten zu laden und einige Vorverarbeitungsschritte durchzuführen, um unerwünschte Spalten zu entfernen. Danach wurde eine Textvorverarbeitung auf den Inhalt der Artikel angewendet, und anschließend wurde eine Länderextraktion durchgeführt, um zu erkennen, welche Länder in den Artikeln erwähnt werden. Es folgte eine Sentiment-Analyse, um die Polarität und Subjektivität der Artikel zu bestimmen. Als nächstes wurde eine Kategorisierung der Themen der Artikel durchgeführt und Entitäten wurden aus den Artikeltiteln extrahiert. Zuletzt wurden die Ländernamen übersetzt und Personen aus dem verarbeiteten Inhalt extrahiert. Die Daten wurden während der Analyse mehrmals gespeichert, um die Ergebnisse zu sichern und die Reproduzierbarkeit zu gewährleisten.

## Funktionen
 - Datumauswahl: Wählen Sie ein bestimmtes Datum, um Nachrichtendaten von diesem Datum zu visualisieren.
 - Kategorieauswahl: Filtern Sie die Nachrichtenartikel nach ihrer Kategorie.
 - Chord-Diagramm: Dies visualisiert die Beziehungen zwischen den in den Artikeln erwähnten Personen.
 - Sentiment-Analyse: Zeigt den Sentiment-Wert der Artikel. Der Wert reicht von -1 (sehr negativ) bis 1 (sehr positiv).
 - Subjektivitätsanalyse: Visualisiert die Objektivität der Artikel. Der Wert reicht von 0 (sehr objektiv) bis 1 (sehr subjektiv).
 - Themenanalyse: Zeigt die am häufigsten vorkommenden Wörter in den Artikeln.

## Installation und Ausführung
1. Klonen Sie das Repository auf Ihren lokalen Computer.
2. Installieren Sie die benötigten Python-Bibliotheken, indem Sie pip install -r requirements.txt in Ihrem Terminal ausführen.
3. Navigieren Sie zu dem Verzeichnis, in dem sich die Datei main.py befindet.
4. Führen Sie streamlit run main.py in Ihrem Terminal aus, um die Web-App zu starten.
5. Öffnen Sie Ihren Webbrowser und navigieren Sie zu der angegebenen URL (normalerweise http://localhost:8501).

## Anforderungen
Dieses Projekt erfordert Python 3.6+ und die folgenden Python-Bibliotheken müssen installiert sein:
- pandas
- streamlit
- holoviews
- plotly
