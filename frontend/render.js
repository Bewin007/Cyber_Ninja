var child = require('child_process').execFile;
var executablePath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe";

child(executablePath, function(err, data) {
    if(err){
       console.error(err);
       return;
    }
 
    console.log(data.toString());
});

const { Terminal } = require('xterm');
const { FitAddon } = require('xterm-addon-fit');

const terminal = new Terminal();
const fitAddon = new FitAddon();
terminal.loadAddon(fitAddon);
terminal.open(document.getElementById('terminal'));
fitAddon.fit();

// Send input to the terminal
terminal.write('ls\n');

// Receive output from the terminal
terminal.onData(data => {
  console.log(data);
});