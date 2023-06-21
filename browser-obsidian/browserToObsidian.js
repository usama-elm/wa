// ==UserScript==
// @name         Webpage to Markdown for Obsidian
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Convert a webpage to Markdown and save it to an Obsidian.md vault
// @author       Usama
// @match        *://*/*
// @grant        GM_download
// @grant        GM_setValue
// @grant        GM_getValue
// @grant        GM_registerMenuCommand
// @require      https://cdnjs.cloudflare.com/ajax/libs/turndown/7.1.1/turndown.min.js
// ==/UserScript==

(function() {
    'use strict';

    const defaultSettings = {
        folderPath: '',
        buttonTextColor: '#000',
        buttonBackgroundColor: '#fff',
        activationKey: 'F8'
    };

    function loadSettings() {
        return {
            folderPath: GM_getValue('folderPath', defaultSettings.folderPath),
            buttonTextColor: GM_getValue('buttonTextColor', defaultSettings.buttonTextColor),
            buttonBackgroundColor: GM_getValue('buttonBackgroundColor', defaultSettings.buttonBackgroundColor),
            activationKey: GM_getValue('activationKey', defaultSettings.activationKey)
        };
    }

    function saveSettings(settings) {
        GM_setValue('folderPath', settings.folderPath);
        GM_setValue('buttonTextColor', settings.buttonTextColor);
        GM_setValue('buttonBackgroundColor', settings.buttonBackgroundColor);
        GM_setValue('activationKey', settings.activationKey);
    }

    function createButton(settings) {
        const button = document.createElement('button');
        button.textContent = 'Save as Markdown';
        button.style.position = 'fixed';
        button.style.top = '10px';
        button.style.right = '10px';
        button.style.zIndex = '9999';
        button.style.color = settings.buttonTextColor;
        button.style.backgroundColor = settings.buttonBackgroundColor;
        document.body.appendChild(button);
        return button;
    }

    function saveAsMarkdown() {
        const turndownService = new TurndownService();
        const markdown = turndownService.turndown(document.documentElement.outerHTML);
        const blob = new Blob([markdown], {type: 'text/plain;charset=utf-8'});
        const url = URL.createObjectURL(blob);
        const title = document.title.replace(/[^a-z0-9]/gi, '_').toLowerCase();
        const fileName = `${settings.folderPath ? settings.folderPath + '/' : ''}${title}.md`;

        GM_download({
            url: url,
            name: fileName,
            saveAs: true
        });
    }
    function openSettingsDialog() {
        const settings = loadSettings();

        const dialog = document.createElement('div');
        dialog.style.position = 'fixed';
        dialog.style.top = '50%';
        dialog.style.left = '50%';
        dialog.style.transform = 'translate(-50%, -50%)';
        dialog.style.backgroundColor = '#fff';
        dialog.style.border = '1px solid #000';
        dialog.style.zIndex = '10000';
        dialog.style.padding = '16px';
        dialog.innerHTML = `
            <h2>Settings</h2>
            <label>
                Folder path: <input type="text" id="folderPath" value="${settings.folderPath}">
            </label>
            <br>
            <label>
                Button text color: <input type="color" id="buttonTextColor" value="${settings.buttonTextColor}">
            </label>
            <br>
            <label>
                Button background color: <input type="color" id="buttonBackgroundColor" value="${settings.buttonBackgroundColor}">
            </label>
            <br>
            <label>
                Activation key: <input type="text" id="activationKey" value="${settings.activationKey}" maxlength="1">
            </label>
            <br>
            <button id="saveSettings">Save</button>
            <button id="cancelSettings">Cancel</button>
        `;

        document.body.appendChild(dialog);

        // Save button click event
        document.getElementById('saveSettings').addEventListener('click', () => {
            settings.folderPath = document.getElementById('folderPath').value.trim();
            settings.buttonTextColor = document.getElementById('buttonTextColor').value;
            settings.buttonBackgroundColor = document.getElementById('buttonBackgroundColor').value;
            settings.activationKey = document.getElementById('activationKey').value.toUpperCase();

            saveSettings(settings);
            document.body.removeChild(dialog);
            window.location.reload();
        });

        // Cancel button click event
        document.getElementById('cancelSettings').addEventListener('click', () => {
            document.body.removeChild(dialog);
        });
    }

    const settings = loadSettings();
    const button = createButton(settings);
    button.addEventListener('click', saveAsMarkdown);

    document.addEventListener('keydown', (event) => {
        if (event.key.toUpperCase() === settings.activationKey) {
            saveAsMarkdown();
        }
    });

    GM_registerMenuCommand('Settings', openSettingsDialog);
})();

