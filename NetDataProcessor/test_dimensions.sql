-- look for new values and add them to the dimensions

select count(distinct vpg.fund_id)
from v_p_g_performance vpg;

select count(distinct dmb.ID)
from dim_managingBody dmb;


-- test dim fund
select distinct vpg.fund_id
from v_p_g_performance vpg
where vpg.fund_id not in (select Fund_ID
						  from dim_fund df);
                          
                          
-- test dim date
select distinct vpg.date
from v_p_g_performance vpg
where vpg.date not in (select dd.Date
						  from dim_date dd);
                          
-- test dim managing body
select distinct vpg.fund_id
from v_p_g_performance vpg
where vpg.fund_id not in (select distinct dm.ID
						  from dim_managingbody dm);
                          
-- test dim manager
select distinct p.num_hevra
from pnet_general p
where p.num_hevra not in (select distinct dm.manager_id	from dim_manager dm)
union
select distinct g.num_hevra
from gnet_general g
where g.num_hevra not in (select distinct dm.manager_id from dim_manager dm);


select *
from pnet_general p
where p.id not in (select distinct dm.ID
						  from dim_managingbody dm);
                          

						
                          
-- test dim channel
select distinct vpg.fund_id
from v_p_g_performance vpg
where vpg.date not in (select dc.ID
						  from dim_channel dc);