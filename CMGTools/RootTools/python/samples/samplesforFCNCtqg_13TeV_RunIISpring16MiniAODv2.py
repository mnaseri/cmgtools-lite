import PhysicsTools.HeppyCore.framework.config as cfg

from CMGTools.RootTools.samples.samples_13TeV_RunIISpring16MiniAODv2 import *

import os

TTs = [ 
TTJets,
TTJets_reHLT,
#TTJets_ext, 
#TTJets_LO,
TT_pow_ext3,
TT_pow_ext4,
TTJets_SingleLeptonFromTbar,
TTJets_SingleLeptonFromTbar_ext,
TTJets_SingleLeptonFromT,
TTJets_SingleLeptonFromT_ext,
TTJets_DiLepton,
TTJets_DiLepton_ext,
#TTLep_pow,
TTLep_pow_ext,
]

# Single top cross sections: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma


SingleTop = [
TToLeptons_tch_amcatnlo,
#TBarToLeptons_tch_amcatnlo,
#TToLeptons_tch_amcatnlo_ext,
TToLeptons_tch_powheg,
TBarToLeptons_tch_powheg,
TToLeptons_sch_amcatnlo,
TBar_tWch,
T_tWch,
#T_tWch_DS,
#TBar_tWch_DS,
TGJets,
TGJets_ext,
tZq_ll,
]

### V+jets inclusive (from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV)
VJets = [
WJetsToLNu,
WJetsToLNu_LO,
WJetsToLNu_reHLT,
WJetsToLNu_LO_reHLT,
DYJetsToLL_M10to50,
DYJetsToLL_M10to50_LO,
DYJetsToLL_M5to50_LO,
DYJetsToLL_M50,
DYJetsToLL_M50_LO,
DYJetsToLL_M50_reHLT,
DYJetsToLL_M50_LO_reHLT,
]

# DY njet bins


DYNJets = [ 
DY1JetsToLL_M50_LO,
DY2JetsToLL_M50_LO,
DY3JetsToLL_M50_LO,
DY4JetsToLL_M50_LO,
DY1JetsToLL_M10to50,
DY2JetsToLL_M10to50,
]

# W njet bins

WNJets = [
W1JetsToLNu_LO,
W2JetsToLNu_LO,
W3JetsToLNu_LO,
W4JetsToLNu_LO
]

# DY HT bins:
#https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#DY_Z

DYJetsM50HT = [
DYJetsToLL_M50_HT100to200,
DYJetsToLL_M50_HT100to200_ext,
DYJetsToLL_M50_HT200to400,
DYJetsToLL_M50_HT200to400_ext,
DYJetsToLL_M50_HT400to600,
DYJetsToLL_M50_HT400to600_ext,
DYJetsToLL_M50_HT600toInf,
DYJetsToLL_M50_HT600toInf_ext,
]


#LO

DYJetsM5to50HT = [
DYJetsToLL_M5to50_HT100to200,
DYJetsToLL_M5to50_HT100to200_ext,
DYJetsToLL_M5to50_HT200to400,
DYJetsToLL_M5to50_HT200to400_ext,
DYJetsToLL_M5to50_HT400to600,
DYJetsToLL_M5to50_HT400to600_ext,
DYJetsToLL_M5to50_HT600toInf,
DYJetsToLL_M5to50_HT600toInf_ext
]


### W+jets

WJetsToLNuHT = [
WJetsToLNu_HT100to200,
WJetsToLNu_HT100to200_ext,
WJetsToLNu_HT200to400,
WJetsToLNu_HT200to400_ext,
WJetsToLNu_HT400to600,
WJetsToLNu_HT400to600_ext,
WJetsToLNu_HT600to800,
WJetsToLNu_HT800to1200,
WJetsToLNu_HT800to1200_ext,
WJetsToLNu_HT1200to2500,
WJetsToLNu_HT1200to2500_ext,
WJetsToLNu_HT2500toInf,
WJetsToLNu_HT2500toInf_ext
]



VJetsQQHT=[
WJetsToQQ_HT180,
WJetsToQQ_HT600toInf,
DYJetsToQQ_HT180,
ZJetsToQQ_HT600toInf
]


### QCD


