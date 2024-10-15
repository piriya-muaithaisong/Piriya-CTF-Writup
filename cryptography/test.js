const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const pug = require('pug');
const vm = require('vm');
const fs = require('fs');
 
FLAG = fs.readFileSync('.passwd', {encoding:'utf8', flag:'r'});
 
const PORT = 59069;
 
var urlencodedParser = bodyParser.urlencoded({ extended: true });
const app = express();
 
/* Template parameters */
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');
 
app.get('/', function (req, res, next) {
    res.send(pug.renderFile(path.join(__dirname, 'views/index.pug'), { code: '', result: '' }));
});
 
app.post('/', urlencodedParser, function (req, res) {
    const code = req.body.code + '';
    if (code.length != 0) {
        try {
            // vm with empty context
            data = vm.runInNewContext(
                code,                                   // Executes user code in new context
                vm.createContext(Object.create(null)),  // Creates an empty context
                { timeout: 200 }                        // Maximum execution time
            );
            if (data !== undefined) {
                if (data['result'] !== undefined) {
                    result = {result: data['result']};
                } else {
                    result = {result: data};
                }
            } else {
                result = {result: "undefined"};
            }
        } catch (err) {
            result = {result: err};
        }
    } else {
        result = {result: 'Empty code'};
    }
 
    // Catch if there is an error in rendering
    try {
        res.send(
            pug.renderFile(
                path.join(__dirname, 'views/index.pug'), {
                    code: code,
                    result: result['result']
                }
            )
        );
    } catch (err) {
        res.send(
            pug.renderFile(
                path.join(__dirname, 'views/index.pug'),
                { code: code, result: err }
            )
        );
    }
});
 
app.get('/css/style.css', function (req, res) {
    res.sendFile(path.join(__dirname, 'css/style.css'));
});
 
// Starts app
app.listen(PORT, function () {
    console.log('Challenge listening on port ' + PORT);
});
