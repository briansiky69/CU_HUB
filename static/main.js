$(document).ready(function() {
    $("#contact-form").on("submit", function(event) {
      event.preventDefault();
  
      var name = $("#name").val();
      var email = $("#email").val();
      var message = $("#message").val();
  
      $.ajax({
        url: "/contact",
        method: "POST",
        data: {
          name: name,
          email: email,
          message: message
        },
        success: function(response) {
          alert("Message sent successfully!");
          $("#contact-form")[0].reset();
        },
        error: function(error) {
          alert("Failed to send message. Please try again.");
        }
      });
    });
  });