function start(){
    const dropdown = document.getElementById("categories")
    const table = document.querySelector("#item_table").querySelector("tbody")
    dropdown.addEventListener("change", ()=>{
        // console.log()
        
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
            // Typical action to be performed when the document is ready:
                JSON.parse(xhttp.response).forEach(el => {
                    var tr = document.createElement('tr')
                    tr.innerHTML = tr_template
                    tr.querySelector('.has-text-weight-semibold').innerHTML = el.name
                    tr.querySelector('input').setAttribute('value', el.name)
                    table.appendChild(tr)
                })
                
            }
        };
        xhttp.open("POST", "/get_item", true);
        xhttp.setRequestHeader('Content-type', 'application/json');
        xhttp.send(JSON.stringify({'category': dropdown.options[dropdown.selectedIndex].text}));
    }, false);
}

function addActivityItem(){
    //option is selected
    alert("yeah");
}

window.addEventListener("load", start, false);

const tr_template = `
<tr>
    <td class="has-text-centered">
        <form action="/delete_item" method="post">
            <input type="hidden" name="name" value="">
            <button type="submit" class="button is-danger is-outlined is-small">
                <span class="icon is-small">
                    <i class="fa fa-close"></i>
                </span>
            </button>
            <span>&nbsp;</span>
            <span class="has-text-weight-semibold"></span>                                    
        </form>
    </td>
</tr>
`