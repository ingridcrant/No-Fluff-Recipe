chrome.runtime.onMessage.addListener(
    function(message) {
        if (message.clicked) {
            const htmlCode = document.documentElement.outerHTML;

            $.post("http://127.0.0.1:5000/postmethod",
                {html: htmlCode}, 
                function(response) {
                    document.body.outerHTML = response.recipe;
                }
            );
        }
    }
);