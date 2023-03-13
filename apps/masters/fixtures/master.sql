-- Create default country
INSERT INTO public.countries (id,"name",country_code,creation_date,update_date,created_by,updated_by) values
	(1,'India','+91', now(),NULL,NULL,NULL),
	(2,'Australia','+61', now(),NULL,NULL,NULL);

INSERT INTO public.cities (id, "name",country_id,creation_date,update_date,created_by,updated_by) VALUES
	 (1,'Gujarat',1, now(),NULL,NULL,NULL),
	 (2,'Maharashtra',1,now(),NULL,NULL,NULL),
	 (3,'Sydney',2,now(),NULL,NULL,NULL),
	 (4,'Canberra',2,now(),NULL,NULL,NULL);

