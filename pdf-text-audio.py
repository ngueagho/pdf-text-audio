import fitz  # PyMuPDF
from gtts import gTTS
import os
from playsound import playsound

def extract_text_from_pdf(pdf_path):
    # Ouvrir le fichier PDF
    document = fitz.open(pdf_path)
    
    # Initialiser une chaîne pour contenir le texte extrait
    extracted_text = ""
    
    # Parcourir chaque page du document
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text("text")
        
        # Sauter les numéros de page (supposons qu'ils sont en bas de chaque page)
        lines = text.splitlines()
        if lines:
            # Enlever la dernière ligne si elle contient le numéro de page
            if lines[-1].strip().isdigit():
                lines = lines[:-1]
        
        # Ajouter le texte de la page sans le numéro de page
        extracted_text += "\n".join(lines) + "\n"

    return extracted_text

def text_to_audio(text, audio_path):
    # Convertir le texte en audio
    tts = gTTS(text, lang='fr')
    tts.save(audio_path)
    # Jouer un extrait de l'audio
    playsound(audio_path)

if __name__ == "__main__":
    # Spécifiez le chemin du fichier PDF
    pdf_path = "terraform-docker.pdf"
    
    # Extraire le texte du PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Spécifiez le chemin pour enregistrer le fichier audio
    audio_path = "output_audio.mp3"
    
    # Convertir le texte en audio et sauvegarder en fichier MP3
    text_to_audio(text, audio_path)
    
    # Afficher un message de succès
    print(f"Le fichier audio a été sauvegardé sous {audio_path}")
