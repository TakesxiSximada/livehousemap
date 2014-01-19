;(function(global, $) {

  global.googleMap;

  var mapOptions = {
    zoom: 12,
    center: new google.maps.LatLng(35.683723, 139.754248) // 皇居
  };

  function fetch() {
    $.ajax({
      url: '/livehouse/',
      dataType: 'json',
      data: {
        q: ''
      }
    })
    .done(function(data) {
      console.log(data);
      parse(data);
    })
    .fail(function() {
      // TODO:
      alert('データの取得に失敗しました');
    });
  }

  function parse(data) {
    var lat;
    var lng;
    var name;
    var landmarks;
    _.each(data, function(item) {
      lat = item.lat;
      lng = item.lng;
      name = item.name;
      //landmarks = item.landmarks;
      addMarker(lat, lng, name);
    });
  }

  function addMarker(lat, lng, name) {
    var marker = new google.maps.Marker({
      position: new google.maps.LatLng(lat, lng),
        map: global.googleMap,
        title: name
    });
    return marker;
  }   

  function initialize() {
    global.googleMap = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
    fetch();
  }

  $(function() {
    google.maps.event.addDomListener(window, 'load', initialize);
  });

})(window, jQuery);
