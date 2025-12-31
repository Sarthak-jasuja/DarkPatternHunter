// 1. Function to extract visible text from the page
function getVisibleText() {
    const textNodes = [];
    const elements = document.body.querySelectorAll('h1, h2, h3, p, span, div, li, button, a');
    
    elements.forEach(el => {
        // Simple filter to get meaningful text (longer than 5 chars)
        if (el.innerText && el.innerText.length > 5 && el.children.length === 0) {
            textNodes.push({
                text: el.innerText.trim(),
                element: el // Keep reference to DOM element to highlight later
            });
        }
    });
    return textNodes;
}

// 2. Send data to FastAPI Backend
async function scanPage() {
    const nodes = getVisibleText();
    const textsOnly = nodes.map(n => n.text);

    console.log("Scanning page...", textsOnly.slice(0, 5)); // Debug log

    try {
        const response = await fetch('http://127.0.0.1:8000/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ texts: textsOnly })
        });

        const data = await response.json();
        
        // 3. Highlight the detected patterns
        if (data.patterns) {
            data.patterns.forEach(pattern => {
                // Find the original element that matches the text
                const match = nodes.find(n => n.text === pattern.text);
                if (match) {
                    match.element.classList.add('dark-pattern-highlight');
                    match.element.setAttribute('data-pattern-type', pattern.label);
                }
            });
        }

    } catch (error) {
        console.error("API Error - Is the backend running?", error);
    }
}

// Run the scan 2 seconds after page load (to let dynamic content load)
setTimeout(scanPage, 2000);