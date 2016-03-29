// Structure of the tree (TIER1 View) used in the EGI Accounting Portal
d.add(0,-1,'Hierarchical Tree');
d.add(1,0,'Tier1','/tier1.php');
d.add(10,1,'CA-TRIUMF','/tier1.php?Path=1.2');
d.add(20,1,'CH-CERN','/tier1.php?Path=1.1');
d.add(30,1,'DE-KIT','/tier1.php?Path=1.4');
d.add(40,1,'ES-PIC','/tier1.php?Path=1.11');
d.add(50,1,'FR-CCIN2P3','/tier1.php?Path=1.3');
d.add(60,1,'IT-INFN-CNAF','/tier1.php?Path=1.5');
d.add(70,1,'KR-KISTI-GSDC','/tier1.php?Path=1.8');
d.add(80,1,'NDGF','/tier1.php?Path=1.7');
d.add(90,1,'NL-T1','/tier1.php?Path=1.6');
d.add(100,1,'NRC-KI-T1','/tier1.php?Path=1.9');
d.add(110,1,'RU-JINR-T1','/tier1.php?Path=1.10');
d.add(120,1,'TW-ASGC','/tier1.php?Path=1.12');
d.add(130,1,'UK-T1-RAL','/tier1.php?Path=1.13');
d.add(140,1,'US-FNAL-CMS','/tier1.php?Path=1.14');
d.add(150,1,'US-T1-BNL','/tier1.php?Path=1.15');
d.add(2,0,'Tier2','/tier2.php','Click to access to the Tier2 View','_top','dtree/dtreeimg/folder.png');
d.add(3,0,'Countries','/country.php','Click to access to the Countries View','_top','dtree/dtreeimg/folder.png');
d.add(4,0,'EMI3','/show.php','Click to access to the EMI3 View','_top','','',true);
d.add(5,0,'EGI','/egi.php','Click to access to the EGI View','_top','','',true);
d.add(6,0,'OSG','/osg.php','Click to access to the OSG View','_top','dtree/dtreeimg/folder.png');
d.add(8,0,'UNREGISTERED','/unreg.php','Click to access to the Unregistered View','_top','dtree/dtreeimg/folder.png');
d.add(9,0,'VO_Discipline','/vodis.php','Click to access to the VO_Discipline View','_top','dtree/dtreeimg/folder.png');
d.add(7,0,'VO_Metrics','/vomet.php','Click to access to the VO_Metrics View');
d.add(10,0,'CUSTOM_view','/custom.php','Click to access to the Custom View');

// Identity number for the TIER1 node
var tier1id=1;
d.add(11,0,'Cloud','/cloud.php','Click to access to the Cloud View','_top','','',true);
d.add(12,0,'Cloud Tier1','/cloud_tier1.php','Click to access to the Cloud TIER1 View','_top','','',true);
d.add(13,0,'Cloud Tier2','/cloud_tier2.php','Click to access to the Cloud TIER2 View','_top','','',true);
