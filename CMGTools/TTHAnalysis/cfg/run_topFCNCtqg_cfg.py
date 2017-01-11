##########################################################
## CONFIGURATION FOR TOP QUARK TREES                    ##
## skim condition: >= 1 loose leptons                   ##
## Author: M. Naseri mohsen.naseri@cern.ch              ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg
import re


#-------- LOAD ALL ANALYZERS -----------

from CMGTools.TTHAnalysis.analyzers.topCore_modules_cff import *
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
from CMGTools.RootTools.samples.autoAAAconfig import *


#-------- SET OPTIONS AND REDEFINE CONFIGURATIONS -----------

is50ns = getHeppyOption("is50ns",False)
analysis = getHeppyOption("analysis","topFCNCtqg")
runData = getHeppyOption("runData",True)
scaleProdToLumi = float(getHeppyOption("scaleProdToLumi",-1)) # produce rough equivalent of X /pb for MC datasets
removeJetReCalibration = getHeppyOption("removeJetReCalibration",False)
removeJecUncertainty = getHeppyOption("removeJecUncertainty",False)
doMETpreprocessor = getHeppyOption("doMETpreprocessor",False)
skipT1METCorr = getHeppyOption("skipT1METCorr",False)

forcedSplitFactor = getHeppyOption("splitFactor",-1)
forcedFineSplitFactor = getHeppyOption("fineSplitFactor",-1)
isTest = getHeppyOption("test",None) != None and not re.match("^\d+$",getHeppyOption("test"))
selectedEvents=getHeppyOption("selectEvents","")
#isTest = getHeppyOption("isTest",False)

sample = "main"

if analysis not in ['topFCNCtqg','topWpol']: raise RuntimeError, 'Analysis type unknown'
print 'Using analysis type: %s'%analysis

jsonAna.useLumiBlocks = True

# Lepton Skimming
ttHLepSkim.minLeptons = 1
ttHLepSkim.maxLeptons = 999
ttHLepSkim.ptCuts=[5]

# Run miniIso
lepAna.doMiniIsolation = True
lepAna.packedCandidates = 'packedPFCandidates'
lepAna.miniIsolationPUCorr = 'rhoArea'
lepAna.miniIsolationVetoLeptons = None # use 'inclusive' to veto inclusive leptons and their footprint in all isolation cones
lepAna.doIsolationScan = False


jetAna.copyJetsByValue = True # do not remove this
metAna.copyMETsByValue = True # do not remove this

##------------------------------------------
## ISOLATED TRACK
##------------------------------------------
isoTrackAna.setOff=False
isoTrackAna.doRelIsolation = True
##------------------------------------------
##------------------------------------------


# store all taus by default
#genAna.allGenTaus = True

if analysis=='topWpol':
    jetAna.cleanJetsFromLeptons=False
    jetAna.cleanSelectedLeptons=True
    jetAna.storeLowPtJets=True
    jetAna.jetEtaCentral = jetAna.jetEta
    jetAna.mcGT="Spring16_25nsV8_MC"    
    jetAna.dataGT   = "Spring16_25nsV8BCD_DATA Spring16_25nsV8E_DATA Spring16_25nsV8F_DATA Spring16_25nsV8_DATA"
    jetAna.runsDataJEC   = [276811, 277420, 278802]

if not removeJecUncertainty:
    jetAna.addJECShifts = True
    jetAnaScaleDown.copyJetsByValue = True # do not remove this
    metAnaScaleDown.copyMETsByValue = True # do not remove this
    jetAnaScaleUp.copyJetsByValue = True # do not remove this
    metAnaScaleUp.copyMETsByValue = True # do not remove this
    topCoreSequence.insert(topCoreSequence.index(jetAna)+1, jetAnaScaleDown)
    topCoreSequence.insert(topCoreSequence.index(jetAna)+1, jetAnaScaleUp)
    topCoreSequence.insert(topCoreSequence.index(metAna)+1, metAnaScaleDown)
    topCoreSequence.insert(topCoreSequence.index(metAna)+1, metAnaScaleUp)


if analysis in ['topFCNCtqg']:
## -- top FCNC tqg preselection settings ---

    # Lepton Skimming
    ttHLepSkim.minLeptons = 1
    ttHLepSkim.maxLeptons = 999
    
