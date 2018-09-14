#!/usr/bin/python
import jarray
from datetime import datetime
 
params=jarray.array(['Properties',''],java.lang.Object)
sign=jarray.array(['java.lang.String','java.lang.String'],java.lang.String)
logFileName='UpdateSOAInboundDir_'+ sys.argv[1]+'_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'.log'
 
f1=open('/home/iaxdaiso/testwlscripts/python_mbean/' + logFileName,'w+')
soaserver={"xdaiso":"t3://ucolhp1o.csd.disa.mil:7039","xdaipo":"t3://ucolhp1o.csd.disa.mil:7003","odaiso":"t3://ucolhp2a.csd.disa.mil:7008","tdaido":"t3://ucolhp1o.csd.disa.mil:7104","tdaifo":"t3://ucolhp2a.csd.disa.mil:7103","ddaido":"t3://ucolhp2b.csd.disa.mil:8003","ddaico":"t3://ucolhp1p.csd.disa.mil:7003"}
agencyList=['DMA','DMEA','DODEA','DODIG','DOTE','MDA','TMA','WHSFMD','DPMO','DSCA','DSS','DTIC','DTRA','DTSA','OEA','DISA','DCAA','DCMA','USU','OUSDC','DHRA']
####dictSOAPath={"DAIEUDTFSPreValRec8Inbound":"EUD","DAIDTSAuthInbound":"DTS/AUTH"}
##dictSOAPath={"DAIOCGlobalCollectionInbound":["GLOBALCOLLECTION"],"DAIPROJECTKMInbound":["PROJECTKM"],"DAICEFTVendorResponseInbound":["CEFT"],"DAIADSCollReceiptsInbound":["ADS/COLL"],"DTSARReceiptInbound":["DTS/AR"],"DAIARReceiptInbound":["AR/RECEIPT"],"DAIADSPaymentInbound":["ADS"], "DAIBiWeeklyMERInbound":["HR/BIWEEKLYMER"], "DAIPRDSAcceptInbound":["PRDS/ACPT"],"DAIDailyMERInbound":["HR/DAILYMER"], "DAIExchangeRateInbound":["EXCHANGERATE"], "DAIEUDTFSPreValRec8Inbound":["EUD"], "DAIGlobalActivityInbound":["GLOBALACTIVITY"], "DAIGlobalInvoiceInbound":["GLOBALINVOICE"], "DAIPRDSAckInbound":["PRDSACK"], "DAITDDCARSInbound":["TDDCARS"], "DAITDDITSSRFTInbound":["ITS/SRF"], "DAITDDPAMSRFInbound":["PAM/SRF"], "DAIDTSInvoiceInbound":["DTS/INVOICE"], "DAIPRIDEBudgetInbound":["PRIDE/BUDGET"], "DAIProjectClassInbound":["PA/PROJCLASS"], "DAIAXOLPCardInbound":["PCARD/INVOICE"], "DAIEUDTBOPayPreVallnbound":["EUD"], "DAIPCardPOInbound":["PCARD/OBLIGATION"], "DAIFVBudgetInbound":["FV/BUDGET"], "DAIProjectTaskInbound":["PA/PROJECT"], "DaiPaGlobalBillingEventsInbound":["PA/BILL_EVENTS"], "DAIDPASAccountingInbound":["DPAS"], "DAIEmployeeInbound":["HR/EMP"], "DAIInvoiceInbound":["AP/INVOICE"], "DAIPRDSMIPRInbound":["PRDS/ORDER"], "DAIPdsInbound":["PDS"], "DAIPdsAttachInbound":["PDSATTACHMENT"], "DAIEDALOAInbound":["EDA_LOA"], "DAIDTSAuthInbound":["DTS/AUTH"], "DAIGlobalObligationInbound":["GLOBALOBLIGATION"], "DAITDDPAMAckInbound":["PAM/ACK"], "DAITDDReturnRejectInbound":["TDDRETURN"], "DAIWAWFAcceptanceInbound":["WAWF/ACCEPTANCE"], "DAIWAWFInvoiceInbound":["WAWF/INVOICE"],"DAIPAClob":["PA/TX"]}
dictSOAPath={"DAIOCGlobalCollectionInbound":["GLOBALCOLLECTION"],"DAIPROJECTKMInbound":["PROJECTKM"],"DAICEFTVendorResponseInbound":["CEFT"],"DAIADSCollReceiptsInbound":["ADS/COLL"],"DTSARReceiptInbound":["DTS/AR"],"DAIARReceiptInbound":["AR/RECEIPT"],"DAIADSPaymentInbound":["ADS"], "DAIBiWeeklyMERInbound":["HR/BIWEEKLYMER"], "DAIPRDSAcceptInbound":["PRDS/ACPT"],"DAIDailyMERInbound":["HR/DAILYMER"], "DAIExchangeRateInbound":["EXCHANGERATE"], "DAIEUDTFSPreValRec8Inbound":["EUD"], "DAIGlobalActivityInbound":["GLOBALACTIVITY"], "DAIGlobalInvoiceInbound":["GLOBALINVOICE"], "DAIPRDSAckInbound":["PRDSACK","PRDS/ORDERACPTACK"], "DAITDDCARSInbound":["TDDCARS"], "DAITDDITSSRFTInbound":["ITS/SRF"], "DAITDDPAMSRFInbound":["PAM/SRF"], "DAIDTSInvoiceInbound":["DTS/INVOICE"], "DAIPRIDEBudgetInbound":["PRIDE/BUDGET"], "DAIProjectClassInbound":["PA/PROJCLASS"], "DAIAXOLPCardInbound":["PCARD/INVOICE"], "DAIEUDTBOPayPreVallnbound":["EUD"], "DAIPCardPOInbound":["PCARD/OBLIGATION"], "DAIFVBudgetInbound":["FV/BUDGET"], "DAIProjectTaskInbound":["PA/PROJECT"], "DaiPaGlobalBillingEventsInbound":["PA/BILL_EVENTS"], "DAIDPASAccountingInbound":["DPAS"], "DAIEmployeeInbound":["HR/EMP"], "DAIInvoiceInbound":["AP/INVOICE"], "DAIPRDSMIPRInbound":["PRDS/ORDER"], "DAIPdsInbound":["PDS"], "DAIPdsAttachInbound":["PDSATTACHMENT"], "DAIEDALOAInbound":["EDA_LOA"], "DAIDTSAuthInbound":["DTS/AUTH"], "DAIGlobalObligationInbound":["GLOBALOBLIGATION"], "DAITDDPAMAckInbound":["PAM/ACK"], "DAITDDReturnRejectInbound":["TDDRETURN"], "DAIWAWFAcceptanceInbound":["WAWF/ACCEPTANCE"], "DAIWAWFInvoiceInbound":["WAWF/INVOICE"],"DAIPAClob":["PA/TX"]}
try:
    if sys.argv[1].lower() != 'ddaido':
       connect(userConfigFile='/home/iaxdaiso/testwlscripts/configfile.secure',userKeyFile='/home/iaxdaiso/testwlscripts/keyfile.secure',url=soaserver[sys.argv[1].lower()],timeout=300000)
    else:
       connect('weblogic','Welc0me2Oracle!',soaserver[sys.argv[1].lower()])
