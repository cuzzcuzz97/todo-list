function DeleteTask() {
    let confirmAction = confirm("Are you sure to Delete?");
    if (confirmAction) {
      alert("successfully Delete");
    } else {
      alert("canceled");    
      return false;
    }
  }


