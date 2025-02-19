import streamlit as st

st.title("Algoritmo Diagnostico Istologico per Neoplasie Mieloproliferative")
st.write("Inserisci i punteggi (da 1 a 3 per la maggior parte dei parametri, mentre per la Fibrosi va da 0 a 3):")

# Input dei punteggi
cellularita = st.slider("1. Cellularità e Panmielosi", 1, 3, 1, help="1: normale, 2: moderata ipercellularità, 3: marcata ipercellularità con panmielosi")
megacariociti = st.slider("2. Morfologia e Clustering dei Megacariociti", 1, 3, 1, help="1: normali, 2: qualche clustering e lievi atypie, 3: atipia marcata con clustering denso")
fibrosi = st.slider("3. Fibrosi Reticolare", 0, 3, 0, help="0: assente, 1: minima, 2: intermedia, 3: marcata")
eritroide = st.slider("4. Proliferazione Eritroide", 1, 3, 1, help="1: minima/assente, 2: moderata, 3: marcata")
granulocitaria = st.slider("5. Proliferazione Granulocitaria", 1, 3, 1, help="1: quasi normale, 2: moderata, 3: marcata")

# Calcolo del punteggio totale
totale = cellularita + megacariociti + fibrosi + eritroide + granulocitaria

st.write("### Punteggio Totale:", totale)

# Interpretazione del punteggio
if totale >= 4 and totale <= 8:
    diagnosi = "Trombocitemia Essenziale (ET)"
elif totale >= 9 and totale <= 12:
    diagnosi = "Policitemia Vera (PV)"
elif totale >= 13 and totale <= 15:
    diagnosi = "Mielofibrosi Primaria (PMF)"
else:
    diagnosi = "Punteggio non valido. Rivedere i valori inseriti."

st.write("### Diagnosi Probabile:", diagnosi)

st.markdown("---")
st.markdown("**Nota:** Questo strumento è un supporto ausiliario e non sostituisce la valutazione clinico-patologica completa. Valuta sempre i risultati in un contesto multidisciplinare, integrando dati clinici, ematochimici e molecolari.")
