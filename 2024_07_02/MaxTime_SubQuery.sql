select * from ubike_data 
	where (sna,updatetime) 
	in (select sna,max(updatetime) from ubike_data group by sna)
--
select d.MaxUpdateTime,o.UpdateTime,* 
	from ubike_data o join 
	(select max(updatetime) MaxUpdateTime,sna from ubike_data group by sna) d on o.sna=d.sna
