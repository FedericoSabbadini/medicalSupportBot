import requests
import fitz  # pymupdf
from pypdf import PdfReader
import io

class Loader:
    def __init__(self, databaseURL: str, databaseKey: str):
        self.databaseURL = databaseURL
        self.databaseKey = databaseKey


    def load(self, AIC: str):

            response = requests.get(
                self.databaseURL, 
                headers={"xc-token": self.databaseKey}, 
            )
            data = response.json()

            for item in data["list"]:
                item_title = item["Title"]
                item_url1 = item["URL1"]
                item_url2 = item["URL2"]
                item_AIC = item["AIC"]

                if item_AIC == AIC:
                    title = item_title
                    url1 = item_url1
                    url2 = item_url2


            # we have to do a request to each one of the URLs to retrieve the context and then use it to generate a response to the question.
            # an example of how this file looks like is, after transofrmation from pdf to json, 
            # {"tipoAutorizzazione":"A","aic6ImportazioneParallela":null,"sisImportazioneParallela":null,"denImportazioneParallela":null,"ragImportazioneParallela":null,"categoriaMedicinale":"1"},{"idPackage":"25501","denominazionePackage":"\"875 MG/125 MG COMPRESSE RIVESTITE CON FILM\" 2 COMPRESSE IN BLISTER PVC/AL/PA-AL","descrizioneFornitura":null,"classeFornitura":"RR","codiceFormaDosaggio":"0000017740","aic":"026089211","descrizioneRf":["Soggetto a Prescrizione Medica"],"carenzaMotivazione":null,"carenzaInizio":null,"carenzaFinePresunta":null,"dataAutorizzazione":"2013-11-22T23:00:00.000+00:00","flagCommercio":0,"flagPrescrizione":1,"carente":0,"vieSomministrazione":["ORALE"],"classeRimborsabilita":"Cnn","descrizioneRimbors"}
            text_url1 = self.get_from_url(url1)
            text_url2 = self.get_from_url(url2)

            return title, text_url1, text_url2

    def get_from_url(self, url: str):
        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/pdf"
            }
        )
        #doc = fitz.open(
        #    stream=response.content,
        #    filetype="pdf"
        #)
        # let's create an alternative version
        reader = PdfReader(io.BytesIO(response.content))
        

        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

        return text