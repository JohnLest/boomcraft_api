CREATE VIEW v_resource AS
SELECT
	r.id_res,
    r.id_user,
    tr.name AS type,
    nr.name AS resource,
    r.quantity
FROM resource AS r
INNER JOIN type_resource as tr ON r.id_type_res = tr.id_type_res
INNER JOIN name_resource as nr ON r.id_name_res = nr.id_name_res;


create view v_weight_resource as
SELECT
	wr.id_weight_res,
    wr.id_name_res,
    nr.name,
    wr.weight
from weight_resource AS wr
inner join name_resource as nr on nr.id_name_res = wr.id_name_res;