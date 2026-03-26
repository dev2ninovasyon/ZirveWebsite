const fs = require('fs');
const files = ['index.html', 'kurul.html', 'program.html', 'sponsorlar.html'];
files.forEach(file => {
  let path = 'C:/Users/lenov/ZirveWebsite/' + file;
  if (fs.existsSync(path)) {
    let text = fs.readFileSync(path, 'utf8');
    text = text.replace(/<link href="https:\/\/fonts\.googleapis\.com\/css\?family=Poppins:100,200,300,400,500,600,700,800,900" rel="stylesheet">/g, '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">');
    text = text.replace(/<link href="https:\/\/fonts\.googleapis\.com\/css\?family=Lato:100,300,400,700,900" rel="stylesheet">/g, '');
    fs.writeFileSync(path, text);
    console.log('Updated ' + file);
  }
});