except Exception,err:
       print >>f1, eachArg + ' failed to connect' +  str(err)
       exit()
custom()
cd('oracle.soa.config')
mydirs = ls(returnMap='true')
for mydir in mydirs:
dirName=java.lang.String(mydir)
if ('SCAComposite.SCAService.SCABinding' in mydir and 'name=AdapterBinding' in mydir and  ('Inbound' in mydir  or 'DAIPAClob' in mydir) and 'partition=DAI_SOA' in mydir) or ('SCAComposite.SCAService' in mydir and 'partition=DAI_SOA' in mydir and 'Inbound' in mydir):
    
  cd(dirName)
  ###cd('oracle.soa.config:SCAComposite.SCAService=InboundFile,revision=1.0,name=AdapterBinding,partition=DAI_SOA,SCAComposite="DAIEUDTFSPreValRec8Inbound",label=soa_29ee5af7-c92b-4163-a560-270dd2070b64,j2eeType=SCAComposite.SCAService.SCABinding,Application=soa-infra')
  try:
                 objectName = get('objectName')
                 ab = ObjectName(objectName)
                 jarray_properties = get('Properties')
                 ##policySName = get('PolicySubjectName')
                 hm = HashMap()
                 ##print >> f1, type(jarray_properties)
                 ##print >> f1, policySName[:policySName.find('/Service')]
                 ##bpelProcessName=policySName[:policySName.find('/Service')]
                 ##bpelProcessName=bpelProcessName[:bpelProcessName.find('/')]
                 bpelProcessName=objectName[objectName.find('SCAComposite="')+14:]
                 bpelProcessName=bpelProcessName[:bpelProcessName.find('"')]
                 ##print >> f1, bpelProcessName
                 if bpelProcessName == sys.argv[2] or sys.argv[2].lower() == 'all':
                  dirPath=''
                  soaInstanceName = sys.argv[1].lower()
                  for instanceName in sys.argv[3:]:
                   for pathName in  dictSOAPath[bpelProcessName]:
                     dirPath = dirPath+'/'+soaInstanceName+'/infgex/dai_inbound/DS_'+instanceName+'/'+ pathName + ';'
                  dirPath=dirPath[:len(dirPath)-1]
                  for i,prop in enumerate(jarray_properties):
                    ##if 'dai_inbound' in prop.toString() and not sys.argv[2] in prop.get('value') :
                     if 'dai_inbound' in prop.toString():
                      ##print >> f1, type(prop)
                      ##print >> f1, prop.getClass().getName()
                      ##print >> f1, prop.getCompositeType().getClass().getName()
                      ##print >> f1, prop.getCompositeType().keySet()
                      for kv in prop.getCompositeType().keySet():
                         ##print >> f1, prop.getCompositeType()
                         ##print >> f1, kv + ':'
                         ##print >> f1, prop.get(kv)
                         ##print >>f1, '----------------------------------------------------------------------'
                         ###t  =CompositeDataSupport(prop.getCompositeType(),{})
                         if kv=='value':
                            hm.put(kv,dirPath)
                         elif kv=="many":
                            hm.put(kv,java.lang.Boolean(False))
                         else:
                            hm.put(kv,prop.get(kv))
                         
                      ##print hm
                      cds =CompositeDataSupport(prop.getCompositeType(),hm)
                      jarray_properties[i]=cds
                     
                      ##params=jarray.array(['Properties',jarray_properties],java.lang.Object)
                      params=jarray.array([],java.lang.Object)
                      ##sign=jarray.array(['java.lang.String','java.lang.String'],java.lang.String)
                      sign=jarray.array([],java.lang.String)
                      ##invoke('setProperty',params,sign);
                      mbs.setAttribute(ab,Attribute('Properties',jarray_properties))
                      invoke('save',params,sign)
                      print >> f1,bpelProcessName
                      print >> f1,dirPath 
                      print >>f1, '-------------------------------------------------------'
  except Exception,err:
                 print >>f1, str(err)
                 print >>f1, '------------------------------------'
  cd('..')
disconnect()
