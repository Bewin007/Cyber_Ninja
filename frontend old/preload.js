const { contextBridge, shell } = require('electron');

// Expose the 'shell' object to the renderer process
contextBridge.exposeInMainWorld('electron', {
  shell: shell,
});
