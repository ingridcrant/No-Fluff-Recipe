chrome.runtime.onMessage.addListener(
    function() {
        console.log("heyyyy");
        const htmlCode = document.documentElement.outerHTML;

        $.post("http://127.0.0.1:5000/postmethod",
            {html: htmlCode}, 
            function(response) {
                console.log(response);
                document.body.outerHTML = response;
            }
        );

        // document.body.innerHTML = recipecard;
        console.log("update site");
    }
);