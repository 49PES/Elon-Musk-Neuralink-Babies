//console.log(data);

// Get the reference to the <ul> element
var listElement = document.getElementById('list');

// Loop through the events and dynamically create <li> elements
data.forEach(function(event) {
  // Create a new list item element
  var listItem = document.createElement('li');
  listItem.classList.add('list-group-item');
  
  // Set the content of the list item with event details
//   listItem.textContent = 'ID: ' + event[0] + ', User: ' + event[1] + ', Content: ' + event[2] + ', Points: ' + event[3];
listItem.innerHTML += listItem.innerHTML += `<div class="my-3 py-3 shadow list-group-item" id="list${event[0]}">
<div class="row">
  <div class="col-1">
    <input class="" type="checkbox" id="check${event[0]}" onclick="done(${event[0]})">
  </div>
  <div class="col-6">
    <span class="h4" id="text${event[0]}">${event[2]}</span>
  </div>
  <div class="col-4">
    <h5>Points: ${event[3]}</h5>
    <form action="/delete" method="post">
        <input type="hidden" name="listId" value="${event[0]}">
        <input type="hidden" name="points" value="${event[3]}">
        <button type="submit" class="btn btn-dark">Delete</button>
      </form>
  </div>
</div>
</div>`;

  // Append the list item to the <ul> element
  listElement.appendChild(listItem);
});

let list= document.getElementById("list");

done=(listId)=>{ 
    let checkbox = document.getElementById(`check${listId}`);
    let current = document.getElementById(`text${listId}`);
    let classExit=current.classList.contains("text-decoration-line-through");
    if (classExit == true) {
        current.classList.remove("text-decoration-line-through");
    }else{
        current.classList.add("text-decoration-line-through");
    }
}