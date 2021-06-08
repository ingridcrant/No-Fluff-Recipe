// function scrapeThePage() {
//     // Keep this function isolated - it can only call methods you set up in content scripts
//     var htmlCode = document.documentElement.outerHTML;

//     $.post("http://127.0.0.1:5000/postmethod",
//     {
//         html: htmlcode
//     }, function(response) {
//         console.log(response);
//         document.body.innerHTML = response;
//     });

//     return htmlCode;
// }

// document.addEventListener('DOMContentLoaded', function () {
//     document.querySelector('button').addEventListener('click',
//     onclick, false)

//     function onclick() {
//         chrome.tabs.query({ active: true, currentWindow: true },
//         function (tabs) {
//             const tab = tabs[0];
//             const scriptToExec = `(${scrapeThePage})()`;

//             chrome.tabs.executeScript(tab.id, { code: scriptToExec });
//         })
//     }
// }, false)

$(document).ready(function() {
	$('.scrape').click(function() {
        chrome.tabs.query({ active: true, currentWindow: true },
            function (tabs) {
		        chrome.tabs.sendMessage(tabs[0].id, { clicked: true });
            }
        )
	})
});