-- create view view_p_g_performance from 'pnet_general' & 'gnet_general'
create or replace view v_p_g_performance as
select
	p.id as 'fund_id',
    p.tkufat_divuach as 'date',
    p.hafkadot_llo_haavarot as 'deposits_no_transfers',
    p.mshichot_llo_haavarot as 'redemptions_no_transfers',
    p.haavarot_bein_hakupot as 'transfers_between_funds',
    p.tzvira_neto as 'net_accumulation',
    p.yitrat_nchasim_lsof_tkufa as 'total_fair_value',
    p.shiur_dmei_nihul_aharon as 'last_managing_fee',
    p.tsua_nominalit_bruto_hodshit as 'yield_monthly_nominal',
    p.tsua_mitzt_mi_thilat_shana as 'yield_cum_bgn_year',
    p.tsua_memuzaat_36_hodashim as 'yield_avg_36_months',
    p.tsua_memuzaat_60_hodashim as 'yield_avg_60_months',
    p.tsua_mitztaberet_36_hodashim as 'yield_cum_36_months',
    p.tsua_mitztaberet_60_hodashim as 'yield_cum_60_months',
    p.tsua_shnatit_memuzaat_3_shanim as 'yield_avg_3_yrs',
    p.tsua_shnatit_memuzaat_5_shanim as 'yield_avg_5_yrs',
    p.stiat_teken_36_hodashim as 'stdev_36_months',
    p.stiat_teken_60_hodashim as 'stdev_60_months',
    p.alpha_shnati as 'alpha_year',
    p.sharp_tsua_hetzyonit_anaf as 'sharp_industry',
    p.sharp_tsua_hetzyonit_all as 'sharp_all_funds',
    p.sharp_ribit_hasrat_sikun as 'sharp_free_risk',
    p.yahas_nezilut as 'liquidity_ratio'
from pnet_general p
union all
select 
	g.id,
    g.tkufat_divuach,
    g.hafkadot_llo_haavarot,
    g.mshichot_llo_haavarot,
    g.haavarot_bein_hakupot,
    g.tzvira_neto,
    g.yitrat_nchasim_lsof_tkufa,
    g.shiur_dmei_nihul_aharon,
    g.tsua_nominalit_bruto_hodshit,
    g.tsua_mitzt_mi_thilat_shana,
    g.tsua_memuzaat_36_hodashim,
    g.tsua_memuzaat_60_hodashim,
    g.tsua_mitztaberet_36_hodashim,
    g.tsua_mitztaberet_60_hodashim,
    g.tsua_shnatit_memuzaat_3_shanim,
    g.tsua_shnatit_memuzaat_5_shanim,
    g.stiat_teken_36_hodashim,
    g.stiat_teken_60_hodashim,
    g.alpha_shnatit,
    g.sharp_anaf,
    g.sharp_kol_hakupot,
    g.sharp_ribit_hasrat_sikun,
    g.yahas_nezilut
from gnet_general g;

-- query and test the view