QCDPt = [
#QCD_Pt10to15,
QCD_Pt15to30,
QCD_Pt30to50,
QCD_Pt50to80,
QCD_Pt80to120,
QCD_Pt120to170,
QCD_Pt170to300,
#QCD_Pt300to470,
#QCD_Pt470to600,
#QCD_Pt600to800,
#QCD_Pt800to1000,
#QCD_Pt1000to1400,
#QCD_Pt1400to1800,
#QCD_Pt1800to2400,
#QCD_Pt2400to3200,
#QCD_Pt3200toInf
]



# qcd muenr

QCD_Mu5 = [
QCD_Pt15to20_Mu5,
QCD_Pt20to30_Mu5,
QCD_Pt30to50_Mu5,
QCD_Pt50to80_Mu5,
QCD_Pt80to120_Mu5,
QCD_Pt120to170_Mu5,
QCD_Pt170to300_Mu5,
QCD_Pt300to470_Mu5,
QCD_Pt300to470_Mu5_ext,
QCD_Pt470to600_Mu5,
QCD_Pt470to600_Mu5_ext,
QCD_Pt600to800_Mu5,
QCD_Pt600to800_Mu5_ext,
QCD_Pt800to1000_Mu5,
QCD_Pt800to1000_Mu5_ext,
QCD_Pt1000toInf_Mu5
]



# qcd emenr

QCDPtEMEnriched = [
#QCD_Pt15to20_EMEnriched,
QCD_Pt20to30_EMEnriched,
QCD_Pt30to50_EMEnriched,
QCD_Pt50to80_EMEnriched,
QCD_Pt80to120_EMEnriched,
QCD_Pt120to170_EMEnriched,
QCD_Pt170to300_EMEnriched,
QCD_Pt300toInf_EMEnriched
]

# qcd bctoe

QCDPtbcToE = [
##QCD_Pt_15to20_bcToE,
#QCD_Pt_20to30_bcToE,
#QCD_Pt_30to80_bcToE,
#QCD_Pt_80to170_bcToE,
#QCD_Pt_170to250_bcToE,
#QCD_Pt_250toInf_bcToE
]

# QCD HT bins (cross sections from McM)

QCDHT = [
QCD_HT100to200,
QCD_HT200to300,
QCD_HT200to300_ext,
QCD_HT300to500,
QCD_HT300to500_ext,
QCD_HT500to700,
QCD_HT500to700_ext,
QCD_HT700to1000,
QCD_HT700to1000_ext,
QCD_HT1000to1500,
QCD_HT1000to1500_ext,
QCD_HT1500to2000,
QCD_HT1500to2000_ext,
QCD_HT2000toInf,
QCD_HT2000toInf_ext
]

### DiBosons

# cross section from https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#Diboson


DiBosons = [
WWTo2L2Nu,
WWToLNuQQ,
WWToLNuQQ_ext,
WWTo1L1Nu2Q,
ZZTo2L2Nu,
ZZTo2L2Q,
ZZTo2Q2Nu,
ZZTo2L2Nu,
ZZTo4L,
#ZZTo4L_amcatnlo,
WZTo1L3Nu,
WZTo1L1Nu2Q,
WZTo2L2Q,
WZTo3LNu,
WZTo3LNu_amcatnlo,
VVTo2L2Nu,
WGToLNuG,
WGJets,
ZGJets,
ZNuNuGJets_40130,
ZGTo2LG,
#ZLLGJets_pt130,
WWDouble,
WpWpJJ,
WW,
WZ,
ZZ
]

### TriBosons
# cross section from https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#Triboson

TriBosons = [
WWW,
WZZ,
WWZ,
ZZZ,
]

### TTV

TTV = [
TTWToLNu,
TTWToQQ,
TTW_LO,
TTZToQQ,
TTZToLLNuNu,
TTLLJets_m1to10,
TTZ_LO,
TTGJets
]

### ----------------------------- summary ----------------------------------------

mcSamples = TTs + SingleTop + VJets + DYJetsM50HT + DYJetsM5to50HT + WJetsToLNuHT + WNJets + ZJetsToNuNuHT + QCDHT + QCDPtbcToE + QCDPt + QCDPtEMEnriched + [QCD_Mu15] + QCD_Mu5 +  DiBosons + TriBosons + TTV

samples = mcSamples

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

#Define splitting
for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples)
