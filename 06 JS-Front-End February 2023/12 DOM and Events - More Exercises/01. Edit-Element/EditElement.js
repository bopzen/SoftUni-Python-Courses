function editElement(element, oldText, newText) {
    let text = element.textContent;
    while (text.includes(oldText)) {
        text = text.replace(oldText, newText);
    }
    element.textContent = text;
}