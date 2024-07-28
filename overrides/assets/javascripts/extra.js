/*
 * Licence MIT - Copyright (c) 2024 Kamil Krzyśków (HRY)
 */

function updateFontPreference(event) {
    console.debug(event);
    let cssRaw = "";
    let root = "";

    const text = event.target.dataset["text"];
    const code = event.target.dataset["code"];
    const src = event.target.dataset["src"];

    if (src !== "") {
	cssRaw += `@import url('${src}');`;
    }
    if (text !== "") {
	root += `--md-text-font: "${text}";`;
    }
    if (code !== "") {
	root += `--md-code-font: "${code}";`;
    }
    if (root !== "") {
	cssRaw += `:root { ${root} }`
    }

    // update style
    const loadedPreferences = __md_get(preferencesKey);
    loadedPreferences["__global"]["cssRaw"] = cssRaw;
    __md_set(preferencesKey, loadedPreferences);
    loadSetPreferences();
}

/*
    This is run immediately when loaded to limit UI elements flashing.
*/
(() => {
    const fonts = document.querySelectorAll("#md-fonts");
    fonts.forEach((font) => {
	let event_type = (font.tagName.toLowerCase() === "a") ? "click" : "change";
	font.addEventListener(event_type, updateFontPreference);
    });
})();
