$(document).ready(function () {
  const amenities = {};

  function updateApiStatus() {
    $.get('http://0.0.0.0:5001/api/v1/status/', function(data) {
      if (data.status === 'OK') {
        $('#api_status').addClass('available');
      } else {
	$('#api_status').removeClass('available');
      }
    });
  }

  updateApiStatus();

  $('input[type=checkbox]').change(function() {
  const amenityId = $(this).data('amenity-id');

    if ($(this).is(':checked')) {
      amenityies[amenityId] = $(this).data('amenity-name');
    } else {
      delete amenities[amenityId];
    }

    const amenitiesList = Object.values(amenities).join(', ');
    $('div.Amenities > h4').text(amenitiesList);
    });

  setInterval(updateApiStatus, 5000);

  });
