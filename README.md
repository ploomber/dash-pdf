<p align="center">
    <h1 align="center"><b>Dash PDF</b></h1>
	<p align="center">
		Display PDFs in your Dash apps.
    <br />
    <br />
    <br />
    <img width="100" height="100" src="https://avatars.githubusercontent.com/u/60114551?s=200&v=4" alt="Ploomber Logo">
    <br />
    <b>  Made by <a href="https://ploomber.io/?utm_source=dash-pdf&utm_medium=github">Ploomber</a> with ❤️</b>
    <br />
    <br />
    <i>Deploy your Dash application on <a href="https://www.platform.ploomber.io/register/?utm_source=dash-pdf&utm_medium=github">Ploomber.io</a> for free.</i>
    <br />
  </p>
</p>
<br/>



https://github.com/user-attachments/assets/bcc9ba7d-5110-4fb9-ba58-551684890ae9


Live demo: [dash-pdf.ploomberapp.io](https://dash-pdf.ploomberapp.io/?utm_source=dash-pdf&utm_medium=github)

## Installation

```sh
pip install dash-pdf
```

## Usage

```python
from dash import Dash, html
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
```

## Run demo locally

```sh
cd demo
pip install -r requirements.txt
python app.py
```

Open: http://localhost:8050


## Documentation


## Setup

```sh
# install js dependencies
npm install
# install python package in editable mode
pip install -e .

# install other python dependencies
pip install -r requirements.txt
pip install -r tests/requirements.txt
```

## Development

```sh
npm run build
python demo.py
```


## Release

```sh
# generate
npm run build
python setup.py sdist bdist_wheel
ls dist

# test artifact
pip install dash dist/dash_pdf-0.0.1.tar.gz
python demo/app.py

# upload
pip install twine
twine upload dist/*

# clean up
rm -rf dist
```
