import PhysicsTools.HeppyCore.framework.config as cfg
from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *

import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### ----------------------------- Zero Tesla run  ----------------------------------------

dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"  # use environmental variable, useful for instance to run on CRAB
json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

run_range = (273158, 284044)
label = "_runs%s_%s"%(run_range[0], run_range[1])


dataSamples_Run2016_v1 = []

### ----------------------------- Run2016B PromptReco v2 ----------------------------------------

SingleElectron_Run2016B_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016B_PromptReco_v2", "/SingleElectron/Run2016B-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016B_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016B_PromptReco_v2"    , "/SingleMuon/Run2016B-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016B_v2 = [SingleElectron_Run2016B_PromptReco_v2, SingleMuon_Run2016B_PromptReco_v2]

### ----------------------------- Run2016C PromptReco v2 ----------------------------------------

SingleElectron_Run2016C_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016C_PromptReco_v2", "/SingleElectron/Run2016C-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016C_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016C_PromptReco_v2"    , "/SingleMuon/Run2016C-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016C_v2 = [SingleElectron_Run2016C_PromptReco_v2, SingleMuon_Run2016C_PromptReco_v2]


### ----------------------------- Run2016D PromptReco v2 ----------------------------------------

SingleElectron_Run2016D_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016D_PromptReco_v2", "/SingleElectron/Run2016D-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016D_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016D_PromptReco_v2"    , "/SingleMuon/Run2016D-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016D_v2 = [SingleElectron_Run2016D_PromptReco_v2, SingleMuon_Run2016D_PromptReco_v2]

### ----------------------------- Run2016E PromptReco v2 ----------------------------------------

SingleElectron_Run2016E_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016E_PromptReco_v2", "/SingleElectron/Run2016E-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016E_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016E_PromptReco_v2"    , "/SingleMuon/Run2016E-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016E_v2 = [SingleElectron_Run2016E_PromptReco_v2, SingleMuon_Run2016E_PromptReco_v2]


### ----------------------------- Run2016F PromptReco v1 ----------------------------------------

