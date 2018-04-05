delete from street_sweep_centerline;

insert into street_sweep_centerline (
  street_seg_id,
  day_of_week,
  count,
  side_of_street
)
select
  s.street_seg_id,
  p.day_of_week,
  count(s.street_seg_id),
  p.side_of_street
from
	street_centerline s, street_sweep_violation p
where 
	s.street_seg_id = p.streetseg_id and p.side_of_street is not null and p.ticket_issue_date > to_date('Jan-2013','Mon-YYYY')
group by
	s.street_seg_id, p.side_of_street, p.day_of_week
having
	count(s.street_seg_id) > 3;

update street_sweep_centerline c
set geom = query.geom
from (select geom, street_seg_id from street_centerline s) as query where query.street_seg_id = c.street_seg_id;