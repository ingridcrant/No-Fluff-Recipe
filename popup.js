$(document).ready(function() {
    $(document).bind('keydown',function(e){
        if(e.keyCode == 13) {
            chrome.tabs.query({ active: true, currentWindow: true },
                function (tabs) {
                    chrome.tabs.sendMessage(tabs[0].id, { clicked: true });
                }
            )
        }
    });
	$('.scrape').click(function() {
        chrome.tabs.query({ active: true, currentWindow: true },
            function (tabs) {
		        chrome.tabs.sendMessage(tabs[0].id, { clicked: true });
            }
        )
	});
});