import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { Document, Page } from 'react-pdf';
import { pdfjs } from 'react-pdf';

pdfjs.GlobalWorkerOptions.workerSrc = `//unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;

/**
 * _DashPdf is a component that renders a PDF.
 * It takes a property, `data`, which is the PDF file to be rendered.
 * It allows navigation through the pages of the PDF.
 */
const _DashPdf = (props) => {
    const { id, data, setProps, buttonClassName, labelClassName, controlsClassName } = props;
    const [numPages, setNumPages] = useState(null);
    const [pageNumber, setPageNumber] = useState(1);

    function onDocumentLoadSuccess({ numPages }) {
        setNumPages(numPages);
        setPageNumber(1);
    }

    function changePage(offset) {
        setPageNumber(prevPageNumber => prevPageNumber + offset);
    }

    function previousPage() {
        changePage(-1);
    }

    function nextPage() {
        changePage(1);
    }

    return (
        <div id={id}>
            <Document
                file={data}
                onLoadSuccess={onDocumentLoadSuccess}
            >
                <Page pageNumber={pageNumber} renderTextLayer={false} renderAnnotationLayer={false} />
            </Document>
            <div className={controlsClassName}>
                <p className={labelClassName}>
                    Page {pageNumber || (numPages ? 1 : '--')} of {numPages || '--'}
                </p>
                <button
                    type="button"
                    disabled={pageNumber <= 1}
                    onClick={previousPage}
                    className={buttonClassName}
                >
                    Previous
                </button>
                <button
                    type="button"
                    disabled={pageNumber >= numPages}
                    onClick={nextPage}
                    className={buttonClassName}
                >
                    Next
                </button>
            </div>
        </div>
    );
}

_DashPdf.defaultProps = {
    buttonClassName: '',
    labelClassName: '',
    controlsClassName: ''
};

_DashPdf.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The PDF data to be rendered.
     */
    data: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.instanceOf(ArrayBuffer),
        PropTypes.instanceOf(Uint8Array)
    ]).isRequired,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

    /**
     * CSS class name for the Previous and Next buttons.
     */
    buttonClassName: PropTypes.string,

    /**
     * CSS class name for the "Page X of Y" label.
     */
    labelClassName: PropTypes.string,

    /**
     * CSS class name for the parent div of label and buttons.
     */
    controlsClassName: PropTypes.string
};

export default _DashPdf;
