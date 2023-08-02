var child = require('child_process').execFile;
var executablePath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe";

child(executablePath, function(err, data) {
    if(err){
       console.error(err);
       return;
    }
 
    console.log(data.toString());
});