SingleElectron_Run2016F_PromptReco_v1 = kreator.makeDataComponent("SingleElectron_Run2016F_PromptReco_v1", "/SingleElectron/Run2016F-PromptReco-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016F_PromptReco_v1     = kreator.makeDataComponent("SingleMuon_Run2016F_PromptReco_v1"    , "/SingleMuon/Run2016F-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016F_v1 = [SingleElectron_Run2016F_PromptReco_v1, SingleMuon_Run2016F_PromptReco_v1]

### ----------------------------- Run2016G PromptReco v1 ----------------------------------------

SingleElectron_Run2016G_PromptReco_v1 = kreator.makeDataComponent("SingleElectron_Run2016G_PromptReco_v1", "/SingleElectron/Run2016G-PromptReco-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016G_PromptReco_v1     = kreator.makeDataComponent("SingleMuon_Run2016G_PromptReco_v1"    , "/SingleMuon/Run2016G-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016G_v1 = [SingleElectron_Run2016G_PromptReco_v1, SingleMuon_Run2016G_PromptReco_v1]

### ----------------------------- Run2016H PromptReco v1 ----------------------------------------

### Skipping this datasets since there were no stable beam collisions

### ----------------------------- Run2016H PromptReco v2 ----------------------------------------

SingleElectron_Run2016H_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016H_PromptReco_v2", "/SingleElectron/Run2016H-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016H_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016H_PromptReco_v2"    , "/SingleMuon/Run2016H-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016H_v2 = [SingleElectron_Run2016H_PromptReco_v2, SingleMuon_Run2016H_PromptReco_v2]

### ----------------------------- Run2016H PromptReco v3 ----------------------------------------

SingleElectron_Run2016H_PromptReco_v3 = kreator.makeDataComponent("SingleElectron_Run2016H_PromptReco_v3", "/SingleElectron/Run2016H-PromptReco-v3/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016H_PromptReco_v3     = kreator.makeDataComponent("SingleMuon_Run2016H_PromptReco_v3"    , "/SingleMuon/Run2016H-PromptReco-v3/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016H_v3 = [SingleElectron_Run2016H_PromptReco_v3, SingleMuon_Run2016H_PromptReco_v3]


### ----------------------------- summary of prompt reco ----------------------------------------
dataSamples_PromptReco = dataSamples_Run2016_v1 + dataSamples_Run2016B_v2 + dataSamples_Run2016C_v2 + dataSamples_Run2016D_v2 + dataSamples_Run2016E_v2 + dataSamples_Run2016F_v1 + dataSamples_Run2016G_v1 + dataSamples_Run2016H_v2 + dataSamples_Run2016H_v3


### ----------------------------- Run2016B 23Sep2016 ----------------------------------------

SingleElectron_Run2016B_23Sep2016 = kreator.makeDataComponent("SingleElectron_Run2016B_23Sep2016", "/SingleElectron/Run2016B-23Sep2016-v3/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016B_23Sep2016     = kreator.makeDataComponent("SingleMuon_Run2016B_23Sep2016"    , "/SingleMuon/Run2016B-23Sep2016-v3/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016B_23Sep2016 = [SingleElectron_Run2016B_23Sep2016, SingleMuon_Run2016B_23Sep2016]

### ----------------------------- Run2016C 23Sep2016 ----------------------------------------

SingleElectron_Run2016C_23Sep2016 = kreator.makeDataComponent("SingleElectron_Run2016C_23Sep2016", "/SingleElectron/Run2016C-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016C_23Sep2016     = kreator.makeDataComponent("SingleMuon_Run2016C_23Sep2016"    , "/SingleMuon/Run2016C-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016C_23Sep2016 = [SingleElectron_Run2016C_23Sep2016, SingleMuon_Run2016C_23Sep2016]


### ----------------------------- Run2016D 23Sep2016 v2 ----------------------------------------

SingleElectron_Run2016D_23Sep2016 = kreator.makeDataComponent("SingleElectron_Run2016D_23Sep2016", "/SingleElectron/Run2016D-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016D_23Sep2016     = kreator.makeDataComponent("SingleMuon_Run2016D_23Sep2016"    , "/SingleMuon/Run2016D-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016D_23Sep2016 = [SingleElectron_Run2016D_23Sep2016, SingleMuon_Run2016D_23Sep2016]

### ----------------------------- Run2016E 23Sep2016 v2 ----------------------------------------

SingleElectron_Run2016E_23Sep2016 = kreator.makeDataComponent("SingleElectron_Run2016E_23Sep2016", "/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016E_23Sep2016     = kreator.makeDataComponent("SingleMuon_Run2016E_23Sep2016"    , "/SingleMuon/Run2016E-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016E_23Sep2016 = [SingleElectron_Run2016E_23Sep2016, SingleMuon_Run2016E_23Sep2016]


### ----------------------------- Run2016F 23Sep2016 v1 ----------------------------------------

SingleElectron_Run2016F_23Sep2016 = kreator.makeDataComponent("SingleElectron_Run2016F_23Sep2016", "/SingleElectron/Run2016F-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016F_23Sep2016     = kreator.makeDataComponent("SingleMuon_Run2016F_23Sep2016"    , "/SingleMuon/Run2016F-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016F_23Sep2016 = [SingleElectron_Run2016F_23Sep2016, SingleMuon_Run2016F_23Sep2016]

### ----------------------------- Run2016G 23Sep2016 v1 ----------------------------------------

SingleElectron_Run2016G_23Sep2016 = kreator.makeDataComponent("SingleElectron_Run2016G_23Sep2016", "/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016G_23Sep2016     = kreator.makeDataComponent("SingleMuon_Run2016G_23Sep2016"    , "/SingleMuon/Run2016G-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016G_23Sep2016 = [SingleElectron_Run2016G_23Sep2016, SingleMuon_Run2016G_23Sep2016]
samples = dataSamples_PromptReco

### Summary of prompt reco
dataSamples_23Sep2016 = dataSamples_Run2016B_23Sep2016 + dataSamples_Run2016C_23Sep2016 + dataSamples_Run2016D_23Sep2016 + dataSamples_Run2016E_23Sep2016 + dataSamples_Run2016F_23Sep2016 + dataSamples_Run2016G_23Sep2016

### Dataset corresponding to the full Run2016 with re-reco + prompt
dataSamples_23Sep2016PlusPrompt = dataSamples_23Sep2016 + dataSamples_Run2016H_v2 + dataSamples_Run2016H_v3

#dataSamples = dataSamples_PromptReco + dataSamples_23Sep2016
dataSamples = dataSamples_23Sep2016PlusPrompt
samples = dataSamples

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

for comp in samples:
    comp.splitFactor = 1000
    comp.isMC = False
    comp.isData = True

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples)
