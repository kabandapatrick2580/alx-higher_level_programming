$(document).ready(function() {
    $('#add_item').click(() => {
      const newItem = $('<li>Item</li>');
      $('ul.my_list').append(newItem);
    });
  });
  