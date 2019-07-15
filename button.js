//REX GODBOUT -Le team (developer)
//Script to execute button functionality via website 


var button = $("#forward");
button.click(function() {
    console.log(button.text());
    if (button.text() === "forward"){
      $.ajax({
      url: "/forward",
      type: "post",
      success: function(response){
        console.log(response);
        button.text("STOP");
        }

      });
    } else {
      $.ajax({
      url: "/STOP",
      type: "post",
      success: function() {
        button.text("forward");

        }
              })
            }
        });

        var button2 = $("#reverse");
        button2.click(function() {
            console.log(button2.text());
            if (button2.text() === "reverse"){
              $.ajax({
              url: "/reverse",
              type: "post",
              success: function(response){
                console.log(response);
                button2.text("STOP");
                }

              });
            } else {
              $.ajax({
              url: "/STOP",
              type: "post",
              success: function() {
                button2.text("reverse");

                }
                      })
                    }
                });

                var button3 = $("#left");
                button3.click(function() {
                    console.log(button3.text());
                    if (button3.text() === "left"){
                      $.ajax({
                      url: "/left",
                      type: "post",
                      success: function(response){
                        console.log(response);
                        button3.text("STOP");
                        }

                      });
                    } else {
                      $.ajax({
                      url: "/STOP",
                      type: "post",
                      success: function() {
                        button3.text("left");

                        }
                              })
                            }
                        });


                        var button4 = $("#right");
                        button4.click(function() {
                            console.log(button4.text());
                            if (button4.text() === "right"){
                              $.ajax({
                              url: "/right",
                              type: "post",
                              success: function(response){
                                console.log(response);
                                button4.text("STOP");
                                }

                              });
                            } else {
                              $.ajax({
                              url: "/STOP",
                              type: "post",
                              success: function() {
                                button4.text("right");

                                }
                                      })
                                    }
                                });
