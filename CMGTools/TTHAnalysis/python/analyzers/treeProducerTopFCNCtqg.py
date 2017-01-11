from CMGTools.TTHAnalysis.analyzers.treeProducerTopCore import *
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

topFCNCtqg_globalVariables = topCore_globalVariables + [


            ## ------- lheHT, needed for merging HT binned samples 
            NTupleVariable("lheHT", lambda ev : getattr(ev,"lheHT",-999), mcOnly=True, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer"),
            
            NTupleVariable("LHEweight_original", lambda ev: ev.LHE_originalWeight if hasattr(ev,'LHE_originalWeight') else 0, mcOnly=True, help="original LHE weight"),

            NTupleVariable("lheHTIncoming", lambda ev : getattr(ev,"lheHTIncoming",-999), mcOnly=True, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer (only LHE status<0 as mothers)"),

            NTupleVariable("lheNj", lambda ev : getattr(ev,"lheNj",-999), mcOnly=True, help="Number of generated jets taken from Heppy LHEAnalyzer"),

            NTupleVariable("lheNb", lambda ev : getattr(ev,"lheNb",-999), mcOnly=True, help="Number of generated b-quarks taken from Heppy LHEAnalyzer"),
 
            NTupleVariable("lheNl", lambda ev : getattr(ev,"lheNl",-999), mcOnly=True, help="Number of generated leptons taken from Heppy LHEAnalyzer"),


            ##-------- custom jets ------------------------------------------
            
            NTupleVariable("nJet20", lambda ev: sum([j.pt() > 20 for j in ev.cleanJets]), int, help="Number of jets with pt > 20, |eta|<2.4"),
            NTupleVariable("nJet20a", lambda ev: sum([j.pt() > 20 for j in ev.cleanJetsAll]), int, help="Number of jets with pt > 20, |eta|<4.7"),


            NTupleVariable("htJet25", lambda ev : ev.htJet25, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 25 GeV)"),
            NTupleVariable("htJet25j", lambda ev : ev.htJet25j, help="H_{T} computed from only jets (with |eta|<2.4, pt > 25 GeV)"),
     #       NTupleVariable("htJet25ja", lambda ev : ev.htJet25ja, help="H_{T} computed from only jets (with |eta|<4.7, pt > 25 GeV)"),
            NTupleVariable("htJet25a", lambda ev : ev.htJet25a, help="H_{T} computed from leptons and jets (with |eta|<4.7, pt > 25 GeV)"),
            ##
            NTupleVariable("nJet25NoTau", lambda ev: sum([ (j.pt() > 25 and not j.taus ) for j in ev.cleanJets]), int, help="Number of jets with pt > 25, not matched with taus"),
    

            NTupleVariable("nBJetLoose20NoTau", lambda ev: sum([(j.btagWP("CSVv2IVFL") and not j.taus) for j in ev.cleanJets if j.pt()>20]), int, help="Number of jets with pt > 20 passing CSV loose, not matched with taus"),

           NTupleVariable("nBJetLoose20", lambda ev: sum([(j.btagWP("CSVv2IVFL") ) for j in ev.cleanJets if j.pt()>20]), int, help="Number of jets with pt > 20 passing CSV loose"),

            NTupleVariable("nBJetMedium20NoTau", lambda ev: sum([(j.btagWP("CSVv2IVFM") and not j.taus) for j in ev.cleanJets if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV medium, not matched with taus"),

            NTupleVariable("nBJetMedium20", lambda ev: sum([(j.btagWP("CSVv2IVFM")) for j in ev.cleanJets if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV medium"),

            NTupleVariable("nBJetCMVALoose20", lambda ev: sum([j.btagWP("CMVAL") for j in ev.cleanJets if j.pt() > 20] ), int, help="Number of jets with pt > 20 passing CMVA Loose"),
            NTupleVariable("nBJetCMVAMedium20", lambda ev: sum([j.btagWP("CMVAM") for j in ev.cleanJets if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CMVA Medium"),
            NTupleVariable("nBJetCMVATight20", lambda ev: sum([j.btagWP("CMVAT") for j in ev.cleanJets if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CMVA Tight"),
            ##

            NTupleVariable("nMuons10", lambda ev: sum([l.pt() > 10 and abs(l.pdgId()) == 13 for l in ev.selectedLeptons]), int, help="Number of muons with pt > 10"),

            NTupleVariable("nElectrons10", lambda ev: sum([l.pt() > 10 and abs(l.pdgId()) == 11 for l in ev.selectedLeptons]), int, help="Number of electrons with pt > 10"),

            NTupleVariable("nTaus10", lambda ev: sum([l.pt() > 10 for l in ev.selectedTaus]), int, help="Number of taus with pt > 10"),


            ##--------------------------------------------------            

]


leptonTypeFCNC = NTupleObjectType("leptonFCNC", baseObjectTypes = [ leptonType, leptonTypeExtra ], variables = [
            NTupleVariable("eleCutIdSpring16_25ns_v1_ConvVeto",     lambda x : (1*x.electronID("POG_Cuts_ID_SPRING16_25ns_v1_ConvVeto_Veto") + 1*x.electronID("POG_Cuts_ID_SPRING16_25ns_v1_ConvVeto_Loose") + 1*x.electronID("POG_Cuts_ID_SPRING16_25ns_v1_ConvVeto_Medium") + 1*x.electronID("POG_Cuts_ID_SPRING16_25ns_v1_ConvVeto_Tight")) if abs(x.pdgId()) == 11 and x.isElectronIDAvailable("POG_Cuts_ID_SPRING16_25ns_v1_ConvVeto_Veto") else -1, int, help="Electron cut-based id (POG Spring16_25ns_v1): 0=none, 1=veto, 2=loose, 3=medium, 4=tight"),
            NTupleVariable("e5x5", lambda x: x.e5x5() if (abs(x.pdgId())==11 and hasattr(x,"e5x5")) else -999, help="Electron e5x5"),
            NTupleVariable("r9", lambda x: x.r9() if (abs(x.pdgId())==11 and hasattr(x,"r9")) else -999, help="Electron r9"),
            NTupleVariable("sigmaIetaIeta", lambda x: x.sigmaIetaIeta() if (abs(x.pdgId())==11 and hasattr(x,"sigmaIetaIeta")) else -999, help="Electron sigmaIetaIeta"),
            NTupleVariable("sigmaIphiIphi", lambda x: x.sigmaIphiIphi() if (abs(x.pdgId())==11 and hasattr(x,"sigmaIphiIphi")) else -999, help="Electron sigmaIphiIphi"),
            NTupleVariable("hcalOverEcal", lambda x: x.hcalOverEcal() if (abs(x.pdgId())==11 and hasattr(x,"hcalOverEcal")) else -999, help="Electron hcalOverEcal"),
            NTupleVariable("full5x5_e5x5", lambda x: x.full5x5_e5x5() if (abs(x.pdgId())==11 and hasattr(x,"full5x5_e5x5")) else -999, help="Electron full5x5_e5x5"),
            NTupleVariable("full5x5_r9", lambda x: x.full5x5_r9() if (abs(x.pdgId())==11 and hasattr(x,"full5x5_r9")) else -999, help="Electron full5x5_r9"),
            NTupleVariable("full5x5_sigmaIetaIeta", lambda x: x.full5x5_sigmaIetaIeta() if (abs(x.pdgId())==11 and hasattr(x,"full5x5_sigmaIetaIeta")) else -999, help="Electron full5x5_sigmaIetaIeta"), 
            NTupleVariable("full5x5_sigmaIphiIphi", lambda x: x.full5x5_sigmaIphiIphi() if (abs(x.pdgId())==11 and hasattr(x,"full5x5_sigmaIphiIphi")) else -999, help="Electron full5x5_sigmaIphiIphi"), 
            NTupleVariable("full5x5_hcalOverEcal", lambda x: x.full5x5_hcalOverEcal() if (abs(x.pdgId())==11 and hasattr(x,"full5x5_hcalOverEcal")) else -999, help="Electron full5x5_hcalOverEcal"),
            NTupleVariable("correctedEcalEnergy", lambda x: x.correctedEcalEnergy() if (abs(x.pdgId())==11 and hasattr(x,"correctedEcalEnergy")) else -999, help="Electron correctedEcalEnergy"),
            NTupleVariable("eSuperClusterOverP", lambda x: x.eSuperClusterOverP() if (abs(x.pdgId())==11 and hasattr(x,"eSuperClusterOverP")) else -999, help="Electron eSuperClusterOverP"),
            NTupleVariable("ecalEnergy", lambda x: x.ecalEnergy() if (abs(x.pdgId())==11 and hasattr(x,"ecalEnergy")) else -999, help="Electron ecalEnergy"),
            NTupleVariable("superCluster_rawEnergy", lambda x: x.superCluster().rawEnergy() if (abs(x.pdgId())==11 and hasattr(x,"superCluster")) else -999, help="Electron superCluster.rawEnergy"),
            NTupleVariable("superCluster_preshowerEnergy", lambda x: x.superCluster().preshowerEnergy() if (abs(x.pdgId())==11 and hasattr(x,"superCluster")) else -999, help="Electron superCluster.preshowerEnergy"),
            NTupleVariable("superCluster_correctedEnergy", lambda x: x.superCluster().correctedEnergy() if (abs(x.pdgId())==11 and hasattr(x,"superCluster")) else -999, help="Electron superCluster.correctedEnergy"),
            NTupleVariable("superCluster_energy", lambda x: x.superCluster().energy() if (abs(x.pdgId())==11 and hasattr(x,"superCluster")) else -999, help="Electron superCluster.energy"),
            NTupleVariable("superCluster_clustersSize", lambda x: x.superCluster().clustersSize() if (abs(x.pdgId())==11 and hasattr(x,"superCluster")) else -999, help="Electron superCluster.clustersSize"),
            NTupleVariable("superCluster_seed.energy", lambda x: x.superCluster().seed().energy() if (abs(x.pdgId())==11 and hasattr(x,"superCluster")) else -999, help="Electron superCluster.seed.energy"),

])


topFCNCtqg_globalObjects = topCore_globalObjects.copy()
topFCNCtqg_globalObjects.update({
            # put more here
})

topFCNCtqg_collections = topCore_collections.copy()
topFCNCtqg_collections.update({
            # put more here
            "selectedTaus"    : NTupleCollection("TauGood",  tauType, 50, help="Taus after the preselection"),
            "selectedLeptons" : NTupleCollection("LepGood",  leptonTypeFCNC, 50, help="Leptons after the preselection"),
            "cleanJets"       : NTupleCollection("CleanJet",     jetTypeSusyExtra, 100, help="Cental jets after full selection and cleaning, sorted by pt"),

            "cleanJetsAll" : NTupleCollection("CleanJetAll", jetTypeSusyExtra, 25, help="Cental jets after full selection and cleaning, sorted by pt"),
            ##------------------------------------------------
            #"discardedJets"    : NTupleCollection("DiscJet", jetTypeSusyExtraLight, 15, help="Jets discarted in the jet-lepton cleaning"),
            #"discardedLeptons" : NTupleCollection("DiscLep", leptonTypeSusy, 8, help="Leptons discarded in the jet-lepton cleaning"),
            ##------------------------------------------------
            "LHE_weights"    : NTupleCollection("LHEweight",  weightsInfoType, 1000, mcOnly=True, help="LHE weight info"),


})
