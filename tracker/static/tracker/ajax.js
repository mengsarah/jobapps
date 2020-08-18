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
                        if ("email" in contacts[i]) {
                            content += contacts[i]['email'];
                        }
                        if ("phone" in contacts[i]) {
                            if ("email" in contacts[i]) {
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

    function loadCompanyInfo() {
        // this (caller) is a button
        var id = this.getAttribute("value"); // e.g. company-3
        var container = document.getElementById(id);
        if (container.innerHTML === "") {
        $.ajax({
            url: $(this).attr("ajax-company-url"),
            success: function(company) {
                // company is a Company object in the form of a json object
                // whose keys are the fields of a Company object
                var content = "";
                if (company["name"] !== company["full_name"]) {
                    content += "<p>" + company["full_name"] + "</p>";
                }
                if ("website" in company) {
                    content += "<p>" + company["website"] + "</p>";
                }
                if ("about" in company) {
                    // need to do my own line break processing here
                    var about = company["about"];
                    content += "<p>" + about[0];
                    for (var i = 1; i < about.length; i++) {
                        if (about[i] === "") {
                            content += "</p><p>";
                        }
                        else if (about[i-1] === "") {
                            content += about[i];
                        }
                        else {
                            content += "<br />" + about[i];
                        }
                    }
                    content += "</p>";
                } // end if company["about"] exists
                container.innerHTML = content;
            } // end success function
        }); // end ajax() call
        } // end if company div is empty
    } // end loadCompanyInfo() definition

    // bind click event handler to contact toggles
    var contact_toggles = document.getElementsByClassName("ajax-contacts");
    for (var i = 0; i < contact_toggles.length; i++) {
        contact_toggles[i].addEventListener("click", loadContacts);
    }

    // bind click event handler to company info toggles
    var company_toggles = document.getElementsByClassName("ajax-company");
    for (var i = 0; i < company_toggles.length; i++) {
        company_toggles[i].addEventListener("click", loadCompanyInfo);
    }
});