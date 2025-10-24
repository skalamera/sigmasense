const messagesEl = document.getElementById('messages')
const formEl = document.getElementById('form')
const inputEl = document.getElementById('input')
const fileEl = document.getElementById('file')
const attachEl = document.getElementById('attach')
let queuedImages = [] // data URLs

/** @param {string} role */
function addBubble(role, text) {
    const wrap = document.createElement('div')
    wrap.className = `bubble ${role}`
    wrap.textContent = text
    messagesEl.appendChild(wrap)
    messagesEl.scrollTop = messagesEl.scrollHeight
}

function fileToDataURL(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader()
        reader.onload = () => resolve(reader.result)
        reader.onerror = reject
        reader.readAsDataURL(file)
    })
}

attachEl.addEventListener('click', () => fileEl.click())
fileEl.addEventListener('change', async (e) => {
    const files = Array.from(e.target.files || [])
    for (const f of files) {
        if (!f.type.startsWith('image/')) continue
        const url = await fileToDataURL(f)
        queuedImages.push(url)
        addBubble('user', `[attached image: ${f.name}]`)
    }
    fileEl.value = ''
})

document.addEventListener('paste', async (e) => {
    const items = e.clipboardData && e.clipboardData.items ? Array.from(e.clipboardData.items) : []
    for (const it of items) {
        if (it.kind === 'file') {
            const file = it.getAsFile()
            if (file && file.type.startsWith('image/')) {
                const url = await fileToDataURL(file)
                queuedImages.push(url)
                addBubble('user', `[pasted image: ${file.name || 'image'}]`)
            }
        }
    }
})

async function send(content) {
    addBubble('user', content)
    inputEl.value = ''
    const thinking = document.createElement('div')
    thinking.className = 'bubble assistant'
    thinking.textContent = 'Thinking…'
    messagesEl.appendChild(thinking)
    messagesEl.scrollTop = messagesEl.scrollHeight

    const images = queuedImages.slice()
    queuedImages = []

    const payload = {
        messages: [
            { role: 'user', content },
        ],
        images,
    }

    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        })
        if (!res.ok) throw new Error(await res.text())
        const data = await res.json()
        thinking.remove()
        addBubble('assistant', data.content || '[no content]')
    } catch (err) {
        thinking.remove()
        addBubble('assistant', `Error: ${err}`)
    }
}

formEl.addEventListener('submit', (e) => {
    e.preventDefault()
    const text = inputEl.value.trim()
    if (!text) return
    send(text)
})

inputEl.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault()
        formEl.requestSubmit()
    }
})


