from dash_pdf._DashPdf import _DashPdf
import requests
import base64


def PDF(id, data, **kwargs):
    if isinstance(data, str) and (
        data.startswith("http://") or data.startswith("https://")
    ):
        response = requests.get(data)
        pdf_content = response.content
        pdf_base64 = base64.b64encode(pdf_content).decode("utf-8")
        data = f"data:application/pdf;base64,{pdf_base64}"
    elif isinstance(data, bytes):
        data = f"data:application/pdf;base64,{base64.b64encode(data).decode('utf-8')}"

    return _DashPdf(id=id, data=data, **kwargs)
