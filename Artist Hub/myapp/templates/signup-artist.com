{% extends 'header.html' %}
{% load static %}
{% block content %}
<!DOCTYPE html>
<html>
<head>
  <style type="text/css">
      td{
    font-size: 20px;
    padding:5px;
    }
  </style>
</head>
<body>
<div class="col-lg-12">
    <div class="breadcrumb-text">
    <h2>SIGN UP</h2>
      <div class="bt-option">
      <a href="/">Home</a>
      <span>Sign up</span>
      </div>
    </div>
</div>
<br>
{% if msg %}
  <b style="color:Green">{{msg}}</b>
{% endif %}
<form method="post" action="{% url 'signup' %}" enctype="multipart/form-data">
    {% csrf_token %}
    <table width="70%" align="center">

      <tr>
        <td width="25%">First Name </td>
        <td><input type="text" name="fname" class="form-control" placeholder="Enter First Name"></td>
      </tr>

      <tr>
        <td>Last Name </td>
        <td><input type="text" name="lname" class="form-control" placeholder="Enter Last Name" ></td>
      </tr>

      <tr>
        <td>Email ID </td>
        <td><input type="text" name="email" class="form-control" id="email" placeholder="Enter Email" required></td>
        <span id="email_error"></span>
      </tr>

      <tr>
        <td>Mobile Number </td>
        <td><input type="text" name="mobile" class="form-control" id="mobile" placeholder="Enter Mobile" required></td>
        <span id="mobile_error"></span>
      </tr>

      <tr>
        <td>Address </td>
        <td><input type="textarea" name="address" class="form-control" placeholder="Enter Address">
      </tr>

      <tr>
        <td>About yourself </td>
        <td><input type="textarea" name="about" class="form-control" placeholder="About yourself">
      </tr>

      <tr>
        <td>Facebook</td>
        <td><input type="text" name="facebook" class="form-control" placeholder="Enter Facebook Link" ></td>
      </tr>

      <tr>
        <td>Instagram</td>
        <td><input type="text" name="instagram" class="form-control" placeholder="Enter Instagram Link" ></td>
      </tr>

      <tr>
        <td>Twitter </td>
        <td><input type="text" name="twitter" class="form-control" placeholder="Enter T witter Link" ></td>
      </tr>


      <tr>
        <td> Password</td>
        <td><input type="password" name="password" class="form-control" id="cpwd" placeholder="Enter Password"></td>
        <span id="confirm_pwd_error"></span>
      </tr>
      
      <tr>
        <td>Confirm Password</td>
        <td><input type="password" name="cpassword" class="form-control" placeholder="Enter Confirm Password"></td>
      </tr>
      <tr>
          <td>Profile Picture</td>
          <td class="form-control"><input class="input" type="file" name="profile_pic" ></td>
      </tr>    

      <tr>
        <td colspan="2" align="center" >
          <input type="submit" name="action" value="SIGNUP" class="btn btn-primary btn-block" style="width:100%">
        </td>
      </tr>

      <tr>
        <td colspan="2" align="right">Already Registered ?
          <a href="{% url 'login' %}"><input type="button" name="action" value="Click to Login" class="btn btn-link"></a>
        </td>
      </tr>
</table> 
</form>     
</center>



</body>
</html>

{% endblock %}