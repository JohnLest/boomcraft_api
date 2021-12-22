DELIMITER |
create trigger after_insert_user after insert
on user for each row
begin
	insert into
	    ressource(name, quantity, idUser, idType)
	values
	    ("wood", 0, new.idUser, 2),
	    ("stone", 0, new.idUser, 2),
	    ("iron", 0, new.idUser, 2),
	    ("food", 0, new.idUser, 2),
	    ("gold", 0, new.idUser, 2),
	    ("worker", 0, new.idUser, 1),
	    ("archer", 0, new.idUser, 1),
	    ("warrior", 0, new.idUser, 1);

end |
DELIMITER ;