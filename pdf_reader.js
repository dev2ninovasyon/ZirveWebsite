const fs = require('fs');
try {
    const pdflib = require('C:/Users/lenov/AppData/Local/Temp/pdf_extract/node_modules/pdf-parse');
    const pdf = typeof pdflib === 'function' ? pdflib : pdflib.default;
    const dataBuffer = fs.readFileSync('C:/Users/lenov/Desktop/zirve program.pdf');
    pdf(dataBuffer).then(function(data) {
        fs.writeFileSync('C:/Users/lenov/ZirveWebsite/pdf_output.txt', data.text);
        console.log("PDF extraction successful!");
    }).catch(function(error) {
        fs.writeFileSync('C:/Users/lenov/ZirveWebsite/err.log', error.stack || error.message || String(error));
        console.error("PDF_ERROR - See err.log");
    });
} catch(e) {
    fs.writeFileSync('C:/Users/lenov/ZirveWebsite/err.log', e.stack || e.message || String(e));
    console.error("REQUIRE_ERROR - See err.log");
}
