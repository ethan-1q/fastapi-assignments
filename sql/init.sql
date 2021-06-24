create database IF NOT EXISTS fastapi_assignments;

use fastapi_assignments;

CREATE TABLE IF NOT EXISTS krew (
	ldap_id VARCHAR(128) primary key,
	profile_image VARCHAR(128),
	identityDisplayName VARCHAR(128),
	deptName VARCHAR(32),
	deptCode VARCHAR(32),
	deptMainYn VARCHAR(32),
	displayName VARCHAR(32),
	personName VARCHAR(32),
	emailId VARCHAR(128),
	deptPathCode VARCHAR(128),
	deptPathName VARCHAR(128),
	parentDeptCode VARCHAR(128),
	parentDeptName VARCHAR(128),
	companyCodeAccount VARCHAR(128),
	concurrentOffice JSON,
	employeeNo VARCHAR(32),
	gradeName VARCHAR(32),
	gradeLevel SMALLINT
);
