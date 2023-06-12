# News Dashboard Projekt

## Installation und Ausführung
1. Klonen Sie das Repository auf Ihren lokalen Computer.
2. Installieren Sie die benötigten Python-Bibliotheken, indem Sie pip install -r requirements.txt in Ihrem Terminal ausführen.
3. Navigieren Sie zu dem Verzeichnis, in dem sich die Datei Medien_Analyse.py befindet.
4. Führen Sie streamlit run Medien_Analyse.py in Ihrem Terminal aus, um die Web-App zu starten.
5. Öffnen Sie Ihren Webbrowser und navigieren Sie zu der angegebenen URL (normalerweise http://localhost:8501).
6. Wir empfehlen die Verwendung des 'Light modes' im Browser.

## Anforderungen
Dieses Projekt erfordert Python 3.6+ und die folgenden Python-Bibliotheken müssen installiert sein:
- pandas
- streamlit
- holoviews
- plotly

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

## Kategorisierung der Themenbereiche
Die Kategorisierung erfolgt durch die Berechnung der Ähnlichkeit zwischen dem gegebenen Text und einer vordefinierten
Gruppe von Schlüsselwörtern für jede Kategorie. Die Ähnlichkeit wird mittels Wortvektor-Ähnlichkeit berechnet,
die von Spacy's Sprachmodell 'de_core_news_lg' bereitgestellt wird. Der Wortvektor ist eine mehrdimensionale
Darstellung eines Worts, die dessen Bedeutung in Bezug auf andere Wörter im Vokabular repräsentiert.
Die Idee ist, dass Wörter, die in ähnlichen Kontexten vorkommen, ähnliche Bedeutungen haben und daher
ähnliche Vektoren haben sollten. Die Ähnlichkeit zwischen zwei Wörtern wird als Kosinus-Ähnlichkeit berechnet,
die den Kosinus des Winkels zwischen zwei Vektoren darstellt. Je näher der Kosinus dem Wert 1 ist, desto ähnlicher
sind die Wörter. Es kommt das deutsche Sprachmodell 'de_core_news_lg' zum Einsatz. Dieses muss vorher mit
'python -m spacy download de_core_news_sm heruntergeladen werden. Das Modell ist für die
Verwendung mit Python 3.8 optimiert.

Attribute:
    - nlp_de (Language): Spacy-Sprachmodell für Deutsch.
    - topics (dict): Ein Dictionary, das jede Kategorie ihren Schlüsselwörtern zuordnet.

## Sentimentätsanalyse
Polarität: TextBlob berechnet die Polarität eines Textes, um zu bestimmen, ob der Text positiv, negativ
oder neutral ist. Der Polaritätswert liegt zwischen -1 und 1, wobei -1 für eine stark negative Aussage steht,
1 für eine stark positive Aussage und 0 für eine neutrale Aussage.

Subjektivität: TextBlob berechnet die Subjektivität eines Textes, um zu bestimmen, inwieweit der Text eine
subjektive Meinung oder eine objektive Tatsache darstellt. Der Wert für Subjektivität liegt zwischen 0 und 1,
wobei 0 für eine objektive Aussage steht und 1 für eine stark subjektive Aussage.

## Extraktion von Entitäten und Subjekten
Die Klasse EntityFinder dient zur Extraktion von Entitäten aus Texten.
Die Methode extract_entities extrahiert alle Substantive aus einem Text. Die Extraktion erfolgt durch das deutsche
Sprachmodell 'de_core_news_lg'.

Die Methode get_people() extrahiert alle Personen aus einem Text. Die Extraktion erfolgt durch den Vergleich der
Wörter des Textes mit der Liste der Personen des öffentlichen Lebens. Die Liste ist eine Zusammenstellung der 1239
relevantesten und einflussreichsten Personen des Jahres 2022 aus den Bereichen Politik, Wirtschaft, Sport, Kultur,
Medien, Wissenschaft und Gesellschaft.

Die Methode SubjectFinder dient zur Extraktion von Subjekten aus Texten.
Subjekte sind diejenigen Entitäten, die im Satz das Verb bestimmen. Die Extraktion erfolgt durch die Erkennung der
Abhängigkeiten zwischen den Wörtern im Satz. Es kommt das deutsche Sprachmodell 'de_core_news_lg' zum Einsatz.

## Extratkion von Ländern
Extrahiert Länder aus einem Text und übersetzt diese in die englische Sprache. Dafür vergleicht die Methode
get_country() die Wörter des Textes mit der Länderliste. Die Methode country_translation() übersetzt die
gefundenen Länder in die englische Sprache. Die Länderliste wurde aus dem Wikipedia-Artikel "Liste der Staaten der
Erde" extrahiert und mit der Google Translate übersetzt. Die Übersetzungen wurden manuell korrigiert.

Attribute: country_en_de_dict: Ein Wörterbuch mit den Ländern als Schlüssel und den englischen Übersetzungen als Werte.

## Datenaufbereitung
Wenn Sie mehr über die Datenaufbereitung erfahren möchten, werfen Sie bitte einen Blick auf das Jupyter Notebook mit dem Namen "data_processing_pipeline.ipynb".
