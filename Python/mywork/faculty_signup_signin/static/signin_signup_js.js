function showForm(formId, btn) {
            // Switch form visibility
            document.querySelectorAll(".form").forEach(form => {
                form.classList.remove("active");
            });
            document.getElementById(formId).classList.add("active");

            // Switch active button
            document.querySelectorAll(".button_style button").forEach(b => {
                b.classList.remove("active");
            });
            btn.classList.add("active");

                // Update header title/subtitle dynamically
            const title = document.getElementById("formTitle");
            const subtitle = document.getElementById("formSubtitle");

            if (formId === "signin") {
                title.textContent = "Faculty Sign In";
                subtitle.textContent = "Welcome back! Sign in to your faculty account.";
            } else {
                title.textContent = "Faculty Sign Up";
                subtitle.textContent = "Create your faculty account to get started.";
            }
        }

        function togglePassword(){
            const input = document.getElementById("password");
            const icon = document.getElementById("toggle_icon");
            
            if(input.type === "password"){
                input.type = "text";
                icon.src = "images/hidden.png";
            }else{
                input.type = "password";
                icon.src = "images/visible.png";
            }

           
        }

        function toggle_Confirm_Password(){
            const confirm_password = document.getElementById("confirm_password");
            const confirm_toggle_icon = document.getElementById("confirm_toggle_icon");
             if(confirm_password.type === "password"){
                confirm_password.type = "text";
                confirm_toggle_icon.src = "images/hidden.png";
            }else{
                confirm_password.type = "password";
                confirm_toggle_icon.src = "images/visible.png";
            }
        }