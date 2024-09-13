# Χρήση μιας ελαφριάς εικόνας Python
FROM python:3.9-slim

# Ρύθμιση του working directory
WORKDIR /app

# Αντιγραφή των αρχείων requirements και του κώδικα
COPY requirements.txt requirements.txt
COPY app.py app.py

# Εγκατάσταση των απαιτούμενων βιβλιοθηκών
RUN pip install -r requirements.txt

# Άνοιγμα του port 8501 που χρησιμοποιεί το Streamlit
EXPOSE 8501

# Εκκίνηση της εφαρμογής
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
