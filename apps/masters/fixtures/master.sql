-- Create default country
INSERT INTO public.masters_country (id, created_ts, updated_ts, is_active, "name", "country_code", created_by_id, updated_by_id) VALUES
	(1, now(), now(), true, 'India','+91', NULL, NULL),
	(2, now(), now(), true, 'Australia','+50',NULL,NULL);

INSERT INTO public.masters_city (id ,created_ts, updated_ts, is_active, "name", country_id_id, created_by_id, updated_by_id) VALUES
	 (1,now(), now(), true, 'Gujarat',1, NULL,NULL),
	 (2, now(), now(), true,'Maharashtra',1, NULL,NULL),
	 (3,now(), now(), true,'Sydney',2, NULL,NULL),
	 (4,now(), now(), true, 'Canberra',2, NULL,NULL);


