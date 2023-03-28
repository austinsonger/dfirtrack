// ####################################
// #
// # generic functions
// #
// ####################################

// go to lastpage (used for cancel button)
function lastpage() {
    window.history.back();
}

// close window (used for cancel popup button to close popup window)
function window_close() {
    window.close()
}

// reload parent page if child page is closed (used when save or cancel button is pushed in popup window or if it is closed)
window.onunload = refreshParent;
function refreshParent() {
    window.opener.location.reload();
}

// reload page with possible argument, argument may contain alphanumerical chars as well as '=' and '?'
function reloadWithArgs(arg) {
    // regex with allowed chars
    var allowed = /^[0-9a-zA-Z\?\=]+$/;
    curr_loc = window.location.href;
    // if the argument contains only allowed chars
    if(arg.length > 0 && arg.match(allowed)){
        // if the current url already includes the argument (without the last two chars, to allow for value assignment, for example ?value=0 or =1)
        if(curr_loc.includes(arg.slice(0, -2))){
            // just switch the extension =0 -> =1 and vice versa
            if(curr_loc.includes('=0')){
                window.location.href = curr_loc.replace('=0','=1')
            }
            else if(curr_loc.includes('=1')){
                window.location.href = curr_loc.replace('=1','=0')
            }
        }
        // current url does not include argument -> add it
        else{
            window.location.href = curr_loc + arg
        }
    }
    // argument doest not exist or contains unexpected chars -> just reload page
    else {
        window.location.href = curr_loc
    }
}

// tooltip
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

// ####################################
// #
// # popup window related functions
// #
// ####################################

// TODO: move to 'dfirtrack/dfirtrack_artifacts/static/dfirtrack_artifacts/dfirtrack_artifacts.js'
// popup window for adding artifacttype
var artifacttype_add_popup;
function artifacttype_add_popup() {
    artifacttype_add_popup = window.open("/artifacts/artifacttype/add_popup/", "artifacttype_add_popup", "height=600, width=1000");
}

// popup window for adding casetype
var casetype_add_popup;
function casetype_add_popup() {
    casetype_add_popup = window.open("/casetype/add_popup/", "casetype_add_popup", "height=600, width=1000");
}

// popup window for adding company
var company_add_popup;
function company_add_popup() {
    company_add_popup = window.open("/company/add_popup/", "company_add_popup", "height=600, width=1000");
}

// popup window for adding contact
var contact_add_popup;
function contact_add_popup() {
    contact_add_popup = window.open("/contact/add_popup/", "contact_add_popup", "height=600, width=1000");
}

// popup window for adding domain
var domain_add_popup;
function domain_add_popup() {
    domain_add_popup = window.open("/domain/add_popup/", "domain_add_popup", "height=600, width=1000");
}

// popup window for adding dnsname
var dnsname_add_popup;
function dnsname_add_popup() {
    dnsname_add_popup = window.open("/dnsname/add_popup/", "dnsname_add_popup", "height=600, width=1000");
}

// popup window for adding headline
var headline_add_popup;
function headline_add_popup() {
    headline_add_popup = window.open("/headline/add_popup/", "headline_add_popup", "height=600, width=1000");
}

// popup window for adding location
var location_add_popup;
function location_add_popup() {
    location_add_popup = window.open("/location/add_popup/", "location_add_popup", "height=600, width=1000");
}

// popup window for adding operating system
var os_add_popup;
function os_add_popup() {
    os_add_popup = window.open("/os/add_popup/", "os_add_popup", "height=600, width=1000");
}

// popup window for adding reason
var reason_add_popup;
function reason_add_popup() {
    reason_add_popup = window.open("/reason/add_popup/", "reason_add_popup", "height=600, width=1000");
}

// popup window for adding recommendation
var recommendation_add_popup;
function recommendation_add_popup() {
    recommendation_add_popup = window.open("/recommendation/add_popup/", "recommendation_add_popup", "height=600, width=1000");
}

// popup window for adding serviceprovider
var serviceprovider_add_popup;
function serviceprovider_add_popup() {
    serviceprovider_add_popup = window.open("/serviceprovider/add_popup/", "serviceprovider_add_popup", "height=600, width=1000");
}

// popup window for adding systemtype
var systemtype_add_popup;
function systemtype_add_popup() {
    systemtype_add_popup = window.open("/systemtype/add_popup/", "systemtype_add_popup", "height=600, width=1000");
}

// popup window for adding taskname
var taskname_add_popup;
function taskname_add_popup() {
    taskname_add_popup = window.open("/taskname/add_popup/", "taskname_add_popup", "height=600, width=1000");
}

// TODO: move to 'dfirtrack/dfirtrack_artifacts/static/dfirtrack_artifacts/dfirtrack_artifacts.js' (did not work so far)
// popup window for artifact exporter spreadsheet xls config
var artifact_exporter_spreadsheet_xls_config_popup;
function artifact_exporter_spreadsheet_xls_config_popup() {
        artifact_exporter_spreadsheet_xls_config_popup = window.open("/config/artifact/exporter/spreadsheet/xls/", "artifact_exporter_spreadsheet_xls_config_popup", "height=800, width=1200");
}

// popup window for main config
var main_config_popup;
function main_config_popup() {
    main_config_popup = window.open("/config/main/", "main_config_popup", "height=1200, width=1800");
}

// popup window for system exporter markdown config
var system_exporter_markdown_config_popup;
function system_exporter_markdown_config_popup() {
    system_exporter_markdown_config_popup = window.open("/config/system/exporter/markdown/", "system_exporter_markdown_config_popup", "height=800, width=600");
}

