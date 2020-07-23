create database api_test;
use api_test;

CREATE TABLE case_info(
	case_id varchar(10),
	case_name varchar(100) not NULL,
	is_run varchar(4) not null DEFAULT '是',
	PRIMARY KEY(case_id)
)DEFAULT  CHARSET = 'utf8';


CREATE TABLE case_step_info(
	case_id VARCHAR(10) not null,
	case_step_name VARCHAR(20) not null,
	api_id VARCHAR(100) not null,
	get_value_type VARCHAR(20) not null,
	variable_name VARCHAR(20) not null,
	get_value_code VARCHAR(100) not null,
	excepted_result_type VARCHAR(20) not null,
	excepted_result VARCHAR(300),
	CONSTRAINT fk_case_id FOREIGN KEY(case_id) REFERENCES case_info(case_id)
)DEFAULT  CHARSET = 'utf8';

create table api_info(
	api_id VARCHAR(100),
	api_name VARCHAR(100),
	api_request_type VARCHAR(10),
	api_request_url VARCHAR(200),
	api_url_params VARCHAR(200),
	api_post_data VARCHAR(1000),
	PRIMARY key(api_id)	
)DEFAULT  CHARSET = 'utf8';

INSERT INTO case_info values('case01','测试能否正确执行获取access_token接口','是');
INSERT INTO case_info values('case02','测试能否正确新增用户标签','是');
INSERT INTO case_info values('case03','测试能否正确删除用户标签','是');

INSERT INTO api_info values('api_0001','获取access_token接口','get','/cgi-bin/token','{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}','');
INSERT INTO api_info values('api_0002','创建标签接口','post','/cgi-bin/tags/create','{"access_token":${token}}','{"tag" : {"name" : "衡东9999"}}');
INSERT INTO api_info values('api_0003','删除标签接口','post','/cgi-bin/tags/delete','{"access_token":${token}}','{"tag":{"id":408}}');

INSERT INTO case_step_info values('case01','step_01','api_0001','无','','','json键是否存在','access_token,expires_in');
INSERT INTO case_step_info values('case02','step_01','api_0001','json取值','token','$.access_token','正则匹配','{"access_token":"(.+?)","expires_in":(.+?)}');
INSERT INTO case_step_info values('case02','step_02','api_0002','无','','','json键值对','{"errcode":45158}');
INSERT INTO case_step_info values('case03','step_01','api_0001','json取值','token','$.access_token','正则匹配','{"access_token":"(.+?)","expires_in":(.+?)}');
INSERT INTO case_step_info values('case03','step_02','api_0003','无','','','json键值对','{"errcode":0,"errmsg":"ok"}');

select * from case_step_info;

select case_info.case_id,case_info.case_name,case_info.is_run,case_step_info.case_step_name,api_info.api_name,api_info.api_request_type,api_info.api_request_url,api_info.api_url_params,api_post_data,case_step_info.get_value_type,case_step_info.variable_name,case_step_info.get_value_code,case_step_info.excepted_result_type,case_step_info.excepted_result
from case_step_info 
LEFT JOIN case_info on case_step_info.case_id = case_info.case_id
LEFT JOIN api_info on case_step_info.api_id = api_info.api_id 
where case_info.is_run = '是'
order by case_info.case_id,case_step_info.case_step_name;