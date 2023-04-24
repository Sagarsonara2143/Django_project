
		function checkFname() 
		{
			var f=document.frm.fname.value;
			var re=/^[A-Za-z]+$/;
			if (f=="")
			{
				document.getElementById('fname').innerHTML="Enter First Name";
			}
			else if(!re.test(f))
			{
				document.getElementById('fname').innerHTML="Enter Only Alphabets";
			}
			else
			{
				document.getElementById('fname').innerHTML="";
			}
		}


		function checkLname()
		{
			var l= document.frm.lname.value;
			var re = /^[A-Za-z]+$/;

			if (l=="")
			{
				document.getElementById('lname').innerHTML="Enter Last Name";
			}
			else if(!re.test(l))
			{
				document.getElementById('lname').innerHTML="Enter only Alphabets";
			}
			else
			{
				document.getElementById('lname').innerHTML="";
			}

		}

		function checkEmail()
		{
			var e=document.frm.email.value;
			var re=/^[A-Za-z0-9._-]+@[A-Za-z]+\.+[A-Za-z]{2,4}$/;
			if(e=="")
			{
				document.getElementById('email').innerHTML="Enter Email ID";
			}
			else if(!re.test(e))
			{
				document.getElementById('email').innerHTML="Please Enter Correct Email ID";
			}
			else
			{
				document.getElementById('email').innerHTML="";	
			}
		}