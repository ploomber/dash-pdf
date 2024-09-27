import dash_pdf
from dash import Dash, html
import dash
import requests
import base64
from pathlib import Path


dash._dash_renderer._set_react_version("18.2.0")


app = Dash(__name__)

URL = "https://css4.pub/2015/textbook/somatosensory.pdf"
URL = "https://arxiv.org/pdf/2302.13971"

# Download the PDF and convert to base64
response = requests.get(URL)
pdf_content = response.content
pdf_base64 = base64.b64encode(pdf_content).decode("utf-8")
# print(type(pdf_base64))

app.layout = html.Div(
    [
        dash_pdf.DashPdf(
            id="pdf-viewer",
            data=f"data:application/pdf;base64,{pdf_base64}",
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
