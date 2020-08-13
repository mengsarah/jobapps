/*** AJAX ***/
$(document).ready(function() {
    function loadContacts() {
        // this (caller) is a button
        var id = this.getAttribute("value"); // e.g. contacts-3
        var container = document.getElementById(id);
        if (container.innerHTML === "") {
        $.ajax({
            url: $(this).attr("ajax-contacts-url"),
            success: function(data) {
                // data is a json object with one key: contacts
                // and data['contacts'] is:
                // a list of Contact objects in the form of json objects
                contacts = data['contacts'];
                var content = "";
                for (var i = 0; i < contacts.length; i++) {
                    // contacts[i] is a json-ified Contact object
                    var person = contacts[i]['name'] + ", " + contacts[i]['role'];
                    content += "<p>" + person + ": ";
                    if (contacts[i]['email'].length == 0 && contacts[i]['phone'].length == 0) {
                        content += "no additional info";
                    }
                    else {
                        if (contacts[i]['email'].length > 0) {
                            content += contacts[i]['email'];
                        }
                        if (contacts[i]['phone'].length > 0) {
                            if (contacts[i]['email'].length > 0) {
                                content += " and ";
                            }
                            content += contacts[i]['phone'];
                        }
                    }
                    content += "</p>";
                } // end for (each Contact in contacts)
                container.innerHTML = content;
            } // end success function
        }); // end ajax() call
        } // end if contacts div is empty
    } // end loadContacts() definition

    // bind click event handler to contact toggles
    var contact_toggles = document.getElementsByClassName("ajax-contacts");
    for (var i = 0; i < contact_toggles.length; i++) {
        contact_toggles[i].addEventListener("click", loadContacts);
    }
});