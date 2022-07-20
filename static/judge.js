function judge(){
   var user = document.getElementById('user_name').value;
   var pass = document.getElementById('password').value;
   if (user==''||pass==''){
   alert("hhh");
   return false;
   }
   else{
   return true;
   }
  }