#    # Jet-Met Skimming
    topAnalysisSkim.jetPtCuts = [10]
    topAnalysisSkim.metCut    = 10
    topCoreSequence.append(topAnalysisSkim)

    # Lepton Preselection
    isolation = "relIso03"
    # Muons

    lepAna.inclusive_muon_pt  = 3
    lepAna.loose_muon_pt  = 3
    lepAna.mu_isoCorr = "deltaBeta"
    lepAna.mu_effectiveAreas = 'Spring15_25ns_v1' #new default
    lepAna.rhoMuon= 'fixedGridRhoFastjetCentralNeutral', #new default
    lepAna.mu_tightId = "POG_ID_Tight" 
    lepAna.loose_muon_id     = "POG_ID_Loose"
    lepAna.loose_muon_dxy = 0.2
    lepAna.loose_muon_dz = 0.5
    lepAna.loose_muon_relIso = 99.
    lepAna.loose_muon_pt = 10.
    lepAna.loose_muon_isoCut = lambda muon :muon.miniRelIso < 0.2

    #Electrons

    lepAna.inclusive_electron_pt  = 5
    lepAna.loose_electron_pt  = 5
    lepAna.loose_electron_eta = 2.5
    lepAna.loose_electron_relIso = 99.
    
    lepAna.loose_electron_id = "POG_Cuts_ID_SPRING16_25ns_v1_ConvVetoDxyDz_Loose"
    lepAna.ele_isoCorr = "rhoArea"
    lepAna.ele_tightId = "Cuts_SPRING16_25ns_v1_ConvVetoDxyDz"
    lepAna.ele_effectiveAreas = 'Spring15_25ns_v1' #new default 
    lepAna.rhoElectron = 'fixedGridRhoFastjetCentralNeutral', #new default

    # Lepton-Jet Cleaning
    #jetAna.minLepPt = 20 
    #jetAnaScaleUp.minLepPt = 20 
    #jetAnaScaleDown.minLepPt = 20 
    # otherwise with only absIso cut at 10 GeV and no relIso we risk cleaning away good jets


#lepAna.doIsoAnnulus = True

if isolation == "miniIso": 
    if (analysis=="topFCNCtqg"):
        lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.4 and muon.sip3D() < 8
        lepAna.loose_electron_isoCut = lambda elec : elec.miniRelIso < 0.4 and elec.sip3D() < 8
    elif analysis=="topWpolar":
        lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.4
        lepAna.loose_electron_isoCut = lambda elec : elec.miniRelIso < 0.4
    else: raise RuntimeError,'analysis field is not correctly configured'
elif isolation == None:
    lepAna.loose_muon_isoCut     = lambda muon : True
    lepAna.loose_electron_isoCut = lambda elec : True
elif isolation == "absIso04":
    lepAna.loose_muon_isoCut     = lambda muon : muon.RelIsoMIV04*muon.pt() < 10 and muon.sip3D() < 8
    lepAna.loose_electron_isoCut = lambda elec : elec.RelIsoMIV04*elec.pt() < 10 and elec.sip3D() < 8
elif isolation == "relIso03":
    lepAna.loose_muon_isoCut     = lambda muon : muon.relIso03 < 1
    lepAna.loose_electron_isoCut = lambda electron : electron.relIso03 < 1  
else:   
    # nothing to do, will use normal relIso03
    pass

# Switch on slow QGL
jetAna.doQG = False
jetAnaScaleUp.doQG = True
jetAnaScaleDown.doQG = True
jetAna.relaxJetId = False
jetAna.doPuId = False
jetAna.jetEta = 4.7
jetAna.jetEtaCentral = 2.4
jetAna.jetPt = 10.

# Loose Tau configuration
tauAna.loose_ptMin = 20
tauAna.loose_etaMax = 2.5
tauAna.loose_decayModeID = "decayModeFinding"
tauAna.loose_tauID = "decayModeFinding"


#-------- ADDITIONAL ANALYZERS -----------


## Event Analyzer for susy multi-lepton (at the moment, it's the TTH one)

#from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
#ttHEventAna = cfg.Analyzer(
#    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
#    minJets25 = 0,
#    )


## JetTau analyzer, to be called (for the moment) once bjetsMedium are produced
#from CMGTools.TTHAnalysis.analyzers.ttHJetTauAnalyzer import ttHJetTauAnalyzer
#ttHJetTauAna = cfg.Analyzer(
#    ttHJetTauAnalyzer, name="ttHJetTauAnalyzer",
#    )

from CMGTools.TTHAnalysis.analyzers.treeProducerTopFCNCtqg import * 

# Spring16 electron MVA - follow instructions on pull request for correct area setup

