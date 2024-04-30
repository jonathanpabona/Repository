$(document).ready(function() {
    $(document).on('change', '.type', function() {
        // Your action here
        var data = $(this).val()
        var checkbox_data = []
        $('.selected_cars:checked').each(function() {
            checkbox_data.push($(this).val());
        });
    });
    $(document).on('change', '.selected_cars', function() {
        var checkedCheckboxes = $('.selected_cars:checked');
        var checkboxValues = []
        checkedCheckboxes.each(function() {
            checkboxValues.push($(this).val());
        });
        if (checkedCheckboxes.length > 2) {
            console.log(checkedCheckboxes.first().val())
            checkboxValues.shift()
            console.log(checkboxValues)
        }



    });
    $("#sortable").sortable({
        update: function(event, ui) {
            var order = $(this).sortable('toArray', { attribute: 'data-car-order' })
            var sort_order = order.sort(function(a, b) {
                                return a - b;
                            });
            var id = $(this).sortable('toArray', { attribute: 'data-car-id' })
            $.ajax({
                url: url,
                type: 'POST',
                data: { id: id, order: sort_order, csrfmiddlewaretoken: csrf },
                success: function(response) {
                },
                error: function(xhr, status, error) {
                    console.error("Error updating order:", error);
                }
            });
        }
    });
    $("#sortable").disableSelection();
});