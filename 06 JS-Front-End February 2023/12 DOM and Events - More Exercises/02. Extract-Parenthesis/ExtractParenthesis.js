function extract(content) {
    let element = document.getElementById(content);
    let text = element.textContent;
    let regex = /\(([^)]+)\)/g
    let matches = text.match(regex).map((m) => m.replace("(", "")).map((m) => m.replace(")",""));
    return `${matches.join("; ")}`
}