const confirmedwebpages = [
    "seriouseats.com",
    "pinchofyum.com",
    "balancedbites.com",
    "cookieandkate.com",
    "therecipecritic.com",
    "minimalistbaker.com",
    "thekitchn.com",
    "smittenkitchen.com",
    "davidlebovitz.com",
    "damndelicious.net",
    "skinnytaste.com",
    "101cookbooks.com",
    "sweetashoney.co",
    "loveandoliveoil.com",
    "closetcooking.com",
    "simplyrecipes.com",
    "thefirstmess.com",
    "halfbakedharvest.com",
    "budgetbytes.com",
    "sallysbakingaddiction.com",
    "recipesfromapantry.com",
    "loveandlemons.com",
    "chef-in-training.com",
    "thesaltymarshmallow.com",
    "spendwithpennies.com",
    "gimmesomeoven.com",
    "theviewfromgreatisland.com",
    "crunchycreamysweet.com",
    "natashaskitchen.com",
    "cookingclassy.com",
    "dinneratthezoo.com",
    "justonecookbook.com",
    "wellplated.com",
    "thestayathomechef.com",
    "downshiftology.com",
    "diethood.com",
    "holycowvegan.net",
    "thewoksoflife.com",
    "askchefdennis.com",
    "apicyperspective.com",
    "tastesbetterfromscratch.com",
    "veganinthefreezer.com",
    "themediterraneandish.com",
    "feelgoodfoodie.net",
    "dinnerthendessert.com",
    "thebigmansworld.com",
    "ambitiouskitchen.com",
    "gimmedelicious.com",
    "acouplecooks.com",
    "jocooks.com",
    "chocolatecoveredkatie.com",
    "livingthegourmet.com",
    "cafedelites.com",
    "grilledcheesesocial.com",
    "everydaymaven.com",
    "skinnyms.com",
    "jessicagavin.com",
    "preppykitchen.com",
    "twopeasandtheirpod.com",
    "panlasangpinoy.com",
    "biggerbolderbaking.com",
    "sugarspunrun.com",
    "thepeachkitchen.com",
    "bowlofdelicious.com",
    "mykoreankitchen.com",
    "lilluna.com",
    "100daysofrealfood.com",
    "momontimeout.com",
    "thechunkychef.com",
    "freshoffthegrid.com",
    "lecremedelacrumb.com",
    "culinaryhill.com",
    "thefoodieaffair.com",
    "asweetpeachef.com",
    "hummingbirdhigh.com",
    "daringgourmet.com",
    "thecookierookie.com",
    "detoxinista.com",
    "chelseasmessyapron.com",
    "familystylefood.com",
    "southerndiscourse.com",
    "snappygourmet.com",
    "ketoconnect.net",
    "nourishedkitchen.com",
    "sweetpeasandsaffron.com",
    "africanbites.com",
    "howsweeteats.com",
    "kirbiecravings.com",
    "easyweeknightrecipes.com",
    "grandbaby-cakes.com",
    "adventuresofanurse.com",
    "lifeloveandsugar.com",
    "cookeatpaleo.com",
    "justataste.com",
    "frugalhausfrau.com",
    "palatablepastime.com",
    "omnivorescookbook.com",
    "addapinch.com",
    "kawalingpinoy.com",
    "barefeetinthekitchen.com",
    "panningtheglobe.com"
];

chrome.tabs.onActivated.addListener(function() {
    getActivatedTab();
});

chrome.webNavigation.onCompleted.addListener(function() {
    getActivatedTab();
});

function getActivatedTab(){
    chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
        try{
            if(tabs[0]!=undefined){

                var match = false;
                for (i = 0; i < confirmedwebpages.length; i++) {
                    if (tabs[0].url.indexOf(confirmedwebpages[i]) >= 0) {
                        match = true;
                        break;
                    }
                }

                if (match) {
                    chrome.browserAction.setIcon({
                        path : {
                            "128": "images/approvedicon128.png"
                        }
                    })
                }
                else {
                    chrome.browserAction.setIcon({
                        path : {
                            "128": "images/icon128.png"
                        }
                    })
                }
            }
        }
        catch(err){
            setTimeout(function() {
            getActivatedTab();
            },100);
        }
    })
}