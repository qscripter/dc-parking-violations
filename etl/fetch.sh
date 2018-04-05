days=('MONDAY' 'TUESDAY' 'WEDNESDAY' 'THURSDAY' 'FRIDAY')

for i in "${days[@]}"
do
	curl "http://localhost:8080/geoserver/wfs?service=WFS&version=1.1.0&request=GetFeature&typename=dc-streets:street_sweep_centerline&outputFormat=application/json&srsname=EPSG:3857&cql_filter=day_of_week=%$i%27%20AND%20BBOX(geom,-20037508.342789244,0,0,20037508.342789244,%27EPSG:3857%27)" > $i.json
done