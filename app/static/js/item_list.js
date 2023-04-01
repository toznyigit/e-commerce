function start(){
    const dropdown = document.getElementById("categories")
    const table = document.querySelector("#item-list")
    dropdown.addEventListener("change", ()=>{
        // console.log()
        
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
            // Typical action to be performed when the document is ready:
                table.innerHTML = ""
                item_list = JSON.parse(xhttp.response)
                for(let i=0;i<Math.ceil(item_list.length/4);i++){
                    var new_item_row = document.createElement('div')
                    new_item_row.classList.add('columns')
                    item_list.slice(i*4,i*4+4).forEach(el => {
                        var new_item_box = document.createElement('div')
                        new_item_box.classList.add('column')
                        new_item_box.classList.add('is-one-quarter')
                        new_item_box.innerHTML = item_box
                        new_item_box.querySelector('#item-name').innerText = el.name
                        new_item_box.querySelector('#item-desc').innerText = el.desc
                        new_item_box.querySelector('#item-rating').innerText = el.rating?el.rating:0.0
                        new_item_box.querySelector('#item-image').setAttribute('src', el.image)
                        new_item_box.querySelector('#item-seller').innerText = el.seller
                        new_item_box.querySelector('#item-price').innerHTML = el.price+`\n<span class="icon is-small"><i class="fa fa-try"></i></span>`
                        new_item_row.appendChild(new_item_box)
                    })
                    table.appendChild(new_item_row)
                }
                // JSON.parse(xhttp.response).forEach(el => {
                //     var new_item_box = document.createElement('div')
                //     new_item_box.innerHTML = item_box
                //     new_item_box.querySelector('#item-name').innerText = el.name
                //     new_item_box.querySelector('#item-rating').innerText = el.rating
                //     new_item_box.querySelector('#item-image').setAttribute('src', el.image)
                //     new_item_box.querySelector('#item-seller').innerText = el.seller
                //     new_item_box.querySelector('#item-price').innerText = el.price
                //     table.appendChild(new_item_box)
                // })
                
            }
        };
        xhttp.open("POST", "/get_item", true);
        xhttp.setRequestHeader('Content-type', 'application/json');
        xhttp.send(JSON.stringify({'category': dropdown.options[dropdown.selectedIndex].text}));
    }, false);
}

window.addEventListener("load", start, false);

const item_row = `
<div class="columns"></div>
`
const item_box = `
<div class="box">
    <div class="card-image has-text-centered">
        <div class="columns">
            <div class="column info is-one-third" id="item-name"></div>
            <div class="column info is-one-third"></div>
            <div class="column info is-one-third" id="item-rating"></div>
        </div>
        <figure class="image is-response-size is-inline-block">
            <img id="item-image" src="" alt="Image">
        </figure>
        <hr class="solid"></hr>
        <div>
            <p id="item-desc"></p>
        </div>
        <hr class="solid"></hr>
        <div class="columns is-hidden">
            <div class="column info is-one-third" id="item-spec-1"></div>
            <div class="column info is-one-third" id="item-spec-2"></div>
            <div class="column info is-one-third" id="item-spec-3"></div>
        </div>
        <hr class="solid is-hidden"></hr>
        <div class="columns">
            <div class="column info is-one-third" id="item-seller"></div>
            <div class="column info is-one-third"></div>
            <div class="column info is-one-third" id="item-price">
                
            </div>
        </div>
    </div>
</div>
`