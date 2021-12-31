DELIMITER |
create trigger after_insert_user after insert
on user for each row
begin
	insert into
	    resource(id_type_res, id_name_res, id_user, quantity)
	values
	    (1, 8, new.id_user, 0),
	    (1, 7, new.id_user, 0),
	    (1, 6, new.id_user, 0),
	    (2, 5, new.id_user, 0),
	    (2, 4, new.id_user, 0),
	    (2, 3, new.id_user, 0),
	    (2, 2, new.id_user, 0),
	    (2, 1, new.id_user, 0);
end |
DELIMITER ;