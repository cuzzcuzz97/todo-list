function DeleteTask() {
    let confirmAction = confirm("Are you sure to Delete?");
    if (confirmAction) {
      alert("successfully Delete");
    } else {
      alert("canceled");    
      return false;
    }
  }

function Complete(clicked_id) { 
  $(clicked_id).load(window.location.href=("form/complete/"+clicked_id))
  // window.location.href=("form/complete/"+clicked_id)
}