#leptonTypeFCNC.addVariables([
#        NTupleVariable("mvaIdSpring16",   lambda lepton : lepton.mvaRun2("Spring16") if abs(lepton.pdgId()) == 11 else 1, help="EGamma POG MVA ID, Spring16; 1 for muons"),
#        ])

if lepAna.doIsolationScan:
    leptonTypeFCNC.addVariables([
            NTupleVariable("miniIsoR", lambda x: getattr(x,'miniIsoR',-999), help="miniIso cone size"),
            NTupleVariable("effArea", lambda x: getattr(x,'EffectiveArea03',-999), help="effective area used for PU subtraction"),
            NTupleVariable("rhoForEA", lambda x: getattr(x,'rho',-999), help="rho used for EA PU subtraction")
            ])

# for electron scale and resolution checks


if not removeJecUncertainty:
    topFCNCtqg_globalObjects.update({
            "met_jecUp" : NTupleObject("met_jecUp", metType, help="PF E_{T}^{miss}, after type 1 corrections (JEC plus 1sigma)"),
            "met_jecDown" : NTupleObject("met_jecDown", metType, help="PF E_{T}^{miss}, after type 1 corrections (JEC minus 1sigma)"),
            })
    topFCNCtqg_collections.update({
            "cleanJets_jecUp"       : NTupleCollection("Jet_jecUp",    jetTypeSusyExtra, 100, help="Cental(All) jets after full selection and cleaning, sorted by pt (JEC plus 1sigma)"),
            "cleanJets_jecDown"     : NTupleCollection("Jet_jecDown",  jetTypeSusyExtra, 100, help="Cental(All) jets after full selection and cleaning, sorted by pt (JEC minus 1sigma)"),
            })

## Tree Producer
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerTopFCNCtqg',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     defaultFloatType = 'F', # use Float_t for floating point
     PDFWeights = PDFWeights,
     globalVariables = topFCNCtqg_globalVariables,
     globalObjects = topFCNCtqg_globalObjects,
     collections = topFCNCtqg_collections,
)

# HBHE new filter
from CMGTools.TTHAnalysis.analyzers.hbheAnalyzer import hbheAnalyzer
hbheAna = cfg.Analyzer(
    hbheAnalyzer, name="hbheAnalyzer", IgnoreTS4TS5ifJetInLowBVRegion=False
    )

topCoreSequence.insert(topCoreSequence.index(ttHCoreEventAna),hbheAna)

treeProducer.globalVariables.append(NTupleVariable("hbheFilterNew50ns", lambda ev: ev.hbheFilterNew50ns, int, help="new HBHE filter for 50 ns"))
treeProducer.globalVariables.append(NTupleVariable("hbheFilterNew25ns", lambda ev: ev.hbheFilterNew25ns, int, help="new HBHE filter for 25 ns"))
treeProducer.globalVariables.append(NTupleVariable("hbheFilterIso", lambda ev: ev.hbheFilterIso, int, help="HBHE iso-based noise filter"))
treeProducer.globalVariables.append(NTupleVariable("Flag_badChargedHadronFilter", lambda ev: ev.badChargedHadron, help="bad charged hadron filter decision"))
treeProducer.globalVariables.append(NTupleVariable("Flag_badMuonFilter", lambda ev: ev.badMuon, help="bad muon filter decision"))

#additional MET quantities
metAna.doTkMet = True
treeProducer.globalVariables.append(NTupleVariable("met_trkPt", lambda ev : ev.tkMet.pt() if  hasattr(ev,'tkMet') else  0, help="tkmet p_{T}"))
treeProducer.globalVariables.append(NTupleVariable("met_trkPhi", lambda ev : ev.tkMet.phi() if  hasattr(ev,'tkMet') else  0, help="tkmet phi"))

print "Mohsen1"

if not skipT1METCorr:
    if doMETpreprocessor: 
        print "WARNING: you're running the MET preprocessor and also Type1 MET corrections. This is probably not intended."
    jetAna.calculateType1METCorrection = True
    metAna.recalibrate = "type1"
    jetAnaScaleUp.calculateType1METCorrection = True
    metAnaScaleUp.recalibrate = "type1"
    jetAnaScaleDown.calculateType1METCorrection = True
    metAnaScaleDown.recalibrate = "type1"

#-------- SAMPLES AND TRIGGERS -----------

