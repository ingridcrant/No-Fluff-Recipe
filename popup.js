function scrapeThePage() {
    // Keep this function isolated - it can only call methods you set up in content scripts
    var htmlCode = document.documentElement.outerHTML;
    return htmlCode;
}

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('button').addEventListener('click',
    onclick, false)
    
    function onclick() {
        chrome.tabs.query({ active: true, currentWindow: true },
        function (tabs) {
            const tab = tabs[0];
            const scriptToExec = `(${scrapeThePage})()`;

            chrome.tabs.executeScript(tab.id, { code: scriptToExec },
                function (scraped) {
                    alert(scraped[0]);
                }
            );
        })
    }
}, false)