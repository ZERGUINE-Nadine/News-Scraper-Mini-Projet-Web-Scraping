#  News Scraper – Mini Projet Web Scraping

##  Description
Ce projet est un **mini scraper d’actualités** développé en **Python**.  
Il récupère automatiquement des articles depuis des **flux RSS officiels**, filtre les articles par mots-clés, nettoie les données et les sauvegarde :

- en **JSON**
- dans une base **MongoDB**

Le projet a été conçu dans un objectif **pédagogique et professionnel**, notamment pour démontrer des compétences en **Web Scraping / Data Engineering junior**.

---

##  Technologies utilisées
- **Python 3**
- **Requests** – requêtes HTTP
- **BeautifulSoup** – parsing XML (RSS)
- **Regex** – nettoyage et traitement du texte
- **JSON** – export des données
- **MongoDB** – stockage NoSQL
- **Git / GitHub** – versioning

---

##  Structure du projet


---

##  Fonctionnalités
- Extraction des :
  - titres
  - liens
  - dates de publication
  - descriptions
- Filtrage par **mots-clés**
- Nettoyage du texte avec **Regex**
- Conversion des dates au format standard (`YYYY-MM-DD`)
- Sauvegarde :
  - en fichier `articles.json`
  - dans MongoDB (`news_db.articles`)
- Gestion des doublons via `upsert`

---

##  Installation & Exécution

### 1- Cloner le projet

git clone https://github.com/ZERGUINE-Nadine/News-Scraper-Mini-Projet-Web-Scraping.git.

cd news-scraper


### 2- Créer un environnement virtuel
python -m venv venv 

source venv/bin/activate   # macOS / Linux

venv\Scripts\activate      # Windows

### 3- Installer les dépendances
pip install -r requirements.txt

### 4- Lancer MongoDB
mongosh

### 5- Exécuter le scraper
python scraper.py


### => Légalité & RGPD

Les données proviennent exclusivement de flux RSS officiels

Aucune donnée personnelle n’est collectée

Respect des bonnes pratiques de scraping (usage raisonnable, sources publiques)
