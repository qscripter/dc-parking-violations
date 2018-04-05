create materialized view street_violation_centerline as
select
  s.streetsegid,
  p.violation_code,
  s.wkb_geometry as geom,
  s.st_name,
  count(s.streetsegid)
from
  street_centerline s, parking_violation p
where
  s.streetsegid = p.streetseg_id and
  p.violation_code is not null
group by
  s.streetsegid,
  p.violation_code,
  s.wkb_geometry,
  s.st_name
;