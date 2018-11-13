function url_validate(txtBox, txtValidation) { //newCode
 
    var WebUrlUser = $.trim(document.getElementById(txtBox).value);
    var WebUrlToLowercase = WebUrlUser.toLowerCase();
    var regUrl = /^((http[s]?:\/\/){0,1}(www\.){0,1}[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,5}[\.]{0,1}|((http)|(https)|(ftp):\/\/{0,1}[a-zA-Z0-9\.\-\_])|((mailto):{0,1}[a-zA-Z0-9\.\-\_]))/;
    if (regUrl.test(WebUrlToLowercase) == false) {
        document.getElementById(txtValidation).style.display = "block";
        document.getElementById(txtValidation).innerText = "Please enter fully qualified URL.";
        Communica.Part.adjustSize();
        return false;
    }
    else {
        document.getElementById(txtValidation).style.display = "none";
        document.getElementById(txtValidation).innerText = "";
        Communica.Part.adjustSize();
        return true;
    }
    Communica.Part.adjustSize();
}
function TestUrl(txtBoxUrlId) {

    var urlToCheck = $("#"+txtBoxUrlId).val();
    urlToCheck = $.trim(urlToCheck);
    if (urlToCheck != "")
    {
        urlToCheck=AppendUrl(urlToCheck);
        window.open(urlToCheck, '_blank');
    }
   
}
function AppendUrl(textUrl) {

    if (!textUrl.match(/^([a-zA-Z]+:\/\/)|(mailto:)/)) {
        textUrl = 'http://' + textUrl;

    }
    return textUrl;
}