from CMGTools.RootTools.samples.triggers_13TeV_DATA2016 import *
triggerFlagsAna.triggerBits = {
#    'DoubleMu' : triggers_mumu_iso,
#    'DoubleMuNoIso' : triggers_mumu_noniso + triggers_mu27tkmu8,
#    'DoubleEl' : triggers_ee + triggers_doubleele33 + triggers_doubleele33_MW,
#    'MuEG'     : triggers_mue + triggers_mu30ele30,
    'SingleMu' : triggers_1mu_iso + triggers_1mu_noniso,
    'SingleEl'     : triggers_1e,
}


triggerFlagsAna.unrollbits = True
triggerFlagsAna.saveIsUnprescaled = True
triggerFlagsAna.checkL1Prescale = True


from CMGTools.RootTools.samples.samplesforFCNCtqg_13TeV_RunIISpring16MiniAODv2 import *
from CMGTools.RootTools.samples.samplesforFCNCtqg_13TeV_DATA2016 import *

from CMGTools.HToZZ4L.tools.configTools import printSummary, configureSplittingFromTime, cropToLumi, prescaleComponents, insertEventSelector

selectedComponents = [TTLep_pow_ext]

if analysis=='topFCNCtqg':
     samples = TTs + SingleTop + VJets + DYJetsM50HT + DYJetsM5to50HT + WJetsToLNuHT + WNJets + QCDHT + QCDPtbcToE + QCDPt + QCDPtEMEnriched + [QCD_Mu15] + QCD_Mu5 +  DiBosons + TriBosons + TTV       
elif analysis=='topWpolar':
     selectedComponents = selectedComponents



if scaleProdToLumi>0: # select only a subset of a sample, corresponding to a given luminosity (assuming ~30k events per MiniAOD file, which is ok for central production)
    target_lumi = scaleProdToLumi # in inverse picobarns
    for c in selectedComponents:
        if not c.isMC: continue
        nfiles = int(min(ceil(target_lumi * c.xSection / 30e3), len(c.files)))
        #if nfiles < 50: nfiles = min(4*nfiles, len(c.files))
        print "For component %s, will want %d/%d files; AAA %s" % (c.name, nfiles, len(c.files), "eoscms" not in c.files[0])
        c.files = c.files[:nfiles]
        c.splitFactor = len(c.files)
        c.fineSplitFactor = 1


if runData and not isTest: # For running on data
    jsonFilter =True    
    is50ns = False
    dataChunks = []

#    json = os.environ['CMSSW_BASE']+'/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt' # 36.15/fb
    print json
    processing = "Run2016B-23Sep2016-v3"; short = "Run2016B_23Sep2016_v3"; run_ranges = [(273150,275376)]; useAAA=True; # -v3 starts from 273150 to 275376
    dataChunks.append((json,processing,short,run_ranges,useAAA))
    processing = "Run2016C-23Sep2016-v1"; short = "Run2016C_23Sep2016_v1"; run_ranges = [(271036,284044)]; useAAA=True;
  #  dataChunks.append((json,processing,short,run_ranges,useAAA))
    processing = "Run2016D-23Sep2016-v1"; short = "Run2016D_23Sep2016_v1"; run_ranges = [(271036,284044)]; useAAA=True;
    dataChunks.append((json,processing,short,run_ranges,useAAA))
    processing = "Run2016E-23Sep2016-v1"; short = "Run2016E_23Sep2016_v1"; run_ranges = [(271036,284044)]; useAAA=True;
    dataChunks.append((json,processing,short,run_ranges,useAAA))
#    processing = "Run2016F-23Sep2016-v1"; short = "Run2016F_23Sep2016_v1"; run_ranges = [(271036,284044)]; useAAA=True;
    dataChunks.append((json,processing,short,run_ranges,useAAA))
