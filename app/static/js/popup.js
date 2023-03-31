document.addEventListener('DOMContentLoaded', () => {
    // Functions to open and close a modal
    function openModal($el, modal) {
      if(modal === 'modal-create-item'){
        var category = document.getElementById("categories");
        category = category.options[category.selectedIndex].text
        if (category === "-- select a category --"){
          return;
        }
        document.getElementById('item-popup-title').innerText = 'Create ' + category
        var formfield = document.querySelector('#item-create-from > .modal-card-body')
        formfield.innerHTML = ""+item_name+item_desc+item_price+item_seller+item_image
        var type = document.createElement("input");
        type.type = "hidden"
        type.name = "type"
        type.value = category
        formfield.appendChild(type)
        if(category === 'Clothing'){
          formfield.innerHTML+=item_size+item_color
        } 
        else if(category === 'Computer Component'){
          formfield.innerHTML+=item_spec
        }
        else if(category === 'Monitor'){
          formfield.innerHTML+=item_spec
        }       
      }
      $el.classList.add('is-active');
    }
  
    function closeModal($el) {
      $el.classList.remove('is-active');
    }
  
    function closeAllModals() {
      (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
      });
    }
  
    // Add a click event on buttons to open a specific modal
    (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
      const modal = $trigger.dataset.target;
      const $target = document.getElementById(modal);
      $trigger.addEventListener('click', () => {
        openModal($target, modal);
      });
    });
  
    // Add a click event on various child elements to close the parent modal
    (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
      const $target = $close.closest('.modal');
  
      $close.addEventListener('click', () => {
        closeModal($target);
      });
    });
  
    // Add a keyboard event to close all modals
    document.addEventListener('keydown', (event) => {
      const e = event || window.event;
  
      if (e.keyCode === 27) { // Escape key
        closeAllModals();
      }
    });
  });

const item_name = `
<div class="field">
    <label class="label has-text-left">Name</label>
    <div class="field control has-icons-left has-icons-right">
        <input class="input" type="text" name="name" placeholder="Name" value="">
        <span class="icon is-small is-left">
            <i class="fa fa-cube"></i>
        </span>
    </div>
</div>
`

const item_desc = `
<div class="field">
    <label class="label has-text-left">Description</label>
    <div class="field control has-icons-left has-icons-right">
        <input class="input" type="text" name="desc" placeholder="Description" value="">
        <span class="icon is-small is-left">
            <i class="fa fa-quote-left"></i>
        </span>
    </div>
</div>
`
const item_price = `
<div class="field">
    <label class="label has-text-left">Price</label>
    <div class="field control has-icons-left has-icons-right">
        <input class="input" type="int" name="price" placeholder="0" value="">
        <span class="icon is-small is-left">
            <i class="fa fa-money"></i>
        </span>
    </div>
</div>
`
const item_seller = `
<div class="field">
    <label class="label has-text-left">Seller</label>
    <div class="field control has-icons-left has-icons-right">
        <input class="input" type="text" name="seller" placeholder="Seller" value="">
        <span class="icon is-small is-left">
            <i class="fa fa-suitcase"></i>
        </span>
    </div>
</div>
`
const item_image = `
<div class="field">
    <label class="label has-text-left">Image URL</label>
    <div class="field control has-icons-left has-icons-right">
        <input class="input" type="text" name="image" placeholder="URL" value="">
        <span class="icon is-small is-left">
            <i class="fa fa-file-image-o"></i>
        </span>
    </div>
</div>
`
const item_size = `
<div class="field">
    <label class="label has-text-left">Size</label>
    <div class="field control has-icons-left has-icons-right">
        <input class="input" type="text" name="size" placeholder="Size" value="">
        <span class="icon is-small is-left">
            <i class="fa fa-expand"></i>
        </span>
    </div>
</div>
`
const item_color = `
<div class="field">
    <label class="label has-text-left">Color</label>
    <div class="field control has-icons-left has-icons-right">
        <input class="input" type="text" name="color" placeholder="Color" value="">
        <span class="icon is-small is-left">
            <i class="fa fa-paint-brush"></i>
        </span>
    </div>
</div>
`
const item_spec =  `
<div class="field">
    <div class="columns">
      <div class="column">
        <label class="label has-text-left">Identifier</label>
        <div class="field control has-icons-left has-icons-right">
          <input class="input" type="text" name="ident" placeholder="Identifier" value="">
          <span class="icon is-small is-left">
              <i class="fa fa-info"></i>
          </span>
        </div>
      </div>
      <div class="column">
        <label class="label has-text-left">Amount</label>
        <div class="field control has-icons-left has-icons-right">
          <input class="input" type="int" name="amount" placeholder="0" value="">
          <span class="icon is-small is-left">
              <i class="fa fa-slack"></i>
          </span>
        </div>
      </div>
      <div class="column">
        <label class="label has-text-left">Unit</label>
        <div class="field control has-icons-left has-icons-right">
          <input class="input" type="text" name="unit" placeholder="Unit" value="">
          <span class="icon is-small is-left">
              <i class="fa fa-cog"></i>
          </span>
        </div>
      </div>
    </div>
</div>
`