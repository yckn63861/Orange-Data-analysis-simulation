# Dashboard Analyse — Centre de Contacts

> Tableau de bord interactif d'analyse de la performance d'un centre de contacts, construit avec Python, Streamlit et Plotly.  
> Projet réalisé dans le cadre de la préparation à une alternance chez **Orange**.

---

## Contexte et objectif

L'équipe CXPM1 d'Orange délivre des projets en centres de contacts dans le cloud auprès de clients entreprises. Une part essentielle de cette mission consiste à analyser les volumes et la qualité des données issues de ces centres, afin d'optimiser la performance opérationnelle et l'expérience client.

Ce projet simule exactement ce travail : à partir d'un jeu de données représentatif, il produit un tableau de bord interactif permettant un suivi en temps réel des indicateurs clés de performance (KPIs).


## Fonctionnalités

### KPIs principaux
| Indicateur | Description |
|---|---|
| **Contacts traités** | Volume total d'interactions sur la période sélectionnée |
| **Taux de résolution** | Pourcentage de contacts résolus au premier contact |
| **Durée moyenne de traitement** | Temps moyen par interaction, en minutes |
| **Satisfaction client moyenne** | Score moyen sur une échelle de 1 à 5 |

### Visualisations
- **Volume de contacts par mois** — suivi de la tendance sur l'année
- **Répartition par canal** — téléphone, chat, email, réseaux sociaux
- **Satisfaction par motif de contact** — identifier les points de friction
- **Taux de résolution par agent** — suivi individuel de la performance
- **Durée moyenne par canal** — comparaison de l'efficacité selon le canal

### Filtres interactifs
- Canal de contact
- Motif de contact
- Période (plage de dates)


## Structure du projet

dashboard-orange-cxpm1/
│
├── DAr.py                      # Application Streamlit principale
├── centre_contacts_data.csv    # Dataset simulé (1 200 interactions)
└── README.md                   # Documentation du projet


## Stack technique

| Outil | Rôle |
|---|---|
| **Python 3.11** | Langage principal |
| **Streamlit** | Framework de création du dashboard web |
| **Plotly** | Bibliothèque de visualisation interactive |
| **Pandas** | Traitement et manipulation des données |

---

## Le dataset

Le jeu de données a été entièrement généré en Python avec la bibliothèque `random` et `csv`. Il simule **1 200 interactions clients** sur l'année 2024, avec les variables suivantes :

| Variable | Description | Valeurs possibles |
|---|---|---|
| `date` | Date de l'interaction | 01/01/2024 → 31/12/2024 |
| `canal` | Canal de contact | Téléphone, Chat, Email, Réseaux sociaux |
| `motif` | Raison du contact | Facturation, Assistance technique, Résiliation, Nouveau contrat, Réclamation, Information |
| `agent` | Agent ayant traité le contact | Agent A → Agent E |
| `duree_secondes` | Durée de l'interaction | Variable selon le canal |
| `statut` | Résultat du contact | Résolu, Escaladé, Non résolu |
| `satisfaction` | Note de satisfaction client | 1 à 5 |

> Les données sont simulées de manière réaliste : par exemple, les contacts non résolus génèrent logiquement des scores de satisfaction plus faibles, et les appels téléphoniques sont plus fréquents que les emails.

---

## Lancer le projet en local

### Prérequis
- Python 3.8 ou supérieur
- pip

### Installation

```bash
# 1. Cloner le repository
git clone https://github.com/VOTRE_USERNAME/dashboard-orange-cxpm1.git

# 2. Se placer dans le dossier
cd dashboard-orange-cxpm1

# 3. Installer les dépendances
pip install streamlit plotly pandas

# 4. Lancer le dashboard
streamlit run DAr.py
```

Le dashboard s'ouvre automatiquement dans votre navigateur à l'adresse `http://localhost:8501`.

---

## Ce que ce projet démontre

- **Analyse de données** : identification de KPIs pertinents pour un centre de contacts
- **Visualisation** : construction de graphiques clairs et actionnables
- **Python** : génération de données, traitement avec pandas, application web avec Streamlit
- **Pensée métier** : les indicateurs choisis répondent directement aux enjeux d'une équipe comme CXPM1 — performance, satisfaction client, pilotage opérationnel

---

## Auteure

**KANA NGANGOM YASMINE CORALINE**  
Étudiante ingénieure — ISEP Paris  
Spécialisation IA & Data Science (à partir de la 4e année)  
Actuellement en échange académique à l'Université INHA — Incheon, Corée du Sud


*Projet réalisé en juin 2026 dans le cadre d'une candidature à une alternance — Orange CXPM1, Saint-Denis.*