#    processing = "Run2016G-23Sep2016-v1"; short = "Run2016G_23Sep2016_v1"; run_ranges = [(271036,284044)]; useAAA=True;
    dataChunks.append((json,processing,short,run_ranges,useAAA))
  #run H ==============================================================================================================
    processing = "Run2016H-PromptReco-v1"; short = "Run2016H-PromptReco-v1"; run_ranges = [(281085,281201)]; useAAA=True;
    dataChunks.append((json,processing,short,run_ranges,useAAA))
    processing = "Run2016H-PromptReco-v2"; short = "Run2016H-PromptReco-v2"; run_ranges = [(281207,284035)]; useAAA=True;
    dataChunks.append((json,processing,short,run_ranges,useAAA))
    processing = "Run2016H-PromptReco-v3"; short = "Run2016H-PromptReco-v3"; run_ranges = [(284036,284044)]; useAAA=True;
    dataChunks.append((json,processing,short,run_ranges,useAAA))


    compSelection = ""; compVeto = ""
    DatasetsAndTriggers = []
    selectedComponents = [];
    exclusiveDatasets = True; # this will veto triggers from previous PDs in each PD, so that there are no duplicate events
 
    if analysis in ['topFCNCtqg']:
            DatasetsAndTriggers.append( ("SingleMuon", triggers_1mu_iso + triggers_1mu_noniso) )
            DatasetsAndTriggers.append( ("SingleElectron", triggers_1e) )


    for json,processing,short,run_ranges,useAAA in dataChunks:
        if len(run_ranges)==0: run_ranges=[None]
        vetos = []
        for pd,triggers in DatasetsAndTriggers:
            for run_range in run_ranges:
                print run_range
                label = ""
                if run_range!=None:
                    label = "_runs_%d_%d" % run_range if run_range[0] != run_range[1] else "run_%d" % (run_range[0],)
                    print label 
                compname = pd+"_"+short+label
                if ((compSelection and not re.search(compSelection, compname)) or
                    (compVeto      and     re.search(compVeto,      compname))):
                        print "Will skip %s" % (compname)
                        continue
                myprocessing = processing
                comp = kreator.makeDataComponent(compname, 
                                                 "/"+pd+"/"+myprocessing+"/MINIAOD", 
                                                 "CMS", ".*root", 
                                                 json=json, 
                                                 run_range=(run_range if "PromptReco" not in myprocessing else None), 
                                                 triggers=triggers[:], vetoTriggers = vetos[:],
                                                 useAAA=useAAA)
                if "PromptReco" in myprocessing:
                    from CMGTools.Production.promptRecoRunRangeFilter import filterComponent
                    filterComponent(comp, verbose=1)
                print "Will process %s (%d files)" % (comp.name, len(comp.files))
                comp.splitFactor = len(comp.files)/1
                comp.fineSplitFactor = 1
                selectedComponents.append( comp )
            if exclusiveDatasets: vetos += triggers
    if json is None:
        topCoreSequence.remove(jsonAna)

printSummary(selectedComponents)


if True and runData:
    from CMGTools.Production.promptRecoRunRangeFilter import filterComponent
    for c in selectedComponents:
        printnewsummary = False
        c.splitFactor = len(c.files)/1
        if "PromptReco" in c.name:
            printnewsummary = True
            filterComponent(c, 1)
            c.splitFactor = len(c.files)/1
    if printnewsummary: printSummary(selectedComponents)


if is50ns:
    # no change in MC GT since there's no 76X 50ns MC
    jetAna.dataGT   = "76X_dataRun2_v15_Run2015B_50ns"
    jetAnaScaleUp.dataGT   = "76X_dataRun2_v15_Run2015B_50ns"
    jetAnaScaleDown.dataGT   = "76X_dataRun2_v15_Run2015B_50ns"
else:
    jetAna.mcGT = "Spring16_25nsV6_MC"
    jetAna.dataGT = "Spring16_25nsV6_DATA"
    jetAnaScaleUp.dataGT = "Spring16_25nsV6_DATA"
    jetAnaScaleDown.dataGT = "Spring16_25nsV6_DATA"

if removeJetReCalibration:
    jetAna.recalibrateJets = False   # True for MC and false for data
    jetAnaScaleUp.recalibrateJets = False  # True for MC and false for data
    jetAnaScaleDown.recalibrateJets = False  # True for MC and false for data

if getHeppyOption("noLepSkim",False):
    if globalSkim in sequence:
        globalSkim.selection = []
    if ttHLepSkim in sequence:
        ttHLepSkim.minLeptons=0 

if forcedSplitFactor>0 or forcedFineSplitFactor>0:
    if forcedFineSplitFactor>0 and forcedSplitFactor!=1: raise RuntimeError, 'splitFactor must be 1 if setting fineSplitFactor'
    for c in selectedComponents:
        if forcedSplitFactor>0: c.splitFactor = forcedSplitFactor
        if forcedFineSplitFactor>0: c.fineSplitFactor = forcedFineSplitFactor


if selectedEvents!="":
    events=[ int(evt) for evt in selectedEvents.split(",") ]
    print "selecting only the following events : ", events
    eventSelector.toSelect = events
        

#-------- SEQUENCE -----------

sequence = cfg.Sequence(topCoreSequence+[
        #ttHJetTauAna,
        #ttHEventAna,
        #topAnalysisSkim,
        treeProducer,
    ])


preprocessor = None

#-------- HOW TO RUN -----------
print "Mohsen7"

