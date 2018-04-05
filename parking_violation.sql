-- Table: public.parking_violation

-- DROP TABLE public.parking_violation;

CREATE TABLE public.parking_violation
(
  id integer NOT NULL DEFAULT nextval('parking_violation_id_seq'::regclass),
  x numeric,
  y numeric,
  day_of_week character varying(255),
  holiday integer,
  week_of_year integer,
  month_of_year integer,
  issue_time integer,
  violation_code character varying(255),
  violation_description character varying(255),
  location character varying(255),
  rp_plate_state character varying(255),
  body_style character varying(255),
  address_id integer,
  streetseg_id integer,
  xcoord integer,
  ycoord integer,
  ticket_issue_date timestamp with time zone
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.parking_violation
  OWNER TO qscripter;

-- Index: public.month_of_year

-- DROP INDEX public.month_of_year;

CREATE INDEX month_of_year
  ON public.parking_violation
  USING btree
  (month_of_year);

-- Index: public.violation_code

-- DROP INDEX public.violation_code;

CREATE INDEX violation_code
  ON public.parking_violation
  USING btree
  (violation_code COLLATE pg_catalog."default");

