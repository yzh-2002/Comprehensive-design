// import { app, BrowserWindow } from "electron"
// import path from "path"
// import url from "url"

// import { DevUrl } from "./AppConfig"

const { app, BrowserWindow } =require("electron")
const path =require("path")
const url =require("url")

const { DevUrl } =require("./AppConfig")

// 
let mainWindow;

function createWindow(){

    mainWindow =new BrowserWindow()
    mainWindow.loadURL(DevUrl)

    mainWindow.on("closed",function(){
        mainWindow =null
    })
}

app.whenReady().then(()=>{
    createWindow()
})

app.on("window-all-closed",function(){
    if(process.platform !=='darwin'){
        app.quit() //macOS除非用户按下Cmd+Q显示退出，否则应用于菜单栏始终处于活动状态
    }
})