test = getHeppyOption('test','3')
selectedComponents = [SingleElectron_Run2016C_23Sep2016]
print test


if test == '1':
    comp = selectedComponents[0]
    comp.files = comp.files[:1]
    comp.splitFactor = 1
    comp.fineSplitFactor = 1
    selectedComponents = [ comp ]
    print "Mohsen9"
elif test == '2':
    from CMGTools.Production.promptRecoRunRangeFilter import filterWithCollection
    for comp in selectedComponents:
        if comp.isData: comp.files = filterWithCollection(comp.files, [274315,275658,276363,276454])
        comp.files = comp.files[:1]
        comp.splitFactor = 1
        comp.fineSplitFactor = 1
elif test == '3':
    for comp in selectedComponents:
        comp.files = comp.files[:1]
        comp.splitFactor = 1
        comp.fineSplitFactor = 4
elif test == '5':
    for comp in selectedComponents:
        comp.files = comp.files[:5]
        comp.splitFactor = 1
        comp.fineSplitFactor = 5
elif test == "ewkinosync":
    comp = cfg.MCComponent( files = ["root://eoscms.cern.ch//store/mc/RunIIFall15MiniAODv2/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/14C51DB0-D6B8-E511-8D9B-8CDCD4A9A484.root"], name="TTW_EWK_sync" )
    comp.triggers = []
    comp.splitFactor = 1
    comp.fineSplitFactor = 1
    selectedComponents = [comp]
    sequence.remove(jsonAna)
elif test == '80X-MC':
    what = getHeppyOption("sample","TTLep")
    if what == "TTLep":
        TTLep_pow = kreator.makeMCComponent("TTLep_pow", "/TTTo2L2Nu_13TeV-powheg/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) )
        selectedComponents = [ TTLep_pow ]
        comp = selectedComponents[0]
        comp.triggers = []
        comp.files = [ '/store/mc/RunIISpring16MiniAODv1/TTTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/00000/002606A5-C909-E611-85DA-44A8423D7E31.root' ]
        tmpfil = os.path.expandvars("/tmp/$USER/002606A5-C909-E611-85DA-44A8423D7E31.root")
        if not os.path.exists(tmpfil):
            os.system("xrdcp root://eoscms//eos/cms%s %s" % (comp.files[0],tmpfil))
        comp.files = [ tmpfil ]
        if not getHeppyOption("single"): comp.fineSplitFactor = 4
    else: raise RuntimeError, "Unknown MC sample: %s" % what
elif test == '80X-Data':
    SingleMuon = kreator.makeDataComponent("SingleMuon_Run2016H_run281693","/SingleMuon/Run2016H-PromptReco-v2/MINIAOD","CMS",".*root", run_range=(281680, 281700), triggers = triggers_1mu_iso)
    SingleMuon.files = [ 'root://eoscms//eos/cms/store/data/Run2016B/DoubleMuon/MINIAOD/23Sep2016-v3/00000/5ADA8008-EE98-E611-A57D-848F69FD852B.root' ]
    selectedComponents = [ SingleMuon ] 
    for comp in selectedComponents:
        comp.json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-283685_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
        tmpfil = os.path.expandvars("/tmp/$USER/%s" % os.path.basename(comp.files[0]))
        if not os.path.exists(tmpfil): os.system("xrdcp %s %s" % (comp.files[0],tmpfil)) 
        comp.files = [tmpfil]
        comp.splitFactor = 1
        comp.fineSplitFactor = 1
elif test != None:
    raise RuntimeError, "Unknown test %r" % test

## Auto-AAA
from CMGTools.RootTools.samples.autoAAAconfig import *
if not getHeppyOption("isCrab"):
    autoAAA(selectedComponents)


## output histogram
outputService=[]
from PhysicsTools.HeppyCore.framework.services.tfile import TFileService
output_service = cfg.Service(
    TFileService,
    'outputfile',
    name="outputfile",
    fname='treeProducerTopFCNCtqg/tree.root',
    option='recreate'
    )    
outputService.append(output_service)

# print summary of components to process
printSummary(selectedComponents)

# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
event_class = EOSEventsWithDownload if not preprocessor else Events
print event_class
EOSEventsWithDownload.aggressive = 2 # always fetch if running on Wigner
if getHeppyOption("nofetch") or getHeppyOption("isCrab"):
    event_class = Events
    if preprocessor: preprocessor.prefetch = False
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [ ], 
                     preprocessor = preprocessor, 
                     events_class = event_class)
