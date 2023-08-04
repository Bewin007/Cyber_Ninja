const { Terminal } = require('xterm');
const { FitAddon } = require('xterm-addon-fit');

const terminal = new Terminal();
const fitAddon = new FitAddon();
terminal.loadAddon(fitAddon);
terminal.open(document.getElementById('terminal'));
fitAddon.fit();
