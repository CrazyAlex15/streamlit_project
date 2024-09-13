import streamlit as st
import pandas as pd
from sklearn.decomposition import PCA
import umap
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Τίτλος της εφαρμογής
st.title('Data Loader, Visualization, and Machine Learning Application')

# Tabs
tab1, tab2, tab3 = st.tabs(["Φόρτωση Δεδομένων", "Οπτικοποίηση", "Μηχανική Μάθηση"])

# Tab 1: Φόρτωση Δεδομένων
with tab1:
    uploaded_file = st.file_uploader("Επέλεξε ένα αρχείο CSV", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Ο πίνακας δεδομένων:")
        st.dataframe(data)
    else:
        st.write("Παρακαλώ ανεβάστε ένα αρχείο για να δείτε τα δεδομένα.")

# Tab 2: Οπτικοποίηση
with tab2:
    if uploaded_file is not None:
        st.subheader('Visualization')

        features = st.multiselect('Επέλεξε τα χαρακτηριστικά (columns) για ανάλυση:', options=data.columns)

        if len(features) > 1:
            X = data[features]

            # PCA Visualization
            pca = PCA(n_components=2)
            X_pca = pca.fit_transform(X)
            fig_pca = px.scatter(X_pca, x=0, y=1, title="PCA 2D Visualization")
            st.plotly_chart(fig_pca)

            # UMAP Visualization
            umap_2d = umap.UMAP(n_components=2, random_state=42)
            X_umap = umap_2d.fit_transform(X)
            fig_umap = px.scatter(X_umap, x=0, y=1, title="UMAP 2D Visualization")
            st.plotly_chart(fig_umap)

        else:
            st.write("Παρακαλώ επέλεξε τουλάχιστον δύο χαρακτηριστικά για την οπτικοποίηση.")

# Tab 3: Μηχανική Μάθηση
with tab3:
    if uploaded_file is not None:
        st.subheader("Μηχανική Μάθηση - KNN Classifier")

        # Επιλογή χαρακτηριστικών και ετικετών (labels)
        features = st.multiselect('Επέλεξε τα χαρακτηριστικά (features) για το μοντέλο:', options=data.columns[:-1])
        label = st.selectbox('Επέλεξε την ετικέτα (label) για κατηγοριοποίηση:', options=[data.columns[-1]])

        if len(features) > 1:
            X = data[features]
            y = data[label]

            # Διαχωρισμός δεδομένων σε training και testing set
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            # Εκτέλεση αλγόριθμου KNN
            knn = KNeighborsClassifier(n_neighbors=3)
            knn.fit(X_train, y_train)

            # Πρόβλεψη και αποτελέσματα
            y_pred = knn.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write(f"Ακρίβεια: {accuracy}")
            st.write("Ανάλυση απόδοσης:")
            st.text(classification_report(y_test, y_pred))

        else:
            st.write("Παρακαλώ επέλεξε τουλάχιστον δύο χαρακτηριστικά για την κατηγοριοποίηση.")
    else:
        st.write("Παρακαλώ ανέβασε ένα αρχείο για να εφαρμόσεις το μοντέλο.")
