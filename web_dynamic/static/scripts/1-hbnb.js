$(document).ready(function () {
  const amenities = {};

  $('input[type=checkbox]').change(function() {
  const amenityId = $(this).data('amenity-id');

  if ($(this).is(':checked')) {
    amenities[amenityId] = $(this).data('amenity-name');
  } else {
    delete amenities[amenityId];
  }

  const amenitiesList = Object.values(amenities).join(', ');
  $('div.Amenities > h4').text(amenitiesList);
  
  });

});	
