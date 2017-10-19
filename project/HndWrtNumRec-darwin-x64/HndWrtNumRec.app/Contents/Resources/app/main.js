const {app, BrowserWindow} = require('electron') 
const url = require('url') 
const path = require('path')  

let win  

function createWindow() {
   win = new BrowserWindow({
   	width: 1200,
   	height: 800,
   	icon: path.join(__dirname, 'assets/icons/png/64x64.png')
   })  
   win.loadURL(url.format ({ 
      pathname: path.join(__dirname, 'index.html'), 
      protocol: 'file:', 
      slashes: true 
   }))
}  

app.on('ready', createWindow)

/*
ideas:
change from initial electron icon to character.png (face) icon
*/