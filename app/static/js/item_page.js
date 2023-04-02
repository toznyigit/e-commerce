window.addEventListener("DOMContentLoaded", ()=>{
    const rating = document.querySelector(".rating")
    const comment = document.querySelector("#send-comment")
    var stars = rating.querySelectorAll('i')
    stars.forEach(el=>{
        var self = el;
        el.addEventListener("click", ()=>{
            rating.setAttribute('value', Number(self.getAttribute('value')))
            stars.forEach(el2=>{
                if(Number(el2.getAttribute('value')) > Number(self.getAttribute('value'))){
                    el2.classList.remove('fa-star')
                    el2.classList.add('fa-star-o')
                }
                else{
                    el2.classList.remove('fa-star-o')
                    el2.classList.add('fa-star')
                }
            })
        })
    })
    comment.addEventListener("click", ()=>{
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                window.location.reload()
            }
        }

        xhttp.open("POST", comment.getAttribute('value'), true);
        xhttp.setRequestHeader('Content-type', 'application/json');
        xhttp.send(JSON.stringify({
                    'item': document.querySelector('#item-name').textContent,
                    'rating': document.querySelector('.rating').getAttribute('value'),
                    'comment': document.querySelector('input.input').value
                }));
    })
}, false);

