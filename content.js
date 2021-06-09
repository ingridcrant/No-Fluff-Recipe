chrome.runtime.onMessage.addListener(
    function() {
        const htmlCode = document.documentElement.outerHTML;

        $.post("http://127.0.0.1:5000/postmethod",
            {html: htmlCode}, 
            function(response) {
                console.log(response.recipe);
                document.body.outerHTML = response.recipe;
            }
        );
    }
);