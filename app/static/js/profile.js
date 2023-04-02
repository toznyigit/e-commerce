window.addEventListener("DOMContentLoaded", ()=>{
    const comments = document.querySelectorAll('.comment-div').forEach(el=>{
        el.addEventListener('click', ()=>{
            window.location = `/item?name=${el.getAttribute('value')}`
        })
    })
})