// popup window for system exporter spreadsheet csv config
var system_exporter_spreadsheet_csv_config_popup;
function system_exporter_spreadsheet_csv_config_popup() {
    system_exporter_spreadsheet_csv_config_popup = window.open("/config/system/exporter/spreadsheet/csv/", "system_exporter_spreadsheet_csv_config_popup", "height=800, width=600");
}

// popup window for system exporter spreadsheet xls config
var system_exporter_spreadsheet_xls_config_popup;
function system_exporter_spreadsheet_xls_config_popup() {
    system_exporter_spreadsheet_xls_config_popup = window.open("/config/system/exporter/spreadsheet/xls/", "system_exporter_spreadsheet_xls_config_popup", "height=800, width=1200");
}

// popup window for system importer file csv config
var system_importer_file_csv_config_popup;
function system_importer_file_csv_config_popup() {
    system_importer_file_csv_config_popup = window.open("/config/system/importer/file/csv/", "system_importer_file_csv_config_popup", "height=1200, width=1800");
}

// ####################################
// #
// # go to top of page button
// #
// ####################################

// go to top of page button (onscroll event)
window.onscroll = function() {show_button()};

// go to top of page button (show btn-top if 20px are scrolled down)
function show_button() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("btn-top").style.display = "block";
    } else {
        document.getElementById("btn-top").style.display = "none";
    }
}

// go to top of page button (on click of button)
function go_to_top() {
    document.body.scrollTop = 0; // Safari
    document.documentElement.scrollTop = 0; // Chrome and Firefox
}

// ####################################
// #
// # workflow add and update dynamic artifacts/tasknames
// #
// ####################################

// get empty form as template and save it to global var
var form_container_template = {};

$(function () {

    $('.formsetLoader').each(function() {
        let formset = $(this).attr('id').split('-')[1]
        let totalForms = $(`#id_${formset}-TOTAL_FORMS`).get(0);
        let formNum =  parseInt(totalForms.value);
        form_container_template[formset] = $(`#formset-${formset}-${formNum-1}-container`).clone(true);
    });

    // append template form to formset
    $('.addForm').click(function(event) {
        let formset = $(this).attr('id').split('-')[1]

        let formRegex = RegExp(`${formset}-(\\d){1,3}-`,'g');
        let totalForms = $(`#id_${formset}-TOTAL_FORMS`).get(0);
        let formNum =  parseInt(totalForms.value);

        let form_container = form_container_template[formset].clone(true);
        form_container.removeAttr('id')
        form_container.removeClass('d-none')
        form_container.html(form_container.html().replace(formRegex, `${formset}-${formNum}-`));

        $(`#formset-${formset}-container`).append(form_container);

        totalForms.setAttribute('value', `${formNum+1}`);
    });
});

// ####################################
// #
// # markdown preview
// #
// ####################################

$(function () {
    $('.markdown-preview pre').each(function(i, block){
        hljs.highlightBlock(block);
    });
    $('.markdown-preview code').each(function(i, block){
        hljs.highlightBlock(block);
    });
});

// ####################################
// #
// # dynamic tag selector
// #
// ####################################

// internal tag array
var added_tags = [];

// var tags = {} will be generated within template file

function add_tag(value, label) {
    // add to internal array
    added_tags.push(value)
    // check tag hidden checkbox form
    $(`#hidden_tags input[value='${value}']`).attr( "checked", "" );
    // remove tag from dropdown
    $(`#tag_select option[value='${value}']`).remove()

    // create span
    let tag_span = $('<span>', {text: " "});
    // create tag icon image default light icon
    let tag_img = $('<img>', {
        src: tag_icon_light,
        class: "icon-sm right-distance copy-false"
    });
    // if tag color is white dark icon
    if(tags[value][1] == "white") {
        tag_img.attr("src", tag_icon)
    }
    // create tag button
    let tag_link = $('<a>', {
        text: `${label} x`,
        class: `btn btn-sm round copy-true top-distance btn-${tags[value][1]}`,
        type: 'button'
    });
    // add image to tag button
    tag_link.prepend(tag_img)
    // add remove tag function to tag button
    tag_link.attr("onclick", `remove_tag(this, ${value})`)
    // add tag button to span
    tag_span.append(tag_link)

    // add visual tag to div
    $(`#selected_tags`).append(tag_span);
}

function remove_tag(self, tag_id) {
    // remove tag from div
    self.remove()
    // uncheck tag from hidden checkbox form
    $(`#hidden_tags input[value='${tag_id}']`).removeAttr("checked");
    // add tag to dropdown
    $('#tag_select').append(new Option(tags[tag_id][0], tag_id))
    // remove from internal array
    added_tags.pop(tag_id)
}

$(function () {
    // if site is loaded, iterate over all pre checked tags (hidden checkbox)
    $('#hidden_tags input').each(function() {
        if($(this).is(':checked')) {
            let check_tag_value = $(this).val();
            let checked_tag_label = $(`#tag_select option[value='${check_tag_value}']`).text();
            add_tag(check_tag_value, checked_tag_label);
        }
    });

    // onclick add tag button
    $('#add_tag').click(function(event) {
        // get tag information id and text
        let selected_tag_value = $('#tag_select').val();
        let selected_tag_label = $('#tag_select option:selected').text();
        // check if tag not already set
        if (!added_tags.includes(selected_tag_value) && selected_tag_value != "") {
            // adds tag
            add_tag(selected_tag_value, selected_tag_label);
        }
    });
});

