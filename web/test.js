var wmsSource = new ol.source.TileWMS({
  url: 'http://localhost:8080/geoserver/wms',
  params: {
    'LAYERS': 'dc_data:street_violation_centerline',
    'CQL_FILTER': "violation_code='P039'"
  },
  serverType: 'geoserver',
  crossOrigin: 'anonymous'
});

var wmsLayer = new ol.layer.Tile({
  source: wmsSource
});

var map = new ol.Map({
  view: new ol.View({
    center: [-8574682.840579, 4709585.127943],
    zoom: 13
  }),
  layers: [
    new ol.layer.Tile({
      source: new ol.source.Stamen({
        layer: 'toner-lite'
      })
    }),
    wmsLayer
  ],
  target: 'map'
});

$(document).ready(init);

function init() {
  $('#day-select').html(buildParkingCodeHtml());
  $('#day-select').on('change', function (e) {
    var code = $('#day-select option:selected').val();
    var wmsSource = new ol.source.TileWMS({
      url: 'http://localhost:8080/geoserver/wms',
      params: {
        'LAYERS': 'dc_data:street_violation_centerline',
        'CQL_FILTER': "violation_code='" + code + "'"
      },
      serverType: 'geoserver',
      crossOrigin: 'anonymous'
    });
    wmsLayer.setSource(wmsSource);
  });
}

function buildParkingCodeHtml() {
  return _.map(parkingCodes, function (o) {
    return '<option value="' + o.code + '">' + o.description + '</option>';
  }).join('');
}