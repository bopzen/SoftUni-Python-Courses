function encodeAndDecodeMessages() {
    let [encodeBtn, decodeBtn] = document.getElementsByTagName("button");
    let [encodeText, decodeText] = document.getElementsByTagName("textarea");
    encodeBtn.addEventListener("click", clickEncode);
    decodeBtn.addEventListener("click", clickDecode);

    function clickEncode() {
        let text = encodeText.value;
        let encodedText = "";
        for (let i = 0; i < text.length; i++) {
            encodedText += String.fromCharCode(text[i].charCodeAt(0) + 1);         
        }
        decodeText.value = encodedText;
        encodeText.value = "";
    }

    function clickDecode() {
        let text = decodeText.value;
        let decodedText = "";
        for (let i = 0; i < text.length; i++) {
            decodedText += String.fromCharCode(text[i].charCodeAt(0) - 1);         
        }
        decodeText.value = decodedText;
    }
}