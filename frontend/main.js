const { app, BrowserWindow } = require('electron');
const path = require('path');
const os = require('os-utils');
const Chart = require('chart.js');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      contextIsolation:false,
      nodeIntegration: true,
      preload: path.join(__dirname, 'render.js'), // Set the path to the preload script
    },

  });

  mainWindow.loadFile('./Html/index.html');
  setInterval(() => {
    os.cpuUsage(function(v){
      mainWindow.webContents.send('cpu',v*150);
      mainWindow.webContents.send('mem',os.freememPercentage()*100);
      mainWindow.webContents.send('total-mem',os.totalmem()/1024);
      // console.log(os.totalmem())
    });
  },1000);
  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});
