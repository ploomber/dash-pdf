import dash_pdf
from dash import Dash, html, dcc, Input, Output, State
import dash
import requests
import base64
from pathlib import Path
import dash_react_syntax_highlighter as dsh

# Set React version
dash._dash_renderer._set_react_version("18.2.0")

# Initialize the app with Tailwind CSS
app = Dash(
    __name__,
    external_stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css"
    ],
)
server = app.server

# Default PDF URL
DEFAULT_URL = "https://css4.pub/2015/textbook/somatosensory.pdf"


# Function to load PDF data
def load_pdf(url):
    response = requests.get(url)
    pdf_content = response.content
    pdf_base64 = base64.b64encode(pdf_content).decode("utf-8")
    return f"data:application/pdf;base64,{pdf_base64}"


# App layout
app.layout = html.Div(
    [
        html.H1(
            "Dash PDF Viewer",
            className="text-4xl font-bold text-center my-8 text-gray-800",
        ),
        html.Div(
            [
                dcc.Input(
                    id="pdf-url-input",
                    type="text",
                    placeholder="Enter PDF URL",
                    value=DEFAULT_URL,
                    className="flex-grow px-3 py-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                ),
                html.Button(
                    "Load PDF",
                    id="load-pdf-button",
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-r-md",
                ),
            ],
            className="w-full max-w-md mb-4 flex",
        ),
        html.Div(
            [
                dash_pdf.PDF(
                    id="pdf-viewer",
                    data=load_pdf(DEFAULT_URL),
                    buttonClassName="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mx-1",
                    labelClassName="text-gray-800 text-lg mb-2",
                    controlsClassName="flex flex-row items-center justify-center space-x-4",
                ),
                html.Div(
                    [
                        html.H2(
                            "Installation",
                            className="text-xl font-bold mb-2 text-gray-800",
                        ),
                        dsh.DashReactSyntaxHighlighter(
                            code="pip install dash-pdf",
                            language="bash",
                            styleName="okaidia",
                        ),
                        html.H2(
                            "Usage",
                            className="text-xl font-bold mt-4 mb-2 text-gray-800",
                        ),
                        dsh.DashReactSyntaxHighlighter(
                            code="""from dash import Dash, html
import dash_pdf
import requests
from pathlib import Path
import dash

dash._dash_renderer._set_react_version("18.2.0")

app = Dash(__name__)

# Download the PDF and read it as bytes
url = 'https://css4.pub/2015/textbook/somatosensory.pdf'
response = requests.get(url)
pdf_bytes = response.content

# Alternatively, you can read a local PDF file
# pdf_bytes = Path('path/to/local/file.pdf').read_bytes()

app.layout = html.Div([
    dash_pdf.PDF(
        id='pdf-viewer',
        # Pass the PDF content as bytes, you can also pass a URL
        data=pdf_bytes,
        # use these to customize the class names
        buttonClassName="",
        labelClassName="",
        controlsClassName="",
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
""",
                            language="python",
                            styleName="okaidia",
                        ),
                    ],
                    className="mt-4 w-full max-w-2xl mx-auto",
                ),
            ],
            className="bg-white p-8 rounded-xl shadow-xl overflow-hidden",
        ),
        html.Footer(
            html.P(
                [
                    "Made with ",
                    html.Span("❤️", className="text-red-500"),
                    " by ",
                    html.A(
                        "Ploomber",
                        href="https://ploomber.io",
                        target="_blank",
                        rel="noopener noreferrer",
                        className="text-blue-500 hover:text-blue-700 underline",
                    ),
                    " • ",
                    html.Span("⭐ on "),
                    html.A(
                        "GitHub",
                        href="https://github.com/ploomber/dash-pdf",
                        target="_blank",
                        rel="noopener noreferrer",
                        className="text-blue-500 hover:text-blue-700 underline",
                    ),
                ],
                className="text-center text-gray-600 mt-8",
            ),
            className="mt-auto",
        ),
    ],
    className="min-h-screen bg-gradient-to-r from-blue-100 to-green-100 p-6 flex flex-col items-center justify-center",
)


@app.callback(
    Output("pdf-viewer", "data"),
    Input("load-pdf-button", "n_clicks"),
    Input("pdf-url-input", "n_submit"),
    State("pdf-url-input", "value"),
    prevent_initial_call=True,
)
def update_pdf(n_clicks, n_submit, url):
    return load_pdf(url)


if __name__ == "__main__":
    app.run_server(debug=True)
