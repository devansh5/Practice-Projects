var form =document.getElementById('addForm');

var itemlist=document.getElementById('items');

// all the filter elements

var filter =document.getElementById('filter')

filter.addEventListener('keyup',searchElements);

form.addEventListener('submit',addItem);

// deleting the item

itemlist.addEventListener('click',removeItem);



function addItem(e){
    e.preventDefault();
    var input=document.getElementById('inputtext').value;
    var li =document.createElement('li');

    li.className='list-group-item';

    li.appendChild(document.createTextNode(input));

    itemlist.appendChild(li);

    var delbtn=document.createElement('button');
    delbtn.className='btn btn-danger btn-sm float-right delete'

    delbtn.appendChild(document.createTextNode('X'));

    li.appendChild(delbtn);
   
}

function removeItem(e){
    if(e.target.classList.contains('delete'))
    {
        var li=e.target.parentElement;
        itemlist.removeChild(li);
    }
}

function searchElements(e){
    var text=e.target.value.toLowerCase();
    var items=itemlist.getElementsByTagName('li');

    // conver collection to an array

    Array.from(items).forEach(function(item){
        var itemName=item.firstChild.textContent;
        if(itemName.toLowerCase().indexOf(text)!=-1){
            item.style.display="block";
        }else{
            item.style.display="none";
        }
    })
    
}