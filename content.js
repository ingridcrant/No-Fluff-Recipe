chrome.runtime.onMessage.addListener(
    function(message) {
        if (message.clicked) {
            const htmlCode = document.documentElement.outerHTML;

            $.post("https://no-fluff-recipes-flask.herokuapp.com/postmethod",
                {html: htmlCode}, 
                function(response) {
                    if (response.compatible) {
                        document.body.outerHTML = response.recipe;
                    }
                }
            );
        }
    }
);