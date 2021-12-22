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